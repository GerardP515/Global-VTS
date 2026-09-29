# Global VTS

Research repository for assessing the viability, scale and structure of a worldwide guide to Vessel Traffic Services (VTS), Traffic Separation Schemes (TSS) and vessel reporting schemes.

## Project objective

Establish:

1. the worldwide inventory of recognised Traffic Separation Schemes;
2. which schemes are associated with an operational VTS and/or vessel reporting scheme;
3. the number of distinct operational areas and proposed guide entries requiring research and production; and
4. the likely research, editorial, charting and maintenance workload.

The proposed guide is intended to make bridge-team reporting actions clear: **who to call, when to call, on which channel, and what information to report**.

## Repository status

This repository is at the scoping and inventory stage. Current totals are working-register counts, not final worldwide totals.

The current inventory contains:

- 170 candidate TSS source rows;
- 15 initial VTS/service records;
- 7 mandatory vessel reporting schemes;
- 1 voluntary vessel reporting scheme.

Some source rows contain grouped schemes. TSS-to-VTS relationships remain subject to authoritative verification.

## Structure

```
Global-VTS/
├── README.md
├── PROJECT_DESCRIPTION.md
├── docs/
│   ├── RESEARCH_PLAN.md
│   ├── METHODOLOGY.md
│   ├── NAMING_SCHEMA.md
│   └── DATA_DICTIONARY.md
├── data/
│   ├── current/
│   └── archive/v0_1/
├── audits/
├── sources/
│   └── SOURCE_REGISTER.md
└── releases/
    └── archive/
```

## Current datasets

The working dataset is held in:

- `data/current/Global_VTS_Inventory_v0_2.xlsx`
- `data/current/Global_VTS_TSS_Candidates_v0_2.csv`
- `audits/Global_VTS_Inventory_v0_2_Audit.md`

Earlier v0.1 outputs are retained under `data/archive/v0_1/` and `releases/archive/`.

## Identification model

Each entity should retain a permanent canonical identifier independent of its name or region.

Examples:

- `TSS-0001`
- `VTS-0001`
- `VRS-0001`
- `CTR-0001`

A separate regional reference may be generated for human use, for example `TSS-BAL-014`. Regional codes are organisational metadata and must not replace the permanent identifier.

See [Naming Schema](docs/NAMING_SCHEMA.md).

## Evidence principle

A failed search is not evidence of absence. Entries remain **unresolved** until supported by authoritative evidence.

Primary evidence should come from IMO, UKHO, national maritime administrations, coastguards, VTS authorities and official hydrographic publications.

## Key documents

- [Project description](PROJECT_DESCRIPTION.md)
- [Research plan](docs/RESEARCH_PLAN.md)
- [Methodology](docs/METHODOLOGY.md)
- [Naming schema](docs/NAMING_SCHEMA.md)
- [Data dictionary](docs/DATA_DICTIONARY.md)
- [Source register](sources/SOURCE_REGISTER.md)

## Versioning

The current working release is **v0.2**. Historical files are retained to preserve the audit trail.

No dataset should be described as a verified worldwide total until the baseline has been reconciled against current official routeing and VTS sources.
