# Great Belt pilot: data-model additions

Recorded: 3 October 2026. Scope: PILOT-02 only.
Schema label: `1.0-draft+greatbelt.1`. No global migration or general schema approval is implied.

The pilot retains one canonical `research/vts/VTS-0002/dossier.md`.
The entry follows `entry-2` and `professional-1`; data additions below support the different reporting arrangements.

## Reporting events and communication actions

`communications_actions` stores mandatory channel changes which are not reporting events.
Each action has a stable ID, boundary reference, from/to contact IDs, conditions and evidence.
For the two Great Belt sector changes, `report_required` is false and `report_type_id` is null.
The action remains mandatory; absence of a verbal report does not make the channel change optional.

`common_reporting_events` stores internal departure and changed-particulars events once.
Directions reference these records rather than copying their operational values.
Alternative external entries remain separate events within each direction.
Their sequence numbers indicate display order, not successive calls on one passage.

The resulting population is six reporting events, two channel-change actions and two advance-delivery options.
These are different record types and must not be added together as ten compulsory reports.

## Participation and field conditions

Structured conditions preserve ANY versus ALL and strict versus inclusive operators.
Pleasure-craft exemption uses an OR condition distinct from the general participation OR condition.
The X bunker condition concerns gross tonnage, not bunker mass.
The W transmission rule explicitly rejects AIS-only completion under the documented Danish implementation.

## Geometry and narrative context

`boundary_vertices` stores ten published positions once.
Four external line records reference ordered vertex IDs; the sector parallel is a separate object.
There is no generated continuous polygon, safe route or inferred waypoint.

`reference_context` records sourced explanatory material and bridge/pilotage qualifications.
`route_codes` stores the authority's identifiers, not an approved passage itinerary.

## Source wording

English descriptions are author translations or paraphrases unless an exact source string is identified.
Original Danish participation wording and the English IMO coordinate notation are retained.
Each translated event carries a wording-basis note and an exact source locator/snapshot.
This pilot does not assert that translated English labels are verbatim Danish source wording.
A general schema should provide separate native-language excerpts and translated summaries consistently.

## Future changes

`future_changes` separates adopted, not-yet-effective instructions from the current field table.
The December 2026 insurance addition does not appear as an October reporting duty.
Its applicability must not inherit the bunker-reporting gross-tonnage condition automatically.
The entry carries a reassessment deadline, not automatic approval or scheduled background maintenance.

## Validation limits

`reviews/vts/checks/great_belt_pilot_check.py` is a bounded pilot checker, not a full generic schema implementation.
It checks selected invariants, relationships, formatting, negative cases and threshold/date boundaries.
It does not prove every claim, independently interpret Danish law or certify current instructions.
Source and publication holds remain in force.

## Correction revision: 1.0-draft+greatbelt.2

Recorded 3 October 2026. This extends only the Great Belt pilot.

- `report_delivery_options[*].mandatory_identifiers`: A/H are mandatory when the optional advance method is used.
- `reporting_policy.etr`: conditional arrival deadline, recommendation status, required VHF contact and unresolved combined timing.
- `communications[*].watch_applicability`: watch duty applies to every radio-equipped-by-requirement ship within the source scope.
- `participation.dangerous_goods_basis`: separate Order 1171 applicability and cargo definitions, not an inferred blanket exemption.
- `reference_context.bridge_east.lane_use_qualification`: subsection 10(3), sailing vessels and the unresolved exact-20 m overlap.
- `reference_context.bridge_east.speed_recommendations`: two recommendations with separate geographic scopes and operators.
- `reference_context.bridge_west.span_clearance`: 104 m navigation spans, central 70 m clearance width and mean-water-level reference.
- `reference_context.langeland`: separate recommended draught conditions for DW-T4 and Route Hotel.
- `reporting_policy.anchoring`: qualified general-provider statement, not a newly invented complete reporting event.
- `reference_context.temporary_works`: notice-check lead, without invented boundaries or current plotting approval.

The eight open gap records are G01-G08. The revised checker validates their links and evidence field paths.
The earlier six-gap checker and its historical results are not overwritten.
This is not a migration of other dossiers or approval of an operational instruction.
