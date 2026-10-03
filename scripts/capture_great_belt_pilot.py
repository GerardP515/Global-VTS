#!/usr/bin/env python3
"""Capture a fixed public-source set for PILOT-02 into a temporary review bundle.

No repository source originals are created or committed. Full-copy public
republication rights remain unassessed. Records distinguish capture from currency.
"""
from __future__ import annotations
import argparse, datetime as dt, hashlib, json, pathlib, shutil, time, urllib.request
import fitz
from bs4 import BeautifulSoup

SOURCES = [
 ('SRC-008','https://www.forsvaret.dk/da/organisation/soevaernet/civile-opgaver/beltrep/','html',[]),
 ('SRC-015','https://www.forsvaret.dk/da/organisation/soevaernet/nationalt-maritimt-operationscenter/vts/','html',[]),
 ('SRC-020','https://wwwcdn.imo.org/localresources/en/KnowledgeCentre/IndexofIMOResolutions/MSCResolutions/MSC.332(90).pdf','pdf',list(range(17))),
 ('SRC-039','https://www.soefartsstyrelsen.dk/Media/638743469510433298/Navigation%20through%20Danish%20Water%20version%2016.0%202025.pdf','pdf',[]),
 ('P02-IMO332REV1','https://wwwcdn.imo.org/localresources/en/KnowledgeCentre/IndexofIMOResolutions/MSCResolutions/MSC.332(90)%20Rev.1.pdf','pdf',[1,2,3,4,5,12,13,14,15,16]),
 ('P02-DK820','https://www.retsinformation.dk/eli/lta/2013/820/pdf','pdf',list(range(13))),
 ('P02-EN820','https://www.dma.dk/Media/637787223374336711/Order%20on%20the%20ship%20reporting%20system%20BELTREP%20and%20on%20navigation%20under%20the%20East%20Bridge%20and%20the%20West%20Bridge%20in%20the%20Great%20Belt.pdf','pdf',list(range(14))),
 ('P02-DMA-VTS','https://www.dma.dk/safety-at-sea/safety-of-navigation/mandatory-ship-reporting-systems-msrs-and-vessel-traffic-services-vts','html',[]),
 ('P02-ETR','https://beltrep.org/transit/','html',[]),
]
INPUTS = ['VTS_RESEARCH_PROMPT.md','VTS_GUIDE_SCHEMA.md','docs/vts-production/GUIDE_PRESENTATION.md','docs/vts-production/LESSONS_LEARNED.md','docs/vts-production/PLAN.md','research/vts/PILOT_PLAN.md','research/vts/STATUS.csv','research/vts/VTS-0002/dossier.md','research/vts/templates/guide.template.yaml','research/vts/templates/guide.entry-v2.md','reviews/vts/REVIEWER_PROMPT.md','reviews/vts/CORRECTION_REPROOF_PROMPT.md','sources/README.md','sources/SOURCE_REGISTER.csv','sources/manifests/storage.json']

def stamp():
    return dt.datetime.now(dt.timezone.utc).isoformat()

def digest(b):
    return hashlib.sha256(b).hexdigest()

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True,type=pathlib.Path);args=ap.parse_args()
    out=args.output;out.mkdir(parents=True,exist_ok=True)
    for folder in ['originals','extracted','renders','inputs']:(out/folder).mkdir(exist_ok=True)
    records=[];start=stamp();clock=time.monotonic()
    for sid,url,kind,pages in SOURCES:
        rec={'source_id':sid,'requested_url':url,'started_utc':stamp(),'capture_state':'NOT_FETCHED','public_republication_rights':'NOT_ASSESSED_NO_PUBLIC_REPOSITORY_COPY','currency_state':'NOT_DETERMINED_BY_CAPTURE'}
        try:
            req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 (compatible; VTSResearch/1.0)'})
            with urllib.request.urlopen(req,timeout=40) as r:
                raw=r.read(15000001);rec.update(http_status=r.status,final_url=r.url,content_type=r.headers.get('Content-Type'),headers_last_modified=r.headers.get('Last-Modified'))
            if len(raw)>15000000:raise ValueError('Source exceeds fixed 15 MB limit')
            if kind=='pdf' and not raw.startswith(b'%PDF-'):raise ValueError('Expected PDF signature missing')
            if kind=='html' and b'<html' not in raw[:6000].lower():raise ValueError('Expected HTML document missing')
            sha=digest(raw);tag=dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%SZ');name=f'{sid}__{tag}__{sha[:12]}'
            path=out/'originals'/f'{name}.{kind}';path.write_bytes(raw)
            rec.update(capture_state='HELD_TEMPORARY_REVIEW_ARTEFACT',original_path=path.relative_to(out).as_posix(),original_sha256=sha,original_bytes=len(raw),snapshot_id=name)
            if kind=='pdf':
                doc=fitz.open(path);rec['pdf_pages']=len(doc)
                text='\n'.join(f'=== PDF page {i+1} | printed page: see original ===\n'+p.get_text() for i,p in enumerate(doc))
                rec['render_paths']=[]
                for i in pages:
                    if i>=len(doc):continue
                    rp=out/'renders'/f'{name}__p{i+1:03}.png';doc[i].get_pixmap(dpi=110).save(rp);rec['render_paths'].append(rp.relative_to(out).as_posix())
                rec['extractor']='PyMuPDF '+fitz.VersionBind
            else:
                soup=BeautifulSoup(raw,'html.parser');rec['html_title']=soup.title.get_text(' ',strip=True) if soup.title else None
                for el in soup(['script','style','noscript']):el.decompose()
                text=soup.get_text('\n',strip=True);rec['extractor']='BeautifulSoup html.parser; mechanical whole-page text'
                if sid=='P02-ETR':rec['substantive_form_verified']=False
            ep=out/'extracted'/f'{name}.txt';ep.write_text(text,encoding='utf-8')
            rec.update(extracted_path=ep.relative_to(out).as_posix(),extracted_sha256=digest(ep.read_bytes()),extracted_bytes=ep.stat().st_size,completed_utc=stamp())
        except Exception as exc:
            rec.update(capture_state='CAPTURE_OR_DERIVATIVE_FAILED',error=repr(exc),completed_utc=stamp())
        records.append(rec)
        print(sid,rec['capture_state'],flush=True)
    inputs=[]
    for name in INPUTS:
        p=pathlib.Path(name)
        if p.is_file():
            dst=out/'inputs'/p;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,dst)
            inputs.append({'path':name,'sha256':digest(p.read_bytes()),'bytes':p.stat().st_size})
    manifest={'study_id':'PILOT-02','started_utc':start,'completed_utc':stamp(),'capture_elapsed_seconds':round(time.monotonic()-clock,3),'storage':'Temporary Actions artefact and downloaded research workspace; not a public repository original archive','source_id_note':'SRC IDs reused from register. P02 IDs are local bibliographic identities pending shared-register reconciliation.','records':records,'repository_inputs':inputs}
    (out/'capture_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    manifest_files=[]
    for p in sorted(out.rglob('*')):
        if p.is_file():manifest_files.append({'path':p.relative_to(out).as_posix(),'bytes':p.stat().st_size,'sha256':digest(p.read_bytes())})
    (out/'bundle_files.json').write_text(json.dumps(manifest_files,indent=2)+'\n',encoding='utf-8')

if __name__=='__main__':main()
