# Guide page schema

**Purpose.** Data model for one published VTS (or coherent passage) page in the Worldwide VTS Guide.

It implements the page outline:

0. Status bar (including open notices)
1. Who
2. When
3. Which channel / method
4. What to report
5. Latest notices to mariners
6. What this entry covers
7. Directional diagrams
8. Next required action
9. Unresolved / maintenance

Plus the extra mariner fields: applicability, watch and failure, pilotage vs VTS, charts/ENC, legal basis, hours and language, secondary contact, non-VTS security reporting.

This schema is the **page layer**. It does not replace the master inventory objects (`tss`, `vts_area`, `vts_centre`, `vts_sector`, `reporting_scheme`). Those remain the system of record. A page is assembled from them.

Canonical research IDs already on `main` (`TSS-0001…`, `VTS-0004`, `VRS-0016`, …) stay as foreign keys. Do not renumber them to `{TYPE}-{RR}-{NNN}` on this page layer.

The page is an aid alongside official navigational information. It is not a replacement for it.

---

## 1. Principles

- One `guide_page` per VTS area or coherent passage. Not one page per TSS.
- First screen answers only: who, channel now, when, what to send, does it apply to this ship, open notice, next sourced action.
- A channel, call sign, trigger, applicability threshold or next-VTS name without a `source_id` is not confirmed and must not render as operational text.
- Routine VTS reports do not create a `reporting_scheme` row.
- Security reporting (UKMTO, MSTC, JMIC, NCAGS) is a `security_overlay`, never a VTS or Part I scheme on this page.
- If any linked notice-review item is open, `publication_status` cannot be `current`.
- Do not invent a next VTS. Use `no_known_requirement` or `unresolved`.

---

## 2. Page object

### 2.1 `guide_page`

One record per editorial unit shown to the mariner.

| Field | Type | Required | Notes |
|---|---|---:|---|
| `page_id` | text | Yes | Primary key. Suggested `PAGE-{existing_vts_or_scheme_id}` e.g. `PAGE-VTS-0004` |
| `title` | text | Yes | Published title |
| `page_type` | enum | Yes | `vts`, `reporting_scheme`, `vts_and_scheme`, `complex_passage`, `hold` |
| `principal_vts_id` | text | No | FK to inventory VTS. Required when `page_type` in `vts`, `vts_and_scheme` |
| `principal_scheme_id` | text | No | FK to VRS/SCH. Required when `page_type` in `reporting_scheme`, `vts_and_scheme` |
| `region_ukho` | text | Yes | UKHO section `02`–`26` |
| `legal_basis` | enum | Yes | `solas_v11`, `mandatory_territorial_sea`, `associated_voluntary`, `voluntary`, `national_mandatory`, `mixed`, `unresolved` |
| `legal_basis_text` | text | Yes | One-line sourced wording |
| `operational_status` | enum | Yes | `operational`, `planned`, `suspended`, `withdrawn`, `unresolved` |
| `publication_status` | enum | Yes | `current`, `future`, `draft`, `hold`, `withdrawn` |
| `complexity` | enum | Yes | `simple`, `intermediate`, `complex` |
| `direction_split` | enum | Yes | `none`, `reciprocal`, `sector`, `both`, `unresolved` |
| `service_hours` | text | No | `H24` or published hours |
| `languages` | text | No | Working language(s) as published |
| `aid_disclaimer` | text | Yes | Default: `Aid only. Use current official publications.` |
| `last_source_check` | date | Yes | |
| `next_review_due` | date | Yes | |
| `open_notice_count` | integer | Yes | Derived |
| `diagram_current_vs_ntm` | enum | Yes | `yes`, `no`, `unchecked` |
| `applicability_known` | enum | Yes | `yes`, `no`, `unresolved` |
| `editorial_status` | enum | Yes | `candidate`, `scoped`, `draft`, `technical_review`, `approved`, `hold`, `withdrawn` |
| `combine_or_split_reason` | text | Yes | Why these TSS/centres share one page |

