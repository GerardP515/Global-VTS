# Stage 2 association audit: B38

### Batch
B38

### TSS reviewed
- TSS-0186 Landfall and approaches to Puerto Ilo (B-VIII/9)
- TSS-0187 In the approaches to Arica (B-VIII/10)
- TSS-0188 In the approaches to Iquique (B-VIII/11)
- TSS-0189 In the approaches to Antofagasta (B-VIII/12)
- TSS-0190 In the approaches to Quintero Bay (B-VIII/13)

### Results

| TSS | VTS | Mandatory reporting | Classification |
|---|---|---|---|
| TSS-0186 Landfall and approaches to Puerto Ilo | - | Unresolved | Unresolved |
| TSS-0187 In the approaches to Arica | VTS-0031 VTS Arica | No | VTS only |
| TSS-0188 In the approaches to Iquique | VTS-0032 VTS Iquique | No | VTS only |
| TSS-0189 In the approaches to Antofagasta | - | No | Unresolved |
| TSS-0190 In the approaches to Quintero Bay | VTS-0033 VTS Quintero | No | VTS only |

### Evidence check
Pass 2 (researcher): Reopened NGA Pub. 125 text and rendered the VTS Arica (p.96) and VTS Iquique (p.99) diagrams: TSS drawn inside the VTS boundary limits in both. Re-ran point-in-polygon for Quintero TSS against VTS Quintero coordinates (all 6 points inside). Rechecked TSS coordinates in COLREG.2/Circ.32 and Circ.48. Re-read CHILREP guidance pp.5-6 (voluntary; internal-waters duty). Antofagasta: confirmed VTS Mejillones limits (to 23°01'.5 S) exclude the TSS.

Pass 4 (coordinator): An independent checker re-opened NGA Pub. 124 and 125 (text and VTS diagrams), the COLREG.2 compilation, SOR/2025-275 Schedules 2 and 3 and DIRECTEMAR documents. Arica, Iquique and Chedabucto Bay upheld; Quintero and Valparaiso wording corrected; Punta Arenas downgraded to Unresolved (research/stage2/pass4/chk_Y_result.json).

### Duplicate check
Three distinct port VTS (Arica, Iquique, Quintero); VTS Quintero overlaps the Zona Control VTS Valparaíso (B39) and is flagged for coordinator reconciliation, not merged. CHILREP recorded as voluntary, not MRS; VTS reporting not counted as MRS. No VRS IDs used or invented.

Shared entities in this batch:
- None within this batch.

### Changes made
Changes at Pass 4 (coordinator review of the research output):
- TSS-0187 unresolved_issue: note added: "Evidence is Tier 3 only (NGA Pub. 125); no DIRECTEMAR primary source could be opened (prontus.directemar.cl returns 403)." (Pass 4 note.)
- TSS-0187 vts_boundary_basis: note added: "Pass 4: the diagram's VTS limits reach about 070 52W (not 071W); the TSS lies well inside." (Pass 4 note.)
- TSS-0188 unresolved_issue: note added: "Evidence is Tier 3 only (NGA Pub. 125); no DIRECTEMAR primary source could be opened (prontus.directemar.cl returns 403)." (Pass 4 caveat.)
- TSS-0190 vts_boundary_basis: note added: "Pass 4 correction: points (1) and (5) at 071 32.00W fall just outside a straight chord from point a to point f; they are inside if the area closes along the coast (point f is at Punta Angeles). The VTS Valparaiso control zone (to about 32 37S) also contains this TSS." (Pass 4 caveat.)
- TSS-0190 unresolved_issue: note added: "Evidence is Tier 3 only (NGA Pub. 125); no DIRECTEMAR primary source could be opened (prontus.directemar.cl returns 403)." (Pass 4 caveat.)

### Unresolved issues
- TSS-0186: No DICAPI source on VTS or mandatory reporting at Ilo; need an official Peruvian list of VTS/traffic control services and status of SIMTRAC.
- TSS-0187: VTS evidence is Tier 3 (NGA) only; DIRECTEMAR instrument defining VTS Arica limits not located (directemar.cl partly blocked). Diagram is schematic. Evidence is Tier 3 only (NGA Pub. 125); no DIRECTEMAR primary source could be opened (prontus.directemar.cl returns 403).
- TSS-0188: VTS evidence is Tier 3 (NGA) only; DIRECTEMAR instrument defining VTS Iquique limits not located. Evidence is Tier 3 only (NGA Pub. 125); no DIRECTEMAR primary source could be opened (prontus.directemar.cl returns 403).
- TSS-0189: Whether DIRECTEMAR operates a VTS/STM at Antofagasta (not named in NGA Pub. 125); need a DIRECTEMAR list of VTS services.
- TSS-0190: Tier 3 only; relationship between VTS Quintero and VTS Valparaíso (separate services or one control zone with two centres) not established from a DIRECTEMAR source. Datum difference (TSS SAD69 chart vs VTS coordinates) negligible given margins. Evidence is Tier 3 only (NGA Pub. 125); no DIRECTEMAR primary source could be opened (prontus.directemar.cl returns 403).

### Audit result
PASS WITH UNRESOLVED ITEMS

Sources are listed in `sources/SOURCE_REGISTER.md`. VTS entities are in `data/current/VTS_Entity_Register.csv`.
