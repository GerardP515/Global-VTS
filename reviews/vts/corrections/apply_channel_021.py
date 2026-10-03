#!/usr/bin/env python3
"""Apply three recorded first-reproof refinements to one exact Channel pilot revision."""
from pathlib import Path
from hashlib import sha256
import json
import yaml
ROOT = Path(__file__).resolve().parents[3]
path = ROOT / 'research/vts/VTS-0001/dossier.md'
raw = path.read_text(encoding='utf-8')
if sha256(raw.encode()).hexdigest() != '45b517e8a953faf2f26b119caa36d695b9c218e8b21fc5879b3e434c08e0358c':
    raise SystemExit('Stage 1 input changed; do not overwrite')
_, yml, body = raw.split('---\n', 2)
data = yaml.safe_load(yml)
for c in data['communications']:
    if c['contact_id'] in {'COM-GRISNEZ','COM-DOVER'}:
        c['working_channel'] = None
        c['gap_ids'] = ['G04']
        c['channel_role_note'] = 'Calling channel retained from MGN 364 sections 3.10-3.11. A separate working-channel assignment is not asserted.'
for gap in data['gaps']:
    if gap['gap_id']=='G04':
        gap['affected_field_paths'] += ['communications[COM-GRISNEZ].working_channel','communications[COM-DOVER].working_channel']
contacts = {c['contact_id']:c for c in data['communications']}
objects = {g['object_id']:g for g in data['reporting_objects']}
lines = ['| Direction | Reporting boundary | Canonical entry timing | Published recipient / calling channel | Evidence |', '|---|---|---|---|---|']
for d in data['directions']:
    e = d['reporting_events'][0]
    c = contacts[e['contact_id']]
    g = objects[e['reporting_object_id']]
    lines.append(f"| {d['direction_label']} | {g['graphic_label']} | {e.get('timing_summary',e['timing_as_published'])} | {c['call_sign']} / VHF {c['calling_channel']} | {', '.join(e['evidence_ids'])} |")
a = body.index('| Direction |')
b = body.index('\n\nEach entry event', a)
body = body[:a] + '\n'.join(lines) + body[b:]
body = body.replace('Research correction 0.2.0', 'Research correction 0.2.1')
body = body.replace('The correction pass addresses QA-01 to QA-07', 'The correction pass addresses QA-01 to QA-07 and records first-reproof refinements RR-01 to RR-03')
body = body.replace('Current ALRS, the full UKHO/French notices chain and current call-name convention require reconciliation before release.', 'Calling channels are retained; separate working-channel assignments remain unknown under G04.\nCurrent ALRS, the full UKHO/French notices chain and current call-name convention require reconciliation before release.')
data['production']['research_revision'] = '0.2.1-author-correction'
path.write_text('---\n'+yaml.safe_dump(data,sort_keys=False,allow_unicode=True,width=110)+'---\n'+body,encoding='utf-8')
print(json.dumps({'revision':data['production']['research_revision'],'dossier_sha256':sha256(path.read_bytes()).hexdigest(),'research_state':data['research_state']}))
