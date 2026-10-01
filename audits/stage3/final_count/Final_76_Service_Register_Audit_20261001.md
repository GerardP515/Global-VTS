# Final 76-Service TSS-Derived Register Audit

**Date:** 1 October 2026  
**Branch:** `review/final-tss-derived-vts-register-20261001`

## Final status

- Source TSS population: **224**
- Distinct canonical TSS-derived service identities: **76**
- Core project services: **67**
- Supplemental monitoring/information services: **9**
- Final unresolved TSS: **13**
- The 13 unresolved are **not negative findings**.

## Supplemental identities

- VTS-0217 — Irish Coast Guard traffic monitoring of the Tuskar and Fastnet TSS — TSS-0085; TSS-0087
- VTS-0039 — NOR VTS (Vardø VTS centre) — TSS-0066; TSS-0067; TSS-0068; TSS-0069; TSS-0070; TSS-0071; TSS-0072; TSS-0073; TSS-0074; TSS-0075; TSS-0076; TSS-0077; TSS-0078; TSS-0079; TSS-0080; TSS-0081; TSS-0082; TSS-0083; TSS-0084
- VTS-0212 — Icelandic Coast Guard Maritime Traffic Service (Vaktstöð siglinga, MTS Reykjavík) — TSS-0092; TSS-0093
- VTS-0043 — Åland Sea Traffic — TSS-0012
- VTS-0045 — Helsinki Traffic (GOFREP monitoring) — TSS-0004; TSS-0005; TSS-0006; TSS-0007
- VTS-0214 — Sweden Traffic (TSS monitoring) — TSS-0008; TSS-0009; TSS-0011; TSS-0013; TSS-0014; TSS-0015; TSS-0016; TSS-0030; TSS-0031
- VTS-0213 — CROSS Méditerranée / Corsica Channel sémaphores (Cap Corse, Sagro) — TSS-0102
- VTS-0229 — Salvamento Marítimo CCS Valencia traffic monitoring service for the Cabo de la Nao DST — TSS-0101
- VTS-0228 — Panama Canal Authority Marine Traffic Control / Panama Canal VTMS, Cristobal and Flamenco Signal Stations (replaces the Atlantic-only D8 entry; not a second service) — TSS-0176; TSS-0213

## Data reconciliation performed

Five newer supplemental identities were already present in the entity and final-count registers but lacked complete backlinks in the service relationship views. This audit reconciled:

- VTS-0212 — TSS-0092; TSS-0093
- VTS-0213 — TSS-0102
- VTS-0217 — TSS-0085; TSS-0087
- VTS-0228 — TSS-0176; TSS-0213
- VTS-0229 — TSS-0101

The following files were updated accordingly:

- `data/current/Guide_Service_Candidates.csv`
- `data/current/TSS_Service_Relationships.csv`
- `data/current/TSS_VTS_MRS_Association_Register.csv`

## Interpretation

The number **76** is the count of distinct service identities produced by the project's TSS→VTS workflow. It must not be described as the total number of VTS worldwide, nor should all 76 be described as formal VTS.

The authoritative publication-facing register is:

- `data/current/TSS_Derived_VTS_Final_Register.csv`
- `research/stage3/TSS_DERIVED_VTS_FINAL_REGISTER.md`
