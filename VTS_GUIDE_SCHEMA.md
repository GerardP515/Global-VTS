# Global VTS Guide: YAML data requirements

Version: 1.0-draft | Recorded: 2 October 2026 | Status: design saved; validator and migration not implemented

Template: [guide.template.yaml](research/vts/templates/guide.template.yaml).
Research method: [VTS_RESEARCH_PROMPT.md](VTS_RESEARCH_PROMPT.md).
Existing service files: [regional index](research/vts/INDEX.md).

## 1. Basis in Iain's brief

This specification follows Iain's email supplied in the project conversation.
It distinguishes his publication requirements from the data model inferred to support them.
It does not make operational assertions about any particular VTS.

| Requirement in the supplied email | Data implication |
|---|---|
| A double-page spread for each VTS area and applicable direction | Separate service, guide area, direction, route variant and spread identifiers |
| A graphic showing each reporting point | Source-backed geometry, official names, graphic labels and event links |
| A clear statement of information required at each report | Report types, ordered fields, conditions and evidence |
| Examples covering approximately three areas, with both directions | Explicit pilot scope and separate directional sequences |
| Agreement on a common style sheet | Style-sheet revision and consistent graphic-data relationships |
| A realistic understanding of development time | Actual acquisition, research, review, correction, artwork and QA effort |
| PDF examples as the initial output | Versioned PDF output paths and checks against the approved research |

Communications details, vessel applicability, source provenance and review gates are inferred design requirements.
They are needed to make the proposed reporting spreads usable and auditable.
The email is not evidence for a reporting duty, a VHF channel or a worldwide VTS count.

The central question is:

> For this transit, where and when must the vessel report, who receives it, and what information is required?

## 2. Publication and identity model

`service -> guide area -> direction/route variant -> reporting event -> report information -> evidence`

The reporting event is the central research record.
A reporting location alone does not establish a duty or identify the affected vessels.
One location can support different events for different directions or vessel categories.
Some events arise from time or circumstances rather than a geographical position.

A service is not a centre, sector, reporting scheme or double-page spread.
One service may support several spreads. A study may reference several services.
For combined studies, designate one owning dossier and reference other service IDs and dossiers without copying their facts.
If one service requires separate guide areas, approve that study structure before extending this draft model.
Do not silently force unrelated areas into one scope or duplicate a service to increase the count.

## 3. YAML as the canonical guide record

The owner requested one Markdown file per service, with YAML.
Use YAML front matter within the existing `research/vts/<VTS-ID>/dossier.md`.
The Markdown body remains the readable research narrative and review commentary.
Operational values are maintained in YAML once, then reused in prose, tables and graphics.

This data-storage decision supersedes the earlier CSV-first instructions in the research scaffold.
In particular, apply this decision when reading sections 9, 10, 12 and 20 of `VTS_RESEARCH_PROMPT.md`.
References there to maintaining operational CSV tables now mean producing derived views from YAML.
All source-first, independent-review, correction, geometry and release controls remain in force.

Existing discovery registers remain unchanged. Source manifests remain separate records of actual captured files.
`packet.json` remains an independent inventory of the exact review inputs.
Effort and signed review records may remain separate ledgers referenced from the guide.
CSV and graphics exports must identify their originating dossier revision; they are not parallel editable masters.

The earlier CSV header templates are retained for compatibility and mapping during the pilot.
No YAML-to-CSV exporter, full schema validator or 76-file migration is supplied by this change.
Do not claim a legacy CSV checker validates the YAML without an implemented, tested adapter.

## 4. How to use the template

The YAML file describes field structure, not a researched guide.
Its null collection items are record prototypes, not genuine reporting events or sources.
In an unresearched dossier use empty collections instead of copying prototype records.
Populate records only when evidence or an explicitly identified research question exists.

Preserve the existing `vts_id`, `region_code`, `project_class`, provenance and state when adopting the template.
Do not reset researched content to `NOT_STARTED` or `REGISTER_SEED_ONLY`.
Do not manufacture a `study_id`, scope, reporting direction or approval to fill an empty field.
The root region is the service's editorial region; `guide_area.region_code` is the assigned study region.
Record any difference rather than changing the service's inventory classification.

Use null for an unknown scalar. Use an empty list for no records captured yet.
Neither means that no reporting obligation exists.
A substantive unresolved question needs a gap record before research can be called ready for review.

## 5. Guide data dictionary

| Group | Required research data | Purpose |
|---|---|---|
| Identity | Service ID, guide-area ID, study ID, publication title, official name and associated service IDs | Stable identity without conflating services and spreads |
| Scope | Region, countries, geographical scope, related TSS, authority and provider | Define the limits of the guide |
| Participation | Published applicability, requirement strength, thresholds, conditions and exemptions | Identify affected vessels |
| Reporting objects | Object ID, official name, displayed label, geometry type, published geometry, datum and sector ID | Locate reporting triggers accurately |
| Communications | Recipient, call sign, method, calling channel, working channel, listening watch and alternatives | Identify whom to contact and how |
| Report types | Official name, field IDs, codes, order, required information and conditional fields | State the information required |
| Directions | Direction ID, official movement description, route variant, scope and vessel applicability | Keep transit sequences separate |
| Events | Event ID, sequence, trigger, timing, applicability, recipient link, report link, exceptions and subsequent action | Connect location or circumstance to the required report |
| Spread | Spread ID, title, layout, map extent, referenced reporting objects/events and graphics data | Supply the double-page presentation |
| Evidence | Evidence ID, bibliographic source ID, exact snapshot, precise locator and supported fields | Trace each operational statement |
| Assurance | Research cutoff, notices check, independent review, marine approval, artwork QA and release records | Separate research from publication approval |
| Production | Research/schema/style revisions, actual effort record and PDF outputs | Support repeatable production and measured effort |

