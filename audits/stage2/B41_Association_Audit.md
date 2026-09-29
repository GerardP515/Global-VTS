# Stage 2 association audit: B41

### Batch
B41

### TSS reviewed
- TSS-0201 Off Delaware Bay (B-IX/7)
- TSS-0202 In the approaches to Chesapeake Bay (B-IX/8)
- TSS-0203 In the approaches to the Cape Fear River (B-IX/9)
- TSS-0204 In the approaches to Galveston Bay (B-IX/10)
- TSS-0205 In the approaches to the port of Veracruz (B-IX/11)

### Results

| TSS | VTS | Mandatory reporting | Classification |
|---|---|---|---|
| TSS-0201 Off Delaware Bay | - | No | Neither confirmed |
| TSS-0202 In the approaches to Chesapeake Bay | - | No | Neither confirmed |
| TSS-0203 In the approaches to the Cape Fear River | - | No | Neither confirmed |
| TSS-0204 In the approaches to Galveston Bay | VTS-0013 VTS Houston-Galveston | No | VTS only |
| TSS-0205 In the approaches to the port of Veracruz | VTS-0039 Centro de Control de Tráfico Marítimo de Veracruz (CCTMVER) | No | VTS only |

### Evidence check
Pass 2 (researcher): VTS Houston-Galveston re-verified from 33 CFR 161.35 (LB 1C inside the inshore precautionary area, point-in-polygon check), Table 1 monitoring box and 161.2 navigable waters; NAVCEN and 2025 User Manual confirm operation. Veracruz CCTM re-opened from the ASIPONA pages and checked against COLREG.2/Circ.41 coordinates. Delaware, Chesapeake and Cape Fear negatives re-checked against 161 Table 1, NAVCEN, 169.105/115 and 165.501.

Pass 4 (coordinator): An independent checker re-opened eCFR 33 CFR 161, 167 and 169, NAVCEN, SOR/2025-275, the ASIPONA Veracruz pages and the current US Coast Pilot chapters. Nothing downgraded; the Neither confirmed basis corrected (33 CFR 161 Table 1 omits VTS Tampa) and re-sourced to 161.2, 161.6, NAVCEN and Coast Pilot; Delaware voluntary service added (research/stage2/pass4/chk_Z1_result.json).

### Duplicate check
VTS Houston-Galveston reused by exact legacy name. The Veracruz CCTM is a new service (no legacy ID), flagged for service-type confirmation. Maritime Exchange (Delaware) kept as a lead, not a VTS. RNA 165.501 notifications not counted as an MRS. No Part I system in the Gulf of Mexico.

Shared entities in this batch:
- None within this batch.

### Changes made
Changes at Pass 4 (coordinator review of the research output):
- TSS-0201 vts_source_ids: ['Z1-S1', 'Z1-S4', 'Z1-S5'] -> ['Z1-S1', 'Z1-S4', 'Z1-S5', 'Z1-P4-CP3-6']. Pass 4.
- TSS-0201 vts_boundary_basis: note added: "Pass 4 correction: 33 CFR 161.12 Table 1 is not a complete list of US VTS (it omits VTS Tampa, which operates jointly with the Tampa Port Authority outside Part 161). VTS absence rests on 33 CFR 161.2 (VTS is a Coast Guard service), 33 CFR 161.6 (federal pre-emption of state VTS), the NAVCEN VTS Locations page (12 operating VTS including Tampa) and the current US Coast Pilot chapter for this approach, which describes it with no VTS." (Pass 4.)
- TSS-0201 voluntary_reporting: 'Unresolved' -> "Yes: Delaware Pilots' voluntary vessel traffic information service (Ch 14) and recommended reports to the Maritime Exchange (US Coast Pilot 3 ch. 6)". Pass 4.
- TSS-0201 vts_leads: 'Maritime Exchange for the Delaware River and Bay (trade association; Cape Henlopen reporting station): lead only, not a VTS' -> "Delaware Pilots' voluntary vessel traffic information service (pilots' association, not a VTS); Maritime Exchange for the Delaware River and Bay". Pass 4.
- TSS-0202 vts_source_ids: ['Z1-S1', 'Z1-S4', 'Z1-S5'] -> ['Z1-S1', 'Z1-S4', 'Z1-S5', 'Z1-P4-CP3-9']. Pass 4.
- TSS-0202 vts_boundary_basis: note added: "Pass 4 correction: 33 CFR 161.12 Table 1 is not a complete list of US VTS (it omits VTS Tampa, which operates jointly with the Tampa Port Authority outside Part 161). VTS absence rests on 33 CFR 161.2 (VTS is a Coast Guard service), 33 CFR 161.6 (federal pre-emption of state VTS), the NAVCEN VTS Locations page (12 operating VTS including Tampa) and the current US Coast Pilot chapter for this approach, which describes it with no VTS." (Pass 4.)
- TSS-0202 reporting_boundary_basis: note added: "Pass 4: the 33 CFR 165.501 regulated navigation area contains the TSS, but its duties are situational reports (e.g. impaired manoeuvrability, emergencies), not a ship reporting scheme." (Pass 4.)
- TSS-0203 vts_source_ids: ['Z1-S1', 'Z1-S4', 'Z1-S5'] -> ['Z1-S1', 'Z1-S4', 'Z1-S5', 'Z1-P4-CP4-6', 'Z1-P4-CP4-5']. Pass 4 correction.
- TSS-0203 vts_boundary_basis: note added: "Pass 4 correction: 33 CFR 161.12 Table 1 is not a complete list of US VTS (it omits VTS Tampa, which operates jointly with the Tampa Port Authority outside Part 161). VTS absence rests on 33 CFR 161.2 (VTS is a Coast Guard service), 33 CFR 161.6 (federal pre-emption of state VTS), the NAVCEN VTS Locations page (12 operating VTS including Tampa) and the current US Coast Pilot chapter for this approach, which describes it with no VTS." (Pass 4 correction.)
- TSS-0205 unresolved_issue: note added: "Pass 4: the port traffic centre's defined area names the TSS, meeting association standards 1 and 3, though it is not designated a VTS; confirm with SEMAR or ALRS Vol 6." (Pass 4.)

### Unresolved issues
- TSS-0201: Maritime Exchange voluntary reporting not verified from an official source. Classification relies on 33 CFR 161 plus NAVCEN being complete lists of US VTS.
- TSS-0202: Classification relies on 33 CFR 161 plus NAVCEN being complete lists of US VTS. Whether 165.501 situational reports should be noted by the coordinator is an editorial choice.
- TSS-0203: Local Sector North Carolina / pilot practice not researched (would be voluntary at most). Classification relies on 33 CFR 161 plus NAVCEN being complete lists of US VTS.
- TSS-0204: 12 NM limit position computed approximately from jetty/shore positions, not from an official baseline chart; the exact split of the lanes needs a NOAA maritime limits check.
- TSS-0205: The ASIPONA pages do not use the term VTS and give no legal designation or mandatory participation rule; the service type should be confirmed from SEMAR/Capitanía or ALRS Vol 6. Partial coverage rests on 1996 TSS coordinates, not checked against any amendment in Ships' Routeing 2025. National mandatory reporting search was not exhaustive (SEMAR sources not located). Pass 4: the port traffic centre's defined area names the TSS, meeting association standards 1 and 3, though it is not designated a VTS; confirm with SEMAR or ALRS Vol 6.

### Audit result
PASS WITH UNRESOLVED ITEMS

Sources are listed in `sources/SOURCE_REGISTER.md`. VTS entities are in `data/current/VTS_Entity_Register.csv`.
