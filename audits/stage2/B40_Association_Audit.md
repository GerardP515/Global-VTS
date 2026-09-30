> Repository review, 30 September 2026: historical research record. Current master fields, review flags and [repository audit](../repository_review_20260930/REVIEW.md) govern readiness. A previous PASS label is not a completeness certificate.

# Stage 2 association audit: B40

### Batch
B40

### TSS reviewed
- TSS-0196 In the Bay of Fundy and approaches (B-IX/2)
- TSS-0197 In the approaches to Portland, Maine (B-IX/3)
- TSS-0198 In the approach to Boston, Massachusetts (B-IX/4)
- TSS-0199 In the approaches to Narragansett Bay, Rhode Island, and Buzzards Bay, Massachusetts (B-IX/5)
- TSS-0200 Off New York (B-IX/6)

### Results

| TSS | VTS | Mandatory reporting | Classification |
|---|---|---|---|
| TSS-0196 In the Bay of Fundy and approaches | VTS-0037 Fundy Traffic (Bay of Fundy VTS Zone) | No | VTS only |
| TSS-0197 In the approaches to Portland, Maine | - | No | Neither confirmed |
| TSS-0198 In the approach to Boston, Massachusetts | - | VRS-0021 Off the north-eastern and south-eastern coasts of the United States: WHALESNORTH (northeastern area) | MRS only |
| TSS-0199 In the approaches to Narragansett Bay, Rhode Island, and Buzzards Bay, Massachusetts | - | No | Neither confirmed |
| TSS-0200 Off New York | VTS-0014 VTS New York | No | VTS only |

### Evidence check
Pass 2 (researcher): All positive links re-opened from saved copies and passages string-verified: SOR/2025-275 Sch.3 item 7, RAMN 2026 Table 3-30 (TSS calling-in points) and Part 2 Halifax entry for TSS-0196; 33 CFR 169.105 plus 167.76-77 geometry for TSS-0198; 33 CFR 161.25, 167.151 and D1 LNM buoy position for TSS-0200. Negative findings rest on 33 CFR 161 Table 1, 161.2 and the NAVCEN enumerated VTC list (eCFR 2026-09-01).

Pass 4 (coordinator): An independent checker re-opened eCFR 33 CFR 161, 167 and 169, NAVCEN, SOR/2025-275, the ASIPONA Veracruz pages and the current US Coast Pilot chapters. Nothing downgraded; the Neither confirmed basis corrected (33 CFR 161 Table 1 omits VTS Tampa) and re-sourced to 161.2, 161.6, NAVCEN and Coast Pilot; Delaware voluntary service added (research/stage2/pass4/chk_Z1_result.json).

### Duplicate check
Fundy zone reporting kept inside the VTS (not a separate MRS). VMRS Buzzards Bay treated as a VMRS (not VTS) and not linked, as it adjoins only. WHALESNORTH linked once as VRS-0021 (Boston only). VTS New York reused by exact legacy name. The Boston/Nantucket junction precautionary area is shared with TSS-0200, and neither record claims WHALESNORTH for it.

Shared entities in this batch:
- None within this batch.

### Changes made
Changes at Pass 4 (coordinator review of the research output):
- TSS-0197 vts_source_ids: ['Z1-S1', 'Z1-S4', 'Z1-S5'] -> ['Z1-S1', 'Z1-S4', 'Z1-S5', 'Z1-P4-CP1-9']. Pass 4 correction.
- TSS-0197 vts_boundary_basis: note added: "Pass 4 correction: 33 CFR 161.12 Table 1 is not a complete list of US VTS (it omits VTS Tampa, which operates jointly with the Tampa Port Authority outside Part 161). VTS absence rests on 33 CFR 161.2 (VTS is a Coast Guard service), 33 CFR 161.6 (federal pre-emption of state VTS), the NAVCEN VTS Locations page (12 operating VTS including Tampa) and the current US Coast Pilot chapter for this approach, which describes it with no VTS." (Pass 4 correction.)
- TSS-0199 vts_source_ids: ['Z1-S1', 'Z1-S2', 'Z1-S4', 'Z1-S5'] -> ['Z1-S1', 'Z1-S2', 'Z1-S4', 'Z1-S5', 'Z1-P4-CP2-7']. Pass 4.
- TSS-0199 vts_boundary_basis: note added: "Pass 4 correction: 33 CFR 161.12 Table 1 is not a complete list of US VTS (it omits VTS Tampa, which operates jointly with the Tampa Port Authority outside Part 161). VTS absence rests on 33 CFR 161.2 (VTS is a Coast Guard service), 33 CFR 161.6 (federal pre-emption of state VTS), the NAVCEN VTS Locations page (12 operating VTS including Tampa) and the current US Coast Pilot chapter for this approach, which describes it with no VTS." (Pass 4.)
- TSS-0199 reporting_boundary_basis: note added: "Pass 4: the Buzzards Bay VMRS line lies about 2.9 to 3.4 nm beyond the approach end (not 3.3 to 3.8 nm); notices of arrival (33 CFR 160), regulated navigation areas (33 CFR 165) and the Block Island Sound speed zone are not ship reporting schemes." (Pass 4.)
- TSS-0200 vts_boundary_basis: note added: "Pass 4 correction: roughly 5 to 10 per cent of the precautionary area (not about 8 per cent) lies inside the VTS area; all lanes are outside." (Pass 4 correction.)

### Unresolved issues
- TSS-0197: Classification relies on 33 CFR 161 plus NAVCEN being complete lists of US VTS. Local voluntary arrangements (e.g. pilots, harbour master) not searched.
- TSS-0198: Reporting coverage partial: lanes south of 41°00'N and the junction precautionary area shared with Off New York (Nantucket) are outside WHALESNORTH. IMO adopting resolution not cited in 33 CFR 169 (VRS-0021 per project baseline).
- TSS-0199: Editorial point for coordinator: VMRS Buzzards Bay adjoins but does not cover the TSS, so it is not linked. Classification relies on 33 CFR 161 plus NAVCEN being complete lists of US VTS.
- TSS-0200: Coverage partial (landward sector of the precautionary area only; fraction is own approximation, Swash/Sandy Hook buoy and Breezy/Sandy Hook point positions approximated). Currency: USCG D1 proposed discontinuing Ambrose Channel Buoys 1, 2 and A (comment window to 2026-10-03); if removed, the 161.25 boundary reference needs re-checking.

### Audit result
PASS WITH UNRESOLVED ITEMS

Sources are listed in `sources/SOURCE_REGISTER.md`. VTS entities are in `data/current/VTS_Entity_Register.csv`.
