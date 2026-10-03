#!/usr/bin/env python3
"""Re-proof the frozen Channel proforma-1 presentation and export a portable copy.

Presentation-only checks against an existing author research record. This is not
source verification, a general VTS validator, or marine/publication approval.
Requires PyYAML. Never writes the dossier, its YAML, packet or research status.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import posixpath
import re
from pathlib import Path
import yaml

DOSSIER_SHA = '566b107d4707713bad252aec46f1aa5a2231ae23cb2d56895bb3e30a9e2ccc4e'
FRONT_SHA = 'e35c68bc166249f2e5244b0bec4a9f30c82ffb084f3c8c71725e49c76ff3e5ef'
REF = 'd1b82038636e5b6738120d1b78e92f2ce561376c'
BASE = f'https://github.com/GerardP515/Global-VTS/blob/{REF}/'
REPO_PATH = 'research/vts/VTS-0001/dossier.md'


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def section(body: str, heading: str, level: int = 2) -> str:
    marker = '#' * level + ' ' + heading + '\n'
    require(body.count(marker) == 1, f'Missing or repeated section: {heading}')
    tail = body.split(marker, 1)[1]
    match = re.search(r'(?m)^#{1,' + str(level) + r'} ', tail)
    return tail[:match.start()] if match else tail


def body_checks(body: str, data: dict) -> dict:
    headings = re.findall(r'^## ([1-9])\. ', body, re.M)
    require(headings == list('123456789'), 'Nine fixed sections not preserved')
    require('DRAFT / HOLD. Not for navigation or publication.' in body,
            'HOLD warning missing')
    anchors = re.findall(r'<a id="([^"]+)"></a>', body)
    require(len(anchors) == len(set(anchors)), 'Duplicate explicit anchor')
    targets = set(re.findall(r'\]\(#([^)]*)\)', body))
    require(targets <= set(anchors), 'Broken internal reference or gap link')
    require(all(f'r{i}' in anchors for i in range(1, 9)), 'Bibliography incomplete')
    require(all(g['gap_id'].lower() in anchors for g in data['gaps']), 'Gap missing')
    for item in data['evidence']:
        require(f"| {item['evidence_id']} |" in body, 'Evidence crosswalk incomplete')
    for direction in data['directions']:
        for event in direction['reporting_events']:
            require(f"| {event['event_id']} |" in body, 'Event crosswalk incomplete')
    main = section(body, '4. Information required')
    rows = [line for line in main.splitlines() if line.startswith('| ')]
    fields = data['report_types'][0]['fields']
    actual_codes = [line.split('|')[1].strip() for line in rows
                    if line.split('|')[1].strip() not in
                    {'Code', '---', 'Subject within X',
                     'Estimated amount and characteristics of bunker fuel.',
                     'Navigational conditions.'}]
    require(actual_codes == [f['code_as_published'] for f in fields],
            'Main report-code order or completeness changed')
    for field in fields:
        matches = [r for r in rows if r.startswith(f"| {field['code_as_published']} |")]
        require(len(matches) == 1, 'Report field duplicated or absent')
        row = matches[0]
        require('[R2 Appendix, item ' in row and '(#r2)' in row,
                'Point-of-use field reference missing')
        if field['code_as_published'] != 'X':
            require(field['information_required'] in row,
                    f"Report subject changed: {field['code_as_published']}")
            condition = field.get('applicability_condition')
            require(not condition or condition in row,
                    f"Report condition omitted: {field['code_as_published']}")
    require('Bunker fuel exceeds 5,000 tonnes.' in main,
            'Strict bunker threshold changed')
    require('Not subject to the bunker-quantity threshold.' in main,
            'Bunker condition incorrectly applied to navigation')
    require('not additional official report codes' in main,
            'X editorial-subitem qualification missing')
    require('Unknown bunker quantity remains a review question.' in main,
            'Unknown-quantity qualification omitted')
    require('This concerns the cargo portion only, not the entire report.' in main,
            'Cargo delivery scope changed')
    require('non-verbal' in main and 'advance' in main,
            'Cargo-delivery method or timing qualification missing')
    require('G06' in main, 'Formatting gap hidden')
    for direction, heading in zip(data['directions'],
            ['3.1 North-eastbound transit', '3.2 South-westbound transit']):
        part = section(body, heading, 3)
        entry = direction['reporting_events'][0]
        timing = entry.get('timing_summary') or entry['timing_as_published']
        require(timing in part, f'Directional timing changed: {heading}')
        contact = next(c for c in data['communications'] if c['contact_id'] == entry['contact_id'])
        require(contact['recipient'] in part and contact['call_sign'] in part,
                f'Directional recipient changed: {heading}')
        channel_row = next((r for r in part.splitlines() if r.startswith('| Published calling channel |')), '')
        require(f"VHF {contact['calling_channel']}." in channel_row,
                f'Calling-channel role or value changed: {heading}')
        require('not established in this sample' in part and 'no report required' in part,
                f'Unresearched transfer/departure warning missing: {heading}')
    conditional = section(body, '6. Conditional and exceptional reporting')
    require('The source says should.' in conditional, 'Conditional obligation strengthened')
    require('G05' in conditional and 'G08' in conditional, 'Conditional implementation gaps hidden')
    require('Notification is not permission to breach Rule 10.' in conditional,
            'ITZ notification incorrectly presented as permission')
    geometry = section(body, '7. Reporting locations and graphic requirements')
    require('Not approved for plotting.' in geometry, 'Plotting warning omitted')
    for obj in data['reporting_objects']:
        require(obj['geometry_as_published'] in geometry, 'Recorded geometry changed')
    require(geometry.count('**Datum:** not stated') == 2, 'Missing datum presented as known')
    return {'fixed_sections': 9, 'report_code_groups': len(fields),
            'directions': len(data['directions']),
            'events': sum(len(d['reporting_events']) for d in data['directions']),
            'evidence_records': len(data['evidence']), 'bibliography_entries': 8,
            'open_gaps': len(data['gaps']), 'internal_link_targets': len(targets)}


def portable_copy(body: str) -> tuple[str, int]:
    """Alter navigation links only. Preserve all research text and limitations."""
    count = 0
    rewrites = []
    def link(match: re.Match) -> str:
        nonlocal count
        label, target = match.groups()
        path = posixpath.normpath(posixpath.join(posixpath.dirname(REPO_PATH), target))
        require(not path.startswith('../') and not path.startswith('/'), 'Invalid repository link')
        count += 1
        replacement = f'[{label}]({BASE}{path})'
        rewrites.append((replacement, match.group(0)))
        return replacement
    result = re.sub(r'\[([^\]\n]+)\]\((?!https?://|#)([^)\n]+)\)', link, body)
    titles = re.findall(r'^## ([1-9])\. (.+)$', result, re.M)
    for n, title in titles:
        result = result.replace(f'{n}. {title}\n', f'{n}. [{title}](#section-{n})\n', 1)
        result = result.replace(f'## {n}. {title}\n',
                                f'<a id="section-{n}"></a>\n\n## {n}. {title}\n', 1)
    # Avoid adding a second master: identify the exact unchanged upstream dossier.
    result = (f'> Generated reading copy of the [canonical dossier]({BASE}{REPO_PATH}) '
              f'at `{REF[:12]}`. Only navigation links differ from the body of that dossier.\n\n' + result)
    require(not re.search(r'\[([^\]\n]+)\]\((?!https?://|#)([^)\n]+)\)', result),
            'Unresolved relative link in export')
    restored = result.split('\n\n', 1)[1]
    for n, title in titles:
        restored = restored.replace(f'{n}. [{title}](#section-{n})\n', f'{n}. {title}\n', 1)
        restored = restored.replace(f'<a id="section-{n}"></a>\n\n', '', 1)
    for replacement, original in rewrites:
        restored = restored.replace(replacement, original, 1)
    require(restored == body, 'Export changed text outside navigation/provenance')
    return result, count


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--dossier', type=Path,
                    default=Path('research/vts/VTS-0001/dossier.md'))
    ap.add_argument('--reading-copy', type=Path)
    ap.add_argument('--export', type=Path)
    ap.add_argument('--report', type=Path)
    args = ap.parse_args()
    raw = args.dossier.read_bytes()
    require(hashlib.sha256(raw).hexdigest() == DOSSIER_SHA,
            'Input is not the reviewed proforma-1 dossier; do not silently reuse this test')
    parts = raw.split(b'---\n', 2)
    require(len(parts) == 3 and parts[0] == b'', 'YAML front matter missing')
    front = b'---\n' + parts[1] + b'---\n'
    require(hashlib.sha256(front).hexdigest() == FRONT_SHA, 'Canonical YAML changed')
    data = yaml.safe_load(parts[1])
    require(data['research_state'] == 'HOLD', 'Unexpected research state')
    body = parts[2].decode('utf-8').lstrip('\n')
    if args.reading_copy:
        require(args.reading_copy.read_bytes() == body.encode('utf-8'),
                'Original reading copy differs from canonical body')
    result = body_checks(body, data)
    mutations = {
        'missing HOLD warning': ('DRAFT / HOLD. Not for navigation or publication.', 'Draft'),
        'wrong report subject W': ('Total number of persons aboard.', 'Personnel particulars.'),
        'lost SW VHF-range qualifier': ('Within VHF range of North Foreland and before the eastern reporting line; MGN states no later than crossing.', 'At the eastern line.'),
        'wrong NE calling channel': ('| VHF 13. Further channel roles', '| VHF 12. Further channel roles'),
        'calling channel relabelled as working': ('| Published calling channel |', '| Working channel |'),
        'inclusive instead of strict bunker threshold': ('Bunker fuel exceeds 5,000 tonnes.', 'Bunker fuel is 5,000 tonnes or more.'),
        'bunker condition extended to navigation': ('Not subject to the bunker-quantity threshold.', 'Subject to the bunker threshold.'),
        'cargo option widened to entire report': ('This concerns the cargo portion only, not the entire report.', 'This concerns the entire report.'),
        'conditional should strengthened': ('The source says should.', 'The source says must.'),
        'broken bibliography anchor': ('<a id="r2"></a>', '<a id="r2-broken"></a>'),
        'ITZ notification treated as permission': ('Notification is not permission to breach Rule 10.', 'Notification gives permission.'),
        'plotting warning omitted': ('Not approved for plotting.', 'Approved for plotting.'),
    }
    rejected = []
    for name, (old, new) in mutations.items():
        require(old in body, f'Mutation fixture not exercised: {name}')
        try:
            body_checks(body.replace(old, new, 1), data)
        except ValueError:
            rejected.append(name)
        else:
            raise ValueError(f'Defective presentation accepted: {name}')
    export, converted = portable_copy(body)
    body_checks(export, data)
    if args.export:
        args.export.parent.mkdir(parents=True, exist_ok=True)
        args.export.write_bytes(export.encode('utf-8'))
    result.update({'result': 'PASS', 'scope': 'Frozen pilot presentation, not operational fact checking',
                   'input_dossier_sha256': DOSSIER_SHA, 'canonical_front_matter_sha256': FRONT_SHA,
                   'original_reading_copy_equals_body': bool(args.reading_copy),
                   'negative_tests_rejected': rejected, 'negative_test_count': len(rejected),
                   'portable_repository_links': converted, 'clickable_contents_entries': 9, 'export_text_round_trip': 'EXACT',
                   'portable_copy_sha256': hashlib.sha256(export.encode()).hexdigest(),
                   'canonical_dossier_modified': False, 'research_state': 'HOLD',
                   'publication_ready': False, 'fresh_source_checks': False,
                   'independent_marine_approval': False})
    encoded = json.dumps(result, indent=2) + '\n'
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(encoded, encoding='utf-8')
    print(encoded, end='')


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, yaml.YAMLError) as exc:
        raise SystemExit(f'Presentation check failed: {exc}') from exc
