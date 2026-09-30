# Coordination note for AI sessions working on Stage 2

Read this before starting any Stage 2 work. Several AI sessions work on this repository at the same time and write to the same shared files. These rules stop them overwriting each other or giving two things the same ID.

## Status on 30 September 2026

- Stage 2 results are in `data/current/TSS_VTS_MRS_Association_Register.csv` for **174 of 224 TSS**: B01 to B19 and B30 to B45.
- **Still to do: B20 to B29 (TSS-0096 to TSS-0145, 50 TSS).** Each has IMO 2025 research notes in `research/batches_imo2025/B20.md` to `B29.md`, but no Stage 2 classification or register row yet.
- Highest IDs in use (30 September 2026): **VTS-0042** and **SRC-192**. The reserved blocks below start well above these.

## Who did what, and what is left

| Session | Batches | Status |
|---|---|---|
| AI 1 | B01 to B10 | Stage 2 complete |
| AI 2 | B10 to B19 and B30 to B45 | Stage 2 complete |
| AI 3 | B20 to B29 | IMO 2025 research notes complete; **Stage 2 still to do** |

**Remaining work:** AI 3 turns its B20 to B29 research into Stage 2 results: classify each TSS under the prompt, run the four passes (with an independent Pass 4 check of every positive and every "Neither confirmed"), add register rows, and write `audits/stage2/B20_Association_Audit.md` to `B29_Association_Audit.md`. The legacy leads file and the neighbouring batches' results (for example B30 for STRAITREP, VTS-0004 Klang VTS) will help.

**Optional follow-up** for AI 1 or AI 2: apply the project decisions below to any earlier batch they change (for example monitoring services outside a declared VTS area in B01 to B09), and a second pass on Unresolved rows.

Work only on your own batches. Do not edit another session's register rows or batch files without saying so in your commit.

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


## Mandatory storage controls added 30 September 2026

Read current main before every write. Preserve concurrent changes.
Use a CSV parser/writer, never physical-line replacement or hand-concatenated CSV.
Check IDs across the complete live register before allocating new ones.
Do not rerun historical ID-resynchronisation scripts against current data.
Run the validator and regression tests before committing.
A Git commit is not an evidence audit, and row coverage is not research completion.
