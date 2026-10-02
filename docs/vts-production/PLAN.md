# VTS Guide production plan

Recorded: 2 October 2026. Status: protocol and scaffold prepared; pilot research not executed by this change.

## Commission

Iain's email, supplied by the project owner, prioritises the Global VTS Guide over new Kiel Canal development.
The immediate deliverables are representative directional PDF examples for approximately three VTS areas.
The prototypes must establish the style sheet, repeatable process and actual development effort.
The message does not establish a verified worldwide area count or approve the suggested pilot selections.
Personnel matters in the email are outside this research protocol.

## Architecture

The source-first workflow is:

`assignment -> acquire -> validate capture -> catalogue -> extract/render -> evidence matrix -> directional reporting -> review -> correction/re-proof -> marine approval -> layout -> graphic QA -> release`

The main prompt is `../../VTS_RESEARCH_PROMPT.md`.
The lessons register is `LESSONS_LEARNED.md`.
Research examples and schemas are under `../../research/vts/templates/`.
Originals and derivatives are separated under `../../sources/`.

Source acquisition must precede claims. A library of URLs alone is not a checked source corpus.
Keep the TSS-derived register unchanged by this setup.
Do not import the separate Australian census into the guide population automatically.

## Pilot gates

| Gate | Deliverable | Acceptance |
|---|---|---|
| M0 Protocol | Master prompt, lessons, source hierarchy and templates | Owner review of method; folders exist |
| M1 Evidence pilot | One complete study with both applicable directions | Held evidence, reporting matrix, geometry and source-located claims |
| M2 First PDF pair | Directional examples for the first study | Marine review and graphic QA; style decisions recorded |
| M3 Second study | Another area testing sector transitions | Template amended only through recorded decisions |
| M4 Third study | A complex multi-sector or multi-authority example | Scope, applicability and transfers remain readable |
| M5 Production baseline | Approved style sheet, measured effort and batch procedure | Owner approves process before five-study batches |

Proposed candidates are Channel VTS, Great Belt VTS, and a bounded Singapore/STRAITREP study.
These are proposed test cases, not source-verified assignments or commissioned outputs.
See `../../research/vts/PILOT_PLAN.md` before execution.
Do not multiply three VTS names by two and assume six identical layouts.
Route variants and directions must be resolved from the sources and editorial scope.

## Components to implement after protocol approval

These names are planned components, not scripts installed by this scaffold.

| Component | Purpose | Required tests |
|---|---|---|
| acquire_vts_sources.py | Retrieve permitted sources; append capture outcomes | Invalid PDF; HTTP challenge; redirects; query-specific URLs; retries |
| index_vts_sources.py | Generate register views from manifests | Duplicates; missing files; immutable versions; no invented totals |
| extract_vts_sources.py | Produce traceable text and page derivatives | Page boundaries; tables; image-only files; original hashes |
| build_vts_review_packet.py | Assemble exact versioned review inputs | Missing renders; changed sources; wrong-file binding |
| validate_vts_research.py | Check identifiers, claims, events and links | CSV multiline fields; unparsed references; no false empty pass |
| check_vts_source_scope.py | Flag service/direction/applicability mismatches | Correct port but wrong sector; port-bound versus through traffic |
| build_vts_graphics_data.py | Export approved geometry and labels | Axis order; directions; source-to-symbol correspondence |
| assess_vts_source_changes.py | Identify affected claims after source changes | New notices; unchanged bytes; only website furniture changed |

Use existing libraries and validators only after checking their interfaces and limits.
No component may silently alter canonical operational values to satisfy a parser.
A single shared manifest or register needs serialised updates or an explicit locking strategy.

## Storage decision

Create source folders inside the existing Global-VTS repository for the pilot.
This change does not create or claim a separate Global-VTS-Ref-Files repository.
The storage manifest permits a later sibling repository or managed archive.
Before migration, verify permissions, capacity, identifiers, hashes and pinned source-store revisions.
Store restricted publications only in a permitted location; record access references rather than unauthorised copies.

## Effort model

Measure acquisition, extraction, research, independent review, correction, layout, and final QA separately.
Record failed acquisition time and shared-source reuse.
Do not use model latency as a substitute for production effort.
Do not promise dates from unmeasured per-area assumptions.
After three pilots, publish observed ranges, bottlenecks and any further calibration needed.

## Setup boundary

This commit establishes instructions, empty ledgers, templates and folders.
It does not download sources, research the pilots, certify the existing register, run a scheduler or release navigational material.
