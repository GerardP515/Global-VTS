#!/usr/bin/env python3
"""Read-only draft-integrity checks for Channel pilot 0.2.x, not a general VTS schema.
A structural pass cannot certify source meaning or authorise publication.
The legacy validator and the original review inputs remain reproducible in Git.
"""
from __future__ import annotations
import argparse
from copy import deepcopy
from datetime import datetime, timezone
from hashlib import sha256
import json
import math
from pathlib import Path
import re
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
KEYS = {'reporting_objects':'object_id', 'communications':'contact_id',
        'report_types':'report_type_id', 'directions':'direction_id',
        'reporting_events':'event_id', 'fields':'field_id', 'subitems':'subitem_id',
        'timing_conditions':'condition_id', 'evidence':'evidence_id', 'gaps':'gap_id',
        'conflicts':'conflict_id', 'report_delivery_options':'option_id',
        'scope_exclusions':'exclusion_id'}
ENUMS = {
    'requirement_strength': {'MANDATORY','VOLUNTARY','RECOMMENDED','ON_REQUEST','INFORMATION','UNKNOWN'},
    'geometry_type': {'POINT','LINE','AREA','BEARING_DISTANCE','VERBAL','UNKNOWN'},
    'verification_state': {'UNCHECKED','AUTHOR_CHECKED','INDEPENDENTLY_CHECKED','CONFLICT','NOT_CHECKED'},
    'event_mode': {'ENTRY','CONDITIONAL'},
    'condition_mode': {'CONDITIONAL','NO_ADDITIONAL_CONDITION'},
}
EXPECTED_CODES = ['A','B','C or D','E','F','G','I','O','P','Q or R','T','W','X']

class Invalid(ValueError):
    pass

def require(test, message):
    if not test:
        raise Invalid(message)

class StrictLoader(yaml.SafeLoader):
    pass

def unique_mapping(loader, node, deep=False):
    loader.flatten_mapping(node)
    result = {}
    for k, v in node.value:
        key = loader.construct_object(k, deep=deep)
        require(isinstance(key, str), 'YAML mapping keys must be strings')
        require(key not in result, 'Duplicate YAML key: ' + key)
        result[key] = loader.construct_object(v, deep=deep)
    return result

StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)

def parse(text):
    match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)', text, re.S)
    require(match is not None, 'Missing or malformed YAML front matter')
    result = yaml.load(match.group(1), Loader=StrictLoader)
    require(isinstance(result, dict), 'Guide must contain a mapping')
    return result

def resolve(data, selector):
    """Resolve stable-ID selectors, never interpret numeric indices as identifiers."""
    require(isinstance(selector, str) and selector, 'Missing field selector')
    nodes = [data]
    for part in selector.split('.'):
        match = re.fullmatch(r'([A-Za-z_][A-Za-z_0-9]*)(?:\[([^\]]+)\])?', part)
        require(match is not None, 'Invalid field selector: ' + selector)
        name, ident = match.groups()
        following = []
        for node in nodes:
            require(isinstance(node, dict) and name in node, 'Unresolvable selector: ' + selector)
            value = node[name]
            if ident is None:
                following.append(value)
            else:
                require(isinstance(value, list) and name in KEYS, 'Unknown collection: ' + selector)
                matches = value if ident == '*' else [x for x in value if isinstance(x, dict) and x.get(KEYS[name]) == ident]
                require(bool(matches), 'Unresolvable selector: ' + selector)
                if ident != '*':
                    require(len(matches) == 1, 'Ambiguous selector: ' + selector)
                following.extend(matches)
        nodes = following
    return nodes

def index(rows, key, name, nonempty=True):
    require(isinstance(rows, list), name + ' must be a list')
    require(bool(rows) or not nonempty, name + ' cannot be empty')
    out = {}
    for row in rows:
        require(isinstance(row, dict), name + ' record must be a mapping')
        ident = row.get(key)
        require(isinstance(ident, str) and bool(ident), name + ' identifier missing')
        require(ident not in out, 'Duplicate ' + name + ': ' + ident)
        out[ident] = row
    return out

