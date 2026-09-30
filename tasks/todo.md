# FC-A: final VTS count fact-check, Europe and Mediterranean (25 TSS)

Method: research/prompts/FINAL_TSS_LINKED_VTS_COUNT_FACT_CHECK_PROMPT.md, run as three regional
macro-batches (FC-A, FC-B, FC-C) at the user's request instead of FC01 to FC14.

- [x] Sync with main; merge the B12 recheck branch (review/b12-20260930) so TSS-0058 to 0060 are ingested, not redone
- [x] Build five country-grouped research packages (F1 UK/NL, F2 Iceland/Spain, F3 Corsica/Tunisia, F4 Greece/Egypt, F5 Black Sea)
- [ ] Pass 1: primary authority research (five agents)
- [ ] Passes 2 to 4: independent source reopening, boundary check, identity/duplicate check
- [ ] Pass 5: count-impact audit and deduplication of new services against the 53
- [ ] Write data/current/Final_VTS_Count_Fact_Check.csv (69 rows, FC-A filled), Final_VTS_Count_New_Services.csv,
      audits/stage3/final_count/FC-A_VTS_Count_Audit.md; update master rows by TSS ID; add services and sources
- [ ] Validator and tests pass; commit; push; PR (merge only with approval)

## Review

(filled in when done)
