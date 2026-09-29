# Stage 2 Prompt: TSS to VTS and Vessel Reporting Association Research

## Purpose

Determine, for each authoritative Traffic Separation Scheme (TSS) in the Global VTS project, whether it has an associated:

1. operational Vessel Traffic Service (VTS);
2. mandatory vessel reporting scheme;
3. both;
4. neither confirmed; or
5. unresolved relationship.

This stage answers the core scoping question:

> Which of the 224 authoritative TSS research entities have an associated operational VTS and/or vessel reporting scheme?

## Authoritative project baseline

Use the repository's IMO 2025 baseline as the TSS source of truth:

- `data/authoritative/IMO_2025_Individual_TSS_Inventory.csv`
- `data/authoritative/IMO_2025_Part_B_Parent_Inventory.csv`
- `data/authoritative/IMO_2025_Mandatory_Reporting_Systems.csv`
- `research/batches_imo2025/`

The TSS list contains 224 named or explicitly enumerated research entities derived from IMO *Ships' Routeing 2025 Edition*.

Do not revert to the legacy 170-row candidate register except for reconciliation or prior-research recovery.

The legacy register is retained at:

- `data/legacy/Global_VTS_TSS_Candidates_v0_2.csv`
- `research/reconciliation/TSS_Crosswalk_Legacy_v0_2_to_IMO_2025.csv`

## Active scope

Research must proceed in sequential five-item batches.

Current active scope:

- B01 to B10
- 50 TSS records
- located in `research/batches_imo2025/`

Do not begin B11 until B01 to B10 are complete unless explicitly instructed.

Complete and audit each five-item batch before closing it.

## Core classification

Assign one primary association status to every TSS:

| Status | Definition |
|---|---|
| VTS + MRS | TSS is supported by evidence as associated with an operational VTS and a mandatory reporting scheme |
| VTS only | TSS is supported by evidence as associated with an operational VTS, with no applicable mandatory reporting scheme established |
| MRS only | TSS is supported by evidence as associated with a mandatory reporting scheme, but an operational VTS relationship is not established |
| Neither confirmed | Authoritative evidence supports neither association within the defined research scope |
| Unresolved | Evidence is incomplete, inaccessible, conflicting or insufficient to classify safely |

"MRS" means mandatory vessel or ship reporting scheme for this project.

Voluntary reporting arrangements must be recorded separately and must not be counted as mandatory reporting schemes.

## Entity separation rule

Treat the following as distinct entities:

- TSS
- VTS area or service
- VTS centre
- VTS sector or zone
- mandatory ship reporting scheme
- voluntary reporting scheme
- reporting point
- radio channel

Do not treat a VTS centre, radio station or reporting point as a VTS area.

Do not assume that a reporting scheme is a VTS.

Do not assume that a VTS operating or monitoring a reporting scheme means that every part of the reporting area is inside a VTS area.

## Association standard

A positive TSS-to-VTS or TSS-to-reporting relationship requires evidence.

Acceptable evidence includes:

1. an official source explicitly naming the TSS;
2. an official chart, map or boundary description showing the TSS inside the operational area;
3. an official service description whose defined boundaries demonstrably include the TSS;
4. an IMO routeing or reporting instrument explicitly linking the scheme and reporting system.

Geographical proximity alone is not enough.

A named VTS in the same port or coastal area is not enough.

A search result snippet is not enough.

If the evidence does not establish the relationship, classify it as unresolved.

## Evidence hierarchy

Use sources in this order where available.

### Tier 1 - primary international and statutory sources

- IMO *Ships' Routeing*
- IMO resolutions and circulars
- SOLAS-related adopted reporting instruments
- national legislation or statutory notices

### Tier 2 - primary operational authorities

- national maritime administrations
- coastguards
- hydrographic offices
- VTS operating authorities
- port authorities operating the VTS
- official waterway authorities

### Tier 3 - official navigational publications

- current Notices to Mariners
- official sailing directions
- ADMIRALTY List of Radio Signals Volume 6
- national radio signal publications
- ITU MARS / List IV where relevant

### Tier 4 - supporting sources

- official pilotage guides
- official port handbooks
- government publications
- authority-issued user guides

