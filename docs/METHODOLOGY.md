# Research Methodology

## Entity separation

The project treats the following as separate entities:

- Traffic Separation Scheme (TSS)
- Vessel Traffic Service (VTS)
- Vessel reporting scheme (VRS/SRS)
- VTS centre
- VTS sector or zone
- proposed guide entry

A single source heading may represent several entities.

## Relationship model

Relationships are recorded explicitly.

Examples:

- TSS **covered by** VTS
- TSS **within** reporting scheme
- VTS **operated by** centre
- VTS **contains** sector
- reporting scheme **administered by** VTS
- guide entry **covers** one or more operational entities

No relationship should be inferred from geographical proximity alone.

## Evidence statuses

### Confirmed

An authoritative source directly supports the claim.

### Provisional

Credible evidence exists, but primary reconciliation remains outstanding.

### Unresolved

Available evidence does not establish the finding.

### Confirmed absent

Use only where authoritative material is sufficient to establish absence within the defined scope.

A failed search is never enough for “confirmed absent”.

## Source classes

### Primary

- IMO instruments and publications
- national maritime administrations
- coastguards
- operating VTS authorities
- official hydrographic material
- statutory or official reporting instructions

### Supporting

- official port guides
- official pilotage information
- official radio-station information
- other government publications

### Lead only

- old guides
- third-party reproductions
- commercial summaries
- search-result snippets

Lead sources may identify candidates but must not establish current operational status by themselves.

## Counting rules

### TSS count

Count distinct verified TSS, not source headings.

### VTS count

Count distinct VTS areas or services according to the adopted project definition.

Do not count each centre, sector or radio channel as a separate VTS unless the authority defines it as a separate service.

### Reporting-scheme count

Count distinct formal schemes.

Routine reports required within a VTS are not automatically a separate reporting scheme.

### Guide-entry count

This is an editorial count, not a regulatory count.

One guide entry may cover several TSS where they form one coherent operational passage.

A complex VTS may require several guide entries.

## Batch workflow

Research in sequential batches of five.

For each record:

1. Verify identity.
2. Verify current status.
3. Check VTS.
4. Check vessel reporting scheme.
5. Check authority and source date.
6. Record relationships.
7. Record unresolved questions.
8. Run quality checks.

Do not close a batch until the audit is complete.

## Change control

Never overwrite a historical identity.

If an official scheme name changes:

- retain the canonical ID;
- update the current official name;
- retain the previous name;
- record the source and effective date.

If a source record is split into several verified schemes:

- retain the source-row record for traceability;
- create child entity records;
- link them to the source row;
- use the verified child entities for the final scheme count.

## Date control

Each finding should record:

- source date or edition;
- date accessed;
- date last checked;
- implementation date where relevant.

Adoption date and implementation date must not be treated as the same field.

## Operational instructions

The scoping inventory identifies services and relationships.

Detailed bridge instructions such as call points, channels, message content and exemptions require a separate operational review before publication.
