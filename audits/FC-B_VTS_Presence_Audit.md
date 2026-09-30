# FC-B — VTS presence validation

**Region:** Red Sea, Arabian, Indian Ocean and Asia  
**TSS count:** 23  
**Date:** 30 September 2026  
**Question:** is a VTS present on the TSS?  
**Categories:** Existing service / New service / No TSS-linked service / Unresolved  
**Coverage (only if a service is linked):** Full / Partial / Monitoring

Against the live register of **53** VTS identities. Pass-1 B26–B29 notes and `B20_B29_Association_Rows.csv` were leads only. Sources below were reopened. A failed search is not a negative finding.

Existing IDs that sit in this geography but are **not** on an FC-B TSS: `VTS-0207` GOS VTIMS, `VTS-0208` Das VTIS, `VTS-0209` Ras Tanura VTMS, `VTS-0028` Hong Kong VTS (only Dangan is in this batch).

---

## Count-impact summary

| Result | TSS | Count impact |
|---|---:|---:|
| Existing service | 1 | 0 |
| New service (after dedup) | 1 | **+1** |
| No TSS-linked VTS | 2 | 0 |
| Unresolved | 19 | 0 |
| **Running new-service add** | | **+1 Nakhodka VTS** |

Do not add Tiran “VTS Gulf of Aqaba”, Mina al Ahmadi Port Control, Marjan MTCC, or Bandar Abbas Port Control to the 53 until an authority polygon names the TSS.

---

## Country groups

### Egypt / Jordan / Saudi — Strait of Tiran

| TSS | Finding | Coverage | Impact | Note |
|---|---|---|---:|---|
| TSS-0126 In the entrance to the Gulf of Aqaba | **Unresolved** | — | 0 | NGA Pub. 172 (current compilation) names a station call sign **VTS Gulf of Aqaba** on VHF 8/9/10/16 “established to ensure safety of navigation within the TSS” and to monitor 15 M N and S of the station. That is a **new-service candidate**, not one of the 53. No Egyptian or Saudi authority users’ page defining the area was opened. **Aqaba VTS** (Jordan / APMSCO in the same NGA volume) runs only from the Jordan–Saudi border to the Jordan–Israel border and does **not** cover Tiran. Do not merge. |

### Saudi — Jazan, Marjan/Zuluf, Khafji

| TSS | Finding | Coverage | Impact | Note |
|---|---|---|---:|---|
| TSS-0127 Jazan deep-water route | **Unresolved** | — | 0 | NGA: Jazan / JECP **Port Control** VHF 67, daylight, `jecp.portcontrol@nps.com.sa`. Mawani corporate pages do not name a VTS on the IMO TSS. Port Control is a Decision-5 lead only until the area is shown to include the TSS. |
| TSS-0137 Marjan/Zuluf | **Unresolved** | — | 0 | Aramco MIPD 2025 paper: offshore **MTCC** on jack-up LB 9 linked to a work-vessel tracking system. That is field construction traffic, not a published VTS area naming the IMO TSS for through traffic. Not `VTS-0209` Ras Tanura. |
| TSS-0138 Approaches to Ra’s al Khafji | **Unresolved** | — | 0 | IMO COLREG.2/Circ.54 scheme. NGA/terminal VHF 16 only. No VTS users’ page opened. |

### Yemen / Eritrea / Djibouti — southern Red Sea and Bab el Mandeb

| TSS | Finding | Coverage | Impact | Note |
|---|---|---|---:|---|
| TSS-0128 W/S of Hanish al Kubra | **Unresolved** | — | 0 | No coastal VTS users’ page opened. UKMTO / MSTC are security overlays, not VTS. |
| TSS-0129 E of Jabal Zuqar | **Unresolved** | — | 0 | Same cluster. |
| TSS-0130 Bab el Mandeb | **Unresolved** | — | 0 | Same. Failed search is not absence. |

### Oman / Iran — Hadd, Kuh, Hormuz, Tunb–Farur