def validate(data, catalogue):
    require(data.get('vts_id') == 'VTS-0001' and data.get('study_id') == 'PILOT-01', 'Wrong pilot')
    require(data.get('schema_version') == '1.0-draft+channel.1', 'Unsupported pilot schema')
    require(data.get('project_class') == 'Core', 'Inventory class must remain unchanged')
    require(data.get('research_state') in {'DRAFT','HOLD','READY_FOR_REVIEW'}, 'Unsupported research state')
    groups = {name:index(data.get(name), key, name, name not in {'gaps','conflicts','scope_exclusions'})
              for name,key in KEYS.items() if name in data}
    for name in ['reporting_objects','communications','report_types','directions','evidence','gaps','conflicts','report_delivery_options']:
        require(name in groups, 'Missing collection ' + name)
    sources = index(catalogue.get('records'), 'source_id', 'sources')
    evidence = groups['evidence']; gaps = groups['gaps']

    def references(record, name, collection, nonempty=False):
        ids = record.get(name, [])
        require(isinstance(ids, list), name + ' must be a list')
        require(bool(ids) or not nonempty, 'Missing ' + name)
        require(all(isinstance(i,str) and i in collection for i in ids), 'Unresolved ' + name)
        require(len(ids) == len(set(ids)), 'Duplicate ' + name)
        return ids

    def walk(value):
        if isinstance(value, dict):
            for key, child in value.items():
                if key == 'sequence':
                    require(type(child) is int and child > 0, 'Sequence must be a positive integer, not a Boolean')
                if key in ENUMS:
                    require(isinstance(child,str) and child in ENUMS[key], 'Invalid ' + key)
                if key in {'calling_channel','working_channel'}:
                    require(child is None or isinstance(child,str), 'Channel representation must be a string')
                if key == 'evidence_ids': references(value, key, evidence)
                if key == 'gap_ids': references(value, key, gaps)
                walk(child)
        elif isinstance(value,list):
            for child in value: walk(child)
    walk(data)
    for row in evidence.values():
        require(row.get('source_id') in sources, 'Unresolved source ID')
        source = sources[row['source_id']]
        require(row.get('source_locator'), 'Missing source locator')
        require(row.get('snapshot_id') == source.get('snapshot_id'), 'Wrong source/snapshot binding')
        paths = row.get('supported_field_paths')
        require(isinstance(paths,list) and bool(paths), 'Missing evidence target')
        for path in paths: resolve(data,path)
        require(row['verification_state'] != 'INDEPENDENTLY_CHECKED', 'No independent evidence review recorded in this revision')
    for gap in gaps.values():
        require(gap.get('missing_information') and gap.get('next_action'), 'Gap lacks description or action')
        for path in gap.get('affected_field_paths',[]): resolve(data,path)
        references(gap,'resolution_evidence_ids',evidence)
    for conflict in groups['conflicts'].values():
        for path in conflict.get('affected_fields',[]): resolve(data,path)
        for assertion in conflict.get('assertions',[]):
            require(assertion.get('source_id') in sources, 'Unresolved conflict source')

    def documented_gap(record, selector):
        for gid in record.get('gap_ids',[]):
            gap = gaps[gid]
            if gap.get('disposition') != 'OPEN': continue
            for path in gap.get('affected_field_paths',[]):
                # Explicit event/field ancestor, not a generic unrelated gap.
                if path == selector or selector.startswith(path + '.'):
                    return True
        return False

    for obj in groups['reporting_objects'].values():
        references(obj,'evidence_ids',evidence,True)
        require(obj.get('geometry_as_published'), 'Missing published geometry description')
    for contact in groups['communications'].values():
        references(contact,'evidence_ids',evidence,True)
        require(contact.get('recipient'), 'Communications recipient missing')
        references(contact,'delivery_option_ids',groups['report_delivery_options'])
        base = 'communications[' + contact['contact_id'] + ']'
        for key in ['communication_method','call_sign']:
            require(contact.get(key) or documented_gap(contact,base+'.'+key), 'Missing contact detail without scoped gap: '+base+'.'+key)
    for option in groups['report_delivery_options'].values():
        require(option.get('report_type_id') in groups['report_types'], 'Unknown delivery report type')
        require(option.get('subject_scope'), 'Unscoped alternative delivery')
        references(option,'evidence_ids',evidence,True)
        references(option,'gap_ids',gaps)
    field_ids = set()
    for report in groups['report_types'].values():
        fields = report.get('fields')
        idx = index(fields,'field_id','fields')
        require([f.get('sequence') for f in fields] == list(range(1,len(fields)+1)), 'Report-field sequence')
        for ident, field in idx.items():
            require(ident not in field_ids, 'Duplicate global field ID')
            field_ids.add(ident)
            require(field.get('information_required'), 'Empty report information')
            references(field,'evidence_ids',evidence,True)
            if 'subitems' in field:
                children = index(field['subitems'],'subitem_id','subitems')
                require(field.get('condition_scope') == 'SUBITEMS_ONLY', 'Mixed conditions must apply to subitems')
                require(field.get('applicability_condition') is None, 'Do not filter the entire mixed X field')
                require([s.get('sequence') for s in children.values()] == list(range(1,len(children)+1)), 'Subitem sequence')
                for child in children.values():
                    references(child,'evidence_ids',evidence,True)
                    if child['condition_mode'] == 'CONDITIONAL':
                        require(child.get('condition') == {'parameter':'bunker_fuel_tonnes','operator':'GT','value':5000,'unit':'tonnes'}, 'Unexpected bunker subitem condition')
                    else:
                        require(child.get('condition') is None, 'Unconditional child has a condition')
    main = groups['report_types'].get('RT-CALDOVREP')
    require(main is not None and [f['code_as_published'] for f in main['fields']] == EXPECTED_CODES, 'CALDOVREP code groups changed')
    events = {}; spreads = set()
    require(len(groups['directions']) == 2, 'Pilot requires two separately researched directions')
    for direction in groups['directions'].values():
        rows = direction.get('reporting_events')
        index(rows,'event_id','events')
        require(direction.get('sequence_semantics') == 'EDITORIAL_DISPLAY_ORDER_NOT_FIXED_ITINERARY', 'Ambiguous sequence semantics')
        require([r.get('sequence') for r in rows] == list(range(1,len(rows)+1)), 'Event sequence')
        geometry = set()
        for event in rows:
            eid = event['event_id']; require(eid not in events, 'Duplicate event identity'); events[eid] = event
            require(event.get('vessel_applicability') and event.get('trigger_as_published'), 'Missing event applicability or trigger')
            require(event.get('report_type_id') in groups['report_types'], 'Unknown event report type')
            references(event,'evidence_ids',evidence,True); references(event,'gap_ids',gaps)
            cid = event.get('contact_id')
            require(cid is None or cid in groups['communications'], 'Unknown event recipient')
            path = 'directions[' + direction['direction_id'] + '].reporting_events[' + eid + ']'
            if cid is None:
                require(documented_gap(event,path+'.contact_id'), 'Missing event recipient without scoped gap')
            gid = event.get('reporting_object_id')
            require(gid is None or gid in groups['reporting_objects'], 'Unknown event geometry')
            if event.get('event_mode') == 'ENTRY': require(gid is not None, 'Entry geometry missing')
            if gid: geometry.add(gid)
            if event.get('timing_conditions'):
                index(event['timing_conditions'],'condition_id','timing_conditions')
                for timing in event['timing_conditions']:
                    references(timing,'evidence_ids',evidence,True)
                    require(timing.get('wording_as_published'), 'Missing timing source wording')
        spread = direction.get('spread',{})
        sid = spread.get('spread_id'); require(isinstance(sid,str) and sid and sid not in spreads, 'Duplicate or missing spread identity'); spreads.add(sid)
        require(set(spread.get('reporting_event_ids',[])) == {r['event_id'] for r in rows}, 'Spread event mismatch')
        objects = spread.get('reporting_object_ids',[])
        require(isinstance(objects,list) and set(objects) <= groups['reporting_objects'].keys(), 'Unknown spread object')
        require(geometry <= set(objects), 'Spread omits event geometry')
    # This revision has no performed approval. Later review needs actual records and a changed contract.
    for key in ['independent_review_record','marine_approval_record','artwork_check_record','release_record']:
        require(data['assurance'].get(key) is None, 'Unperformed approval: '+key)
    require(data['production'].get('pdf_output_paths') == [], 'No PDF has been produced for this revision')
    unheld = [s['source_id'] for s in sources.values() if s.get('source_status') != 'HELD']
    for sid in unheld:
        require(sources[sid].get('snapshot_id') is None and sources[sid].get('original_path') is None, 'Unheld source given a held identity')
    if unheld: require(data['research_state'] in {'DRAFT','HOLD'}, 'Incomplete sources cannot pass packet readiness')
    blockers = ['unretained_source:'+sid for sid in unheld]
    blockers += ['open_gap:'+g['gap_id'] for g in gaps.values() if g.get('disposition')=='OPEN']
    blockers += ['independent_review_missing','marine_approval_missing','artwork_QA_missing','complete_notices_check_missing']
    return {'draft_integrity':'PASS','directions':len(groups['directions']),'events':len(events),
            'report_types':len(groups['report_types']),'main_report_code_groups':len(main['fields']),
            'evidence_records':len(evidence),'sources':len(sources),'held_sources':len(sources)-len(unheld),
            'unretained_sources':unheld,'gaps':len(gaps),'publication_ready':False,'release_blockers':blockers}

