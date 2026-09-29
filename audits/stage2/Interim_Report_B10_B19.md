# Stage 2 interim report: B10 to B19

**Date:** 29 September 2026
**Scope:** TSS-0046 to TSS-0095 (50 IMO 2025 TSS), assigned B10 to B19 by the user.
**Method:** Stage 2 prompt, four passes per batch. Pass 4 was run by independent checkers who re-opened the source behind every positive and every "Neither confirmed" classification (`research/stage2/pass4/`).

These figures cover 50 of 224 TSS. They are not a worldwide total and must not be extrapolated.

## Results

| Classification | TSS |
|---|---:|
| VTS + MRS | 2 |
| VTS only | 10 |
| MRS only | 15 |
| Neither confirmed | 11 |
| Unresolved | 12 |
| **Total** | **50** |

All ten batch audits closed as PASS WITH UNRESOLVED ITEMS, except B14 and B16 (PASS).

| Batch | Area | VTS + MRS | VTS only | MRS only | Neither | Unresolved |
|---|---|---:|---:|---:|---:|---:|
| B10 | Friesland, Botney Ground, Maas | 0 | 3 | 0 | 0 | 2 |
| B11 | Maas West Outer, North Hinder, IJmuiden | 0 | 2 | 2 | 0 | 1 |
| B12 | IJmuiden, Texel, Vlieland | 0 | 0 | 0 | 0 | 5 |
| B13 | German Bight, Jade, Elbe, Humber | 0 | 5 | 0 | 0 | 0 |
| B14 | Norway: Vardø to Torsvåg | 0 | 0 | 5 | 0 | 0 |
| B15 | Norway: Andenes to Halten | 0 | 0 | 3 | 2 | 0 |
| B16 | Norway: Runde to Egersund | 0 | 0 | 0 | 5 | 0 |
| B17 | Norway: Farsund to Risør; Fastnet | 0 | 0 | 1 | 4 | 0 |
| B18 | Smalls, Tuskar, Skerries, Liverpool Bay, North Channel | 0 | 0 | 3 | 0 | 2 |
| B19 | Little Minches, Iceland, Finisterre, Cape Roca | 2 | 0 | 1 | 0 | 2 |

## Distinct entities

**VTS areas identified: 6** (canonical IDs VTS-0017 to VTS-0022; see ID note below)

| ID | VTS | TSS linked |
|---|---|---:|
| VTS-0017 | Finisterre VTS | 1 |
| VTS-0018 | Coast of Portugal VTS (Roca Control) | 1 |
| VTS-0019 | Rotterdam VTS (Sector Maas Approach) | 4 |
| VTS-0020 | VTS North Sea Canal Area | 1 (partial) |
| VTS-0021 | German Bight Traffic | 4 (2 partial) |
| VTS-0022 | VTS Humber | 1 |

**Mandatory reporting schemes identified: 4**, all existing IMO Part I IDs: BARENTS SRS (VRS-0009, 8 TSS), WETREP (VRS-0005, 7 TSS), FINREP (VRS-0011, 1), COPREP (VRS-0012, 1). No national scheme and no new VRS ID was needed.

**Shared relationships:** Rotterdam VTS and German Bight Traffic each serve four TSS; BARENTS SRS covers eight and WETREP seven. Finisterre and Cape Roca are also inside WETREP; the register records their primary scheme (FINREP, COPREP) in `vrs_id` and WETREP in the evidence.

**Partial coverage:** TSS-0055 IJmuiden West Inner, TSS-0061 Terschelling–German Bight and TSS-0062 German Bight western approach are inside a VTS area for part of their length only. TSS-0054 Off North Hinder and TSS-0087 Off Tuskar Rock are partly inside WETREP.

## Decisions needed from the project

1. **Shore monitoring outside a declared VTS area (19 TSS).** NOR VTS (Vardø) monitors the Norwegian offshore routeing measures, but Norway's regulations list six VTS areas and none includes these TSS. Rule applied here: not VTS coverage. If this changes, the 8 Barents TSS become VTS + MRS and the 11 southern TSS become VTS only.
2. **Tanker-only schemes (7 TSS).** WETREP applies only to oil tankers over 600 dwt carrying heavy-grade oil. It is counted as MRS, as the prompt defines MRS, with the applicability recorded. The guide may want to show it differently.
3. **Port-authority descriptions as boundaries.** Maas West Outer (TSS-0051) rests on the Port of Rotterdam's description of its VTS as extending 38 nm seawards, not on a statutory limit. Kept as VTS only with lower confidence.

## Principal source gaps

- **UK and Ireland:** no official complete list of UK or Irish VTS areas was found, so VTS absence could not be established for six UK and Irish TSS. ADMIRALTY List of Radio Signals Vol 6 would close this.
- **Netherlands:** no official complete list of Dutch VTS areas; Off Texel and Vlieland VTS status and the Dutch territorial-sea reporting channel remain open.
- **Germany:** VTS area limits exist only on a small-scale 2005 statutory chart; the BSH VTS Guide Germany 2026 is not freely available. The western reach of German Bight Traffic is probably larger than recorded.
- **Iceland:** the status of the Icelandic Maritime Traffic Service and any national reporting duty.
- **Spain:** the Salvamento Marítimo website was unreachable throughout (TLS error and HTTP 503).
- **IMO circulars:** several COLREG.2 circulars were read on non-IMO hosts; COLREG.2/Circ.75 (Norway 2021) could not be retrieved.

## Method changes recommended

- Use official WFS or GIS data where a State publishes it (Norway's Kystverket layers made the Norwegian findings the strongest in this set).
- Check IMO Part I boundary text before VTS research. All 17 mandatory-reporting positives in this set came from Part I boundaries or scheme lists.
- Obtain ALRS Vol 6 before the UK, Irish and Dutch unresolved items are re-opened.
- Record the partial-coverage extent in every positive link (now a `vts_coverage` field in the register).

## ID note

This work was first done on a branch with reserved IDs (VTS-0101 onward, SRC-Bxx-nn) to avoid clashing with parallel sessions.
It has since been merged into main's canonical registers: the six VTS are VTS-0017 to VTS-0022 in `data/current/VTS_Entity_Register.csv`,
and the 56 sources are SRC-033 to SRC-088 in `sources/SOURCE_REGISTER.md`. The mapping is in `research/stage2/id_mapping_b10_b19.csv`.

## Files

- Register: `data/current/TSS_VTS_MRS_Association_Register.csv`
- VTS entities: `data/current/VTS_Entity_Register.csv`
- Sources: `sources/SOURCE_REGISTER.md` (56 sources)
- Batch audits: `audits/stage2/B10_Association_Audit.md` to `B19_Association_Audit.md`
- Raw research and Pass 4 checks: `research/stage2/`
