# VTS guide presentation standard

Current standard: entry-2. Recorded: 3 October 2026.
Applies to subsequent assigned entries and authorised revisions.
Approval of this writing standard is not approval of any service's operational content.

## 1. Editorial purpose

Produce an encyclopaedic reference entry for mariners, not a research summary or an audit report.
Explain the service, its operating area, participation and reporting arrangements in connected, original prose.
Use concise tables for information that mariners need to compare or retrieve.
Do not replace explanation with a succession of metadata fields.

The Bulk Ports approach supplies consistent structure and immediate source references.
It does not supply cargo, berth or terminal sections, or operational facts to copy into VTS entries.
The Channel example establishes an editorial approach, not universal reporting procedures.

## 2. One canonical record

Each service retains `research/vts/<VTS-ID>/dossier.md` with YAML front matter.
YAML is the canonical operational data. The body is its mariner-facing entry followed by a separated editorial appendix.
Operational values appear in prose and tables through controlled mappings to the same YAML records.

This entry-2 body standard supersedes earlier descriptions of the main body as research narrative or review commentary.
It does not alter the YAML schema, source controls or approval gates.
Research history and exact source wording remain available in their appropriate evidence records.

Reading copies are versioned derivatives, not separately edited masters.
A proposed style rewrite may be issued for review without replacing the canonical dossier.
Identify it as a proposed rewrite and retain its exact evidence basis.
Never describe an authored rewrite as a byte-identical export.

## 3. Fixed reader-facing structure

Use `research/vts/templates/guide.entry-v2.md`.

| Section | Reader-facing content |
| --- | --- |
| 1. Service and operating area | Service identity, role, provider and geographical context; distinguish linked schemes and neighbouring services. |
| 2. Participation and applicability | Affected vessels, precise thresholds, requirement strength, exemptions and scope qualifications. |
| 3. Reporting procedures | Separate directions and route variants; explain triggers, timing, recipients and report obligations. |
| 4. Information to report | Every applicable official report-code group, its meaning, order and individual conditions. |
| 5. Communications and watchkeeping | Calling and working channels, watch requirements, transfers, supported alternatives and failure arrangements. |
| 6. Special circumstances | Conditional changes, defects, route decisions, specialist operations and related-service interfaces within scope. |
| 7. Boundaries and reporting locations | Published geographical definitions, geometry types, datum, reporting-line descriptions and limitations. |
| 8. Operational limitations | Material limits on the entry's use; no hidden unresolved duty or unsupported negative finding. |
| 9. References | Complete reader bibliography with precise source identification and recorded version/access information. |

Appendix A contains evidence/source crosswalks, acquisition status, conflicts, gaps, review records and change history.
Use references and brief qualifications in the main entry, not internal evidence IDs or packet hashes.
Do not remove an operational warning when moving its detailed investigation into the appendix.

Retain a section when research is incomplete. State the precise limitation without filling it with stock text.
Do not describe an unresearched subject as inapplicable or free of reporting duties.
Hours, historical background, service functions and local traffic context require their own evidence.
Encyclopaedic means explanatory and sufficiently complete within the declared scope, not padded to a word target.

## 4. Explanatory prose

Write in UK English and the third person, using established maritime terminology.
Keep sentences short, normally no more than 20 words. Do not use em dashes or promotional language.
Explain unfamiliar abbreviations when their meanings are established by the evidence.
Avoid second-person advice and generic seamanship that the entry does not substantiate.

Lead substantive sections with a useful explanation before any table.
For example, explain which movement triggers a report before listing its recipient and calling channel.
Describe an official report code's subject without inventing a transmission syntax or nil-report convention.

Do not repeatedly announce that a source was found, a field was recorded or an author resolved a conflict.
Present the supported subject directly; put the detailed source comparison in Appendix A.
Use a short point-of-use limitation where the instruction remains uncertain.

## 5. Originality and attribution

Build a factual outline from the evidence, then write a fresh explanation.
Do not draft by replacing words in source sentences or copying their distinctive paragraph construction.
Do not reproduce prose from neighbouring entries or unattributed translations.

Keep names, call signs, codes, numerical values, units and established technical terms accurate.
These are not rewritten merely to make text appear different.
Exact source wording belongs in the evidence record or a short, clearly attributed quotation where necessary.
A reference is not a substitute for quotation marks around copied distinctive wording.

Check distinctive overlapping phrases against source texts actually available for comparison.
Review each flagged match in context, distinguishing technical labels and data from expressive prose.
Record sources checked, excluded sources, findings and amendments.
A scan result is not an originality certificate; no score proves that an entry is plagiarism-free.
Do not claim a whole-web or full-source comparison that was not performed.
Keep reproduction permissions separate from attribution and originality checks.

