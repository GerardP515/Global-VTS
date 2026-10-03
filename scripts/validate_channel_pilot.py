#!/usr/bin/env python3
"""Read-only checks for PILOT-01 only. Not a general guide or navigation validator.
Dependency for this pilot: PyYAML 6.0.2. No operational values are modified.
"""
from copy import deepcopy
from hashlib import sha256
from pathlib import Path
import json
import yaml

ROOT = Path(__file__).resolve().parents[1]
GUIDE = ROOT / 'research/vts/VTS-0001/dossier.md'
CAT = ROOT / 'research/vts/VTS-0001/source_catalogue.json'

class StrictLoader(yaml.SafeLoader):
    pass

def unique_keys(loader, node, deep=False):
    result = {}
    for key, value in node.value:
        key = loader.construct_object(key, deep=deep)
        if key in result:
            raise ValueError('Duplicate YAML key: ' + str(key))
        result[key] = loader.construct_object(value, deep=deep)
    return result

StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_keys)

def parse(text):
    if not text.startswith('---\n'):
        raise ValueError('Missing YAML front matter')
    return yaml.load(text.split('---\n', 2)[1], Loader=StrictLoader)

def validate(data, catalogue):
    ids = {}
    for group, key in [('reporting_objects', 'object_id'), ('communications', 'contact_id'),
                       ('report_types', 'report_type_id'), ('directions', 'direction_id'),
                       ('evidence', 'evidence_id'), ('gaps', 'gap_id'), ('conflicts', 'conflict_id')]:
        values = [row[key] for row in data[group]]
        assert values and all(values) and len(values) == len(set(values)), group
        ids[group] = set(values)
    assert data['vts_id'] == 'VTS-0001' and data['study_id'] == 'PILOT-01'
    assert data['research_state'] == 'HOLD' and data['project_class'] == 'Core'
    assert len(data['directions']) == 2
    sources = {row['source_id']: row for row in catalogue['records']}
    assert len(sources) == len(catalogue['records'])
    def walk(value):
        if isinstance(value, dict):
            for key, child in value.items():
                if key == 'evidence_ids':
                    assert set(child) <= ids['evidence'], 'Unresolved evidence ID'
                walk(child)
        elif isinstance(value, list):
            for child in value:
                walk(child)
    walk(data)
    missing = 0
    for row in data['evidence']:
        assert row['source_id'] in sources, 'Unresolved source'
        assert row['source_locator'], 'Missing locator'
        assert row['snapshot_id'] == sources[row['source_id']]['snapshot_id'], 'Wrong source binding'
        assert row['verification_state'] == 'AUTHOR_CHECKED', 'Unperformed independent review'
        missing += row['snapshot_id'] is None
    events = []
    for direction in data['directions']:
        rows = direction['reporting_events']
        assert [r['sequence'] for r in rows] == list(range(1, len(rows) + 1)), 'Sequence'
        for row in rows:
            events.append(row['event_id'])
            assert row['report_type_id'] in ids['report_types']
            assert row['contact_id'] is None or row['contact_id'] in ids['communications']
            assert row['reporting_object_id'] is None or row['reporting_object_id'] in ids['reporting_objects']
            assert row['evidence_ids'] and row['vessel_applicability']
        assert set(direction['spread']['reporting_event_ids']) == {r['event_id'] for r in rows}
        assert set(direction['spread']['reporting_object_ids']) <= ids['reporting_objects']
    assert len(events) == len(set(events)), 'Duplicate event'
    for report in data['report_types']:
        fields = report['fields']
        assert [f['sequence'] for f in fields] == list(range(1, len(fields) + 1))
        assert len(fields) == len({f['field_id'] for f in fields})
        assert all(f['evidence_ids'] for f in fields)
    expected = ['A', 'B', 'C or D', 'E', 'F', 'G', 'I', 'O', 'P', 'Q or R', 'T', 'W', 'X']
    assert [f['code_as_published'] for f in data['report_types'][0]['fields']] == expected
    for key in ['independent_review_record', 'marine_approval_record', 'artwork_check_record', 'release_record']:
        assert data['assurance'][key] is None, 'Unperformed approval'
    assert data['production']['pdf_output_paths'] == []
    assert missing and 'G01' in ids['gaps']
    assert all(r['datum_as_published'] is None for r in data['reporting_objects'])
    return {'directions': 2, 'events': len(events), 'report_code_groups': 13,
            'evidence_records': len(data['evidence']), 'live_only_evidence_records': missing,
            'gaps': len(data['gaps']), 'conflicts': len(data['conflicts'])}

def file_record(path):
    data = path.read_bytes()
    return {'path': path.relative_to(ROOT).as_posix(), 'bytes': len(data), 'sha256': sha256(data).hexdigest()}

def main():
    data = parse(GUIDE.read_text(encoding='utf-8'))
    catalogue = json.loads(CAT.read_text(encoding='utf-8'))
    result = validate(data, catalogue)
    files = [file_record(GUIDE), file_record(CAT)]
    held = []
    for source in catalogue['records']:
        if source['source_status'] != 'HELD':
            continue
        original = file_record(ROOT / source['original_path'])
        text = file_record(ROOT / source['text_path'])
        assert original['sha256'] == source['original_sha256']
        assert original['bytes'] == source['original_bytes']
        assert text['sha256'] == source['text_sha256']
        held.append(source['source_id'])
        files.extend([original, text])
    assert len(held) == 2
    tests = []
    try:
        parse('---\nx: 1\nx: 2\n---\n')
    except ValueError:
        tests.append('duplicate YAML key rejected')
    else:
        raise AssertionError('Duplicate keys accepted')
    mutations = [
        ('invalid evidence', lambda d: d['directions'][0]['reporting_events'][0]['evidence_ids'].append('BOGUS')),
        ('duplicate event', lambda d: d['directions'][1]['reporting_events'][0].update(event_id='NE-ENTRY')),
        ('wrong sequence', lambda d: d['directions'][0]['reporting_events'][0].update(sequence=2)),
        ('wrong snapshot binding', lambda d: d['evidence'][0].update(snapshot_id='FAKE')),
        ('unperformed approval', lambda d: d['assurance'].update(marine_approval_record='APPROVED')),
        ('old field list', lambda d: d['report_types'][0]['fields'][0].update(code_as_published='L')),
        ('empty direction pack', lambda d: d.update(directions=[])),
    ]
    for name, mutate in mutations:
        trial = deepcopy(data)
        mutate(trial)
        try:
            validate(trial, catalogue)
        except AssertionError:
            tests.append(name + ' rejected')
        else:
            raise AssertionError('Fault not detected: ' + name)
    result.update(structural_result='PASS_WITH_DECLARED_LIMITATIONS', publication_ready=False,
                  independent_review_performed=False, held_sources=held, negative_tests=tests,
                  checked_files=files,
                  limitations=['Pilot-specific checks only; not the complete guide schema',
                               'Five consulted sources remain outside the retained packet',
                               'Source meaning, current notices and marine approval are not certified'])
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
