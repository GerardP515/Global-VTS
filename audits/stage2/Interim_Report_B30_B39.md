# Stage 2 interim report: B30 to B39

**Date:** 29 September 2026
**Scope:** TSS-0146 to TSS-0195 (50 IMO 2025 TSS), taken as the next unassigned block after B20 to B29.
**Method:** Stage 2 prompt, four passes per batch. Pass 4 was run by independent checkers who re-opened the source behind every positive classification (`research/stage2/pass4/chk_U` to `chk_Y`).

These figures cover 50 of 224 TSS. They are not a worldwide total and must not be extrapolated.

## Results

| Classification | TSS |
|---|---:|
| VTS + MRS | 7 |
| VTS only | 19 |
| MRS only | 4 |
| Neither confirmed | 0 |
| Unresolved | 20 |
| **Total** | **50** |

| Batch | Area | VTS + MRS | VTS only | MRS only | Neither | Unresolved | Audit |
|---|---|---:|---:|---:|---:|---:|---|
| B30 | Malacca Strait segments | 5 | 0 | 0 | 0 | 0 | PASS WITH UNRESOLVED ITEMS |
| B31 | Singapore Strait, Horsburgh, Sunda, Lombok, Tathong | 2 | 1 | 0 | 0 | 2 | PASS WITH UNRESOLVED ITEMS |
| B32 | East Lamma, Dangan, south-west Australia, Wilson Promontory | 0 | 1 | 3 | 0 | 1 | PASS WITH UNRESOLVED ITEMS |
| B33 | Bass Strait, Prince William Sound, Juan de Fuca approaches | 0 | 4 | 1 | 0 | 0 | PASS |
| B34 | Juan de Fuca lanes, Puget Sound, Haro Strait | 0 | 5 | 0 | 0 | 0 | PASS |
| B35 | Strait of Georgia, San Francisco, Santa Barbara, LA-LB, Salina Cruz | 0 | 3 | 0 | 0 | 2 | PASS WITH UNRESOLVED ITEMS |
| B36 | Pacific Panama, northern Peru | 0 | 0 | 0 | 0 | 5 | PASS WITH UNRESOLVED ITEMS |
| B37 | Central and southern Peru | 0 | 0 | 0 | 0 | 5 | PASS WITH UNRESOLVED ITEMS |
| B38 | Ilo, Arica, Iquique, Antofagasta, Quintero | 0 | 3 | 0 | 0 | 2 | PASS WITH UNRESOLVED ITEMS |
| B39 | Valparaíso, Concepción, San Vicente, Punta Arenas, Chedabucto Bay | 0 | 2 | 0 | 0 | 3 | PASS WITH UNRESOLVED ITEMS |

## Distinct entities

**VTS services linked: 15.** Seven reuse legacy v0.2 IDs; eight are new.

| ID | VTS | TSS linked | Note |
|---|---|---:|---|
| VTS-0004 | Klang VTS | 3 | legacy ID |
| VTS-0005 | Johor VTS | 1 | legacy ID |
| VTS-0006 | Singapore VTS | 5 | legacy ID |
| VTS-0009 | VTS Prince William Sound | 1 | legacy ID; partial |
| VTS-0010 | VTS Puget Sound | 7 | legacy ID |
| VTS-0011 | VTS San Francisco | 1 | legacy ID; partial |
| VTS-0012 | VTS Los Angeles-Long Beach | 1 | legacy ID; partial |
| VTS-0028 | Hong Kong VTS | 2 | new |
| VTS-0029 | Victoria VTS Zone (Victoria Traffic) | 3 | new |
| VTS-0031 | Prince Rupert VTS Zone (Prince Rupert Traffic) | 3 | new; two partial |
| VTS-0032 to VTS-0035 | VTS Arica, Iquique, Quintero, Valparaíso | 1 each | new; Tier 3 evidence only |
| VTS-0036 | Strait of Canso and Eastern Approaches VTS Zone (Canso Traffic) | 1 | new; partial |

VTS-0030 was allocated in error and corrected to VTS-0009; it is unused.

**Mandatory reporting schemes: 2.** STRAITREP (VRS-0016, 7 TSS) and MASTREP (Australian national scheme under Marine Order 63, 4 TSS; no VRS ID).

**Partial coverage (7):** TSS-0152 Horsburgh, TSS-0162 Prince William Sound, TSS-0163 and TSS-0164 Juan de Fuca approaches, TSS-0172 Off San Francisco, TSS-0174 Los Angeles-Long Beach approaches, TSS-0195 Chedabucto Bay.

## Changes made at Pass 4

- **Downgraded to Unresolved:** TSS-0153 Sunda Strait and TSS-0154 Lombok Strait (VTS evidence is a 2020 release only; SUNDAREP and LOMBOKREP bind Indonesian-flag ships only, so they are recorded as voluntary for foreign ships); TSS-0194 Punta Arenas (no named mandatory scheme; foreign-ship duty only on reciprocity).
- **Coverage set to partial:** TSS-0162, TSS-0163, TSS-0164.
- **Evidence corrected:** TSS-0148 (Singapore Sector 7 overlap is up to about 1.6 nm), TSS-0190 and TSS-0191 (Quintero and Valparaíso polygon wording), TSS-0172 (part of the San Francisco northern approach lies beyond 12 nm), Australian VTS citation.

## Rules applied (for confirmation)

1. **National reporting schemes** count as MRS only if they impose a penal reporting duty on foreign ships in the TSS under defined voyage conditions. MASTREP meets this; SUNDAREP, LOMBOKREP and the Chilean reporting do not.
2. **Currency:** a VTS link resting only on evidence older than about three years, with no later official source, is Unresolved (Sunda, Lombok).
3. **Joint frameworks:** the US/Canada Cooperative Vessel Traffic Service is not given its own ID; the component services (VTS Puget Sound, Victoria and Prince Rupert VTS Zones) are linked instead.
4. **Legacy services** reuse their v0.2 ID (VTS-00N becomes VTS-000N), following main's B04 and B05 practice.

## Principal source gaps

- **Latin America:** no primary VTS source was found for Peru, Panama or Mexico; Chilean VTS findings rest on US NGA Sailing Directions (Tier 3) because DIRECTEMAR's site returns 403.
- **Indonesia:** no official source after 2020 for Merak and Benoa VTS; national decrees KM 129/2020 and KM 130/2020 not read.
- **China:** no MSA notice defining VTS coverage of the Dangan Channel TSS.
- **Australia:** VTS absence is strongly supported by AMSA's provider list but not closed (Port of Melbourne VTS area not opened).
- **Santa Barbara Channel:** IMO and local sources disagree on where the scheme ends; Ships' Routeing 2025 would settle it.

## Files

- Register rows TSS-0146 to TSS-0195 in `data/current/TSS_VTS_MRS_Association_Register.csv`.
- VTS entities in `data/current/VTS_Entity_Register.csv`; sources in `sources/SOURCE_REGISTER.md`.
- Batch files `research/batches_imo2025/B30.md` to `B39.md`; audits `audits/stage2/B30` to `B39_Association_Audit.md`.
- Raw research and Pass 4 checks in `research/stage2/`.
