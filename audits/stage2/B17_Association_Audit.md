# Stage 2 association audit: B17

### Batch
B17

### TSS reviewed
- TSS-0081 Off Farsund (B-II/19)
- TSS-0082 Off Ryvingen (B-II/19)
- TSS-0083 Off Lillesand (B-II/19)
- TSS-0084 Off Risør (B-II/19)
- TSS-0085 Off Fastnet Rock (B-II/20)

### Results

| TSS | VTS | Mandatory reporting | Classification |
|---|---|---|---|
| TSS-0081 Off Farsund | VTS-0039 NOR VTS (Vardø VTS centre) | No | VTS only |
| TSS-0082 Off Ryvingen | VTS-0039 NOR VTS (Vardø VTS centre) | No | VTS only |
| TSS-0083 Off Lillesand | VTS-0039 NOR VTS (Vardø VTS centre) | No | VTS only |
| TSS-0084 Off Risør | VTS-0039 NOR VTS (Vardø VTS centre) | No | VTS only |
| TSS-0085 Off Fastnet Rock | - | VRS-0005 West European Tanker Reporting System (WETREP) | MRS only |

### Evidence check
Pass 2 (researcher): Norwegian records as for B16 (same sources, own geometry per TSS). Fastnet: MSC.190(79) reopened from IMO CDN, boundary points 5-8 and 21 and Irish shore authorities checked; gov.ie IRCG page reopened (dateModified 2025-07-08) and passage confirmed.

Pass 4 (coordinator): An independent checker re-opened the Norwegian regulations (s.6 VTS list, chapter 5, notification regulation 2015 no. 1790), the Kystverket Barents SRS page, SN.1/Circ.318, MSC.190(79) and the Kystverket WFS polygons, and upheld every classification (research/stage2/pass4/chk_norway_result.json). Project decisions of 30 Sep 2026 applied (audits/stage2/Project_Decisions_2026-09-30.md).

### Duplicate check
WETREP (VRS-0005) reused, not a new ID; tanker-only threshold recorded; IRCG monitoring not counted as VTS; MRCC/MRSC treated as reporting authorities not VTS centres; Norwegian records share the same negative evidence without duplication.

Shared entities in this batch:
- VTS-0039: TSS-0081, TSS-0082, TSS-0083, TSS-0084

