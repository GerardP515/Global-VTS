# Global VTS inventory: v0.2 audit

**Date:** 29 September 2026  
**Status:** Reconciled working register. Not a verified worldwide census.

Version 0.2 supersedes both conflicting v0.1 workbooks. The original files remain unchanged.

## What was checked

Both workbooks, both supplied CSV files and the workbook inside the supplied ZIP were compared.
The audit checked counts, exact duplicates, identifiers, relationships, source references and batch allocation.
Selected primary-authority sources were checked for the retained service and reporting identities.
This is not the full 170-record operational or current-baseline audit.

## Reconciled counts

| Measure | Earlier dot-named v0.1 | Later underscore-named v0.1 | Corrected v0.2 |
|---|---:|---:|---:|
| Candidate source rows | 170 | 170 | 170 |
| Named VTS service records | 14 | 8 | 15 |
| Mandatory reporting records | 7 | 7 | 7 |
| Voluntary reporting records | 1 | 0 | 1 |
| TSS identification screening started | 27 | 17 | 28 |
| Fully audited operational records | 0 | 0 | 0 |

Version 0.2 has 10 TSS records with initially evidenced named associations.
Proposed and system-level links remain separate.
The 2 Gdańsk component records are non-additive children, not two extra parent rows.

## Corrections

### Missing records

Six US services were restored: Prince William Sound, Puget Sound, San Francisco, Los Angeles–Long Beach, Houston-Galveston and New York.
USCG describes these services in its detailed location register. [SRC-017]

San Francisco's Offshore Vessel Movement Reporting System was restored as SRS-008.
USCG describes OVMRS as voluntary. It is excluded from the mandatory subtotal. [SRC-017]

### Gdańsk

VTS Zatoka Gdańska was added as VTS-015.
The Polish authority links its VTS area to GDANREP and identifies TSS East and TSS West.
Those components are recorded under parent TSS-0043. [SRC-019]

### REEFVTS

Reef North and Reef South were recorded, with Townsville and Gladstone centres.
MSQ states that either centre can manage either sector.
This remains one named service record, not two new services. [SRC-018]

### Relationship controls

The earlier file proposed 24 component-to-VTS links across Malacca–Singapore.
These assigned each of eight candidate segments to all three authorities without component-boundary evidence.
They remain visible in Legacy Links, but are not active component-to-service assertions.

STRAITREP is recorded separately from its nine sectors and three VTS service identities.
Component allocation still needs research. [SRC-006; SRC-007]

Great Belt and Sound links were strengthened using the named TSS in their IMO reporting-system resolutions.
Current authority pages were used alongside those historical instruments. [SRC-008; SRC-009; SRC-015; SRC-020; SRC-021]

The missing Falsterbo lead was restored.
Three eastern Gulf of Finland GOFREP hypotheses were also restored, but remain explicitly unverified.
The checked Fintraffic text does not substantiate those three named connections. [SRC-011; SRC-012]

### Source controls

MPA source dates were corrected to 6 August 2026.
The AMSA data-policy date was corrected to 21 January 2021.
Current MSQ service information now supports the REEFVTS operating structure.
The GOFREP source was changed to the canonical English Master's Guide.

## Structural results

Both input workbooks have the same 170 candidate labels, in the same order.
No exact duplicate candidate labels or identifiers were found.
Each original CSV matches its corresponding workbook.
The ZIP workbook matches the later standalone workbook byte-for-byte.

The corrected register has no duplicate active relationship pairs or dangling relationship/source identifiers.
Every related service or reporting ID in the candidate table has a corresponding active relationship.
All 170 candidates are allocated once across 34 batches.

These checks do not prove geographical uniqueness, current operation or worldwide completeness.

## Outstanding baseline

The official UKHO index lists the 2026 Annual Notice 17.
Its PDF could not be retrieved during this audit.
The 170 labels have therefore not been reconciled against that primary list. [SRC-001; SRC-002]

