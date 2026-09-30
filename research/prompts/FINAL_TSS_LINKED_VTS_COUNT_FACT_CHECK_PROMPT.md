# Final VTS Count Fact-Check Prompt

## Purpose

Produce a **defensible final count of TSS-linked operational traffic services** for the Global VTS project.

The authoritative baseline is the project's **224 IMO 2025 TSS research entities**. Stage 2 has already classified 155 records positively or negatively and left **69 TSS with an unresolved VTS association**.

This prompt is **not** a worldwide port-VTS census.

Standalone port VTS with no demonstrated relationship to one of the 224 TSS are **out of scope**.

The task is to resolve the 69 remaining TSS, identify any additional TSS-linked VTS/VTIS/VTMS/operational monitoring services, reconcile them against the existing service register, and calculate the final rationalised count.

---

## Authoritative repository inputs

Use the current `main` branch.

Primary project files:

- `data/authoritative/IMO_2025_Individual_TSS_Inventory.csv`
- `data/current/TSS_VTS_MRS_Association_Register.csv`
- `data/current/VTS_Entity_Register.csv`
- `data/current/TSS_Service_Relationships.csv`
- `data/current/Research_Gaps.csv`
- `docs/REGIONS.md`
- `sources/SOURCE_REGISTER.md`
- `audits/stage2/`

Do not renumber canonical TSS IDs.

Do not replace the 224-TSS baseline.

Do not undo previous audited positive associations unless new authoritative evidence directly contradicts them.

---

## Counting objective

At the end, report three counts separately:

1. **Core TSS-linked VTS count**  
   Distinct operational VTS / VTIS / VTMS / operational VTS sectors that have a demonstrated relationship with at least one authoritative TSS.

2. **Supplemental traffic-service count**  
   Monitoring/information services or traffic-control services associated with a TSS but not confirmed as a formal VTS/VTIS/VTMS.

3. **Total guide-service candidates**  
   Core + supplemental services that would plausibly require a practical mariner-facing guide entry.

Do not combine these three numbers into one ambiguous total.

### Counting unit

Count the **operational service a bridge team actually interacts with**.

- One VTS covering several TSS = one service.
- One centre operating several named sectors = count sectors separately **only where vessels use distinct operational call signs/procedures and the sector would require its own guide treatment**.
- Several centres jointly operating one coherent VTS = one service.
- A reporting system is not a VTS.
- A VTS centre is not automatically a separate VTS.
- A port VTS is out of scope unless the evidence shows that its service area covers or controls one of the 224 TSS.
- Reuse an existing VTS ID whenever the service already exists in `VTS_Entity_Register.csv`.

---

## Current unresolved list: 69 TSS

### BIS — British Isles and southern North Sea (3)

| TSS ID | TSS |
|---|---|
| TSS-0052 | North Hinder North |
| TSS-0088 | Off Skerries |
| TSS-0089 | In Liverpool Bay |

### NSC — North Sea continental coast (5)

| TSS ID | TSS |
|---|---|
| TSS-0056 | IJmuiden North |
| TSS-0057 | IJmuiden West Outer |
| TSS-0058 | Off Texel |
| TSS-0059 | Off Vlieland |
| TSS-0060 | Vlieland North |

### NOI — Norway and Iceland (2)

| TSS ID | TSS |
|---|---|
| TSS-0092 | North-west of Garðskagi Point |
| TSS-0093 | South-west of the Reykjanes Peninsula |

### FIC — France, Iberia and Canary Islands (1)

| TSS ID | TSS |
|---|---|
| TSS-0097 | At Banco del Hoyo |

### MED — Mediterranean and Black Seas (14)

| TSS ID | TSS |
|---|---|
| TSS-0100 | Off Cape Palos |
| TSS-0101 | Off Cape La Nao |
| TSS-0102 | In the Corsica Channel |
| TSS-0103 | Off Cani Island |
| TSS-0104 | Off Cape Bon |
| TSS-0111 | Saronicos Gulf (in the approaches to Piraeus Harbour) |
| TSS-0112 | In the approaches to the port of Thessaloniki |
| TSS-0113 | Western approach to Mina Dumyat |
| TSS-0114 | Eastern approaches to Mina Dumyat |
| TSS-0115 | Western approaches to Bur Said |
| TSS-0116 | Eastern approach to Bur Said |
| TSS-0117 | In the southern approaches to the Kerch Strait |
| TSS-0118 | In the area off the south-western coast of the Crimea |
| TSS-0119 | Approaches to the Chornomorsk, Odesa and Pivdennyi ports |

