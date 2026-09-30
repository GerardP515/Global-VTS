# FC-A: final VTS count fact-check, Europe and Mediterranean (25 TSS)

Method: research/prompts/FINAL_TSS_LINKED_VTS_COUNT_FACT_CHECK_PROMPT.md, run as three regional
macro-batches (FC-A, FC-B, FC-C) at the user's request instead of FC01 to FC14.

- [x] Sync with main; merge the B12 recheck branch (review/b12-20260930) so TSS-0058 to 0060 are ingested, not redone
- [x] Build five country-grouped research packages (F1 UK/NL, F2 Iceland/Spain, F3 Corsica/Tunisia, F4 Greece/Egypt, F5 Black Sea)
- [x] Pass 1: primary authority research (five agents)
- [x] Passes 2 to 4: independent source reopening, boundary check, identity/duplicate check
- [x] Pass 5: count-impact audit and deduplication of new services against the 53
- [x] Write data/current/Final_VTS_Count_Fact_Check.csv (69 rows, FC-A filled), Final_VTS_Count_New_Services.csv,
      audits/stage3/final_count/FC-A_VTS_Count_Audit.md; update master rows by TSS ID; add services and sources
- [x] Validator and tests pass; commit; push; PR (merge only with approval)

## Review

FC-A (25 TSS): 3 existing service (VTS-0044, from the B12 recheck), 2 new core (VTS-0210 Kerch Strait VTS,
VTS-0211 Delta-Lotsman VTS), 3 records on 2 new supplemental services (VTS-0212 Iceland MTS, VTS-0213 CROSS Med /
Corsica sémaphores), 3 no service (Off Skerries, Liverpool Bay, Thessaloniki), 14 unresolved.
Running count: 53 + 2 core + 2 supplemental = 57 identities (not final; FC-B and FC-C pending).
Project owner decisions: decision 6 (disputed-jurisdiction services counted, flagged); Iceland MTS supplemental.
Checker corrections: Liverpool Bay to no service (1971 Act limit); Corsica to supplemental; Odesa to new service
(Order 655 consolidated 2025). Another AI's FC-B audits landed on main during this work (audits only, no ID clash).

# Double-check of disputed and marginal VTS negatives (decision 7)

- [x] Record decision 7: include by default on conflict
- [ ] Triage the whole register for marginal or disputed removals and no-VTS results
- [ ] Independent double-check per country group; apply decision 7
- [ ] Update register, fact-check table and audit; validator and tests; commit to the FC-A PR
