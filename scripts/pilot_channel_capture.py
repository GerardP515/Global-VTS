#!/usr/bin/env python3
"""One-shot capture of two OGL-licensed MCA sources for PILOT-01.

No dossier editing, source approval, publication or recurring scheduling.
Original responses and mechanically extracted text remain separate.
Only the fixed public GOV.UK URLs below are fetched.
"""
from datetime import datetime, timezone
from hashlib import sha256
from html.parser import HTMLParser
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.parse import urlparse
import json

ROOT = Path(__file__).resolve().parents[1]
SOURCES = [
    ('SRC-004', 'https://www.gov.uk/government/publications/dover-strait-crossings-channel-navigation-information-service/dover-strait-crossings-channel-navigation-information-service-cnis'),
    ('SRC-005', 'https://www.gov.uk/government/publications/mgn-364-mf-amendment-2-navigation-safety-traffic-separation-schemes-application-of-rule-10-and-navigation-in-the-dover-strait/mgn-364-mf-amendment-2-navigation-safety-traffic-separation-schemes-application-of-rule-10-and-navigation-in-the-dover-strait'),
]

class PageText(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.skip = 0
        self.parts = []
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.skip += 1
        if not self.skip and tag in ('p', 'li', 'h1', 'h2', 'h3', 'h4', 'br', 'tr'):
            self.parts.append('\n')
    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.skip = max(0, self.skip - 1)
        if not self.skip and tag in ('p', 'li', 'h1', 'h2', 'h3', 'h4', 'tr'):
            self.parts.append('\n')
    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)


def main():
    output = ROOT / 'sources/manifests/PILOT-01/capture_result.json'
    if output.exists():
        raise SystemExit('Capture already recorded. Create a new explicit acquisition revision; do not overwrite it.')
    records = []
    for source_id, url in SOURCES:
        now = datetime.now(timezone.utc)
        stamp = now.strftime('%Y%m%dT%H%M%SZ')
        row = {
            'source_id': source_id, 'study_id': 'PILOT-01', 'service_ids': ['VTS-0001'],
            'requested_url': url, 'retrieved_at_utc': now.isoformat(timespec='seconds'),
            'capture_status': 'NOT_FETCHED', 'http_status': None, 'final_url': None,
            'original_path': None, 'sha256': None, 'bytes': None,
            'text_path': None, 'text_sha256': None,
            'rights': 'Open Government Licence v3.0 for MCA text; third-party artwork not approved',
            'inspection_status': 'CAPTURE_ONLY_NOT_INDEPENDENTLY_CHECKED',
            'failure_reason': None,
        }
        try:
            request = Request(url, headers={'User-Agent': 'VTS-Guide-Research/0.1'})
            with urlopen(request, timeout=30) as response:
                data = response.read(5_000_001)
                row['http_status'] = response.status
                row['final_url'] = response.url
                row['content_type'] = response.headers.get('Content-Type')
            if urlparse(row['final_url']).hostname != 'www.gov.uk':
                raise ValueError('Unexpected redirect host; capture rejected')
            if len(data) > 5_000_000 or len(data) < 1000:
                raise ValueError('Unexpected response size')
            if b'CALDOVREP' not in data or b'<html' not in data.lower():
                raise ValueError('Expected substantive MCA HTML not found')
            if b'Open Government Licence' not in data and b'open-government-licence' not in data:
                raise ValueError('Expected OGL notice absent; do not archive')
            digest = sha256(data).hexdigest()
            snap = f'{source_id}__{stamp}__{digest[:12]}'
            raw = ROOT / 'sources/archive/html' / (snap + '.html')
            textfile = ROOT / 'sources/extracted' / (snap + '.txt')
            raw.parent.mkdir(parents=True, exist_ok=True)
            textfile.parent.mkdir(parents=True, exist_ok=True)
            raw.write_bytes(data)
            parser = PageText()
            parser.feed(data.decode('utf-8', errors='strict'))
            lines = [line.strip() for line in ''.join(parser.parts).splitlines() if line.strip()]
            text = '\n'.join(lines) + '\n'
            textfile.write_text(text, encoding='utf-8')
            row.update(capture_status='HELD', snapshot_id=snap,
                       original_path=raw.relative_to(ROOT).as_posix(), sha256=digest, bytes=len(data),
                       text_path=textfile.relative_to(ROOT).as_posix(),
                       text_sha256=sha256(text.encode('utf-8')).hexdigest(),
                       extractor='Python standard-library HTMLParser; scripts/pilot_channel_capture.py')
        except Exception as exc:
            row['capture_status'] = 'NETWORK_ERROR' if not isinstance(exc, ValueError) else 'INVALID_CONTENT'
            row['failure_reason'] = str(exc)
        records.append(row)
        print(source_id, row['capture_status'], row.get('bytes'))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps({'schema_version': 'pilot-capture-0.1', 'records': records}, indent=2) + '\n')

if __name__ == '__main__':
    main()
