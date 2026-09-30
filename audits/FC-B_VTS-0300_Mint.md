# VTS-0300 minted

**Date:** 30 September 2026  
**Action:** Add Nakhodka VTS to the master identity set.

| Field | Value |
|---|---|
| `vts_id` | `VTS-0300` (AI 3 reserved block `VTS-0300–0399`) |
| Official name | Nakhodka VTS (Peter the Great Gulf Regional VTS — Sectors 1B and 2) |
| Call sign | Nakhodka-Traffic |
| Authority | FSUE Rosmorport Far-Eastern Basin Branch; operator JSC NORFES |
| Linked TSS | TSS-0217 only |
| Coverage | Partial |
| Count impact | +1 (register was 53) |

## Files

- Row to append to `data/current/VTS_Entity_Register.csv` after `VTS-0209`: `data/current/VTS_0300_Entity_Row.csv`
- Row to append to `data/current/TSS_Service_Relationships.csv`: `data/current/TSS-0217_VTS-0300_Relationship.csv`
- TSS-0217 association fields to set: `association_status=VTS only`, `vts_id=VTS-0300`, `vts_coverage_type=Partial`

The live 53-row `VTS_Entity_Register.csv` was not rewritten in this commit because of file size. The identity is allocated. Splice the one-row file to make the master list 54.

## Do not also add

Tiran VTS Gulf of Aqaba, Jazan Port Control, Marjan MTCC, Mina al Ahmadi tower, Aniva Bay VTS, a second “Peter the Great Gulf VTS” row.
