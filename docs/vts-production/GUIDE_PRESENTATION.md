# VTS guide presentation standard

Current structure: entry-2. Language standard: professional-1. Recorded: 3 October 2026.
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

## 4. Professional language standard

Language revision: professional-1, adopted from the Channel version 3 language edit on 3 October 2026.
This governs drafting, rewriting, review and reading-copy preparation. It is not optional final polishing.
The Channel reading draft supplies stylistic examples only, not approved operational facts for reuse.

### 4.1 Register and terminology

Write as a professional maritime reference work: factual, direct and restrained.
Use UK spelling and the third person. Do not address the reader or use conversational questions.
Use established maritime terminology instead of elaborate substitutes for familiar concepts.
Keep the same technical term for the same subject; do not vary terminology merely to avoid repeated words.
Explain an unfamiliar abbreviation at first use when its meaning is established by the evidence.

Prefer a named subject and a direct verb when the responsible party is known.
Use passive construction where the actor is unknown or the operational subject properly takes priority.
Do not invent an actor, duty or causal explanation to make a sentence more active.
Use adjectives and adverbs only where they define a relevant distinction.

Keep authored prose sentences within 20 words. Vary sentence length without producing disconnected fragments.
Preserve exact quotations, official titles, codes and technical notation; do not distort them to meet that limit.
Use short subject headings, normal punctuation and no em dashes.
Concise table entries may use standard noun phrases, such as 'Total number of persons on board.'

### 4.2 Remove drafting commentary and formulaic language

State the fact, procedure or limitation directly. Do not explain that the text states it clearly or preserves it accurately.
Remove commentary about the writing process, source selection, retained qualifications or reasons for organising the entry.
Place necessary research decisions and detailed source comparisons in Appendix A.
Retain concise source attribution in the main entry where it explains a disputed or uncertain requirement.

Delete empty framing such as 'This distinction matters' and stock statements about the importance of a subject.
Do not introduce ordinary facts with 'It is important to note' or similar announcements.
Avoid promotional claims, metaphors, rhetorical contrasts and repeated claims of clarity, completeness or reliability.
Do not use 'not merely X but Y', 'serves as' or 'plays a key role' as stock sentence frames.
Use simple connections between sentences; remove repeated transitions that add no logical relationship.
Avoid generic seamanship advice, moralising, motivational language and unsupported statements about benefits or risks.

Review the sentence's purpose, not just a list of flagged words.
Professional language cannot be established by an AI-detection score or by replacing conspicuous vocabulary with synonyms.

### 4.3 Explain what needs explanation

Each sentence must supply a fact, necessary explanation, material qualification or useful cross-reference.
Explain the relationship between the service, reporting scheme, vessel category and reporting event where needed.
Do not assume professional readers need elementary explanations of familiar maritime terms.
Do not omit an unfamiliar local procedure merely to make the entry shorter.

A table may follow its heading directly when its purpose and qualifications are already clear.
Do not require an introductory paragraph, a table and a concluding summary under every heading.
Use prose before a table only when it adds context, scope or an explanation not apparent from the table.
Do not repeat every table row in prose or end each section by restating its opening.
Repeat a value or caution where separate directions or reference tables need it for correct interpretation.
Check those repetitions against the same canonical record.

Remove redundancy, not substance. Do not set a percentage reduction or imitate another entry's word count.
Describe an official report code's subject without inventing transmission syntax or nil-report conventions.

### 4.4 Preserve technical meaning and necessary cautions

Language edits must preserve the reporting subject, actor, trigger, timing, recipient, method, applicability and source reference.
Retain every supported condition, exception, numerical operator, unit and distinction between requirement strengths.
Do not replace 'should' with 'must', or an unconfirmed duty with a statement that no duty exists.
Keep calling channels distinct from working channels, and conditional reports distinct from scheduled calls.
Do not simplify an individual field condition into a whole-report exemption.

State an uncertainty precisely: identify the unconfirmed value, procedure or source scope.
Prefer a direct limitation over a paragraph about what the researcher did or did not establish.
Do not replace specific gaps with a general instruction to consult current publications.
Keep material limitations beside the affected instructions and retain the required DRAFT/HOLD notice.
Remove repeated boilerplate only when no independently used direction, table or instruction loses its necessary warning.
Do not present incomplete reporting geometry as suitable for plotting.

### 4.5 Edit examples

These illustrate language treatment, not operational instructions or universal replacement rules.

| Wording to revise | Preferred treatment |
| --- | --- |
| 'The distinction between the service and the reporting system matters.' | Define the service and reporting system directly; delete the announcement. |
| 'provides a route to the general ship-reporting format' | 'is the general ship-reporting format reference' |
| 'The number of people aboard, including everyone carried rather than crew alone.' | 'Total number of persons on board.' |
| 'Both qualifications are retained here; neither introduces a two-mile south-westbound trigger.' | State the supported timing and its qualification directly; remove commentary about retaining them. |

Apply an edit only after checking that it preserves the intended factual meaning.
Do not copy the example service's facts into another entry.

### 4.6 Required language pass

After content and structure edits, read the complete mariner-facing entry as a standalone reference work.
Check for drafting commentary, empty framing, inflated wording, forced introductions, repetitive summaries and unnecessary explanation.
Check terminology, sentence length, UK spelling, headings and punctuation.
Do not use a word blacklist as a substitute for reading the complete entry.

Then compare the edited assertions with their pre-edit wording, canonical data and available evidence.
Check every operational value and qualification, including citations attached to shortened paragraphs and table rows.
Record language findings separately from operational-source findings, with locations and actual dispositions.
Record the entry revision, reviewer role, checked scope and any checks not performed.
An author-side language pass is not an independent review, originality clearance or operational fact-check.
Any change affecting operational meaning must return to the correction and re-proof process.
Recheck affected citations, links and warnings after the final edit.

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
Complete the professional-language pass in section 4.6 before issuing a revised reading copy.
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

Entry-2 remains the structural standard under master prompt version 1.1.
Professional-1 adds the language requirements in section 4 for all subsequent assignments and authorised revisions.
The Channel version 3 reading copy is a stylistic example, not an approved operational source or canonical dossier migration.
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
