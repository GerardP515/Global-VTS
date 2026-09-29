# Global VTS

Research repository for assessing the viability, scale and structure of a worldwide guide to Vessel Traffic Services (VTS), Traffic Separation Schemes (TSS) and vessel reporting schemes.

## Project objective

Establish the worldwide TSS baseline, identify associated VTS and reporting systems, reconcile shared operational areas, and estimate the work required for a practical worldwide guide.

The proposed guide should make four actions clear to bridge teams: **who to call, when to call, on which channel, and what information to report**.

## Authoritative baseline

The baseline is now derived directly from IMO *Ships’ Routeing 2025 Edition*.

- **164** indexed Part B parent entries.
- **224** named or explicitly enumerated TSS research entities after source-level decomposition.
- **23** mandatory ship reporting systems in Part I.
- **19** Part B parents contain multiple named or explicitly enumerated TSS entities.
- **1** authoritative TSS candidate was absent from the legacy v0.2 register: B-IV/3 near the deep-water route leading to Jazan Economic City Port.

The 224 figure is a project research-entity count. Internal lane segments and unnamed sub-schemes are not automatically split into separate records.

## Active research scope

The authoritative research sequence is in [research/batches_imo2025](research/batches_imo2025/README.md).

**B01–B10 are active.** Later batches are paused until the first 50 TSS records are researched and audited.

The older `research/batches/` sequence is retained as historical/reconciliation material because work had already been carried out against it.

## Key data

- [Part B parent inventory](data/authoritative/IMO_2025_Part_B_Parent_Inventory.csv)
- [Individual TSS inventory](data/authoritative/IMO_2025_Individual_TSS_Inventory.csv)
- [Mandatory reporting systems](data/authoritative/IMO_2025_Mandatory_Reporting_Systems.csv)
- [Legacy crosswalk](research/reconciliation/TSS_Crosswalk_Legacy_v0_2_to_IMO_2025.csv)
- [Second-pass audit](audits/IMO_2025_Second_Pass_Audit.md)

## Identification model

Version 1.0 freezes the authoritative TSS identifiers as `TSS-0001` onward in IMO 2025 source order. The v0.2 `TSS-xxxx` values are now explicitly **legacy provisional IDs** and are interpreted through the crosswalk.

From v1.0 onward, canonical identifiers are never reused or renumbered.

See [Naming Schema](docs/NAMING_SCHEMA.md).

## Evidence principle

A failed search is not evidence of absence. Operational VTS findings remain confirmed, provisional, unresolved or confirmed absent according to the documented methodology.

Primary evidence should come from IMO, UKHO, national maritime administrations, coastguards, VTS authorities and official hydrographic publications.

## Key documents

- [Project description](PROJECT_DESCRIPTION.md)
- [Research plan](docs/RESEARCH_PLAN.md)
- [Methodology](docs/METHODOLOGY.md)
- [Naming schema](docs/NAMING_SCHEMA.md)
- [Data dictionary](docs/DATA_DICTIONARY.md)
- [Source register](sources/SOURCE_REGISTER.md)

## Versioning

**v1.0 baseline:** authoritative IMO 2025 TSS and mandatory reporting inventories established. Existing VTS-association research remains subject to migration and revalidation against the new canonical IDs.