**Control.** `publication_status = current` only if: `editorial_status = approved`, `open_notice_count = 0` unassessed items, `diagram_current_vs_ntm != no`, and every first-screen field has `verification_status` in `confirmed_present` or an explicit `unresolved` label rendered to the user.

---

## 3. Status bar (section 0)

Derived view. Do not store as a separate table unless needed for localisation.

| Display field | Source |
|---|---|
| Operational state | `guide_page.operational_status` |
| Last check / next review | `last_source_check`, `next_review_due` |
| Open notices | Count of `page_notice` where `page_relevance` in `current`,`future` and `assessment_status != no_effect` |
| Mandatory for this ship | Unresolved on the page; resolved in the onboard filter from `applicability_rule` |
| Diagram vs NtM | `diagram_current_vs_ntm` |
| Disclaimer | `aid_disclaimer` |

---

## 4. Who (section 1)

### 4.1 `page_identity`

| Field | Type | Required | Notes |
|---|---|---:|---|
| `page_id` | text | Yes | |
| `official_name` | text | Yes | Authority name |
| `call_sign_default` | text | No | Area default only |
| `authority` | text | Yes | Competent authority |
| `provider` | text | No | Operator if different |
| `centre_ids` | text | Yes | One or more inventory `vts_centre` IDs |
| `sector_ids` | text | No | Inventory `vts_sector` IDs listed on this page, not separate pages |
| `mmsi` | text | No | Only if published for ships |
| `source_id` | text | Yes | |
| `verification_status` | enum | Yes | `confirmed_present`, `unresolved` |

Sectors stay on this page. Do not mint a new `guide_page` per sector.

---

## 5. When, channel, report (sections 2–4)

Reuse master tables. Do not flatten into one row.

| Page section | Master table |
|---|---|
| When | `reporting_point`, `operational_action` |
| Channel / method | `vts_sector.working_vhf`, `vts_sector.calling_vhf`, `report_content.method` |
| What to report | `report_content` |
| Sequence | `operational_action.sequence` + `route_direction` |

### 5.1 Render rules

- Split inbound / outbound when any `operational_action.route_direction` is not `either`.
- Show calling VHF only when it differs from working VHF in the source.
- Show AIS/email only when `report_content.method` or an `applicability_rule` says it may replace or supplement voice.
- `required_items` must follow source order. Store IMO designators when the source uses them.

---

## 6. Applicability

Use master `applicability_rule`. Every page needs at least one rule or an explicit unresolved row.

| Field | Type | Required |
|---|---|---:|
| `rule_id` | text | Yes |
| `parent_type` | enum | Yes: `guide_page`, `vts_area`, `reporting_scheme`, `operational_action` |
| `parent_id` | text | Yes |
| `rule_type` | enum | Yes: `gross_tonnage`, `length`, `draught`, `cargo`, `passenger`, `tow`, `ship_type`, `navigational_status`, `route`, `other` |
| `operator` | enum | Yes: `>=`, `>`, `=`, `<`, `<=`, `in`, `except`, `conditional` |
| `value` | text | Yes |
| `rule_text` | text | Yes |
| `exception_text` | text | No |
| `source_id` | text | Yes |

`guide_page.applicability_known = yes` only when a sourced rule exists. The first screen must not display “all ships” unless `rule_text` says that.

---

## 7. Latest notices (section 5)

### 7.1 `page_notice`

One row per notice **assessed against this page**. Newest first on render.

