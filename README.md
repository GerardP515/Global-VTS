# Global VTS

Worldwide VTS-guide scoping research: who to call, when, on which channel, and what to report.

## Current status

**The full required VTS register is not yet established.**

| Measure | Current repository count |
|---|---:|
| IMO 2025 Part B parents | 164 |
| Baseline TSS with a master row | 224 / 224 |
| Rows with historical Stage 2 audit documents | 174 |
| First-pass-only rows | 50 |
| Primary classification still Unresolved | 73 |
| Service identity records, not final VTS-area count | 43 |
| IMO reporting schemes | 23 |
| National reporting identities | 5 |

Read [the repository review](audits/repository_review_20260930/REVIEW.md) before using old completion reports.
The 224-row baseline is derived from the 2025 source edition. Later amendments still need systematic reconciliation.

## Working registers

- [Master TSS associations](data/current/TSS_VTS_MRS_Association_Register.csv)
- [VTS and monitoring-service identities](data/current/VTS_Entity_Register.csv)
- [IMO and national reporting schemes](data/current/Reporting_Scheme_Register.csv)
- [Research gaps](data/current/Research_Gaps.csv)
- [Current batches](research/batches_imo2025/README.md)
- [Service candidates for editorial grouping](data/current/Guide_Service_Candidates.csv)
- [Additional non-TSS coverage](data/current/Additional_Coverage_Candidates.csv)
- [Source index](sources/SOURCE_REGISTER.csv)

## Rules and research plan

[Research plan](docs/RESEARCH_PLAN.md) · [Counting and completion rules](docs/STAGE_2_COUNTING_AND_COMPLETION.md) · [Project decisions](audits/stage2/Project_Decisions_2026-09-30.md)

Service, centre, sector, reporting-system and guide-entry counts are different.
First-pass and unresolved findings are not complete merely because they have been committed.
The earlier Excel files and 170-row candidate list are historical, not current working masters.

## Validation

Run `python3 scripts/validate_registers.py` and `python3 -m unittest discover -s tests` before committing.
The automated checks validate structure and references; they do not certify navigational accuracy.
