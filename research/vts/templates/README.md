# Research templates and field rules

## Current data model

Use [guide.template.yaml](guide.template.yaml) with [VTS_GUIDE_SCHEMA.md](../../../VTS_GUIDE_SCHEMA.md).
The owner requested YAML within each service's existing `dossier.md`.
YAML is the primary operational guide record; CSV tables will be generated exports, not parallel editable masters.
This replaces the earlier CSV-first storage decision while retaining its evidence and review controls.

The YAML file is a draft data template, not an executable schema validator.
Null collection items describe record shapes only. Unresearched dossiers use empty collections instead.
Preserve existing IDs, metadata and researched content when adopting the model.
No service dossier migration or YAML exporter has been implemented by this change.

The CSV headers below remain compatibility references for the pilot export mapping.
Do not assume their old field names already map directly to the new YAML names.
For example, evidence IDs and legacy claim IDs need an explicit stable mapping before exports are validated.
These files contain headers or null structures only. They are not operational evidence.
Create a real package only after an assignment is authorised.

## Identity

`study_id` identifies editorial scope. `vts_id` retains the existing canonical service identifier.
`direction_id` identifies a direction and route variant within a study.
Reporting object, event, contact, report-type, report-field and evidence IDs must be unique in their declared scope.
Use stable references, not row numbers that change after sorting.
Existing service, sector, centre and study counts remain distinct.

## Evidence

Every operational field requires evidence and a precise source locator.
`source_id` identifies the bibliographic source; `snapshot_id` identifies the exact held version.
`source_locator` identifies PDF/printed pages, clauses, annexes, table rows or stable HTML headings.
`supported_field_paths` identifies the precise guide fields supported by an evidence record.
`wording_as_published` retains the original. Interpretation must never overwrite it.
Use additional evidence records where different sources support different parts of a requirement.

`requirement_strength` uses MANDATORY, VOLUNTARY, RECOMMENDED, ON_REQUEST, INFORMATION or UNKNOWN.
`verification_state` uses UNCHECKED, AUTHOR_CHECKED, INDEPENDENTLY_CHECKED, CONFLICT or NOT_CHECKED.
INDEPENDENTLY_CHECKED requires an actual review record and exact input revision.
It is not release approval.

## Reporting

One event record represents one event for one direction and route variant.
`trigger_as_published` and `timing_as_published` retain the source conditions.
`reporting_object_id` may be null for a genuinely non-geographical trigger, with its basis recorded.
`contact_id` resolves to communications details; `report_type_id` resolves to the required report fields.
`evidence_ids` connects trigger, recipient, communications and applicability to the source records.
Use YAML lists for multiple references rather than hiding unrelated facts in one string.
Separate calling channel, working channel and listening watch.
Vessel applicability must be explicit; a blank is not universal applicability.

## Geometry

`geometry_type` uses POINT, LINE, AREA, BEARING_DISTANCE, VERBAL or UNKNOWN.
`geometry_as_published` preserves coordinates, labels and vertex order verbatim.
`datum_as_published` remains unknown when the source gives no datum. Do not assume WGS84.
Normalised graphics data is a reviewed technical derivative, not the original evidence.
Record the method and reviewer when conversion is required.
Operational values must not be invented to populate empty geometry fields.

## Gaps and conflicts

Severity uses BLOCKER, ERROR, OMISSION or NOTE.
A gap disposition must distinguish unanswered, inaccessible, defective, accepted limitation and resolved-with-evidence.
A conflict decision must retain both source assertions and its recorded authority/basis.
Resolved does not mean NO_VTS unless that specific outcome is evidenced.
Use the record requirements in VTS_GUIDE_SCHEMA.md before populating YAML gap or conflict collections.

## Packet

Replace null metadata and populate `files` with exact paths, bytes and SHA-256 values.
Each source snapshot must resolve to its manifest and original, or a permitted restricted-access record.
Include required renders and source-store revisions.
`unchecked_claim_ids` and `review_limitations` must remain explicit, including when empty.
Never fabricate a hash, retrieval time or reviewer.
The packet inventories its YAML-bearing dossier and any generated exports at their exact revisions.

## Effort

Record only observed effort. Keep active human minutes and elapsed minutes separate.
Model/tool counts may be recorded where available; unknown figures stay empty with a note.
The guide references the actual effort ledger rather than inventing measurements in its production metadata.