### RSA — Red Sea and Arabian region (14)

| TSS ID | TSS |
|---|---|
| TSS-0126 | In the entrance to the Gulf of Aqaba |
| TSS-0127 | Near the deep-water route leading to Jazan Economic City Port |
| TSS-0128 | In the southern Red Sea – west and south of Hanish al Kubra |
| TSS-0129 | In the southern Red Sea – east of Jabal Zuqar Island |
| TSS-0130 | In the Strait of Bab el Mandeb |
| TSS-0131 | Off Ras al Hadd |
| TSS-0132 | Off Ra’s al Kuh |
| TSS-0133 | In the Strait of Hormuz |
| TSS-0134 | Tunb–Farur |
| TSS-0137 | Marjan/Zuluf |
| TSS-0138 | Approaches to the port of Ra’s al Khafji |
| TSS-0139 | Off Mina Al-Ahmadi – North scheme I |
| TSS-0140 | Off Mina Al-Ahmadi – North scheme II |
| TSS-0141 | Off Mina Al-Ahmadi – South scheme |

### IOS — Indian Ocean and South Asia (1)

| TSS ID | TSS |
|---|---|
| TSS-0142 | Off Dondra Head |

### SAF — Southern Africa (2)

| TSS ID | TSS |
|---|---|
| TSS-0143 | Off Alphard Banks 34 miles south of Cape Infanta |
| TSS-0144 | Off the FA platform 47 miles south of Mossel Bay |

### CSC — China Sea and China (1)

| TSS ID | TSS |
|---|---|
| TSS-0157 | In the Dangan Channel |

### NPC — North America Pacific coast (2)

| TSS ID | TSS |
|---|---|
| TSS-0173 | In the Santa Barbara Channel |
| TSS-0175 | In the approaches to Salina Cruz |

### CAP — Central and South America Pacific coast (11)

| TSS ID | TSS |
|---|---|
| TSS-0176 | Gulf of Panama |
| TSS-0177 | Morro de Puercos |
| TSS-0178 | Isla Jicarita |
| TSS-0179 | Landfall and approaches to Talara Bay |
| TSS-0180 | Landfall and approaches to Paita Bay |
| TSS-0181 | Landfall off Puerto Salaverry |
| TSS-0182 | Landfall and approaches to Ferrol Bay (Puerto Chimbote) |
| TSS-0183 | Approaches to Puerto Callao |
| TSS-0184 | In the approaches to Puerto Pisco |
| TSS-0185 | Landfall and approaches to San Nicolas Bay |
| TSS-0186 | Landfall and approaches to Puerto Ilo |

### CGP — Caribbean, Gulf of Mexico and Panama (8)

| TSS ID | TSS |
|---|---|
| TSS-0206 | Off Cabo San Antonio |
| TSS-0207 | Off La Tabla |
| TSS-0208 | Off Costa de Matanzas |
| TSS-0209 | In the Old Bahama Channel |
| TSS-0210 | Off Punta Maternillos |
| TSS-0211 | Off Punta Lucrecia |
| TSS-0212 | Off Cabo Maysi |
| TSS-0213 | At the approaches to Puerto Cristobal |

### NWP — North-west Pacific (5)

| TSS ID | TSS |
|---|---|
| TSS-0214 | In the fourth Kuril Strait |
| TSS-0215 | In the Proliv Bussol |
| TSS-0216 | Off the Aniwa Cape |
| TSS-0217 | In the approaches to the Gulf of Nakhodka |
| TSS-0218 | Off the Ostrovnoi Point |

---

## Sequential five-record work plan

Research these **sequentially**. Complete the evidence audit for one batch before starting the next.

