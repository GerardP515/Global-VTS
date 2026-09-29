# IMO 2025 Baseline Verification

## Source

- Publication: *Ships’ Routeing 2025 Edition*
- Edition: Fifteenth edition, 2025
- Scope: routeing measures adopted through MSC 110 and reporting systems adopted through MSC 110.
- Local source SHA-256: `69660c0418285f81931e26a0d6e5544029572bc6b7a52623cc3a6be03234d613`

## Verified counts

- Part B indexed parent entries: **164**
- Individual TSS records after source-level decomposition: **224**
- Part I mandatory ship reporting systems: **23**

## Method

1. Extract every Part B index entry from the 2025 edition contents.
2. Review each Part B description for explicit multiple TSS.
3. Split only where the IMO text identifies separate traffic separation schemes.
4. Do not split a single TSS merely because it contains several parts, lanes or precautionary areas.
5. Preserve the Part B parent reference for every individual TSS.

## Multi-TSS parent entries

| IMO ref | Parent title | Individual TSS |
|---|---|---:|
| B-I/11 | The Åland Sea | 2 |
| B-I/16 | On the approaches to the Polish ports in the Gulf of Gdańsk | 2 |
| B-I/26 | In the vicinity of Kattegat | 5 |
| B-II/8 | In the SUNK area and in the northern approaches to the Thames estuary | 3 |
| B-II/9 | Off Friesland | 5 |
| B-II/10 | In the approaches to Hook of Holland and at North Hinder | 7 |
| B-II/11 | In the approaches to IJmuiden | 3 |
| B-II/13 | Off Vlieland, Vlieland North and Vlieland Junction | 2 |
| B-II/19 | Off the coast of Norway | 19 |
| B-II/27 | Off the south-west coast of Iceland | 2 |
| B-III/11 | In the Adriatic Sea: in the Gulf of Trieste | 3 |
| B-III/14 | Off the Mediterranean coast of Egypt | 4 |
| B-IV/15 | Off Mina Al-Ahmadi | 3 |
| B-V/11 | In the East Lamma and Tathong Channels | 2 |
| B-VI/1 | Off Southwest Australia | 2 |
| B-VII/2 | In the Strait of Juan de Fuca and its approaches | 6 |
| B-VII/4 | In Haro Strait and Boundary Pass, and in the Strait of Georgia | 2 |
| B-VIII/1 | On the Pacific coast of Panama | 3 |
| B-X/6 | In the waters off Chengshan Jiao Promontory | 4 |

## Section totals

| IMO section | Parent entries | Individual TSS |
|---|---:|---:|
| Baltic Sea and adjacent waters | 26 | 32 |
| Western European waters | 31 | 65 |
| Mediterranean Sea and Black Sea | 22 | 27 |
| Indian Ocean and adjacent waters | 18 | 20 |
| South-East Asia | 12 | 13 |
| Australasia | 3 | 4 |
| North America, Pacific coast | 8 | 14 |
| South America, Pacific coast | 17 | 19 |
| Western North Atlantic Ocean, Gulf of Mexico and Caribbean Sea | 19 | 19 |
| Asia, Pacific coast | 6 | 9 |
| Eastern North Atlantic and South Atlantic Oceans | 2 | 2 |

## Identifier migration

The v0.2 `TSS-xxxx` identifiers were provisional and based on a third-party candidate list.
Version 1.0 freezes the canonical `TSS-0001` onward sequence in IMO 2025 source order.
The legacy IDs remain available through the crosswalk and must not be treated as current canonical IDs.