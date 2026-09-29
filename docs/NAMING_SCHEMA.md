# Naming and Identifier Schema

## Principle

Identity and geography are separate. Canonical identifiers remain stable if a name, boundary, region or service structure later changes.

## v1.0 baseline migration

The v0.1 and v0.2 `TSS-xxxx` identifiers were provisional candidate IDs derived before the IMO 2025 baseline was available. They are now treated as **legacy IDs**.

Version 1.0 freezes the authoritative TSS sequence as `TSS-0001` through `TSS-0224`, ordered by IMO Part B source order and component order within multi-TSS parent entries.

The one-time migration is documented in `research/reconciliation/TSS_Crosswalk_Legacy_v0_2_to_IMO_2025.csv`.

**From v1.0 onward, canonical IDs must never be renumbered or reused.**

## Canonical identifiers

| Entity | Format | Example |
|---|---|---|
| Traffic Separation Scheme | `TSS-NNNN` | `TSS-0001` |
| Vessel Traffic Service | `VTS-NNNN` | `VTS-0001` |
| Vessel reporting scheme | `VRS-NNNN` | `VRS-0001` |
| VTS centre | `CTR-NNNN` | `CTR-0001` |
| Sector or zone | `SEC-NNNN` | `SEC-0001` |
| Source | `SRC-NNN` | `SRC-001` |
| Relationship | `REL-NNNN` | `REL-0001` |

## IMO parent references

Each TSS record retains the source parent reference, for example `B-II/10`. A parent entry may contain one or several TSS records.

Parent references are source locators, not canonical project identifiers.

## Regional reference

A human-readable regional reference may later be generated, for example `TSS-BAL-014`. It remains metadata and never replaces the canonical ID.

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

These are project editorial regions, not IMO codes. Region allocation is separate from identity.

## Grouped source entries

A Part B parent entry is retained as a source entity. Where IMO names or explicitly enumerates several TSS within that parent, each receives its own canonical TSS ID.

A single named TSS is not split merely because it contains several parts, zones, lanes or precautionary areas.

## File naming

Use `<EntityID>_<short-name>.md` for entity files and semantic versioning for release datasets.
