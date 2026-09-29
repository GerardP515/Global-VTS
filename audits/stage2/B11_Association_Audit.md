# Stage 2 association audit: B11

### Batch
B11

### TSS reviewed
- TSS-0051 Maas West Outer (B-II/10)
- TSS-0052 North Hinder North (B-II/10)
- TSS-0053 North Hinder South (B-II/10)
- TSS-0054 Off North Hinder (B-II/10)
- TSS-0055 IJmuiden West Inner (B-II/11)

### Results

| TSS | VTS | Mandatory reporting | Classification |
|---|---|---|---|
| TSS-0051 Maas West Outer | VTS-0019 Rotterdam VTS | No | VTS only |
| TSS-0052 North Hinder North | - | No | Unresolved |
| TSS-0053 North Hinder South | - | VRS-0005 West European Tanker Reporting System (WETREP) | MRS only |
| TSS-0054 Off North Hinder | - | VRS-0005 West European Tanker Reporting System (WETREP) | MRS only |
| TSS-0055 IJmuiden West Inner | VTS-0020 VTS North Sea Canal Area (Noordzeekanaalgebied) | No | VTS only |

### Evidence check
Pass 2 (researcher): Rotterdam VTS link for TSS-0051 rechecked with distance test (about 34 nm vs 38 nm). WETREP links for TSS-0053/0054 rechecked: resolution vertices 19-20 and chartlet reopened; side-of-line test rerun with UK point at 001 35'-001 40'E (NHS inside except NE corner on the line; Off North Hinder split). CALDOVREP exclusion rechecked in MGN 364. IJmuiden: Circ.64 positions and the 2025 regulation scope and Appendix I chart reopened; 12 nm distances recomputed.

Pass 4 (coordinator): An independent checker re-opened the Port Information Guide 2026, Staatscourant 2026 8272, the IJmuiden VTS regulation 2025, MSC.190(79), COLREG.2/Circ.64 and 67 and the Scheldt VTS folder, and re-did the WETREP, 38 nm and 12 nm geometry. Six positives upheld; Maas West Outer kept with its basis corrected and confidence lowered (research/stage2/pass4/chk_P_result.json).

### Duplicate check
WETREP reused as VRS-0005 (no new VRS). Rotterdam VTS shared with B10. IJmuiden Approaches VHF 7 (information only) not treated as a VTS or MRS. North Hinder North left Unresolved rather than inferring Rotterdam coverage from the 38 nm figure. MRS-only classifications are tanker-specific (WETREP) and flagged as such.

Shared entities in this batch:
- VRS-0005: TSS-0053, TSS-0054

### Changes made
Changes at Pass 4 (coordinator review of the research output):
- TSS-0051 vts_boundary_basis: note added: "Pass 4 correction: the 2026 sector chart does not show this scheme (it stops at the western edge of the Maas Junction precautionary area). Coverage rests only on the Port Information Guide 2026 description of the VTS area as 38 nm seawards of the port entrance; the scheme's westernmost positions are 33.7 to 34.5 nm out." (Pass 4.)
- TSS-0051 unresolved_issue: note added: "Lower confidence: coverage rests on the port authority's 38 nm description, not a statutory boundary (the statutory Rotterdam approach area ends at the inner end of the scheme). Confirm against ALRS Vol 6 or a charted VTS limit." (Pass 4.)
- TSS-0052 reporting_boundary_basis: note added: "Pass 4: Scheepvaartreglement territoriale zee art. 5(1) requires ships of 300 GT or more, or carrying dangerous goods, to report before entering the Dutch territorial sea; this is made as the VTS or approach-area arrival report and is not a separate ship reporting system." (Pass 4 note.)
- TSS-0055 vts_boundary_basis: note added: "Pass 4: the 12 nm arc crosses the scheme at about 004 12.5E to 004 13.3E; the extended IJ-geul corridor runs between the separation zones, so the VTS area adjoins the scheme's inner edge but the lanes west of about 004 13E are outside." (Pass 4 note.)

### Unresolved issues
- TSS-0051: Outer VTS limit is stated as a distance ('38 nautical miles seawards'); the western end of the scheme is 4 nm inside it on a radius reading. If the 38 nm were measured along the channel the result is the same, but no coordinate boundary was found to confirm. Lower confidence: coverage rests on the port authority's 38 nm description, not a statutory boundary (the statutory Rotterdam approach area ends at the inner end of the scheme). Confirm against ALRS Vol 6 or a charted VTS limit.
- TSS-0052: Whether the Rotterdam VTS Sector Maas Approach outer limit (38 nm, basis of measurement undefined) includes the north-eastern part of North Hinder North. Needs ALRS Vol 6 / Dutch radio publication or a VTS boundary with coordinates.
- TSS-0053: WETREP boundary test is by computation from the resolution vertices (UK coast point longitude taken as about 001 37'E); the NE extremity sits on the line. Belgian/UK VTS absence not verified from a current official list; Scheldt VTS limit source is a 2014 folder.
- TSS-0054: Partial WETREP coverage computed from resolution vertices, sensitive to the exact longitude of point 20 (UK coast at 52 12'N) and line type; confirm on the Ships' Routeing 2025 Part I chartlet. VTS absence not proven from an official list.
- TSS-0055: Exact split point depends on whether the 12 nm is measured from the breakwater heads or the STZ reference point and on the territorial-sea limit; partial coverage itself is not in doubt. Name of the traffic centre not stated in the regulation.

### Audit result
PASS WITH UNRESOLVED ITEMS

Sources are listed in `sources/SOURCE_REGISTER.md` (renumbered from SRC-B11-nn; see `research/stage2/id_mapping_b10_b19.csv`). VTS entities are in `data/current/VTS_Entity_Register.csv`.
