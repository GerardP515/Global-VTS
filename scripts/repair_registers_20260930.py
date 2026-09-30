#!/usr/bin/env python3
"""One-off, hash-guarded recovery of the 30 September 2026 research register.

This repairs storage and applies recorded project decisions. It is not a new
worldwide operational verification. Original bytes are archived before writes.
Run from the repository root. A completed run cannot be applied twice.
"""
from __future__ import annotations
import collections
import csv
import hashlib
import io
import json
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATE = '2026-09-30'
AUDIT = 'audits/repository_review_20260930'
MARKER = f'{AUDIT}/summary.json'
MASTER = 'data/current/TSS_VTS_MRS_Association_Register.csv'
SPLIT = 'data/current/B20_B29_Association_Rows.csv'
VTS = 'data/current/VTS_Entity_Register.csv'
SOURCES = 'sources/SOURCE_REGISTER.md'
BASE = 'data/authoritative/IMO_2025_Individual_TSS_Inventory.csv'
PARENTS = 'data/authoritative/IMO_2025_Part_B_Parent_Inventory.csv'
IMO_REPORTING = 'data/authoritative/IMO_2025_Mandatory_Reporting_Systems.csv'
LEGACY = 'data/legacy/Global_VTS_TSS_Candidates_v0_2.csv'
CROSSWALK = 'research/reconciliation/TSS_Crosswalk_Legacy_v0_2_to_IMO_2025.csv'
DECISIONS = 'audits/stage2/Project_Decisions_2026-09-30.md'
EXPECTED = {'data/current/TSS_VTS_MRS_Association_Register.csv': 'aa7a6d5d5270ee14ca7f31a1f9630787c8e84b160287c52ff0048c3d6201ec83', 'data/current/B20_B29_Association_Rows.csv': '967491a594c2310c6f938afe1cbde0d9d0137241b0ddc8d4ec5b787be429e92f', 'data/current/VTS_Entity_Register.csv': '3466522ecbbd1135dcdd9d88f53e13fc10b2b636d30fb58404e659c9fd12ad3b', 'sources/SOURCE_REGISTER.md': '37430e94ed93a82c5f9ec0542144f7745e7e95f0843726c92d1cf1b09eb78274', 'data/authoritative/IMO_2025_Individual_TSS_Inventory.csv': '5bd1a56bc9a99a7ae8c57da6ed42e1dbf2f43923cb27dc18b23dea9421834268', 'data/authoritative/IMO_2025_Part_B_Parent_Inventory.csv': '2dfafb855ca8f43bdc336e08e88de4aba561ce0e68f3e6b645ee5ac6bf6cc6b9', 'data/authoritative/IMO_2025_Mandatory_Reporting_Systems.csv': 'f5ed95a1a466513f6a7d0ecbed5fb0c546b53f3140607d87ffa142ce27dce0ed', 'data/legacy/Global_VTS_TSS_Candidates_v0_2.csv': '378d7158405b707ba4267b40d2a39ad63baf9dbbe00cdfe7cbdcca447fde6d7a', 'research/reconciliation/TSS_Crosswalk_Legacy_v0_2_to_IMO_2025.csv': '60da11b9b89726532420082fee38e2a2dd1a2bfe60c3ffa3476c39698ccb419f', 'audits/stage2/Project_Decisions_2026-09-30.md': 'c0953936f87353fedecd1bb2d39288ba097cdc80b599034327433bbba0ae333f'}
REGIONS = {
 'British Isles and southern North Sea':'BIS','Norway and Iceland':'NOI',
 'Baltic Sea and approaches':'BAL','North Sea continental coast':'NSC',
 'France, Iberia and Canary Islands':'FIC','Mediterranean and Black Seas':'MED',
 'Southern Africa':'SAF','Red Sea and Arabian region':'RSA',
 'Indian Ocean and South Asia':'IOS','Malacca, Singapore and Indonesia':'MSI',
 'China Sea and China':'CSC','North-west Pacific':'NWP','Australia':'AUS',
 'North America Pacific coast':'NPC','Central and South America Pacific coast':'CAP',
 'Caribbean, Gulf of Mexico and Panama':'CGP','North America Atlantic coast':'NAC'}
CHANGES: set[str] = set()
BEFORE: dict[str, bytes] = {}
REPAIRS: list[dict] = []


def text(path: str) -> str:
    return (ROOT/path).read_text(encoding='utf-8-sig')


def put(path: str, content: str | bytes) -> None:
    p = ROOT/path
    value = content.encode('utf-8') if isinstance(content, str) else content
    if p.exists() and p.read_bytes() == value:
        return
    if p.exists() and path not in BEFORE:
        BEFORE[path] = p.read_bytes()
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(value)
    CHANGES.add(path)


def strict_table(path: str) -> tuple[list[str], list[dict[str, str]]]:
    data = list(csv.reader(io.StringIO(text(path)), strict=True))
    if not data or not data[0] or len(set(data[0])) != len(data[0]):
        raise ValueError(f'Invalid header: {path}')
    if any(len(row) != len(data[0]) for row in data[1:]):
        raise ValueError(f'Invalid CSV width: {path}')
    return data[0], [dict(zip(data[0], row)) for row in data[1:]]


def write_table(path: str, fields: list[str], rows: list[dict]) -> None:
    output = io.StringIO(newline='')
    writer = csv.DictWriter(output, fields, lineterminator='\n', extrasaction='raise')
    writer.writeheader()
    for row in rows:
        writer.writerow({k: '' if row.get(k) is None else row.get(k, '') for k in fields})
    put(path, output.getvalue())


def ids(value: str, prefix: str) -> list[str]:
    return list(dict.fromkeys(re.findall(rf'\b{prefix}-\d+\b', value)))


