# Research templates and field rules

These files contain headers or null structures only. They are not operational evidence.
Create a real package only after an assignment is authorised.

## Identity

`study_id` identifies editorial scope. `vts_id` retains the existing canonical service identifier.
`direction_id` identifies a direction and route variant within a study.
`claim_id`, `event_id`, `geometry_id` and `report_type_id` must be unique within the study.
Use stable references, not row numbers that change after sorting.

## Evidence

Every operational value requires a claim ID and a precise citation.
`source_id` identifies the bibliographic source; `snapshot_id` identifies the exact held version.
`locator` must identify PDF/printed pages, clauses, annexes, table rows or stable HTML headings.
`value_as_published` retains the original. `interpretation` must never overwrite it.
Use additional evidence rows when different sources support different parts of a requirement.

`requirement_strength` uses MANDATORY, VOLUNTARY, RECOMMENDED, ON_REQUEST, INFORMATION or UNKNOWN.
`verification_state` uses UNCHECKED, AUTHOR_CHECKED, INDEPENDENTLY_CHECKED, CONFLICT or NOT_CHECKED.
INDEPENDENTLY_CHECKED requires an actual review record and exact input revision.
It is not release approval.

## Reporting

One matrix row is one event for one direction and route variant.
`trigger_text` preserves conditions and timing; `geometry_id` is blank for genuinely non-geographical triggers.
`report_type_id` joins the event to required report fields.
`claim_ids` identifies evidence for the trigger, recipient, communications and applicability.
Use semicolon-separated IDs only for references, not to hide unrelated facts in one value.
Separate call channel, working channel and listening watch.
Vessel applicability must be explicit; a blank is not universal applicability.

## Geometry

`geometry_type` uses POINT, LINE, AREA, BEARING_DISTANCE, VERBAL or UNKNOWN.
`geometry_as_published` preserves coordinates, labels and vertex order verbatim.
An unknown datum stays unknown. Do not assume WGS84.
`normalised_geometry_path` is optional and names a reviewed technical derivative, not the original evidence.
`transformation_record` identifies the method and reviewer when conversion is required.
Operational values must not be invented to populate empty geometry fields.

## Gaps and conflicts

Severity uses BLOCKER, ERROR, OMISSION or NOTE.
A gap disposition must distinguish unanswered, inaccessible, defective, accepted limitation and resolved-with-evidence.
A conflict decision must retain both source assertions and its recorded authority/basis.
Resolved does not mean NO_VTS unless that specific outcome is evidenced.

## Packet

Replace null metadata and populate `files` with exact paths, bytes and SHA-256 values.
Each source snapshot must resolve to its manifest and original, or a permitted restricted-access record.
Include required renders and source-store revisions.
`unchecked_claim_ids` and `review_limitations` must remain explicit, including when empty.
Never fabricate a hash, retrieval time or reviewer.

## Effort

Record only observed effort. Keep active human minutes and elapsed minutes separate.
Model/tool counts may be recorded where available; unknown figures stay empty with a note.
