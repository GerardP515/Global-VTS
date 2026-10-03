# Great Belt VTS: canonical correction and re-proof

**PILOT-02 / VTS-0002 | 3 October 2026 | Research revision 0.2-author-correction**

The owner authorised incorporation, re-proof and repository merging. Publication approval was not authorised.
The corrected entry and YAML now occupy the existing `research/vts/VTS-0002/dossier.md`.
This report records author work, not independent or named marine approval.

## Corrections incorporated

The original review remains unchanged at `PILOT-02__fact_style_review_2026-10-03.md`.
The original 0.1 packet is preserved under `reviews/vts/packets/PILOT-02__0.1__packet.json`.

| Finding | Canonical treatment | Remaining qualification |
| --- | --- | --- |
| F01 | Both advance-delivery options now require A/H when used; reader wording corrected. | The advance method remains optional or recommended, not compulsory for every ship. |
| F02 | ETR recommendation, conditional minimum 60-minute arrival lead and mandatory entry VHF recorded separately. | G02 retains form/acknowledgement and combined EEZ/VHF-range timing questions. |
| F03 | East Bridge subsection 10(3), sailing-vessel qualification and exact-20 m overlap recorded. | New G07 and conflict C05 remain open; no boundary-case route decision invented. |
| F04 | West Bridge 104 m span width and central 70 m clearance width recorded with the mean-water-level reference. | No vessel-specific clearance or plotting approval. |
| F05 | TSS 20-knot recommendation and provider below-20-knot bridge advice have separate scopes and operators. | Neither is presented as a statutory speed limit. |
| F06 | Both communications records state the watch requirement's radio-carriage scope. | Reporting participation and radio-watch applicability remain separate. |
| F07 | Order 1171, its applicability and cargo definitions added to YAML, evidence and references. | Complete amendment history and cargo-specific assessment remain outside approval. |
| F08 | General provider anchoring statement recorded without creating an unsupported full-report event. | New G08 retains BELTREP implementation questions. Confirmed pre-departure reporting remains. |
| F09 | DW-T4 and Route Hotel recommendations retain greater-than-10 m and 10 m-or-less conditions. | Advisory status preserved. |
| F10 | Order 1171 added to the coded-position comparison. | G03 and C04 remain open; published boundary coordinates are unchanged. |
| L01-L05 | Research-process commentary removed or shortened; direct maritime wording used. | Source comparisons needed to explain uncertainty remain beside affected instructions. |

All findings have dispositions in `correction_dispositions.json`. Acceptance does not mean an underlying uncertainty is resolved.

## Further re-proof findings

Order 1171 contains its own W-reporting inconsistency. Annex 4's opening summary permits AIS, while its W row specifies non-verbal reporting.
The source comparison is recorded in C01 and the reader. Order 820's explicit W procedure was not removed.

The earlier EV-DELIVERY evidence record pointed to a nonexistent `reporting_policy.delivery` field.
It now maps to the actual voice-reporting and AIS-policy fields. No operational value changed through that link repair.

The master prompt's compulsory table-introduction instruction conflicted with professional-1.
That sentence now permits a table directly beneath its heading when context and qualifications are already clear.
No wider schema migration or batch-production authorisation is claimed.

## Source record

The existing 88-file source-bundle manifest was checked against actual bytes and hashes.
Order 1171 was additionally captured and its PDF signature, byte count and hash checked.
The catalogue now contains ten captured responses: nine substantive sources and one non-operational application shell.
The reader cites eight bibliography records. Comparison-only material remains catalogued without becoming an extra reader reference.

New original: `P02-DK1171__20261003T104013Z__d7eeeb09921e.pdf`.
SHA-256: `d7eeeb09921ed8d53efc666ef0a1ceed60d148ffc8f8c64c8438a26ae69d8db0`.
Size: 269,617 bytes. Capture completed 3 October 2026 at 10:40:13 UTC.
Capture run: `37117171014`. Artefact: `11271423361`; expiry: 2 November 2026 at 10:40:13 UTC.

No complete original publication was placed in the public repository archive.
Sources remain in temporary review artefacts. Durable authorised storage and republication rights remain open under G04.
Mechanical text and page images were generated locally for the new original; their creation does not establish independent review.

Source locators are recorded in YAML and the bibliography, principally:

- Order 820: sections 3-5, 8 and 10-12; Annexes 1-2.
- MSC.332(90): sections 3, 6.4.3 and 6.6.1-6.7.1; reporting Appendix 3.
- Provider VTS overview: Storebælt ETR, speed, works and general anchoring paragraphs.
- Order 1171: sections 1, 4-5 and 8; Annex 4, including C, P, T and W.
- MSC.332(90)/Rev.1: operative commencement provisions and future Appendix 3 X.

The future instrument remains separated from current reporting particulars. No early insurance requirement was introduced.

## Author re-proof and checks

The first pass covered all nine reader sections and their canonical changes, figures, source bindings and review findings.
The two further findings above were addressed before local snapshot `2545c56df688eac463ac7706ff8bd7eadd0a69c7`.
The second pass checked the complete corrected entry and YAML relationships from that committed local snapshot.
This snapshot is a local audit checkpoint, not a GitHub commit or independent review.
No additional operational correction was identified in the second pass; the research cutoff metadata was then refreshed.
Detailed scope and exclusions are recorded in `correction_reproof.json`.

The new checker is `reviews/vts/checks/great_belt_correction_check.py`.
The original revision-0.1 checker and historical results remain unchanged.

Executed locally against the corrected dossier:

| Check | Result |
| --- | --- |
| Original and correction-specific faulty variants | 40 rejected |
| Participation boundary cases | 12 passed |
| Bunker-GT boundary cases | 3 passed |
| Future effective-date boundary cases | 3 passed |
| Evidence records / resolved field paths | 68 / 74 |
| Reporting events / channel-change actions / advance options | 6 / 2 / 2 |
| Directions / report-code groups / coordinate rows | 2 / 15 / 10 |
| Reader references / internal links | 8 / 149; all targets resolved |
| Existing source-bundle files | 88 size/hash matches |
| Additional original | 1 size/hash match; catalogue binding checked |
| Open gaps | G01-G08 retained |
| Existing repository unit tests | 18 passed |
| Register validation | Passed |
| Release-mode check | Blocked as required, exit 2 |

No authored prose sentence exceeded 20 words under the recorded check; tables, bibliography and metadata were excluded.
No new whole-source or whole-web plagiarism scan was performed. No originality certificate is claimed.
Automated results test structural consistency and defined regressions, not complete legal currency or marine accuracy.
Remote execution results, once run, belong in a separate `correction_remote_check.json`, not in historical test records.

## Merge boundary

Dossier SHA-256 at local closing check: `4fec09e293317f66cb0e546573f7e78cae29367668a3f34818e65096aece3c30`.
The new review packet must pin the actual research commit and exact files after remote application.
Merging does not change `HOLD`, `publication_ready: false`, or any independent, marine, artwork or release record.
The eight gaps concern currency, ETR, position encoding, source storage, approvals, exit/radio-failure details, bridge length and anchoring implementation.

Channel VTS and the discovery registers are outside this correction. PILOT-02 alone receives a new status checkpoint.
The owner-authorised merge includes the dependent protocol, Channel and style branches; it does not approve publication of either guide.
