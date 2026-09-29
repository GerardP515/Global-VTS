# Global VTS inventory: v0.3 Stage 4 audit (B10 to B34)

**Date:** 29 September 2026
**Status:** First-pass record research. Not a verified worldwide census. Not for navigation.

Version 0.3 adds Stage 4 research for batches B10 to B34 (125 source rows, TSS-0046 to TSS-0170).
Batches B01 to B09 are unchanged from v0.2.
The v0.2 workbook and CSV are archived unchanged under `data/archive/v0_2/`.

## What was done

The 125 records were researched in seven regional groups, each in sequential batches of five.
For every record the research established, from web sources actually retrieved:

1. TSS identity (adoption instrument, implementation date, grouping, renaming or withdrawal);
2. the VTS finding;
3. the mandatory ship reporting finding, recorded separately from routine VTS reporting;
4. voluntary reporting, applicability notes and a provisional production complexity.

Each finding is one of **Confirmed present**, **Confirmed absent** or **Unresolved**.
A failed search was never treated as absence.
Each batch received the three checks in the research plan (evidence, classification and duplication, then unresolved items).
The raw research output is kept in `research/stage4/raw/` so every finding can be traced to its source passage.

The plan's Stage 3 pilot (two batches of five, run before full research) was not run separately.
The method lessons it would have produced are recorded under **Method findings** below.

## Headline results (B10 to B34 only)

| Measure | Count |
|---|---:|
| Source rows researched | 125 |
| TSS identity confirmed by an adopting or official instrument | 101 |
| TSS identity provisional | 24 |
| In force on first-pass evidence | 119 |
| Withdrawn or superseded | 2 |
| Status not established | 4 |
| **VTS: confirmed present** | **40** |
| VTS: unresolved | 85 |
| VTS: confirmed absent | 0 |
| **Mandatory reporting scheme: confirmed present** | **32** |
| Mandatory reporting scheme: unresolved | 93 |
| Mandatory reporting scheme: confirmed absent | 0 |
| Both VTS and mandatory reporting confirmed | 23 |
| VTS only | 17 |
| Mandatory reporting only | 9 |
| Neither confirmed | 76 |

These are source-row counts. Several rows are parts of one scheme and some may be duplicates (see **Counting cautions**).
They are not the number of distinct TSS, VTS areas or guide entries.

### By region

| Region | Rows | Identity confirmed | VTS confirmed | Mandatory reporting confirmed |
|---|---:|---:|---:|---:|
| North Sea continental coast | 13 | 12 | 4 | 0 |
| France, Iberia and Canary Islands | 7 | 6 | 4 | 6 |
| Mediterranean and Black Seas | 24 | 23 | 9 | 10 |
| Southern Africa | 2 | 2 | 0 | 0 |
| Red Sea and Arabian region | 14 | 13 | 0 | 0 |
| Indian Ocean and South Asia | 1 | 0 | 0 | 0 |
| Malacca, Singapore and Indonesia | 10 | 10 | 10 | 10 |
| China Sea and China | 4 | 4 | 4 | 1 |
| North-west Pacific | 5 | 4 | 1 | 0 |
| Australia | 3 | 2 | 0 | 3 |
| North America Pacific coast | 6 | 5 | 5 | 0 |
| Central and South America Pacific coast | 17 | 1 | 0 | 0 |
| Caribbean, Gulf of Mexico and Panama | 10 | 10 | 1 | 0 |
| North America Atlantic coast | 9 | 9 | 2 | 2 |

The pattern matters for scoping. Evidence is strong where States publish VTS areas in law or official guides
(Europe, Malacca and Singapore, Indonesia, Hong Kong, US, Canada).
It is weak in Latin America, the Gulf, the Red Sea, Cuba, Russia and Australia, where official sites failed or were not found.
Those unresolved rows are research gaps, not evidence that no VTS exists.

## Register changes

| Register | v0.2 | v0.3 | Note |
|---|---:|---:|---|
| VTS service records | 15 | 57 | 16 are research leads, marked "not counted" |
| Distinct counted services linked to a researched TSS (B10 to B34) | n/a | 29 | Confirmed coverage only |
| Reporting scheme records | 8 | 27 | 21 mandatory, 6 voluntary |
| Distinct mandatory schemes linked to a researched TSS (B10 to B34) | n/a | 13 | Includes STRAITREP from v0.2 |
| Relationships | 44 | 157 | Leads and voluntary links labelled separately |
| Sources | 23 | 136 | Every cited source ID resolves |
| TSS structural parts | 2 | 101 | Lanes, approaches, precautionary areas; non-additive |
| Issues | 17 | 28 | 11 new, all open |

New mandatory schemes linked to researched TSS: OUESSREP, FINREP, COPREP, CANREP, GIBREP, ADRIREP, TÜBRAP,
SUNDAREP, LOMBOKREP, the Chengshan Jiao ship reporting system, MASTREP, WHALESNORTH and VMRS Buzzards Bay.
STRAITREP (v0.2) is now allocated to all eight Malacca and Singapore segments.