def bunker_selection(field, amount):
    """Regression helper only: unknown quantity never means zero or an exemption."""
    result = {}
    for child in field['subitems']:
        if child['condition_mode']=='NO_ADDITIONAL_CONDITION': state='INCLUDE_WITHIN_PARENT_REPORT'
        elif amount is None: state='REVIEW_REQUIRED'
        else:
            require(isinstance(amount,(int,float)) and not isinstance(amount,bool) and math.isfinite(amount) and amount>=0, 'Invalid bunker amount')
            state='INCLUDE_WITHIN_PARENT_REPORT' if amount>child['condition']['value'] else 'CONDITION_NOT_MET'
        result[child['subitem_id']]=state
    return result

def negative_tests(data, catalogue):
    tests = []
    try: parse('---\nx: 1\nx: 2\n---\n')
    except Invalid: tests.append('duplicate YAML key')
    else: raise Invalid('Duplicate YAML key accepted')
    mutations = [
      ('invalid evidence',lambda d:d['directions'][0]['reporting_events'][0]['evidence_ids'].append('BOGUS')),
      ('duplicate event',lambda d:d['directions'][1]['reporting_events'][0].update(event_id='NE-ENTRY')),
      ('Boolean sequence',lambda d:d['directions'][0]['reporting_events'][0].update(sequence=True)),
      ('wrong sequence',lambda d:d['directions'][0]['reporting_events'][0].update(sequence=2)),
      ('wrong snapshot binding',lambda d:d['evidence'][0].update(snapshot_id='FAKE')),
      ('unperformed approval',lambda d:d['assurance'].update(marine_approval_record='APPROVED')),
      ('old field list',lambda d:d['report_types'][0]['fields'][0].update(code_as_published='L')),
      ('empty direction pack',lambda d:d.update(directions=[])),
      ('invalid requirement strength',lambda d:d['directions'][0]['reporting_events'][0].update(requirement_strength='BOGUS')),
      ('mandatory entry without recipient',lambda d:d['directions'][0]['reporting_events'][0].update(contact_id=None)),
      ('communications without evidence',lambda d:d['communications'][0].update(evidence_ids=[])),
      ('unresolvable supported field path',lambda d:d['evidence'][0].update(supported_field_paths=['guide_area.nonexistent'])),
      ('spread omits entry geometry',lambda d:d['directions'][0]['spread'].update(reporting_object_ids=[])),
      ('duplicate spread identity',lambda d:d['directions'][1]['spread'].update(spread_id=d['directions'][0]['spread']['spread_id'])),
      ('invalid geometry type',lambda d:d['reporting_objects'][0].update(geometry_type='BOGUS')),
      ('empty event list in one direction',lambda d:d['directions'][0].update(reporting_events=[])),
      ('whole X field filter',lambda d:d['report_types'][0]['fields'][12].update(applicability_condition='bunkers over 5000')),
      ('bunker threshold confused with vessel GT',lambda d:d['report_types'][0]['fields'][12]['subitems'][0]['condition'].update(parameter='vessel_gt')),
      ('missing subitem evidence',lambda d:d['report_types'][0]['fields'][12]['subitems'][0].update(evidence_ids=[])),
      ('unrelated recipient gap',lambda d:(d['directions'][0]['reporting_events'][0].update(contact_id=None,gap_ids=['G06']))),
      ('missing recipient with invented gap',lambda d:d['directions'][0]['reporting_events'][0].update(contact_id=None,gap_ids=['G999'])),
    ]
    for name, mutate in mutations:
        trial = deepcopy(data); mutate(trial)
        try: validate(trial,catalogue)
        except Invalid: tests.append(name)
        else: raise Invalid('Fault accepted: '+name)
    x = data['report_types'][0]['fields'][12]
    expected = {4999:'CONDITION_NOT_MET',5000:'CONDITION_NOT_MET',5000.1:'INCLUDE_WITHIN_PARENT_REPORT',None:'REVIEW_REQUIRED'}
    for amount,state in expected.items():
        selected = bunker_selection(x,amount)
        require(selected['X-BUNKERS']==state and selected['X-NAVIGATION']=='INCLUDE_WITHIN_PARENT_REPORT','X boundary selection failure')
    return {'defective_inputs_rejected':tests,'count':len(tests),'bunker_boundary_tests':4}