| Fact-check batch | TSS IDs |
|---|---|
| FC01 | TSS-0052, TSS-0056, TSS-0057, TSS-0058, TSS-0059 |
| FC02 | TSS-0060, TSS-0088, TSS-0089, TSS-0092, TSS-0093 |
| FC03 | TSS-0097, TSS-0100, TSS-0101, TSS-0102, TSS-0103 |
| FC04 | TSS-0104, TSS-0111, TSS-0112, TSS-0113, TSS-0114 |
| FC05 | TSS-0115, TSS-0116, TSS-0117, TSS-0118, TSS-0119 |
| FC06 | TSS-0126, TSS-0127, TSS-0128, TSS-0129, TSS-0130 |
| FC07 | TSS-0131, TSS-0132, TSS-0133, TSS-0134, TSS-0137 |
| FC08 | TSS-0138, TSS-0139, TSS-0140, TSS-0141, TSS-0142 |
| FC09 | TSS-0143, TSS-0144, TSS-0157, TSS-0173, TSS-0175 |
| FC10 | TSS-0176, TSS-0177, TSS-0178, TSS-0179, TSS-0180 |
| FC11 | TSS-0181, TSS-0182, TSS-0183, TSS-0184, TSS-0185 |
| FC12 | TSS-0186, TSS-0206, TSS-0207, TSS-0208, TSS-0209 |
| FC13 | TSS-0210, TSS-0211, TSS-0212, TSS-0213, TSS-0214 |
| FC14 | TSS-0215, TSS-0216, TSS-0217, TSS-0218 |

---

## Question to answer for every TSS

For each record establish one of the following:

1. **EXISTING SERVICE CONFIRMED**  
   A current service already in `VTS_Entity_Register.csv` covers, controls or monitors the TSS.

2. **NEW SERVICE CONFIRMED**  
   A current TSS-linked service exists but is not in the current VTS register.

3. **NO TSS-LINKED SERVICE CONFIRMED**  
   Current authoritative evidence supports the absence of a qualifying service within the defined scope.

4. **UNRESOLVED**  
   Evidence remains insufficient, inaccessible or conflicting.

Do not convert an unsuccessful search into a negative finding.

---

## Positive-association standard

A TSS-to-service relationship is positive only where one or more current authoritative sources provide:

- an explicit statement naming the TSS;
- a VTS/VTIS/VTMS boundary demonstrably containing all or part of the TSS;
- an official chart or map demonstrating overlap;
- a named monitoring responsibility for the TSS;
- an operational procedure whose geographical extent demonstrably covers it.

Proximity is not evidence.

A nearby port VTS is not relevant unless its service boundary reaches the TSS.

A radio-reporting point alone is not a VTS.

A port pre-arrival report alone is not a VTS.

---

## Negative-association standard

Use **NO TSS-LINKED SERVICE CONFIRMED** only when supported by evidence such as:

- an official complete national/service-area list that excludes the TSS;
- official VTS polygons/boundaries demonstrating that all plausible nearby services exclude the TSS;
- an authority source expressly stating the relevant service scope;
- authoritative navigational publications showing no service while identifying the applicable services for that coast.

If a national authority is inaccessible and only third-party absence evidence exists, leave the record **UNRESOLVED**.

---

## Source hierarchy

### Tier 1
- national legislation and statutory instruments;
- official VTS designation orders;
- IMO instruments;
- current national hydrographic Notices to Mariners.

### Tier 2
- maritime administrations;
- coastguards;
- VTS operating authorities;
- national port/maritime authorities where they operate the relevant VTS;
- official service manuals and VHF procedures.

### Tier 3
- national sailing directions;
- official radio-signal publications;
- ADMIRALTY List of Radio Signals Vol. 6 where accessible;
- official port guides.

### Lead only
- NGA publications;
- commercial port guides;
- agent guides;
- blogs;
- search snippets;
- AIS websites;
- Wikipedia.

Lead-only material may identify a candidate but may not close the finding by itself.

---

## Current-status rule

This is a **current operational** count.

Prefer 2025-2026 material where available.

Where only older statutory material exists:

- confirm it is still in force;
- check for replacement or amendment;
- distinguish historical operation from current operation.

For conflict-affected areas, report current claims and operational evidence neutrally. Do not treat disputed jurisdiction as settled.

---

## Existing-service reconciliation

Before creating a new service:

1. search `data/current/VTS_Entity_Register.csv`;
2. search aliases, centre names and call signs;
3. check whether it is a sector of an existing service;
4. check whether one existing service already covers several TSS;
5. reuse the canonical ID if it is the same operational service.

A new VTS ID is justified only when the operational identity is genuinely new.

---

## Required output for each TSS

Record:

