# VTS guide presentation standard

Recorded: 3 October 2026. Presentation revision: proforma-1.
Status: applied to Channel VTS only; publication HOLD remains.

## Purpose

Use the fixed-section and immediate-reference approach from the Bulk Ports guides.
Present reporting requirements directly, rather than describing where research data can be found.
Do not import cargo, berth or terminal-service sections into the VTS reporting guide.

One service retains one canonical Markdown dossier with YAML front matter.
The YAML contains operational data; the readable body presents that data for marine editors and designers.
A reading-copy export omits the YAML, without becoming a separately maintained master.

## Fixed pro forma

1. Service overview.
2. Participation and applicability.
3. Reporting arrangements by direction.
4. Information required.
5. Communications and watchkeeping.
6. Conditional and exceptional reporting.
7. Reporting locations and graphic requirements.
8. References.
9. Outstanding checks and editorial notes.

Appendix A contains research history, source-ID crosswalks and review records.
Retain missing-information headings. Do not turn an unresearched departure section into a finding of no reporting duty.

## Presentation rules

- Give each direction a separate entry table.
- Use consistent labels: applicability, boundary, timing, recipient, channel and information required.
- Separate routine entry events from conditional notifications.
- Display every report-code group and its required information in the readable body.
- Preserve subitem conditions without turning them into additional official report codes.
- Place a precise source reference beside each factual claim or table row.
- Preserve source qualifiers, unresolved communication roles and geometry limitations.
- Keep operational limitations beside the affected instruction, not only in an appendix.
- Put detailed review history and internal evidence identifiers in the appendix.
- Do not claim independent review, source acquisition or release through a formatting change.

## Citation convention

Reader labels such as R1 are local bibliography aliases, not new global source IDs.
Each alias maps to the existing source catalogue and its retained or unretained status.
Citations use the relevant clause, heading, table item or PDF page.
The Appendix item label must not be mistaken for a separately lettered appendix.
For example, use `R2 Appendix, item W`, not an ambiguous `Appendix W` title.

The readable bibliography includes issuer, title, edition/date, original URL, recorded access and source-copy status.
The complete evidence locator ledger retains the original detailed locators.
A citation to a live-consulted source does not imply that its original has been archived.

## Current implementation

- Template: `research/vts/templates/guide.proforma.md`.
- Pilot adapter: `scripts/render_channel_proforma.py`.
- Canonical guide: `research/vts/VTS-0001/dossier.md`.
- Presentation record: `research/vts/VTS-0001/presentation_check.json`.
- Exact review inputs: `research/vts/VTS-0001/packet.json`.

The adapter is deliberately pilot-specific. It checks the expected canonical YAML hash before rendering.
It does not author guides for other services or approve their operational content.
Further schema or content changes require a reviewed adapter update.
The template is a draft/HOLD presentation, not an approved publication template.

Default command, read-only:

```sh
python3 scripts/render_channel_proforma.py
```

Authorised presentation refresh:

```sh
python3 scripts/render_channel_proforma.py --apply
```

Commit the changed dossier before assembling its packet, so the packet can identify that exact commit.

```sh
python3 scripts/render_channel_proforma.py --packet
python3 scripts/validate_channel_pilot_v2.py
```

Exports are generated copies, not editable parallel masters.

## Executed Channel checks

Workflow: https://github.com/GerardP515/Global-VTS/actions/runs/37109509176
Job: 111164528235. Completed successfully.
Presentation output checkpoint: `0a87381d308cb540aa7bd7e8c6803487eebaa20a`.

| Check | Observed result |
|---|---|
| Canonical YAML bytes | Unchanged from research 0.2.1 |
| Main sections | 9 plus Appendix A |
| Directions / events | 2 / 6 |
| Main report-code groups | 13 |
| Evidence records / bibliography aliases | 32 / 8 |
| Existing gaps / conflicts | 8 / 4, retained |
| Citation and gap anchors | Resolved within the generated document |
| Review-packet hashes and sizes | 14 of 14 matched |
| Existing defective-input tests | 22 rejected |
| Existing bunker-boundary tests | 4 passed |
| Existing repository unit tests | 18 passed |
| Publication mode | Correctly blocked, exit 2 |

Canonical YAML SHA-256: `e35c68bc166249f2e5244b0bec4a9f30c82ffb084f3c8c71725e49c76ff3e5ef`.
Full reformatted dossier SHA-256: `566b107d4707713bad252aec46f1aa5a2231ae23cb2d56895bb3e30a9e2ccc4e`.

These tests check presentation integrity and existing structural rules, not source meaning or legal currency.
No new sources were obtained. No independent marine review, graphic or PDF was produced.
The other 75 service dossiers, source originals and discovery registers are unchanged.
