#!/usr/bin/env python3
"""Apply a bounded, row-hash-guarded B12 research update. No other TSS is edited.

Run from a checkout containing the corresponding reviewed evidence bundle.
The script stops if a target record changed, rather than replacing concurrent work.
The historical repository-repair script is deliberately not rerun.
"""
from __future__ import annotations
import csv, hashlib, io, json, re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / 'research/stage2/b12_recheck_20260930'
MASTER = 'data/current/TSS_VTS_MRS_Association_Register.csv'
AUDIT = 'audits/stage2/B12_Recheck_20260930.md'
TARGETS = {f'TSS-{n:04d}' for n in range(56,61)}
CHANGED: list[str] = []

def digest(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(',',':')).encode()).hexdigest()

def read_table(path: str) -> tuple[list[str], list[dict[str,str]]]:
    with (ROOT/path).open(encoding='utf-8-sig', newline='') as stream:
        raw=list(csv.reader(stream, strict=True))
    if not raw or len(raw[0])!=len(set(raw[0])):
        raise ValueError(f'Invalid header: {path}')
    if any(len(row)!=len(raw[0]) for row in raw[1:]):
        raise ValueError(f'Unequal field counts: {path}')
    return raw[0],[dict(zip(raw[0], row)) for row in raw[1:]]

def put(path: str, content: str) -> None:
    p=ROOT/path
    if not p.exists() or p.read_text(encoding='utf-8')!=content:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding='utf-8')
        CHANGED.append(path)

def write_table(path: str, header: list[str], rows: list[dict[str,str]]) -> None:
    out=io.StringIO(newline='')
    writer=csv.DictWriter(out, fieldnames=header, lineterminator='\n', extrasaction='raise')
    writer.writeheader(); writer.writerows(rows)
    put(path,out.getvalue())

def refs(value: str, prefix: str) -> list[str]:
    return re.findall(rf'\b{prefix}-\d+\b',value)

