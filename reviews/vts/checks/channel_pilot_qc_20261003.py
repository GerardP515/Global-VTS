#!/usr/bin/env python3
"""Review-only structural probes. Never modify source, dossier or approval records.

The original pilot validator is rerun unchanged. Mutations exist in memory only.
Acceptance of a defective mutation is a recorded coverage gap, not a safe result.
This is author-side follow-up QA, not independent marine verification.
"""
from copy import deepcopy
from hashlib import sha256
from pathlib import Path
import contextlib
import importlib.util
import io
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
TARGET = 'c5fde2d0114b3dcec06e4a013c60a9241d1d553c'
EXPECTED_GUIDE = 'c9cb6c3cb07f8856a3cede312894454eded7aa2d24ff04d9a6e1dbbf847f9ecf'
GUIDE = ROOT / 'research/vts/VTS-0001/dossier.md'


def main():
    if sha256(GUIDE.read_bytes()).hexdigest() != EXPECTED_GUIDE:
        raise ValueError('Dossier changed: these checks apply only to the frozen pilot')
    spec = importlib.util.spec_from_file_location('pilot_validator', ROOT / 'scripts/validate_channel_pilot.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        module.main()
    baseline = json.loads(out.getvalue())
    data = module.parse(GUIDE.read_text(encoding='utf-8'))
    catalogue = json.loads(module.CAT.read_text(encoding='utf-8'))
    packet = json.loads((GUIDE.parent / 'packet.json').read_text(encoding='utf-8'))
    packet_checks = []
    for item in packet['files']:
        path = (ROOT / item['path']).resolve()
        if not path.is_relative_to(ROOT):
            raise ValueError('Packet path leaves repository')
        body = path.read_bytes()
        valid = len(body) == item['bytes'] and sha256(body).hexdigest() == item['sha256']
        packet_checks.append({'path': item['path'], 'matches_packet': valid})
        if not valid:
            raise ValueError('Packet mismatch: ' + item['path'])
    probes = [
        ('invalid_requirement_strength', lambda d: d['directions'][0]['reporting_events'][0].update(requirement_strength='MISSPELLED_ENUM')),
        ('mandatory_entry_without_recipient', lambda d: d['directions'][0]['reporting_events'][0].update(contact_id=None)),
        ('communications_without_evidence', lambda d: d['communications'][0].update(evidence_ids=[])),
        ('unresolvable_supported_field_path', lambda d: d['evidence'][0].update(supported_field_paths=['guide_area.NONEXISTENT_FIELD'])),
        ('spread_omits_entry_geometry', lambda d: d['directions'][0]['spread'].update(reporting_object_ids=[])),
        ('duplicate_spread_identity', lambda d: d['directions'][1]['spread'].update(spread_id=d['directions'][0]['spread']['spread_id'])),
        ('invalid_geometry_type', lambda d: d['reporting_objects'][0].update(geometry_type='INVALID_GEOMETRY')),
    ]
    results = []
    for name, mutate in probes:
        trial = deepcopy(data)
        mutate(trial)
        try:
            module.validate(trial, catalogue)
        except (AssertionError, ValueError, KeyError, TypeError) as exc:
            results.append({'probe': name, 'original_validator_rejected': True, 'error_type': type(exc).__name__})
        else:
            results.append({'probe': name, 'original_validator_rejected': False, 'finding': 'VALIDATOR_COVERAGE_GAP'})
    records = data['evidence']
    report = {
        'target_research_commit': TARGET,
        'executed_checkout': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
        'dossier_unchanged': True,
        'baseline_result': baseline['structural_result'],
        'baseline_negative_tests': baseline['negative_tests'],
        'population': {k: baseline[k] for k in ['directions', 'events', 'report_code_groups', 'evidence_records', 'live_only_evidence_records', 'gaps', 'conflicts']},
        'held_source_ids': baseline['held_sources'],
        'packet_file_checks': packet_checks,
        'additional_structural_probes': results,
        'undetected_structural_defects': sum(not r['original_validator_rejected'] for r in results),
        'source_binding': [{'evidence_id': r['evidence_id'], 'source_id': r['source_id'], 'retained_snapshot': r['snapshot_id'] is not None} for r in records],
        'qa_disposition': 'FINDINGS_RECORDED_RETAIN_HOLD',
        'independent_review_performed': False,
        'publication_ready': False,
        'limitations': ['These tests do not assess source meaning or current operational instructions', 'Five consulted original sources are absent from the frozen packet', 'No dossier or source was changed', 'The existing validator is pilot-specific, not a complete guide-schema validator']
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0

if __name__ == '__main__':
    sys.exit(main())
