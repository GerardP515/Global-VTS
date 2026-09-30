# Current working registers

`TSS_VTS_MRS_Association_Register.csv` is the master: one row for each of 224 baseline TSS.
`B20_B29_Association_Rows.csv` is a generated compatibility subset, not a separate master.
`Global_VTS_TSS_Candidates_v0_2.csv` is a legacy compatibility file, not the current TSS baseline.
`VTS_Entity_Register.csv` contains typed service records, including eligible monitoring services.
`Reporting_Scheme_Register.csv` distinguishes IMO-adopted and national schemes.
`Research_Gaps.csv` and `Batch_Status.csv` govern remaining work.
`Guide_Service_Candidates.csv` is not a final guide contents list.

The old Excel inventory remains historical. These CSVs are the current research data.
Run `python3 scripts/validate_registers.py` before committing changes.
