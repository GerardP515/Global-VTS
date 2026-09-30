# Stage 3 — Guide page research

**Purpose.** Collect sourced data for each `guide_page` so a later editorial pass can fill the seven first-screen slots and the supporting sections. This stage does not write shipboard guidance.

Governing documents:

- `docs/GUIDE_PAGE_SCHEMA.md` — page objects and render rules
- `docs/STAGE_2_COUNTING_AND_COMPLETION.md` — association gates
- `docs/AI_COORDINATION.md` — ID blocks and concurrent writes
- Master schema (linked objects; do not flatten)

---

## 1. Do not start Stage 3 on a page until Stage 2 allows it

Stage 2 answers: does this TSS have a VTS, a scheme, both, or an unresolved finding?

Stage 3 answers: who / when / channel / what / applicability / open notices / next sourced action.

A page may enter Stage 3 only when **all** of these are true:

1. Every TSS that the page will cover has a row in `data/current/TSS_VTS_MRS_Association_Register.csv` (not only a batch markdown note).
2. Every asserted VTS or Part I scheme on the page already has a canonical ID, **or** the page is explicitly `hold` until that ID is minted from the reserved block.
3. Association status is not an unchecked first-pass lead.
4. Contested-operator pages (Kerch, Crimea) stay `hold`. Research may record sources; it may not pick an operator.

B20–B29 pass-1 notes and `data/current/B20_B29_Association_Rows.csv` are **leads**. They are not Stage 2 completion. Run the four-pass Stage 2 method on those 50 TSS before opening their pages.

---

## 2. What Stage 3 produces

Per page, one research pack (markdown + rows), not a published chapter.

| Deliverable | Location |
|---|---|
| Page stub | `research/pages/PAGE-*.md` |
| First-screen field sheet | Same file, section `First screen` |
| Source list | `sources` IDs from the reserved block; reuse existing SRC where the URL already exists |
| Notice check | `page_notice` candidates in the pack |
| Open issues | `page_issue` list |
| Audit | `audits/stage3/PAGE-*_Audit.md` |

Do not write into the association register from Stage 3. That file stays Stage 2.

Do not mark `publication_status = current`. Stage 3 maximum is `editorial_status = scoped` or `draft`.

---

## 3. Source hierarchy (same as the page schema)

1. IMO instrument / Ships’ Routeing 2025 / MSC circular (identity, SOLAS V/11 scheme, cutover dates).
2. National administration, VTS authority, port authority users’ page or statutory text (operation, limits, channels, hours, language, reports).
3. Official HO publications: UKHO Weekly/Annual NtM, national equivalent, chart/ENC correction, NGA only as a lead unless it quotes the authority.
4. ALRS Volume 6 — licensed cross-check only. If it disagrees with IMO, IMO wins.
5. Historical guides — leads only.

A failed search is `unresolved`. It is not `confirmed_absent`.

A channel, call sign, GT threshold, reporting line or “next VTS” without a source row does not go on the first screen.

---

## 4. Method for one page

Work one page to close, then commit. Do not open five pages at once.

### Pass A — identity

Confirm official name, authority, centre(s), default call sign. List sectors on the same page. Reuse inventory VTS IDs. Search registers before minting.

### Pass B — first screen

Fill or mark unresolved:

1. Who + call sign
2. Channel now (per sector if needed)
3. When to call (inbound and outbound if the source splits them)
4. What to send (source order; IMO letters if used)
5. Applicability rule (GT / length / cargo / exemption as published)
6. Open notices (see Pass D)
7. Next sourced action or `no_known_requirement`

Also capture: hours, language, listen-watch, VHF-fail if published, pilotage vs VTS, ship-published secondary contact, chart/ENC numbers.

### Pass C — coverage

Link TSS with `whole` / `part` / `approach` and a source. Link the scheme or set `routine_vts_only`. Security reporting goes in `security_overlay` only.

### Pass D — notices

Check, and record the check date:

- Current UKHO Weekly Notice geographical section for that region
- Authority / VTS local notice page
- IMO circular if a scheme cutover is pending (e.g. ADRIREP 1 Dec 2026)
- ALRS correction only as secondary

Write one `page_notice` row per relevant notice. Unassessed relevant notices block `current` forever until assessed; they also block calling the pack “complete.”

### Pass E — audit

Independent read of every positive first-screen value and every `no_known_requirement`. If the source does not support the text, revert to `unresolved`.

---

## 5. Pilot order

Do not start with contested or empty pages.

| Order | Page | IDs to reuse | Why first |
|---:|---|---|---|
| 1 | Klang VTS / STRAITREP | `VTS-0004`, `VRS-0016`, TSS-0145+ | Stage 2 already exists on B30; handoff to Johor/Singapore is sourced |
| 2 | Roca Control / COPREP | `VTS-0023`, `VRS-0012`, TSS-0095–0096 | Identity already on B19/B20 edge |
| 3 | GIBREP | `VRS-0013`, TSS-0098 | Scheme frozen; VTS IDs only if Stage 2 mints Tarifa/Tangier |
| 4 | ADRIREP block | `VRS-0015`, TSS-0105–0110 | Must carry MSC.598(111) as a future notice |
| 5 | TSVTS | mint only after Stage 2 | One family, two centres, TUBRAP national not Part I |

Hold: Banco del Hoyo overlay, Kerch, Crimea, Jazan, Dondra, FA platform, UKMTO-only passages.

After the five pilots, estimate page count and diagram count from real packs. Do not extrapolate from one easy entry.

---

## 6. IDs and concurrency

- Reuse `VTS-*`, `VRS-*`, `TSS-*`, `SRC-*` already on `main`.
- New VTS/SRC IDs only from the session reserved block in `docs/AI_COORDINATION.md` (AI 3: `VTS-0300–0399`, `SRC-3000–3999`).
- Page IDs: `PAGE-VTS-0004`, `PAGE-VRS-0015`, etc. Never reuse a retired page ID.
- Pull `main` before and immediately before write. Append new files. Do not rewrite another session’s page pack.
- No force-push.

---

## 7. Page pack template

Use this heading set in `research/pages/PAGE-*.md`:

```
# PAGE-...
Status: scoped | draft | hold
Stage 2 prerequisite: list TSS IDs and register row dates

## First screen
1 Who
2 Channel now
3 When
4 What to send
5 Applicability
6 Open notices
7 Next sourced action

## Identity and sectors
## Hours language watch failure pilotage contacts charts
## Coverage (TSS and schemes)
## Security overlay (or none)
## Notices checked
## Issues
## Sources
```

Every non-empty operational line ends with `(SRC-xxxx)`.

---

## 8. Completion for one page

A page pack is **research-complete** only when:

- All seven first-screen slots are sourced or labelled `unresolved`
- Applicability is a rule, not “all ships” unless the source says that
- Notice check date is recorded
- Next action is sourced or `no_known_requirement`
- Audit file exists
- No channel copied from an old guide without a current authority or IMO source

A page pack is **not** a published guide entry. Technical review is a later stage.

---

## 9. Workload signal (after pilots)

From the five packs record:

- Hours per simple / intermediate / complex page
- Diagrams actually required
- Notice volume in one UKHO week for that region
- Fields that stayed unresolved after the hierarchy

Those five numbers feed the feasibility report. Do not invent a worldwide page total before the pilots exist.
