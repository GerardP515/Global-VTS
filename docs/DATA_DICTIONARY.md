# Data Dictionary

## Core tables

### TSS

Minimum fields:

| Field | Meaning |
|---|---|
| canonical_id | Permanent TSS identifier |
| source_record_id | Original extracted source-row identifier |
| official_name | Current official name |
| previous_name | Superseded official name |
| region_code | Project editorial region |
| state_or_states | Relevant coastal State or States |
| record_type | Verified entity, grouped source row or research lead |
| baseline_status | Status of reconciliation against authoritative routeing baseline |
| current_status | Current, withdrawn, superseded or unresolved |
| adoption_instrument | IMO or national instrument |
| adoption_date | Date adopted |
| implementation_date | Date brought into effect |
| source_id | Primary source identifier |
| source_locator | Page, section, annex or named section |
| last_checked | Date of last verification |

### VTS

| Field | Meaning |
|---|---|
| canonical_id | Permanent VTS identifier |
| official_name | Service name |
| authority | Operating authority |
| area_name | Named VTS area |
| status | Operational, temporary, planned, suspended or unresolved |
| centre_ids | Linked centres |
| sector_ids | Linked sectors |
| participation | Mandatory, voluntary or mixed where applicable |
| source_id | Supporting primary source |
| last_checked | Date checked |

### Vessel reporting scheme

| Field | Meaning |
|---|---|
| canonical_id | Permanent scheme identifier |
| official_name | Formal scheme name |
| scheme_type | Mandatory or voluntary |
| legal_basis | IMO resolution, national rule or other authority |
| authority | Responsible administration |
| area | Geographical coverage |
| associated_vts_ids | Related VTS |
| source_id | Primary source |
| last_checked | Date checked |

### VTS centre

| Field | Meaning |
|---|---|
| canonical_id | Permanent centre identifier |
| official_name | Centre or call name |
| authority | Operator |
| associated_vts_ids | Services managed |
| associated_sector_ids | Sectors managed |
| source_id | Primary source |

### Relationships

| Field | Meaning |
|---|---|
| relationship_id | Permanent relationship identifier |
| subject_id | Source entity |
| predicate | Relationship type |
| object_id | Target entity |
| evidence_id | Source supporting the relationship |
| status | Confirmed, provisional or unresolved |
| note | Boundary or interpretation note |

Recommended predicates include:

- `covered_by`
- `within_reporting_scheme`
- `operated_by`
- `contains_sector`
- `administered_by`
- `source_component_of`
- `guide_entry_covers`

## Evidence status vocabulary

Use controlled values:

- Confirmed
- Provisional
- Unresolved
- Confirmed absent
- Historical

## Review status vocabulary

Suggested values:

- Candidate recorded
- Identity checked
- Primary source checked
- Association checked
- Batch audited
- Final verified

## Existing workbook

Version 0.3 contains the following sheets:

- Overview
- TSS Candidates
- Stage 4 Findings (one row per researched record; findings use Confirmed present, Confirmed absent or Unresolved)
- VTS Services
- Reporting Schemes
- Relationships
- Sources
- Issues
- Batches
- Definitions
- Audit Findings
- TSS Components
- ID Crosswalk
- Legacy Links

The workbook is the current working register. This dictionary sets the direction for later normalisation.
