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
- 125 of them (batches B10 to B34) researched in a first Stage 4 pass;
- 57 VTS/service records, of which 16 are research leads and not counted;
- 21 mandatory and 6 voluntary vessel reporting schemes.

For B10 to B34: VTS confirmed present for 40 rows, mandatory reporting confirmed for 31, and unresolved for the rest.
No confirmed-absence findings have been made. Some source rows contain grouped or duplicate schemes, so these are not scheme or guide-entry totals.
See the [v0.3 Stage 4 audit](audits/Global_VTS_Inventory_v0_3_Stage4_Audit.md).

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
│   └── archive/ (v0_1, v0_2)
├── research/stage4/
├── tools/
├── tasks/
├── audits/
├── sources/
│   └── SOURCE_REGISTER.md
└── releases/
    └── archive/
```

## Current datasets

The working dataset is held in:

- `data/current/Global_VTS_Inventory_v0_3.xlsx` (includes the Stage 4 Findings sheet)
- `data/current/Global_VTS_TSS_Candidates_v0_3.csv`
- `research/stage4/stage4_findings_v0_3.csv` (one row per researched record)
- `audits/Global_VTS_Inventory_v0_3_Stage4_Audit.md`

Raw research output is in `research/stage4/raw/`, merge adjustments in `research/stage4/merge_log.md`,
and the merge script in `tools/merge_stage4.py`.

Earlier outputs are retained under `data/archive/v0_1/`, `data/archive/v0_2/` and `releases/archive/`.

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

The current working release is **v0.3**. Historical files are retained to preserve the audit trail.

No dataset should be described as a verified worldwide total until the baseline has been reconciled against current official routeing and VTS sources.
