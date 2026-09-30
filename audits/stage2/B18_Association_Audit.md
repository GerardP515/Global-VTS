> Repository review, 30 September 2026: historical research record. Current master fields, review flags and [repository audit](../repository_review_20260930/REVIEW.md) govern readiness. A previous PASS label is not a completeness certificate.

# Stage 2 association audit: B18

### Batch
B18

### TSS reviewed
- TSS-0086 Off Smalls (B-II/21)
- TSS-0087 Off Tuskar Rock (B-II/22)
- TSS-0088 Off Skerries (B-II/23)
- TSS-0089 In Liverpool Bay (B-II/24)
- TSS-0090 In the North Channel (B-II/25)

### Results

| TSS | VTS | Mandatory reporting | Classification |
|---|---|---|---|
| TSS-0086 Off Smalls | - | VRS-0005 WETREP (West European Tanker Reporting System) | MRS only |
| TSS-0087 Off Tuskar Rock | - | VRS-0005 WETREP (West European Tanker Reporting System) | MRS only |
| TSS-0088 Off Skerries | - | Unresolved | Unresolved |
| TSS-0089 In Liverpool Bay | - | No | Unresolved |
| TSS-0090 In the North Channel | - | VRS-0005 WETREP (West European Tanker Reporting System) | MRS only |

### Evidence check
Pass 2 (researcher): Reopened MSC.190(79) text and rendered Appendix 3 chartlet at 400 dpi: dashed closing lines across St George's Channel and North Channel confirmed. Rechecked each TSS position against the closing lines (A.284(VIII), COLREG.2/Circ.41 and Circ.60). WETREP positive for Smalls and North Channel (full), Tuskar (partial). No VTS positive asserted.

Pass 4 (coordinator): An independent checker re-opened MSC.190(79), MSC.162(78), Decree-Law 263/2009, COLREG.2 circulars and the DGRM and EMSA pages, re-did the boundary geometry, and upheld every positive classification (research/stage2/pass4/chk_T_result.json).

### Duplicate check
Single shared scheme VRS-0005 across Smalls, Tuskar, North Channel; no new VRS or VTS entities. Mersey VTS is a port VTS recorded as a lead only. Tanker-only applicability recorded.

Shared entities in this batch:
- VRS-0005: TSS-0086, TSS-0087, TSS-0090

### Changes made
Changes at Pass 4 (coordinator review of the research output):
- TSS-0087 unresolved_issue: note added: "WETREP para 6.2.1 also names Off Skerries, which lies beyond both Irish Sea closing lines; the list does not match the boundary, so coordinates govern." (Pass 4 caveat.)
- TSS-0088 mandatory_reporting: 'No' -> 'Unresolved'. Pass 4: WETREP para 6.2.1 names Off Skerries but the boundary excludes the Irish Sea; conflict within the IMO text, so reporting is Unresolved, not No.

### Unresolved issues
- TSS-0086: VTS: none established. No authoritative complete list of UK VTS (e.g. ALRS Vol 6) was opened; MGN 401 (R02) gives VTS guidance but no list. WETREP Appendix 1 UK station list is 2004 and outdated by Coastguard reorganisation.
- TSS-0087: Partial WETREP coverage by coordinate comparison against the 1973/1996 centreline; confirm on current chart. No Irish coastal VTS source found; Irish Coast Guard VTS status not researched to exhaustion. WETREP para 6.2.1 also names Off Skerries, which lies beyond both Irish Sea closing lines; the list does not match the boundary, so coordinates govern.
- TSS-0088: VTS status unknown: No authoritative complete list of UK VTS (e.g. ALRS Vol 6) was opened; MGN 401 (R02) gives VTS guidance but no list. WETREP 6.2.1 listing vs boundary conflict should be checked against Ships' Routeing 2025 Part I text. UK national reporting (VTMIS regs) is port-related and not counted.
- TSS-0089: Need Port of Liverpool port limits (Mersey Docks and Harbour Act) or ALRS Vol 6 VTS chart to test whether Mersey VTS area includes the TSS.
- TSS-0090: VTS: none established. No authoritative complete list of UK VTS (e.g. ALRS Vol 6) was opened; MGN 401 (R02) gives VTS guidance but no list.

### Audit result
PASS WITH UNRESOLVED ITEMS

Sources are listed in `sources/SOURCE_REGISTER.md` (renumbered from SRC-B18-nn; see `research/stage2/id_mapping_b10_b19.csv`). VTS entities are in `data/current/VTS_Entity_Register.csv`.