| TSS | Finding | Coverage | Impact | Note |
|---|---|---|---:|---|
| TSS-0131 Off Ras al Hadd | **Unresolved** | — | 0 | IMO TSS + ITZ. AMNAS maintains the light. ASYAD rules seen are port (PSQ), not this TSS. |
| TSS-0132 Off Ra’s al Kuh | **Unresolved** | — | 0 | NGA: ships **bound for Iranian ports** report to Bandar Abbas Port Control when passing the cape. Destination rule, not an all-traffic VTS on the TSS. |
| TSS-0133 Strait of Hormuz | **Unresolved** | — | 0 | No SOLAS V/11 scheme. No standing authority VTS whose published area is the IMO TSS. 2026 temporary corridors / IRGC “smart control” are security or crisis traffic management. Do not mint a VTS from them. |
| TSS-0134 Tunb–Farur | **Unresolved** | — | 0 | Same Bandar Abbas lead. Island dispute is not a second TSS or a second VTS. |

### Kuwait — Mina Al-Ahmadi

| TSS | Finding | Coverage | Impact | Note |
|---|---|---|---:|---|
| TSS-0139 North scheme I | **Unresolved** | — | 0 | NGA Pub. 172: **Mina al Ahmadi control tower / Port Control** VHF 69 grants permission inside a buoyed security zone; IMO TSS lies in the approaches. Decision-5 candidate if an overlay shows the TSS inside that zone. No document titled VTS. One control family for all three children. |
| TSS-0140 North scheme II | **Unresolved** | — | 0 | Same tower. Do not invent a second service. |
| TSS-0141 South scheme | **Unresolved** | — | 0 | Same. |

### Sri Lanka

| TSS | Finding | Coverage | Impact | Note |
|---|---|---|---:|---|
| TSS-0142 Off Dondra Head | **Unresolved** | — | 0 | IMO TSS since 1980. Colombo / Hambantota are port VTS and are not shown to cover this offshore scheme. No SLPA list proving absence. |

### South Africa

| TSS | Finding | Coverage | Impact | Note |
|---|---|---|---:|---|
| TSS-0143 Off Alphard Banks | **No TSS-linked VTS** | — | 0 | NGA Pub. 160 (current) lists SA **inshore** VTS and states they are “distinct from an offshore system; i.e., for Laden Tankers off the Alphard Bank”. SANHO Annual 2026 describes the two Agulhas Bank TSS as obligatory for laden tankers and points reports to SAMSA via port control — routeing / tanker reporting, not a named VTS on the TSS. |
| TSS-0144 Off the FA platform | **No TSS-linked VTS** | — | 0 | SANHO Mossel Bay VTS appendix: radar ~20 NM, reporting lines 12 NM and 6 NM. FA platform TSS is 47 miles south of Mossel Bay. Boundary comparison: TSS is outside Mossel Bay VTS. Same offshore tanker family as Alphard. |

### China / Hong Kong — Dangan Channel

| TSS | Finding | Coverage | Impact | Note |
|---|---|---|---:|---|
| TSS-0157 In the Dangan Channel | **Existing service** `VTS-0028` Hong Kong VTS | **Partial** | 0 | HK Marine Department 2003 DCTSS paper and 2015 HK NtM 97: parts of Dangan Channel TSS (precautionary areas / lanes) lie in HKSAR waters; HK VTC provides traffic information inside HKSAR; mainland authorities outside. HK VTS-0028 already exists. Shenzhen VTS 2024 eastern report line L7 is ~22°24.8'N; Dangan lanes sit ~22°06'–22°08'N, so Shenzhen VTS is not shown to cover this TSS. Mainland portion remains a second-service **lead**, not minted. |

### Russian Federation — Kurils, Aniva, Nakhodka, Ostrovnoi