def run() -> None:
    marker=EVIDENCE/'application_checks.json'
    if marker.exists():
        raise RuntimeError('B12 update already applied. Do not rerun a dated research migration.')
    header,rows=read_table(MASTER)
    before={r['tss_id']:dict(r) for r in rows}
    if len(before)!=224 or len(rows)!=224:
        raise ValueError('The master must have exactly 224 unique baseline IDs.')
    patch=json.loads((EVIDENCE/'master_patch.json').read_text())['records']
    if {r['tss_id'] for r in patch}!=TARGETS:
        raise ValueError('Unexpected target set.')
    source_head,sources=read_table('sources/SOURCE_REGISTER.csv')
    source_map={r['source_id']:r for r in sources}
    source_updates=json.loads((EVIDENCE/'source_patch.json').read_text())
    # Validate every guard before writing anything.
    for p in patch:
        if digest(before[p['tss_id']])!=p['expected_record_sha256']:
            raise RuntimeError(f"Target changed: {p['tss_id']}. Reconcile before applying.")
        if set(p['changes'])-set(header): raise ValueError('Unknown master columns.')
    for p in source_updates:
        if digest(source_map[p['source_id']])!=p['expected_record_sha256']:
            raise RuntimeError(f"Source changed: {p['source_id']}. Reconcile before applying.")
    protected={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest()
               for p in ROOT.rglob('*') if p.is_file() and (
                   re.search(r'B2[0-9](?:[_.-]|$)',p.name) or p.name=='B20_B29_Association_Rows.csv')}
    updates={r['tss_id']:r['changes'] for r in patch}
    for r in rows:
        if r['tss_id'] in updates:r.update(updates[r['tss_id']])
    after={r['tss_id']:r for r in rows}
    if any(after[k]!=v for k,v in before.items() if k not in TARGETS):
        raise ValueError('Unrelated master row changed.')
    write_table(MASTER,header,rows)
    # Refresh only existing source definitions; allocate no source IDs.
    for p in source_updates:source_map[p['source_id']].update(p['changes'])
    write_table('sources/SOURCE_REGISTER.csv',source_head,sources)
    md_path='sources/SOURCE_REGISTER.md';md=(ROOT/md_path).read_text()
    for p in source_updates:
        sid=p['source_id']; note=source_map[sid]
        pattern=rf'(^### {re.escape(sid)}\b[^\n]*\n)(.*?)(?=^### SRC-\d+\b|\Z)'
        m=re.search(pattern,md,re.M|re.S)
        if not m:raise ValueError(f'Missing source Markdown definition: {sid}')
        extra=('\n**B12 recheck, 30 September 2026:** '+note['review_verification']+'\n'
               'Rechecked locator: '+note['locator']+'\n\n')
        md=md[:m.end()]+extra+md[m.end():]
    put(md_path,md)
    # Reuse two existing services. No new identity is created.
    vh,services=read_table('data/current/VTS_Entity_Register.csv')
    for s in services:
        if s['vts_id']=='VTS-0044':
            s.update({'evidence_status':'Declared polygon recovered; positive associations confirmed for TSS-0058 to TSS-0060; partial coverage and datum caveats retained',
                'source_ids':'; '.join(dict.fromkeys(refs(s['source_ids'],'SRC')+['SRC-047','SRC-191','SRC-003'])),
                'identity_review':'Current official identity and three positive TSS associations checked on 30 September 2026',
                'candidate_tss_ids':'','guide_entry_status':'One existing service; three TSS associations; exact crossing points and entry drafting not publication-ready',
                'notes':s['notes']+' B12 recheck supersedes the former no-mapping status: Off Texel and Off Vlieland are partial; Vlieland North overlap is confirmed, exact north-west edge remains a precision issue.'})
        if s['vts_id']=='VTS-0025':
            s['candidate_tss_ids']='; '.join(dict.fromkeys(refs(s['candidate_tss_ids'],'TSS')+['TSS-0056','TSS-0057']))
            s['notes']+=' B12: supporting VHF 7 inbound reports confirmed from SRC-062, but no offshore TSS coverage/monitoring assertion is made.'
    write_table('data/current/VTS_Entity_Register.csv',vh,services)
    # Regenerate relationship rows for B12 only, preserving other rows and evidence.
    rh,relationships=read_table('data/current/TSS_Service_Relationships.csv')
    relationships=[r for r in relationships if r['tss_id'] not in TARGETS]
    for r in rows:
        if r['tss_id'] not in TARGETS:continue
        for field,prefix,kind,sfield in [('vts_id','VTS','recorded_vts_association','vts_source_id'),('vrs_id','VRS','recorded_reporting_association','reporting_source_id'),('candidate_vts_ids','VTS','candidate_service_to_check','candidate_source_ids')]:
            for target in refs(r[field],prefix):
                relationships.append({'tss_id':r['tss_id'],'target_id':target,'relationship_type':kind,
                  'review_status':r['readiness_status'],'source_ids':r[sfield],
                  'coverage_note':r['vts_coverage_type'] if prefix=='VTS' else r['reporting_boundary_basis'],'audit_path':AUDIT})
    write_table('data/current/TSS_Service_Relationships.csv',rh,relationships)
    gh,gaps=read_table('data/current/Research_Gaps.csv')
    gaps=[g for g in gaps if g['tss_id'] not in TARGETS]
    for tid in sorted(TARGETS):
        r=after[tid]
        if r['quality_flags']:
            gaps.append({'gap_id':'GAP-'+tid,'tss_id':tid,'batch_id':'B12','tss_name':r['tss_name'],
              'priority':'High' if r['association_status']=='Unresolved' else 'Review',
              'reason_codes':r['quality_flags'],'outstanding':r['unresolved_issue'],
              'source_context':AUDIT,'next_action':'Resolve the specific remaining authority/precision question in the dated B12 recheck; do not repeat identity screening.'})
    write_table('data/current/Research_Gaps.csv',gh,gaps)
    members=[after[t] for t in sorted(TARGETS)]; open_count=sum(bool(r['quality_flags']) for r in members)
    bh,batches=read_table('data/current/Batch_Status.csv')
    state=f'Rechecked: 3 positive VTS links, 2 unresolved; {open_count} follow-up records'
    for b in batches:
        if b['batch_id']=='B12':b.update({'records':'5','first_pass_only':'0','follow_up_records':str(open_count),'status':state})
    write_table('data/current/Batch_Status.csv',bh,batches)
    index_path='research/batches_imo2025/README.md'; index=(ROOT/index_path).read_text()
    new_line=f'| [B12](B12.md) | 5 | 0 | {open_count} | {state} |'
    index,n=re.subn(r'^\| \[B12\]\(B12\.md\) \|.*$',lambda m:new_line,index,flags=re.M)
    if n!=1:raise ValueError('Expected one B12 batch index row.')
    put(index_path,index)
    view=('# B12 Research Batch\n\n**Recheck:** 30 September 2026  \n**Status:** '+state+'  \n**Batch closure:** Not closed\n\n'
          'This view follows the master register. Positive associations do not close remaining boundary questions.\n\n'
          '| ID | TSS | IMO parent | Recorded classification | Coverage / readiness |\n|---|---|---|---|---|\n')
    for r in members:view+='| '+' | '.join([r['tss_id'],r['tss_name'],r['imo_parent_ref'],r['association_status'],r['vts_coverage_type']])+' |\n'
    view+='\n## Current evidence\n\n[B12 recheck audit](../../'+AUDIT+') supersedes the earlier B12 completion claim.\n\n'
    for r in members:
        view+='### '+r['tss_id']+'\n\n'+r['evidence_summary']+'\n\nSources: '+r['vts_source_id']+'.\n\n'
        view+='Outstanding: '+(r['unresolved_issue'] or 'No remaining association flag; operational publication checks still apply.')+'\n\n'
    put('research/batches_imo2025/B12.md',view)
    # Only the affected two candidate rows change; no whole-register reclassification.
    ch,candidates=read_table('data/current/Guide_Service_Candidates.csv')
    for c in candidates:
        if c['service_id'] not in {'VTS-0044','VTS-0025'}:continue
        linked=[r for r in rows if c['service_id'] in refs(r['vts_id'],'VTS')]
        proposed=[r for r in rows if c['service_id'] in refs(r['candidate_vts_ids'],'VTS')]
        c.update({'linked_tss_count':str(len(linked)),'linked_tss_ids':'; '.join(r['tss_id'] for r in linked),
           'candidate_tss_ids':'; '.join(r['tss_id'] for r in proposed),'open_link_reviews':str(sum(bool(r['quality_flags']) for r in linked))})
    write_table('data/current/Guide_Service_Candidates.csv',ch,candidates)
    old='audits/stage2/B12_Association_Audit.md'
    notice=('> Superseded by [B12 recheck, 30 September 2026](B12_Recheck_20260930.md). '
            'The copied Pass 4 paragraph about German Bight/Humber is not evidence for B12. Historical text is retained below.\n\n')
    put(old,notice+(ROOT/old).read_text())
    for p,h in protected.items():
        if hashlib.sha256((ROOT/p).read_bytes()).hexdigest()!=h:raise ValueError('Protected B20-B29 path changed: '+p)
    out=io.StringIO(newline='');w=csv.DictWriter(out,fieldnames=header,lineterminator='\n');w.writeheader();w.writerows(members)
    put('research/stage2/b12_recheck_20260930/B12_Association_Rows.csv',out.getvalue())
    summary={'scope':sorted(TARGETS),'master_rows':len(rows),'unchanged_other_tss_rows':219,
             'unchanged_b20_b29_rows':50,'protected_paths_checked':len(protected),
             'positive_vts_associations':3,'unresolved_vts_associations':2,'follow_up_records':open_count,
             'new_service_ids':0,'new_source_ids':0,'batch_fully_closed':False,'changed_paths':CHANGED.copy(),
             'master_sha256_after':hashlib.sha256((ROOT/MASTER).read_bytes()).hexdigest()}
    marker.write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(summary,indent=2))

if __name__=='__main__':run()
