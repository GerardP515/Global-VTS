# FC-A Europe / Mediterranean recheck

**Date:** 1 October 2026  
**Branch:** `review/fc-a-europe-med-20261001`  
**Scope:** 25 TSS records, reviewed as five sequential groups of five.  
**Baseline for count impact:** 53 service identities.  
**Method:** apply the current Stage 2 project decisions, including Decisions 1, 4, 5, 6 and 7.

This file is the definitive FC-A reporting table for the 1 October recheck. It supersedes the summary table in `FC-A_VTS_Count_Audit.md`, while preserving that file as audit history.

## Result

| TSS | TSS name | Region | Result | Coverage | Service | Count impact |
|---|---|---|---|---|---|---:|
| TSS-0052 | North Hinder North | BIS | Existing service | Partial | Rotterdam VTS, Sector Maas Approach (VTS-0024) | 0 |
| TSS-0056 | IJmuiden North | NSC | Existing service | Partial | VTS North Sea Canal Area, Sector IJmuiden (VTS-0025) | 0 |
| TSS-0057 | IJmuiden West Outer | NSC | Existing service | Partial | VTS North Sea Canal Area / extended IJ-geul (VTS-0025) | 0 |
| TSS-0058 | Off Texel | NSC | Existing service | Partial | VTS Off Texel (VTS-0044) | 0 |
| TSS-0059 | Off Vlieland | NSC | Existing service | Partial | VTS Off Texel (VTS-0044) | 0 |
| TSS-0060 | Vlieland North | NSC | Existing service | Partial | VTS Off Texel (VTS-0044) | 0 |
| TSS-0088 | Off Skerries | BIS | No TSS-linked service | — | — | 0 |
| TSS-0089 | In Liverpool Bay | BIS | New service | Partial | Liverpool VTS / Mersey VTS (VTS-0216) | +1 |
| TSS-0092 | North-west of Garðskagi Point | NOI | New service | Monitoring | Icelandic Coast Guard Maritime Traffic Service (VTS-0212) | +1 |
| TSS-0093 | South-west of the Reykjanes Peninsula | NOI | New service | Monitoring | Icelandic Coast Guard Maritime Traffic Service (VTS-0212) | 0 |
| TSS-0097 | At Banco del Hoyo | FIC | Unresolved | — | — | unresolved |
| TSS-0100 | Off Cape Palos | MED | New service | Monitoring | Salvamento Marítimo CCS Cartagena traffic service (VTS-0218) | +1 |
| TSS-0101 | Off Cape La Nao | MED | New service | Monitoring | Salvamento Marítimo CCS Valencia traffic monitoring service (VTS-0229) | +1 |
| TSS-0102 | In the Corsica Channel | MED | New service | Partial | CROSS Méditerranée / Cap Corse and Sagro sémaphores (VTS-0213) | +1 |
| TSS-0103 | Off Cani Island | MED | Unresolved | — | — | unresolved |
| TSS-0104 | Off Cape Bon | MED | Unresolved | — | — | unresolved |
| TSS-0111 | Saronicos Gulf, approaches to Piraeus | MED | New service | Partial | VTS Piraeus (VTS-0221) | +1 |
| TSS-0112 | Approaches to Thessaloniki | MED | No TSS-linked service | — | — | 0 |
| TSS-0113 | Western approach to Mina Dumyat | MED | Unresolved | — | Damietta Port Authority VTS candidate | unresolved |
| TSS-0114 | Eastern approaches to Mina Dumyat | MED | Unresolved | — | Damietta Port Authority VTS candidate | unresolved |
| TSS-0115 | Western approaches to Bur Said | MED | New service | Partial | Suez Canal SC-VTMS, Port Said approaches (VTS-0222) | +1 |
| TSS-0116 | Eastern approach to Bur Said | MED | New service | Partial | Suez Canal SC-VTMS, Port Said approaches (VTS-0222) | 0 |
| TSS-0117 | Southern approaches to the Kerch Strait | MED | New service | Partial | Kerch Strait VTS / Kavkaz-Traffic (VTS-0210) | +1 |
| TSS-0118 | South-western coast of Crimea | MED | New service | Partial | Sevastopol VTS (VTS-0223) | +1 |
| TSS-0119 | Approaches to Chornomorsk, Odesa and Pivdennyi | MED | New service | Partial | Delta-Lotsman VTS, north-western Black Sea (VTS-0211) | +1 |

