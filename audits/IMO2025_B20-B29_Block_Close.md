> Superseded status note: all 50 first-pass rows are now integrated into the master CSV. They remain first-pass-only, not audited.

# IMO 2025 B20–B29 block close

**Date:** 30 September 2026  
**IDs:** TSS-0096 to TSS-0145

## Register

50 pass-1 rows are in [`data/current/B20_B29_Association_Rows.csv`](../data/current/B20_B29_Association_Rows.csv).

**Insert point in the live file** [`data/current/TSS_VTS_MRS_Association_Register.csv`](../data/current/TSS_VTS_MRS_Association_Register.csv): after `TSS-0095` (Off Cape Roca) and before `TSS-0146` (Port Klang to Port Dickson).

The live register was not rewritten in place in this commit (payload size). The 50-row file uses the same columns. `review_status=pass1-recorded` (not `audited`).

## IDs reused (not minted)

| ID | Use |
|---|---|
| VTS-0023 | TSS-0096 Cape S. Vicente (same as TSS-0095) |
| VRS-0012 COPREP | TSS-0096 |
| VRS-0013 GIBREP | TSS-0098 |
| VRS-0015 ADRIREP | TSS-0105 to TSS-0110 |
| VTS-0004 Klang | TSS-0145 |
| VRS-0016 STRAITREP | TSS-0145 |

TUBRAP, UKMTO, MSTC, JMIC, NCAGS are not in `vrs_id`.
