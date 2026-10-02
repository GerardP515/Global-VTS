# VTS production research

Start with [VTS_RESEARCH_PROMPT.md](../../VTS_RESEARCH_PROMPT.md).
Use the [regional index](INDEX.md) to open an individual service file.
This folder is separate from legacy TSS-discovery batches.

## One Markdown file per service

Each of the 76 registered services has one working file: `<VTS-ID>/dossier.md`.
These files start as `REGISTER_SEED_ONLY` scaffolds, with production research `NOT_STARTED`.
They preserve the service ID, name, project class, region, TSS links and existing source IDs.
The [frozen register input](inputs/README.md) retains the remaining inventory fields and historical caveats.
Source-first research has not been performed merely because these files exist.
Core is a project class, not proof of formal VTS designation.

Develop the same dossier in place when a service is assigned. Do not create duplicate per-service Markdown files.
Scaffold creation supplies headings and inherited inventory metadata only; it does not author operational guide text.
The protocol's source-first rule applies before adding reporting instructions or an evidence-based narrative.

## Study packages and structured data

A study may reference one or more service dossiers. Record study scope and directions separately from service identity.
For a single-service study, keep its supporting files beside `dossier.md`.
For a combined study, its packet references the existing service dossiers rather than copying them.

Create these files from `templates/` only as research begins:

- `evidence.csv`: atomic claims and precise source citations.
- `reporting_matrix.csv`: directional events, triggers and applicability.
- `report_fields.csv`: required information for each report type.
- `reporting_geometry.csv`: as-published points, lines, areas and verbal triggers.
- `gaps.csv` and `conflicts.csv`: missing evidence and source disagreements.
- `packet.json`: exact input versions, paths, bytes and hashes.
- `effort.csv`: observed effort only.

The CSV tables remain the canonical operational data once populated. Dossier prose and graphics are dependent views.
An unopened register URL is a lead, not a held or verified source.
All directions require separate research; none is inferred by reversing another direction.

## Status and storage

`STATUS.csv` continues to track the proposed pilot studies. It is not a count of service scaffolds.
The service dossiers record their own research state and remain unapproved until actual review occurs.
Do not reset an existing researched dossier during regeneration or import.

Original source files belong under `sources/archive/`; capture manifests belong under `sources/manifests/`.
Shared sources are stored once and linked to multiple dossiers.
Reviews belong under `reviews/vts/reports/` and publication artefacts under `production/vts/`.
A Git commit or merge is not navigational or publication approval.
