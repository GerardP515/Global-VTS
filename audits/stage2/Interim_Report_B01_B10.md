> Repository review, 30 September 2026: historical research record. Current master fields, review flags and [repository audit](../repository_review_20260930/REVIEW.md) govern readiness. A previous PASS label is not a completeness certificate.

# Stage 2 Interim Report: B01–B10

**Scope:** TSS-0001 to TSS-0050  
**Batches:** B01–B10  
**TSS researched:** 50  
**Status:** Assigned block complete  
**Date closed:** 30 September 2026

## Classification totals

| Classification | TSS count |
|---|---:|
| VTS + MRS | 13 |
| VTS only | 11 |
| MRS only | 8 |
| Neither confirmed | 18 |
| Unresolved | 0 |
| **Total** | **50** |

### Association totals

- TSS with an operational VTS association: **24 / 50**
- TSS with at least one mandatory reporting-system association: **21 / 50**
- TSS with both: **13 / 50**
- TSS with neither confirmed: **18 / 50**
- TSS left with primary classification Unresolved: **0 / 50**

These are counts for B01–B10 only. They must not be extrapolated to the 224-TSS worldwide baseline.

## Distinct operational entities

### VTS

**14 distinct VTS services** are associated with at least one TSS in B01–B10:

- VTS-0001 Channel VTS
- VTS-0002 Great Belt VTS
- VTS-0003 Sound VTS
- VTS-0015 VTS Zatoka Gdańska
- VTS-0016 Saint Petersburg VTS / regional VTS
- VTS-0017 VTS Ławica Słupska
- VTS-0018 Sassnitz Traffic
- VTS-0019 Stralsund Traffic
- VTS-0020 Kadetrenden Traffic
- VTS-0021 Kiel Traffic
- VTS-0024 Rotterdam VTS
- VTS-0040 Ouessant Traffic / CROSS Corsen
- VTS-0041 Jobourg Traffic / CROSS Jobourg
- VTS-0042 Sunk VTS

### Mandatory reporting systems

**8 distinct IMO mandatory reporting systems** are associated with the first 50 TSS:

- VRS-0001 GOFREP
- VRS-0002 GDANREP
- VRS-0003 SOUNDREP
- VRS-0004 BELTREP
- VRS-0005 WETREP
- VRS-0006 OUESSREP
- VRS-0007 MANCHEREP
- VRS-0008 CALDOVREP

Several TSS fall within more than one mandatory reporting system. Do not add those systems together as if each TSS had only one reporting relationship.

## Shared VTS relationships

Six VTS services cover more than one TSS in this block:

| VTS | TSS linked |
|---|---:|
| VTS-0016 Saint Petersburg VTS | 3 |
| VTS-0015 VTS Zatoka Gdańska | 2 |
| VTS-0003 Sound VTS | 3 |
| VTS-0002 Great Belt VTS | 2 |
| VTS-0042 Sunk VTS | 3 |
| VTS-0024 Rotterdam VTS | 3 |

These six shared services account for **16 TSS-to-VTS links**. The remaining eight VTS services each link to one TSS in B01–B10.

## Significant findings

1. **TSS and VTS are not one-to-one.** One VTS commonly covers several TSS.
2. **Mandatory reporting and VTS are independent relationships.** GOFREP provides several clear MRS-only cases.
3. **Monitoring is not automatically VTS.** Åland Sea Traffic and Sweden Traffic were retained as operational context without being counted as VTS.
4. **Multiple mandatory systems can overlap one TSS.** Ushant, Casquets, Dover and West Hinder demonstrate this.
5. **Negative findings need geometry.** Several "Neither confirmed" decisions required comparing official TSS coordinates with current VTS polygons or statutory boundaries.
6. **Parent routeing systems must remain decomposed.** Sunk and Off Friesland demonstrate why individual TSS components need their own association records.

## Remaining source gaps within B01–B10

The primary classifications are complete, but several later-production issues remain:

- **West Hinder:** exact TSS-to-VTS-Scheldt boundary relationship is not explicit enough to count a VTS association.
- **Rotterdam Maas TSS:** Rotterdam VTS states an outer service extent of 38 nautical miles and provides a sector chart, but no coordinate polygon was located. The positive association remains supported but the boundary basis should be retained in the guide notes.
- **Isles of Scilly:** the separate voluntary UK reporting arrangement needs exact TSS-level boundary treatment if voluntary reporting is included in the final guide.
- **Monitoring-only services:** the final data model may need a service type separate from VTS and reporting schemes.

## Method changes confirmed by the first 50

The following rules should remain in force for subsequent Stage 2 work:

1. Use exact boundary or named-scheme evidence for positive associations.
2. Use coordinate comparison where a nearby VTS does not explicitly name a TSS.
3. Record more than one mandatory reporting system where areas overlap.
4. Preserve monitoring-only services separately from VTS.
5. Do not create a new VTS ID for each sector or centre.
6. Reuse one VTS entity where several TSS share the service.
7. Keep national VTS reporting procedures separate from IMO mandatory ship reporting systems.
8. Run an ID-uniqueness check after parallel merges before the next research block is closed.

## Repository integrity check

During closure of B10, a parallel Stage 2 merge was found to have reused three VTS IDs and eight source IDs that had subsequently been allocated in B08/B09.

The collision was repaired before this block was closed:

- Ouessant Traffic → VTS-0040
- Jobourg Traffic → VTS-0041
- Sunk VTS → VTS-0042
- B08/B09 source IDs → SRC-185 to SRC-192

The VTS register and source register were rechecked after the repair and contain **no duplicate IDs**.

## Audit status by batch

| Batch | Result |
|---|---|
| B01 | PASS |
| B02 | PASS |
| B03 | PASS |
| B04 | PASS |
| B05 | PASS |
| B06 | PASS |
| B07 | PASS |
| B08 | PASS WITH UNRESOLVED ITEMS |
| B09 | PASS |
| B10 | PASS WITH UNRESOLVED ITEMS |

The unresolved items in B08 and B10 do not leave any of the 50 TSS with a primary classification of Unresolved.

## Block result

**B01–B10 COMPLETE: 50 / 50 TSS classified and saved to the master Stage 2 association register.**
