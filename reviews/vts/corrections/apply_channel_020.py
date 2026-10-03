#!/usr/bin/env python3
"""One-shot author correction of PILOT-01. Never run against another input revision.
Writes only this pilot's dossier and catalogue. Does not approve or release content.
"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json
import yaml

ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / 'research/vts/VTS-0001'
raw = (WORK / 'dossier.md').read_text(encoding='utf-8')
if sha256(raw.encode()).hexdigest() != 'c9cb6c3cb07f8856a3cede312894454eded7aa2d24ff04d9a6e1dbbf847f9ecf':
    raise SystemExit('Input changed: do not overwrite an intervening research revision')
if sha256((WORK / 'source_catalogue.json').read_bytes()).hexdigest() != 'c46767941a9b1885d088e66dcb8ddd6d2e5c4721d8ea9f128a76480ec8c3ab83':
    raise SystemExit('Source catalogue changed: review before applying')
data = yaml.safe_load(raw.split('---\n', 2)[1])
body = raw.split('---\n', 2)[2]
geometry_before = json.dumps(data['reporting_objects'], sort_keys=True)
data['schema_version'] = '1.0-draft+channel.1'
data['production']['schema_revision'] = data['schema_version']
data['production']['research_revision'] = '0.2.0-author-correction'
data['production']['effort_record'] = 'effort.csv'
data['assurance']['research_cutoff_utc'] = datetime.now(timezone.utc).isoformat()
data['assurance']['subsequent_notices_check'] = 'PARTIAL. Existing MCA pages and cited IMO material rechecked for this correction. Complete ALRS, UKHO and French notices reconciliation remains G03.'
ev = {x['evidence_id']: x for x in data['evidence']}
fields = data['report_types'][0]['fields']
fields[11]['information_required'] = 'Total number of persons aboard.'
fields[9]['information_required'] = 'Report structural, cargo or equipment defects, damage or deficiencies. Also report other circumstances disrupting normal navigation under SOLAS or MARPOL.'
fields[12]['information_required'] = 'Miscellaneous information. Apply the condition to its individual subitem, not the entire X group.'
fields[12]['applicability_condition'] = None
fields[12]['condition_scope'] = 'SUBITEMS_ONLY'
fields[12]['subitems'] = [
    {'subitem_id': 'X-BUNKERS', 'sequence': 1, 'information_required': 'Estimated amount and characteristics of bunker fuel.', 'condition_mode': 'CONDITIONAL', 'condition': {'parameter': 'bunker_fuel_tonnes', 'operator': 'GT', 'value': 5000, 'unit': 'tonnes'}, 'requirement_strength': 'MANDATORY', 'evidence_ids': ['EV-F13']},
    {'subitem_id': 'X-NAVIGATION', 'sequence': 2, 'information_required': 'Navigational conditions.', 'condition_mode': 'NO_ADDITIONAL_CONDITION', 'condition': None, 'requirement_strength': 'MANDATORY', 'evidence_ids': ['EV-F13']}
]
sw = data['directions'][1]['reporting_events'][0]
sw['timing_conditions'] = [
    {'condition_id': 'SW-TIME-MGN', 'wording_as_published': 'not later than crossing', 'evidence_ids': ['EV-SW']},
    {'condition_id': 'SW-TIME-MCA', 'wording_as_published': 'when they’re in VHF radio range of North Foreland and before crossing the boundary line in the SW traffic lane.', 'evidence_ids': ['EV-SW-TIMING']}
]
sw['timing_summary'] = 'Within VHF range of North Foreland and before the eastern reporting line; MGN states no later than crossing.'
sw['evidence_ids'].append('EV-SW-TIMING')
ev['EV-SW-TIMING']['supported_field_paths'] += ['directions[P01-SW].reporting_events[SW-ENTRY].timing_conditions[SW-TIME-MCA].wording_as_published', 'directions[P01-SW].reporting_events[SW-ENTRY].timing_summary']
ev['EV-SW']['supported_field_paths'].append('directions[P01-SW].reporting_events[SW-ENTRY].timing_conditions[SW-TIME-MGN].wording_as_published')
ev['EV-F13']['supported_field_paths'] += ['report_types[RT-CALDOVREP].fields[FLD-13].subitems[X-BUNKERS]', 'report_types[RT-CALDOVREP].fields[FLD-13].subitems[X-NAVIGATION]']
data['conflicts'][3]['decision'] = 'Both source wordings are retained in the canonical SW event timing_conditions. timing_summary supplies the combined display instruction. No two-mile SW condition is inferred.'
data['conflicts'][3]['disposition'] = 'AUTHOR_CORRECTED_PENDING_REVIEW'

def add_evidence(eid, sid, locator, paths):
    snapshot = next((x['snapshot_id'] for x in data['evidence'] if x['source_id'] == sid), None)
    data['evidence'].append({'evidence_id': eid, 'source_id': sid, 'snapshot_id': snapshot, 'source_locator': locator, 'supported_field_paths': paths, 'wording_as_published': None, 'effective_from': None, 'effective_until': None, 'verification_state': 'AUTHOR_CHECKED'})

data['report_delivery_options'] = [{'option_id': 'OPT-CONFIDENTIAL-CARGO', 'report_type_id': 'RT-CALDOVREP', 'subject_scope': 'Commercially confidential cargo information only, not the entire CALDOVREP report.', 'method_as_published': 'non-verbal means', 'timing_as_published': 'prior to entering the system', 'requirement_strength': 'VOLUNTARY', 'implementation_state': 'CURRENT_DETAILS_UNRESOLVED', 'current_delivery_address': None, 'gap_ids': ['G04'], 'evidence_ids': ['EV-CARGO-OPTION']}]
for contact in data['communications']:
    contact['delivery_option_ids'] = ['OPT-CONFIDENTIAL-CARGO']
    contact['evidence_ids'].append('EV-CARGO-OPTION')
add_evidence('EV-CARGO-OPTION', 'P01-IMO85', 'Annex 2 section 3 opening paragraph, PDF page 11; section 5, PDF page 13', ['report_delivery_options[OPT-CONFIDENTIAL-CARGO]'])
data['communications'].append({'contact_id': 'COM-CHANNEL-ITZ', 'recipient': 'Channel VTS', 'call_sign': None, 'communication_method': None, 'calling_channel': None, 'working_channel': None, 'listening_watch': None, 'alternative_method': None, 'delivery_option_ids': [], 'gap_ids': ['G08'], 'evidence_ids': ['EV-ITZ-MGN']})
data['report_types'].append({'report_type_id': 'RT-ITZ-DECISION', 'official_name': None, 'fields': [{'field_id': 'FLD-ITZ', 'sequence': 1, 'code_as_published': None, 'information_required': 'Notify the decision to use the English ITZ, the intended route and reasons.', 'requirement_strength': 'MANDATORY', 'applicability_condition': 'Only when the master decides that circumstances warrant use of the English ITZ. Notification is not permission to breach Rule 10.', 'evidence_ids': ['EV-ITZ-MGN', 'EV-ITZ-DETAIL']}]})
for direction in data['directions']:
    direction['sequence_semantics'] = 'EDITORIAL_DISPLAY_ORDER_NOT_FIXED_ITINERARY'
    for event in direction['reporting_events']:
        event['event_mode'] = 'ENTRY' if event['event_id'].endswith('ENTRY') else 'CONDITIONAL'
        event['gap_ids'] = [] if event['event_mode'] == 'ENTRY' else ['G05']
        if event['event_mode'] == 'CONDITIONAL':
            event['recipient_as_published'] = 'relevant shore station'
    eid = direction['direction_id'].split('-')[-1] + '-ITZ-DECISION'
    direction['reporting_events'].append({'event_id': eid, 'sequence': 3, 'event_mode': 'CONDITIONAL', 'reporting_object_id': None, 'trigger_as_published': 'Masters deciding that circumstances warrant their use of the English ITZ, must report their decision to Channel VTS.', 'timing_as_published': None, 'requirement_strength': 'MANDATORY', 'vessel_applicability': 'Masters deciding that circumstances warrant use of the English ITZ; not a routine through-transit report.', 'contact_id': 'COM-CHANNEL-ITZ', 'report_type_id': 'RT-ITZ-DECISION', 'exceptions': 'Notification does not authorise use contrary to Rule 10(d).', 'subsequent_action': None, 'gap_ids': ['G08'], 'evidence_ids': ['EV-ITZ-MGN', 'EV-ITZ-DETAIL']})
    direction['spread']['reporting_event_ids'].append(eid)
add_evidence('EV-ITZ-MGN', 'SRC-005', 'Section 3.4', ['communications[COM-CHANNEL-ITZ].recipient', 'report_types[RT-ITZ-DECISION]', 'directions[P01-NE].reporting_events[NE-ITZ-DECISION]', 'directions[P01-SW].reporting_events[SW-ITZ-DECISION]'])
add_evidence('EV-ITZ-DETAIL', 'SRC-004', 'Inshore traffic zones, final notification paragraph', ['report_types[RT-ITZ-DECISION].fields[FLD-ITZ].information_required'])
data['guide_area']['geographical_scope'] = 'Standard NE-bound and SW-bound through-transits, approach reporting, conditional navigation changes and English ITZ notification. Special-operation variants are outside this sample, not exempt from their rules.'
data['scope_exclusions'] = [
    {'exclusion_id': 'EX-SMALL', 'subject': 'Complete reporting procedures for vessels below 300 GT.', 'basis': 'SRC-005 section 3.9 remains a specific conditional-reporting lead. No universal exemption is asserted.', 'approval_state': 'PROPOSED_FOR_MARINE_REVIEW'},
    {'exclusion_id': 'EX-TOW', 'subject': 'Complete tug and long-tow reporting procedures.', 'basis': 'SRC-005 section 5.1(iv) contains best-practice early and continued reporting advice. It is not applied to every vessel.', 'approval_state': 'PROPOSED_FOR_MARINE_REVIEW'},
    {'exclusion_id': 'EX-FERRY', 'subject': 'Ferry, harbour-entry, joining and crossing route variants.', 'basis': 'P01-IMO85 Annex 2 section 3.3 includes port-departure and ship-specific ferry arrangements. These remain outside the bounded through-transit example.', 'approval_state': 'PROPOSED_FOR_MARINE_REVIEW'},
    {'exclusion_id': 'EX-RECREATION', 'subject': 'Recreational and dive-support operations.', 'basis': 'SRC-005 section 6.4 contains a specific notification recommendation. Separate research is required for this vessel/activity scope.', 'approval_state': 'PROPOSED_FOR_MARINE_REVIEW'}
]
data['gaps'].append({'gap_id': 'G08', 'affected_field_paths': ['communications[COM-CHANNEL-ITZ]', 'directions[P01-NE].reporting_events[NE-ITZ-DECISION]', 'directions[P01-SW].reporting_events[SW-ITZ-DECISION]'], 'missing_information': 'Current operational recipient selection, contact method and timing for the English ITZ notification.', 'reason': 'MCA identifies Channel VTS and the reporting subject; the exact event-handling detail is not stated in the reviewed clause.', 'severity': 'BLOCKER', 'disposition': 'OPEN', 'next_action': 'Obtain current provider implementation before presenting this conditional event as a complete bridge instruction.', 'resolution_evidence_ids': [], 'decision_record': None})
add_evidence('EV-FORMAT-ROUTE', 'P01-A851', 'Appendix paragraph 2, PDF pages 7-9; read with P01-IMO85 Annex 2 section 3.1', ['gaps[G06]'])
for gap in data['gaps']:
    if gap['gap_id'] == 'G01':
        gap['missing_information'] = 'Retained originals and permitted storage for six live-only sources, including newly catalogued A.851(20).'
        gap['reason'] = 'Two MCA sources are held. Remaining consulted sources lack permitted retained originals. Rights and access are tracked separately.'
        gap['next_action'] = 'Confirm an authorised archive and applicable reproduction rights; capture actual bytes and renders, then issue a new packet.'
    if gap['gap_id'] == 'G04':
        gap['missing_information'] = 'Current watch, working-channel roles, AIS acceptance, non-verbal cargo delivery implementation and failure procedures.'
        gap['reason'] = 'The limited confidential-cargo option is now recorded. Current delivery addresses, accepted fields and procedures remain unconfirmed.'
    if gap['gap_id'] == 'G06':
        gap['reason'] = 'A.851(20), Appendix paragraph 2, is an identified format source. Current CALDOVREP implementation, amendments and nil conventions remain unchecked.'
        gap['next_action'] = 'Retain and reconcile A.851(20) and amendments with current provider/ALRS instructions. Do not import generic final-report events.'
cat = json.loads((WORK / 'source_catalogue.json').read_text(encoding='utf-8'))
cat['records'].append({'source_id': 'P01-A851', 'title': 'Resolution A.851(20): ship-reporting format reference', 'issuer': 'International Maritime Organization', 'publication_or_update_date': '1997-11-27', 'url': 'https://wwwcdn.imo.org/localresources/en/KnowledgeCentre/IndexofIMOResolutions/AssemblyDocuments/A.851(20).pdf', 'scope_locator': 'Appendix paragraph 2, PDF pages 7-9, especially B/C/D/E/F/I. Generic report schedules are not adopted as CALDOVREP duties.', 'accessed_date': '2026-10-03', 'source_status': 'LIVE_CONSULTED_NOT_HELD', 'snapshot_id': None, 'original_path': None, 'original_sha256': None, 'inspection_basis': 'Current author correction: parsed text and table page images inspected live. No retained original or independent review.', 'public_reproduction_status': 'Permission for this commercial-development public archive not established. IMO website terms and IP policy require assessment.', 'limitations': ['Format-reference route only. No provider implementation, nil-report convention or new final-report duty inferred.']})
for source in cat['records']:
    source['last_live_recheck_date'] = '2026-10-03'
    if source['source_status'] != 'HELD':
        source['retention_review'] = 'PENDING_RIGHTS_OR_APPROVED_REPOSITORY; no new original copy claimed'

lines = ['| Direction | Canonical entry timing | Published recipient / calling channel | Evidence |', '|---|---|---|---|']
contacts = {c['contact_id']: c for c in data['communications']}
for direction in data['directions']:
    event = direction['reporting_events'][0]
    contact = contacts[event['contact_id']]
    lines.append(f"| {direction['direction_label']} | {event.get('timing_summary', event['timing_as_published'])} | {contact['call_sign']} / VHF {contact['calling_channel']} | {', '.join(event['evidence_ids'])} |")
begin = body.index('| Direction |')
end = body.index('\n\nEach entry event', begin)
body = body[:begin] + '\n'.join(lines) + body[end:]
body = body.replace('Research sample 0.1.0 | 2 October 2026', 'Research correction 0.2.0 | 3 October 2026')
body = body.replace('The second event in each direction is conditional on changed navigation circumstances, not a routine second position report.', 'Each direction also records conditional navigation-change and English ITZ notification events.\nSequence values control display order, not a fixed itinerary or scheduled series of calls.')
body = body.replace('Seven open gaps remain in YAML', 'Eight open gaps remain in YAML')
body = body.replace('The next gate is a complete retained source packet and independent evidence/marine review before directional PDF production.', 'The correction pass addresses QA-01 to QA-07 without closing the remaining evidence or release gates.\nA complete retained source packet and independent evidence/marine review remain necessary before approved directional PDF production.')
body = body.replace('The field descriptions are paraphrases, not a complete encoded radio message.', 'The field descriptions are paraphrases, not a complete encoded radio message.\nW explicitly requests the number aboard. Q/R retains structure, cargo and equipment scope.\nX contains two subitems in the published order. Only the bunker subitem has the greater-than-5,000-tonne condition.')
body = body.replace('Details remain G04.', 'Current implementation details remain G04.\nThe base instrument permits advance non-verbal delivery for confidential cargo information only.\nThis is not an exemption from the remaining report. No delivery address has been invented.\n[P01-IMO85, Annex 2 section 3 opening paragraph and section 5]')
body = body.replace('## 5. Geometry and artwork', 'English ITZ notification is recorded as a separate conditional event, not permission to contravene Rule 10.\nThe reporting subject is established; current contact handling and timing remain G08.\n[SRC-005, 3.4; SRC-004, Inshore traffic zones]\n\nThe YAML scope_exclusions explicitly identify special-operation variants outside this sample.\nThey are proposed editorial boundaries, not vessel exemptions or approved operational exclusions.\n\n## 5. Geometry and artwork')
body = body.replace('Current ALRS, the full UKHO/French notices chain and current call-name convention require reconciliation before release.', 'A.851(20) has been catalogued as the format-source route for G06; no encoded example is claimed.\nCurrent ALRS, the full UKHO/French notices chain and current call-name convention require reconciliation before release.')
body = body.replace('`author_check.json` records structural checks and limitations; it is not independent approval.', '`author_check.json` records the historical 0.1.0 checks. It is not approval of this corrected revision.\nThe current packet and correction report identify the actual corrected files and later test results.')
if json.dumps(data['reporting_objects'], sort_keys=True) != geometry_before:
    raise SystemExit('Unexpected geometry change')
if data['research_state'] != 'HOLD' or len(data['evidence']) != 32:
    raise SystemExit('Unexpected state or evidence population')
if any(data['assurance'][key] for key in ['independent_review_record', 'marine_approval_record', 'artwork_check_record', 'release_record']):
    raise SystemExit('Unperformed approval')
(WORK / 'dossier.md').write_text('---\n' + yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=110) + '---\n' + body, encoding='utf-8')
(WORK / 'source_catalogue.json').write_text(json.dumps(cat, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'result': 'AUTHOR_CORRECTION_CHECKPOINT_NOT_APPROVAL', 'directions': 2, 'events': 6, 'evidence_records': 32, 'source_records': 8, 'held_sources': 2, 'research_state': 'HOLD', 'dossier_sha256': sha256((WORK / 'dossier.md').read_bytes()).hexdigest()}))