def recover() -> tuple[list[str], list[dict], dict]:
    result = []
    fragments = {}
    headers = []
    for path in [MASTER, SPLIT]:
        # Deliberately limited to this corrupted snapshot. Future writes must use csv.DictWriter.
        chunks = re.split(r'(?m)(?=^TSS-\d{4},)', text(path))
        header = next(csv.reader(io.StringIO(chunks[0]), strict=True))
        headers.append(header)
        for chunk in chunks[1:]:
            parsed = list(csv.reader(io.StringIO(chunk), strict=True))
            row = parsed[0]
            key = row[0]
            if len(parsed) > 1:
                if key not in {'TSS-0046', 'TSS-0047'}:
                    raise ValueError(f'Unexpected continuation records at {key}')
                fragments[key] = parsed[1:]
            if len(row) == 28:
                if key in {'TSS-0033', 'TSS-0034', 'TSS-0035'}:
                    row[22:24] = [' '.join(row[22:24])]
                    reason = 'Joined two evidence-summary fields; neither narrative was discarded.'
                else:
                    if row[18] != '':
                        raise ValueError(f'Unexpected non-empty surplus column: {key}')
                    del row[18]
                    reason = 'Removed surplus empty field before reporting_boundary_basis.'
                REPAIRS.append({'tss_id':key, 'input_path':path, 'repair':reason})
            if len(row) != len(header):
                raise ValueError(f'Unexpected row width: {key}: {len(row)}')
            item = dict(zip(header, row))
            item['record_origin'] = path
            result.append(item)
    assert headers[0] == headers[1] and len(headers[0]) == 27
    assert len(result) == len({r['tss_id'] for r in result}) == 224
    assert len(REPAIRS) == 61 and len(fragments) == 2
    return headers[0], sorted(result, key=lambda r:r['tss_id']), fragments


def source_section(key: str, title: str, url: str, authority: str, use: str,
                   verification: str='Opened during the repository review on 30 September 2026.') -> str:
    return (f'\n\n### {key} — {title}\n\n- Authority: {authority}.\n- URL: {url}\n'
            f'- Evidence class: Primary authority material.\n- Verification: {verification}\n- Use: {use}\n')


def source_rows(content: str) -> list[dict]:
    out = []
    for m in re.finditer(r'(?ms)^### (SRC-\d+)\s+[^\n]*?(?:—|–|-)\s*([^\n]+)\n(.*?)(?=^### |\Z)', content):
        body=m.group(3)
        def value(label):
            match=re.search(rf'(?im)^- {re.escape(label)}:\s*(.*)$', body)
            return match.group(1).strip() if match else ''
        urls=re.findall(r'https?://[^\s<>]+', value('URL'))
        tier=value('Evidence class')
        if 'data/authoritative/' in m.group(2) or value('URL') == 'repository file':
            tier='Project-derived inventory; not independent primary evidence'
        out.append({'source_id':m.group(1),'title':m.group(2),'authority':value('Authority'),
                    'url':'; '.join(urls),'evidence_class':tier,
                    'source_date':value('Edition or date') or value('Edition') or value('Date') or value('Updated'),
                    'last_recorded_access':value('Accessed'),
                    'review_verification':value('Verification') or 'Carried forward; URL not reopened in this repository review.',
                    'locator':value('Locator'), 'use':value('Use')})
    return sorted(out,key=lambda r:int(r['source_id'].split('-')[1]))


