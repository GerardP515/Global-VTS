#!/usr/bin/env python3
"""Apply a reviewed Stage 2 update to first-pass register rows and rebuild derived files.

Usage: python3 scripts/apply_stage2_update.py UPDATE.json

The update JSON holds finished research, already checked by the four-pass audit:
  rows      {tss_id: {master field: value}} for first-pass rows being promoted
  services  new VTS register rows (vts_id must be new)
  schemes   new national reporting-scheme rows (vrs_id must be new)
  sources   new source definitions (source_id must be new)
  audits    {batch_id: markdown} written to audits/stage2/{batch_id}_Association_Audit.md

Rows not named in the update are left byte-for-byte as they are. Derived tables are
rebuilt with the same rules as scripts/repair_registers_20260930.py. Run
scripts/validate_registers.py afterwards.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from repair_registers_20260930 import (MASTER, SPLIT, VTS, SOURCES, ROOT, ids, put,  # noqa: E402
                                       source_rows, strict_table, text, write_table)

REPORTING = 'data/current/Reporting_Scheme_Register.csv'
EDITABLE = {'association_status', 'vts_id', 'vts_name', 'vts_authority', 'vts_centre', 'vts_sector',
            'vts_boundary_basis', 'vts_source_id', 'vts_source_url', 'mandatory_reporting', 'vrs_id',
            'reporting_scheme_name', 'reporting_authority', 'reporting_boundary_basis', 'reporting_source_id',
            'reporting_source_url', 'voluntary_reporting', 'voluntary_reporting_notes', 'evidence_summary',
            'source_date', 'accessed_date', 'unresolved_issue', 'vts_association_state',
            'reporting_association_state', 'vts_coverage_type', 'candidate_vts_ids', 'candidate_source_ids',
            'review_note'}


def flags_for(r: dict) -> list[str]:
    """Stage 2 flags. Same codes as the repair, without FIRST_PASS_NOT_AUDITED."""
    flags = []
    status = r['association_status']
    if status == 'Unresolved': flags.append('ASSOCIATION_UNRESOLVED')
    if r['unresolved_issue'].strip(): flags.append('OPEN_SOURCE_OR_BOUNDARY_ISSUE')
    if status == 'Neither confirmed': flags.append('NEGATIVE_FINDING_REQUIRES_SCOPE_RECHECK')
    if 'VTS' in status and (not r['vts_id'] or not r['vts_source_id']): flags.append('POSITIVE_VTS_EVIDENCE_INCOMPLETE')
    if 'MRS' in status and (not r['vrs_id'] or not r['reporting_source_id']): flags.append('POSITIVE_REPORTING_EVIDENCE_INCOMPLETE')
    if r['candidate_vts_ids']: flags.append('KNOWN_CURRENT_SERVICE_COMPONENT_MAPPING_REQUIRED')
    return flags


def source_section(s: dict) -> str:
    lines = [f"\n\n### {s['source_id']} — {s['title']}\n", f"- Authority: {s['authority']}."]
    lines.append(f"- URL: {s['url']}")
    lines.append(f"- Evidence class: {s['evidence_class']}")
    for label, key in [('Edition or date', 'date'), ('Accessed', 'accessed'), ('Locator', 'locator')]:
        if s.get(key): lines.append(f'- {label}: {s[key]}')
    lines.append(f"- Verification: {s['verification']}")
    lines.append(f"- Use: {s['use']}")
    return '\n'.join(lines[:1]) + '\n' + '\n'.join(lines[1:]) + '\n'


def patch_view(batch: str, members: list[dict]) -> None:
    """Update the classification cell of changed rows in a hand-maintained batch page."""
    path = f'research/batches_imo2025/{batch}.md'
    lines = text(path).split('\n')
    for r in members:
        for i, line in enumerate(lines):
            if line.startswith(f"| {r['tss_id']} |"):
                cells = line.split(' | ')
                cells[3] = r['association_status']
                lines[i] = ' | '.join(cells)
    put(path, '\n'.join(lines))


def rebuild(rows: list[dict], fields: list[str], batches: set[str], date: str,
            changed: set[str] | None = None, views: bool = True) -> None:
    """Regenerate every table derived from the master register.

    changed: TSS rows whose gap entries are rebuilt (default: every row in batches).
    views: rebuild whole batch pages; otherwise only the changed rows' table lines are patched.
    """
    if changed is None:
        changed = {r['tss_id'] for r in rows if r['batch_id'] in batches}
    write_table(MASTER, fields, rows)
    write_table(SPLIT, fields, [r for r in rows if r['recorded_review_status'] == 'pass1-recorded'])
    # Keep existing index rows as they are (they may carry verification detail the Markdown lacks);
    # append rows only for newly defined sources.
    src_fields, src_rows = strict_table('sources/SOURCE_REGISTER.csv')
    have = {r['source_id'] for r in src_rows}
    src_rows += [r for r in source_rows(text(SOURCES)) if r['source_id'] not in have]
    write_table('sources/SOURCE_REGISTER.csv', src_fields, src_rows)
    _, services = strict_table(VTS)

    relationships = []
    for r in rows:
        for column, prefix, kind, evidence in [('vts_id', 'VTS', 'recorded_vts_association', 'vts_source_id'),
                                               ('vrs_id', 'VRS', 'recorded_reporting_association', 'reporting_source_id'),
                                               ('candidate_vts_ids', 'VTS', 'candidate_service_to_check', 'candidate_source_ids')]:
            for target in ids(r[column], prefix):
                relationships.append({'tss_id': r['tss_id'], 'target_id': target, 'relationship_type': kind,
                                      'review_status': r['readiness_status'], 'source_ids': r[evidence],
                                      'coverage_note': r['vts_coverage_type'] if prefix == 'VTS' else r['reporting_boundary_basis'],
                                      'audit_path': r['audit_path']})
    write_table('data/current/TSS_Service_Relationships.csv', list(relationships[0]), relationships)

    gap_fields, old_gaps = strict_table('data/current/Research_Gaps.csv')
    old_by_id = {g['tss_id']: g for g in old_gaps if g['tss_id']}
    gaps = []
    for r in rows:
        if not r['quality_flags']:
            continue
        if r['tss_id'] not in changed and r['tss_id'] in old_by_id:
            gaps.append(old_by_id[r['tss_id']])
            continue
        gaps.append({'gap_id': f"GAP-{r['tss_id']}", 'tss_id': r['tss_id'], 'batch_id': r['batch_id'],
                     'tss_name': r['tss_name'],
                     'priority': 'High' if r['review_status'] == 'pass1-recorded' or r['association_status'] == 'Unresolved' else 'Review',
                     'reason_codes': r['quality_flags'],
                     'outstanding': r['unresolved_issue'] or ('Recheck negative finding against the approved broader project scope.'
                                                              if r['association_status'] == 'Neither confirmed'
                                                              else 'Complete recorded evidence gaps and national-scheme scope checks.'),
                     'source_context': r['audit_path'],
                     'next_action': 'Complete authority/boundary review; update the master record and rerun validation.'})
    gaps += [g for g in old_gaps if not g['tss_id']]
    write_table('data/current/Research_Gaps.csv', gap_fields, gaps)

    candidates = []
    for s in services:
        linked = [r for r in rows if s['vts_id'] in ids(r['vts_id'], 'VTS')]
        proposed = [r for r in rows if s['vts_id'] in ids(r['candidate_vts_ids'], 'VTS')]
        candidates.append({'service_id': s['vts_id'], 'service_name': s['vts_name'], 'entity_kind': s['entity_kind'],
                           'centre': s['centre'], 'linked_tss_count': str(len(linked)),
                           'linked_tss_ids': '; '.join(r['tss_id'] for r in linked),
                           'candidate_tss_ids': '; '.join(r['tss_id'] for r in proposed),
                           'open_link_reviews': str(sum(bool(r['quality_flags']) for r in linked)),
                           'counting_basis': s['counting_basis'],
                           'guide_entry_status': 'Not final: shared centre, sector and multi-TSS grouping require editorial decision'})
    write_table('data/current/Guide_Service_Candidates.csv', list(candidates[0]), candidates)

    status_fields, old_status = strict_table('data/current/Batch_Status.csv')
    batch_rows = []
    for old in old_status:
        members = [r for r in rows if r['batch_id'] == old['batch_id']]
        if old['batch_id'] not in batches:
            batch_rows.append(old)
            continue
        opened = sum(bool(r['quality_flags']) for r in members)
        first = all(r['review_status'] == 'pass1-recorded' for r in members)
        state = ('First pass only' if first else f'Reviewed records; {opened} require follow-up' if opened
                 else 'Association review recorded; publication checks pending')
        if not views:
            batch_rows.append(dict(old, records=str(len(members)), follow_up_records=str(opened),
                                   first_pass_only=str(sum(r['review_status'] == 'pass1-recorded' for r in members)),
                                   status=state if old['status'].startswith(('Reviewed records', 'First pass', 'Association review')) else old['status']))
            patch_view(old['batch_id'], [r for r in members if r['tss_id'] in changed])
            continue
        batch_rows.append({'batch_id': old['batch_id'], 'records': str(len(members)),
                           'first_pass_only': str(sum(r['review_status'] == 'pass1-recorded' for r in members)),
                           'follow_up_records': str(opened), 'status': state})
        view = (f"# {old['batch_id']} Research Batch\n\n**Stage 2 association review:** {date}  \n**Status:** {state}  \n"
                f'**Records:** {len(members)}  \n**Scope:** IMO 2025 source order\n\n'
                'The table below is generated from the master register. Old checkmarks do not close open evidence issues.\n\n'
                '| ID | TSS | IMO parent | Recorded classification | Current review status |\n|---|---|---|---|---|\n')
        for r in members:
            vals = [r['tss_id'], r['tss_name'], r['imo_parent_ref'], r['association_status'], r['readiness_status']]
            view += '| ' + ' | '.join(v.replace('|', '\\|') for v in vals) + ' |\n'
        view += '\n## Evidence and outstanding checks\n\n'
        for r in members:
            view += (f"### {r['tss_id']}\n\nVTS: {r['vts_id'] or 'Not established'}. Reporting: {r['vrs_id'] or 'Not established'}.\n\n"
                     f"Review flags: {r['quality_flags'] or 'No structural/scope flag raised in the Stage 2 review'}.\n\n"
                     f"{r['unresolved_issue'] or r['review_note']}\n\n"
                     f"Stage 2 evidence: [{Path(r['audit_path']).name}](../../{r['audit_path']}).\n\n")
        view += (f"## Historical research\n\nThe first-pass audit remains at "
                 f"[IMO2025_{old['batch_id']}_Audit.md](../../audits/IMO2025_{old['batch_id']}_Audit.md).\n")
        put(f"research/batches_imo2025/{old['batch_id']}.md", view)
    write_table('data/current/Batch_Status.csv', status_fields, batch_rows)
    idx = '# IMO 2025 research batches\n\nCurrent status is derived from the master register, not historical PASS labels.\n\n'
    idx += '| Batch | TSS rows | First-pass only | Follow-up records | Status |\n|---|---:|---:|---:|---|\n'
    for r in batch_rows:
        idx += f"| [{r['batch_id']}]({r['batch_id']}.md) | {r['records']} | {r['first_pass_only']} | {r['follow_up_records']} | {r['status']} |\n"
    put('research/batches_imo2025/README.md', idx)


def main(path: str) -> None:
    update = json.loads(Path(path).read_text(encoding='utf-8'))
    date = update['date']
    fields, rows = strict_table(MASTER)
    by_id = {r['tss_id']: r for r in rows}

    # New sources, services and schemes first, so row references can be checked.
    src = text(SOURCES)
    known_sources = {s['source_id'] for s in source_rows(src)}
    for s in update.get('sources', []):
        assert s['source_id'] not in known_sources, f"Source already exists: {s['source_id']}"
        src += source_section(s)
        known_sources.add(s['source_id'])
    put(SOURCES, src)
    vt_fields, services = strict_table(VTS)
    known_vts = {s['vts_id'] for s in services}
    for s in update.get('services', []):
        assert s['vts_id'] not in known_vts, f"Service already exists: {s['vts_id']}"
        assert set(s) == set(vt_fields), f"Service fields differ: {s['vts_id']}"
        services.append(s)
        known_vts.add(s['vts_id'])
    services.sort(key=lambda s: s['vts_id'])
    write_table(VTS, vt_fields, services)
    rep_fields, schemes = strict_table(REPORTING)
    known_vrs = {s['vrs_id'] for s in schemes}
    for s in update.get('schemes', []):
        assert s['vrs_id'] not in known_vrs, f"Scheme already exists: {s['vrs_id']}"
        assert set(s) == set(rep_fields) and not s['imo_ref'], f"Scheme fields invalid: {s['vrs_id']}"
        schemes.append(s)
        known_vrs.add(s['vrs_id'])
    write_table(REPORTING, rep_fields, schemes)

    batches = set()
    for tid, values in update['rows'].items():
        r = by_id[tid]
        final_count = update.get('mode') == 'final_count'
        assert final_count or r['recorded_review_status'] == 'pass1-recorded', f'Only first-pass rows are promoted here: {tid}'
        unknown = set(values) - EDITABLE
        assert not unknown, f'{tid}: fields not editable here: {sorted(unknown)}'
        r.update(values)
        for field, prefix, known in [('vts_id', 'VTS', known_vts), ('candidate_vts_ids', 'VTS', known_vts),
                                     ('vrs_id', 'VRS', known_vrs), ('vts_source_id', 'SRC', known_sources),
                                     ('reporting_source_id', 'SRC', known_sources),
                                     ('candidate_source_ids', 'SRC', known_sources)]:
            for key in ids(r[field], prefix):
                assert key in known, f'{tid}: unknown {key} in {field}'
        flags = flags_for(r)
        r['quality_flags'] = '; '.join(flags)
        r['readiness_status'] = 'Review required' if flags else 'Association record reviewed; not publication-ready'
        r['review_status'] = 'reopened' if flags else 'audited'
        if not final_count:
            r['audit_path'] = f"audits/stage2/{r['batch_id']}_Association_Audit.md"
        r['last_integrity_check'] = date
        batches.add(r['batch_id'])
    for batch, content in update.get('audits', {}).items():
        put(f'audits/stage2/{batch}_Association_Audit.md', content)
    for path, content in update.get('files', {}).items():
        put(path, content)
    if update.get('mode') == 'final_count':
        rebuild(rows, fields, batches, date, changed=set(update['rows']), views=False)
    else:
        for batch in batches:
            assert (ROOT / f'audits/stage2/{batch}_Association_Audit.md').is_file(), f'Missing Stage 2 audit: {batch}'
        rebuild(rows, fields, batches, date)
    print(f'Updated {len(update["rows"])} rows in {len(batches)} batches.')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    main(sys.argv[1])
