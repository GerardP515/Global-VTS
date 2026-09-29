# Stage 2 association audit: B39

### Batch
B39

### TSS reviewed
- TSS-0191 In the approaches to Valparaiso (B-VIII/14)
- TSS-0192 In the approaches to Concepcion Bay (B-VIII/15)
- TSS-0193 In the approaches to San Vicente Bay (B-VIII/16)
- TSS-0194 In the approaches to Punta Arenas (B-VIII/17)
- TSS-0195 In the approaches to Chedabucto Bay (B-IX/1)

### Results

| TSS | VTS | Mandatory reporting | Classification |
|---|---|---|---|
| TSS-0191 In the approaches to Valparaiso | VTS-0035 VTS Valparaíso | No | VTS only |
| TSS-0192 In the approaches to Concepcion Bay | - | Unresolved | Unresolved |
| TSS-0193 In the approaches to San Vicente Bay | - | No | Unresolved |
| TSS-0194 In the approaches to Punta Arenas | - | Unresolved | Unresolved |
| TSS-0195 In the approaches to Chedabucto Bay | VTS-0036 Strait of Canso and Eastern Approaches VTS Zone (Canso Traffic) | No | VTS only |

### Evidence check
Pass 2 (researcher): Reopened SOR/2025-275 Schedule 3 item 5 and COLREG.2/Circ.59 Annex 7 and recomputed each TSS point against the zone limits (Part I east end and Part II south end outside; rest inside). Rechecked NGA Pub. 145 para 4.1 (TSS and Canso Traffic). Rendered VTS Valparaiso diagram (p.149): TSS inside Zona Control. Re-read NGA Pub. 124 Strait of Magellan reporting text and Punta Arenas port section. RAMN Table 3-24 not verifiable; no claim rests on it.

Pass 4 (coordinator): An independent checker re-opened NGA Pub. 124 and 125 (text and VTS diagrams), the COLREG.2 compilation, SOR/2025-275 Schedules 2 and 3 and DIRECTEMAR documents. Arica, Iquique and Chedabucto Bay upheld; Quintero and Valparaiso wording corrected; Punta Arenas downgraded to Unresolved (research/stage2/pass4/chk_Y_result.json).

### Duplicate check
Canso Traffic zone reporting kept inside the VTS (no MRS). Strait of Magellan reporting recorded as a national mandatory scheme without a VRS ID; flagged for coordinator decision. VTS Valparaíso and VTS Quintero overlap flagged, not duplicated. Talcahuano information service and port radios kept as leads, not VTS.

Shared entities in this batch:
- None within this batch.

### Changes made
Changes at Pass 4 (coordinator review of the research output):
- TSS-0191 vts_boundary_basis: note added: "Pass 4 correction: with a straight chord, 4 of the 6 TSS points lie outside the VTS Quintero area, so the secondary Quintero overlap claim is qualified; coverage rests on the VTS Valparaiso diagram." (Pass 4 caveat.)
- TSS-0191 unresolved_issue: note added: "Evidence is Tier 3 only (NGA Pub. 125); no DIRECTEMAR primary source could be opened (prontus.directemar.cl returns 403)." (Pass 4 caveat.)
- TSS-0194 association_status: 'MRS only' -> 'Unresolved'. Pass 4: no formally named mandatory scheme; CHILREP is voluntary; reporting frequencies conflict (NGA every 4 h or 0800/2000 with pilot; DIRECTEMAR 12:00Z/24:00Z); the traceable legal basis (D.S. (M) 1190 of 1976, Title III) makes foreign-ship reporting compulsory only on reciprocity; no Strait of Magellan instrument found. Fails the project's national-scheme test.
- TSS-0194 mandatory_reporting: 'Yes' -> 'Unresolved'. Pass 4: no formally named mandatory scheme; CHILREP is voluntary; reporting frequencies conflict (NGA every 4 h or 0800/2000 with pilot; DIRECTEMAR 12:00Z/24:00Z); the traceable legal basis (D.S. (M) 1190 of 1976, Title III) makes foreign-ship reporting compulsory only on reciprocity; no Strait of Magellan instrument found. Fails the project's national-scheme test.
- TSS-0194 unresolved_issue: note added: "Strong lead: area-based reporting to the Maritime Authority at Punta Arenas; find the governing Chilean instrument." (Pass 4: no formally named mandatory scheme; CHILREP is voluntary; reporting frequencies conflict (NGA every 4 h or 0800/2000 with pilot; DIRECTEMAR 12:00Z/24:00Z); the traceable legal basis (D.S. (M) 1190 of 1976, Title III) makes foreign-ship reporting compulsory only on reciprocity; no Strait of Magellan instrument found. Fails the project's national-scheme test.)
- TSS-0195 unresolved_issue: note added: "Pass 4: the Eastern VTS Zone is limited to Canadian waters and the local zone's eastern edge is the territorial sea limit, so the eastern end of Part I is probably outside every VTS zone, while the southern end of Part II may fall in the Eastern zone." (Pass 4 note.)

### Unresolved issues
- TSS-0191: Tier 3 only; DIRECTEMAR instrument (e.g. resolution 12.000/934 of 2018 lead) not opened. Overlap with the VTS Quintero area to be reconciled by the coordinator (one service or two). Evidence is Tier 3 only (NGA Pub. 125); no DIRECTEMAR primary source could be opened (prontus.directemar.cl returns 403).
- TSS-0192: Whether the Talcahuano information service is a VTS; whether the TSS lies in internal waters (CHILREP position-report duty).
- TSS-0193: Whether any DIRECTEMAR VTS/STM covers San Vicente/Talcahuano approaches.
- TSS-0194: Primary DIRECTEMAR instrument for Strait of Magellan reporting not opened; sources differ on frequency (every 4 h / 0800 and 2000 per NGA vs 12:00Z and 24:00Z per DIRECTEMAR). Coordinator to confirm this qualifies as a named national MRS (no VRS ID exists; do not invent one). VTS status unresolved. Strong lead: area-based reporting to the Maritime Authority at Punta Arenas; find the governing Chilean instrument.
- TSS-0195: Exact territorial sea limit near the TSS not opened, so whether the Part I eastern end and Part II southern end lie in the Eastern VTS Zone or outside Canadian waters is not established. RAMN Table 3-24 calling-in points not read (page truncated; direct download refused). Pass 4: the Eastern VTS Zone is limited to Canadian waters and the local zone's eastern edge is the territorial sea limit, so the eastern end of Part I is probably outside every VTS zone, while the southern end of Part II may fall in the Eastern zone.

### Audit result
PASS WITH UNRESOLVED ITEMS

Sources are listed in `sources/SOURCE_REGISTER.md`. VTS entities are in `data/current/VTS_Entity_Register.csv`.