def main() -> None:
    if (ROOT/MARKER).exists():
        print('Repair already applied. No files changed.')
        return
    for path, digest in EXPECTED.items():
        actual=hashlib.sha256((ROOT/path).read_bytes()).hexdigest()
        if actual!=digest:
            raise SystemExit(f'Input changed since review: {path}. Reconcile before running; no files written.')
    fields, rows, fragments = recover()
    by_id={r['tss_id']:r for r in rows}
    baseline_fields, baseline = strict_table(BASE)
    parent_fields, parents = strict_table(PARENTS)
    assert len(baseline)==224 and len(parents)==164
    assert set(by_id)=={r['canonical_id'] for r in baseline}
    vt_fields, services = strict_table(VTS)
    assert len(services)==40 and len({r['vts_id'] for r in services})==40
    original_counts=dict(collections.Counter(r['association_status'] for r in rows))

    # Repair legacy aliases without using their provisional IDs as current identity.
    legacy_raw=text(LEGACY)
    start=legacy_raw.find('index,Record ID')
    assert start>=0
    legacy_csv=list(csv.reader(io.StringIO(legacy_raw[start:]), strict=True))
    assert len(legacy_csv)==171 and all(len(r)==20 for r in legacy_csv)
    legacy_fields=legacy_csv[0][1:]
    legacy=[dict(zip(legacy_fields,r[1:])) for r in legacy_csv[1:]]
    for path in [LEGACY,'data/current/Global_VTS_TSS_Candidates_v0_2.csv']:
        write_table(path,legacy_fields,legacy)
    legacy_regions={r['Record ID']:REGIONS[r['Region']] for r in legacy}
    _,crosswalk=strict_table(CROSSWALK)
    region_options=collections.defaultdict(set)
    for entry in crosswalk:
        if entry['legacy_id'] in legacy_regions:
            region_options[entry['canonical_id']].add(legacy_regions[entry['legacy_id']])
    # The one new source candidate is Jazan, in the existing Red Sea editorial group.
    region_options['TSS-0127'].add('RSA')
    for r in baseline:
        choices=region_options[r['canonical_id']]
        assert len(choices)==1,(r['canonical_id'],choices)
        r['project_region_code']=next(iter(choices))
    baseline_map={r['canonical_id']:r for r in baseline}
    for r in parents:
        regions={b['project_region_code'] for b in baseline if b['imo_parent_ref']==r['imo_ref']}
        r['project_region_code']='; '.join(sorted(regions))
    write_table(BASE,baseline_fields,baseline)
    write_table(PARENTS,parent_fields,parents)

    # Restore six source definitions already cited by current records.
    src=text(SOURCES)
    restore=[
     ('SRC-008','BELTREP reporting procedures','https://www.forsvaret.dk/da/organisation/soevaernet/civile-opgaver/beltrep/','Danish Defence / Royal Danish Navy','Existing BELTREP operating source'),
     ('SRC-009','About SOUNDREP','https://www.sjofartsverket.se/en/services/maritime-traffic-information/soundrep/soundrep-information/about-soundrep/','Swedish Maritime Administration','Existing Sound VTS / SOUNDREP operating source'),
     ('SRC-011','GOFREP Area: Master’s Guide','https://mastersguide.fintraffic.fi/en/gofrep-area','Fintraffic','Existing GOFREP identity, boundaries and centre source'),
     ('SRC-015','Vessel Traffic Service','https://www.forsvaret.dk/da/organisation/soevaernet/nationalt-maritimt-operationscenter/vts/','Danish Defence / Royal Danish Navy','Existing Great Belt, Sound and Fehmarnbelt service source'),
     ('SRC-020','Resolution MSC.332(90): BELTREP','https://wwwcdn.imo.org/localresources/en/KnowledgeCentre/IndexofIMOResolutions/MSCResolutions/MSC.332(90).pdf','International Maritime Organization','Existing BELTREP adopted instrument'),
     ('SRC-021','Resolution MSC.314(88): SOUNDREP','https://www.sjofartsverket.se/globalassets/tjanster/sjotrafiktjanster/msc.31488.pdf','IMO; Swedish Maritime Administration host','Existing SOUNDREP adopted instrument')]
    for key,title,url,authority,use in restore:
        assert not re.search(rf'^### {key}\b',src,re.M)
        src+=source_section(key,title,url,authority,use,
               'Definition recovered from the v0.2 audit/source history. Not newly verified by this repair.')
    new_sources=[
     ('SRC-194','South Åland Sea TSS: Master’s Guide','https://mastersguide.fintraffic.fi/en/south-aland-sea-tss','Fintraffic','South Åland Sea monitoring by Åland Sea Traffic from the Western Finland VTS centre; decision 1 applies.'),
     ('SRC-195','New VTS Off Texel operational from 3 November 2025','https://www.rijkswaterstaat.nl/nieuws/archief/2025/10/nieuw-vts-gebied-off-texel-vanaf-3-november-operationeel','Rijkswaterstaat','Current service identity and commencement; not proof of whole-TSS coverage.'),
     ('SRC-196','Container-ship advice and Off Texel VTS','https://kustwacht.nl/beroepsvaart/advies-voor-containerschepen-bij-waddeneilanden/','Netherlands Coastguard','Current authority confirmation of Off Texel; limits of route coverage require component mapping.'),
     ('SRC-197','VTS Centres: international-waters monitoring','https://www.fintraffic.fi/fi/node/255','Fintraffic','Helsinki Traffic monitors northern GOFREP from the Gulf of Finland VTS centre; Åland Sea Traffic from Western Finland.'),
     ('SRC-198','Monitoring international waters','https://www.fintraffic.fi/sv/node/254','Fintraffic','GOFREP centre allocation and four named TSS; South Åland Sea has no obligatory reporting system.')]
    for args in new_sources:
        assert not re.search(rf'^### {args[0]}\b',src,re.M)
        src+=source_section(*args)
    src='> Current machine-readable index: `SOURCE_REGISTER.csv`. Access history is not a fresh link-validation claim.\n\n'+src
    put(SOURCES,src)
    indexed_sources=source_rows(src)
    source_ids={r['source_id'] for r in indexed_sources}
    assert len(indexed_sources)==len(source_ids)
    write_table('sources/SOURCE_REGISTER.csv',list(indexed_sources[0]),indexed_sources)

    # Keep physical VTS areas, sectors and project-eligible monitoring distinguishable.
    extra_vt=['entity_kind','counting_basis','identity_review','candidate_tss_ids','guide_entry_status']
    for s in services:
        s.update({k:'' for k in extra_vt})
        s['entity_kind']='VTS service or area (as recorded; hierarchy not fully reconciled)'
        if s['vts_id'] in {'VTS-0018','VTS-0019','VTS-0020','VTS-0021'}:
            s['entity_kind']='VTS sector/service; centre grouping requires editorial review'
        if s['vts_id']=='VTS-0039':
            s['entity_kind']='Monitoring/information service from a VTS centre'
        if s['vts_id']=='VTS-0038':
            s['entity_kind']='Official port traffic centre'
        s['counting_basis']='Recorded project decisions; not a count of distinct statutory VTS areas'
        s['identity_review']='Carried forward; not independently revalidated during this repository repair'
        s['guide_entry_status']='Not scoped; service record is not a final guide entry'
    additions=[
      {'vts_id':'VTS-0043','vts_name':'Åland Sea Traffic','area_label':'South Åland Sea TSS',
       'authority_or_jurisdiction':'Fintraffic Vessel Traffic Services Ltd','centre':'Western Finland Vessel Traffic Centre',
       'sectors':'South Åland Sea monitoring','service_status':'Operational monitoring',
       'evidence_status':'Current operator explicitly names the TSS and VTS centre',
       'source_ids':'SRC-194; SRC-197; SRC-198',
       'source_urls':'https://mastersguide.fintraffic.fi/en/south-aland-sea-tss; https://www.fintraffic.fi/fi/node/255; https://www.fintraffic.fi/sv/node/254',
       'accessed_date':DATE,'notes':'Counted under decision 1. Not represented as a designated statutory VTS area.',
       'entity_kind':'Monitoring/information service from a VTS centre','counting_basis':'Project decision 1',
       'identity_review':'Current operator checked in repository review','candidate_tss_ids':'TSS-0012','guide_entry_status':'Candidate; not a finished guide entry'},
      {'vts_id':'VTS-0044','vts_name':'VTS Off Texel','area_label':'Declared Off Texel area; not the entire Texel/Vlieland routeing system',
       'authority_or_jurisdiction':'Royal Netherlands Navy harbourmaster / Rijkswaterstaat','centre':'Verkeerscentrale Den Helder',
       'sectors':'VTS Off Texel','service_status':'Operational since 3 November 2025',
       'evidence_status':'Current official service confirmed; individual TSS boundary reconciliation pending',
       'source_ids':'SRC-195; SRC-196; SRC-192; SRC-191',
       'source_urls':'https://www.rijkswaterstaat.nl/nieuws/archief/2025/10/nieuw-vts-gebied-off-texel-vanaf-3-november-operationeel; https://kustwacht.nl/beroepsvaart/advies-voor-containerschepen-bij-waddeneilanden/',
       'accessed_date':DATE,'notes':'Known service missing from the entity register. Do not infer full coverage of TSS-0058 to TSS-0060.',
       'entity_kind':'Designated VTS area','counting_basis':'Current authority service description',
       'identity_review':'Current official identity checked; component extent unresolved',
       'candidate_tss_ids':'TSS-0058; TSS-0059; TSS-0060','guide_entry_status':'Candidate; scope/extent check required'},
      {'vts_id':'VTS-0045','vts_name':'Helsinki Traffic (GOFREP monitoring)',
       'area_label':'Northern GOFREP monitoring responsibility','authority_or_jurisdiction':'Fintraffic Vessel Traffic Services Ltd',
       'centre':'Gulf of Finland Vessel Traffic Centre','sectors':'North of the Central Reporting Line',
       'service_status':'Operational monitoring','evidence_status':'Operator names the VTS centre and monitored GOFREP area',
       'source_ids':'SRC-197; SRC-198; SRC-011','source_urls':'https://www.fintraffic.fi/fi/node/255; https://www.fintraffic.fi/sv/node/254; https://mastersguide.fintraffic.fi/en/gofrep-area',
       'accessed_date':DATE,'notes':'Decision 1 includes monitoring from a VTS centre. Not Helsinki VTS, and not a new reporting scheme.',
       'entity_kind':'Monitoring/information service from a VTS centre','counting_basis':'Project decision 1',
       'identity_review':'Current operator checked; responsibility limited to northern monitored portions',
       'candidate_tss_ids':'TSS-0004; TSS-0005; TSS-0006; TSS-0007','guide_entry_status':'Candidate; may share GOFREP guide entry with other centres'}]
    assert not {s['vts_id'] for s in services} & {s['vts_id'] for s in additions}
    services+=additions
    services.sort(key=lambda r:r['vts_id'])
    write_table(VTS,vt_fields+extra_vt,services)
    service_map={s['vts_id']:s for s in services}

    # One register for IMO and named national schemes. Internal IDs do not imply IMO adoption.
    _,imo_reports=strict_table(IMO_REPORTING)
    report_fields=['vrs_id','scheme_name','adoption_scope','imo_ref','applicability','source_ids','evidence_status','notes']
    reporting=[]
    for r in imo_reports:
        title=r['parent_title']; short=re.search(r'\[([^]]+)\]',title)
        key=r['reporting_id']
        reporting.append({'vrs_id':key,'scheme_name':short.group(1) if short else title,
          'adoption_scope':'IMO-adopted baseline','imo_ref':r['imo_ref'],
          'applicability':'Scheme-specific; verify governing requirements before operational use',
          'source_ids':'SRC-003','evidence_status':'2025 source inventory; later amendments not exhaustively reconciled',
          'notes':title})
    national=[('VRS-0024','SUNDAREP',[153]),('VRS-0025','LOMBOKREP',[154]),
              ('VRS-0026','MASTREP',list(range(158,162))),('VRS-0027','CHILREP',list(range(187,195))),
              ('VRS-0028','Strait of Magellan reporting',[194])]
    for key,name,numbers in national:
        related=[by_id[f'TSS-{n:04d}'] for n in numbers]
        reporting.append({'vrs_id':key,'scheme_name':name,'adoption_scope':'National scheme; internal project ID',
          'imo_ref':'','applicability':related[0]['reporting_scheme_name'],
          'source_ids':'; '.join(sorted({sid for r in related for sid in ids(r['reporting_source_id'],'SRC')})),
          'evidence_status':'Identity recovered from existing audited research; not freshly legally reverified',
          'notes':'Project decisions 3/3a apply. Vessel-flag and geographical qualifications remain in the TSS records.'})
        for r in related:
            r['vrs_id']='; '.join(dict.fromkeys(ids(r['vrs_id'],'VRS')+[key]))
    write_table('data/current/Reporting_Scheme_Register.csv',report_fields,reporting)
    reporting_ids={r['vrs_id'] for r in reporting}

    # Original assertions remain visible. A clean CSV does not turn a first pass into an audit.
    extra=['batch_id','recorded_association_status','recorded_review_status','readiness_status',
           'vts_association_state','reporting_association_state','vts_coverage_type','candidate_vts_ids','candidate_source_ids',
           'quality_flags','review_note','audit_path','voluntary_reporting_notes','record_origin','last_integrity_check']
    flags_by_id={}
    for r in rows:
        b=baseline_map[r['tss_id']]; n=int(r['tss_id'].split('-')[1]); batch=(n-1)//5+1
        old_status=r['association_status']; old_review=r['review_status']
        r['recorded_association_status']=old_status;r['recorded_review_status']=old_review
        r['tss_name']=b['display_name'];r['imo_parent_ref']=b['imo_parent_ref'];r['region_code']=b['project_region_code']
        r['batch_id']=f'B{batch:02d}';r['last_integrity_check']=DATE
        r['audit_path']=f'audits/IMO2025_B{batch:02d}_Audit.md' if old_review=='pass1-recorded' else f'audits/stage2/B{batch:02d}_Association_Audit.md'
        r['review_note']='Storage repaired and evidence consistency checked. Historical source assertions are not a fresh worldwide operational verification.'
        r['vts_coverage_type']='As recorded; full/partial extent not standardised'
        r['candidate_vts_ids']='';r['candidate_source_ids']=''
        if not r['mandatory_reporting'].strip():r['mandatory_reporting']='Unresolved'
        voluntary=r['voluntary_reporting'];r['voluntary_reporting_notes']=''
        if voluntary not in {'Yes','No','Unresolved'}:
            r['voluntary_reporting_notes']=voluntary
            r['voluntary_reporting']='Yes' if voluntary.startswith('Yes') else 'No' if voluntary.startswith('No') else 'Unresolved'
        flags=[]
        if old_review=='pass1-recorded': flags.append('FIRST_PASS_NOT_AUDITED')
        if old_status=='Unresolved':flags.append('ASSOCIATION_UNRESOLVED')
        if r['unresolved_issue'].strip():flags.append('OPEN_SOURCE_OR_BOUNDARY_ISSUE')
        if old_status=='Neither confirmed':flags.append('NEGATIVE_FINDING_REQUIRES_SCOPE_RECHECK')
        if n<=50 and (r['mandatory_reporting']=='No'):
            flags.append('NATIONAL_REPORTING_SCREEN_NOT_DEMONSTRATED')
        if 'VTS' in old_status and (not r['vts_id'] or not r['vts_source_id']):flags.append('POSITIVE_VTS_EVIDENCE_INCOMPLETE')
        if 'MRS' in old_status and (not r['vrs_id'] or not r['reporting_source_id']):flags.append('POSITIVE_REPORTING_EVIDENCE_INCOMPLETE')
        # Missing evidence is a gap, not permission to manufacture a citation.
        for field in ['vts_source_id','reporting_source_id']:
            for sid in ids(r[field],'SRC'):
                assert sid in source_ids,(r['tss_id'],sid)
        for key in ids(r['vts_id'],'VTS'):assert key in service_map,(r['tss_id'],key)
        for key in ids(r['vrs_id'],'VRS'):assert key in reporting_ids,(r['tss_id'],key)
        r['vts_association_state']='Recorded positive' if r['vts_id'] else 'Not established'
        r['reporting_association_state']='Recorded positive' if r['mandatory_reporting']=='Yes' else 'Not established'
        if old_review=='pass1-recorded':
            if r['vts_id']:r['vts_association_state']='First-pass lead'
            if r['mandatory_reporting']=='Yes':r['reporting_association_state']='First-pass lead'
        if n in {4,5,6,7}:
            s=service_map['VTS-0045']
            r['association_status']='VTS + MRS';r['vts_id']=s['vts_id'];r['vts_name']=s['vts_name']
            r['vts_authority']=s['authority_or_jurisdiction'];r['vts_centre']=s['centre'];r['vts_sector']=s['sectors']
            r['vts_source_id']='SRC-197; SRC-198; SRC-011';r['vts_source_url']=s['source_urls']
            r['vts_boundary_basis']='Fintraffic assigns Helsinki Traffic the northern GOFREP area. The Central Reporting Line passes through these named TSS separation zones. Decision 1 counts monitoring from the VTS centre; no whole-TSS statutory VTS designation is asserted.'
            r['vts_association_state']='Confirmed under project decision 1'
            r['vts_coverage_type']='Monitoring of northern GOFREP portion; not whole-TSS designated VTS coverage'
            r['review_note']='Policy correction: monitoring from the Gulf of Finland VTS centre counts under decision 1. Helsinki Traffic remains distinct from Helsinki VTS and from GOFREP as a reporting scheme.'
            r['evidence_summary']=r['review_note']+' '+r['reporting_boundary_basis']
            r['accessed_date']=DATE
        if n==12:
            s=service_map['VTS-0043']
            r['association_status']='VTS only';r['vts_id']=s['vts_id'];r['vts_name']=s['vts_name']
            r['vts_authority']=s['authority_or_jurisdiction'];r['vts_centre']=s['centre'];r['vts_sector']=s['sectors']
            r['vts_source_id']=s['source_ids'];r['vts_source_url']=s['source_urls']
            r['vts_boundary_basis']='Fintraffic explicitly names South Åland Sea TSS, Åland Sea Traffic and the Western Finland VTS centre. Monitoring qualifies under project decision 1.'
            r['vts_association_state']='Confirmed under project decision 1';r['vts_coverage_type']='Monitoring from VTS centre, not designated VTS area'
            r['review_note']='Corrected earlier exclusion: project decision 1 expressly permits this monitoring service. Operator states no obligatory reporting system.'
            r['evidence_summary']=r['review_note'];r['accessed_date']=DATE
            flags=[f for f in flags if f not in {'NEGATIVE_FINDING_REQUIRES_SCOPE_RECHECK','NATIONAL_REPORTING_SCREEN_NOT_DEMONSTRATED'}]
        if n in {58,59,60}:
            r['candidate_vts_ids']='VTS-0044';r['candidate_source_ids']='SRC-195; SRC-196'
            r['review_note']='Current VTS Off Texel identity is confirmed. Earlier no-VTS lead is stale. Exact full/partial overlap and datum reconciliation remain open; no blanket coverage assertion has been substituted.'
            flags.append('KNOWN_CURRENT_SERVICE_COMPONENT_MAPPING_REQUIRED')
        if n in range(187,194):
            # Existing summary predates an approved CHILREP correction. Retain it in archived input.
            r['evidence_summary']='Recorded project decision 3a counts CHILREP with its flag/internal-water qualifications. '+r['reporting_scheme_name']+'. '+r['unresolved_issue']
            r['review_note']+=' Superseded wording calling CHILREP wholly voluntary has been removed; applicability has not been generalised.'
        r['quality_flags']='; '.join(dict.fromkeys(flags));flags_by_id[r['tss_id']]=flags
        r['readiness_status']='First pass only' if old_review=='pass1-recorded' else 'Review required' if flags else 'Association record reviewed; not publication-ready'
        r['review_status']='pass1-recorded' if old_review=='pass1-recorded' else 'reopened' if flags else 'audited'
    write_table(MASTER,fields+extra,rows)
    write_table(SPLIT,fields+extra,[r for r in rows if r['recorded_review_status']=='pass1-recorded'])

    # Derived relationship table: explicit positive assertions, with evidence stage attached.
    relationships=[]
    for r in rows:
        for column,prefix,kind,evidence in [('vts_id','VTS','recorded_vts_association','vts_source_id'),('vrs_id','VRS','recorded_reporting_association','reporting_source_id'),('candidate_vts_ids','VTS','candidate_service_to_check','candidate_source_ids')]:
            for target in ids(r[column],prefix):
                relationships.append({'tss_id':r['tss_id'],'target_id':target,'relationship_type':kind,
                  'review_status':r['readiness_status'],'source_ids':r[evidence],
                  'coverage_note':r['vts_coverage_type'] if prefix=='VTS' else r['reporting_boundary_basis'],
                  'audit_path':r['audit_path']})
    write_table('data/current/TSS_Service_Relationships.csv',list(relationships[0]),relationships)

    gaps=[]
    for r in rows:
        if r['quality_flags']:
            gaps.append({'gap_id':f"GAP-{r['tss_id']}",'tss_id':r['tss_id'],'batch_id':r['batch_id'],
              'tss_name':r['tss_name'],'priority':'High' if r['recorded_review_status']=='pass1-recorded' or r['association_status']=='Unresolved' else 'Review',
              'reason_codes':r['quality_flags'],'outstanding':r['unresolved_issue'] or ('Recheck negative finding against the approved broader project scope.' if r['recorded_association_status']=='Neither confirmed' else 'Complete recorded evidence gaps and national-scheme scope checks.'),
              'source_context':r['audit_path'],'next_action':'Complete authority/boundary review; update the master record and rerun validation.'})
    global_gaps=[
      ('POST_BASELINE_AMENDMENTS','Later IMO/national changes have not been reconciled systematically against the 2025 snapshot.'),
      ('NON_TSS_CENSUS','No worldwide national/ALRS/ITU reconciliation establishes non-TSS VTS coverage.'),
      ('GUIDE_ENTRY_DEDUPLICATION','Services, sectors, centres and editorial entries are not yet reconciled into a final publication count.'),
      ('REPORTING_APPLICABILITY','National-only, tanker-only and partial-overlap requirements need operational applicability checks.'),
      ('SOURCE_LINK_VERIFICATION','A source index is not a fresh verification of every URL or quoted claim.'),
      ('PUBLISHER_VIABILITY','Final illustration/page/workload and maintenance estimates remain outstanding.')]
    for key,note in global_gaps:
        gaps.append({'gap_id':'GAP-'+key,'tss_id':'','batch_id':'ALL','tss_name':'','priority':'High',
          'reason_codes':key,'outstanding':note,'source_context':'docs/RESEARCH_PLAN.md',
          'next_action':'Close this scope-wide gate before describing the register as complete.'})
    write_table('data/current/Research_Gaps.csv',list(gaps[0]),gaps)

    # Keep already-known non-TSS and monitoring leads visible without asserting current coverage.
    additional=[
     {'candidate_id':'ADD-001','name':'REEFVTS / REEFREP','legacy_id':'VTS-007','candidate_type':'Non-TSS or additional-area VTS/reporting',
      'source_context':'audits/Global_VTS_Inventory_v0_2_Audit.md; SRC-018','status':'Legacy authority-supported lead; current scope reconciliation pending',
      'reason':'TSS-led inventory alone does not demonstrate coverage of the Great Barrier Reef reporting/VTS area.'},
     {'candidate_id':'ADD-002','name':'Fehmarnbelt VTS','legacy_id':'VTS-008','candidate_type':'Temporary/voluntary VTS',
      'source_context':'Legacy v0.2 source history SRC-015/SRC-016','status':'Legacy service lead; current construction-phase limits/status need rechecking',
      'reason':'Do not drop a service merely because it is temporary, voluntary or absent from the 224 TSS links.'},
     {'candidate_id':'ADD-003','name':'Sweden Traffic','legacy_id':'','candidate_type':'Monitoring-service eligibility review',
      'source_context':'SRC-033; Project_Decisions_2026-09-30.md decision 1','status':'TSS monitoring recorded; eligibility as VTS-centre monitoring not established here',
      'reason':'Recheck before treating Swedish offshore TSS negative findings as final.'}]
    write_table('data/current/Additional_Coverage_Candidates.csv',list(additional[0]),additional)
    candidates=[]
    for s in services:
        linked=[r for r in rows if s['vts_id'] in ids(r['vts_id'],'VTS')]
        proposed=[r for r in rows if s['vts_id'] in ids(r['candidate_vts_ids'],'VTS')]
        candidates.append({'service_id':s['vts_id'],'service_name':s['vts_name'],'entity_kind':s['entity_kind'],
          'centre':s['centre'],'linked_tss_count':str(len(linked)),'linked_tss_ids':'; '.join(r['tss_id'] for r in linked),
          'candidate_tss_ids':'; '.join(r['tss_id'] for r in proposed),
          'open_link_reviews':str(sum(bool(r['quality_flags']) for r in linked)),
          'counting_basis':s['counting_basis'],'guide_entry_status':'Not final: shared centre, sector and multi-TSS grouping require editorial decision'})
    write_table('data/current/Guide_Service_Candidates.csv',list(candidates[0]),candidates)

    # Batch records become current views; original narratives and audits remain archived and linked.
    batch_rows=[]
    for batch in range(1,46):
        members=[r for r in rows if r['batch_id']==f'B{batch:02d}']
        first=all(r['recorded_review_status']=='pass1-recorded' for r in members)
        opened=sum(bool(r['quality_flags']) for r in members)
        state='First pass only' if first else f'Reviewed records; {opened} require follow-up' if opened else 'Association review recorded; publication checks pending'
        path=f'research/batches_imo2025/B{batch:02d}.md'
        previous=text(path)
        view=(f'# B{batch:02d} Research Batch\n\n**Repository review:** {DATE}  \n**Status:** {state}  \n'
              f'**Records:** {len(members)}  \n**Scope:** IMO 2025 source order\n\n'
              'The table below is generated from the master register. Old checkmarks do not close open evidence issues.\n\n'
              '| ID | TSS | IMO parent | Recorded classification | Current review status |\n|---|---|---|---|---|\n')
        for r in members:
            vals=[r['tss_id'],r['tss_name'],r['imo_parent_ref'],r['association_status'],r['readiness_status']]
            view+='| '+' | '.join(v.replace('|','\\|') for v in vals)+' |\n'
        view+='\n## Evidence and outstanding checks\n\n'
        for r in members:
            view+=(f"### {r['tss_id']}\n\nVTS: {r['vts_id'] or 'Not established'}. Reporting: {r['vrs_id'] or 'Not established'}.\n\n"
                   f"Review flags: {r['quality_flags'] or 'No structural/scope flag raised in this repository review'}.\n\n"
                   f"{r['unresolved_issue'] or r['review_note']}\n\n"
                   f"Prior evidence: [{Path(r['audit_path']).name}](../../{r['audit_path']}).\n\n")
        view+='## Historical research\n\nThe previous batch file is preserved in the pre-review archive. Audit narratives remain on their original paths.\n'
        put(path,view)
        batch_rows.append({'batch_id':f'B{batch:02d}','records':str(len(members)), 'first_pass_only':str(sum(r['recorded_review_status']=='pass1-recorded' for r in members)),
                           'follow_up_records':str(opened),'status':state})
    write_table('data/current/Batch_Status.csv',list(batch_rows[0]),batch_rows)
    idx='# IMO 2025 research batches\n\nCurrent status is derived from the master register, not historical PASS labels.\n\n'
    idx+='| Batch | TSS rows | First-pass only | Follow-up records | Status |\n|---|---:|---:|---:|---|\n'
    for r in batch_rows:
        idx+=f"| [{r['batch_id']}]({r['batch_id']}.md) | {r['records']} | {r['first_pass_only']} | {r['follow_up_records']} | {r['status']} |\n"
    put('research/batches_imo2025/README.md',idx)

    # Do not erase audit evidence. Add a precedence notice to historical audits/reports.
    notice=('> Repository review, 30 September 2026: historical research record. Current master fields, review flags and '
            '[repository audit](../repository_review_20260930/REVIEW.md) govern readiness. A previous PASS label is not a completeness certificate.\n\n')
    for p in sorted((ROOT/'audits/stage2').glob('*.md')):
        if p.name.startswith('Project_Decisions'):continue
        rel=p.relative_to(ROOT).as_posix()
        put(rel,notice+text(rel))
    block='audits/IMO2025_B20-B29_Block_Close.md'
    put(block,'> Superseded status note: all 50 first-pass rows are now integrated into the master CSV. They remain first-pass-only, not audited.\n\n'+text(block))

    policy='''# Stage 2 counting and completion rules

## Governing decisions

Apply `audits/stage2/Project_Decisions_2026-09-30.md` before older prompt language.
Monitoring from a VTS centre can count as a project service association outside statutory VTS limits.
Record that service type explicitly. Do not describe it as a statutory VTS area.
Official port traffic centres may qualify under decision 5.
National schemes count under decisions 3 and 3a, with vessel and geographical qualifications.
Routine reports within a VTS remain part of that VTS.

## Separate questions

Record the VTS relationship and reporting relationship independently.
An established reporting scheme does not prove either presence or absence of a VTS.
A first-pass lead is not an audited relationship.
A source-access failure is not an absence finding.
A broad distance description or overview diagram is not an exact boundary polygon.

## Existing category labels

`VTS only` and `MRS only` describe the positive relationships recorded so far.
They do not certify absence of an unresolved relationship on the other side.
`Neither confirmed` is retained as a historical research category, not proof that neither service exists.
Use the independent state fields, `readiness_status`, `quality_flags` and gaps register when counting completed work.
Never describe a batch as complete while its required follow-up remains open.

## Completion gates

1. Every baseline TSS has one valid master row.
2. Every asserted service/scheme has one canonical identity and evidence references.
3. Every TSS has been assessed under the same approved scope.
4. Current boundaries, applicability, conflicts and source gaps are resolved or explicitly accepted by the project owner.
5. Additional non-TSS VTS/reporting coverage has been checked against worldwide references and national lists.
6. Service, area, centre, sector and proposed guide-entry counts have been reconciled separately.

Only gate 1 and mechanical parts of gate 2 are closed by the repository repair.
No navigation instructions or final worldwide VTS total are authorised by a clean CSV.
'''
    put('docs/STAGE_2_COUNTING_AND_COMPLETION.md',policy)
    prompt='research/prompts/STAGE_2_TSS_VTS_REPORTING_ASSOCIATION_PROMPT.md'
    put(prompt,'> **30 September 2026 correction:** `docs/STAGE_2_COUNTING_AND_COMPLETION.md` and the recorded project decisions take precedence over contradictory wording below. Read both before starting.\n\n'+text(prompt))
    dictionary='docs/DATA_DICTIONARY.md'
    put(dictionary,text(dictionary)+'''\n\n## Repository review schema, 30 September 2026

The current master retains the original 27 fields and adds explicit provenance and readiness fields.
`recorded_association_status` and `recorded_review_status` preserve the pre-review findings.
`association_status` includes documented policy corrections; it is not a publication-readiness flag.
`review_status` is `pass1-recorded`, `reopened` or `audited`.
`readiness_status` distinguishes first-pass, follow-up and recorded association review.
`quality_flags` identify unresolved evidence, boundary, national-scheme and scope issues.
`candidate_vts_ids` are leads, never confirmed links.
`vts_coverage_type` distinguishes monitoring, partial coverage and unsettled extent.
`record_origin` and `audit_path` retain traceability.
`voluntary_reporting_notes` preserves qualified prose while the flag uses Yes/No/Unresolved.
The reporting register combines IMO and national identities without implying IMO adoption of national schemes.
The guide-service table counts service records only, not final VTS areas or editorial entries.
''')
    put('data/current/README.md','''# Current working registers

`TSS_VTS_MRS_Association_Register.csv` is the master: one row for each of 224 baseline TSS.
`B20_B29_Association_Rows.csv` is a generated compatibility subset, not a separate master.
`Global_VTS_TSS_Candidates_v0_2.csv` is a legacy compatibility file, not the current TSS baseline.
`VTS_Entity_Register.csv` contains typed service records, including eligible monitoring services.
`Reporting_Scheme_Register.csv` distinguishes IMO-adopted and national schemes.
`Research_Gaps.csv` and `Batch_Status.csv` govern remaining work.
`Guide_Service_Candidates.csv` is not a final guide contents list.

The old Excel inventory remains historical. These CSVs are the current research data.
Run `python3 scripts/validate_registers.py` before committing changes.
''')
    put('research/TODO.md','''# Remaining project work

Use `data/current/Research_Gaps.csv` as the task queue.

1. Complete and audit B20–B29. Their 50 rows are present but first-pass only.
2. Resolve per-TSS source, boundary and scope flags across all batches.
3. Apply the approved monitoring and national-reporting rules consistently.
4. Finish Off Texel component mapping and the recorded Rotterdam/West Hinder boundary checks.
5. Reconcile later amendments against the 2025 routeing snapshot.
6. Check non-TSS coverage and convert services/sectors into proposed guide entries.

A PASS in a historical audit is not sufficient to close a current gap.
''')
    put('docs/AI_COORDINATION.md',text('docs/AI_COORDINATION.md')+'''\n\n## Mandatory storage controls added 30 September 2026

Read current main before every write. Preserve concurrent changes.
Use a CSV parser/writer, never physical-line replacement or hand-concatenated CSV.
Check IDs across the complete live register before allocating new ones.
Do not rerun historical ID-resynchronisation scripts against current data.
Run the validator and regression tests before committing.
A Git commit is not an evidence audit, and row coverage is not research completion.
''')

    counts=dict(collections.Counter(r['association_status'] for r in rows))
    readiness=dict(collections.Counter(r['readiness_status'] for r in rows))
    summary={'review_date':DATE,'baseline_parents':164,'baseline_tss':224,
      'master_rows_before':174,'unintegrated_first_pass_rows':50,'master_rows_after':len(rows),
      'csv_width_repairs':len(REPAIRS),'orphan_continuation_groups':len(fragments),
      'orphan_continuation_rows':sum(len(v) for v in fragments.values()),
      'existing_stage2_audit_records':174,'first_pass_only_records':50,
      'service_records_before':40,'service_records_after':len(services),
      'imo_reporting_schemes':23,'national_reporting_schemes':5,
      'source_records_before':177,'source_records_after':len(indexed_sources),
      'restored_source_definitions':6,'policy_corrections':5,
      'reported_classifications_before':original_counts,'reported_classifications_after':counts,
      'readiness_status':readiness,'records_requiring_follow_up':sum(bool(r['quality_flags']) for r in rows),
      'per_tss_gap_records':len(gaps)-len(global_gaps),'scope_wide_gates_open':len(global_gaps),
      'full_required_vts_register':False,'publication_ready':False,
      'scope_of_review':'Whole-repository storage/integrity and policy-consistency audit with targeted current-authority checks; not a fresh audit of every operational claim.'}
    put(MARKER,json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
    report=f'''# Repository review: Global VTS

**Date:** {DATE}  
**Conclusion:** The required full VTS register is not yet established.

## What is now reliable

All **224 baseline TSS** have one structurally valid master record.
The **164 parent records** and **224 canonical IDs** are unchanged.
The **50 B20–B29 first-pass rows** are integrated without being promoted to audited findings.
There are **{len(services)} service records**, not {len(services)} verified distinct VTS areas or guide entries.
The reporting register contains **23 IMO** and **5 national** scheme identities.

## Repairs completed

- Corrected **61 misaligned CSV rows** and preserved all substantive narrative fields.
- Removed **five orphan continuation records in two groups**, retaining original bytes and recovery notes.
- Integrated the **50 rows** previously outside the master.
- Restored **six missing source definitions** already cited by the research.
- Assigned canonical IDs to five named national schemes; fourteen TSS records lacked these links.
- Standardised project regions, restored canonical names and repaired the legacy CSV wrapper.
- Rebuilt all 45 batch views from the master, fixing malformed tables and stale completion labels.
- Added current service identities for Åland Sea Traffic, VTS Off Texel and Helsinki Traffic monitoring.
- Applied recorded decision 1 to **five TSS records**: South Åland Sea and four GOFREP TSS.
- Preserved first-pass findings, historical classifications, audit narratives and pre-review bytes.
- Added machine-readable relationships, source index, service candidates, batch status and research gaps.

## Why completion cannot be claimed

**50 records remain first-pass only.** Existing Stage 2 audit documents cover 174 records, but their PASS labels are not universal completion evidence.
**{counts.get('Unresolved',0)} records retain the primary category Unresolved.**
**{summary['records_requiring_follow_up']} records carry follow-up flags** under the consistent review rules.
These counts overlap and must not be added.
Negative findings require checking against the broader approved monitoring and national-reporting scope.
Off Texel exists, but its full/partial relationship to individual Texel/Vlieland components remains open in the register.
Rotterdam distance descriptions and overview charts do not provide a precise outer VTS polygon.
The worldwide non-TSS census, later-amendment reconciliation and final guide-entry grouping are not complete.

## Recorded classifications after policy corrections

| Classification | Records |
|---|---:|
'''
    for key in ['VTS + MRS','VTS only','MRS only','Neither confirmed','Unresolved']:
        report+=f"| {key} | {counts.get(key,0)} |\n"
    report+='''
These are research categories, not final verified absence/presence totals.
Use the independent state and readiness fields for progress decisions.
A service record may represent a statutory area, sector, port centre or project-eligible monitoring service.

## Targeted source checks

Fintraffic explicitly identifies South Åland Sea monitoring from its Western Finland VTS centre [SRC-194, SRC-197, SRC-198].
Decision 1 therefore changes TSS-0012 from Neither confirmed to VTS only, without claiming statutory VTS designation.
Fintraffic also assigns northern GOFREP monitoring to Helsinki Traffic at its Gulf of Finland VTS centre [SRC-197, SRC-198].
The four named GOFREP TSS receive project monitoring links, not whole-TSS Helsinki VTS coverage claims.
Rijkswaterstaat and the Netherlands Coastguard confirm the current Off Texel service [SRC-195, SRC-196].
That missing service is now recorded, with component mapping still flagged.
The Rotterdam 2026 guide and sector diagram were inspected; the unresolved precision caveat is retained [SRC-054, SRC-055].

## Review limits

This review checked the complete repository text snapshot, data structure, IDs, references, progress claims and policy consistency.
It did not reopen every source or independently re-audit every operational relationship.
The source index distinguishes fresh checks from carried-forward material.
The 2025 IMO list remains a source-edition baseline, not a guarantee of September 2026 worldwide currency.
No copyrighted IMO PDF has been uploaded by this repair.

## Next work

Use `data/current/Research_Gaps.csv` to complete B20–B29 and resolve other flagged records.
Then reconcile non-TSS coverage and produce the deduplicated guide-entry list.
Only then can the project state the full number of VTS/reporting areas requiring production.
'''
    put(f'{AUDIT}/REVIEW.md',report)
    put(f'{AUDIT}/csv_repairs.json',json.dumps({'repairs':REPAIRS,'orphan_fragments':fragments},ensure_ascii=False,indent=2)+'\n')
    put('README.md',f'''# Global VTS

Worldwide VTS-guide scoping research: who to call, when, on which channel, and what to report.

## Current status

**The full required VTS register is not yet established.**

| Measure | Current repository count |
|---|---:|
| IMO 2025 Part B parents | 164 |
| Baseline TSS with a master row | 224 / 224 |
| Rows with historical Stage 2 audit documents | 174 |
| First-pass-only rows | 50 |
| Primary classification still Unresolved | {counts.get('Unresolved',0)} |
| Service identity records, not final VTS-area count | {len(services)} |
| IMO reporting schemes | 23 |
| National reporting identities | 5 |

Read [the repository review]({AUDIT}/REVIEW.md) before using old completion reports.
The 224-row baseline is derived from the 2025 source edition. Later amendments still need systematic reconciliation.

## Working registers

- [Master TSS associations]({MASTER})
- [VTS and monitoring-service identities]({VTS})
- [IMO and national reporting schemes](data/current/Reporting_Scheme_Register.csv)
- [Research gaps](data/current/Research_Gaps.csv)
- [Current batches](research/batches_imo2025/README.md)
- [Service candidates for editorial grouping](data/current/Guide_Service_Candidates.csv)
- [Additional non-TSS coverage](data/current/Additional_Coverage_Candidates.csv)
- [Source index](sources/SOURCE_REGISTER.csv)

## Rules and research plan

[Research plan](docs/RESEARCH_PLAN.md) · [Counting and completion rules](docs/STAGE_2_COUNTING_AND_COMPLETION.md) · [Project decisions]({DECISIONS})

Service, centre, sector, reporting-system and guide-entry counts are different.
First-pass and unresolved findings are not complete merely because they have been committed.
The earlier Excel files and 170-row candidate list are historical, not current working masters.

## Validation

Run `python3 scripts/validate_registers.py` and `python3 -m unittest discover -s tests` before committing.
The automated checks validate structure and references; they do not certify navigational accuracy.
''')
    put('CHANGELOG.md','# Changelog\n\n## Repository integrity review - 30 September 2026\n\nRepaired CSV storage, integrated 50 first-pass rows, applied recorded counting decisions, restored references and reopened unsupported completion claims. See the repository review and gaps register.\n\n'+text('CHANGELOG.md').removeprefix('# Changelog\n'))
    # Archive exact changed input bytes, including historical batch views and summaries.
    out=io.BytesIO()
    with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
        for path,value in sorted(BEFORE.items()):
            zi=zipfile.ZipInfo(path,date_time=(2026,9,30,0,0,0));zi.compress_type=zipfile.ZIP_DEFLATED
            z.writestr(zi,value)
    put(f'{AUDIT}/pre_review_files.zip',out.getvalue())
    manifest={p:{'sha256':hashlib.sha256(v).hexdigest(),'bytes':len(v)} for p,v in sorted(BEFORE.items())}
    put(f'{AUDIT}/pre_review_manifest.json',json.dumps(manifest,indent=2)+'\n')
    change_path=f'{AUDIT}/changed_paths.json'
    put(change_path,json.dumps(sorted(CHANGES|{change_path}),indent=2)+'\n')
    print(json.dumps(summary,ensure_ascii=False,indent=2))
    print(f'Changed {len(CHANGES)} paths. Run validation before committing.')


if __name__=='__main__':
    main()