| Field | Type | Required | Notes |
|---|---|---:|---|
| `page_notice_id` | text | Yes | |
| `page_id` | text | Yes | |
| `notice_id` | text | Yes | FK to master `update_notice` |
| `issuer` | enum | Yes | `UKHO`, `national_ho`, `vts_authority`, `port_authority`, `coastguard`, `IMO`, `other` |
| `notice_number` | text | Yes | Exact published number |
| `issue_date` | date | Yes | |
| `effective_from` | date | No | |
| `effective_to` | date | No | Temporary notices |
| `notice_status` | enum | Yes | `current`, `future`, `expired`, `superseded`, `cancelled` |
| `subject_class` | enum | Yes | `tss`, `vts_boundary`, `vts_channel`, `call_sign`, `reporting_point`, `report_content`, `applicability`, `sector`, `route_transition`, `diagram`, `other` |
| `change_summary` | text | Yes | One line. Not the full notice |
| `editorial_impact` | enum | Yes | `none`, `data_only`, `text`, `diagram`, `text_and_diagram`, `withdraw_or_hold` |
| `assessment_status` | enum | Yes | `unassessed`, `no_effect`, `affected`, `requires_source_check`, `superseded` |
| `source_location` | text | Yes | Official URL or publication ref |
| `assessed_on` | date | Yes | |
| `imo_prevails` | boolean | Yes | If UKHO/ALRS differs from IMO annex, IMO wins |

Priority when selecting notices: IMO instrument → authority/VTS local notice → UKHO or national HO NtM / chart correction → ALRS Vol. 6 correction.

A notice is linked only if it changes this page’s TSS, boundary, channel, call sign, point, report content, applicability, sector, transition or diagram.

### 7.2 Dated instrument (also section 9)

Use `page_notice` with `notice_status = future` for known cutovers (example: ADRIREP MSC.598(111) from 2026-12-01 0000 UTC). When that date passes, set it `current` and mark the previous instrument `superseded`.

---

## 8. Coverage (section 6)

### 8.1 `page_covers_tss`

| Field | Type | Required |
|---|---|---:|
| `page_id` | text | Yes |
| `tss_id` | text | Yes |
| `role` | enum | Yes: `primary`, `associated`, `approach`, `departure`, `context` |
| `coverage` | enum | Yes: `whole`, `part`, `approach` |
| `source_id` | text | Yes |

### 8.2 `page_covers_scheme`

| Field | Type | Required |
|---|---|---:|
| `page_id` | text | Yes |
| `scheme_id` | text | Yes |
| `role` | enum | Yes: `primary`, `associated` |
| `routine_vts_only` | boolean | Yes | `true` = no separate scheme on this page |
| `source_id` | text | Yes |

If `routine_vts_only = true`, render: `Routine VTS reports only — not a separate reporting scheme.`

---

## 9. Diagrams (section 7)

Reuse master `diagram`. Add page-level currency.

| Field | Type | Required |
|---|---|---:|
| `diagram_id` | text | Yes |
| `page_id` | text | Yes |
| `title` | text | Yes |
| `direction` | enum | Yes |
| `diagram_type` | enum | Yes: `overview`, `directional_passage`, `sector`, `reporting_point`, `transition`, `other` |
| `stale_vs_notice` | boolean | Yes | True if a `page_notice` with `editorial_impact` including `diagram` is current and unapplied |

`diagram_count` is derived. Never default to two.

---

## 10. Next required action (section 8)

Reuse master `route_transition`.

Allowed `to_action_type` values on a published page:

- `enter_vts`
- `enter_reporting_scheme`
- `sector_change`
- `next_report_point`
- `no_known_requirement`
- `unresolved`

`next_service_name`, `next_call_sign` and `next_working_vhf` are generated from the target record. Do not type them freehand.

---

## 11. Extra mariner objects

### 11.1 `watch_and_failure`

| Field | Type | Required | Notes |
|---|---|---:|---|
| `page_id` | text | Yes | |
| `listen_watch_text` | text | No | After first report |
| `no_reply_text` | text | No | Only if published |
| `vhf_fail_text` | text | No | |
| `ais_in_lieu_text` | text | No | Do not assume AIS replaces voice |
| `defect_report_required` | enum | Yes | `yes`, `no`, `unresolved` |
| `source_id` | text | Yes | |

### 11.2 `pilotage_relationship`

| Field | Type | Required |
|---|---|---:|
| `page_id` | text | Yes |
| `vts_is_pilot` | enum | Yes: `no`, `yes`, `partial`, `unresolved` |
| `pilot_frequency` | text | No |
| `handover_text` | text | No |
| `source_id` | text | Yes |

Default render if `no`: `VTS is not the pilot.`

### 11.3 `page_chart`