## 6. Directional event rules

Research each direction independently. Never create the opposite direction by reversing the first sequence.
Retain joining, crossing and leaving movements as separate route variants where the approved scope requires them.
Do not infer cardinal direction from the page orientation.

Keep entry, pre-entry, passing, sector-transfer, changed-particulars and incident reports distinct.
A channel change is not automatically a new report.
A pilot boarding position is not automatically a reporting point.
AIS carriage does not automatically remove a voice-reporting requirement.
Port-bound reporting must not become an instruction for all through traffic.

Each event links to its reporting object, communications record, report type and supporting evidence IDs.
A non-geographical event may have a null reporting-object ID, with its trigger explicitly documented.
A non-radio event may have null VHF fields, with its published communication method documented.
Do not invent a point or a radio channel to satisfy a template.

Every mandatory statement must retain the source's applicability and exceptions.
Preserve threshold operators, units and qualifications exactly.
Do not interpret an empty applicability field as universal participation.

## 7. Graphics and geometry

Supported geometry types: POINT, LINE, AREA, BEARING_DISTANCE, VERBAL and UNKNOWN.
Retain published positions, notation, precision, vertex order, labels and datum without silent correction.
An unknown datum stays unknown. A reporting line remains a line.
A direction arrow is not an approved track or a source of invented waypoints.

Normalised graphics data must be a traceable derivative of the published geometry.
Record any conversion and review outside the original value; a format conversion is not a datum transformation.
Every plotted object and callout must resolve to the same IDs used by the reporting events.
Map context and base material need a recorded source and appropriate reproduction permission.

The `DOUBLE_PAGE` layout value expresses Iain's publication concept only.
It does not establish page dimensions, cartographic accuracy or an approved style sheet.
Inspect the finished PDF as page images against the approved data before release.

## 8. Evidence and source records

Every operational field needs evidence; one general reference for an entire guide is insufficient.
`source_id` identifies the publication. `snapshot_id` identifies the exact held version.
The capture manifest retains issuer, publication date, retrieval date, original-file path, hash and permissions.
The guide's effective dates describe the applicable provision, not merely when a webpage was retrieved.

`source_locator` identifies the page, clause, annex, table row, heading or feature used.
`supported_field_paths` identifies the exact fields supported by an evidence item.
Use stable-ID selectors rather than array positions that change after sorting.
Preserve the author's interpretation separately from `wording_as_published` in the dossier narrative.
An interpretation cannot silently replace the source wording or become a mandatory instruction.

Source extracts are derived from held originals, never authored summaries presented as source files.
Foreign-language requirements retain original wording and a traceable translation record.
Sources shared by several guides are stored once and referenced by ID.

## 9. Gaps and conflicts

A gap record should include `gap_id`, affected field paths, missing information, reason, severity and next action.
It should also record disposition, any resolution evidence IDs and the decision record.
Distinguish not searched, not located, inaccessible, not inspected, absent within the inspected scope, defective and ambiguous.

A conflict record should include `conflict_id`, affected fields and each assertion with its evidence IDs.
Retain the competing assertions, effective periods, decision basis, reviewer and resolution record.
Use HOLD where a safety-bearing conflict lacks a defensible resolution.
A source-inclusion decision for the discovery register does not settle a reporting instruction.

An owner-reported resolution needs a disposition record before factual fields change.
Resolved does not mean NO_VTS unless that particular outcome is supported.
Empty gap/conflict lists at NOT_STARTED do not certify that the guide has no gaps or conflicts.

## 10. Permitted states and validation requirements

Requirement strength: MANDATORY, VOLUNTARY, RECOMMENDED, ON_REQUEST, INFORMATION or UNKNOWN.
Evidence state: UNCHECKED, AUTHOR_CHECKED, INDEPENDENTLY_CHECKED, CONFLICT or NOT_CHECKED.
Research state follows the lifecycle defined in `VTS_RESEARCH_PROMPT.md`.
An independent evidence check is not marine approval or permission to publish.

All IDs must be unique in their declared scope and every reference must resolve.
Sequence values are positive integers within a direction/variant or ordered report type.
Quote coordinates, VHF channel strings, report codes and timestamps to preserve their source representation.
Reject duplicate YAML keys rather than accepting a silently overwritten field.
Never place invented hashes, reviewer names or dates in approval records.

A future validator must check identifiers, types, references, event ordering, evidence coverage and state-dependent requirements.
Publication readiness requires no unaddressed safety blockers and actual review/approval records for the exact revision.
Unknown or unreviewed fields may exist in a draft; they cannot silently pass a release check.
YAML parsing alone proves syntax, not completeness, operational accuracy or release readiness.

## 11. Effort and boundaries

Record actual acquisition, extraction, research, review, correction, graphics and PDF-checking effort separately.
Distinguish active human minutes, elapsed time and model/tool usage.
Leave unknown effort unmeasured with a note; do not backfill assumed production timings.
Use the three pilots to establish the style and realistic development effort before wider production.

This is not a complete passage-planning or port-entry schema.
Cargo handling, bunkering, berth facilities and towage are excluded unless they directly affect the reporting scope.
The guide remains supplementary to the appropriate official navigational publications.

## 12. Change boundary and next implementation gate

This commit saves the agreed draft data model and its YAML template.
It updates the research-folder guidance to record YAML as the primary guide data.
It does not change any of the 76 service memberships, classifications, reporting instructions or research states.
It does not migrate the service dossiers, acquire sources, implement exporters or claim independent verification.

Before production use, implement and test the validator and export mapping on one assigned pilot.
Test unknown fields, non-geographical triggers, repeated source use, both directions and invalid references.
Record any pilot-driven schema changes before applying them across other guides.
