# Global VTS Census Pilot — AUS / Australia

**Date:** 1 October 2026  
**Branch:** `review/global-vts-census-aus-20261001`  
**Region:** AUS — Australia  
**Competent authority:** Australian Maritime Safety Authority (AMSA)  
**Status:** **COUNTRY COMPLETE at formal VTS-area level**

## Result

Australia has **35 currently authorised formal VTS areas** in the live AMSA competent-authority list.

| Measure | Count |
|---|---:|
| Authorised formal VTS areas | **35** |
| Authorised VTS provider organisations / provider groups | **7** |
| Matches in the current 76-service TSS-linked register | **0** |
| Provisional new formal VTS-area records for the global census | **35** |
| Unresolved candidate areas | **0** |

This is a **global VTS census result**, not a change to the TSS→VTS project count.

## Primary completeness rule

AMSA is the competent authority for VTS in Australia under the Navigation Act / Marine Order 64 framework. Its live page states that it authorises and audits VTS providers and gives the entities/areas authorised to provide vessel traffic services in Australia.

Because a competent authority publishes an explicit national authorised list, Australia meets the project's strongest country-completeness stopping rule. ALRS discovery is therefore a cross-check rather than the primary population source for this country.

Primary sources:

- **SRC-2303** — AMSA, VTS areas in Australia.
- **SRC-2304** — AMSA, Australian legislative framework for VTS / Marine Order 64.

## Authorised areas by provider

| VTS provider | Formal VTS areas | Count |
|---|---|---:|
| Maritime Safety Queensland | Abbot Point; Brisbane; Cairns; Gladstone; Hay Point; Mackay; REEFVTS; Townsville; Weipa | **9** |
| TasPorts | Bell Bay; Burnie; Coles Bay; Devonport; Grassy; Hobart; Lady Barron; Port Latta; Stanley; Strahan | **10** |
| Flinders Ports Pty Ltd | Adelaide; Ardrossan; Klein Point; Port Giles; Port Lincoln; Spencer; Thevenard; Wallaroo | **8** |
| Pilbara Ports | Ashburton; Dampier; Port Hedland | **3** |
| Port Authority of New South Wales | Newcastle; Port Kembla; Sydney | **3** |
| Ports Victoria | Melbourne | **1** |
| Fremantle Ports | Fremantle | **1** |
| **Total** | | **35** |

## Deduplication decisions

### REEFVTS

Count **one** formal VTS area.

REEFVTS is the Great Barrier Reef and Torres Strait coastal VTS. Maritime Safety Queensland divides operations into Reef North and Reef South, but these are operational subdivisions of one authorised VTS area, not two census identities.

### Melbourne

Count **one** formal VTS area.

Ports Victoria operates Melbourne VTS and Lonsdale VTS operational sectors. AMSA's competent-authority register identifies **Melbourne** as the authorised VTS area. The sectors are retained as sub-entities and are not counted as separate VTS areas.

### Spencer

Count **one** formal VTS area.

Flinders Ports confirms that Spencer VTS comprises Port Pirie, Port Bonython, Whyalla, transhipment areas and the Spencer Gulf Deep Water Passage. Those ports/areas must not be inflated into separate formal VTS identities.

### Sydney

Count **one** formal VTS area.

Sydney VTS manages both Sydney Harbour and Port Botany. AMSA lists Sydney as one authorised VTS area.

### Shared centres

Do not use VTS-centre count as the service count.

Examples:
- Queensland has multiple authorised VTS areas served by five regional VTS centres.
- Flinders Ports uses a centralised VTS centre for Adelaide and its regional VTS areas.
- Pilbara Ports uses the Dampier VTS centre for Dampier/Ashburton operations while Port Hedland has its own VTS centre.

The global census must therefore preserve **area**, **service identity**, **centre** and **sector** as separate fields.

## Provider corroboration

Current provider sources were reopened to test the AMSA population and identity structure:

- **SRC-2305** — Maritime Safety Queensland: current VTS provider and five regional VTS centres.
- **SRC-2306** — REEFVTS: coastal VTS, split into Reef North and Reef South.
- **SRC-2307** — TasPorts: current 10-area VTS list and call signs.
- **SRC-2308** — Flinders Ports: eight VTS identities/areas, with regional accreditation obtained in 2024.
- **SRC-2309** — Ashburton VTS.
- **SRC-2310** — Dampier VTS.
- **SRC-2311** — Port Hedland VTS.
- **SRC-2312** — Ports Victoria current marine operations; Melbourne/Lonsdale operational structure.

The displayed metadata on the AMSA list says "Last updated: 14 November 2023", but the live list contains Flinders regional VTS areas that the provider says gained accreditation in 2024. The displayed page-update date must therefore **not** be used alone as a currency test. Live competent-authority listing plus current provider corroboration is the safer method.

## Comparison with the TSS→VTS register

A name/provider comparison against the current `VTS_Entity_Register.csv` found **no Australian VTS identities** in the 76-service TSS-linked register.

That is expected: the TSS→VTS register answers a different question and should not be used as the global census population.

Do **not** calculate a worldwide total by simply adding 35 to 76. The final global census must independently census every region and then reconcile/deduplicate against the existing TSS-derived identities.

## Census file

`research/global_vts_census/AUS_Australia_VTS_Census.csv`

It contains 35 provisional census IDs:

`GVTS-AUS-001` to `GVTS-AUS-035`.

These are census IDs only. Final `VTS-xxxx` canonical IDs should be minted after the global identity/rationalisation rules are frozen.

## Method assessment

The pilot validates the proposed automated workflow:

1. identify competent authority;
2. obtain explicit national authorised list where available;
3. create candidate rows;
4. reopen provider sources to verify currency and identity structure;
5. separate VTS areas from centres and sectors;
6. deduplicate;
7. compare against existing project corpus;
8. assign country-completeness status;
9. send only genuine ambiguities to manual review.

**Australia outcome: PASS — no unresolved formal VTS-area candidates.**
