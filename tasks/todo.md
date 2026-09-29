# Task: Stage 4 research, batches B10 to B34

Requested 29 September 2026: "start researching batches 10 onwards".

Scope: 125 candidate records, TSS-0046 to TSS-0170, in 25 batches of five.

Note: the plan's Stage 3 pilot (two batches of five) has not been run as a separate exercise.
These batches are researched with the Stage 4 method directly, at the user's request.
Batches B01 to B09 are not part of this task.

## Plan

- [x] Split batches into seven regional research groups and run them in parallel
- [x] For each record: verify TSS identity, VTS finding, mandatory reporting finding, with primary sources
- [x] Audit each group's findings (evidence, classification, duplication) before accepting them
- [x] Add findings to a new v0.3 workbook and CSV, without deleting v0.2
- [x] Add new VTS services, reporting schemes, relationships, sources and issues as separate records
- [x] Write the v0.3 batch audit (audits/) and update CHANGELOG and README counts
- [x] Fix the corrupted header line in the v0.2 CSV export (carry the fix into v0.3)
- [x] Commit and push to claude/hopeful-mccarthy-p2z48x

## Research groups

| Group | Batches | Records | Area |
|---|---|---|---|
| A | B10 to B13 | TSS-0046 to 0065 | German Bight, Netherlands, Ushant, Iberia, Canaries |
| B | B14 to B16 | TSS-0066 to 0080 | Gibraltar, W Mediterranean, Adriatic, Greece, Istanbul N |
| C | B17 to B19 | TSS-0081 to 0095 | Turkish Straits, Black Sea, Egypt, South Africa, Suez, Aqaba, S Red Sea |
| D | B20 to B22 | TSS-0096 to 0110 | Bab-el-Mandeb, Oman, Hormuz, Gulf, Sri Lanka, Malacca |
| E | B23 to B26 | TSS-0111 to 0130 | Singapore, Indonesia, Hong Kong, China, Russian Far East, Australia, Alaska, Juan de Fuca |
| F | B27 to B30 | TSS-0131 to 0150 | US West Coast, Mexico Pacific, Peru, Chile |
| G | B31 to B34 | TSS-0151 to 0170 | Panama, Cuba, Gulf of Mexico, US East Coast, Canada |

## Review

Completed 29 September 2026. All 125 records researched; results merged into v0.3.

- VTS confirmed present: 40 rows. Mandatory reporting confirmed: 31 rows (after verification). No confirmed-absence findings.
- Merge audit changed 12 raw findings (see research/stage4/merge_log.md): one weak VTS finding downgraded,
  three unsupported "Confirmed absent" findings removed, eight VTS/port reporting duties reclassified under their services.
- Verification: every relationship and source ID resolves; workbook totals were recomputed in Python
  (LibreOffice could not open either the v0.2 or v0.3 file in this environment, so formulas were checked by hand).
- Open: B25 and B26 batch audits; 11 new issues (ISS-018 to ISS-028); decisions listed in the audit.
- Not done: Stage 3 pilot as a separate exercise; B01 to B09 re-research; release pack zip for v0.3.

## Verification (29 September 2026, second pass)

- Three independent checkers re-tested 90 claims on 30 sampled records against the cited sources.
- 82 supported; 3 downgraded; 2 upgraded; 1 upgrade held (TSS-0126, source not loadable here); 2 already fixed at merge.
- Fixed a merge-script defect: v0.2 proposed links were not upgraded when Stage 4 confirmed them.
- Final B10 to B34 totals: VTS confirmed 40, mandatory reporting confirmed 31, no confirmed absence.