| Field | Type | Required |
|---|---|---:|
| `page_id` | text | Yes |
| `chart_or_enc` | text | Yes |
| `carries` | enum | Yes: `tss`, `vts_limit`, `reporting_line`, `sector`, `other` |
| `permission_status` | enum | Yes: `not_required`, `to_check`, `requested`, `granted`, `not_granted` |
| `source_id` | text | Yes |

A sketch is never `authoritative`.

### 11.4 `page_contact`

| Field | Type | Required |
|---|---|---:|
| `page_id` | text | Yes |
| `contact_type` | enum | Yes: `vhf`, `mmsi`, `telephone`, `email`, `other` |
| `value` | text | Yes |
| `published_for_ships` | boolean | Yes | False = do not render |
| `source_id` | text | Yes |

### 11.5 `security_overlay`

Separate box. Not a VTS. Not Part I.

| Field | Type | Required |
|---|---|---:|
| `page_id` | text | Yes |
| `overlay_name` | text | Yes | e.g. UKMTO, MSTC, JMIC, NCAGS |
| `overlay_type` | enum | Yes | `voluntary_security`, `military_reporting`, `other` |
| `note_text` | text | Yes | One short box |
| `source_id` | text | Yes |

Do not write `overlay_name` into `principal_scheme_id`.

---

## 12. Unresolved / maintenance (section 9)

### 12.1 `page_issue`

| Field | Type | Required |
|---|---|---:|
| `issue_id` | text | Yes |
| `page_id` | text | Yes |
| `issue_type` | enum | Yes: `research`, `instrument_change`, `contested_operator`, `geometry`, `notice_lag`, `other` |
| `summary` | text | Yes |
| `effective_on` | date | No |
| `blocks_publication` | boolean | Yes |

Notices already in `page_notice` are not copied here unless they remain unresolved after assessment.

---

## 13. First screen (required render)

Ordered fields. If any is empty, show `unresolved` rather than omitting the slot.

| Order | Slot | Source |
|---:|---|---|
| 1 | Who + call sign | `page_identity` |
| 2 | Channel now | Active `vts_sector` or scheme default |
| 3 | When to call | Next `operational_action` for the selected direction |
| 4 | What to send | Linked `report_content.required_items` |
| 5 | Applies to this ship | Filter over `applicability_rule` |
| 6 | Open notice | `open_notice_count` + newest `page_notice` one-liner |
| 7 | Next sourced action | `route_transition` or `no_known_requirement` |

---

## 14. Do not store on the page

- Full ALRS reprint or port regulations
- Weather, tide tables, berth plans
- Freehand next-VTS names
- Historical narrative except `alternate_names`
- Operator commentary on contested areas (use `page_issue` type `contested_operator`)
- Channel numbers without `source_id`

---

## 15. Mapping to work already on main

| Ready page candidate | `principal_*` | First TSS on page |
|---|---|---|
| Roca Control | `VTS-0023` + `VRS-0012` | TSS-0096 |
| Gibraltar / GIBREP | `VRS-0013` (VTS ID not minted) | TSS-0098 |
| ADRIREP block | `VRS-0015` | TSS-0105 |
| TSVTS | none minted; candidate only | TSS-0120 |
| Klang VTS / STRAITREP | `VTS-0004` + `VRS-0016` | TSS-0145 |

Banco del Hoyo, Kerch, Crimea, Jazan, Dondra, FA platform stay `editorial_status = hold`.

---

## 16. Quality-control checklist (page close)

- [ ] First-screen seven slots are filled or labelled unresolved
- [ ] Every rendered channel, call sign, trigger and threshold has a source
- [ ] Applicability is a rule row, not an adjective
- [ ] Notices assessed; none unassessed if status is current
- [ ] Diagram count comes from routes/sectors
- [ ] Next action is sourced or explicitly unknown
- [ ] Security overlay is boxed separately
- [ ] Pilotage is not merged into the VTS call
- [ ] Inventory TSS/VTS/VRS IDs are unchanged
- [ ] Page is not released as standalone shipboard guidance without technical review