### Lead-only sources

The following may identify a lead but must not establish current operational status alone:

- commercial port guides
- old guidebooks
- third-party summaries
- unofficial chart reproductions
- search-result snippets
- forums
- blogs

## Currency rule

The research concerns current operational arrangements.

For every positive or negative finding:

- record the source publication date where available;
- record the date accessed;
- check whether the source has been superseded;
- distinguish adoption date from implementation date;
- identify temporary suspension or amended boundaries where relevant.

An historical association is not evidence of current operation.

## Research workflow for each TSS

### Step 1 - confirm identity

Read the TSS record from the authoritative inventory.

Record:

- canonical TSS ID;
- official TSS name;
- IMO parent reference;
- IMO parent title;
- IMO source page;
- relevant State or States;
- project region.

Do not rename the TSS based on a local source without recording the IMO name separately.

### Step 2 - check mandatory reporting

Check the IMO 2025 mandatory reporting inventory first.

Then check the relevant Part I scheme description and current authority material.

Determine:

- whether the TSS is inside or explicitly linked to a mandatory reporting scheme;
- reporting scheme name;
- project VRS ID;
- responsible authority or authorities;
- participation threshold;
- geographical relationship;
- evidence source.

Record voluntary reporting separately.

### Step 3 - check VTS

Search current authoritative sources for an operational VTS covering the TSS.

Determine:

- official VTS name;
- whether the service is operational;
- defined VTS area;
- operating authority;
- VTS centre or centres;
- sector or sectors;
- service type if stated;
- geographical relationship to the TSS;
- evidence source.

Do not infer VTS coverage from a reporting-system boundary unless the official source states or shows VTS coverage.

### Step 4 - reconcile overlaps

Check whether:

- one VTS covers several TSS;
- one TSS crosses several VTS sectors;
- several centres operate one VTS;
- one mandatory reporting scheme covers several TSS;
- a VTS and reporting scheme have different boundaries.

Record one operational entity once, then link multiple TSS to it.

Do not create duplicate VTS records merely because several TSS use the same service.

### Step 5 - classify

Assign:

- VTS + MRS
- VTS only
- MRS only
- Neither confirmed
- Unresolved

Add a short evidence-based reason.

### Step 6 - record uncertainty

Use "Unresolved" where:

- current authoritative documentation cannot be located;
- service boundaries are unclear;
- sources conflict;
- only historical evidence is available;
- a nearby VTS exists but coverage of the TSS is not established;
- reporting-system and VTS boundaries cannot be separated reliably.

Never convert an unsuccessful search into "Neither confirmed" without sufficient evidence.

## Required master association register

Create and maintain:

`data/current/TSS_VTS_MRS_Association_Register.csv`

Minimum fields:

| Field | Requirement |
|---|---|
| tss_id | Canonical TSS ID |
| tss_name | IMO 2025 TSS name |
| imo_parent_ref | IMO Part B reference |
| region_code | Project region |
| coastal_state_s | Relevant State or States |
| association_status | VTS + MRS / VTS only / MRS only / Neither confirmed / Unresolved |
| vts_id | Canonical VTS ID where applicable |
| vts_name | Official VTS name |
| vts_authority | Operating authority |
| vts_centre | Centre or centres |
| vts_sector | Sector or sectors where relevant |
| vts_boundary_basis | How coverage of the TSS was established |
| vts_source_id | Source ID |
| vts_source_url | Official URL |
| mandatory_reporting | Yes / No / Unresolved |
| vrs_id | Canonical reporting-scheme ID |
| reporting_scheme_name | Official scheme name |
| reporting_authority | Responsible authority |
| reporting_boundary_basis | How association was established |
| reporting_source_id | Source ID |
| reporting_source_url | Official URL |
| voluntary_reporting | Yes / No / Unresolved |
| evidence_summary | Concise factual explanation |
| source_date | Publication or update date |
| accessed_date | Date checked |
| review_status | Research / audited / reopened |
| unresolved_issue | Outstanding issue if any |

Add fields where needed, but do not remove the core evidence fields.

## Canonical IDs

Reuse existing VTS and VRS records where the entity already exists.

If a new operational entity is confirmed:

- allocate the next unused `VTS-NNNN` ID;
- allocate the next unused `VRS-NNNN` ID for reporting schemes;
- allocate centre or sector IDs only where needed.

Never assign a second ID to an existing entity.

Check the current register and crosswalk before allocating a new ID.

## Source register

Every new authoritative source must be added to the project source register or source dataset.

Record:

- source ID;
- authority;
- document/page title;
- date or edition;
- URL;
- access date;
- source class;
- what claim it supports.

Do not cite a home page where a specific operational notice or procedure is available.

## Batch procedure

For each five-TSS batch:

### Pass 1 - primary research

Research all five records separately.

Do not use one TSS finding as evidence for the next without checking the source coverage.

### Pass 2 - evidence audit

For all five:

- reopen the supporting sources;
- verify each positive association;
- check that the source is current;
- confirm that quoted or paraphrased boundaries support the relationship;
- remove unsupported associations.

### Pass 3 - classification and duplicate audit

Check:

- VTS versus reporting-system distinction;
- centre versus VTS distinction;
- shared VTS duplication;
- shared reporting-scheme duplication;
- parent-routeing-system versus individual TSS confusion;
- mandatory versus voluntary reporting.

### Pass 4 - final batch audit

Before closing the batch, confirm:

- all five TSS have a classification;
- every positive relationship has evidence;
- every unresolved case states what remains unknown;
- new source records are saved;
- new entity IDs are unique;
- master association register is updated;
- batch Markdown file is updated;
- no later batch was modified accidentally.

## Batch Markdown update

Update the relevant file under:

`research/batches_imo2025/Bxx.md`

For each TSS, record:

- final association status;
- VTS name and ID if applicable;
- mandatory reporting scheme and ID if applicable;
- evidence source IDs;
- unresolved issue if any.

Mark checklist items only when actually completed.

Do not mark a batch closed until the final audit passes.

## GitHub save rule

After each audited batch:

1. update the master association register;
2. update the relevant batch Markdown file;
3. update source records;
4. add any new VTS/VRS entity records;
5. save a short batch audit under `audits/stage2/`;
6. commit the completed batch to the repository.

Suggested commit message:

`Stage 2 B01: verify TSS VTS and reporting associations`

Do not combine several unaudited batches into one commit.

## Audit report format

Create:

`audits/stage2/Bxx_Association_Audit.md`

Include:

### Batch
Bxx

### TSS reviewed
List the five canonical IDs and names.

### Results
Table:

| TSS | VTS | Mandatory reporting | Classification |
|---|---|---|---|

### Evidence check
State whether each relationship was rechecked.

### Duplicate check
Identify shared VTS or reporting entities.

### Changes made
List additions, corrections and removals.

### Unresolved issues
List any remaining questions.

### Audit result
Use only:

- PASS
- PASS WITH UNRESOLVED ITEMS
- FAIL - RESEARCH REQUIRED

A batch with unsupported positive associations cannot pass.

## Research constraints

Do not:

- infer a VTS relationship from proximity;
- treat a VHF reporting point as a VTS;
- count a VTS centre as a separate VTS unless the authority defines a separate service;
- assume all IMO mandatory reporting schemes are VTS;
- assume all VTS participation is mandatory;
- use an historical source as proof of current operation;
- hide conflicting evidence;
- silently correct the IMO TSS baseline;
- renumber canonical TSS IDs;
- overwrite legacy research without preserving traceability.

## Deliverable after B01-B10

After the first ten authoritative batches are complete, produce an interim Stage 2 report showing:

- TSS researched: 50;
- VTS + MRS count;
- VTS-only count;
- MRS-only count;
- neither-confirmed count;
- unresolved count;
- number of distinct VTS areas identified;
- number of distinct mandatory reporting schemes identified;
- number of shared VTS relationships;
- principal source gaps;
- any changes required to the research method.

Do not extrapolate the 50-record results to a worldwide total unless explicitly requested.

## Completion criterion for Stage 2

Stage 2 is complete only when all 224 authoritative TSS records have:

1. been researched;
2. received a defensible association classification;
3. passed evidence and duplicate review;
4. been linked to canonical operational entities where applicable; and
5. been saved in the master association register with source evidence.
