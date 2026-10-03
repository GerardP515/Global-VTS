#!/usr/bin/env python3
"""Bounded PILOT-02 checks. These do not certify source meaning or currency."""
from __future__ import annotations
import argparse,copy,datetime as dt,hashlib,json,re
from pathlib import Path
import yaml

EXPECTED_CODES=['A','B','C','E','F','G and I','H','L','O','P','Q or R','T','U','W','X']
HEADINGS=['Service and operating area','Participation and applicability','Reporting procedures','Information to report','Communications and watchkeeping','Special circumstances','Boundaries and reporting locations','Operational limitations','References']
class StrictLoader(yaml.SafeLoader): pass
def mapping(loader,node,deep=False):
    pairs=loader.construct_pairs(node,deep=deep);out={}
    for k,v in pairs:
        if k in out:raise ValueError('Duplicate YAML key: '+str(k))
        out[k]=v
    return out
StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,mapping)
def require(ok,msg):
    if not ok:raise ValueError(msg)
def load(raw):
    a=raw.split('---\n',2);require(len(a)==3 and not a[0],'YAML front matter missing')
    return yaml.load(a[1],Loader=StrictLoader),a[2].lstrip('\n')
def participation(d,gt,air,pleasure=False,length=None,state=False):
    if state:return False
    r=d['participation']['rules'];e=d['participation']['exemption_rules']
    ops={'GE':lambda a,b:a>=b,'LT':lambda a,b:a<b}
    def test(record,value):return None if value is None else ops[record['operator']](value,record['value'])
    def combine(values,op):
        if op=='ANY':return True if True in values else (None if None in values else False)
        return False if False in values else (None if None in values else True)
    duty=combine([test(r['gross_tonnage'],gt),test(r['air_draught_m'],air)],r['combiner'])
    if pleasure:
        exempt=combine([test(e['gross_tonnage'],gt),test(e['hull_length_m'],length)],e['combiner'])
        if exempt is True:return False
        if exempt is None:return None if duty is not False else False
    return duty

