# URGENT — restore `VTS_Entity_Register.csv`

**What happened (30 September 2026).**  
A splice attempt wrote the literal string `PLACEHOLDER` over `data/current/VTS_Entity_Register.csv` (commit `ffa025d8`). The 53-row master list is not in HEAD.

**The file is intact in git history.** Last good copy:

- Commit: `dc6cff48609f07c5e7f7737f40f95f4baeaca6f0`
- Blob SHA: `61d2ed19c736329d09e61e587b55373f70cfb6fe`
- Raw: https://raw.githubusercontent.com/GerardP515/Global-VTS/dc6cff48609f07c5e7f7737f40f95f4baeaca6f0/data/current/VTS_Entity_Register.csv

**Restore locally, then append VTS-0300:**

```bash
curl -fsSL -o data/current/VTS_Entity_Register.csv \
  https://raw.githubusercontent.com/GerardP515/Global-VTS/dc6cff48609f07c5e7f7737f40f95f4baeaca6f0/data/current/VTS_Entity_Register.csv
tail -n +2 data/current/VTS_0300_Entity_Row.csv >> data/current/VTS_Entity_Register.csv
# expect 54 VTS rows + header
```

Or:

```bash
git checkout dc6cff48609f07c5e7f7737f40f95f4baeaca6f0 -- data/current/VTS_Entity_Register.csv
tail -n +2 data/current/VTS_0300_Entity_Row.csv >> data/current/VTS_Entity_Register.csv
```

Then commit that file. Also append `data/current/TSS-0217_VTS-0300_Relationship.csv` (minus header) to `TSS_Service_Relationships.csv`.

VTS-0300 identity files were not damaged:
- `data/current/VTS_0300_Entity_Row.csv`
- `data/current/TSS-0217_VTS-0300_Relationship.csv`
- `audits/FC-B_VTS-0300_Mint.md`
