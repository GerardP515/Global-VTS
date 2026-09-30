# Stage 2 association audit: B13

### Batch
B13

### TSS reviewed
- TSS-0061 Terschelling–German Bight (B-II/14)
- TSS-0062 German Bight western approach (B-II/15)
- TSS-0063 Jade approach (B-II/16)
- TSS-0064 Elbe approach (B-II/17)
- TSS-0065 In the approaches to the River Humber (B-II/18)

### Results

| TSS | VTS | Mandatory reporting | Classification |
|---|---|---|---|
| TSS-0061 Terschelling–German Bight | VTS-0026 German Bight Traffic | No | VTS only |
| TSS-0062 German Bight western approach | VTS-0026 German Bight Traffic | No | VTS only |
| TSS-0063 Jade approach | VTS-0026 German Bight Traffic | No | VTS only |
| TSS-0064 Elbe approach | VTS-0026 German Bight Traffic | No | VTS only |
| TSS-0065 In the approaches to the River Humber | VTS-0027 VTS Humber | No | VTS only |

### Evidence check
Pass 2 (researcher): Re-opened AnlBV Anlage (Nr. 1.17, 3.1, 5.1, 6, 8) and rendered the BGBl. I 2005 p. 2297 Anhang chart to read the Inner German Bight boundary; re-read ELWIS VTS list, WSA pages, GDWS Bekanntmachung Nr. 29.1, VTS Humber description and Circ.60 coordinates (Humber vertices checked against the VTS limit lines by calculation). The GBWA lead was corrected to partial coverage. The unretrieved GDWS Bekanntmachung 19.1.x cited by the lead is not relied on.

Pass 4 (coordinator): An independent checker re-rendered the AnlBV Anhang chart, re-read the AnlBV, SeeSchStrO and 2014 GDWS notice, the ABP Humber page and COLREG.2/Circ.60, and upheld all five positives; German Bight western approach coverage note widened (research/stage2/pass4/chk_Q_result.json).

### Duplicate check
German Bight Traffic is one VTS sector entity (Verkehrszentrale Wilhelmshaven) shared by TSS-0061, 0062, 0063 and 0064; do not create four entries. Cuxhaven Elbe Traffic and German North Sea Traffic are separate sectors of Verkehrszentrale Cuxhaven (adjoining/lead). AnlBV 3.1 and SeeSchStrO § 58 reports are VTS reporting, not an MRS. No IMO Part I system applies (WETREP boundary checked). VTS Humber is recorded once, for TSS-0065.

Shared entities in this batch:
- VTS-0026: TSS-0061, TSS-0062, TSS-0063, TSS-0064

### Changes made
Changes at Pass 4 (coordinator review of the research output):
- TSS-0062 vts_boundary_basis: note added: "Pass 4: AnlBV Nr. 3.1 requires a report to German Bight Traffic at 007 10E, west of the statutory VHF 80 boundary (about 007 19E); a commercial source (findaport, lead only) gives a German Bight Traffic VHF 79 reporting point at buoy GW/B (54 10.42N 006 54.00E) on this TSS. Coverage probably extends further west than recorded; not confirmed by a Tier 1 source." (Pass 4 note.)

### Unresolved issues
- TSS-0061: Precise boundary longitude (chart-scale estimate about 006°16'-006°22'E, 2005 chart; TSS geometry since amended). Whether German Bight Traffic's western area (VHF 79, lead Q-S21) extends further west than the VHF 80 Inner German Bight. Status of Dutch STZ art. 5(1) reporting and Brandaris approach-area buoy 'TG' position.
- TSS-0062: Whether German North Sea Traffic (VTS Centre Cuxhaven, 'Äußere Deutsche Bucht') has a defined area including the GBWA lanes (BSH VTS Guide Germany 2026 section C5.1 not freely available). Current IMO geometry of GBWA against the 2005 chart boundary (about 007°18'E) and the 007°10'E reporting meridian.
- TSS-0063: Coverage 'full' relies on the 2005 statutory chart; Jade Approach geometry may have been amended since (IMO instrument not retrieved), but any amendment near 54°N 007°30'-007°45'E would remain well inside the area.
- TSS-0064: Current IMO Elbe approach geometry versus Tonne Elbe (sector hand-over), and whether later amendments moved the Cuxhaven Elbe Traffic limit (the prior lead cited Nordergründe-Nord). This affects the sector split, not the VTS association.
- TSS-0065: VTS Humber web page is undated; confirm against ALRS Vol 6 or current Humber standing notices. IMO 2025 may include later amendments to the TSS after 2009 (none found).

### Audit result
PASS WITH UNRESOLVED ITEMS

Sources are listed in `sources/SOURCE_REGISTER.md` (renumbered from SRC-B13-nn; see `research/stage2/id_mapping_b10_b19.csv`). VTS entities are in `data/current/VTS_Entity_Register.csv`.
