# Channel pilot: first correction re-proof

Date: 3 October 2026. Role: author-side re-proof, not independent review.
Input research commit: `f8a6580195d0137cfbdd5f8c00d6d1ca14514a44`.
Input dossier SHA-256: `45b517e8a953faf2f26b119caa36d695b9c218e8b21fc5879b3e434c08e0358c`.

The Stage 1 correction was read completely against its existing evidence and the reopened source provisions.
New sources remain live comparisons where no permitted retained original exists.
The correction scope remains one service, two directions, six events and thirteen official main report-code groups.

| ID | Severity | Finding | Required action |
|---|---|---|---|
| RR-01 | NOTE | SRC-005 sections 3.10-3.11 explicitly identify calling channels. Separate working-channel roles are not established there. | Preserve calling channels 11/13. Set the separately modelled working-channel fields unknown and link G04. Do not claim the channel numbers are wrong. |
| RR-02 | OMISSION | The regenerated entry table supplies timings but not the named reporting boundary in its own column. | Generate a boundary-label column from the existing object ID; do not change geometry. |
| RR-03 | ERROR | Python comparisons can accept a Boolean sequence value because True equals 1. | Require positive integers excluding Boolean values. Add a defective-input regression case. |

QA-01 to QA-06 changes remain supported within their stated source scope.
The X bunker condition is applied to its first subitem only; the second subitem stays within the parent report.
The six events are not six mandatory routine calls: four are conditional author-modelled event records.
No default AIS exemption, new radio address, reporting line endpoint or datum was introduced.
Apply these refinements, then re-proof the resulting committed dossier and regenerated packet.