| TSS | Finding | Coverage | Impact | Note |
|---|---|---|---:|---|
| TSS-0214 Fourth Kuril Strait | **Unresolved** | — | 0 | No Rosmorport VTS page for the Kurils. Petropavlovsk-Kamchatskiy VTS is a port service. No complete official RF VTS list. |
| TSS-0215 Proliv Bussol | **Unresolved** | — | 0 | Same. |
| TSS-0216 Off the Aniwa Cape | **Unresolved** | — | 0 | Rosmorport lists **VTS of the Aniva Bay** (Sakhalin). An older Korsakov draft zone ended ~46°25'N / 143°04'E; the national scheme off Cape Aniva sits further S/E on previously cited coordinates. Existing nearby VTS; coverage of **this TSS** not demonstrated. Not in the 53. Do not add until overlay. |
| TSS-0217 Approaches to the Gulf of Nakhodka | **New service** | **Partial** | **+1** | Current Rosmorport Far-Eastern pages: **Nakhodka VTS** (call sign Nakhodka-Traffic) is Sector 1B + Sector 2 of the Peter the Great Gulf Regional VTS. Sector 1B is the approaches, limited S by the territorial-sea boundary, E 133°43.00'E, W 132°28.00'E. UKHO ALRS-style notice (Wk 11/26 extract) describes Nakhodka VTS. Not one of the 53. TSS coordinates were not replotted on the 1B polygon, so coverage is **Partial** not Full. Dedup: one service, not a second “Peter the Great Gulf VTS” row for this TSS. |
| TSS-0218 Off the Ostrovnoi Point | **Unresolved** | — | 0 | Possible edge of the same regional VTS. No coordinate overlay. Do not extend Nakhodka VTS to this TSS by proximity. |

---

## Identity / duplicate check (step 4)

| Candidate name | Against the 53 | Decision |
|---|---|---|
| VTS Gulf of Aqaba (Tiran) | No match. Not Jordan Aqaba VTS | Do not add |
| Aqaba VTS (Jordan) | No match in 53; wrong TSS | Out of scope for 0126 |
| Jazan / JECP Port Control | No match | Lead only |
| Marjan MTCC | Not Ras Tanura `VTS-0209` | Lead only |
| Bandar Abbas Port Control | No match | Lead only |
| Mina al Ahmadi Port Control | No match | One family for 0139–0141; lead only |
| Mossel Bay VTS | No match in 53 | Exists as inshore VTS; **does not** cover 0143/0144 |
| Hong Kong VTS | **VTS-0028** | Reuse; Partial on 0157 |
| Shenzhen VTS | No match | Not shown on Dangan lanes |
| Nakhodka VTS / Peter the Great Gulf Regional VTS | No match | **+1 new** (single identity) |
| Aniva Bay VTS | No match | Nearby; not linked |

---

## Sources reopened

| Source | Used for |
|---|---|
| NGA Pub. 172 (Red Sea / Gulf) | 0126, 0127, 0132, 0138, 0139–0141 |
| NGA Pub. 160 (South Africa) | 0143, 0144 |
| SANHO Annual Notice 2026; Mossel Bay VTS appendix | 0143, 0144 |
| Aramco MIPD 2025 MTCC paper | 0137 |
| HK MD DCTSS paper 2003; HK NtM 97/2015; HK VTS configuration plan 2025 | 0157 |
| Shenzhen MSA VTS rules 2024 (in force 1 Apr 2024) | 0157 negative for Shenzhen coverage |
| COLREG.2/Circ.71 Dangan Channel | 0157 identity |
| Rosmorport Far-Eastern / Nakhodka VTS pages | 0216–0218 |
| UKHO Wk 11/26 Nakhodka VTS extract | 0217 |
| ADNOC PPA VTIS procedure / ALRS Wk 14/26 Das VTS | Identity check only (not an FC-B TSS) |

---

## What this batch does not do

- Does not mint `VTS-030x` IDs. Nakhodka VTS is a **count** of +1 pending the Stage 2 identity row.
- Does not treat UKMTO, MSTC, JMIC, NCAGS, or 2026 Hormuz crisis corridors as VTS.
- Does not mark southern Red Sea “no service” after a failed search.
- Does not splice register rows. Live `association_status` can stay Unresolved except where the project owner accepts the two SA negatives and the HK / Nakhodka positives.