IMO's 2025 edition includes measures adopted before September 2025.
Its full contents and later changes remain to be reconciled. [SRC-003]

The 170 figure is a candidate source-row count.
It is not a confirmed count of TSS, operational VTS areas or proposed guide entries.

## Workbook contents

The original register sheets remain, with corrected records and formula-driven dashboard totals.
Audit Findings, TSS Components, ID Crosswalk and Legacy Links document the changes.
Last record check means an editorial check date, not a guarantee of current regulatory coverage.

No record is marked as having completed the full multi-pass operational audit.
The register must not be used for passage planning or VHF reporting instructions.

## Sources cited in this audit


**SRC-001: UKHO-labelled Notice 17: candidate extraction**  
UKHO-labelled text; third-party host | Edition not visible  
https://www.scribd.com/document/1014775753/1-1-IMO-Adopted-Traffic-Separation-Schemes-on-the-ADMIRALTY-Chart-Series

**SRC-002: Annual Summary of Notices to Mariners (NP247)**  
UK Hydrographic Office | 2026 listing  
https://msi.admiralty.co.uk/NoticesToMariners/Annual

**SRC-003: Ships’ Routeing, 2025 Edition**  
International Maritime Organization | 2025 edition  
https://imo-epublications.org/content/books/9789280118353

**SRC-006: Vessel Traffic Information System**  
Maritime and Port Authority of Singapore | Updated 6 August 2026  
https://www.mpa.gov.sg/port-marine-ops/operations/vessel-traffic-information-system

**SRC-007: STRAITREP operational areas**  
Maritime and Port Authority of Singapore | Updated 6 August 2026  
https://www.mpa.gov.sg/port-marine-ops/operations/vessel-traffic-information-system/operational-areas

**SRC-008: BELTREP: Reporting Procedures**  
Danish Defence / Royal Danish Navy | Undated live page  
https://www.forsvaret.dk/da/organisation/soevaernet/civile-opgaver/beltrep/

**SRC-009: About SOUNDREP**  
Swedish Maritime Administration | Updated 26 October 2022  
https://www.sjofartsverket.se/en/services/maritime-traffic-information/soundrep/soundrep-information/about-soundrep/

**SRC-011: GOFREP Area: Master's Guide**  
Fintraffic | Undated live page  
https://mastersguide.fintraffic.fi/en/gofrep-area

**SRC-012: Monitoring international waters**  
Fintraffic | Undated live page  
https://www.fintraffic.fi/sv/node/254

**SRC-015: Vessel Traffic Service**  
Danish Defence / Royal Danish Navy | Updated 29 July 2026  
https://www.forsvaret.dk/da/organisation/soevaernet/nationalt-maritimt-operationscenter/vts/

**SRC-017: Vessel Traffic Services Locations**  
United States Coast Guard Navigation Center | Live page; date not displayed  
https://www.navcen.uscg.gov/vessel-traffic-services-locations

**SRC-018: Great Barrier Reef and Torres Strait VTS (REEFVTS)**  
Maritime Safety Queensland | Live operating-authority page  
https://www.msq.qld.gov.au/shipping/reefvts

**SRC-019: VTS Zatoka Gdańska**  
Maritime Office in Gdynia | Updated 22 October 2024  
https://www.umgdy.gov.pl/en/marine-safety/vts-zatoka-gdanska-en/

**SRC-020: Resolution MSC.332(90): BELTREP amendments**  
International Maritime Organization | Adopted 22 May 2012  
https://wwwcdn.imo.org/localresources/en/KnowledgeCentre/IndexofIMOResolutions/MSCResolutions/MSC.332(90).pdf

**SRC-021: Resolution MSC.314(88): SOUNDREP**  
IMO; hosted by Swedish Maritime Administration | Adopted 29 November 2010  
https://www.sjofartsverket.se/globalassets/tjanster/sjotrafiktjanster/msc.31488.pdf