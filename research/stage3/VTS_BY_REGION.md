# Rationalised VTS List by Region

**Working Stage 3 register**  
**Source:** current Stage 2 service register on `main`  
**Service records rationalised:** 53

This list gives each recorded traffic service one publication-facing working name and one primary editorial region.

It is **not yet a final worldwide VTS count**. Monitoring-only services and traffic-control centres remain visible but are separated from core VTS/VTIS/VTMS candidates. Claude's B20-B29 work may add or amend services.

## Rationalisation rules

- Keep one record per operational calling service or coherent VTS/VTIS/VTMS area.
- Keep operational sectors such as *Sassnitz Traffic* where the mariner calls that sector directly.
- Do not split one service merely because it has several centres or sectors.
- Keep joint services such as Channel VTS as one entry.
- Keep adjacent national services such as Puget Sound and Victoria separate.
- Treat monitoring-only services separately from statutory/designated VTS.
- Treat port traffic-control services separately unless their VTS status is confirmed.
- Preserve the existing `VTS-NNNN` identifier for traceability.

## BIS — British Isles and southern North Sea (5)

| ID | Rationalised name | Type | Action |
|---|---|---|---|
| VTS-0001 | Channel VTS | Core VTS | KEEP |
| VTS-0024 | Rotterdam VTS | Core VTS | KEEP |
| VTS-0027 | Humber VTS | Core VTS | NORMALISE_NAME |
| VTS-0041 | Jobourg Traffic | Core VTS | NORMALISE_NAME |
| VTS-0042 | Sunk VTS | Core VTS | KEEP |

## NOI — Norway and Iceland (1)

| ID | Rationalised name | Type | Action |
|---|---|---|---|
| VTS-0039 | NOR VTS (Vardø monitoring service) | Monitoring/information service | SUPPLEMENTAL |

## BAL — Baltic Sea and approaches (11)

| ID | Rationalised name | Type | Action |
|---|---|---|---|
| VTS-0002 | Great Belt VTS | Core VTS | KEEP |
| VTS-0003 | Sound VTS | Core VTS | KEEP |
| VTS-0015 | VTS Zatoka Gdańska | Core VTS | KEEP |
| VTS-0016 | Saint Petersburg VTS | Core VTS | NORMALISE_NAME |
| VTS-0017 | VTS Ławica Słupska (Słupska Bank) | Core VTS | NORMALISE_NAME |
| VTS-0018 | Sassnitz Traffic | Operational VTS sector | KEEP_AS_SECTOR |
| VTS-0019 | Stralsund Traffic | Operational VTS sector | KEEP_AS_SECTOR |
| VTS-0020 | Kadetrenden Traffic | Operational VTS sector | KEEP_AS_SECTOR |
| VTS-0021 | Kiel Traffic | Operational VTS sector | KEEP_AS_SECTOR |
| VTS-0043 | Åland Sea Traffic | Monitoring/information service | SUPPLEMENTAL |
| VTS-0045 | Helsinki Traffic (GOFREP monitoring) | Monitoring/information service | SUPPLEMENTAL |

## NSC — North Sea continental coast (3)

| ID | Rationalised name | Type | Action |
|---|---|---|---|
| VTS-0025 | North Sea Canal Area VTS | Core VTS | NORMALISE_NAME |
| VTS-0026 | German Bight Traffic | Operational VTS sector | KEEP_AS_SECTOR |
| VTS-0044 | VTS Off Texel | Core VTS | KEEP |

## FIC — France, Iberia and Canary Islands (3)

| ID | Rationalised name | Type | Action |
|---|---|---|---|
| VTS-0022 | Finisterre Traffic (Finisterre VTS) | Core VTS | NORMALISE_NAME |
| VTS-0023 | Roca Control (Coast of Portugal VTS) | Core VTS | NORMALISE_NAME |
| VTS-0040 | Ouessant Traffic | Core VTS | NORMALISE_NAME |

## MED — Mediterranean and Black Seas (7)

