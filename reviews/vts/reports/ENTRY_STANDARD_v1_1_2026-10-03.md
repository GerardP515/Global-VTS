# Entry-2 standard adoption and Channel writing specimen

Date: 3 October 2026.
Decision basis: the owner requested a standard going forward, then specified encyclopaedic entries for mariners with original writing.
This is an author/editorial change record, not an independent review or publication approval.

## Standard adopted

Master prompt `VTS_RESEARCH_PROMPT.md` is now version 1.1.
Presentation standard: `entry-2`.
It applies to subsequent assigned entries and authorised revisions.

The main entry now explains the service and reporting arrangements in original prose, supported by claim-level references.
It is not a description of research activities or a collection of metadata fields.
Tables support look-up tasks after the relevant explanation.
Research, source conflicts, archive details and review history remain in a separated editorial appendix.
Operational uncertainties remain beside affected instructions and in the limitations section.

One YAML-backed canonical dossier per service remains the data model.
Reading copies and graphics remain derivatives, not competing operational masters.
No source, independent-review, marine, artwork or release gate has been relaxed.

## Changed instruction files

- `VTS_RESEARCH_PROMPT.md`
- `docs/vts-production/GUIDE_PRESENTATION.md`
- `research/vts/templates/guide.entry-v2.md` (new)
- `reviews/vts/REVIEWER_PROMPT.md`
- `reviews/vts/CORRECTION_REPROOF_PROMPT.md`

Comparison of base `bf9aa8f83661b5f5e76b47d273e87e3a984fe757` with instruction checkpoint `8df593c355c17a06e0f1f2d6b04f0a835191f8fa` confirmed those five changed files.
No operational dossier, source original, register, historical template or review packet changed at that checkpoint.
The historical Channel template is preserved because its hash belongs to the existing frozen packet.
The old Channel renderer and frozen checks are not presented as entry-2 implementations.

## Proposed Channel reading version

A proposed original-prose rewrite was produced as a conversation attachment:
`Channel_VTS_Encyclopaedic_Entry_v2.md`.
It is a writing specimen for editorial review, not a replacement canonical dossier or a completed operational guide.
It contains the nine entry-2 sections, separate through-transit directions, the 13 report-code groups and eight source references.

Evidence basis: existing Channel research revision `0.2.1-author-correction` at the recorded baseline.
Canonical dossier SHA-256: `566b107d4707713bad252aec46f1aa5a2231ae23cb2d56895bb3e30a9e2ccc4e`.
Specimen SHA-256: `25a422b41d4e98fbc60c193afbcb599d4faabda89b0ac2d51717cd5ee9786fd7`.
Specimen size: 18,141 bytes, UTF-8.

The specimen was checked locally against the downloaded, hash-verified earlier dossier.
Source-reference metadata was reconciled with the existing repository catalogue, not fresh external research.
No new operational facts, source acquisitions, source-currency checks or approvals are claimed.
The specimen links to the immutable canonical evidence record and preserves DRAFT / HOLD status.

## Executed author-side checks

Local checker: `check_entry_v2.py`, retained with the conversation working files.
Result record: `Channel_VTS_Entry_v2_Author_Check.json`, also in the conversation working files.
These files are not represented as a general repository validator.

Observed checks:

- Nine expected sections and clickable contents entries.
- Two through-transit directions.
- All 13 main report-code groups in canonical order, each with a precise source reference.
- Seventeen unique explicit anchors and 77 internal links, with no unresolved internal targets.
- Eight bibliography records and no repository-relative links in the standalone copy.
- Three published coordinate strings compared directly with canonical geometry text.
- Presence checks for recorded threshold, timing, calling-channel, condition-scope and HOLD qualifications.
- No unresolved authoring placeholders or em dashes in the reading copy.

An author-side semantic read compared the rewritten procedures, fields and qualifications with the existing canonical record.
This was not an independent review against newly consulted original sources.
String checks do not prove full semantic accuracy or operational completeness.

## Original-writing assessment and limits

The prose was written afresh from the factual structure rather than by replacing words in source sentences.
Official names, codes, positions and numerical conditions were retained where technical accuracy requires them.
Source references remain at point of use.

A local comparison with the preceding supplied proforma-1 reading copy found no matching ten-token windows in the main prose.
The comparison lowercased and tokenised the text, excluded bibliography sections, and removed Markdown links and HTML tags.
This is a limited draft-to-draft comparison, not proof of originality against every source.
Full-original-source comparison and whole-web plagiarism scanning were NOT_PERFORMED.
No guaranteed plagiarism-free certification is claimed.

The frozen Channel research/presentation validators and repository unit tests were NOT_RUN during this writing-standard change.
No suitable entry-2 general validator has been installed by this work.
Historical test results have not been assigned to the new specimen.

## Remaining boundary

The Channel operational dossier, YAML, packet and research HOLD remain unchanged.
Replacing the canonical prose later requires an authorised migration, a revised packet and the applicable re-proof and review stages.
Existing source-retention, current-instruction, geometry, communications and marine/artwork gaps remain open.

All changes are on `review/channel-vts-qc-20261003`, within PR #15.
This record does not authorise merging, release, bulk conversion of other services or unattended research.
