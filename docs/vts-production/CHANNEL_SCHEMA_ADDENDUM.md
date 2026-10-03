# Channel pilot schema addendum

Version: `1.0-draft+channel.1`. Recorded: 3 October 2026.
Applies only to PILOT-01 / VTS-0001 while the common schema remains draft.
The existing 76 service identities, other dossiers and source originals are unchanged.

## Primary record

YAML front matter remains the primary operational record. Prose and entry tables are dependent views.
No separately edited operational CSV master is introduced.
Every new operational subject still requires evidence and a precise locator.

## Extensions tested by the pilot

| Field | Contract |
|---|---|
| `timing_conditions[]` | Stable `condition_id`, source-specific `wording_as_published`, and `evidence_ids`. Preserve different authoritative formulations. |
| `timing_summary` | Author-reconciled display wording supported by the timing-condition evidence. It must not discard a material condition. |
| Report-field `subitems[]` | Stable `subitem_id`, sequence, information, individual condition and evidence. Subitems do not create new official report-code groups. |
| `condition_scope` | `SUBITEMS_ONLY` for a mixed field. A whole-field applicability filter is prohibited for the tested X group. |
| `condition_mode` | `CONDITIONAL` or `NO_ADDITIONAL_CONDITION`. The latter applies within the parent report, not independently of vessel/report applicability. |
| `condition` | Typed parameter, comparison operator, value and unit. The tested parameter is bunker-fuel tonnes, not gross tonnage. Unknown quantities require review. |
| `report_delivery_options[]` | Link an option to its report type, subject scope, published method/timing, current implementation state, gap and evidence. |
| Contact `delivery_option_ids` | References existing delivery options. It does not establish a current delivery address or a whole-report exemption. |
| `event_mode` | `ENTRY` or `CONDITIONAL` in this bounded pilot. Conditional events are not scheduled position reports. |
| Event/contact `gap_ids` | Must resolve to an open gap explicitly covering the missing record or field. Unrelated gaps cannot excuse a missing recipient. |
| `recipient_as_published` | Source wording may be retained while the exact current routing remains unknown. This does not replace a required recipient reference. |
| Direction `sequence_semantics` | `EDITORIAL_DISPLAY_ORDER_NOT_FIXED_ITINERARY`. Sequence numbers order presentation, not when conditional events necessarily occur. |
| `scope_exclusions[]` | Identify unresearched variants and their scope rationale. Proposed editorial exclusions do not exempt vessels from requirements. |
| Contact `channel_role_note` | Explain the evidence scope when a calling channel is known but a separate working-channel role remains unestablished. |

## Identity and evidence

Selectors use stable IDs, for example `directions[P01-SW].reporting_events[SW-ENTRY]`.
Every referenced object must exist. Wildcards in gap scopes are resolved, not treated as a successful match by default.
Sequence values must be positive integers. Boolean values are rejected.
Calling/working channel values remain strings. Unknown values remain null with the relevant gap.
The original published reporting-line coordinates and datums were not changed by this addendum.

## Validator boundary

`scripts/validate_channel_pilot_v2.py` is read-only and specific to the corrected Channel pilot.
It checks draft integrity, declared evidence links, identifiers, packet hashes and the recorded regression cases.
It does not infer operational truth from a nonempty citation or certify current source currency.
The historical validator remains unchanged for replay against its original input.

A draft-integrity pass is separate from publication readiness.
`--release` returns a nonzero exit while evidence, geometry, notices or approvals remain outstanding.
The pilot has no independent evidence, marine, artwork or release approval.
A future approved revision requires the validator's approval contract to be updated against real review records.

## No automatic corpus migration

Do not insert Channel-specific fields or instructions into other services by generation.
Test the common schema on the remaining pilots before a separate approved migration.
