> Repository review, 30 September 2026: historical research record. Current master fields, review flags and [repository audit](../repository_review_20260930/REVIEW.md) govern readiness. A previous PASS label is not a completeness certificate.

# Stage 2 association audit: B30

### Batch
B30

### TSS reviewed
- TSS-0146 Port Klang to Port Dickson (B-V/2)
- TSS-0147 Port Dickson to Tanjung Keling (B-V/3)
- TSS-0148 Malacca to Iyu Kecil (B-V/4)
- TSS-0149 In the Singapore Strait (Main Strait) (B-V/5)
- TSS-0150 Singapore Strait (Off St. John’s Island) (B-V/6)

### Results

| TSS | VTS | Mandatory reporting | Classification |
|---|---|---|---|
| TSS-0146 Port Klang to Port Dickson | VTS-0004 Klang VTS | VRS-0016 STRAITREP (Mandatory Ship Reporting System in the Straits of Malacca and Singapore; IMO Part I I-I/16) | VTS + MRS |
| TSS-0147 Port Dickson to Tanjung Keling | VTS-0004 Klang VTS | VRS-0016 STRAITREP (Mandatory Ship Reporting System in the Straits of Malacca and Singapore; IMO Part I I-I/16) | VTS + MRS |
| TSS-0148 Malacca to Iyu Kecil | VTS-0004; VTS-0005; VTS-0006 Klang VTS; Johor VTS; Singapore VTS | VRS-0016 STRAITREP (Mandatory Ship Reporting System in the Straits of Malacca and Singapore; IMO Part I I-I/16) | VTS + MRS |
| TSS-0149 In the Singapore Strait (Main Strait) | VTS-0006 Singapore VTS | VRS-0016 STRAITREP (Mandatory Ship Reporting System in the Straits of Malacca and Singapore; IMO Part I I-I/16) | VTS + MRS |
| TSS-0150 Singapore Strait (Off St. John’s Island) | VTS-0006 Singapore VTS | VRS-0016 STRAITREP (Mandatory Ship Reporting System in the Straits of Malacca and Singapore; IMO Part I I-I/16) | VTS + MRS |

### Evidence check
Pass 2 (researcher): All positive links reopened on 29 Sep 2026: MSC.73(69) IMO PDF re-downloaded; MPA VTIS, Operational Areas and Vessels-arriving pages re-fetched (updated 28 Sep 2026); SPI 2026 (updated 17 Apr 2026) and PC 65/1998 re-downloaded and byte-identical to cached copies. TSS coordinates extracted from SPI Annexes 2-5 and compared with sector limits; Appendix 1/2 chartlets rendered and inspected. Tg Piai line side test computed for TSS-0148.

Pass 4 (coordinator): An independent checker re-opened MSC.73(69), the MPA VTIS pages (updated 28 Sep 2026), the Singapore Port Information 2026 chartlets, the 2020 DG Sea Transportation release and the Hong Kong Marine Department sources. Seven positives upheld; TSS-0148 wording corrected; Sunda and Lombok downgraded (research/stage2/pass4/chk_U_result.json).

### Duplicate check
STRAITREP (VRS-0016) is one reporting entity shared by all five TSS; VTS-sector reporting to Klang/Johor/Singapore VTS is STRAITREP, not separate MRS. Three VTS entities (Klang VTS, Johor VTS, Singapore VTS) each recorded once; VTIS West/Central/East treated as sectors/call signs of Singapore VTS, not separate services. Precautionary areas not treated as separate TSS.

Shared entities in this batch:
- VTS-0004: TSS-0146, TSS-0147, TSS-0148
- VTS-0006: TSS-0148, TSS-0149, TSS-0150
- VRS-0016: TSS-0146, TSS-0147, TSS-0148, TSS-0149, TSS-0150

### Changes made
Changes at Pass 4 (coordinator review of the research output):
- TSS-0148 vts_boundary_basis: note added: "Pass 4 correction: the eastern lane ends lie up to about 1.6 nm east of the Tg Piai to Pulau Karimun Kecil line (point 70 about 0.05 nm, 58 about 0.7 nm, 59 about 1.2 nm, 76 about 1.6 nm), so they are in Singapore VTS Sector 7." (Pass 4 correction.)
- TSS-0148 vts_name: 'Klang VTS; Johor VTS; Singapore VTS (marginal south-eastern terminus only)' -> 'Klang VTS; Johor VTS; Singapore VTS'. Pass 4 correction.

### Unresolved issues
- TSS-0146: Sector 1-6 boundaries are published only as chartlets (no coordinates); sector attribution is by chartlet reading. Parent operating body of Klang VTS (Marine Department Malaysia) supported only by a lead source; marine.gov.my unavailable (HTTP 503 / certificate error).
- TSS-0147: Sector boundaries graphical only. Parent operating body of Klang VTS supported only by lead source.
- TSS-0148: Sector 4/5 and 5/6 boundaries graphical only. Singapore VTS link is a marginal terminal overlap (editor may prefer to record Klang VTS and Johor VTS as the principal services). Operating body of Klang and Johor VTS supported only by lead source; Johor VTS centre location not stated in sources opened.

### Audit result
PASS WITH UNRESOLVED ITEMS

Sources are listed in `sources/SOURCE_REGISTER.md`. VTS entities are in `data/current/VTS_Entity_Register.csv`.
