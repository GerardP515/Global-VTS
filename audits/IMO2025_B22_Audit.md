# IMO 2025 Batch 22 audit

**Sequence:** `research/batches_imo2025`  
**Records:** TSS-0106 to TSS-0110  
**Date:** 29 September 2026  
**Assignment:** B20–B29

## Batch result

| ID | Scheme | IMO identity | Mandatory reporting | Named operational VTS |
|---|---|---|---|---|
| TSS-0106 | Approaches to Gulf of Trieste | Confirmed — B-III/9 | **VRS-0015 ADRIREP** (whole Adriatic N of 40°25'N) | Trieste VTS — lead; polygon vs this TSS not opened |
| TSS-0107 | Approaches to Gulf of Venice | Confirmed — B-III/10 | **VRS-0015 ADRIREP** | Venice VTS users’ manual places a TSS **in the VTS area** and cites the North Adriatic TSS |
| TSS-0108 | In the Gulf of Trieste | Confirmed — B-III/11 | **VRS-0015 ADRIREP** | Trieste VTS (IT) and Koper VTS (SI) share the gulf. Not one VTS |
| TSS-0109 | Approaches to/from Koper | Confirmed — B-III/11 | **VRS-0015 ADRIREP** | **Koper VTS manual: manages the TSS** in Slovenian waters |
| TSS-0110 | Approaches to/from Monfalcone | Confirmed — B-III/11 | **VRS-0015 ADRIREP** | No separate national VTS centre. Capitaneria monitor; parent is Trieste VTS |

One reporting scheme for all five. No new VRS ID. No VTS-0xx minted.

Dates for ADRIREP: [research/TODO.md](../research/TODO.md).

---

## Duplicate control

| Entity | Count once |
|---|---|
| VRS-0015 ADRIREP | Same ID as TSS-0105 (B21). Sectors / CSTs are not extra schemes |
| Venice VTS | Italian national centre. Also an ADRIREP CST. One VTS, two functions |
| Trieste VTS | Same pattern |
| Koper VTS | Slovenian Maritime Administration. Area = SI inland + territorial waters. Not a sector of Trieste VTS |
| Monfalcone | Port monitoring. Do not invent a fifth North Adriatic VTS |

B-III/11 is one IMO parent with three child TSS (0108, 0109, 0110). Count three schemes, one parent.

---

## Authority evidence

### Koper VTS — gov.si / Users Manual

- Area: inland waters and territorial sea of Slovenia.
- “management of the Traffic Separation Scheme (TSS)”.
- Call: Koper VTS. VHF 69 primary, 72 backup. MSI on 07.
- Mandatory: 300 GT+; fishing, traditional and recreational ≥45 m.
- Contact 1 hour before entering the VTS area; continuous watch on 69.
- ENCs include SI3TZ003 Approach to Port of Koper.

That is enough to treat Koper VTS as the named service on TSS-0109. ID not minted.

### Venice VTS — Guardia Costiera users’ manual (EN)

- Area polygon off Lido, Malamocco and Chioggia.
- “A Traffic Separation Scheme (TSS) has been established in Venice VTS area.”
- Also: vessels bound to report the North Adriatic TSS (COLREG.2/Circ.58) even if not inside the VTS area.
- Primary Ch 9. Venice MRSC cited as ADRIREP authority under MSC.139(76).

### Trieste VTS — Guardia Costiera national list

- One of 11 Italian VTS centres. English users’ manual published, not opened line-by-line this pass.
- EMSA modernised-ADRIREP table: VTS TRIESTE is a competent shore-based authority.

### Monfalcone — ADSPMAO port page

- “Il monitoraggio del traffico marittimo è effettuato da parte della Capitaneria di Porto di Monfalcone con sistema VTS.”
- Not on the national 11-centre list. Classify as local monitoring under Trieste unless a decree names a centre.

---

## Unresolved

1. Open Trieste VTS users’ manual and tick which of 0106 / 0108 / 0110 sit inside its polygon.
2. Confirm whether Venice VTS area contains the IMO “approaches to Gulf of Venice” TSS or only the inner port TSS.
3. Overlay Koper VTS limit vs TSS-0108 (gulf scheme) — likely only the Slovenian slice.
4. Master workbook.

## Next

B23: B-III/12–14 (Mediterranean continuation, including Egypt multi-TSS parent).
