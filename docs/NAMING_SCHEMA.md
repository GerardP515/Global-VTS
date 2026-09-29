# Naming and Identifier Schema

## Principle

Identity and geography are separate.

The canonical identifier must remain stable even if:

- an official name changes;
- a boundary changes;
- the editorial region changes;
- a service is reorganised.

## Canonical identifiers

Use four digits initially.

| Entity | Format | Example |
|---|---|---|
| Traffic Separation Scheme | `TSS-NNNN` | `TSS-0001` |
| Vessel Traffic Service | `VTS-NNNN` | `VTS-0001` |
| Vessel reporting scheme | `VRS-NNNN` | `VRS-0001` |
| VTS centre | `CTR-NNNN` | `CTR-0001` |
| Sector or zone | `SEC-NNNN` | `SEC-0001` |
| Source | `SRC-NNN` | `SRC-001` |
| Relationship | `REL-NNNN` | `REL-0001` |

Existing workbook identifiers using `SRS-` may be retained during migration and mapped to `VRS-` through the crosswalk.

## Regional reference

A human-readable regional reference may be generated from the canonical entity.

Example:

`TSS-BAL-014`

This is an editorial reference only.

It must never replace `TSS-0048` as the permanent identity.

## Regional codes

| Code | Region |
|---|---|
| BIS | British Isles and southern North Sea |
| NOI | Norway and Iceland |
| BAL | Baltic Sea and approaches |
| NSC | North Sea continental coast |
| FIC | France, Iberia and Canary Islands |
| MED | Mediterranean and Black Seas |
| SAF | Southern Africa |
| RSA | Red Sea and Arabian region |
| IOS | Indian Ocean and South Asia |
| MSI | Malacca, Singapore and Indonesia |
| CSC | China Sea and China |
| NWP | North-west Pacific |
| AUS | Australia |
| NPC | North America Pacific coast |
| CAP | Central and South America Pacific coast |
| CGP | Caribbean, Gulf of Mexico and Panama |
| NAC | North America Atlantic coast |

These are project editorial regions. They are not IMO codes.

## Official names

Store the official name exactly as supported by the source.

Recommended fields:

- `canonical_id`
- `official_name`
- `previous_name`
- `alternate_name`
- `regional_ref`
- `region_code`
- `state_or_states`
- `adoption_instrument`
- `adoption_date`
- `implementation_date`
- `current_status`

## Number allocation

Canonical numbers are sequential and never reused.

Deleted, withdrawn or superseded entities retain their IDs.

Do not renumber records to close gaps.

## Grouped source labels

A grouped heading such as a source entry covering several routeing measures retains a traceability record.

Verified component schemes receive their own canonical IDs.

The source-row ID and verified entity IDs must be linked through the relationship or crosswalk table.

## File naming

Use:

`<EntityID>_<short-name>.md`

Example:

`TSS-0005_Dover_Strait.md`

For release datasets:

`Global_VTS_Inventory_v0_2.xlsx`

Use underscores within release filenames and semantic version numbers in release notes.
