> Repository review, 30 September 2026: historical research record. Current master fields, review flags and [repository audit](../repository_review_20260930/REVIEW.md) govern readiness. A previous PASS label is not a completeness certificate.

# Stage 2 association audit: B44

### Batch
B44

### TSS reviewed
- TSS-0216 Off the Aniwa Cape (B-X/3)
- TSS-0217 In the approaches to the Gulf of Nakhodka (B-X/4)
- TSS-0218 Off the Ostrovnoi Point (B-X/5)
- TSS-0219 Chengshan Jiao inner (B-X/6)
- TSS-0220 North (B-X/6)

### Results

| TSS | VTS | Mandatory reporting | Classification |
|---|---|---|---|
| TSS-0216 Off the Aniwa Cape | - | No | Unresolved |
| TSS-0217 In the approaches to the Gulf of Nakhodka | - | No | Unresolved |
| TSS-0218 Off the Ostrovnoi Point | - | No | Unresolved |
| TSS-0219 Chengshan Jiao inner | VTS-0036 Chengshan Jiao VTS Centre | VRS-0022 Off Chengshan Jiao Promontory | VTS + MRS |
| TSS-0220 North | VTS-0036 Chengshan Jiao VTS Centre | VRS-0022 Off Chengshan Jiao Promontory | VTS + MRS |

### Evidence check
Pass 2 (researcher): Reopened MSC.389(94) and COLREG.2/Circ.66 local copies and re-verified the SRS circle, authority and TSS coordinates; distances recomputed ellipsoidally for boundary-critical points. Reopened Nakhodka rules (RG original and legalacts consolidation), Directive 1226-r and Korsakov draft; quoted passages re-checked verbatim. Prior 'VTS only' for TSS-0218 removed as not established to Tier 1/2 current standard.

Pass 4 (coordinator): An independent checker re-opened MSC.389(94), MSC.213(81), COLREG.2/Circ.57 and 66 and the La Moncloa release, found the Shandong MSA 2024 VTS notice, and re-did the 24 nm and CANREP geometry. All six positives upheld; TSS-0221 wording corrected (research/stage2/pass4/chk_Z3_result.json).

### Duplicate check
VRS-0022 reused, not re-allocated; Chengshan Jiao VTS Centre recorded once and linked to TSS-0219/0220 (and TSS-0221/0222 in B45). VTS versus SRS: the VTS extent is derived from the IMO SRS instrument that names the VTS Centre as operator; flagged. Parent B-X/6 versus components: each component checked separately against the 24 nm circle. Russian VTS communication duties treated as part of VTS, not MRS. Regional VTS of Peter the Great Gulf and Korsakov VTS recorded as leads only.

Shared entities in this batch:
- VTS-0036: TSS-0219, TSS-0220
- VRS-0022: TSS-0219, TSS-0220

### Changes made
Changes at Pass 4 (coordinator review of the research output):
- TSS-0219 vts_source_ids: ['Z3-S1', 'Z3-S2'] -> ['Z3-S1', 'Z3-S2', 'Z3-P4-S1']. Pass 4.
- TSS-0219 vts_boundary_basis: note added: "Pass 4: the Shandong MSA notice of 12 Nov 2024 (revised Chengshan Jiao VTS rules and User Guide, in force 2 Dec 2024) places the routeing lanes and precautionary areas inside the Chengshan VTS area, so VTS coverage is stated, not only inferred from the reporting boundary. VTS area coordinates not obtained." (Pass 4.)
- TSS-0219 source_date: note added: "; Shandong MSA notice 12 Nov 2024 (rules in force 2 Dec 2024)" (Pass 4.)
- TSS-0220 vts_source_ids: ['Z3-S1', 'Z3-S2'] -> ['Z3-S1', 'Z3-S2', 'Z3-P4-S1']. Pass 4.
- TSS-0220 vts_boundary_basis: note added: "Pass 4: the Shandong MSA notice of 12 Nov 2024 (revised Chengshan Jiao VTS rules and User Guide, in force 2 Dec 2024) places the routeing lanes and precautionary areas inside the Chengshan VTS area, so VTS coverage is stated, not only inferred from the reporting boundary. VTS area coordinates not obtained." (Pass 4.)
- TSS-0220 source_date: note added: "; Shandong MSA notice 12 Nov 2024 (rules in force 2 Dec 2024)" (Pass 4.)

### Unresolved issues
- TSS-0216: Current approved Korsakov port rules not obtained (only a Mintrans draft); no official complete list of Russian VTS/VTS zones for Sakhalin; identity of IMO B-X/3 geometry with Directive 1226-r Scheme No. 6 not checked against Ships' Routeing 2025; UKHO/Russian Notices to Mariners not checked.
- TSS-0217: TSS coordinates (IMO circular, Ships' Routeing 2025 B-X/4 or Russian NtM) not obtained; whether Order No. 169 is still in force in 2026 or replaced not confirmed (official Consultant/Garant texts not accessible); territorial sea limit not plotted.
- TSS-0218: Confirm Nakhodka port rules in force in 2026 and current sector 1B limits; plot the territorial sea limit against scheme part III; confirm that IMO B-X/5 geometry equals Directive 1226-r Scheme No. 3 (and whether the directive has been amended). If confirmed, the likely result is VTS only (partial).
- TSS-0219: National Chinese VTS area description for Chengshan Jiao VTS not located (VTS extent taken from the IMO SRS instrument). Coordinates taken from COLREG.2/Circ.66 (2014); not re-compared with the Ships' Routeing 2025 text, and no post-2015 amendment found.
- TSS-0220: National Chinese VTS area description for Chengshan Jiao VTS not located (VTS extent taken from the IMO SRS instrument). Coordinates taken from COLREG.2/Circ.66 (2014); not re-compared with the Ships' Routeing 2025 text, and no post-2015 amendment found. IMO component name is 'North' (display name 'Chengshan Jiao outer - North').

### Audit result
PASS WITH UNRESOLVED ITEMS

Sources are listed in `sources/SOURCE_REGISTER.md`. VTS entities are in `data/current/VTS_Entity_Register.csv`.
