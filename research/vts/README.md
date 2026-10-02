# VTS production research

Start with `../../VTS_RESEARCH_PROMPT.md`.
This folder is separate from legacy TSS-discovery batches.

For each authorised study create `<study-id>/` with:

- `dossier.md`: evidence-based research narrative and declared scope.
- `evidence.csv`: canonical atomic claims and citations.
- `reporting_matrix.csv`: directional reporting events and conditions.
- `report_fields.csv`: required information for each report type.
- `reporting_geometry.csv`: as-published reporting points, lines, areas or verbal triggers.
- `gaps.csv` and `conflicts.csv`: explicit missing evidence and unresolved contradictions.
- `packet.json`: exact input files, source snapshots, hashes and review scope.
- `effort.csv`: actual stage effort; never invented estimates presented as measurements.

Copy headers from `templates/`; do not populate them with illustrative operational values.
The CSV tables are the canonical operational data. Dossier prose and graphics are dependent views.
Do not maintain conflicting hand-edited JSON and CSV versions of the same facts.

Original sources belong under `sources/archive/`, not here.
Reviews belong under `reviews/vts/reports/`.
Publication artefacts belong under `production/vts/`.