## 6. Claim-level references

Cite each factual paragraph, item or table row at the point of use.
Use a precise clause, heading, table item, annex or PDF page rather than a whole-document reference.
Several assertions in one paragraph require citations that support all of them.
Background facts require references just as operational particulars do.

R1, R2 and similar labels are local bibliography aliases, not new source identities.
Map each alias to the source catalogue and its exact version.
Distinguish PDF page order from printed page numbers.
Use `Appendix, item W` where W is a report item, not the name of a separately lettered appendix.

The bibliography records issuer, title, edition/date, original URL and the recorded access date.
Do not invent missing metadata or imply current verification from an old access record.
Archive and rights details remain in Appendix A unless their absence limits operational use.
A live consultation is not proof that an original is held for independent review.

## 7. Operational meaning must survive rewriting

Retain every reporting event and all applicable directions without assuming symmetry.
Keep pre-entry, entry, transfer, departure and conditional reports distinct.
Conditional event order is not necessarily a sequence of routine calls.

Preserve requirement strength and exact threshold operators.
Apply each condition to the proper report, field or subitem.
A conditional cargo option must not exempt the whole report.
Calling channels must not be relabelled as working channels without evidence.
AIS capability alone does not establish a reporting exemption.

Retain published geometry, precision, reference features and uncertainty.
Do not replace an obsolete or missing feature with an assumed successor.
State missing datums and incomplete geometry beside the affected description.
Do not supply a purportedly complete bridge instruction where contact selection, timing or report content remains unresolved.

## 8. Presentation and export checks

Compare the completed entry with canonical data and source meaning, not only expected strings.
Check all sections, directions, event subjects, report groups, qualifiers, references and limitations.
Record checked and unchecked populations.

For presentation-only work, verify canonical YAML bytes are unchanged.
For navigation-only exports, verify an exact reverse transformation to the source body.
For authored rewrites, perform a claim-by-claim semantic comparison; a text-equality claim would be false.

Reading copies must retain citations, bibliography, status and all operational qualifications.
They may omit YAML and Appendix A.
Supply clickable contents and valid, unique anchors.
Convert repository-relative links to absolute immutable-commit URLs for standalone copies.
Check the converted targets and identify the canonical revision.

Use negative tests suited to the actual service and implementation.
Examples include changed channels, omitted qualifiers, altered thresholds, false exemptions, broken references and weakened warnings.
Record NOT_RUN where no suitable checker exists; do not import the Channel pilot's counts as universal acceptance criteria.
Passing presentation tests does not certify source currency, operational accuracy, originality or marine approval.

## 9. Adoption and version control

Entry-2 is the standard for subsequent assignments under master prompt version 1.1.
Existing entries are not automatically migrated, approved or released.
The frozen Channel proforma-1 dossier and its packet remain an earlier reviewed input until an authorised migration updates them.

Retain `research/vts/templates/guide.proforma.md` for historical reproduction.
Do not overwrite it: the Channel packet records its exact hash.
The existing Channel renderer and frozen presentation checker do not implement entry-2.
Use a separately reviewed adapter for any new deterministic rendering workflow.
Do not alter pinned hash constants to make a new entry pass an old test.

After an authorised migration, commit the revised dossier, assemble a new packet and record the exact input versions.
Do not replace historical results with claims that the new version has already passed them.
All existing independent, marine, artwork and release gates remain in force.

## Appendix H. Historical proforma-1 implementation

The former presentation standard was applied to Channel VTS only.
It used nine fixed sections plus Appendix A and retained the canonical research YAML.

Historical files:

- `research/vts/templates/guide.proforma.md`
- `scripts/render_channel_proforma.py`
- `research/vts/VTS-0001/presentation_check.json`
- `reviews/vts/checks/channel_presentation_reproof_20261003.py`
- `reviews/vts/reports/PILOT-01__presentation_reproof_2026-10-03.md`

The earlier presentation workflow was `37109509176`, job `111164528235`.
Its recorded output checkpoint was `0a87381d308cb540aa7bd7e8c6803487eebaa20a`.
The previous record reports 14 matching packet files, 22 rejected defective inputs, four bunker-boundary tests and 18 repository tests.
Publication mode remained blocked with exit 2.
These are historical results, not tests rerun or extended to entry-2 by this standards revision.

Historical canonical YAML SHA-256: `e35c68bc166249f2e5244b0bec4a9f30c82ffb084f3c8c71725e49c76ff3e5ef`.
Historical proforma-1 dossier SHA-256: `566b107d4707713bad252aec46f1aa5a2231ae23cb2d56895bb3e30a9e2ccc4e`.
No operational source, independent approval, graphic or PDF is created by adopting entry-2.
