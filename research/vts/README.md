# VTS production research

Read [VTS_GUIDE_SCHEMA.md](../../VTS_GUIDE_SCHEMA.md) for the YAML data model.
Then follow [VTS_RESEARCH_PROMPT.md](../../VTS_RESEARCH_PROMPT.md) for source-first research and review.
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

## YAML data decision: 2 October 2026

The owner requested YAML and accepted the directional data model inferred from Iain's email.
The canonical operational record will be YAML front matter within each existing dossier.
The Markdown body is its readable narrative; CSV tables and graphics are dependent exports.
This supersedes the earlier CSV-first storage instructions, not the source, review or release controls.
See [the schema specification](../../VTS_GUIDE_SCHEMA.md) and [YAML template](templates/guide.template.yaml).

The template contains null record prototypes to show structure. Use empty collections in an unresearched dossier.
Preserve all existing identity metadata and research work when adopting it.
No migration of the 76 dossiers, YAML exporter or full schema validator has been performed by this setup.
The old CSV headers remain compatibility templates, not separately editable operational masters.

## Study packages and supporting files

A study may reference one or more service dossiers. Record study scope and directions separately from service identity.
For a single-service study, keep its supporting files beside `dossier.md`.
For a combined study, designate an owning dossier and reference the others without copying their operational records.
Do not assume one service means one area, centre or spread.

The supporting package includes:

- Source manifests identifying the exact original files and versions.
- `packet.json`: exact input versions, paths, bytes and hashes for independent review.
- An effort ledger recording actual effort only.
- Derived evidence, reporting, geometry, gap and conflict tables when an exporter is implemented.
- Graphics data and PDF outputs tied to an approved dossier revision.

An unopened register URL is a lead, not a held or verified source.
All directions require separate research; none is inferred by reversing another direction.
Generated exports must not compete with hand-edited YAML for authority.

## Status and storage

`STATUS.csv` continues to track the proposed pilot studies. It is not a count of service scaffolds.
The service dossiers record their own research state and remain unapproved until actual review occurs.
Do not reset an existing researched dossier during regeneration or import.

Original source files belong under `sources/archive/`; capture manifests belong under `sources/manifests/`.
Shared sources are stored once and linked to multiple dossiers.
Reviews belong under `reviews/vts/reports/` and publication artefacts under `production/vts/`.
A Git commit or merge is not navigational or publication approval.
