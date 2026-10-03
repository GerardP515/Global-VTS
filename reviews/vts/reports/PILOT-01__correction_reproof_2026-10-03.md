# Channel VTS pilot: correction and re-proof record

Date: 3 October 2026. Service: VTS-0001. Study: PILOT-01.
Role: ChatGPT author-side correction and re-proof. No independent non-author or marine approval.
Original review: `PILOT-01__qc_2026-10-03__c5fde2d.md`.
Original research revision: `0.1.0-author-sample`.
Corrected revision: `0.2.1-author-correction`.
Corrected dossier SHA-256: `5ac557049d0e7e2d644fc25167206b64831351ebd1aafbbb6f595ccf7eec0341`.
Research/code input commit: `f444892bc2dcd2bbfa6fbe1f730a12717aea2c91`.
Executed final validation checkout: `cb6dcb2d4ff7a9d8f908cd145014317a682e3377`.

## Verdict

**Recorded content corrections applied. Draft structural integrity passes. Publication HOLD remains.**

The six content/data findings QA-01 to QA-06 were accepted and corrected within the declared pilot scope.
QA-07 was addressed by a new, tested pilot validator. The historical validator remains unchanged for replay.
The full corrected package was re-proofed twice on the author side.
These checks do not replace a complete retained-source review or named marine approval.

## Finding dispositions

| Finding | Disposition | Change and evidence |
|---|---|---|
| QA-01 | ACCEPT / APPLIED | SW event now holds both source-specific timing conditions and a reconciled display summary. EV-SW-TIMING links directly to the event. SRC-004 mandatory-reporting SW paragraph; SRC-005 section 3.10. |
| QA-02 | ACCEPT / APPLIED | W expressly requests a total number, rather than describing persons carried. P01-IMO251 Appendix W, PDF page 3. |
| QA-03 | ACCEPT / APPLIED | Q/R retains the structural, cargo and equipment reporting scope. P01-IMO251 Appendix Q/R, PDF page 3. |
| QA-04 | ACCEPT / APPLIED | X has separately identified subitems and a typed bunker-only condition. The parent remains one official code group. P01-IMO251 Appendix X, PDF page 3. |
| QA-05 | ACCEPT / APPLIED WITH OPEN IMPLEMENTATION GAP | English ITZ decision notification is a conditional event in each direction. Exact current contact handling remains G08. Special-operation variants have explicit proposed scope exclusions, not vessel exemptions. SRC-005 sections 3.4, 3.9, 5.1(iv), 6.4; SRC-004 ITZ paragraph; P01-IMO85 Annex 2 section 3.3. |
| QA-06 | ACCEPT / APPLIED WITH OPEN IMPLEMENTATION GAP | A scoped advance non-verbal confidential-cargo option is recorded. No whole-report exemption or delivery address is invented. Current implementation remains G04. P01-IMO85 Annex 2, PDF pages 11 and 13. |
| QA-07 | ACCEPT / IMPLEMENTED AND TESTED | All seven previously missed defective-input cases are rejected by validate_channel_pilot_v2.py. Draft integrity and publication readiness have separate outcomes. |
| QA-08 | ACCEPT / PARTIAL SOURCE ROUTE RECORDED | A.851(20) is catalogued and its Appendix paragraph 2 inspected. No current encoded reporting example or nil convention is claimed. Retention, amendments and provider implementation remain open. |
| QA-09 | ACCEPT / LEDGER STARTED | effort.csv records a prospectively timed machine-validation stage. No retrospective human production effort is invented. The pilot still cannot establish full publishing labour. |

## Correction cycle

### Stage 1: apply existing findings

The one-shot correction required exact original dossier and catalogue hashes before writing.
It changed only this pilot's dossier and catalogue; unrelated guides and inventories remained untouched.
Checkpoint: `f8a6580195d0137cfbdd5f8c00d6d1ca14514a44`, revision 0.2.0.

### Stage 2: first complete re-proof

Read the corrected YAML and narrative, all report fields, both event sequences, source mappings, gaps and conflicts.
Compare held MCA provisions with the archived material and reopened authority pages.
Compare the unretained IMO and supporting provisions live, including the relevant PDF table/annex page images.
The exact earlier unretained source versions cannot be reconstructed; this limitation remains explicit.

The first re-proof recorded RR-01 to RR-03 in `PILOT-01__first_reproof_2026-10-03.md`.
These concerned channel-role qualification, a missing boundary-label table column and Boolean sequence acceptance.

### Stage 3: apply first-reproof findings

Retain the published calling channels; leave separately modelled working-channel assignments unknown under G04.
Regenerate the directional table with labels from the existing reporting objects.
Reject Boolean sequence values and test that failure case.
The corrected dossier advanced to 0.2.1 without changing source geometry or adding approval claims.

### Stage 4: second complete re-proof