| Field | Requirement |
|---|---|
| tss_id | Canonical ID |
| tss_name | IMO name |
| region_code | Project region |
| coastal_state_s | State(s) |
| final_vts_result | EXISTING SERVICE CONFIRMED / NEW SERVICE CONFIRMED / NO TSS-LINKED SERVICE CONFIRMED / UNRESOLVED |
| vts_id | Existing or newly allocated canonical ID |
| official_service_name | Current authority name |
| operational_call_name | Call sign/service name used by ships |
| service_type | VTS / VTIS / VTMS / operational VTS sector / monitoring-information / traffic-control |
| authority | Operating authority |
| centre | VTS/traffic centre |
| coverage | Full / Partial / Monitoring / Boundary only / Not applicable |
| association_basis | Exact evidence linking service and TSS |
| source_ids | Project source IDs |
| source_urls | Official URLs |
| source_date | Publication/update date |
| accessed_date | Date checked |
| count_impact | +1 new service / 0 existing service / 0 no service / unresolved |
| rationalisation_note | Merge/sector/alias issue |
| unresolved_issue | Remaining question if any |

---

## Count-impact rule

For every positive result explicitly state whether it changes the current service count.

### +1 new service
Use only when:
- the service is current;
- the TSS association is supported;
- it is not already represented by an existing VTS ID;
- it is not merely an alias for an existing service.

### 0 existing service
Use when a newly confirmed TSS maps to an existing canonical service.

### 0 no service
Use for a defensible negative result.

### unresolved
Use where a count-changing possibility remains open.

---

## Batch audit

After every five records:

### Pass 1 — primary research
Research all five independently.

### Pass 2 — source reopening
Reopen every source used for a positive or negative finding.

### Pass 3 — boundary audit
Where geography determines the result:
- compare TSS coordinates with service boundaries;
- distinguish full from partial overlap;
- record datum issues;
- do not infer whole-area coverage from a shared name.

### Pass 4 — identity audit
Check:
- service already exists under another name;
- centre versus service;
- sector versus VTS;
- joint service;
- monitoring-only service;
- duplicate VTS ID.

### Pass 5 — count audit
For each record verify the `count_impact`.

Do not proceed to the next batch until the current batch passes.

---

## Batch result

Use one of:

- **PASS**
- **PASS WITH UNRESOLVED ITEMS**
- **FAIL — RESEARCH REQUIRED**

Create:

`audits/stage3/final_count/FCxx_VTS_Count_Audit.md`

Do not overwrite the historical Stage 2 audit.

---

## Working output files

Maintain:

### 1. Per-TSS fact-check register

`data/current/Final_VTS_Count_Fact_Check.csv`

One row for each of the 69 TSS.

### 2. Candidate service additions

`data/current/Final_VTS_Count_New_Services.csv`

Only genuinely new service identities.

### 3. Rationalisation register

Use/update:

`data/current/Rationalised_VTS_Register.csv`

Do not delete historical VTS IDs.

### 4. Final count report

Create when all 69 are resolved:

`audits/stage3/FINAL_TSS_LINKED_VTS_COUNT.md`

---

## Final report requirements

The final report must state:

- authoritative TSS baseline: **224**;
- TSS with confirmed core VTS association;
- TSS with supplemental monitoring/traffic-control association;
- TSS with no qualifying service;
- TSS still unresolved;
- existing service identities before this pass: **53**;
- new services added by the 69-record fact check;
- duplicates/aliases/sectors merged during rationalisation;
- **final core TSS-linked VTS count**;
- **final supplemental service count**;
- **final guide-service candidate count**;
- counts by editorial region;
- complete rationalised name list by region;
- any residual caveats.

A final count may only be described as **final researched** when the number of TSS with unresolved VTS association is **zero**.

---

## GitHub safety rules

- Work sequentially in five-record batches.
- Fetch current `main` before every write.
- Do not replace a shared CSV with an older snapshot.
- Update records by canonical TSS ID.
- Preserve all unrelated TSS rows.
- Do not alter B20-B29 findings except where this fact-check directly resolves one of their remaining unresolved VTS questions.
- Re-run register validation after every batch.
- Do not force-push.
- Commit each audited batch separately.

Suggested commit:

`Stage 3 FC01: resolve final TSS-linked VTS count candidates`

---

## Completion test

The task is complete only when:

1. all 69 records have a final VTS result;
2. no count-changing TSS remains unresolved;
3. every positive association maps to one canonical service identity;
4. new services are deduplicated against the existing 53;
5. the rationalised service list has one publication-facing name and region per service;
6. the final count report passes the register validator;
7. the final core, supplemental and guide-candidate counts are stated separately.
