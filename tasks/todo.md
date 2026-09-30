# Stage 2 for B20 to B29 (TSS-0096 to TSS-0145)

- [x] Build research inputs from the first-pass rows (five groups of two batches)
- [x] Write `scripts/apply_stage2_update.py` and prove it changes nothing when given no updates
- [x] Passes 1 to 3: research agents K1 to K5
- [x] Pass 4: independent checks of every positive and every "Neither confirmed"
- [x] Apply results (VTS-0200 to VTS-0209, VRS-0200, SRC-2000 to SRC-2090), write the ten Stage 2 audits
- [x] Run `python3 scripts/validate_registers.py` and the unit tests (passed after every batch)
- [x] Commit one batch at a time, push, open a PR (merge only with approval)

## Review

Result for 50 TSS: 13 VTS + MRS, 4 VTS only, 1 MRS only, 0 Neither confirmed, 32 Unresolved.
All ten batch audits: PASS WITH UNRESOLVED ITEMS.

Pass 4 changed: TSS-0100 and TSS-0101 (Neither confirmed to Unresolved), TSS-0106 (MRS only to
VTS + MRS, VTS Croatia Sector A), TSS-0108 (VTS Croatia added), SAFREP recorded as voluntary
(TSS-0143, TSS-0144), plus boundary wording on TSS-0096, 0120, 0124, 0125, 0135 and 0136.

Every Stage 2 row keeps at least one review flag, so none is marked `audited`; they are `reopened`
with specific open items in `data/current/Research_Gaps.csv`.