def file_record(root, relative):
    path=(root/relative).resolve()
    require(path.is_relative_to(root.resolve()),'Unsafe file path')
    require(path.is_file(),'Missing file: '+relative)
    b=path.read_bytes()
    return {'path':relative,'bytes':len(b),'sha256':sha256(b).hexdigest()}

def run(root):
    start=datetime.now(timezone.utc)
    work=root/'research/vts/VTS-0001'
    data=parse((work/'dossier.md').read_text(encoding='utf-8'))
    cat=json.loads((work/'source_catalogue.json').read_text(encoding='utf-8'))
    result=validate(data,cat)
    records=[]
    for source in cat['records']:
        if source['source_status']!='HELD':continue
        original=file_record(root,source['original_path']);text=file_record(root,source['text_path'])
        require(original['sha256']==source['original_sha256'] and original['bytes']==source['original_bytes'],'Original source mismatch')
        require(text['sha256']==source['text_sha256'],'Source extraction mismatch')
        records.extend([original,text])
    packet=json.loads((work/'packet.json').read_text(encoding='utf-8'))
    for entry in packet['files']:
        current=file_record(root,entry['path'])
        require(current['bytes']==entry['bytes'] and current['sha256']==entry['sha256'],'Packet mismatch: '+entry['path'])
    result.update(negative_tests=negative_tests(data,cat),packet_files_checked=len(packet['files']),source_files_checked=len(records),
                  dossier=file_record(root,'research/vts/VTS-0001/dossier.md'),
                  started_at_utc=start.isoformat(),finished_at_utc=datetime.now(timezone.utc).isoformat(),
                  independent_review_performed=False,limitations=['Pilot-specific structural checks, not a complete global schema','Source semantics, later notices and rights are not certified','No independent marine or artwork approval'])
    return result

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=ROOT)
    parser.add_argument('--release',action='store_true',help='Exit nonzero while release is blocked')
    args=parser.parse_args()
    try: result=run(args.root)
    except (Invalid,KeyError,TypeError,OSError,yaml.YAMLError) as error:
        print(json.dumps({'draft_integrity':'FAIL','error':str(error)}));return 1
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return 2 if args.release and not result['publication_ready'] else 0

if __name__=='__main__': sys.exit(main())
