> Repository review, 30 September 2026: historical research record. Current master fields, review flags and [repository audit](../repository_review_20260930/REVIEW.md) govern readiness. A previous PASS label is not a completeness certificate.

# Stage 2 association audit: B45

### Batch
B45

### TSS reviewed
- TSS-0221 East (B-X/6)
- TSS-0222 South (B-X/6)
- TSS-0223 Between Grand Canary and Fuerteventura (B-XI/1)
- TSS-0224 Between Grand Canary and Tenerife (B-XI/2)

### Results

| TSS | VTS | Mandatory reporting | Classification |
|---|---|---|---|
| TSS-0221 East | VTS-0036 Chengshan Jiao VTS Centre | VRS-0022 Off Chengshan Jiao Promontory | VTS + MRS |
| TSS-0222 South | VTS-0036 Chengshan Jiao VTS Centre | VRS-0022 Off Chengshan Jiao Promontory | VTS + MRS |
| TSS-0223 Between Grand Canary and Fuerteventura | - | VRS-0023 CANREP (Mandatory ship reporting system for the Canary Islands) | MRS only |
| TSS-0224 Between Grand Canary and Tenerife | - | VRS-0023 CANREP (Mandatory ship reporting system for the Canary Islands) | MRS only |

### Evidence check
Pass 2 (researcher): Reopened MSC.389(94)/COLREG.2/Circ.66 for East and South (East found partial: points 22-23 at 24.1 and 25.7 nm). Reopened MSC.213(81) and COLREG.2/Circ.57 and plotted both Canary TSS against the CANREP polygon (point-in-polygon test; northern terminations lie on the CANREP boundary within 0.05'). Voluntary notification notes re-quoted. Canary VTS: no official VTS designation found; press release and media treated as Tier 4 / lead only.

Pass 4 (coordinator): An independent checker re-opened MSC.389(94), MSC.213(81), COLREG.2/Circ.57 and 66 and the La Moncloa release, found the Shandong MSA 2024 VTS notice, and re-did the 24 nm and CANREP geometry. All six positives upheld; TSS-0221 wording corrected (research/stage2/pass4/chk_Z3_result.json).

### Duplicate check
VRS-0022 and VRS-0023 reused; one CANREP entity linked to both Canary TSS; MRCC Las Palmas / Tenerife recorded as MRCCs, not VTS; mandatory CANREP (tankers only) separated from voluntary TSS notification. Chengshan Jiao VTS Centre not duplicated.

Shared entities in this batch:
- VTS-0036: TSS-0221, TSS-0222
- VRS-0022: TSS-0221, TSS-0222
- VRS-0023: TSS-0223, TSS-0224

### Changes made
Changes at Pass 4 (coordinator review of the research output):
- TSS-0221 vts_source_ids: ['Z3-S1', 'Z3-S2'] -> ['Z3-S1', 'Z3-S2', 'Z3-P4-S1']. Pass 4 correction.
- TSS-0221 vts_boundary_basis: note added: "Pass 4: the Shandong MSA notice of 12 Nov 2024 (revised Chengshan Jiao VTS rules and User Guide, in force 2 Dec 2024) places the routeing lanes and precautionary areas inside the Chengshan VTS area, so VTS coverage is stated, not only inferred from the reporting boundary. VTS area coordinates not obtained. Pass 4 correction: point 22 (24.14 nm) and point 23 (25.74 nm) are both outside the 24 nm circle, so the whole outer limit of the north-westbound lane (22 to 23) lies outside; the circle cuts across the lane at an angle." (Pass 4 correction.)
- TSS-0221 source_date: note added: "; Shandong MSA notice 12 Nov 2024 (rules in force 2 Dec 2024)" (Pass 4 correction.)
- TSS-0222 vts_source_ids: ['Z3-S1', 'Z3-S2'] -> ['Z3-S1', 'Z3-S2', 'Z3-P4-S1']. Pass 4.
- TSS-0222 vts_boundary_basis: note added: "Pass 4: the Shandong MSA notice of 12 Nov 2024 (revised Chengshan Jiao VTS rules and User Guide, in force 2 Dec 2024) places the routeing lanes and precautionary areas inside the Chengshan VTS area, so VTS coverage is stated, not only inferred from the reporting boundary. VTS area coordinates not obtained." (Pass 4.)
- TSS-0222 source_date: note added: "; Shandong MSA notice 12 Nov 2024 (rules in force 2 Dec 2024)" (Pass 4.)
- TSS-0223 unresolved_issue: note added: "Pass 4: Salvamento Maritimo reportedly says its Las Palmas and Tenerife centres 'controlled' ships in the TSS in 2025; its website was unreachable, so a Spanish coastal VTS designation is not fully ruled out (lead)." (Pass 4.)
- TSS-0224 unresolved_issue: note added: "Pass 4: Salvamento Maritimo reportedly says its Las Palmas and Tenerife centres 'controlled' ships in the TSS in 2025; its website was unreachable, so a Spanish coastal VTS designation is not fully ruled out (lead)." (Pass 4.)

### Unresolved issues
- TSS-0221: National Chinese VTS area description for Chengshan Jiao VTS not located (VTS extent taken from the IMO SRS instrument). Coordinates taken from COLREG.2/Circ.66 (2014); not re-compared with the Ships' Routeing 2025 text, and no post-2015 amendment found. Eastern end of the East TSS (north-westbound lane, points 22-23) lies up to 25.7 nm from the VTS Centre, outside the SRS circle; VTS operation beyond 24 nm not documented. IMO component name is 'East'.
- TSS-0222: National Chinese VTS area description for Chengshan Jiao VTS not located (VTS extent taken from the IMO SRS instrument). Coordinates taken from COLREG.2/Circ.66 (2014); not re-compared with the Ships' Routeing 2025 text, and no post-2015 amendment found. IMO component name is 'South'.
- TSS-0223: Salvamento Marítimo website unavailable (TLS/503), so its own description of CCS functions and any Spanish designation of a coastal VTS for the Canary TSS could not be checked; ALRS Vol 6 not consulted. CANREP chartlet not inspected (coordinate check used instead). Pass 4: Salvamento Maritimo reportedly says its Las Palmas and Tenerife centres 'controlled' ships in the TSS in 2025; its website was unreachable, so a Spanish coastal VTS designation is not fully ruled out (lead).
- TSS-0224: Salvamento Marítimo website unavailable (TLS/503), so its own description of CCS functions and any Spanish designation of a coastal VTS for the Canary TSS could not be checked; ALRS Vol 6 not consulted. CANREP chartlet not inspected (coordinate check used instead). Pass 4: Salvamento Maritimo reportedly says its Las Palmas and Tenerife centres 'controlled' ships in the TSS in 2025; its website was unreachable, so a Spanish coastal VTS designation is not fully ruled out (lead).

### Audit result
PASS WITH UNRESOLVED ITEMS

Sources are listed in `sources/SOURCE_REGISTER.md`. VTS entities are in `data/current/VTS_Entity_Register.csv`.
