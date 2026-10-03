# PILOT-01: presentation re-proof and continuation record

Date: 3 October 2026.
Service: Channel VTS / CALDOVREP, VTS-0001.
Research revision: 0.2.1-author-correction.
Presentation revision: proforma-1.
Outcome: PASS for the bounded presentation checks below. Research remains HOLD.

## 1. Where the preceding work ended

The project owner approved a Bulk Ports-style fixed pro forma with claim-level references. The approved implementation retains one canonical Markdown dossier with YAML front matter, presents reporting requirements in the body, separates the two transit directions and places the research history and evidence crosswalks in an appendix. Unresolved operational requirements must remain beside the affected instructions.

The presentation was already saved on `review/channel-vts-qc-20261003`, within open PR #15. This continuation did not redo the earlier research or alter the 76-service discovery inventory.

Inspected branch checkpoint: `d1b82038636e5b6738120d1b78e92f2ce561376c`.
Canonical file: `research/vts/VTS-0001/dossier.md`.
Presentation standard: `docs/vts-production/GUIDE_PRESENTATION.md`.

## 2. Exact inputs and scope

The input was downloaded through the GitHub connector from the completed presentation workflow, not reconstructed from chat history.

- Workflow run: `37109509176`.
- Artifact: `11269450650`, `channel-vts-proforma`.
- Artifact ZIP SHA-256: `0b326a93bb3c7fae874c63907f781d231d7a3edb56e2341f52a763c50a6591cc`.
- Artifact output checkpoint: `0a87381d308cb540aa7bd7e8c6803487eebaa20a`.
- Full dossier SHA-256: `566b107d4707713bad252aec46f1aa5a2231ae23cb2d56895bb3e30a9e2ccc4e`.
- Canonical YAML front matter, including delimiters, SHA-256: `e35c68bc166249f2e5244b0bec4a9f30c82ffb084f3c8c71725e49c76ff3e5ef`.

The original artifact reading copy exactly equals the dossier body with its leading blank line removed. The dossier and YAML were not modified.

The previous workflow records were inspected: 14 packet files checked, 22 defective research inputs rejected, four bunker-boundary tests and 18 repository unit tests passed, and publication mode remained blocked. Those are PREVIOUS execution results, not tests rerun in this continuation. This continuation ran the additional presentation checks in section 3 locally against the downloaded, hash-verified files.

No fresh operational-source, legal-currency, external-URL-availability or marine-approval check was performed. References were checked for presentation mapping and internal resolution, not independently reassessed for source meaning.

## 3. Additional executed presentation checks

Executable: `reviews/vts/checks/channel_presentation_reproof_20261003.py`.
Executed-script SHA-256: `adcd444914981257ee695b0ca83e0ee26b1d62294c3e6758693c0b8c3a758071`.

| Check | Observed result |
| --- | --- |
| Fixed main sections | 9, in the expected order |
| Transit directions | 2 |
| Event crosswalk | All 6 events retained |
| Main report-code groups | All 13 retained in order, with immediate references |
| Report information and recorded conditions | Compared with canonical YAML; field X has separate subitem checks |
| Evidence crosswalk | All 32 records retained |
| Bibliography aliases | R1-R8 retained |
| Original internal reference/gap targets | 16 distinct targets resolve |
| Open gaps | All 8 remain visible |
| Directional timing and contacts | Retained against canonical records |
| Calling-channel distinction | Calling role retained, not promoted to a working-channel assignment |
| Conditional obligations | Existing should wording and unresolved implementation gaps remain |
| Plotting limitations | Both published geometries and both missing-datum qualifications retained |
| Research status | HOLD; publication-ready remains false |

Twelve deliberately defective presentation variants were separately rejected:

1. Missing HOLD warning.
2. Replacing the persons-on-board count with vague personnel particulars.
3. Removing the SW VHF-range timing qualification.
4. Changing the NE calling channel.
5. Relabelling a calling channel as a working channel.
6. Making the bunker threshold inclusive instead of strictly greater than.
7. Applying the bunker threshold to navigational conditions.
8. Extending the confidential-cargo delivery option to the entire report.
9. Replacing should with must in the conditional-change wording.
10. Breaking the R2 bibliography anchor.
11. Presenting English ITZ notification as permission.
12. Removing the plotting warning.

These are pilot-specific regression checks. Passing them does not prove every possible presentation defect is detected, nor that the underlying operational research is current or complete. The checker deliberately refuses input other than the frozen proforma-1 dossier; a new research revision requires a reviewed checker update.

## 4. Portable reading-copy correction

An exported standalone reading copy contained five repository-relative appendix links. These are valid in the dossier's repository folder but do not resolve as intended when the Markdown is downloaded on its own.

The new export function changes those five links to absolute GitHub paths pinned to the inspected immutable commit. It also adds nine clickable contents entries and a provenance note identifying the exact canonical dossier.

All reporting text, conditions, sources, unresolved gaps and HOLD warnings are preserved. An exact reverse transformation confirms that removing only the export provenance and reversing the navigation-link changes reproduces the original body byte-for-byte in UTF-8.

Portable export SHA-256: `24797375c7bceaa292e903280e55800fb3fa0c7e44d16cb64152e53f9b5fe7bd`.

The portable reading copy is a generated delivery, not a separately maintained guide. It was not added beside the canonical dossier as a second master. No PDF or operational map was produced.

To reproduce from this repository checkpoint, with PyYAML available:

```sh
python3 reviews/vts/checks/channel_presentation_reproof_20261003.py \
  --export /tmp/Channel_VTS_Reading_Copy.md \
  --report /tmp/channel-presentation-reproof.json
```

The optional `--reading-copy` argument compares the original workflow reading copy with the canonical body. Without that input, the output reports that comparison as not performed. This tool writes only the explicitly requested export/result paths, never the canonical dossier or review packet.

## 5. Remaining work and limits

The reader-friendly presentation step and this bounded re-proof are complete. The pilot is not publication-ready. The next substantive work is to complete the source and current-instruction reconciliation already recorded in G01-G08, not start another round of cosmetic restructuring.

Priority remains the retained review sources, current UK/French/ALRS instructions, full reporting-line geometry and datum, communication roles and conditional-report implementation, and report formatting. Independent evidence review, marine approval and artwork checks remain required under the existing project gates.

Do not fill missing positions, call procedures, time standards or reporting exemptions from inference. Do not close a source gap merely because a live citation is present. Do not create a purportedly complete bridge instruction from a conditional event whose implementation is unresolved.

No source originals, operational YAML, packet hashes, other service dossiers or discovery-register rows were changed in this continuation. PRs #13, #14 and #15 remain unmerged. No release is authorised by this report.