## Adjustments made at merge audit

Twelve findings were changed from the raw research output. Every change is listed in `research/stage4/merge_log.md`
and in the "Audit adjustments at merge" column of the Stage 4 Findings sheet.

1. **Downgraded VTS finding (1).** TSS-0101 Zaqqum/Umm Shaif: the only evidence was a temporary 2023 oilfield notice that does not state the VTS area. Das VTIS is kept as a lead.
2. **Removed "Confirmed absent" (3).** TSS-0067, 0068 and 0069 (Spain): absence of mandatory reporting rested on a ministry magazine article, not a formal complete list. The project still has no confirmed-absence findings.
3. **Reclassified VTS and port reporting (8).** Reporting duties owed to a VTS or port service are recorded under that service, as the counting rules require, not as a separate scheme:
   - German Bight and Elbe statutory reports to German Bight Traffic (TSS-0046 to 0049);
   - Canadian VTS zone reports under SOR/2025-275 (TSS-0169, 0170);
   - Panama Canal signal station approach reports (TSS-0151, 0161).
   The same rule was already applied by the researchers to US VTS participation (TSS-0129 to 0133, 0160).

## Counting cautions

- **Grouped and duplicate rows.** West, North and East Friesland and Off Botney Ground appear to be parts of one "Off Friesland" system. Vlieland North and Off Vlieland appear to be one entry. TSS-0121/0122 and TSS-0127/0128 may overlap. TSS-0081/0082 may overlap.
- **Superseded rows.** The two Odesa/Ilichevsk rows (TSS-0085, 0086) appear to have been merged into one successor scheme from 1 June 2023. The successor circular has not been read.
- **Conflict-affected areas.** Crimea, Kerch Strait and the Strait of Hormuz are recorded neutrally. IMO adoption is not treated as evidence of current safe operation.
- **Partial coverage.** Several confirmed findings cover only part of a scheme (for example Santa Barbara Channel, the Horsburgh north-east end, Cape Hinchinbrook precautionary area, part of Terschelling-German Bight). The link is recorded, with the limit, in the Stage 4 Findings sheet.
- **Derived coverage.** Some coverage was derived by comparing official coordinates or chartlets, not from an explicit authority statement (for example Venice, the Malacca and Singapore sector allocation, US and Canadian areas). These stand as first-pass findings and need specialist review.
- **Structural parts are not schemes.** The 101 structural-part rows describe lanes and precautionary areas. They must not be added to any TSS count.

## Decisions needed

1. **Counting rule for VTS reporting.** Should reporting owed to a VTS ever count as a separate mandatory reporting scheme? v0.3 says no, following the plan. This affects 15 rows (ISS-018).
2. **Buzzards Bay VMRS.** Kept as a separate mandatory scheme because it is a standalone US reporting system with no VTS. It covers the approach, not the lanes.
3. **National schemes mandatory only for some ships.** SUNDAREP and LOMBOKREP are mandatory only for Indonesian-flag ships. MASTREP applies only to certain vessel categories. They are counted as mandatory with the applicability recorded.

## Method findings (in place of the Stage 3 pilot)

- **Best primary sources.** eCFR (33 CFR 161, 167, 169) for the US; Canadian Coast Guard Radio Aids to Marine Navigation 2026 and SOR/2025-275 for Canada; German statutes and ELWIS; MPA Singapore; Italian Guardia Costiera VTS manuals; IMO resolutions on wwwcdn.imo.org.
- **IMO circular access.** Many COLREG.2 circulars were read in a Swedish Transport Agency compilation or other non-IMO hosts. Identity findings stand but carry a source-host limitation (ISS-022).
- **Access failures.** Salvamento Marítimo, the Italian and Greek ministries, UKHO Notice 17, Australian Notices to Mariners, Russian and Turkish official gazettes, Saudi Aramco and UKMTO pages failed or were blocked.
- **Recommendation.** Obtain the ADMIRALTY List of Radio Signals Vol 6 and the current Ships' Routeing before any second pass. Most of the 85 unresolved VTS rows are likely to close fastest from those two sources rather than from further web searching.
- **Effort.** About 630 research tool actions for 125 rows (about five per row, with national sources reused). Rows in well-documented jurisdictions took two to four actions; rows with no official web presence took eight or more and still ended unresolved.

## Batch audit status

All 25 batches received the three checks. B25 (Russian Far East) and B26 (Australia and North America Pacific) remain open,
because current Russian port rules and the Australian Notices to Mariners could not be read. All other batches are closed.
No record is marked "Fully audited": this is a first pass, not the multi-pass operational audit.

## Limits

This audit does not establish a worldwide TSS, VTS or guide-entry total.
The official baseline (Ships' Routeing 2025 and UKHO Notice 17) is still unreconciled, and B01 to B09 have not been re-researched.
VHF channels recorded in the register are research notes only and must not be used for navigation or reporting.
