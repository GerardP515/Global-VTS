# IMO 2025 Reconciliation

This folder maps the provisional v0.2 candidate register to the authoritative IMO 2025 baseline.

- `TSS_Crosswalk_Legacy_v0_2_to_IMO_2025.csv` records one-to-one, grouped and renamed mappings.
- `IMO_2025_Legacy_Coverage.csv` shows whether each authoritative TSS had a legacy candidate.

The legacy register had 170 rows. The authoritative source-level inventory contains 224 named or explicitly enumerated TSS research entities. Of these, 223 are covered by at least one legacy candidate. The newly identified candidate is B-IV/3, near the deep-water route leading to Jazan Economic City Port.

Legacy identifiers are retained for traceability only.

## Legacy v0.3 findings carried onto IMO 2025 IDs

`Legacy_v0_3_Findings_to_IMO_2025.csv` carries the first-pass findings from the legacy v0.3 research
(legacy B10 to B34, legacy TSS-0046 to TSS-0170, researched and independently sample-checked on 29 September 2026)
onto the IMO 2025 canonical IDs, using the crosswalk above. It is produced by `carry_over_legacy_v0_3.py`,
which reads the legacy files from git history (commit 63b9000).

It covers 146 of the 224 IMO 2025 TSS, in IMO 2025 batches B08 to B45.

| Proposed status | TSS |
|---|---:|
| VTS + MRS | 26 |
| VTS only | 25 |
| MRS only | 10 |
| Unresolved | 85 |
| Neither confirmed | 0 |

**These are leads for Stage 2, not audited Stage 2 findings.** Each row must still go through the Stage 2 four-pass batch audit
before it enters `data/current/TSS_VTS_MRS_Association_Register.csv`.

Rules applied when carrying over:

- Reporting schemes use the IMO 2025 VRS IDs. National schemes not in IMO Part I (TUBRAP, SUNDAREP, LOMBOKREP, MASTREP) are named but have no VRS ID yet.
- No VTS IDs are allocated here. VTS names and authorities are given so IDs can be allocated once, in the master register.
- Routine reporting owed to a VTS is not counted as a mandatory reporting scheme. Voluntary schemes are listed separately.
- Where one legacy row splits into several IMO 2025 TSS, the legacy component notes were used where they exist (IJmuiden, Santa Barbara Channel and LA/LB). Otherwise the finding is carried with a note to confirm it for the individual TSS (17 positive rows).
- The legacy Odesa/Ilichevsk rows map to the successor Chornomorsk, Odesa and Pivdennyi scheme and are carried as Unresolved.
- The legacy research never checked WETREP (VRS-0005). 4 rows are flagged to check it.
- Where the IMO 2025 batch research on main already covers a TSS (B20), the `main_stage2_note` column compares the two. Four agree. TSS-0099 Off Cabo de Gata conflicts and must be resolved.
