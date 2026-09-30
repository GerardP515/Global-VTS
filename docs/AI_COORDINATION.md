# Coordination note for AI sessions working on Stage 2

Read this before starting any Stage 2 work. Several AI sessions work on this repository at the same time and write to the same shared files. These rules stop them overwriting each other or giving two things the same ID.

## Status on 30 September 2026

- Stage 2 results are in `data/current/TSS_VTS_MRS_Association_Register.csv` for **174 of 224 TSS**: B01 to B19 and B30 to B45.
- **Still to do: B20 to B29 (TSS-0096 to TSS-0145, 50 TSS).** Each has IMO 2025 research notes in `research/batches_imo2025/B20.md` to `B29.md`, but no Stage 2 classification or register row yet.
- Highest IDs in use: **VTS-0039** and **SRC-184**.

## Suggested split for three sessions

| Session | Work |
|---|---|
| AI 1 | Stage 2 for B20 to B24 (TSS-0096 to TSS-0120) |
| AI 2 | Stage 2 for B25 to B29 (TSS-0121 to TSS-0145) |
| AI 3 | Apply the project decisions (below) to B01 to B09, then a second pass on Unresolved rows using sources not yet tried (UKHO weekly Notices to Mariners, US NGA Sailing Directions, national radio-aids publications) |

Work only on your own batches. Do not edit another session's register rows or batch files.

## Reserved ID blocks

Allocate new IDs only from your own block. Gaps in numbering do not matter; duplicate IDs do.

| Session | VTS IDs | Source IDs |
|---|---|---|
| AI 1 | VTS-0100 to VTS-0199 | SRC-1000 to SRC-1999 |
| AI 2 | VTS-0200 to VTS-0299 | SRC-2000 to SRC-2999 |
| AI 3 | VTS-0300 to VTS-0399 | SRC-3000 to SRC-3999 |

Before creating a VTS or source record, search the registers for the same service or URL and reuse its existing ID. Legacy v0.2 services keep their normalised IDs (legacy VTS-00N becomes VTS-000N; for example Klang VTS is VTS-0004).

## Routine for every batch

1. **Before starting:** get the latest `main`.
2. Do the four-pass Stage 2 method in `research/prompts/STAGE_2_TSS_VTS_REPORTING_ASSOCIATION_PROMPT.md`.
3. **Immediately before writing:** get the latest `main` again.
4. Write only your own rows. **Add** rows to the register, VTS register and source register; never rewrite or re-sort other sessions' rows. Keep Unix line endings (LF).
5. Commit that one batch and upload it straight away, before starting the next.
6. If the upload is rejected because `main` moved, get the latest `main`, re-apply your additions and upload again. Never force-push.

## Project decisions (apply to every batch)

From `audits/stage2/Project_Decisions_2026-09-30.md`:

1. Shore monitoring of a TSS by a **VTS centre** outside a statutory VTS area counts as VTS coverage (for example NOR VTS, Norway). Monitoring by bodies that are not VTS centres (coastguard rescue centres, "control posts") stays a lead.
2. Tanker-only IMO Part I schemes (WETREP, CANREP) count as mandatory reporting (MRS), with applicability recorded.
3. National reporting schemes count as MRS, including schemes mandatory only for national-flag ships (for example MASTREP, SUNDAREP, LOMBOKREP, CHILREP, TÜBRAP). Routine reporting owed to a VTS is part of the VTS, not a separate MRS.
4. A VTS link resting only on evidence older than about three years, with no later official source, stays Unresolved.
5. An official port traffic centre whose defined area names the TSS counts as a VTS even if not called a VTS.

Never convert a failed search into "Neither confirmed"; that needs an authoritative source establishing absence.

## Useful tools already in the repository

- `research/stage2/write_stage2_batches.py`: writes register rows, batch files and audits from research output. It appends new rows and leaves other rows byte-for-byte unchanged. To allocate from your reserved block, run it with `STAGE2_VTS_START` and `STAGE2_SRC_START` set, for example `STAGE2_VTS_START=100 STAGE2_SRC_START=1000 python3 research/stage2/write_stage2_batches.py B20`.
- `research/stage2/resync_with_main.py`: renumbers a branch's own IDs after main has moved (only needed if working on a branch).
- `research/reconciliation/Legacy_v0_3_Findings_to_IMO_2025.csv`: earlier findings for TSS-0036 onward, usable as leads (not evidence).
