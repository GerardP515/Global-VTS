#!/usr/bin/env python3
"""Render the Channel pilot's readable body; never rewrite its canonical YAML.
Pilot-specific presentation adapter, not a navigational or general-schema validator.
Requires the existing PyYAML dependency. Default mode only checks committed output.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import io
import json
import re
import subprocess
from pathlib import Path
from string import Template
import yaml

ROOT = Path(__file__).resolve().parents[1]
DOSSIER = 'research/vts/VTS-0001/dossier.md'
CATALOGUE = 'research/vts/VTS-0001/source_catalogue.json'
TEMPLATE = 'research/vts/templates/guide.proforma.md'
EXPECTED_YAML = 'e35c68bc166249f2e5244b0bec4a9f30c82ffb084f3c8c71725e49c76ff3e5ef'
INPUT_COMMIT = 'b175a412fc2c118a3d4f1c266e667e92984d5571'
PRESENTATION = 'proforma-1'
SOURCE_ORDER = ['SRC-005','P01-IMO251','SRC-004','P01-IMO85','P01-TH-RS','P01-A851','P01-DOVER-PORT','P01-LIB-NCSR13']
LOCATORS = {
 'EV-IDENTITY':'About the Dover Strait; How Channel VTS works',
 'EV-THRESHOLD':'§§3.7–3.9','EV-THRESHOLD-IMO':'Annex 2 §1',
 'EV-EXEMPT':'Exemptions','EV-FERRY':'Annex 2 §3.3, Crossing Traffic',
 'EV-NE':'§3.11','EV-SW':'§3.10','EV-SW-TIMING':'Mandatory reporting, SW paragraph',
 'EV-AMENDMENT':'commencement paragraph; Appendix (PDF pp.2–3)',
 'EV-OLD-LIST':'Mandatory reporting, content list','EV-CHANGE':'Annex 2 §3.3',
 'EV-AIS':'Mandatory reporting, communications','EV-RS':'deconstruction account',
 'EV-FUTURE':'PDF pp.1–2','EV-PORT':'VTS Information; Entry procedure',
 'EV-CARGO-OPTION':'Annex 2 §§3, 5','EV-ITZ-MGN':'§3.4',
 'EV-ITZ-DETAIL':'Inshore traffic zones, final paragraph',
 'EV-FORMAT-ROUTE':'Appendix §2 (PDF pp.7–9)'
}

def require(condition, message):
    if not condition:
        raise ValueError(message)

class StrictLoader(yaml.SafeLoader):
    pass

def unique_keys(loader, node, deep=False):
    result = {}
    for k, v in node.value:
        key = loader.construct_object(k, deep=deep)
        require(key not in result, 'Duplicate YAML key: '+str(key))
        result[key] = loader.construct_object(v, deep=deep)
    return result

StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_keys)

def split_dossier(raw):
    require(raw.startswith(b'---\n'), 'Missing YAML front matter')
    end = raw.index(b'\n---\n', 4) + 5
    front = raw[:end]
    require(hashlib.sha256(front).hexdigest() == EXPECTED_YAML,
            'Canonical YAML changed: review this presentation adapter before reuse')
    data = yaml.load(front[4:-5].decode('utf-8'), Loader=StrictLoader)
    require(data['vts_id']=='VTS-0001' and data['research_state']=='HOLD', 'Wrong pilot or lifecycle')
    return front, data

def cell(value):
    return str(value).replace('|', '&#124;').replace('\n', ' ')

def table(headers, rows):
    return '\n'.join(['| '+' | '.join(headers)+' |',
                      '| '+' | '.join('---' for _ in headers)+' |']+
                     ['| '+' | '.join(cell(v) for v in row)+' |' for row in rows])+'\n'

def render(data, catalogue, template):
    sources = {r['source_id']:r for r in catalogue['records']}
    require(set(sources)==set(SOURCE_ORDER), 'Unexpected catalogue membership')
    refs = {sid:'R'+str(i+1) for i,sid in enumerate(SOURCE_ORDER)}
    evidence = {r['evidence_id']:r for r in data['evidence']}
    seen = set()
    def cite(*ids):
        out = []
        for eid in ids:
            ev = evidence[eid]; seen.add(eid); label = refs[ev['source_id']]
            locator = LOCATORS.get(eid)
            if eid.startswith('EV-F') and eid[4:].isdigit():
                field = data['report_types'][0]['fields'][int(eid[4:])-1]
                locator = 'Appendix, item '+field['code_as_published']+' (PDF p.3)'
            require(bool(locator), 'Missing display locator: '+eid)
            item = f'[{label} {locator}](#{label.lower()})'
            if item not in out: out.append(item)
        return ' '.join(out)
    objects = {r['object_id']:r for r in data['reporting_objects']}
    contacts = {r['contact_id']:r for r in data['communications']}
    reports = {r['report_type_id']:r for r in data['report_types']}
    overview = table(['Item','Recorded position'],[
      ('Service',data['guide_area']['official_service_name']+' '+cite('EV-IDENTITY')),
      ('Operating centres',data['guide_area']['provider']+' '+cite('EV-IDENTITY')),
      ('Reporting system','CALDOVREP. '+cite('EV-IDENTITY','EV-AMENDMENT')),
      ('Study scope',data['guide_area']['geographical_scope']+' (Editorial scope.)'),
      ('Authority detail',data['guide_area']['authority']+' '+cite('EV-IDENTITY')+' [G03](#g03).')])
    overview += '\nChannel VTS and Port of Dover harbour VTS are separate services. Harbour-entry procedures are outside this guide. '+cite('EV-PORT')+'\n'
    participation = ('**Standard participation:** '+data['participation']['applicability_as_published']+'. '+cite('EV-THRESHOLD','EV-THRESHOLD-IMO')+'\n\n'
      '**Naval vessels:** '+data['participation']['exemptions_as_published']+'. '+cite('EV-EXEMPT')+'\n\n'
      '**Ferry arrangements:** simplified reporting must not be treated as a blanket exemption. The original scheme requires ship-specific bilateral approval. '+cite('EV-FERRY','EV-EXEMPT')+'\n\n'
      'The shorter MCA summary uses a different threshold formulation. The inclusive threshold is retained; see C01 in Section 9. '+cite('EV-THRESHOLD','EV-THRESHOLD-IMO')+' [R3 Mandatory reporting](#r3)'+'\n\n'
      '### 2.1 Scope exclusions\n\nThese are proposed editorial exclusions, not exemptions from applicable reporting rules.\n\n')
    scope_refs = {'EX-SMALL':('SRC-005 section 3.9','R1 §3.9','r1'),
      'EX-TOW':('SRC-005 section 5.1(iv)','R1 §5.1(iv)','r1'),
      'EX-FERRY':('P01-IMO85 Annex 2 section 3.3','R4 Annex 2 §3.3','r4'),
      'EX-RECREATION':('SRC-005 section 6.4','R1 §6.4','r1')}
    scope_rows=[]
    for x in data['scope_exclusions']:
        old,label,anchor=scope_refs[x['exclusion_id']]
        wording=x['basis'].replace(old,'The source')
        scope_rows.append((x['subject'],wording+f' [{label}](#{anchor})'))
    participation += table(['Not fully developed in this sample','Research position'],scope_rows)
    directional = 'The two directions are presented separately. Conditional notifications are not routine second or third reporting points.\n\n'
    for i,direction in enumerate(data['directions'],1):
        entry = next(e for e in direction['reporting_events'] if e['event_mode']=='ENTRY')
        com = contacts[entry['contact_id']]; obj = objects[entry['reporting_object_id']]
        timing = entry.get('timing_summary',entry['timing_as_published'])
        directional += f"### 3.{i} {direction['direction_label']} transit\n\n"
        directional += table(['Action or condition','Reporting arrangement','Reference'],[
          ('Applicability',direction['vessel_applicability'],cite('EV-THRESHOLD','EV-EXEMPT')),
          ('Entry boundary',obj['graphic_label']+'. Full description in Section 7.',cite(*obj['evidence_ids'])),
          ('When to report',timing,cite(*[e for e in entry['evidence_ids'] if e in ['EV-NE','EV-SW','EV-SW-TIMING']])),
          ('Who to call',com['call_sign']+'; '+com['recipient']+'.',cite(*[e for e in com['evidence_ids'] if e in ['EV-NE','EV-SW']])),
          ('Published calling channel','VHF '+com['calling_channel']+'. Further channel roles remain open under G04.',cite(*[e for e in com['evidence_ids'] if e in ['EV-NE','EV-SW']])),
          ('Information required','CALDOVREP information in Section 4, including each stated condition.',cite('EV-AMENDMENT'))])
        directional += ('\n**During transit:** see Section 6 for conditional navigation-change and English ITZ notifications. '
                        +cite('EV-CHANGE','EV-ITZ-MGN')+'\n\n'
                        '**Transfers and departure:** subsequent routine instructions are not established in this sample. '
                        'Do not read this as “no report required”. See [G03](#g03)–[G05](#g05).\n\n')
    main = reports['RT-CALDOVREP']
    information = ('The table shows the report subjects retained in the amended CALDOVREP list. '
      'It is not a worked radio message. '+cite('EV-AMENDMENT')+'\n\n'
      '**Open formatting checks:** units, time standard, encoding and nil-report handling remain under [G06](#g06).\n\n')
    rows=[]
    for field in main['fields']:
        text=field['information_required']
        condition=field['applicability_condition'] or 'Not separately recorded.'
        if field.get('subitems'):
            text='Bunker particulars and navigational conditions. See the separate subjects in Section 4.1.'
            condition='Apply the bunker threshold only to the bunker particulars.'
        rows.append((field['code_as_published'],text,condition,cite(*field['evidence_ids'])))
    information += table(['Code','Information required','Condition or qualification','Reference'],rows)
    information += '\n### 4.1 Field X: separate reporting subjects\n\nThe following labels are editorial descriptions, not additional official report codes.\n\n'
    rows=[]
    for s in main['fields'][-1]['subitems']:
        cond=s['condition']
        condition=(f"Bunker fuel exceeds {cond['value']:,} {cond['unit']}." if cond else 'Not subject to the bunker-quantity threshold.')
        rows.append((s['information_required'],condition,cite(*s['evidence_ids'])))
    information+=table(['Subject within X','Condition','Reference'],rows)
    information+='\nUnknown bunker quantity remains a review question. It is not treated as zero or an automatic exemption.\n\n'
    information+='### 4.2 Confidential cargo information\n\n'
    option=data['report_delivery_options'][0]
    information+=('The original scheme provides an advance non-verbal option for commercially confidential cargo particulars. '
       +cite(*option['evidence_ids'])+'\n\n'
       'This concerns the cargo portion only, not the entire report. '+cite(*option['evidence_ids'])+'\n\n'
       '**Current delivery details remain unconfirmed.** No address or whole-report exemption is supplied. See [G04](#g04).\n')
    comms=table(['Purpose','Recipient / call sign','Calling channel','Other channel roles','Reference'],[
       ('NE entry',contacts['COM-GRISNEZ']['recipient']+' / '+contacts['COM-GRISNEZ']['call_sign'],'VHF '+contacts['COM-GRISNEZ']['calling_channel'],'Working-channel assignment and listening watch not established: G04.',cite('EV-NE')),
       ('SW entry',contacts['COM-DOVER']['recipient']+' / '+contacts['COM-DOVER']['call_sign'],'VHF '+contacts['COM-DOVER']['calling_channel'],'Working-channel assignment and listening watch not established: G04.',cite('EV-SW')),
       ('English ITZ notification',contacts['COM-CHANNEL-ITZ']['recipient'],'Not established: G08.','Recipient selection, method and timing remain open.',cite('EV-ITZ-MGN'))])
    comms+='\nAIS reception capability does not establish a universal exemption from voice reporting. '+cite('EV-AIS')+'\n\n'
    comms+='Current call-name, watch, transfer, failure and alternative-delivery details remain subject to [G03](#g03), [G04](#g04) and [G08](#g08).\n'
    conditional='These notifications are conditional. Display order is not a schedule of calls.\n\n'
    conditional+='### 6.1 Changed navigational circumstances\n\n'
    change=reports['RT-CHANGE']['fields'][0]
    conditional+=table(['Item','Recorded requirement'],[
      ('Trigger','Whenever navigational circumstances change. '+cite('EV-CHANGE')),
      ('Information',change['information_required']+' '+cite(*change['evidence_ids'])),
      ('Recipient','The relevant shore station. Exact selection remains open under G05. '+cite('EV-CHANGE')),
      ('Strength',change['applicability_condition']+' '+cite('EV-CHANGE')+' [G05](#g05).')])
    conditional+='\n### 6.2 Decision to use the English ITZ\n\n'
    itz=reports['RT-ITZ-DECISION']['fields'][0]
    conditional+=itz['information_required']+' '+cite(*itz['evidence_ids'])+'\n\n'
    conditional+=itz['applicability_condition']+' '+cite(*itz['evidence_ids'])+'\n\n'
    conditional+='**Implementation gap:** exact current contact selection, method and timing remain [G08](#g08).\n'
    geometry='**Not approved for plotting.** Published descriptions are retained below. Missing endpoints or datum must not be inferred.\n\n'
    for obj in data['reporting_objects']:
        geometry+='### 7.'+str(list(objects).index(obj['object_id'])+1)+' '+obj['graphic_label']+'\n\n'
        geometry+=obj['geometry_as_published']+' '+cite(*obj['evidence_ids'])+'\n\n'
        geometry+='**Datum:** not stated in the recorded source clause. **Plotting:** blocked pending [G02](#g02).\n\n'
    geometry+=('The western reference requires confirmation following the reported removal of Royal Sovereign lighthouse topsides. '
       +cite('EV-RS','EV-NE')+'\n\n'
       'That removal does not establish a replacement reporting line. No replacement position is supplied.\n\n'
       '### 7.3 Artwork requirements\n\n'
       'Keep reporting boundaries as lines. Direction arrows must not imply approved tracks. '
       'Show applicability and conditional notices beside the relevant callouts.\n\n'
       'Map extent, base material, reproduction permissions and finished artwork remain unapproved. See [G02](#g02) and [G07](#g07).\n')
    bibliography=('References below identify the exact provisions used by this draft. '
      'A citation is not a claim that an unretained original is held.\n\n'
      '“PDF page” refers to file-page order. Printed page numbers are retained in the underlying evidence ledger.\n\n')
    for sid in SOURCE_ORDER:
        src=sources[sid]; rid=refs[sid]
        bibliography+=f'<a id="{rid.lower()}"></a>\n\n### {rid}. {src["title"]}\n\n'
        bibliography+=f'**Issuer:** {src["issuer"]}. **Publication/update:** {src.get("publication_or_update_date") or "not recorded"}.\n\n'
        bibliography+=f'[Original source]({src["url"]}) · **Recorded access:** {src["accessed_date"]}.\n\n'
        bibliography+='**Source scope:** '+src['scope_locator']+'\n\n'
        if src['source_status']=='HELD':
            bibliography+='**Retained:** original HTML and mechanical text extraction.\n\n'
            bibliography+=f'Original: `{src["original_path"]}`.\n\nExtraction: `{src["text_path"]}`.\n\n'
        else:
            bibliography+='**Not retained:** consulted live in the earlier research; no original snapshot is held in this packet. See [G01](#g01).\n\n'
        bibliography+='**Limitations:** '+'; '.join(src.get('limitations',[]))+'\n\n'
    issues='Open checks remain visible here and beside the affected instructions. None is closed by this presentation change.\n\n'
    for gap in data['gaps']:
        gid=gap['gap_id']
        issues+=f'<a id="{gid.lower()}"></a>\n\n### {gid}. {gap["missing_information"]}\n\n'
        issues+=f'**Status:** {gap["disposition"]}. **Severity:** {gap["severity"]}.\n\n'
        issues+=gap['reason']+'\n\n**Required action:** '+gap['next_action']+'\n\n'
    issues+='### 9.1 Source conflicts and author dispositions\n\n'
    for conflict in data['conflicts']:
        issues+=f'**{conflict["conflict_id"]} · {conflict["disposition"]}**\n\n'
        for assertion in conflict['assertions']:
            citation=cite(*assertion.get('evidence_ids',[])) if assertion.get('evidence_ids') else f'[{refs[assertion["source_id"]]}](#{refs[assertion["source_id"]].lower()})'
            issues+=assertion['assertion']+' '+citation+'\n\n'
        issues+='**Author disposition:** '+conflict['decision']+'\n\n'
    issues+='### 9.2 Amendment and format follow-up\n\n'
    issues+='The catalogued NCSR 13 account is a prospective amendment lead, not an adopted instruction. '+cite('EV-FUTURE')+'\n\n'
    issues+='A.851(20) is the recorded format-reference route. Current implementation and nil conventions remain unconfirmed. '+cite('EV-FORMAT-ROUTE')+'\n'
    appendix=('The operational YAML is unchanged from revision 0.2.1. This is presentation revision '+PRESENTATION+'.\n\n'
      'No new source acquisition, current-notice check, independent review or publication approval is claimed.\n\n'
      'The YAML, source catalogue and capture manifests remain the underlying evidence records. '
      'Reader labels R1–R8 are aliases, not replacement source IDs.\n\n')
    appendix+=table(['Record','Location'],[
      ('Detailed correction and re-proof history','[Correction report](../../../reviews/vts/reports/PILOT-01__correction_reproof_2026-10-03.md)'),
      ('Source catalogue','[source_catalogue.json](source_catalogue.json)'),
      ('Exact review inputs','[packet.json](packet.json)'),
      ('Presentation checks','[presentation_check.json](presentation_check.json)'),
      ('Prospective effort ledger','[effort.csv](effort.csv)')])
    appendix+='\n### A.1 Citation crosswalk\n\n'
    appendix+=table(['Reader reference','Source ID'],[(refs[s],s) for s in SOURCE_ORDER])
    appendix+='\n### A.2 Complete evidence locator ledger\n\n'
    appendix+=table(['Evidence ID','Reader citation','Exact recorded locator'],[(eid,cite(eid),ev['source_locator']) for eid,ev in evidence.items()])
    appendix+='\n### A.3 Event-to-section crosswalk\n\n'
    event_rows=[]
    for d in data['directions']:
        for e in d['reporting_events']:
            location='Section 3.1' if e['event_id']=='NE-ENTRY' else 'Section 3.2' if e['event_id']=='SW-ENTRY' else 'Section 6.2' if 'ITZ' in e['event_id'] else 'Section 6.1'
            event_rows.append((e['event_id'],d['direction_label'],e['event_mode'],location))
    appendix+=table(['Event ID','Direction','Event type','Readable location'],event_rows)
    blocks=dict(guide_title=data['guide_area']['official_service_name']+' / '+main['official_name'],
                revision=data['production']['research_revision'],presentation=PRESENTATION,overview=overview,participation=participation,directional=directional,information=information,
                communications=comms,conditional=conditional,geometry=geometry,references=bibliography,
                outstanding=issues,appendix=appendix)
    body=Template(template).substitute(blocks).rstrip()+'\n'
    require(seen==set(evidence),'Evidence missing from readable ledger')
    require(len(re.findall(r'^## [1-9]\. ',body,re.M))==9,'Wrong pro forma section population')
    require(len(re.findall(r'^### R[1-8]\. ',body,re.M))==8,'Missing bibliography item')
    for target in re.findall(r'\]\(#([^)]*)\)',body):
        require(f'id="{target}"' in body, 'Unresolved anchor: '+target)
    return body, {'presentation_revision':PRESENTATION,'canonical_yaml_sha256':EXPECTED_YAML,
      'directions':len(data['directions']),'events':len(event_rows),'main_report_code_groups':len(main['fields']),
      'evidence_records':len(evidence),'bibliography_entries':len(refs),'gaps':len(data['gaps']),
      'conflicts':len(data['conflicts']),'research_state':data['research_state'],'publication_ready':False,
      'source_reference_map':refs,'checks':['YAML bytes unchanged','all evidence mapped','all citation anchors resolve',
      'all events mapped','nine fixed sections','eight bibliography records'],
      'limits':['Presentation transformation only','No fresh operational fact check','No independent or marine approval']}

def file_record(root, name):
    raw=(root/name).read_bytes()
    return dict(path=name,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--root',type=Path,default=ROOT)
    ap.add_argument('--apply',action='store_true')
    ap.add_argument('--packet',action='store_true')
    ap.add_argument('--export-dir',type=Path)
    args=ap.parse_args(); root=args.root.resolve(); work=root/'research/vts/VTS-0001'
    old=(root/DOSSIER).read_bytes();front,data=split_dossier(old)
    cat=json.loads((root/CATALOGUE).read_text(encoding='utf-8'))
    body,checks=render(data,cat,(root/TEMPLATE).read_text(encoding='utf-8'))
    result=front+b'\n'+body.encode('utf-8')
    require(split_dossier(result)[0]==front,'Canonical YAML was modified')
    if args.apply:
        (root/DOSSIER).write_bytes(result)
        checks.update(input_dossier_sha256=hashlib.sha256(old).hexdigest(),
                      output_dossier_sha256=hashlib.sha256(result).hexdigest(),input_commit=INPUT_COMMIT)
        (work/'presentation_check.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    else:
        require(old==result,'Readable body differs from canonical rendering; run --apply only after review')
    if args.packet:
        p=work/'packet.json'; packet=json.loads(p.read_text(encoding='utf-8'))
        packet['presentation_parent_packet_revision']=packet['packet_revision']
        packet['packet_revision']='P01-0.2.1-P1-INCOMPLETE'
        packet['research_commit']=subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip()
        packet['presentation_revision']=PRESENTATION
        names=[r['path'] for r in packet['files']]
        names+=['research/vts/VTS-0001/presentation_check.json',TEMPLATE,'scripts/render_channel_proforma.py']
        packet['files']=[file_record(root,n) for n in dict.fromkeys(names)]
        packet['assembly_note']='Presentation-only dossier commit and exact input hashes; canonical YAML unchanged. HOLD and source limitations remain.'
        p.write_text(json.dumps(packet,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        status=root/'research/vts/STATUS.csv'
        with status.open(newline='',encoding='utf-8') as f:
            reader=csv.DictReader(f); fields=reader.fieldnames; rows=list(reader)
        for row in rows:
            if row['study_id']=='PILOT-01':
                row['research_commit']=packet['research_commit'];row['source_packet_revision']=packet['packet_revision']
                row['notes']='0.2.1 canonical YAML unchanged; proforma-1 readable guide; HOLD; eight gaps; no new sources, independent approval or PDF.'
        out=io.StringIO(newline='');writer=csv.DictWriter(out,fieldnames=fields,lineterminator='\n');writer.writeheader();writer.writerows(rows)
        status.write_text(out.getvalue(),encoding='utf-8')
    if args.export_dir:
        args.export_dir.mkdir(parents=True,exist_ok=True)
        (args.export_dir/'Channel_VTS_Guide.md').write_bytes(result)
        (args.export_dir/'Channel_VTS_Reading_Copy.md').write_text(body,encoding='utf-8')
        (args.export_dir/'presentation_check.json').write_text(json.dumps(checks,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(checks,ensure_ascii=False,indent=2))

if __name__=='__main__':
    main()