### Changes made
Changes at Pass 4 (coordinator review of the research output):
- TSS-0081 evidence_summary: note added: "Pass 4: the Regulation on vessels' notification obligations (21 Dec 2015 no. 1790) confirms the only transit reporting duty is Barents SRS (chapter 7), southern limit 67 10 N." (Project decision 1 (user, 30 Sep 2026): NOR VTS monitoring of the offshore routeing measures counts as VTS coverage.)
- TSS-0081 unresolved_issue: "None blocking. Caveat for Pass 4: if the project decides to count Vardø VTS (NOR VTS) coast-wide monitoring of routeing compliance as VTS coverage, this record would move to 'VTS only'. No official source found that names this TSS as within a Vardø VTS service area." -> 'Coverage rests on a project rule (decision 1): NOR VTS provides an information and monitoring service for the TSS, not a statutory VTS area; participation is not compulsory.'. Project decision 1 (user, 30 Sep 2026): NOR VTS monitoring of the offshore routeing measures counts as VTS coverage.
- TSS-0081 association_status: 'Neither confirmed' -> 'VTS only'. Project decision 1 (user, 30 Sep 2026): NOR VTS monitoring of the offshore routeing measures counts as VTS coverage.
- TSS-0081 vts_name: '' -> 'NOR VTS (Vardø VTS centre)'. Project decision 1 (user, 30 Sep 2026): NOR VTS monitoring of the offshore routeing measures counts as VTS coverage.
- TSS-0081 vts_authority: '' -> 'Norwegian Coastal Administration (Kystverket)'. Project decision 1 (user, 30 Sep 2026): NOR VTS monitoring of the offshore routeing measures counts as VTS coverage.
- TSS-0081 vts_centre: '' -> 'Vardø'. Project decision 1 (user, 30 Sep 2026): NOR VTS monitoring of the offshore routeing measures counts as VTS coverage.
- TSS-0081 vts_sector: '' -> 'Information service and monitoring for routeing measures outside the statutory VTS areas'. Project decision 1 (user, 30 Sep 2026): NOR VTS monitoring of the offshore routeing measures counts as VTS coverage.
- TSS-0081 vts_coverage: 'n/a' -> 'full'. Project decision 1 (user, 30 Sep 2026): NOR VTS monitoring of the offshore routeing measures counts as VTS coverage.
- TSS-0081 vts_boundary_basis: "Sjøtrafikkforskriften (FOR-2021-02-10-523) s.6 is the complete statutory list of Norwegian VTS areas (Horten, Brevik, Kvitsøy, Fedje, Kinn, Melkøya). NCA official VTS-area geometry (WFS layer_696) compared with NCA TSS geometry (WFS layer_706, group 'mellom Egersund og Risør', layer_706.38-40 (57.69-57.84N, 6.45-6.70E)): bounding boxes disjoint, so the TSS is outside every VTS area. Nearest: Kvitsøy VTS area (c. 60 nm). TSS-to-feature matching is by position (my inference; the WFS names only the group)." -> "Project decision 1 (user, 30 Sep 2026): shore monitoring of a TSS by a VTS centre outside a statutory VTS area counts as VTS coverage. Kystverket lists NOR VTS (Vardø) as the 'Information service for Barents SRS and routing schemes (TSS) in Norway' and states the centre 'monitors tankers and other risk vessels that follow the routing measures established outside the Norwegian coast'. The TSS is not inside any statutory VTS area under the Maritime Traffic Regulations s.6.". Project decision 1 (user, 30 Sep 2026): NOR VTS monitoring of the offshore routeing measures counts as VTS coverage.
- TSS-0081 vts_source_ids: ['S-S1', 'S-S2', 'S-S3'] -> ['S-S1', 'S-S2', 'S-S3', 'R-S3', 'R-S4']. Project decision 1 (user, 30 Sep 2026): NOR VTS monitoring of the offshore routeing measures counts as VTS coverage.
- TSS-0081 vts_leads: 'Vardø VTS (NOR VTS), Kystverket: coast-wide monitoring of risk traffic and routeing compliance outside the VTS areas (S-S10, historical SSB text; S-S1 s.172)' -> ''. Project decision 1 (user, 30 Sep 2026): NOR VTS monitoring of the offshore routeing measures counts as VTS coverage.
- TSS-0082 evidence_summary: note added: "Pass 4: the Regulation on vessels' notification obligations (21 Dec 2015 no. 1790) confirms the only transit reporting duty is Barents SRS (chapter 7), southern limit 67 10 N." (Project decision 1 (user, 30 Sep 2026): NOR VTS monitoring of the offshore routeing measures counts as VTS coverage.)
- TSS-0082 unresolved_issue: "None blocking. Caveat for Pass 4: if the project decides to count Vardø VTS (NOR VTS) coast-wide monitoring of routeing compliance as VTS coverage, this record would move to 'VTS only'. No official source found that names this TSS as within a Vardø VTS service area." -> 'Coverage rests on a project rule (decision 1): NOR VTS provides an information and monitoring service for the TSS, not a statutory VTS area; participation is not compulsory.'. Project decision 1 (user, 30 Sep 2026): NOR VTS monitoring of the offshore routeing measures counts as VTS coverage.
- TSS-0082 association_status: 'Neither confirmed' -> 'VTS only'. Project decision 1 (user, 30 Sep 2026): NOR VTS monitoring of the offshore routeing measures counts as VTS coverage.
- TSS-0082 vts_name: '' -> 'NOR VTS (Vardø VTS centre)'. Project decision 1 (user, 30 Sep 2026): NOR VTS monitoring of the offshore routeing measures counts as VTS coverage.
- TSS-0082 vts_authority: '' -> 'Norwegian Coastal Administration (Kystverket)'. Project decision 1 (user, 30 Sep 2026): NOR VTS monitoring of the offshore routeing measures counts as VTS coverage.
- TSS-0082 vts_centre: '' -> 'Vardø'. Project decision 1 (user, 30 Sep 2026): NOR VTS monitoring of the offshore routeing measures counts as VTS coverage.
- TSS-0082 vts_sector: '' -> 'Information service and monitoring for routeing measures outside the statutory VTS areas'. Project decision 1 (user, 30 Sep 2026): NOR VTS monitoring of the offshore routeing measures counts as VTS coverage.
- TSS-0082 vts_coverage: 'n/a' -> 'full'. Project decision 1 (user, 30 Sep 2026): NOR VTS monitoring of the offshore routeing measures counts as VTS coverage.
- TSS-0082 vts_boundary_basis: "Sjøtrafikkforskriften (FOR-2021-02-10-523) s.6 is the complete statutory list of Norwegian VTS areas (Horten, Brevik, Kvitsøy, Fedje, Kinn, Melkøya). NCA official VTS-area geometry (WFS layer_696) compared with NCA TSS geometry (WFS layer_706, group 'mellom Egersund og Risør', layer_706.41-43 (57.66-57.82N, 7.70-8.00E)): bounding boxes disjoint, so the TSS is outside every VTS area. Nearest: none within c. 75 nm. TSS-to-feature matching is by position (my inference; the WFS names only the group)." -> "Project decision 1 (user, 30 Sep 2026): shore monitoring of a TSS by a VTS centre outside a statutory VTS area counts as VTS coverage. Kystverket lists NOR VTS (Vardø) as the 'Information service for Barents SRS and routing schemes (TSS) in Norway' and states the centre 'monitors tankers and other risk vessels that follow the routing measures established outside the Norwegian coast'. The TSS is not inside any statutory VTS area under the Maritime Traffic Regulations s.6.". Project decision 1 (user, 30 Sep 2026): NOR VTS monitoring of the offshore routeing measures counts as VTS coverage.
- TSS-0082 vts_source_ids: ['S-S1', 'S-S2', 'S-S3'] -> ['S-S1', 'S-S2', 'S-S3', 'R-S3', 'R-S4']. Project decision 1 (user, 30 Sep 2026): NOR VTS monitoring of the offshore routeing measures counts as VTS coverage.
- TSS-0082 vts_leads: 'Vardø VTS (NOR VTS), Kystverket: coast-wide monitoring of risk traffic and routeing compliance outside the VTS areas (S-S10, historical SSB text; S-S1 s.172)' -> ''. Project decision 1 (user, 30 Sep 2026): NOR VTS monitoring of the offshore routeing measures counts as VTS coverage.
- TSS-0083 evidence_summary: note added: "Pass 4: the Regulation on vessels' notification obligations (21 Dec 2015 no. 1790) confirms the only transit reporting duty is Barents SRS (chapter 7), southern limit 67 10 N." (Project decision 1 (user, 30 Sep 2026): NOR VTS monitoring of the offshore routeing measures counts as VTS coverage.)
- TSS-0083 unresolved_issue: "None blocking. Caveat for Pass 4: if the project decides to count Vardø VTS (NOR VTS) coast-wide monitoring of routeing compliance as VTS coverage, this record would move to 'VTS only'. No official source found that names this TSS as within a Vardø VTS service area." -> 'Coverage rests on a project rule (decision 1): NOR VTS provides an information and monitoring service for the TSS, not a statutory VTS area; participation is not compulsory.'. Project decision 1 (user, 30 Sep 2026): NOR VTS monitoring of the offshore routeing measures counts as VTS coverage.
- TSS-0083 association_status: 'Neither confirmed' -> 'VTS only'. Project decision 1 (user, 30 Sep 2026): NOR VTS monitoring of the offshore routeing measures counts as VTS coverage.
- TSS-0083 vts_name: '' -> 'NOR VTS (Vardø VTS centre)'. Project decision 1 (user, 30 Sep 2026): NOR VTS monitoring of the offshore routeing measures counts as VTS coverage.
- TSS-0083 vts_authority: '' -> 'Norwegian Coastal Administration (Kystverket)'. Project decision 1 (user, 30 Sep 2026): NOR VTS monitoring of the offshore routeing measures counts as VTS coverage.
- TSS-0083 vts_centre: '' -> 'Vardø'. Project decision 1 (user, 30 Sep 2026): NOR VTS monitoring of the offshore routeing measures counts as VTS coverage.
- TSS-0083 vts_sector: '' -> 'Information service and monitoring for routeing measures outside the statutory VTS areas'. Project decision 1 (user, 30 Sep 2026): NOR VTS monitoring of the offshore routeing measures counts as VTS coverage.
- TSS-0083 vts_coverage: 'n/a' -> 'full'. Project decision 1 (user, 30 Sep 2026): NOR VTS monitoring of the offshore routeing measures counts as VTS coverage.
- TSS-0083 vts_boundary_basis: "Sjøtrafikkforskriften (FOR-2021-02-10-523) s.6 is the complete statutory list of Norwegian VTS areas (Horten, Brevik, Kvitsøy, Fedje, Kinn, Melkøya). NCA official VTS-area geometry (WFS layer_696) compared with NCA TSS geometry (WFS layer_706, group 'mellom Egersund og Risør', layer_706.44-46 (57.93-58.09N, 8.71-9.01E)): bounding boxes disjoint, so the TSS is outside every VTS area. Nearest: Brevik VTS area (c. 50 nm). TSS-to-feature matching is by position (my inference; the WFS names only the group)." -> "Project decision 1 (user, 30 Sep 2026): shore monitoring of a TSS by a VTS centre outside a statutory VTS area counts as VTS coverage. Kystverket lists NOR VTS (Vardø) as the 'Information service for Barents SRS and routing schemes (TSS) in Norway' and states the centre 'monitors tankers and other risk vessels that follow the routing measures established outside the Norwegian coast'. The TSS is not inside any statutory VTS area under the Maritime Traffic Regulations s.6.". Project decision 1 (user, 30 Sep 2026): NOR VTS monitoring of the offshore routeing measures counts as VTS coverage.
- TSS-0083 vts_source_ids: ['S-S1', 'S-S2', 'S-S3'] -> ['S-S1', 'S-S2', 'S-S3', 'R-S3', 'R-S4']. Project decision 1 (user, 30 Sep 2026): NOR VTS monitoring of the offshore routeing measures counts as VTS coverage.
- TSS-0083 vts_leads: 'Vardø VTS (NOR VTS), Kystverket: coast-wide monitoring of risk traffic and routeing compliance outside the VTS areas (S-S10, historical SSB text; S-S1 s.172)' -> ''. Project decision 1 (user, 30 Sep 2026): NOR VTS monitoring of the offshore routeing measures counts as VTS coverage.
- TSS-0084 evidence_summary: note added: "Pass 4: the Regulation on vessels' notification obligations (21 Dec 2015 no. 1790) confirms the only transit reporting duty is Barents SRS (chapter 7), southern limit 67 10 N." (Project decision 1 (user, 30 Sep 2026): NOR VTS monitoring of the offshore routeing measures counts as VTS coverage.)
- TSS-0084 unresolved_issue: "None blocking. Caveat for Pass 4: if the project decides to count Vardø VTS (NOR VTS) coast-wide monitoring of routeing compliance as VTS coverage, this record would move to 'VTS only'. No official source found that names this TSS as within a Vardø VTS service area." -> 'Coverage rests on a project rule (decision 1): NOR VTS provides an information and monitoring service for the TSS, not a statutory VTS area; participation is not compulsory.'. Project decision 1 (user, 30 Sep 2026): NOR VTS monitoring of the offshore routeing measures counts as VTS coverage.
- TSS-0084 association_status: 'Neither confirmed' -> 'VTS only'. Project decision 1 (user, 30 Sep 2026): NOR VTS monitoring of the offshore routeing measures counts as VTS coverage.
- TSS-0084 vts_name: '' -> 'NOR VTS (Vardø VTS centre)'. Project decision 1 (user, 30 Sep 2026): NOR VTS monitoring of the offshore routeing measures counts as VTS coverage.
- TSS-0084 vts_authority: '' -> 'Norwegian Coastal Administration (Kystverket)'. Project decision 1 (user, 30 Sep 2026): NOR VTS monitoring of the offshore routeing measures counts as VTS coverage.
- TSS-0084 vts_centre: '' -> 'Vardø'. Project decision 1 (user, 30 Sep 2026): NOR VTS monitoring of the offshore routeing measures counts as VTS coverage.
- TSS-0084 vts_sector: '' -> 'Information service and monitoring for routeing measures outside the statutory VTS areas'. Project decision 1 (user, 30 Sep 2026): NOR VTS monitoring of the offshore routeing measures counts as VTS coverage.
- TSS-0084 vts_coverage: 'n/a' -> 'full'. Project decision 1 (user, 30 Sep 2026): NOR VTS monitoring of the offshore routeing measures counts as VTS coverage.
- TSS-0084 vts_boundary_basis: "Sjøtrafikkforskriften (FOR-2021-02-10-523) s.6 is the complete statutory list of Norwegian VTS areas (Horten, Brevik, Kvitsøy, Fedje, Kinn, Melkøya). NCA official VTS-area geometry (WFS layer_696) compared with NCA TSS geometry (WFS layer_706, group 'mellom Egersund og Risør', layer_706.47-49 (58.41-58.56N, 9.48-9.78E)): bounding boxes disjoint, so the TSS is outside every VTS area. Nearest: Brevik VTS area (southern limit c. 58°52'N). TSS-to-feature matching is by position (my inference; the WFS names only the group)." -> "Project decision 1 (user, 30 Sep 2026): shore monitoring of a TSS by a VTS centre outside a statutory VTS area counts as VTS coverage. Kystverket lists NOR VTS (Vardø) as the 'Information service for Barents SRS and routing schemes (TSS) in Norway' and states the centre 'monitors tankers and other risk vessels that follow the routing measures established outside the Norwegian coast'. The TSS is not inside any statutory VTS area under the Maritime Traffic Regulations s.6.". Project decision 1 (user, 30 Sep 2026): NOR VTS monitoring of the offshore routeing measures counts as VTS coverage.
- TSS-0084 vts_source_ids: ['S-S1', 'S-S2', 'S-S3'] -> ['S-S1', 'S-S2', 'S-S3', 'R-S3', 'R-S4']. Project decision 1 (user, 30 Sep 2026): NOR VTS monitoring of the offshore routeing measures counts as VTS coverage.
- TSS-0084 vts_leads: 'Vardø VTS (NOR VTS), Kystverket: coast-wide monitoring of risk traffic and routeing compliance outside the VTS areas (S-S10, historical SSB text; S-S1 s.172)' -> ''. Project decision 1 (user, 30 Sep 2026): NOR VTS monitoring of the offshore routeing measures counts as VTS coverage.
- TSS-0085 reporting_boundary_basis: note added: "Pass 4: MSC.190(79) annex para 6.2.1 names 'Off Fastnet Rock' among the TSS in the WETREP area. Applies to oil tankers over 600 dwt carrying heavy grade oil." (Pass 4 stronger citation.)

### Unresolved issues
- TSS-0081: Coverage rests on a project rule (decision 1): NOR VTS provides an information and monitoring service for the TSS, not a statutory VTS area; participation is not compulsory.
- TSS-0082: Coverage rests on a project rule (decision 1): NOR VTS provides an information and monitoring service for the TSS, not a statutory VTS area; participation is not compulsory.
- TSS-0083: Coverage rests on a project rule (decision 1): NOR VTS provides an information and monitoring service for the TSS, not a statutory VTS area; participation is not compulsory.
- TSS-0084: Coverage rests on a project rule (decision 1): NOR VTS provides an information and monitoring service for the TSS, not a statutory VTS area; participation is not compulsory.
- TSS-0085: Whether Irish Coast Guard monitoring of the Fastnet TSS amounts to a VTS (no official VTS designation found); no official list of Irish VTS consulted to prove absence. TSS coordinates taken from a search snippet only (lead only); inclusion in WETREP rests on the boundary geometry, not on those coordinates.

### Audit result
PASS WITH UNRESOLVED ITEMS

Sources are listed in `sources/SOURCE_REGISTER.md`. VTS entities are in `data/current/VTS_Entity_Register.csv`.
