> Repository review, 30 September 2026: historical research record. Current master fields, review flags and [repository audit](../repository_review_20260930/REVIEW.md) govern readiness. A previous PASS label is not a completeness certificate.

# Stage 2 association audit: B10

### Batch
B10

### TSS reviewed
- TSS-0046 East Friesland (B-II/9)
- TSS-0047 Off Botney Ground (B-II/9)
- TSS-0048 Maas North (B-II/10)
- TSS-0049 Maas North-west (B-II/10)
- TSS-0050 Maas West Inner (B-II/10)

### Results

| TSS | VTS | Mandatory reporting | Classification |
|---|---|---|---|
| TSS-0046 East Friesland | None established | No | **Neither confirmed** |
| TSS-0047 Off Botney Ground | None established | No | **Neither confirmed** |
| TSS-0048 Maas North | VTS-0024 Rotterdam VTS | No | VTS only |
| TSS-0049 Maas North-west | VTS-0024 Rotterdam VTS | No | VTS only |
| TSS-0050 Maas West Inner | VTS-0024 Rotterdam VTS | No | VTS only |

### Evidence check
Pass 2 (researcher): All positive VTS links (TSS-0048/0049/0050) reopened: PIG 2026 p.18 quote re-read; 2026 procedure pages 4, 6, 8, 9 re-read as images; Stcrt. 2026, 8272 article 1 and section 2 re-read; STZ Bijlage 1(f) re-read and matched to Circ.67 positions (MN3=(9), MN2=(12), MNW2=(13), MNW3-MW4=(21), MW5=(37)). Distances recomputed. Negative evidence for TSS-0046/0047 re-read (BaZ 261(P)/25 polygon, BWBR0033648 table of contents, MSC.190(79) points 19-20).

Pass 4 (coordinator): An independent checker re-opened the Port Information Guide 2026, Staatscourant 2026 8272, the IJmuiden VTS regulation 2025, MSC.190(79), COLREG.2/Circ.64 and 67 and the Scheldt VTS folder, and re-did the WETREP, 38 nm and 12 nm geometry. Six positives upheld; Maas West Outer kept with its basis corrected and confidence lowered (research/stage2/pass4/chk_P_result.json).

### Duplicate check
One shared VTS (Rotterdam VTS, Sector Maas Approach) linked to three TSS in B10 and one in B11; recorded once in services. Traffic centres (Hook of Holland, Botlek) not treated as separate VTS. Statutory approach area (aanloopgebied) distinguished from the VTS service area. VTS arrival reports kept inside the VTS, not counted as MRS. Coastguard VTMon kept as lead only. No parent/child confusion: B-II/9 and B-II/10 components assessed individually.

Shared entities in this batch:
- VTS-0024: TSS-0048, TSS-0049, TSS-0050

### Changes made
Changes at Pass 4 (coordinator review of the research output):
- TSS-0046 reporting_boundary_basis: note added: "Pass 4: Scheepvaartreglement territoriale zee art. 5(1) requires ships of 300 GT or more, or carrying dangerous goods, to report before entering the Dutch territorial sea; this is made as the VTS or approach-area arrival report and is not a separate ship reporting system." (Pass 4 note.)
- TSS-0047 reporting_boundary_basis: note added: "Pass 4: Scheepvaartreglement territoriale zee art. 5(1) requires ships of 300 GT or more, or carrying dangerous goods, to report before entering the Dutch territorial sea; this is made as the VTS or approach-area arrival report and is not a separate ship reporting system." (Pass 4 note.)
- TSS-0048 unresolved_issue: note added: "Pass 4: the sector chart shows only the southern end; full coverage rests on the 38 nm description (scheme 8.6 to 24.8 nm from the North Mole head)." (Pass 4.)

### Resolution of former Friesland uncertainties

- **TSS-0046 East Friesland:** IMO coordinates were retrieved. The TSS runs from about 005°07.7'E to 006°03.0'E and 54°01.7'N to 54°10.9'N. It is north of VTS Off Texel and west of the Inner German Bight / German Bight Traffic boundary. Classification changed from Unresolved to **Neither confirmed**.
- **TSS-0047 Off Botney Ground:** IMO coordinates were retrieved. The TSS lies between about 002°46.9'E and 003°44.2'E, wholly west of VTS Off Texel and far west of German Bight Traffic. Classification changed from Unresolved to **Neither confirmed**.
- Current Rijkswaterstaat VTS-centre data was checked alongside the specific VTS boundaries. No separate current offshore service covering either TSS was found.

### Unresolved issues

- TSS-0048: Rotterdam VTS's published outer service limit is expressed as 38 nautical miles seawards plus the official sector chart, rather than a coordinate polygon. The whole Maas North TSS remains within the stated distance.
- TSS-0049 and TSS-0050: the same service-area description supports coverage, while the smaller statutory approach area ends at the inner TSS limits. This distinction remains documented.

### Audit result
PASS WITH UNRESOLVED ITEMS

B10 was rechecked on 30 September 2026. The two former Friesland classification uncertainties are resolved; the remaining notes concern precision of the published Rotterdam VTS outer boundary, not the positive association decision.

Sources are listed in `sources/SOURCE_REGISTER.md` (renumbered from SRC-B10-nn; see `research/stage2/id_mapping_b10_b19.csv`). VTS entities are in `data/current/VTS_Entity_Register.csv`.
