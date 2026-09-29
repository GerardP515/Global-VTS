# Stage 2 association audit: B19

### Batch
B19

### TSS reviewed
- TSS-0091 Little Minches (B-II/26)
- TSS-0092 North-west of Garðskagi Point (B-II/27)
- TSS-0093 South-west of the Reykjanes Peninsula (B-II/27)
- TSS-0094 Off Finisterre (B-II/28)
- TSS-0095 Off Cape Roca (B-II/29)

### Results

| TSS | VTS | Mandatory reporting | Classification |
|---|---|---|---|
| TSS-0091 Little Minches | - | VRS-0005 WETREP (West European Tanker Reporting System) | MRS only |
| TSS-0092 North-west of Garðskagi Point | - | Unresolved | Unresolved |
| TSS-0093 South-west of the Reykjanes Peninsula | - | Unresolved | Unresolved |
| TSS-0094 Off Finisterre | VTS-0017 Finisterre VTS (call sign 'Finisterre Traffic') | VRS-0011 FINREP | VTS + MRS |
| TSS-0095 Off Cape Roca | VTS-0018 VTS costeiro do continente (Coast of Portugal VTS; call sign 'Roca Control') | VRS-0012 COPREP | VTS + MRS |

### Evidence check
Pass 2 (researcher): Reopened MSC.63(67), MSC.162(78), MSC.278(85), MSC.301(87), MSC.250(83), MSC.316(88), DL 263/2009 and COLREG.2/Circ.58/59/61 text; recomputed Cape Roca and Iceland boundary comparisons. Finisterre and Cape Roca positives verified; Iceland TRANSREP confirmed adjoining/outside only.

Pass 4 (coordinator): An independent checker re-opened MSC.190(79), MSC.162(78), Decree-Law 263/2009, COLREG.2 circulars and the DGRM and EMSA pages, re-did the boundary geometry, and upheld every positive classification (research/stage2/pass4/chk_T_result.json).

### Duplicate check
Finisterre VTS and Coast of Portugal VTS are distinct from their centres (CCS Finisterre, CCTMC) and from the reporting schemes FINREP/COPREP. WETREP recorded as additional MRS for Finisterre, Cape Roca and Little Minches without new IDs. Iceland MTS not treated as VTS.

Shared entities in this batch:
- None within this batch.

### Changes made
Changes at Pass 4 (coordinator review of the research output):
- TSS-0091 reporting_boundary_basis: note added: "Pass 4: Minches are UK internal waters but WETREP's coast-based area does not exclude them." (Pass 4 note.)
- TSS-0094 unresolved_issue: note added: "Salvamento Maritimo website unreachable (TLS error, HTTP 503); current operation rests on the February 2025 Ministry of Transport article." (Pass 4 caveat.)
- TSS-0095 unresolved_issue: note added: "Whether Decree-Law 263/2009 has been amended could not be confirmed (Diario da Republica page empty)." (Pass 4 caveat.)

### Unresolved issues
- TSS-0091: VTS: none established. No authoritative complete list of UK VTS (e.g. ALRS Vol 6) was opened; MGN 401 (R02) gives VTS guidance but no list. A voluntary Minches reporting arrangement with Stornoway Coastguard appears only in non-official sources; not verified.
- TSS-0092: Whether Iceland's national reporting system (Act on the Maritime Traffic Service) is a formally named mandatory scheme applicable to ships using this TSS; whether MTS is declared a VTS. No authoritative absence evidence, so not 'Neither confirmed'.
- TSS-0093: Whether Iceland's national reporting system (Act on the Maritime Traffic Service) is a formally named mandatory scheme applicable to ships using this TSS; whether MTS is declared a VTS. No authoritative absence evidence, so not 'Neither confirmed'.
- TSS-0094: Salvamento Marítimo website unavailable (HTTP 503 / TLS chain error), so current VHF channels not confirmed from the operator. Salvamento Maritimo website unreachable (TLS error, HTTP 503); current operation rests on the February 2025 Ministry of Transport article.
- TSS-0095: Coverage rests on coordinate comparison with narrow margins (about 0.2' of longitude); consolidated current text of DL 263/2009 not opened; DGRM own web page not opened. Whether Decree-Law 263/2009 has been amended could not be confirmed (Diario da Republica page empty).

### Audit result
PASS WITH UNRESOLVED ITEMS

Sources are listed in `sources/SOURCE_REGISTER.md` (renumbered from SRC-B19-nn; see `research/stage2/id_mapping_b10_b19.csv`). VTS entities are in `data/current/VTS_Entity_Register.csv`.