def validate(d,body,cat):
    require(d['vts_id']=='VTS-0002' and d['study_id']=='PILOT-02','Wrong service')
    require(d['research_state']=='HOLD','Unexpected approval state')
    require(d['participation']['rules']=={'combiner':'ANY','gross_tonnage':{'operator':'GE','value':50},'air_draught_m':{'operator':'GE','value':15.0}},'Participation threshold/logic')
    require(d['participation']['exemption_rules']=={'vessel_type':'PLEASURE_CRAFT','combiner':'ANY','hull_length_m':{'operator':'LT','value':15},'gross_tonnage':{'operator':'LT','value':50}},'Recreational exemption logic')
    f=d['report_types'][0]['fields'];require([x['code_as_published'] for x in f]==EXPECTED_CODES,'Report groups/order')
    require(f[-1]['condition']=={'parameter':'gross_tonnage','operator':'GE','value':1000,'unit':'GT'},'Bunker condition')
    require(f[-2]['ais_only_accepted'] is False,'W AIS-only acceptance')
    p=d['reporting_policy'];require(p['minimum_voice_entry']==['SHIP_NAME','MAXIMUM_AIR_DRAUGHT','DEADWEIGHT','ENTRY_LINE'],'Minimum voice entry')
    require(p['q_or_r_always_voice_if_applicable'] is True,'Q/R voice requirement')
    require('W' not in p['ais_accepted_codes'],'W listed as AIS sufficient')
    require(p['contact_email']=='vts@beltrep.org','Provider email mismatch')
    com={x['contact_id']:x for x in d['communications']}
    require(com['S1']['working_channel']=='74' and com['S2']['working_channel']=='11','Sector channel assignment')
    for x in com.values():require(x['calling_channel'] is None and x['listening_watch']==[x['working_channel'],'16'],'Channel roles/watch')
    actions=d['communications_actions'];require(len(actions)==2,'Channel action population')
    for a in actions:require(a['report_required'] is False and a['report_type_id'] is None,'Transfer made into report')
    require([(x['from_contact_id'],x['to_contact_id']) for x in actions]==[('S2','S1'),('S1','S2')],'Direction reversal')
    events=[e for x in d['directions'] for e in x['reporting_events']]+d['common_reporting_events']
    require(len(events)==6,'Reporting-event population')
    for x in d['directions']:
        require(x['sequence_semantics']=='ENTRY_EVENTS_ARE_ALTERNATIVES_NOT_SUCCESSIVE_CALLS','False successive entry itinerary')
    require(d['report_delivery_options'][0]['distance_is_approximate'] is True,'Approximate range made exact')
    require(d['report_delivery_options'][1]['advance_minutes']==60,'Advance internal-departure timing')
    require(not any(x['whole_report_exemption'] for x in d['report_delivery_options']),'Advance report removes voice duty')
    require(len(d['boundary_vertices'])==10,'Coordinate population')
    require(d['reporting_objects'][-1]['latitude_as_published']=='55°35′.00 N','Sector boundary')
    require(all(x['datum_as_published']=='WGS 84' for x in d['reporting_objects']),'Datum lost')
    require([x.get('vertex_ids') for x in d['reporting_objects'][:4]]==[['P1','P2'],['P2','P3','P4'],['P5','P6','P7','P8'],['P9','P10']],'Boundary order')
    fc=d['future_changes'][0]
    require(fc['effective_from']=='2026-12-01T00:00:00Z' and fc['state_at_cutoff']=='ADOPTED_NOT_YET_EFFECTIVE','Future commencement')
    require(fc['current_field_table_includes_change'] is False,'Future requirement applied early')
    require('insurance' not in f[-1]['information_required'].lower(),'Future insurance in current X')
    require(d['assurance']['must_reassess_before_utc']==fc['effective_from'],'Missing revision deadline')
    src={x['source_id']:x for x in cat['records']};ids=[x['evidence_id'] for x in d['evidence']];require(len(ids)==len(set(ids)),'Duplicate evidence IDs')
    for e in d['evidence']:
        require(e['source_id'] in src,'Missing source')
        require(e['snapshot_id']==src[e['source_id']]['snapshot_id'],'Wrong source/snapshot binding')
        require(e['source_id']!='P02-ETR','Application shell used as evidence')
    def walk(obj):
        if isinstance(obj,dict):
            for k,v in obj.items():
                if k=='evidence_ids':require(set(v)<=set(ids),'Broken evidence relationship')
                walk(v)
        elif isinstance(obj,list):
            for v in obj:walk(v)
    walk(d)
    require(re.findall(r'^## [1-9]\. (.+)$',body,re.M)==HEADINGS,'Reader sections')
    require('DRAFT / HOLD. Not for navigation or publication.' in body,'Draft warning lost')
    anchors=re.findall(r'<a id="([^"]+)"></a>',body);require(len(anchors)==len(set(anchors)),'Duplicate anchors')
    links=re.findall(r'\]\(#([^)]*)\)',body);require(set(links)<=set(anchors),'Broken anchor')
    require(not re.search(r'\]\((?!https?://|#)[^)]+\)',body),'Standalone relative link')
    require('—' not in body.split('## Appendix A.')[0],'Em dash')
    main=body.split('## 4. Information to report\n',1)[1].split('### AIS',1)[0]
    rows=[r for r in main.splitlines() if r.startswith('| ')][2:]
    require([r.split('|')[1].strip() for r in rows]==EXPECTED_CODES,'Readable field order')
    for row in rows:require('](#r1)' in row,'Missing field point-of-use reference')
    require('no routine verbal report' in body.lower() or 'does **not** require a verbal report' in body,'No-report transfer distinction lost')
    for v in d['boundary_vertices']:
        require(v['latitude_as_published'] in body and v['longitude_as_published'] in body,'Coordinate lost in prose')
    require(len(d['gaps'])==6 and all(g['disposition']=='OPEN' for g in d['gaps']),'Open gaps silently closed')
    return {'evidence_records':len(ids),'reporting_events':len(events),'channel_change_actions':len(actions),'delivery_options':2,'directions':2,'report_code_groups':len(f),'coordinate_vertices':10,'external_reporting_lines':4,'bibliography_records':6,'internal_links':len(links)}

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--root',type=Path,default=Path('.'));ap.add_argument('--sources',type=Path);ap.add_argument('--output',type=Path);ap.add_argument('--release',action='store_true');args=ap.parse_args()
    folder=args.root/'research/vts/VTS-0002';raw=(folder/'dossier.md').read_text();d,b=load(raw);cat=json.loads((folder/'source_catalogue.json').read_text());r=validate(d,b,cat)
    mutations=[('wrong participation',lambda x:x['participation']['rules']['gross_tonnage'].update(value=300)),('threshold AND',lambda x:x['participation']['rules'].update(combiner='ALL')),('recreational AND',lambda x:x['participation']['exemption_rules'].update(combiner='ALL')),('fuel quantity condition',lambda x:x['report_types'][0]['fields'][-1]['condition'].update(parameter='bunker_tonnes')),('strict1000GT',lambda x:x['report_types'][0]['fields'][-1]['condition'].update(operator='GT')),('AIS-only W',lambda x:x['report_types'][0]['fields'][-2].update(ais_only_accepted=True)),('missing deadweight voice',lambda x:x['reporting_policy']['minimum_voice_entry'].remove('DEADWEIGHT')),('wrong channel',lambda x:x['communications'][0].update(working_channel='13')),('no watch16',lambda x:x['communications'][1]['listening_watch'].remove('16')),('transfer-report invention',lambda x:x['communications_actions'][0].update(report_required=True)),('reversed transfer',lambda x:x['communications_actions'][0].update(to_contact_id='S2')),('advance exemption',lambda x:x['report_delivery_options'][0].update(whole_report_exemption=True)),('exact20NM',lambda x:x['report_delivery_options'][0].update(distance_is_approximate=False)),('wrong futuredate',lambda x:x['future_changes'][0].update(effective_from='2026-05-22T00:00:00Z')),('early insurance',lambda x:x['future_changes'][0].update(current_field_table_includes_change=True)),('wrong snapshot',lambda x:x['evidence'][0].update(snapshot_id='wrong')),('missing field',lambda x:x['report_types'][0]['fields'].pop()),('lost datum',lambda x:x['reporting_objects'][0].update(datum_as_published=None))]
    rejected=[]
    for name,fn in mutations:
        x=copy.deepcopy(d);fn(x)
        try:validate(x,b,cat)
        except (ValueError,KeyError):rejected.append(name)
        else:raise ValueError('Mutation accepted: '+name)
    for name,old,new in [('missing HOLD','DRAFT / HOLD. Not for navigation or publication.','Approved'),('broken citation','<a id="r1"></a>','<a id="broken-r1"></a>')]:
        try:validate(d,b.replace(old,new,1),cat)
        except ValueError:rejected.append(name)
        else:raise ValueError('Text mutation accepted: '+name)
    cases=[(49,14.99,False,None,False,False),(50,0,False,None,False,True),(1,15,False,None,False,True),(50,15,False,None,False,True),(50,15,True,14.99,False,False),(49,20,True,30,False,False),(50,15,True,15,False,True),(10000,40,False,None,True,False),(None,14,False,None,False,None),(None,15,False,None,False,True),(50,None,False,None,False,True),(50,15,True,None,False,None)]
    for gt,air,p,l,s,out in cases:require(participation(d,gt,air,p,l,s) is out,'Participation boundary failed')
    deadline=dt.datetime.fromisoformat(d['assurance']['must_reassess_before_utc'].replace('Z','+00:00'))
    for stamp,out in [('2026-11-30T23:59:59+00:00',False),('2026-12-01T00:00:00+00:00',True),('2026-12-01T00:00:01+00:00',True)]:require((dt.datetime.fromisoformat(stamp)>=deadline) is out,'Effective-date boundary failed')
    for gt,out in [(999,False),(1000,True),(1001,True)]:require((gt>=d['report_types'][0]['fields'][-1]['condition']['value']) is out,'BunkerGTboundary failed')
    verified=0
    if args.sources:
        mf=json.loads((args.sources/'bundle_files.json').read_text())
        for x in mf:
            p=args.sources/x['path'];z=p.read_bytes();require(len(z)==x['bytes'] and hashlib.sha256(z).hexdigest()==x['sha256'],'Source bundle mismatch '+x['path']);verified+=1
    r.update(result='PASS',scope='Pilot-specific structural, mapping and boundary tests; not independent marine/source-currency approval',negative_tests_rejected=rejected,negative_test_count=len(rejected),participation_boundary_tests=len(cases),bunker_boundary_tests=3,effective_date_boundary_tests=3,source_bundle_files_verified=verified,source_hash_check='EXECUTED' if args.sources else 'NOT_RUN_SOURCE_BUNDLE_NOT_PROVIDED',dossier_sha256=hashlib.sha256(raw.encode()).hexdigest(),publication_ready=False,independent_review='NOT_STARTED')
    if args.release:r.update(result='BLOCKED',reason='HOLD; open source/currency/approval gaps')
    result=json.dumps(r,indent=2)+'\n'
    if args.output:args.output.write_text(result)
    print(result,end='')
    if args.release:raise SystemExit(2)
if __name__=='__main__':main()
