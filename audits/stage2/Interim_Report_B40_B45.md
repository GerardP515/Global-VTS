> Repository review, 30 September 2026: historical research record. Current master fields, review flags and [repository audit](../repository_review_20260930/REVIEW.md) govern readiness. A previous PASS label is not a completeness certificate.

# Stage 2 interim report: B40 to B45

**Date:** 29 September 2026
**Scope:** TSS-0196 to TSS-0224 (29 IMO 2025 TSS), the last unassigned block.
**Method:** Stage 2 prompt, four passes per batch. Pass 4 was run by independent checkers who re-opened the source behind every positive and every "Neither confirmed" classification (`research/stage2/pass4/chk_Z1` and `chk_Z3`). B42 and B43 had no positive or "Neither confirmed" classification to re-check.

These figures cover 29 of 224 TSS. They are not a worldwide total and must not be extrapolated.

## Results

| Classification | TSS |
|---|---:|
| VTS + MRS | 4 |
| VTS only | 4 |
| MRS only | 3 |
| Neither confirmed | 5 |
| Unresolved | 13 |
| **Total** | **29** |

| Batch | Area | VTS + MRS | VTS only | MRS only | Neither | Unresolved |
|---|---|---:|---:|---:|---:|---:|
| B40 | Bay of Fundy, Portland, Boston, Narragansett/Buzzards Bay, New York | 0 | 2 | 1 | 2 | 0 |
| B41 | Delaware, Chesapeake, Cape Fear, Galveston, Veracruz | 0 | 2 | 0 | 3 | 0 |
| B42 | Cuba (five schemes) | 0 | 0 | 0 | 0 | 5 |
| B43 | Cuba (two schemes), Puerto Cristóbal, Fourth Kuril Strait, Proliv Bussol' | 0 | 0 | 0 | 0 | 5 |
| B44 | Aniwa Cape, Nakhodka, Ostrovnoi Point, Chengshan Jiao inner and North | 2 | 0 | 0 | 0 | 3 |
| B45 | Chengshan Jiao East and South, Canary Islands (two schemes) | 2 | 0 | 2 | 0 | 0 |

All six batch audits closed as PASS WITH UNRESOLVED ITEMS.

## Update after project decisions (30 September 2026)

The project owner's decisions (`audits/stage2/Project_Decisions_2026-09-30.md`) confirm the rules applied in this block (decisions 2 and 5). No records changed.

## Distinct entities

**VTS services linked: 5.**

| ID | VTS | TSS linked | Note |
|---|---|---:|---|
| VTS-0013 | VTS Houston-Galveston | 1 | legacy ID; partial (offshore parts beyond 12 nm) |
| VTS-0014 | VTS New York | 1 | legacy ID; partial (about 5 to 10 per cent of the precautionary area) |
| VTS-0036 | Chengshan Jiao VTS Centre | 4 | new; East component partial |
| VTS-0037 | Fundy Traffic (Bay of Fundy VTS Zone) | 1 | new |
| VTS-0038 | Veracruz Maritime Traffic Control Centre (CCTMVER) | 1 | new; partial; not designated a VTS, but its official area names the TSS |

**Mandatory reporting schemes: 3**, all IMO Part I: VRS-0022 Off Chengshan Jiao (4 TSS), VRS-0023 CANREP (2 TSS, heavy-oil tankers only) and VRS-0021 WHALESNORTH (1 TSS, Boston, partial).

## "Neither confirmed" (5 US TSS)

Portland, Narragansett/Buzzards Bay, Delaware, Chesapeake and Cape Fear are classified "Neither confirmed". Pass 4 corrected the basis: 33 CFR 161.12 Table 1 is **not** a complete list (it omits VTS Tampa). Absence now rests on 33 CFR 161.2 (VTS is a Coast Guard service), 33 CFR 161.6 (federal pre-emption), the NAVCEN VTS Locations page (12 operating VTS, including Tampa) and the current US Coast Pilot chapter for each approach, none of which describes a VTS. None of the TSS is inside the WHALES reporting areas.

Voluntary arrangements recorded separately: the Delaware Pilots' voluntary vessel traffic information service (Ch 14) and recommended reports to the Maritime Exchange; the Buzzards Bay VMRS begins about 3 nm beyond the TSS.

## Rules applied (for confirmation)

1. **Non-VTS traffic centres:** an official port traffic centre whose defined area expressly names the TSS is linked as a VTS even if not designated a VTS (Veracruz). Confirmation from SEMAR or ALRS Vol 6 is recorded as outstanding.
2. **Voluntary pilots' or exchange services** (Delaware) are not VTS and not MRS.
3. **Tanker-only Part I schemes** (CANREP) are counted as MRS with the applicability recorded, as for WETREP in B10 to B19.

## Principal source gaps

- **Cuba (7 TSS):** no Cuban official source could be reached; NGA Pub. 147 mentions only enforcement "control posts".
- **Russian Far East (5 TSS):** no official complete list of Russian VTS; Nakhodka port rules confirmed only to 2017; the Russian 2006 routeing directive read from an unofficial copy.
- **Panama (Puerto Cristóbal):** the ACP's approach reporting is canal arrival reporting; the canal traffic management system's area is not defined.
- **Spain (Canaries):** Salvamento Marítimo's site unreachable; a coastal VTS designation for the Las Palmas and Tenerife centres is not fully ruled out.
- **New York:** the Coast Guard has proposed removing the Ambrose Channel buoys that fix the VTS boundary (comments close 3 October 2026).

## Files

- Register rows TSS-0196 to TSS-0224 in `data/current/TSS_VTS_MRS_Association_Register.csv`.
- VTS entities in `data/current/VTS_Entity_Register.csv`; sources in `sources/SOURCE_REGISTER.md`.
- Batch files `research/batches_imo2025/B40.md` to `B45.md`; audits `audits/stage2/B40` to `B45_Association_Audit.md`.
- Raw research and Pass 4 checks in `research/stage2/`.
