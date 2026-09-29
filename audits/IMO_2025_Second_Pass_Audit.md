# IMO 2025 TSS Baseline Second-Pass Audit

## Result

- Part B indexed parent entries: **164**
- Multi-TSS parent entries identified: **19**
- Named or explicitly enumerated individual TSS records: **224**
- Part I mandatory ship reporting systems: **23**

## Counting rule

The individual inventory splits a Part B parent only where the IMO text names or explicitly enumerates separate traffic separation schemes.
It does not split a single named TSS merely because that scheme contains several parts, separation zones, lane groups, precautionary areas or internal routeing elements.

This makes the 224-record dataset a research-entity inventory for the Global VTS project. It is not a count of every geometric lane segment.

## Multi-TSS parents verified

| IMO ref | Parent title | TSS records |
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

## Second-pass exceptions checked

- **Słupska Bank (B-I/17):** retained as one TSS. The IMO text says the scheme consists of three parts.
- **Off Neist Point in The Minches (B-II/26):** retained as one TSS, with explicit scheme name `Little Minches`.
- **In the Dangan Channel (B-V/12):** retained as one named TSS. East and West are internal sections within a singular scheme description.
- **In Puget Sound and its approaches (B-VII/3):** retained as one named project TSS entity. The text contains internal traffic-separation arrangements under Rosario Strait, Approaches to Puget Sound and Puget Sound, but does not give separate top-level TSS titles for the inventory.
- **Off New York (B-IX/6):** retained as one TSS. The scheme consists of five parts.

## Legacy reconciliation

- Legacy v0.2 candidate rows: **170**
- Current authoritative TSS records covered by legacy candidates: **223 of 224**
- New Part B candidate with no legacy v0.2 record: **B-IV/3 — Near the deep-water route leading to Jazan Economic City Port**.

## Status

This baseline is suitable for the next VTS-association research stage. Future IMO amendments must be handled through change control rather than renumbering existing canonical IDs.