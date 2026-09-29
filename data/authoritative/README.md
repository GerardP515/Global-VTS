# Authoritative IMO 2025 Baseline

This folder contains the Global VTS project baseline derived from the attached IMO *Ships’ Routeing 2025 Edition*.

## Files

- `IMO_2025_Part_B_Parent_Inventory.csv` — 164 Part B indexed parent entries.
- `IMO_2025_Individual_TSS_Inventory.csv` — 224 named or explicitly enumerated TSS research entities.
- `IMO_2025_Mandatory_Reporting_Systems.csv` — 23 Part I mandatory ship reporting systems.

## Scope rule

The TSS inventory splits parent entries where the IMO text names or explicitly enumerates distinct TSS. Internal parts or lane groups are not automatically treated as separate research entities.

The v0.2 candidate register is retained as legacy material and is reconciled through the crosswalk under `research/reconciliation/`.