| ID | Rationalised name | Type | Action |
|---|---|---|---|
| VTS-0200 | Tarifa Traffic | Core VTS | KEEP |
| VTS-0201 | Tangier Traffic | Core VTS | KEEP |
| VTS-0202 | Cabo de Gata Traffic Service (CCS Almería) | Traffic service; VTS designation unconfirmed | REVIEW |
| VTS-0203 | Croatia VTS | Core national VTS | NORMALISE_NAME |
| VTS-0204 | Koper VTS | Core VTS | KEEP |
| VTS-0205 | Trieste VTS | Core VTS | NORMALISE_NAME |
| VTS-0206 | Turkish Straits VTS (TSVTS) | Core VTS | NORMALISE_NAME |

## RSA — Red Sea and Arabian region (3)

| ID | Rationalised name | Type | Action |
|---|---|---|---|
| VTS-0207 | Gulf of Suez VTIMS | Core VTIMS | NORMALISE_NAME |
| VTS-0208 | ADNOC PPA VTIS (Ruwais–Das) | Core VTIS | NORMALISE_NAME |
| VTS-0209 | Ras Tanura VTMS | Core VTMS | NORMALISE_NAME |

## MSI — Malacca, Singapore and Indonesia (3)

| ID | Rationalised name | Type | Action |
|---|---|---|---|
| VTS-0004 | Klang VTS | Core VTS | KEEP |
| VTS-0005 | Johor VTS | Core VTS | KEEP |
| VTS-0006 | Singapore VTIS | Core VTS/VTIS | NORMALISE_NAME |

## CSC — China Sea and China (2)

| ID | Rationalised name | Type | Action |
|---|---|---|---|
| VTS-0028 | Hong Kong VTS | Core VTS | NORMALISE_NAME |
| VTS-0036 | Chengshan Jiao VTS | VTS/reporting centre | NORMALISE_NAME |

## NPC — North America Pacific coast (6)

| ID | Rationalised name | Type | Action |
|---|---|---|---|
| VTS-0009 | Prince William Sound VTS | Core VTS | NORMALISE_NAME |
| VTS-0010 | Puget Sound VTS | Core VTS | NORMALISE_NAME |
| VTS-0011 | San Francisco VTS | Core VTS | NORMALISE_NAME |
| VTS-0012 | Los Angeles–Long Beach VTS | Core VTS | NORMALISE_NAME |
| VTS-0029 | Victoria Traffic (Victoria VTS Zone) | Core VTS | NORMALISE_NAME |
| VTS-0030 | Prince Rupert Traffic (Prince Rupert VTS Zone) | Core VTS | NORMALISE_NAME |

## CAP — Central and South America Pacific coast (4)

| ID | Rationalised name | Type | Action |
|---|---|---|---|
| VTS-0031 | Arica VTS | Core VTS | NORMALISE_NAME |
| VTS-0032 | Iquique VTS | Core VTS | NORMALISE_NAME |
| VTS-0033 | Quintero VTS | Core VTS | NORMALISE_NAME |
| VTS-0034 | Valparaíso VTS | Core VTS | NORMALISE_NAME |

## CGP — Caribbean, Gulf of Mexico and Panama (2)

| ID | Rationalised name | Type | Action |
|---|---|---|---|
| VTS-0013 | Houston–Galveston VTS | Core VTS | NORMALISE_NAME |
| VTS-0038 | Veracruz Maritime Traffic Control Centre (CCTMVER) | Port traffic-control service | SUPPLEMENTAL |

## NAC — North America Atlantic coast (3)

| ID | Rationalised name | Type | Action |
|---|---|---|---|
| VTS-0014 | New York VTS | Core VTS | NORMALISE_NAME |
| VTS-0035 | Canso Traffic (Strait of Canso and Eastern Approaches VTS Zone) | Core VTS | NORMALISE_NAME |
| VTS-0037 | Fundy Traffic (Bay of Fundy VTS Zone) | Core VTS | NORMALISE_NAME |

