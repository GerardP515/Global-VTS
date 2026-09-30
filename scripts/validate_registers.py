#!/usr/bin/env python3
"""Validate register structure and referential integrity, not maritime accuracy."""
from __future__ import annotations
import collections
import csv
import io
import json
import re
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
REGIONS={'BIS','NOI','BAL','NSC','FIC','MED','SAF','RSA','IOS','MSI','CSC','NWP','AUS','NPC','CAP','CGP','NAC'}
CATEGORIES={'VTS + MRS','VTS only','MRS only','Neither confirmed','Unresolved'}
MASTER='data/current/TSS_VTS_MRS_Association_Register.csv'


def parse_table(content: str, label: str='CSV') -> tuple[list[str],list[dict[str,str]]]:
    parsed=list(csv.reader(io.StringIO(content),strict=True))
    if not parsed or len(set(parsed[0]))!=len(parsed[0]) or any(not h for h in parsed[0]):
        raise ValueError(f'{label}: missing or duplicate header')
    for index,row in enumerate(parsed[1:],2):
        if len(row)!=len(parsed[0]):
            raise ValueError(f'{label}: logical record {index} has {len(row)} fields, expected {len(parsed[0])}')
    return parsed[0],[dict(zip(parsed[0],row)) for row in parsed[1:]]


def table(path: str) -> tuple[list[str],list[dict[str,str]]]:
    return parse_table((ROOT/path).read_text(encoding='utf-8-sig'),path)


def unique(rows: list[dict],key: str,label: str) -> set[str]:
    values=[r[key] for r in rows]
    if any(not x for x in values) or len(values)!=len(set(values)):
        raise ValueError(f'{label}: blank/duplicate {key}')
    return set(values)


def references(value: str,prefix: str) -> list[str]:
    return re.findall(rf'\b{prefix}-\d+\b',value)


def check(condition: bool,message: str) -> None:
    if not condition:raise ValueError(message)


