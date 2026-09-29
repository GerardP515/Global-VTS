# Stage 2 association audit: B33

### Batch
B33

### TSS reviewed
- TSS-0161 In the Bass Strait (B-VI/3)
- TSS-0162 In Prince William Sound (B-VII/1)
- TSS-0163 Western approach (B-VII/2)
- TSS-0164 South-western approach (B-VII/2)
- TSS-0165 Western lanes (B-VII/2)

### Results

| TSS | VTS | Mandatory reporting | Classification |
|---|---|---|---|
| TSS-0161 In the Bass Strait | - | national MASTREP (Modernised Australian Ship Tracking and Reporting System), national mandatory scheme under the Navigation Act 2012 and Marine Order 63 (Vessel reporting systems) 2019; not an IMO Part I system | MRS only |
| TSS-0162 In Prince William Sound | VTS-0009 Vessel Traffic Service Prince William Sound | No | VTS only |
| TSS-0163 Western approach | VTS-0031 Prince Rupert VTS Zone (Prince Rupert Traffic) | No | VTS only |
| TSS-0164 South-western approach | VTS-0031 Prince Rupert VTS Zone (Prince Rupert Traffic) | No | VTS only |
| TSS-0165 Western lanes | VTS-0010; VTS-0031 Vessel Traffic Service Puget Sound; Prince Rupert VTS Zone (Prince Rupert Traffic) | No | VTS only |

### Evidence check
Pass 2 (researcher): eCFR parts 161 and 167 (point in time 2026-09-01) downloaded and the relevant sections re-read; TSS coordinates compared with VTS area limits. SOR/2025-275 Schedule 1 re-read in full text. RAMN 2026 s.3.5.4 quotes obtained twice via WebFetch (direct download failed). NAVCEN VTC list confirmed. MASTREP evidence re-read for TSS-0161.

Pass 4 (coordinator): An independent checker re-opened eCFR 33 CFR 161 and 167, CCG RAMN 2026, SOR/2025-275, AMSA pages, Marine Order 63, the TasPorts Marine Order 64 instrument and Hong Kong Marine Department sources. No status downgraded; coverage set to partial for TSS-0162 to 0164; MASTREP retained as MRS under the national-scheme rule; Australian citation corrected (research/stage2/pass4/chk_V_result.json).

### Duplicate check
VMRS and Canadian VTS Zone reporting kept under the VTS, not an MRS. The CVTS is shared by TSS-0163, 0164, 0165; component services listed once each. Victoria Traffic removed from the approaches (not its sector). TSS-0161 is a distinct IMO entry from TSS-0160 and shares MASTREP. Prince William Sound precautionary area partly outside the VTS, recorded in the notes.

Shared entities in this batch:
- VTS-0031: TSS-0163, TSS-0164, TSS-0165

### Changes made
Changes at Pass 4 (coordinator review of the research output):
- TSS-0161 reporting_boundary_basis: note added: "Pass 4: Marine Order 63 (2019) gives effect to SOLAS V/11 (s.2), applies to regulated Australian vessels and to foreign vessels from arrival at their first Australian port until departure from their final Australian port (s.6(1)), with a strict-liability penalty (s.7). Counted as MRS under the project rule that a national scheme counts when it imposes a penal reporting duty on foreign ships in the TSS under defined voyage conditions. Through traffic not calling at Australian ports is not covered." (Pass 4.)
- TSS-0161 vts_boundary_basis: note added: "Pass 4: AMSA's 'VTS areas in Australia' list (updated 14 Nov 2023) does not itself cite Marine Order 64; VTS providers are authorised under Marine Order 64 (Vessel Traffic Services) 2022 only in areas approved by AMSA (e.g. TasPorts instrument, Dec 2025)." (Pass 4.)
- TSS-0161 unresolved_issue: note added: "Pass 4: VTS absence strongly supported (TasPorts areas are small) but not closed: the Port of Melbourne VTS area was not opened." (Pass 4.)
- TSS-0162 vts_coverage: 'full' -> 'partial'. Pass 4: the Cape Hinchinbrook precautionary area (to 59 51.80N 146 00W) lies largely outside the VTS area in 33 CFR 161.60(a); the lanes and Valdez Arm TSS are inside.
- TSS-0163 vts_coverage: 'full' -> 'partial'. Pass 4: component service named instead of the CVTS framework.
- TSS-0163 vts_name: 'Cooperative Vessel Traffic Service (CVTS) for the Juan de Fuca Region' -> 'Prince Rupert VTS Zone (Prince Rupert Traffic)'. Pass 4: component service named instead of the CVTS framework.
- TSS-0164 vts_coverage: 'full' -> 'partial'. Pass 4: component service named instead of the CVTS framework.
- TSS-0164 vts_name: 'Cooperative Vessel Traffic Service (CVTS) for the Juan de Fuca Region' -> 'Prince Rupert VTS Zone (Prince Rupert Traffic)'. Pass 4: component service named instead of the CVTS framework.
- TSS-0165 vts_name: 'Cooperative Vessel Traffic Service (CVTS) for the Juan de Fuca Region' -> 'Vessel Traffic Service Puget Sound; Prince Rupert VTS Zone (Prince Rupert Traffic)'. Pass 4: component services named instead of the CVTS framework (Seattle Traffic east of 124 40W, Prince Rupert Traffic west).

### Unresolved issues
- TSS-0161: Exact position of the TSS not re-plotted from the IMO text or Australian NtM; port VTS area charts not opened. MASTREP has no project VRS ID. Pass 4: VTS absence strongly supported (TasPorts areas are small) but not closed: the Port of Melbourne VTS area was not opened.
- TSS-0162: Coverage is full for the traffic lanes and separation zones; the southern part of the associated Cape Hinchinbrook precautionary area is outside the VTS area (and partly outside the VMRS area). Light position for Cape Hinchinbrook Light taken from the reporting-point coordinates, not the Light List.
- TSS-0163: 33 CFR 161.55(a) defines the CVTS for the Juan de Fuca Region with a western limit near 124°48'W, narrower than the RAMN CVTS Area of Operation (125°15'W); coverage relies on RAMN s.3.5.4 and Table 161.12(c). RAMN quotes were extracted through WebFetch because direct download failed. Territorial-sea distances are my approximations.
- TSS-0164: Same as TSS-0163 (narrower CVTS definition in §161.55(a); RAMN extracted via WebFetch; approximate territorial-sea plot).
- TSS-0165: Coordinator to decide whether the CVTS is recorded as one VTS entity or as links to its component services (VTS Puget Sound, Prince Rupert and Victoria VTS Zones). SOR/2025-275 in-force date not verified.

### Audit result
PASS

Sources are listed in `sources/SOURCE_REGISTER.md`. VTS entities are in `data/current/VTS_Entity_Register.csv`.
