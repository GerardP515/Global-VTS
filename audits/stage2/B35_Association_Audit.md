> Repository review, 30 September 2026: historical research record. Current master fields, review flags and [repository audit](../repository_review_20260930/REVIEW.md) govern readiness. A previous PASS label is not a completeness certificate.

# Stage 2 association audit: B35

### Batch
B35

### TSS reviewed
- TSS-0171 In the Strait of Georgia (B-VII/4)
- TSS-0172 Off San Francisco (B-VII/5)
- TSS-0173 In the Santa Barbara Channel (B-VII/6)
- TSS-0174 In the approaches to Los Angeles – Long Beach (B-VII/7)
- TSS-0175 In the approaches to Salina Cruz (B-VII/8)

### Results

| TSS | VTS | Mandatory reporting | Classification |
|---|---|---|---|
| TSS-0171 In the Strait of Georgia | VTS-0029; VTS-0010 Victoria VTS Zone; Vessel Traffic Service Puget Sound | No | VTS only |
| TSS-0172 Off San Francisco | VTS-0011 Vessel Traffic Service San Francisco | No | VTS only |
| TSS-0173 In the Santa Barbara Channel | - | No | Unresolved |
| TSS-0174 In the approaches to Los Angeles – Long Beach | VTS-0012 Vessel Traffic Service Los Angeles-Long Beach | No | VTS only |
| TSS-0175 In the approaches to Salina Cruz | - | Unresolved | Unresolved |

### Evidence check
Pass 2 (researcher): Re-checked positive links for TSS-0171 (SOR/2025-275, RAMN 2026, 33 CFR 161.12/161.55, COLREG.2/Circ.51), TSS-0172 (33 CFR 161.50, VTS SF manual Apr 2025, COLREG.2/Circ.64 with distances recomputed from Mount Tamalpais) and TSS-0174 (NAVCEN, VTS LA-LB manual 2021, HSP Rev. 2026, 33 CFR 161.12 item (4), Circ.64 with distances recomputed from Point Fermin). Partial coverage is stated explicitly for 0172 and 0174. Unsupported links were withheld for 0173 (conflicting junction descriptions) and 0175 (no current official service description).

Pass 4 (coordinator): An independent checker re-opened eCFR 33 CFR 161 and 167, SOR/2025-275, CCG RAMN 2026 (CVTS), NAVCEN and the VTS Puget Sound, San Francisco and LA-LB user manuals, and COLREG.2/Circ.64, re-did the Race Rocks exchange-line and arc geometry, and upheld all eight positives; the San Francisco partial-coverage note was widened (research/stage2/pass4/chk_W_result.json).

### Duplicate check
Victoria VTS Zone and VTS Puget Sound are shared with B34 (same entities, no duplicates). VTS SF and VTS LA-LB are single entities; San Pedro Traffic is the centre and call sign, not a separate VTS. OVMRS is recorded as voluntary only. VMRS reporting is not counted as MRS. The Salina Cruz centre is kept as a lead only.

Shared entities in this batch:
- None within this batch.

### Changes made
Changes at Pass 4 (coordinator review of the research output):
- TSS-0171 vts_name: 'Victoria VTS Zone; Vessel Traffic Service Puget Sound (US waters, within the Cooperative Vessel Traffic Service for the Juan de Fuca Region)' -> 'Victoria VTS Zone; Vessel Traffic Service Puget Sound'. Pass 4: VTS name normalised (qualifier moved out of the name).
- TSS-0171 vts_boundary_basis: note added: "Services US waters, within the Cooperative Vessel Traffic Service for the Juan de Fuca Region." (Pass 4: VTS name normalised (qualifier moved out of the name).)
- TSS-0172 vts_boundary_basis: note added: "Pass 4: the Offshore Sector is defined as navigable waters (12 nm territorial sea) within 38 nm of Mount Tamalpais; the manual notes a small part of the 38 nm arc lies outside navigable waters. Roughly the outer 5 to 7 nm of the northern approach, and possibly the last 2 to 3 nm of the southern approach, lie beyond 12 nm. The VTS uses a 'VTS Boundary Line' reporting waypoint on these routes (MSIB 13-04)." (Pass 4.)
- TSS-0172 unresolved_issue: note added: "Plot the 12 nm territorial-sea limit against the IMO (Circ.64) coordinates to fix the extent of partial coverage." (Pass 4.)
- TSS-0174 unresolved_issue: note added: "Pass 4: whether any of the San Pedro Channel along the southern approach lies more than 12 nm from both Santa Catalina Island and the mainland was not checked." (Pass 4.)

### Unresolved issues
- TSS-0172: Minor: the outer tip of the Northern approach is about 0.8 nm beyond the 38 nm arc; the OVMRS extent is not documented. Plot the 12 nm territorial-sea limit against the IMO (Circ.64) coordinates to fix the extent of partial coverage.
- TSS-0173: Confirm the B-VII/6 and B-VII/7 junction in Ships' Routeing 2025. If it is at 33°44'N 118°36'W (IMO Circ.64), record VTS Los Angeles-Long Beach as partial coverage (south-east ~10 nm only); if it is at ~33°49'N 118°47'W (local sources), the scheme only adjoins the VTS area. Also check for any Marine Exchange information service beyond 25 nm.
- TSS-0174: Minor: the outer ~0.3-0.7 nm of the southern approach is beyond 25 nm. The western approach's end point differs between IMO Circ.64 and local sources (see TSS-0173), but on either reading the western approach is within 25 nm. Pass 4: whether any of the San Pedro Channel along the southern approach lies more than 12 nm from both Santa Catalina Island and the mainland was not checked.
- TSS-0175: Need a current SEMAR (UNICAPAM / Capitanía de Puerto Salina Cruz) or ASIPONA Salina Cruz source (Reglas de Operación del Puerto, aviso náutico, or national radio aids list / ALRS Vol 6) giving the traffic control centre's status, area and any reporting duties, and whether the VHF Ch 6 contact request is still current.

### Audit result
PASS WITH UNRESOLVED ITEMS

Sources are listed in `sources/SOURCE_REGISTER.md`. VTS entities are in `data/current/VTS_Entity_Register.csv`.