def validate() -> dict:
    paths=list((ROOT/'data/current').glob('*.csv'))+list((ROOT/'data/authoritative').glob('*.csv'))+[ROOT/'sources/SOURCE_REGISTER.csv']
    for p in paths:table(p.relative_to(ROOT).as_posix())
    header,rows=table(MASTER)
    _,base=table('data/authoritative/IMO_2025_Individual_TSS_Inventory.csv')
    _,parents=table('data/authoritative/IMO_2025_Part_B_Parent_Inventory.csv')
    _,vts=table('data/current/VTS_Entity_Register.csv')
    _,reports=table('data/current/Reporting_Scheme_Register.csv')
    _,sources=table('sources/SOURCE_REGISTER.csv')
    _,batch=table('data/current/Batch_Status.csv')
    _,relations=table('data/current/TSS_Service_Relationships.csv')
    _,gaps=table('data/current/Research_Gaps.csv')
    tids=unique(rows,'tss_id','master');bids=unique(base,'canonical_id','baseline')
    check(tids==bids and len(tids)==224,'Master must cover all 224 baseline IDs exactly once')
    pids=unique(parents,'imo_ref','parents');check(len(pids)==164,'Expected 164 source parent entries')
    parent_counts=collections.Counter(r['imo_parent_ref'] for r in base)
    for p in parents:check(parent_counts[p['imo_ref']]==int(p['individual_tss_count']),f"Parent count mismatch: {p['imo_ref']}")
    vids=unique(vts,'vts_id','VTS register');rids=unique(reports,'vrs_id','reporting register');sids=unique(sources,'source_id','sources')
    bmap={r['canonical_id']:r for r in base};mapping={r['tss_id']:r for r in rows}
    check(len(rids)==28 and sum(r['adoption_scope']=='IMO-adopted baseline' for r in reports)==23,'Reporting inventory must distinguish 23 IMO and five national schemes')
    for r in rows:
        tid=r['tss_id'];b=bmap[tid]
        check(r['tss_name']==b['display_name'],f'Name drift: {tid}')
        check(r['imo_parent_ref']==b['imo_parent_ref'],f'Parent drift: {tid}')
        check(r['region_code'] in REGIONS and r['region_code']==b['project_region_code'],f'Region mismatch: {tid}')
        check(r['association_status'] in CATEGORIES,f'Unknown classification: {tid}')
        check(r['mandatory_reporting'] in {'Yes','No','Unresolved'},f'Invalid mandatory flag: {tid}')
        check(r['voluntary_reporting'] in {'Yes','No','Unresolved'},f'Invalid voluntary flag: {tid}')
        check(r['review_status'] in {'pass1-recorded','reopened','audited'},f'Invalid review state: {tid}')
        check(re.fullmatch(r'\d{4}-\d{2}-\d{2}',r['accessed_date']) is not None,f'Invalid access date: {tid}')
        for field,prefix,known in [('vts_id','VTS',vids),('candidate_vts_ids','VTS',vids),('vrs_id','VRS',rids),('vts_source_id','SRC',sids),('reporting_source_id','SRC',sids),('candidate_source_ids','SRC',sids)]:
            for key in references(r[field],prefix):check(key in known,f'Dangling reference: {tid}/{field}/{key}')
        check((ROOT/r['audit_path']).is_file(),f'Missing evidence audit: {tid}')
        if r['recorded_review_status']=='pass1-recorded':
            check(r['review_status']=='pass1-recorded' and r['readiness_status']=='First pass only',f'First pass improperly promoted: {tid}')
        if r['quality_flags']:check(r['review_status']!='audited',f'Open issues marked audited: {tid}')
        if r['review_status']=='audited':check(r['association_status']!='Unresolved',f'Unresolved final classification: {tid}')
    for s in vts:
        for sid in references(s['source_ids'],'SRC'):check(sid in sids,f"Missing service source: {s['vts_id']}/{sid}")
        check(bool(s['entity_kind']),f"Missing service type: {s['vts_id']}")
    for r in reports:
        for sid in references(r['source_ids'],'SRC'):check(sid in sids,f"Missing scheme source: {r['vrs_id']}/{sid}")
        check(bool(r['imo_ref'])==(r['adoption_scope']=='IMO-adopted baseline'),f"National ID represented as IMO: {r['vrs_id']}")
    relkeys=[]
    for rel in relations:
        check(rel['tss_id'] in tids,'Dangling relationship subject')
        check(rel['target_id'] in vids|rids,'Dangling relationship object')
        for sid in references(rel['source_ids'],'SRC'):check(sid in sids,'Dangling relationship source')
        relkeys.append((rel['tss_id'],rel['target_id'],rel['relationship_type']))
    check(len(relkeys)==len(set(relkeys)),'Duplicate relationship')
    expected_rel={(r['tss_id'],target,kind) for r in rows for field,prefix,kind in [('vts_id','VTS','recorded_vts_association'),('vrs_id','VRS','recorded_reporting_association'),('candidate_vts_ids','VTS','candidate_service_to_check')] for target in references(r[field],prefix)}
    check(set(relkeys)==expected_rel,'Relationship table is stale')
    expected_gaps={r['tss_id'] for r in rows if r['quality_flags']}
    check({r['tss_id'] for r in gaps if r['tss_id']}==expected_gaps,'Gaps table is stale')
    check(len(unique(batch,'batch_id','batch index'))==45,'Expected 45 batches')
    for b in batch:
        members=[r for r in rows if r['batch_id']==b['batch_id']]
        check(len(members)==int(b['records']),f"Batch count drift: {b['batch_id']}")
        check(sum(bool(r['quality_flags']) for r in members)==int(b['follow_up_records']),f"Batch flags drift: {b['batch_id']}")
        content=(ROOT/'research/batches_imo2025'/f"{b['batch_id']}.md").read_text()
        found=re.findall(r'^\| (TSS-\d{4}) \|',content,re.M)
        check(set(found)=={r['tss_id'] for r in members} and len(found)==len(members),'Batch view out of sync')
    _,subset=table('data/current/B20_B29_Association_Rows.csv')
    check(len(subset)==50 and all(r==mapping[r['tss_id']] for r in subset),'Compatibility subset out of sync')
    source_md=(ROOT/'sources/SOURCE_REGISTER.md').read_text()
    source_keys=re.findall(r'^### (SRC-\d+)\b',source_md,re.M)
    check(len(source_keys)==len(set(source_keys)) and set(source_keys)==sids,'Source MD/CSV mismatch')
    summary=json.loads((ROOT/'audits/repository_review_20260930/summary.json').read_text())
    check(summary['master_rows_after']==len(rows),'Summary row count drift')
    check(summary['service_records_after']==len(vts),'Summary service count drift')
    check(summary['reported_classifications_after']==dict(collections.Counter(r['association_status'] for r in rows)),'Summary classification drift')
    check(summary['records_requiring_follow_up']==len(expected_gaps),'Summary gap count drift')
    check(not summary['full_required_vts_register'] and not summary['publication_ready'],'Unjustified completeness flag')
    return {'structural_validation':'PASS','master_records':len(rows),'service_records':len(vts),
            'reporting_schemes':len(reports),'source_definitions':len(sources),
            'records_requiring_follow_up':len(expected_gaps),'operational_verification':'NOT CERTIFIED BY THIS VALIDATOR'}


if __name__=='__main__':
    try:
        print(json.dumps(validate(),indent=2))
    except (ValueError,csv.Error,KeyError,FileNotFoundError) as exc:
        print(f'VALIDATION FAILED: {exc}',file=sys.stderr)
        raise SystemExit(1)