Re-read the 0.2.1 dossier whose Git blob is `8d87af0a9d46e1c1363ae73f8bc5f97e389b0c13`.
The local byte identity was checked against the remote blob before closing this stage.
Review every main report-code group, both X subitems, three report types and all six event records.
Review the 32 evidence records and their declared source scope, all eight gaps and four conflict dispositions.
Confirm the entry table follows the canonical YAML timing, recipient, channel and boundary references.
Confirm conditional sequence numbers describe display order, not scheduled reporting points.
No further operational correction was accepted after this second pass within the declared source scope.
Remaining source, interpretation, geometry and approval limitations are not treated as checked absences.

### Stage 5: closing controls

Regenerate packet hashes, retain historical author_check.json as the original 0.1 review record, and update the pilot status ledger.
The original review report and original validator are preserved.
Run the corrected draft validator, its defective-input tests, its release-blocking mode and the existing repository tests.
No merge, artwork or PDF release is performed.

## Corrected population

| Object | Count |
|---|---:|
| Services | 1 |
| Directions | 2 |
| Events | 6 |
| Entry events | 2 |
| Conditional event records | 4 |
| Report types | 3 |
| Official CALDOVREP code groups | 13 |
| X subitems within the existing code group | 2 |
| Evidence records | 32 |
| Evidence records with retained source snapshots | 10 |
| Evidence records limited to live comparison | 22 |
| Catalogued sources | 8 |
| Retained originals | 2 |
| Unretained originals | 6 |
| Open gaps | 8 |
| Existing conflict dispositions retained | 4 |

The six event records do not mean that each vessel must make six routine calls.
Each direction has one entry event, one conditional navigation-change event and one conditional English ITZ notification.
The new G08 is an explicit implementation gap, not proof that the earlier seven gaps were closed.

## Evidence re-proof coverage

All 32 records were accounted for, without sampling safety-bearing report fields.

Retained-source comparison: EV-IDENTITY, EV-THRESHOLD, EV-EXEMPT, EV-NE, EV-SW, EV-SW-TIMING,
EV-OLD-LIST, EV-AIS, EV-ITZ-MGN and EV-ITZ-DETAIL.

Live-source comparison only: EV-THRESHOLD-IMO, EV-FERRY, EV-AMENDMENT, EV-CHANGE, EV-RS,
EV-FUTURE, EV-PORT, EV-F01, EV-F02, EV-F03, EV-F04, EV-F05, EV-F06, EV-F07, EV-F08,
EV-F09, EV-F10, EV-F11, EV-F12, EV-F13, EV-CARGO-OPTION and EV-FORMAT-ROUTE.

For the latter 22 records, exact retained-snapshot verification remains NOT_CHECKED.
The source catalogue supplies URLs, issuers, precise locators and stated limitations.
Source-locator support is not a certification that all later amendments were found.

## Executed tests

Workflow: https://github.com/GerardP515/Global-VTS/actions/runs/37107680752
Job: 111159312069. Conclusion: success.

| Check | Result |
|---|---|
| Corrected draft integrity | PASS |
| Packet paths, byte sizes and SHA-256 | 11 of 11 matched |
| Held original/text file hashes | 4 of 4 matched |
| Deliberately defective input tests | 22 rejected |
| Previously missed QA-07 cases | All 7 rejected |
| Bunker boundary tests | 4 passed: below, equal, above, unknown |
| Publication command | Correctly returned exit code 2, not approved |
| Existing register structural validator | PASS: 224 TSS and 76 service records unchanged |
| Existing unit tests | 18 passed |
| Working-file changes caused by tests | None |

Unknown bunker quantity triggers review, not zero or an automatic exemption.
The other X subitem remains within the parent report at every tested bunker boundary.
A successful workflow means these checks ran successfully, not that the guide is publication-ready.
The validator is pilot-specific and does not establish semantic truth from a populated evidence reference.

## Source retention and remaining blockers

No new original source was captured in this correction pass. The two existing MCA originals remain unchanged.
The eight-source catalogue includes the newly recorded A.851(20) format reference, so six originals remain unretained.

The public IMO website terms do not establish permission for complete originals in this commercial-development public archive.
Any publisher-specific licence and authorised review-store arrangements remain to be confirmed.
The other unretained sources also lack a confirmed redistribution basis in this packet.
This records a rights check, not a conclusion that permission cannot be obtained or that factual research must stop.
See `research/vts/VTS-0001/rights_review.json` and its policy URLs.

Keep HOLD for source retention, current ALRS/UK/French notices, complete plotting geometry, current communications implementation,
conditional-change handling, report formatting and independent marine/artwork approval.
Current calling-name and other implementation questions are not closed by copying older source statements.
No map or PDF was created, and no local chart or source datum was inferred.

## Repository boundary

The corrected dossier and records are on `review/channel-vts-qc-20261003`, PR #15, stacked on PRs #14 and #13.
The 76-service discovery inventory, other service dossiers and original source captures were not changed.
This is an author correction checkpoint, not authority to merge or release navigational content.
