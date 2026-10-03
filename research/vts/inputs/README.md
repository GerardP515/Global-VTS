# Frozen input for the 76 service files

`TSS_Derived_76_Register.csv` is an unchanged copy of the existing final-register Git blob.
It is an inventory input, not a captured authority source or new operational verification.

| Field | Recorded value |
|---|---|
| Repository | GerardP515/Global-VTS |
| Original path | data/current/TSS_Derived_VTS_Final_Register.csv |
| Source branch | review/final-tss-derived-vts-register-20261001 |
| Source commit | 0de8d3247dc77caa68d699f68d753fa5e213c5e8 |
| Original Git blob | 5aa536d0f55b737750496514ce1a06653e9a6eaf |
| Imported membership | 76 service records |
| Classes retained | 67 Core; 9 Supplemental |
| Purpose | Seed one Markdown workspace per existing service |

The snapshot preserves all 17 original columns, including authority, centre, source URLs, status wording and notes.
Individual dossiers cite their own row by `service_id`; source IDs and URLs must not be paired by list position.
Resolve each source ID through the source catalogue, then obtain and inspect its actual publication.

Copying this blob does not merge the source branch or change the main registers.
Historical status and caveat text remain as recorded. This import does not decide any previously unresolved TSS outcome.
Later research must preserve the distinction between discovery inclusion, source sufficiency and publication approval.