**Coverage normalisation:** detailed register values such as “Boundary only” and “near-whole, exact edge unresolved” are reported as **Partial** here. This keeps the deliverable to Full / Partial / Monitoring.

## Count audit

- Existing-service rows: **6**.
- New-service rows: **12**.
- No TSS-linked service rows: **2**.
- Unresolved rows: **5**.
- Distinct new service identities: **10**.
- New core identities: **7**.
- New supplemental monitoring/information identities: **3**.
- FC-A count impact: **+10**.
- FC-A isolated running count from the 53-service baseline: **63 service identities**.

Two new services cover two FC-A records each and are counted once:

- VTS-0212: TSS-0092 and TSS-0093.
- VTS-0222: TSS-0115 and TSS-0116.

## Group self-audit

| Group | Records | Result |
|---|---|---|
| 1 | TSS-0052, 0056, 0057, 0058, 0059 | PASS |
| 2 | TSS-0060, 0088, 0089, 0092, 0093 | PASS |
| 3 | TSS-0097, 0100, 0101, 0102, 0103 | PASS after TSS-0101 correction |
| 4 | TSS-0104, 0111, 0112, 0113, 0114 | PASS WITH UNRESOLVED ITEMS |
| 5 | TSS-0115, 0116, 0117, 0118, 0119 | PASS |

All 25 requested records appear once. Service identities were checked for duplicate counting.

## Material recheck findings

### TSS-0101 Cabo de la Nao

**Changed to New service / Monitoring.**

SRC-2296 is a current SASEMAR statement dated 9 April 2026. It explicitly assigns control of the Cabo de la Nao TSS to CCS Valencia.

This is stronger than the earlier negative inference from 2025 general SASEMAR summaries. Those summaries omitted La Nao but did not expressly exclude it.

No formal VTS polygon was found. The service is therefore recorded as supplemental monitoring/information, VTS-0229.

### TSS-0111 Piraeus

The live Hellenic Coast Guard VTS page was reopened successfully on 1 October 2026 and upgraded to SRC-2041 Tier 2.

It confirms VTS Piraeus is operational on VHF 13, 14 and 15. The page does not publish its service-area boundary.

The Decision 7 inclusion therefore remains **New service / Partial**.

### TSS-0113 and TSS-0114 Damietta

SRC-2297 and SRC-2298 provide current Egyptian authority evidence.

They confirm Damietta Port is operational, with port communications and 24-hour operations. They do not identify an operating VTS or define a VTS area.

Both records therefore remain **Unresolved**. The 2025 VTS tender cannot establish current service entry into operation.

### TSS-0115 and TSS-0116 Port Said

SRC-2236 confirms SC-VTMS surveillance of the Canal and Port Said approaches from 15 miles out.

SRC-2237 ties the 15-mile arrival call to the Port Said Fairway Buoy. SRC-2238 provides 2026 operational corroboration.

The existing Decision 7 outcome remains **New service / Partial**, counted once as VTS-0222.

## Disputed-jurisdiction records

TSS-0117 and TSS-0118 remain counted under project Decision 6.

The register records the relevant Russian Federation service claims without taking a position on jurisdiction. This does not change the geometry findings.

## Files changed by this recheck

- `sources/SOURCE_REGISTER.md`
- `data/current/Final_VTS_Count_Fact_Check.csv`
- `data/current/Final_VTS_Count_New_Services.csv`
- `data/current/VTS_Entity_Register.csv`
- `data/current/TSS_VTS_MRS_Association_Register.csv`
- `data/current/Guide_Service_Candidates.csv`
- `data/current/Research_Gaps.csv`
- `audits/stage3/final_count/FC-A_Recheck_20261001.md`
