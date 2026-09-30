# Stage 3: VTS rationalisation rules

## Objective

Create the practical list of traffic services that would become candidate entries in a worldwide VTS guide.

Stage 2 answers which TSS are associated with traffic services. Stage 3 changes the unit of analysis from **TSS** to **service**.

## Unit of account

A rationalised guide service is an operational VTS, VTIS, VTMS, traffic-information service or approved monitoring service that has its own operational identity for mariners.

A VTS centre is not automatically a separate guide service. A sector may be a separate guide service where mariners call it by a distinct call sign and use separate procedures.

## Required fields

- existing VTS ID
- rationalised publication-facing name
- primary editorial region
- service type
- authority/jurisdiction
- centre
- service area
- associated TSS
- reporting schemes
- call sign
- channels
- source evidence
- rationalisation action
- publication readiness

## Rationalisation decisions

### KEEP
The existing record already represents a coherent guide service.

### NORMALISE_NAME
The service remains one entry, but the publication-facing name is simplified or aligned with the operational call sign.

### KEEP_AS_SECTOR
The record is formally a sector/service under a larger VTS centre, but remains a separate guide entry because vessels interact with it directly.

### SUPPLEMENTAL
Operationally relevant monitoring or traffic-control service, but not counted as a confirmed core VTS until the project scope says otherwise.

### REVIEW
Evidence confirms a traffic service but its formal VTS identity, title or boundary still needs resolution.

## Region rule

Use the 17 editorial regions in `docs/REGIONS.md`. Region is publication metadata and does not change the canonical VTS ID.

Where a service spans countries or boundaries, assign one primary editorial region and retain the international/joint nature in the authority and area fields.

## Next pass

1. Verify the publication-facing name against current authority material.
2. Resolve REVIEW records.
3. Merge Claude's B20-B29 service findings.
4. Attach all TSS and reporting-scheme relationships to each service.
5. Produce the final deduplicated guide-entry count.
