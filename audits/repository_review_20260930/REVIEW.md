# Repository review: Global VTS

**Date:** 2026-09-30  
**Conclusion:** The required full VTS register is not yet established.

## What is now reliable

All **224 baseline TSS** have one structurally valid master record.
The **164 parent records** and **224 canonical IDs** are unchanged.
The **50 B20–B29 first-pass rows** are integrated without being promoted to audited findings.
There are **43 service records**, not 43 verified distinct VTS areas or guide entries.
The reporting register contains **23 IMO** and **5 national** scheme identities.

## Repairs completed

- Corrected **61 misaligned CSV rows** and preserved all substantive narrative fields.
- Removed **five orphan continuation records in two groups**, retaining original bytes and recovery notes.
- Integrated the **50 rows** previously outside the master.
- Restored **six missing source definitions** already cited by the research.
- Assigned canonical IDs to five named national schemes; fourteen TSS records lacked these links.
- Standardised project regions, restored canonical names and repaired the legacy CSV wrapper.
- Rebuilt all 45 batch views from the master, fixing malformed tables and stale completion labels.
- Added current service identities for Åland Sea Traffic, VTS Off Texel and Helsinki Traffic monitoring.
- Applied recorded decision 1 to **five TSS records**: South Åland Sea and four GOFREP TSS.
- Preserved first-pass findings, historical classifications, audit narratives and pre-review bytes.
- Added machine-readable relationships, source index, service candidates, batch status and research gaps.

## Why completion cannot be claimed

**50 records remain first-pass only.** Existing Stage 2 audit documents cover 174 records, but their PASS labels are not universal completion evidence.
**73 records retain the primary category Unresolved.**
**195 records carry follow-up flags** under the consistent review rules.
These counts overlap and must not be added.
Negative findings require checking against the broader approved monitoring and national-reporting scope.
Off Texel exists, but its full/partial relationship to individual Texel/Vlieland components remains open in the register.
Rotterdam distance descriptions and overview charts do not provide a precise outer VTS polygon.
The worldwide non-TSS census, later-amendment reconciliation and final guide-entry grouping are not complete.

## Recorded classifications after policy corrections

| Classification | Records |
|---|---:|
| VTS + MRS | 44 |
| VTS only | 49 |
| MRS only | 29 |
| Neither confirmed | 29 |
| Unresolved | 73 |

These are research categories, not final verified absence/presence totals.
Use the independent state and readiness fields for progress decisions.
A service record may represent a statutory area, sector, port centre or project-eligible monitoring service.

## Targeted source checks

Fintraffic explicitly identifies South Åland Sea monitoring from its Western Finland VTS centre [SRC-194, SRC-197, SRC-198].
Decision 1 therefore changes TSS-0012 from Neither confirmed to VTS only, without claiming statutory VTS designation.
Fintraffic also assigns northern GOFREP monitoring to Helsinki Traffic at its Gulf of Finland VTS centre [SRC-197, SRC-198].
The four named GOFREP TSS receive project monitoring links, not whole-TSS Helsinki VTS coverage claims.
Rijkswaterstaat and the Netherlands Coastguard confirm the current Off Texel service [SRC-195, SRC-196].
That missing service is now recorded, with component mapping still flagged.
The Rotterdam 2026 guide and sector diagram were inspected; the unresolved precision caveat is retained [SRC-054, SRC-055].

## Review limits

This review checked the complete repository text snapshot, data structure, IDs, references, progress claims and policy consistency.
It did not reopen every source or independently re-audit every operational relationship.
The source index distinguishes fresh checks from carried-forward material.
The 2025 IMO list remains a source-edition baseline, not a guarantee of September 2026 worldwide currency.
No copyrighted IMO PDF has been uploaded by this repair.

## Next work

Use `data/current/Research_Gaps.csv` to complete B20–B29 and resolve other flagged records.
Then reconcile non-TSS coverage and produce the deduplicated guide-entry list.
Only then can the project state the full number of VTS/reporting areas requiring production.
