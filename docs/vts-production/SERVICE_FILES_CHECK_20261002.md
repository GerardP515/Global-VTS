# Service-file setup check

Date: 2 October 2026
Scope: one Markdown workspace per existing TSS-derived service.

## Output

- 76 service directories, each containing one `dossier.md`.
- 76 unique canonical service IDs; no new service IDs allocated.
- Existing classes retained: 67 Core and 9 Supplemental.
- A regional index links to every dossier once.
- The exact 17-column register blob is retained under `research/vts/inputs/`.
- All dossiers are `REGISTER_SEED_ONLY` and `NOT_STARTED` for production research.

## Input provenance

The source register is `data/current/TSS_Derived_VTS_Final_Register.csv` from commit
`0de8d3247dc77caa68d699f68d753fa5e213c5e8`, blob `5aa536d0f55b737750496514ce1a06653e9a6eaf`.
Its Git blob was reused unchanged. This does not merge its branch or overwrite live registers.
The previously exported workbook supplied a local field projection for mechanical file construction.
The corresponding live regional register and source register revision were read before construction.

## Checks performed

Local Python checks covered all 76 IDs, class totals, six section headings, inherited TSS strings and source-ID strings.
The full contents of all 76 Markdown files were hashed as Git blobs.
Their expected combined subtree, including the unchanged protocol files and register input, was calculated locally.
The resulting tree `e365b213a7af08e04284b8cb2e41fcdea7ae4d13` matched GitHub's tree before index/readme additions.
This verifies that all 76 remote file contents match the locally checked files, not only their filenames.

## Limits

This is file creation and inventory organisation, not fresh operational research.
No authority sources were downloaded or revalidated. No independent marine review or publication approval occurred.
No legacy register, membership count, TSS disposition, source archive or pilot research status was changed.
Full legacy repository tests were not run in this setup task.
Research remains subject to `VTS_RESEARCH_PROMPT.md` and its separate approval gates.
