> Repository review, 30 September 2026: historical research record. Current master fields, review flags and [repository audit](../repository_review_20260930/REVIEW.md) govern readiness. A previous PASS label is not a completeness certificate.

# Stage 2 association audit: B34

### Batch
B34

### TSS reviewed
- TSS-0166 Southern lanes (Strait of Juan de Fuca) (B-VII/2)
- TSS-0167 Northern lanes (Strait of Juan de Fuca) (B-VII/2)
- TSS-0168 Eastern lanes (Strait of Juan de Fuca) (B-VII/2)
- TSS-0169 In Puget Sound and its approaches (B-VII/3)
- TSS-0170 In Haro Strait and Boundary Pass (B-VII/4)

### Results

| TSS | VTS | Mandatory reporting | Classification |
|---|---|---|---|
| TSS-0166 Southern lanes (Strait of Juan de Fuca) | VTS-0010 Vessel Traffic Service Puget Sound | No | VTS only |
| TSS-0167 Northern lanes (Strait of Juan de Fuca) | VTS-0029; VTS-0010 Victoria VTS Zone; Vessel Traffic Service Puget Sound | No | VTS only |
| TSS-0168 Eastern lanes (Strait of Juan de Fuca) | VTS-0010 Vessel Traffic Service Puget Sound | No | VTS only |
| TSS-0169 In Puget Sound and its approaches | VTS-0010 Vessel Traffic Service Puget Sound | No | VTS only |
| TSS-0170 In Haro Strait and Boundary Pass | VTS-0029; VTS-0010 Victoria VTS Zone; Vessel Traffic Service Puget Sound | No | VTS only |

### Evidence check
Pass 2 (researcher): All positive VTS links for TSS-0166 to 0170 were re-checked against sources reopened on 2026-09-29: eCFR Parts 161 and 167 were re-downloaded (point-in-time 2026-09-01), the NAVCEN page and the VTS PS 2024 manual were re-fetched, SOR/2025-275 was re-fetched (current to 2026-09-21), and RAMN 2026 v8 was re-read from the copy downloaded on 2026-09-29 (a live re-request failed with a server reset). TSS coordinates (33 CFR 167.1312-1314, 1320-1323, 1331) were compared with the sector and exchange-line definitions.

Pass 4 (coordinator): An independent checker re-opened eCFR 33 CFR 161 and 167, SOR/2025-275, CCG RAMN 2026 (CVTS), NAVCEN and the VTS Puget Sound, San Francisco and LA-LB user manuals, and COLREG.2/Circ.64, re-did the Race Rocks exchange-line and arc geometry, and upheld all eight positives; the San Francisco partial-coverage note was widened (research/stage2/pass4/chk_W_result.json).

### Duplicate check
Only two VTS entities: VTS Puget Sound (US) and Victoria VTS Zone (Canada). The CVTS is a cooperative framework, not a third VTS. Centres (Seattle, Patricia Bay) and call signs are not treated as separate VTS. Prince Rupert Traffic / Prince Rupert VTS Zone is not linked to these five TSS (it serves waters west of 124°40'W). US VMRS and Canadian VTS-zone reporting are recorded as VTS participation, not MRS. Each TSS (Southern, Northern and Eastern lanes) was assessed on its own coordinates, not at parent level. TSS-0169 no longer carries Victoria (US waters only).

Shared entities in this batch:
- VTS-0010: TSS-0166, TSS-0167, TSS-0168, TSS-0169, TSS-0170
- VTS-0029: TSS-0167, TSS-0170

### Changes made
Changes at Pass 4 (coordinator review of the research output):
- TSS-0167 vts_name: 'Victoria VTS Zone; Vessel Traffic Service Puget Sound (jointly within the Cooperative Vessel Traffic Service for the Juan de Fuca Region)' -> 'Victoria VTS Zone; Vessel Traffic Service Puget Sound'. Pass 4: VTS name normalised (qualifier moved out of the name).
- TSS-0167 vts_boundary_basis: note added: "Services jointly within the Cooperative Vessel Traffic Service for the Juan de Fuca Region." (Pass 4: VTS name normalised (qualifier moved out of the name).)
- TSS-0170 vts_name: 'Victoria VTS Zone; Vessel Traffic Service Puget Sound (jointly within the Cooperative Vessel Traffic Service for the Juan de Fuca Region)' -> 'Victoria VTS Zone; Vessel Traffic Service Puget Sound'. Pass 4: VTS name normalised (qualifier moved out of the name).
- TSS-0170 vts_boundary_basis: note added: "Services jointly within the Cooperative Vessel Traffic Service for the Juan de Fuca Region." (Pass 4: VTS name normalised (qualifier moved out of the name).)

### Unresolved issues
- None.

### Audit result
PASS

Sources are listed in `sources/SOURCE_REGISTER.md`. VTS entities are in `data/current/VTS_Entity_Register.csv`.
