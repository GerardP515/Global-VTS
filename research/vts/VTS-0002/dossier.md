---
schema_version: 1.0-draft+greatbelt.1
vts_id: VTS-0002
study_id: PILOT-02
region_code: BAL
project_class: Core
research_state: HOLD
provenance: AUTHOR_RESEARCH_FROM_HELD_SOURCES
guide_area:
  area_id: P02-AREA
  publication_title: Great Belt VTS and BELTREP
  official_service_name: Great Belt VTS
  region_code: BAL
  countries:
  - Denmark
  associated_service_ids:
  - VTS-0002
  related_tss_ids:
  - TSS-0026
  - TSS-0027
  geographical_scope: Published BELTREP area; northbound and southbound through passages, alternative external entry
    lines, internal departure and conditional reports. Bridge and pilotage context only, not a complete passage
    plan.
  authority: Danish national competent authorities; operational service as published by Danish Defence
  provider: Danish Naval Command; Great Belt VTS, Korsør
  evidence_ids:
  - EV-IDENTITY
  - EV-PROVIDER
participation:
  applicability_as_published: Alle skibe med en bruttotonnage på 50 og derover. Alle skibe med en højde over vandoverfladen
    på 15,0 meter og derover.
  exemptions_as_published: Fritidsfartøjer med en skroglængde mindre end 15 meter eller med en bruttotonnage mindre
    end 50 er undtaget fra at deltage i meldesystemet.
  requirement_strength: MANDATORY
  rules:
    combiner: ANY
    gross_tonnage:
      operator: GE
      value: 50
    air_draught_m:
      operator: GE
      value: 15.0
  exemption_rules:
    vessel_type: PLEASURE_CRAFT
    combiner: ANY
    hull_length_m:
      operator: LT
      value: 15
    gross_tonnage:
      operator: LT
      value: 50
  state_exemptions:
  - WARSHIP
  - TROOPSHIP
  - NAVAL_AUXILIARY
  - STATE_EXCLUSIVELY_PUBLIC_NONCOMMERCIAL
  bridge_rules_scope: All ships; reporting exemption does not remove navigation provisions.
  evidence_ids:
  - EV-PART
  - EV-PLEASURE
  - EV-STATE
  - EV-BRIDGE-SCOPE
  translation_note: State-vessel exemption recorded separately; Danish phrases from §3(1)-(2), not claimed English
    verbatim wording.
boundary_vertices:
- vertex_id: P1
  published_point_number: 1
  name: Korshavn, Fyn
  latitude_as_published: 55° 36′.00 N
  longitude_as_published: 010° 38′.00 E
  evidence_ids:
  - EV-GEOMETRY
  - EV-LINES
- vertex_id: P2
  published_point_number: 2
  name: East coast of Samsø
  latitude_as_published: 55° 47′.00 N
  longitude_as_published: 010° 38′.00 E
  evidence_ids:
  - EV-GEOMETRY
  - EV-LINES
- vertex_id: P3
  published_point_number: 3
  name: Near Marthe Flak
  latitude_as_published: 56° 00′.00 N
  longitude_as_published: 010° 56′.00 E
  evidence_ids:
  - EV-GEOMETRY
  - EV-LINES
- vertex_id: P4
  published_point_number: 4
  name: Sjællands Odde
  latitude_as_published: 56° 00′.00 N
  longitude_as_published: 011° 17′.00 E
  evidence_ids:
  - EV-GEOMETRY
  - EV-LINES
- vertex_id: P5
  published_point_number: 5
  name: Gulfhavn, Stigsnæs
  latitude_as_published: 55° 12′.00 N
  longitude_as_published: 011° 15′.40 E
  evidence_ids:
  - EV-GEOMETRY
  - EV-LINES
- vertex_id: P6
  published_point_number: 6
  name: Ørespids, Omø
  latitude_as_published: 55° 08′.40 N
  longitude_as_published: 011° 09′.00 E
  evidence_ids:
  - EV-GEOMETRY
  - EV-LINES
- vertex_id: P7
  published_point_number: 7
  name: South of Ørespids
  latitude_as_published: 55° 05′.00 N
  longitude_as_published: 011° 09′.00 E
  evidence_ids:
  - EV-GEOMETRY
  - EV-LINES
- vertex_id: P8
  published_point_number: 8
  name: Snøde Øre, Langeland
  latitude_as_published: 55° 05′.00 N
  longitude_as_published: 010° 56′.10 E
  evidence_ids:
  - EV-GEOMETRY
  - EV-LINES
- vertex_id: P9
  published_point_number: 9
  name: South of Korsebølle Rev
  latitude_as_published: 55° 00′.00 N
  longitude_as_published: 010° 48′.70 E
  evidence_ids:
  - EV-GEOMETRY
  - EV-LINES
- vertex_id: P10
  published_point_number: 10
  name: Thurø Rev buoy
  latitude_as_published: 55° 01′.20 N
  longitude_as_published: 010° 44′.00 E
  evidence_ids:
  - EV-GEOMETRY
  - EV-LINES
reporting_objects:
- object_id: RW
  official_name: RW
  graphic_label: RW
  geometry_type: LINE
  geometry_as_published: Join published points 1, 2 in this order.
  vertex_ids:
  - P1
  - P2
  datum_as_published: WGS 84
  sector_id: S1
  evidence_ids:
  - EV-GEOMETRY
  - EV-LINES
  wording_basis: COORDINATE_TRANSCRIPTION_WITH_EDITORIAL_DESCRIPTION
- object_id: RN
  official_name: RN
  graphic_label: RN
  geometry_type: LINE
  geometry_as_published: Join published points 2, 3, 4 in this order.
  vertex_ids:
  - P2
  - P3
  - P4
  datum_as_published: WGS 84
  sector_id: S1
  evidence_ids:
  - EV-GEOMETRY
  - EV-LINES
  wording_basis: COORDINATE_TRANSCRIPTION_WITH_EDITORIAL_DESCRIPTION
- object_id: RS
  official_name: RS
  graphic_label: RS
  geometry_type: LINE
  geometry_as_published: Join published points 5, 6, 7, 8 in this order.
  vertex_ids:
  - P5
  - P6
  - P7
  - P8
  datum_as_published: WGS 84
  sector_id: S2
  evidence_ids:
  - EV-GEOMETRY
  - EV-LINES
  wording_basis: COORDINATE_TRANSCRIPTION_WITH_EDITORIAL_DESCRIPTION
- object_id: RSW
  official_name: RSW
  graphic_label: RSW
  geometry_type: LINE
  geometry_as_published: Join published points 9, 10 in this order.
  vertex_ids:
  - P9
  - P10
  datum_as_published: WGS 84
  sector_id: S2
  evidence_ids:
  - EV-GEOMETRY
  - EV-LINES
  wording_basis: COORDINATE_TRANSCRIPTION_WITH_EDITORIAL_DESCRIPTION
- object_id: SECTOR
  official_name: null
  graphic_label: Sector division
  geometry_type: LINE
  geometry_as_published: 55°35′.00 N within the BELTREP area.
  latitude_as_published: 55°35′.00 N
  datum_as_published: WGS 84
  sector_id: null
  evidence_ids:
  - EV-SECTOR
  - EV-GEOMETRY
  wording_basis: COORDINATE_TRANSCRIPTION_WITH_EDITORIAL_DESCRIPTION
communications:
- contact_id: S1
  recipient: Great Belt VTS
  call_sign: Belt Traffic
  communication_method: VHF voice
  calling_channel: null
  working_channel: '74'
  listening_watch:
  - '74'
  - '16'
  alternative_method: VHF10 for reserve/assistance as directed; not automatic fallback.
  evidence_ids:
  - EV-CHANNELS
  - EV-WATCH
- contact_id: S2
  recipient: Great Belt VTS
  call_sign: Belt Traffic
  communication_method: VHF voice
  calling_channel: null
  working_channel: '11'
  listening_watch:
  - '11'
  - '16'
  alternative_method: VHF10 for reserve/assistance as directed; not automatic fallback.
  evidence_ids:
  - EV-CHANNELS
  - EV-WATCH
report_types:
- report_type_id: RT-BELTREP
  official_name: BELTREP
  fields:
  - field_id: F01
    sequence: 1
    code_as_published: A
    information_required: Ship name, MMSI, call sign and IMO number where applicable.
    requirement_strength: MANDATORY
    applicability_condition: Ship name always by VHF.
    preferred_delivery_methods:
    - AIS
    - ADVANCE
    - VHF
    evidence_ids:
    - EV-F01
  - field_id: F02
    sequence: 2
    code_as_published: B
    information_required: Report date and time in UTC; six-digit DDHHMM group.
    requirement_strength: MANDATORY
    applicability_condition: null
    preferred_delivery_methods:
    - AIS
    evidence_ids:
    - EV-F02
  - field_id: F03
    sequence: 3
    code_as_published: C
    information_required: Latitude and longitude.
    requirement_strength: MANDATORY
    applicability_condition: Exact coded precision remains unresolved under G03.
    preferred_delivery_methods:
    - AIS
    evidence_ids:
    - EV-F03
    gap_ids:
    - G03
  - field_id: F04
    sequence: 4
    code_as_published: E
    information_required: True course, three digits.
    requirement_strength: MANDATORY
    applicability_condition: null
    preferred_delivery_methods:
    - AIS
    evidence_ids:
    - EV-F04
  - field_id: F05
    sequence: 5
    code_as_published: F
    information_required: Speed in knots.
    requirement_strength: MANDATORY
    applicability_condition: IMO specifies knots and tenths.
    preferred_delivery_methods:
    - AIS
    evidence_ids:
    - EV-F05
    - EV-F-SPEED
  - field_id: F06
    sequence: 6
    code_as_published: G and I
    information_required: Previous port, destination and ETA; UN/LOCODE ports via AIS and UTC ETA.
    requirement_strength: MANDATORY
    applicability_condition: null
    preferred_delivery_methods:
    - AIS
    evidence_ids:
    - EV-F06
  - field_id: F07
    sequence: 7
    code_as_published: H
    information_required: Expected entry date, UTC time and reporting line.
    requirement_strength: MANDATORY
    applicability_condition: Required when sending the relevant fields in advance.
    preferred_delivery_methods:
    - ADVANCE
    evidence_ids:
    - EV-F07
  - field_id: F08
    sequence: 8
    code_as_published: L
    information_required: Intended route using published BELTREP route identifiers.
    requirement_strength: MANDATORY
    applicability_condition: null
    preferred_delivery_methods:
    - ADVANCE
    evidence_ids:
    - EV-F08
  - field_id: F09
    sequence: 9
    code_as_published: O
    information_required: Maximum present draught in metres.
    requirement_strength: MANDATORY
    applicability_condition: null
    preferred_delivery_methods:
    - AIS
    evidence_ids:
    - EV-F09
  - field_id: F10
    sequence: 10
    code_as_published: P
    information_required: Cargo and dangerous goods; total tonnes per IMO class.
    requirement_strength: MANDATORY
    applicability_condition: Dangerous-goods detail when carried.
    preferred_delivery_methods:
    - ADVANCE
    evidence_ids:
    - EV-F10
  - field_id: F11
    sequence: 11
    code_as_published: Q or R
    information_required: Defects, damage or limitations affecting navigation/manoeuvring; pollution or dangerous
      goods lost overboard.
    requirement_strength: MANDATORY
    applicability_condition: Applicable cases always VHF; changes immediately.
    preferred_delivery_methods:
    - VHF
    evidence_ids:
    - EV-F11
  - field_id: F12
    sequence: 12
    code_as_published: T
    information_required: Contact details for obtaining cargo information.
    requirement_strength: MANDATORY
    applicability_condition: null
    preferred_delivery_methods:
    - ADVANCE
    evidence_ids:
    - EV-F12
  - field_id: F13
    sequence: 13
    code_as_published: U
    information_required: Maximum air draught in metres and deadweight tonnage, including applicable tow/floatingequipment.
    requirement_strength: MANDATORY
    applicability_condition: Always VHF, even if already sent.
    preferred_delivery_methods:
    - VHF
    evidence_ids:
    - EV-F13
  - field_id: F14
    sequence: 14
    code_as_published: W
    information_required: Total number of persons on board.
    requirement_strength: MANDATORY
    applicability_condition: 'Danish implementation: email/similar or VHF; do not rely on AIS alone.'
    preferred_delivery_methods:
    - ADVANCE
    - VHF
    evidence_ids:
    - EV-F14
    ais_only_accepted: false
  - field_id: F15
    sequence: 15
    code_as_published: X
    information_required: Bunker fuel types and estimated total tonnes per type.
    requirement_strength: MANDATORY
    applicability_condition: Ships of 1,000 GT and over only.
    preferred_delivery_methods:
    - ADVANCE
    evidence_ids:
    - EV-F15
    condition:
      parameter: gross_tonnage
      operator: GE
      value: 1000
      unit: GT
directions:
- direction_id: NB
  direction_label: Northbound
  route_variant: Through passage with alternative external entry lines
  geographical_scope: Published BELTREP area only
  vessel_applicability: See participation
  sequence_semantics: ENTRY_EVENTS_ARE_ALTERNATIVES_NOT_SUCCESSIVE_CALLS
  reporting_events:
  - event_id: NB-ENTRY-RS
    sequence: 1
    event_mode: ALTERNATIVE_ENTRY
    reporting_object_id: RS
    trigger_as_published: Entry across external reporting line RS
    timing_as_published: No later than crossing
    requirement_strength: MANDATORY
    vessel_applicability: Participating vessels after statutory exemptions
    contact_id: S2
    report_type_id: RT-BELTREP
    exceptions: Previously supplied data only through accepted methods; minimum voice retained
    subsequent_action: Sector change only if route crosses sector parallel
    evidence_ids:
    - EV-ENTRY
    - EV-MINVOICE
    - EV-DIRECTIONS
    wording_basis: AUTHOR_TRANSLATION_FROM_DANISH_ORDER
  - event_id: NB-ENTRY-RSW
    sequence: 2
    event_mode: ALTERNATIVE_ENTRY
    reporting_object_id: RSW
    trigger_as_published: Entry across external reporting line RSW
    timing_as_published: No later than crossing
    requirement_strength: MANDATORY
    vessel_applicability: Participating vessels after statutory exemptions
    contact_id: S2
    report_type_id: RT-BELTREP
    exceptions: Previously supplied data only through accepted methods; minimum voice retained
    subsequent_action: Sector change only if route crosses sector parallel
    evidence_ids:
    - EV-ENTRY
    - EV-MINVOICE
    - EV-DIRECTIONS
    wording_basis: AUTHOR_TRANSLATION_FROM_DANISH_ORDER
  common_event_ids:
  - PORT-DEPART
  - CHANGE
  delivery_option_ids:
  - ADV-SEA
  - ADV-PORT
  communications_action_ids:
  - NB-CHANGE-CHANNEL
  spread:
    spread_id: NB-SPREAD
    title: 'Great Belt VTS / BELTREP: NB'
    layout: DOUBLE_PAGE
    map_extent: null
    reporting_object_ids:
    - RS
    - RSW
    - SECTOR
    reporting_event_ids:
    - NB-ENTRY-RS
    - NB-ENTRY-RSW
    graphics_dataset_path: null
    base_material_reference: null
    reproduction_permission_record: null
- direction_id: SB
  direction_label: Southbound
  route_variant: Through passage with alternative external entry lines
  geographical_scope: Published BELTREP area only
  vessel_applicability: See participation
  sequence_semantics: ENTRY_EVENTS_ARE_ALTERNATIVES_NOT_SUCCESSIVE_CALLS
  reporting_events:
  - event_id: SB-ENTRY-RN
    sequence: 1
    event_mode: ALTERNATIVE_ENTRY
    reporting_object_id: RN
    trigger_as_published: Entry across external reporting line RN
    timing_as_published: No later than crossing
    requirement_strength: MANDATORY
    vessel_applicability: Participating vessels after statutory exemptions
    contact_id: S1
    report_type_id: RT-BELTREP
    exceptions: Previously supplied data only through accepted methods; minimum voice retained
    subsequent_action: Sector change only if route crosses sector parallel
    evidence_ids:
    - EV-ENTRY
    - EV-MINVOICE
    - EV-DIRECTIONS
    wording_basis: AUTHOR_TRANSLATION_FROM_DANISH_ORDER
  - event_id: SB-ENTRY-RW
    sequence: 2
    event_mode: ALTERNATIVE_ENTRY
    reporting_object_id: RW
    trigger_as_published: Entry across external reporting line RW
    timing_as_published: No later than crossing
    requirement_strength: MANDATORY
    vessel_applicability: Participating vessels after statutory exemptions
    contact_id: S1
    report_type_id: RT-BELTREP
    exceptions: Previously supplied data only through accepted methods; minimum voice retained
    subsequent_action: Sector change only if route crosses sector parallel
    evidence_ids:
    - EV-ENTRY
    - EV-MINVOICE
    - EV-DIRECTIONS
    wording_basis: AUTHOR_TRANSLATION_FROM_DANISH_ORDER
  common_event_ids:
  - PORT-DEPART
  - CHANGE
  delivery_option_ids:
  - ADV-SEA
  - ADV-PORT
  communications_action_ids:
  - SB-CHANGE-CHANNEL
  spread:
    spread_id: SB-SPREAD
    title: 'Great Belt VTS / BELTREP: SB'
    layout: DOUBLE_PAGE
    map_extent: null
    reporting_object_ids:
    - RN
    - RW
    - SECTOR
    reporting_event_ids:
    - SB-ENTRY-RN
    - SB-ENTRY-RW
    graphics_dataset_path: null
    base_material_reference: null
    reproduction_permission_record: null
common_reporting_events:
- event_id: PORT-DEPART
  event_mode: BEFORE_INTERNAL_DEPARTURE
  trigger_as_published: Departure from a port or anchorage inside BELTREP
  timing_as_published: Before departure
  requirement_strength: MANDATORY
  report_type_id: RT-BELTREP
  contact_selection: Applicable sector S1 or S2
  evidence_ids:
  - EV-DEPART
  - EV-DELIVERY
  gap_ids:
  - G06
  wording_basis: AUTHOR_TRANSLATION_FROM_DANISH_ORDER
- event_id: CHANGE
  event_mode: CONDITIONAL_UPDATE
  trigger_as_published: Change in navigational status or previously reported information
  timing_as_published: Immediately
  requirement_strength: MANDATORY
  report_type_id: RT-BELTREP
  subject_scope: Changed particulars; Q/R if applicable, not assumed complete repeat
  contact_selection: Applicable sector S1 or S2
  method: VHF for Q/R
  evidence_ids:
  - EV-UPDATE
  wording_basis: AUTHOR_TRANSLATION_FROM_DANISH_ORDER
communications_actions:
- action_id: NB-CHANGE-CHANNEL
  action_type: CHANNEL_CHANGE
  report_required: false
  report_type_id: null
  reporting_object_id: SECTOR
  from_contact_id: S2
  to_contact_id: S1
  condition: Only when route crosses the sector boundary
  requirement_strength: MANDATORY
  evidence_ids:
  - EV-SECTOR
  - EV-NO-TRANSFER-REPORT
- action_id: SB-CHANGE-CHANNEL
  action_type: CHANNEL_CHANGE
  report_required: false
  report_type_id: null
  reporting_object_id: SECTOR
  from_contact_id: S1
  to_contact_id: S2
  condition: Only when route crosses the sector boundary
  requirement_strength: MANDATORY
  evidence_ids:
  - EV-SECTOR
  - EV-NO-TRANSFER-REPORT
report_delivery_options:
- option_id: ADV-SEA
  report_type_id: RT-BELTREP
  requirement_strength: RECOMMENDED
  fields:
  - A
  - H
  - L
  - P
  - T
  - W
  - X
  timing: After entry into Danish EEZ, before approximate20NMVHF range
  distance_is_approximate: true
  distance_nm: 20
  whole_report_exemption: false
  evidence_ids:
  - EV-ADVANCE
- option_id: ADV-PORT
  report_type_id: RT-BELTREP
  requirement_strength: VOLUNTARY
  fields:
  - A
  - H
  - L
  - P
  - T
  - W
  - X
  timing: One hour before departure
  advance_minutes: 60
  scope: Ports/anchorages inside BELTREP or20NMVHF range
  whole_report_exemption: false
  evidence_ids:
  - EV-ADV-PORT
reporting_policy:
  minimum_voice_entry:
  - SHIP_NAME
  - MAXIMUM_AIR_DRAUGHT
  - DEADWEIGHT
  - ENTRY_LINE
  minimum_voice_internal_departure:
  - SHIP_NAME
  - MAXIMUM_AIR_DRAUGHT
  - DEADWEIGHT
  q_or_r_always_voice_if_applicable: true
  ais_accepted_codes:
  - A
  - B
  - C
  - E
  - F
  - G and I
  - O
  language: English; Danish in special circumstances
  contact_phone: +45 5837 6868
  contact_email: vts@beltrep.org
  etr:
    provider_link: https://beltrep.org/transit/
    form_verified: false
    submission_made: false
  routine_exit_report: NOT_CONFIRMED
  shipboard_radio_failure: NOT_CONFIRMED
route_codes:
  RN: Report line north
  RW: Report line west
  RS: Report line south
  RSW: Report line southwest
  DW-T3: Deep-water route Between Hatter Rev and Hatter Barn
  TSS-T5: TSS At Hatter Barn
  BE: East Bridge / Route T
  BW: West Bridge
  DW-T4: Deep-water route Off the east coast of Langeland
  RH: Route Hotel
  KAL FJ: Kalundborg Fjord anchorage
reference_context:
  functions: Information, individual assistance, anchorage recommendations; notification when assistance starts/ends.
  broadcasts: Announced on16andsector channels.
  shore_failure: Published backup provisions; current shipboard fallback not established.
  bridge_east:
    air_draught_m:
      operator: LT
      value: 65
    loa_tss_m:
      operator: GE
      value: 20
    evidence_ids:
    - EV-BRIDGE-E
  bridge_west:
    thresholds:
      combiner: ALL
      deadweight_tonnes:
        operator: LT
        value: 1000
      air_draught_m:
        operator: LT
        value: 18
    marked_spans_gt:
      operator: GE
      value: 50
    northbound_span: EASTERN
    southbound_span: WESTERN
    evidence_ids:
    - EV-BRIDGE-W
    - EV-BRIDGE-W-AND
  clearance: Mean-water-level span figures are not ship-specific clearance approval.
  under_bridge: Prior permission for listed activities.
  hatter:
    deep_water_recommended_draught_m:
      operator: GT
      value: 13
    tss_recommended_draught_m:
      operator: LE
      value: 13
  pilotage:
    route_t_recommended_draught_m:
      operator: GE
      value: 11
    inf_cargo_independent_trigger: true
    compulsory_port_pilotage: NOT_FULLY_ASSESSED
  ferries: Special crossing arrangements may be authorised; not blanket exemption.
  evidence_ids:
  - EV-FUNCTION
  - EV-BROADCAST
  - EV-FAILURE
  - EV-CLEARANCE
  - EV-UNDER-BRIDGE
  - EV-HATTER
  - EV-PILOT
  - EV-FERRY
future_changes:
- change_id: CHANGE-20261201
  source_id: P02-IMO332REV1
  adopted: '2026-05-22'
  effective_from: '2026-12-01T00:00:00Z'
  state_at_cutoff: ADOPTED_NOT_YET_EFFECTIVE
  current_field_table_includes_change: false
  affected_code: X
  addition: Applicable convention insurance and civil-liability certificate information:1992CLC,2001Bunkers,2007NairobiWRC.
  condition_scope: CERTIFICATE_APPLICABILITY_NOT_AUTOMATICALLY_BUNKER_GT_THRESHOLD
  evidence_ids:
  - EV-FUTURE
evidence:
- evidence_id: EV-IDENTITY
  source_id: P02-DK820
  snapshot_id: P02-DK820__20261003T093555Z__6fb467672a72
  source_locator: §§4–6, PDF pp.1–2
  supported_field_paths:
  - guide_area
  claim_summary: Great Belt VTS operates BELTREP; central/northern Great Belt and Hatter Barn; call sign Belt Traffic.
  wording_as_published: null
  effective_from: '2013-07-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-PROVIDER
  source_id: P02-DMA-VTS
  snapshot_id: P02-DMA-VTS__20261003T093558Z__c66ebb2ed694
  source_locator: BELTREP and SOUNDREP; Vessel Traffic Service in the Fehmarn Belt (operator paragraph)
  supported_field_paths:
  - guide_area.provider
  claim_summary: 24-hour operation; Naval Command under Danish Defence Command.
  wording_as_published: null
  effective_from: null
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-FUNCTION
  source_id: P02-DK820
  snapshot_id: P02-DK820__20261003T093555Z__6fb467672a72
  source_locator: §8(1), PDF p.2
  supported_field_paths:
  - reference_context.functions
  claim_summary: Traffic/navigation information; individual assistance with start/end notification; suitable anchorages.
  wording_as_published: null
  effective_from: '2013-07-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-PART
  source_id: P02-DK820
  snapshot_id: P02-DK820__20261003T093555Z__6fb467672a72
  source_locator: §3(1), PDF p.1
  supported_field_paths:
  - participation.rules
  claim_summary: GT >=50 OR air draught >=15.0m.
  wording_as_published: null
  effective_from: '2013-07-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-PLEASURE
  source_id: P02-DK820
  snapshot_id: P02-DK820__20261003T093555Z__6fb467672a72
  source_locator: §3(2), PDF p.1
  supported_field_paths:
  - participation.exemption_rules
  claim_summary: 'Pleasure craft: hull length <15m OR GT<50.'
  wording_as_published: null
  effective_from: '2013-07-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-STATE
  source_id: P02-DK820
  snapshot_id: P02-DK820__20261003T093555Z__6fb467672a72
  source_locator: §3(3), PDF p.1
  supported_field_paths:
  - participation.state_exemptions
  claim_summary: Specified State ships exempt from reporting, not all local navigation rules.
  wording_as_published: null
  effective_from: '2013-07-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-BRIDGE-SCOPE
  source_id: P02-DK820
  snapshot_id: P02-DK820__20261003T093555Z__6fb467672a72
  source_locator: §2(4), PDF p.1
  supported_field_paths:
  - participation.bridge_rules_scope
  claim_summary: Bridge navigation provisions §§9–13 apply to all ships.
  wording_as_published: null
  effective_from: '2013-07-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-ENTRY
  source_id: P02-DK820
  snapshot_id: P02-DK820__20261003T093555Z__6fb467672a72
  source_locator: §3(4), PDF p.1
  supported_field_paths:
  - directions[*].reporting_events
  claim_summary: Report no later than external entry-line crossing; internal departures require prior reporting.
  wording_as_published: null
  effective_from: '2013-07-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-MINVOICE
  source_id: SRC-020
  snapshot_id: SRC-020__20261003T093550Z__e2f24644816b
  source_locator: Annex §3.1.4, PDF p.4 / Annex20 p.3
  supported_field_paths:
  - reporting_policy.minimum_voice_entry
  claim_summary: Voice remains compulsory for ship name, air draught, DWT and entry line even after AIS/advance
    delivery.
  wording_as_published: null
  effective_from: '2013-07-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-DELIVERY
  source_id: P02-DK820
  snapshot_id: P02-DK820__20261003T093555Z__6fb467672a72
  source_locator: Annex2 opening provisions and W footnote, PDF pp.6–7
  supported_field_paths:
  - reporting_policy.delivery
  claim_summary: AIS fields exclude W under Danish implementation; always voice A ship name and U; Q/R voice if
    applicable.
  wording_as_published: null
  effective_from: '2013-07-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-ADVANCE
  source_id: P02-DK820
  snapshot_id: P02-DK820__20261003T093555Z__6fb467672a72
  source_locator: Annex2 supplementary procedures1–2, PDF p.7
  supported_field_paths:
  - report_delivery_options[ADV-SEA]
  claim_summary: Advance A,H,L,P,T,W,X after Danish EEZ entry and before approximate 20NM VHF range; otherwise voice
    at entry.
  wording_as_published: null
  effective_from: '2013-07-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-ADV-PORT
  source_id: P02-DK820
  snapshot_id: P02-DK820__20261003T093555Z__6fb467672a72
  source_locator: Annex2 supplementary procedure3, PDF p.7
  supported_field_paths:
  - report_delivery_options[ADV-PORT]
  claim_summary: Advance reporting one hour before departure for ports/anchorages within the 20NM VHF range.
  wording_as_published: null
  effective_from: '2013-07-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-DEPART
  source_id: P02-DK820
  snapshot_id: P02-DK820__20261003T093555Z__6fb467672a72
  source_locator: §3(4); Annex2 opening provisions, PDF pp.1,6
  supported_field_paths:
  - common_reporting_events[PORT-DEPART]
  claim_summary: Before internal departure, report by VHF; retain name and U even if advance data supplied.
  wording_as_published: null
  effective_from: '2013-07-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-UPDATE
  source_id: P02-DK820
  snapshot_id: P02-DK820__20261003T093555Z__6fb467672a72
  source_locator: Annex2 supplementary procedures4–5, PDF p.7
  supported_field_paths:
  - common_reporting_events[CHANGE]
  claim_summary: Immediate updates to navigational status or earlier particulars; Q/R always voice when applicable.
  wording_as_published: null
  effective_from: '2013-07-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-SECTOR
  source_id: P02-DK820
  snapshot_id: P02-DK820__20261003T093555Z__6fb467672a72
  source_locator: §5 and Annex1 procedure2, PDF pp.2,5
  supported_field_paths:
  - reporting_objects[SECTOR]
  - communications_actions
  claim_summary: Sector line55°35′.00N; sector1 north,sector2 south; change to appropriate channel.
  wording_as_published: null
  effective_from: '2013-07-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-NO-TRANSFER-REPORT
  source_id: SRC-020
  snapshot_id: SRC-020__20261003T093550Z__e2f24644816b
  source_locator: Annex §3.2, PDF p.4 / Annex20 p.3
  supported_field_paths:
  - communications_actions[*].report_required
  claim_summary: Sector crossing requires frequency change but no verbal report.
  wording_as_published: null
  effective_from: '2013-07-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-CHANNELS
  source_id: P02-DK820
  snapshot_id: P02-DK820__20261003T093555Z__6fb467672a72
  source_locator: Annex1 table, PDF p.5
  supported_field_paths:
  - communications
  claim_summary: Sector1 74; sector2 11;10 information/assistance/reserve;16watch/announcements.
  wording_as_published: null
  effective_from: '2013-07-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-WATCH
  source_id: P02-DK820
  snapshot_id: P02-DK820__20261003T093555Z__6fb467672a72
  source_locator: §8(2); Annex1 procedure1, PDF pp.2,5
  supported_field_paths:
  - communications[*].listening_watch
  claim_summary: Relevant working channel and16continuouswatch.
  wording_as_published: null
  effective_from: '2013-07-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-LANGUAGE
  source_id: P02-DK820
  snapshot_id: P02-DK820__20261003T093555Z__6fb467672a72
  source_locator: Annex1 procedures3–4, PDF p.5
  supported_field_paths:
  - reporting_policy.language
  claim_summary: English; Danish in special circumstances. Ship-to-ship intentions should use sector channel.
  wording_as_published: null
  effective_from: '2013-07-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-BROADCAST
  source_id: P02-DK820
  snapshot_id: P02-DK820__20261003T093555Z__6fb467672a72
  source_locator: §8(1), PDF p.2
  supported_field_paths:
  - reference_context.broadcasts
  claim_summary: Announcements on16andsector channels before designatedbroadcast channel.
  wording_as_published: null
  effective_from: '2013-07-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-PHONE
  source_id: SRC-008
  snapshot_id: SRC-008__20261003T093548Z__67f4410df043
  source_locator: Contact information and links / Great Belt VTS and links
  supported_field_paths:
  - reporting_policy.contact_phone
  claim_summary: +45 5837 6868
  wording_as_published: null
  effective_from: null
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-EMAIL
  source_id: SRC-008
  snapshot_id: SRC-008__20261003T093548Z__67f4410df043
  source_locator: Contact information and links / Great Belt VTS and links
  supported_field_paths:
  - reporting_policy.contact_email
  claim_summary: vts@beltrep.org
  wording_as_published: null
  effective_from: null
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-ETR
  source_id: SRC-008
  snapshot_id: SRC-008__20261003T093548Z__67f4410df043
  source_locator: Reporting Procedures; Expected transit request hyperlink
  supported_field_paths:
  - reporting_policy.etr
  claim_summary: Provider links ETR; minimum VHF contact stillrequired. Linkedform not substantivelyretrieved.
  wording_as_published: null
  effective_from: null
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-FAILURE
  source_id: SRC-020
  snapshot_id: SRC-020__20261003T093550Z__e2f24644816b
  source_locator: Annex §8, PDF p.10 / Annex20 p.9
  supported_field_paths:
  - reference_context.shore_failure
  claim_summary: Published shore backup and reduced capability notice provisions; no current shipboard fallback
    assumed.
  wording_as_published: null
  effective_from: '2013-07-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-GEOMETRY
  source_id: SRC-020
  snapshot_id: SRC-020__20261003T093550Z__e2f24644816b
  source_locator: Annex §§2.2–2.2.4, PDF p.3 / Annex20 p.2
  supported_field_paths:
  - boundary_vertices
  claim_summary: Ten listed points; WGS84 expressly identified. Published notation retained.
  wording_as_published: null
  effective_from: '2013-07-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-LINES
  source_id: P02-DK820
  snapshot_id: P02-DK820__20261003T093555Z__6fb467672a72
  source_locator: §4, PDF pp.1–2; Annex3-A, PDF p.9
  supported_field_paths:
  - reporting_objects
  claim_summary: RW 1-2; RN2-3-4;RS5-6-7-8;RSW9-10; preserve line geometry.
  wording_as_published: null
  effective_from: '2013-07-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-DIRECTIONS
  source_id: P02-DK820
  snapshot_id: P02-DK820__20261003T093555Z__6fb467672a72
  source_locator: Annex2 coded route examples, PDF p.8; Annex3-A, PDF p.9
  supported_field_paths:
  - directions
  claim_summary: NB and SB source examples plus boundary/sector chart. Alternative entries not successive reports.
  wording_as_published: null
  effective_from: '2013-07-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-ROUTES
  source_id: P02-DK820
  snapshot_id: P02-DK820__20261003T093555Z__6fb467672a72
  source_locator: Annex2 L and coded-route examples, PDF pp.6–8
  supported_field_paths:
  - route_codes
  claim_summary: Published identifiers describe intended route, not universal mandated track.
  wording_as_published: null
  effective_from: '2013-07-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-BRIDGE-E
  source_id: P02-DK820
  snapshot_id: P02-DK820__20261003T093555Z__6fb467672a72
  source_locator: §10(1)–(2), PDF p.2
  supported_field_paths:
  - reference_context.bridge_east
  claim_summary: Air draught<65m;LOA>=20m useTSSlanes; smallcraft/sailingdetailnotfullycovered.
  wording_as_published: null
  effective_from: '2013-07-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-BRIDGE-W
  source_id: P02-DK820
  snapshot_id: P02-DK820__20261003T093555Z__6fb467672a72
  source_locator: §12(1)–(3), PDF p.3
  supported_field_paths:
  - reference_context.bridge_west
  claim_summary: DWT<1000 andairdraught<18m;GT>=50markedspans;NB eastern/SBwestern.
  wording_as_published: null
  effective_from: '2013-07-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-BRIDGE-W-AND
  source_id: SRC-020
  snapshot_id: SRC-020__20261003T093550Z__e2f24644816b
  source_locator: Annex §6.5.1, PDF p.8 / Annex20 p.7
  supported_field_paths:
  - reference_context.bridge_west.thresholds
  claim_summary: Both DWT<1000t and air draught<18m required.
  wording_as_published: null
  effective_from: '2013-07-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-CLEARANCE
  source_id: P02-DK820
  snapshot_id: P02-DK820__20261003T093555Z__6fb467672a72
  source_locator: §§9(2),11(2)–(3), PDF pp.2–3
  supported_field_paths:
  - reference_context.clearance
  claim_summary: Span clearances at mean water level; other spans differ; not ship-specific clearanceapproval.
  wording_as_published: null
  effective_from: '2013-07-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-UNDER-BRIDGE
  source_id: P02-DK820
  snapshot_id: P02-DK820__20261003T093555Z__6fb467672a72
  source_locator: §13, PDF p.3
  supported_field_paths:
  - reference_context.under_bridge
  claim_summary: Prior VTS permission for mooring/anchoring underbridges,diving/unnecessaryoccupationunderpassages.
  wording_as_published: null
  effective_from: '2013-07-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-HATTER
  source_id: SRC-020
  snapshot_id: SRC-020__20261003T093550Z__e2f24644816b
  source_locator: Annex §§6.2.2–6.3.1, PDF p.7 / Annex20 p.6
  supported_field_paths:
  - reference_context.hatter
  claim_summary: Draught>13m deepwaterrecommendation; <=13mTSSrecommendation.
  wording_as_published: null
  effective_from: '2013-07-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-PILOT
  source_id: SRC-039
  snapshot_id: SRC-039__20261003T093551Z__6b1d9e72c57e
  source_locator: §7.3, Great Belt paragraphs3–4, PDF pp.37–38
  supported_field_paths:
  - reference_context.pilotage
  claim_summary: RouteT pilotage recommendation draught>=11m andINFcargoirrespectivesize/draught. Notcompletecompulsorypilotageassessment.
  wording_as_published: null
  effective_from: null
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-FERRY
  source_id: SRC-020
  snapshot_id: SRC-020__20261003T093550Z__e2f24644816b
  source_locator: Annex §3.6.1, PDF p.6 / Annex20 p.5
  supported_field_paths:
  - reference_context.ferries
  claim_summary: Specialreportingarrangements may beauthorised for crossingferriesinsector1; nogeneralexemption.
  wording_as_published: null
  effective_from: '2013-07-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-FUTURE
  source_id: P02-IMO332REV1
  snapshot_id: P02-IMO332REV1__20261003T093553Z__25aa10a3efd5
  source_locator: Operative paragraphs1–4, PDF p.2 / Annex29 p.1; Appendix3 X,PDF p.16 / Annex29 p.15
  supported_field_paths:
  - future_changes
  claim_summary: Revised system from2026-12-01T00:00:00Z; X adds applicable insurance/civilliabilitycertificate
    information. Not current beforethen.
  wording_as_published: null
  effective_from: '2026-12-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-F01
  source_id: P02-DK820
  snapshot_id: P02-DK820__20261003T093555Z__6fb467672a72
  source_locator: Annex2, item A, PDF p.6
  supported_field_paths:
  - report_types[RT-BELTREP].fields[F01]
  claim_summary: Ship name, MMSI, call sign and IMO number where applicable. Ship name always by VHF.
  wording_as_published: null
  effective_from: '2013-07-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-F02
  source_id: P02-DK820
  snapshot_id: P02-DK820__20261003T093555Z__6fb467672a72
  source_locator: Annex2, item B, PDF p.6
  supported_field_paths:
  - report_types[RT-BELTREP].fields[F02]
  claim_summary: Report date and time in UTC; six-digit DDHHMM group.
  wording_as_published: null
  effective_from: '2013-07-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-F03
  source_id: P02-DK820
  snapshot_id: P02-DK820__20261003T093555Z__6fb467672a72
  source_locator: Annex2, item C, PDF p.6
  supported_field_paths:
  - report_types[RT-BELTREP].fields[F03]
  claim_summary: Latitude and longitude. Exact coded precision remains unresolved under G03.
  wording_as_published: null
  effective_from: '2013-07-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-F04
  source_id: P02-DK820
  snapshot_id: P02-DK820__20261003T093555Z__6fb467672a72
  source_locator: Annex2, item E, PDF p.6
  supported_field_paths:
  - report_types[RT-BELTREP].fields[F04]
  claim_summary: True course, three digits.
  wording_as_published: null
  effective_from: '2013-07-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-F05
  source_id: P02-DK820
  snapshot_id: P02-DK820__20261003T093555Z__6fb467672a72
  source_locator: Annex2, item F, PDF p.6
  supported_field_paths:
  - report_types[RT-BELTREP].fields[F05]
  claim_summary: Speed in knots. IMO specifies knots and tenths.
  wording_as_published: null
  effective_from: '2013-07-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-F06
  source_id: P02-DK820
  snapshot_id: P02-DK820__20261003T093555Z__6fb467672a72
  source_locator: Annex2, item G and I, PDF p.6
  supported_field_paths:
  - report_types[RT-BELTREP].fields[F06]
  claim_summary: Previous port, destination and ETA; UN/LOCODE ports via AIS and UTC ETA.
  wording_as_published: null
  effective_from: '2013-07-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-F07
  source_id: P02-DK820
  snapshot_id: P02-DK820__20261003T093555Z__6fb467672a72
  source_locator: Annex2, item H, PDF p.6
  supported_field_paths:
  - report_types[RT-BELTREP].fields[F07]
  claim_summary: Expected entry date, UTC time and reporting line. Required when sending the relevant fields in
    advance.
  wording_as_published: null
  effective_from: '2013-07-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-F08
  source_id: P02-DK820
  snapshot_id: P02-DK820__20261003T093555Z__6fb467672a72
  source_locator: Annex2, item L, PDF p.6
  supported_field_paths:
  - report_types[RT-BELTREP].fields[F08]
  claim_summary: Intended route using published BELTREP route identifiers.
  wording_as_published: null
  effective_from: '2013-07-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-F09
  source_id: P02-DK820
  snapshot_id: P02-DK820__20261003T093555Z__6fb467672a72
  source_locator: Annex2, item O, PDF p.7
  supported_field_paths:
  - report_types[RT-BELTREP].fields[F09]
  claim_summary: Maximum present draught in metres.
  wording_as_published: null
  effective_from: '2013-07-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-F10
  source_id: P02-DK820
  snapshot_id: P02-DK820__20261003T093555Z__6fb467672a72
  source_locator: Annex2, item P, PDF p.7
  supported_field_paths:
  - report_types[RT-BELTREP].fields[F10]
  claim_summary: Cargo and dangerous goods; total tonnes per IMO class. Dangerous-goods detail when carried.
  wording_as_published: null
  effective_from: '2013-07-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-F11
  source_id: P02-DK820
  snapshot_id: P02-DK820__20261003T093555Z__6fb467672a72
  source_locator: Annex2, item Q or R, PDF p.7
  supported_field_paths:
  - report_types[RT-BELTREP].fields[F11]
  claim_summary: Defects, damage or limitations affecting navigation/manoeuvring; pollution or dangerous goods lost
    overboard. Applicable cases always VHF; changes immediately.
  wording_as_published: null
  effective_from: '2013-07-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-F12
  source_id: P02-DK820
  snapshot_id: P02-DK820__20261003T093555Z__6fb467672a72
  source_locator: Annex2, item T, PDF p.7
  supported_field_paths:
  - report_types[RT-BELTREP].fields[F12]
  claim_summary: Contact details for obtaining cargo information.
  wording_as_published: null
  effective_from: '2013-07-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-F13
  source_id: P02-DK820
  snapshot_id: P02-DK820__20261003T093555Z__6fb467672a72
  source_locator: Annex2, item U, PDF p.7
  supported_field_paths:
  - report_types[RT-BELTREP].fields[F13]
  claim_summary: Maximum air draught in metres and deadweight tonnage, including applicable tow/floatingequipment.
    Always VHF, even if already sent.
  wording_as_published: null
  effective_from: '2013-07-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-F14
  source_id: P02-DK820
  snapshot_id: P02-DK820__20261003T093555Z__6fb467672a72
  source_locator: Annex2, item W, PDF p.7
  supported_field_paths:
  - report_types[RT-BELTREP].fields[F14]
  claim_summary: 'Total number of persons on board. Danish implementation: email/similar or VHF; do not rely on
    AIS alone.'
  wording_as_published: null
  effective_from: '2013-07-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-F15
  source_id: P02-DK820
  snapshot_id: P02-DK820__20261003T093555Z__6fb467672a72
  source_locator: Annex2, item X, PDF p.7
  supported_field_paths:
  - report_types[RT-BELTREP].fields[F15]
  claim_summary: Bunker fuel types and estimated total tonnes per type. Ships of 1,000 GT and over only.
  wording_as_published: null
  effective_from: '2013-07-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-F-SPEED
  source_id: SRC-020
  snapshot_id: SRC-020__20261003T093550Z__e2f24644816b
  source_locator: Appendix3 F, PDF p.14 / Annex20 p.13
  supported_field_paths:
  - report_types[RT-BELTREP].fields[F05]
  claim_summary: Speedin knotsandtenths.
  wording_as_published: null
  effective_from: '2013-07-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
gaps:
- gap_id: G01
  affected_field_paths:
  - assurance
  missing_information: Complete current-notice and national amendment reconciliation
  reason: Provider and adopted instruments checked; current Danish notice series and complete ALRS amendment chain
    not obtained.
  severity: BLOCKER
  disposition: OPEN
  next_action: Obtain current notice set and corrected radio-signal entry; reconcile before release.
  resolution_evidence_ids: []
  decision_record: null
- gap_id: G02
  affected_field_paths:
  - reporting_policy
  missing_information: ETR form and acknowledgement procedure
  reason: Provider link confirmed, but captured target is a 1,125-byte application shell. Form contents and submission
    acceptance not verified.
  severity: ERROR
  disposition: OPEN
  next_action: Inspect permitted rendered form/provider instructions without submitting a report.
  resolution_evidence_ids: []
  decision_record: null
- gap_id: G03
  affected_field_paths:
  - reporting_policy
  missing_information: Position encoding
  reason: Danish Annex2 C says four/five digits; IMO Appendix3 C says five/six. No invented precision convention.
  severity: ERROR
  disposition: OPEN
  next_action: Seek current operational reporting-format clarification.
  resolution_evidence_ids: []
  decision_record: null
- gap_id: G04
  affected_field_paths:
  - assurance
  missing_information: Durable source archive and permissions
  reason: Exact originals held in temporary artefact/local workspace; artefact expires 2 November2026. Public full-copy
    republication not assessed.
  severity: BLOCKER
  disposition: OPEN
  next_action: Transfer to authorised durable source store and verify all hashes before expiry.
  resolution_evidence_ids: []
  decision_record: null
- gap_id: G05
  affected_field_paths:
  - assurance
  missing_information: Independent, marine and artwork approval
  reason: All reviews in this test are author-side; no map, PDF or named independent reviewer.
  severity: BLOCKER
  disposition: OPEN
  next_action: Review exact packet; obtain marine approval and graphic checks before release.
  resolution_evidence_ids: []
  decision_record: null
- gap_id: G06
  affected_field_paths:
  - reporting_policy
  missing_information: Exit reporting and shipboard radio-failure implementation
  reason: Reviewed scheme does not establish a complete routine exit or shipboard radio-failure sequence. No absence
    conclusion.
  severity: ERROR
  disposition: OPEN
  next_action: Confirm current provider requirements; keep unknowns qualified.
  resolution_evidence_ids: []
  decision_record: null
conflicts:
- conflict_id: C01
  subject: W transmission
  assertions:
  - source_id: SRC-020
    locator: §3.1.2,Appendix3 W
    assertion: AIS permitted for W.
  - source_id: P02-DK820
    locator: Annex2 W footnote
    assertion: Send W by email/fax/similar or VHF; AIS cannot be read under documented implementation.
  disposition: AUTHOR_RESOLVED_PENDING_INDEPENDENT_REVIEW
  decision: Use explicit national implementation; do not assert present equipment incapability as independently
    measured fact.
  evidence_ids:
  - EV-DELIVERY
  - EV-F14
- conflict_id: C02
  subject: Contact email
  assertions:
  - source_id: P02-DK820
    locator: Annex1
    assertion: beltrep@sok.dk
  - source_id: SRC-008
    locator: Contact information
    assertion: vts@beltrep.org
  disposition: AUTHOR_RESOLVED_PENDING_INDEPENDENT_REVIEW
  decision: Use live operating-provider address; historical address retained in evidence, not guide instructions.
  evidence_ids:
  - EV-EMAIL
- conflict_id: C03
  subject: English translation identifier
  assertions:
  - source_id: P02-EN820
    locator: PDF p.1 title
    assertion: Order no.8230
  - source_id: P02-DK820
    locator: PDF p.1 official heading/footer
    assertion: Order no.820
  disposition: AUTHOR_RESOLVED_PENDING_INDEPENDENT_REVIEW
  decision: Authentic Danish identifier820; English typo not silently accepted as identity. English file is comparison
    aid only.
  evidence_ids: []
- conflict_id: C04
  subject: C digit encoding
  assertions:
  - source_id: P02-DK820
    locator: Annex2 C,PDF p.6
    assertion: 4-digit N and5-digit E
  - source_id: SRC-020
    locator: Appendix3 C,PDF p.14
    assertion: 5-digit N and6-digit E
  disposition: OPEN
  decision: G03; state latitude/longitude but no invented resolution.
  evidence_ids:
  - EV-F03
assurance:
  research_cutoff_utc: '2026-10-03T09:46:53.604267+00:00'
  subsequent_notices_check: PARTIAL; provider/law/resolutions checked; complete notice/ALRS chain not obtained.
  independent_review_record: null
  marine_approval_record: null
  artwork_check_record: null
  release_record: null
  publication_ready: false
  must_reassess_before_utc: '2026-12-01T00:00:00Z'
production:
  research_revision: '0.1'
  schema_revision: 1.0-draft+greatbelt.1
  style_sheet_revision: entry-2 / professional-1
  effort_record: effort.csv
  pdf_output_paths: []
  entry_revision: 1.1-author-reproof
source_wording_policy:
  operational_english: Author translation/paraphrase except identified source coordinate strings and short Danish
    participation extracts.
  as_published_field_note: For translated event and geometry labels, _as_published denotes the source-derived requirement,
    not a claim of an English verbatim quote. See source_locator and original snapshot.
  normalisation: Coordinates retain English IMO notation. No datum transformation or new waypoint calculated.
---

# Great Belt VTS and BELTREP

**Storebælt, Denmark | Pilot 02 | Research revision 0.1 | Editorial draft: 3 October 2026**

> **DRAFT / HOLD. Not for navigation or publication.**
> This entry describes the source provisions assessed on 3 October 2026. Independent review and current-notice reconciliation remain outstanding.
> **A revised IMO reporting system takes effect at 0000 UTC on 1 December 2026.** See Section 8.

## Contents

1. [Service and operating area](#section-1)
2. [Participation and applicability](#section-2)
3. [Reporting procedures](#section-3)
4. [Information to report](#section-4)
5. [Communications and watchkeeping](#section-5)
6. [Special circumstances](#section-6)
7. [Boundaries and reporting locations](#section-7)
8. [Operational limitations](#section-8)
9. [References](#section-9)

<a id="section-1"></a>

## 1. Service and operating area

Great Belt VTS operates BELTREP, the mandatory ship-reporting system for the central and northern Great Belt. Its area includes the waters around Hatter Barn in Samsø Bælt. The service operates continuously from Korsør under the Danish Naval Command. Its radio call sign is **Belt Traffic**. [R1, §§4–6 and Annex 1](#r1) [R4, BELTREP and SOUNDREP; VTS operator](#r4)

The service supplies traffic and navigational information, provides individual navigational assistance and identifies suitable anchorages when circumstances require. Information covers matters including weather, currents, water levels, ice and changes affecting navigation. VTS advises a ship when individual navigational assistance begins and ends. [R1, §8](#r1)

BELTREP has two radio sectors, divided at **55°35′.00 N**. Sector 1 lies north of this parallel; Sector 2 lies south. The reporting area and its four external reporting lines are described in Section 7. [R1, §§4–5](#r1)

This entry covers northbound and southbound passages, alternative entry lines, internal departures, sector changes and conditional reporting. It does not provide a passage plan, port-entry guide or complete pilotage assessment.

<a id="section-2"></a>

## 2. Participation and applicability

Ships must participate when they meet **either** the gross-tonnage threshold or the air-draught threshold, subject to the exemptions below. Reporting applies to through traffic and ships using ports or anchorages within BELTREP. [R1, §3](#r1)

| Category | Participation |
| --- | --- |
| Ships of 50 GT and over | Mandatory, including exactly 50 GT, unless exempt. [R1, §3(1)](#r1) |
| Ships with an air draught of 15.0 m or more | Mandatory, including exactly 15.0 m, unless exempt. Gross tonnage need not reach 50 GT. [R1, §3(1)](#r1) |
| Pleasure craft | Exempt when hull length is below 15 m **or** gross tonnage is below 50 GT. Either condition is sufficient. [R1, §3(2)](#r1) |
| Specified State vessels | Warships, troopships and naval auxiliaries are exempt from BELTREP reporting. The exemption also covers other State-owned or State-operated ships used exclusively for public, non-commercial service. [R1, §3(3)](#r1) |

Reporting exemptions do not remove the bridge-navigation requirements. The Order applies those provisions to all ships. [R1, §2(4)](#r1)

AIS and advance reports can fulfil specified information requirements, but they do not replace the mandatory VHF contact. [R1, Annex 2, opening provisions](#r1) [R3, Reporting Procedures](#r3)

<a id="section-3"></a>

## 3. Reporting procedures

### 3.1 Before entering

BELTREP accepts reporting through a combination of current Class A AIS data, advance communication and VHF. The accepted methods differ between report fields. Section 4 identifies those differences. [R1, Annex 2](#r1)

Advance reports should include the applicable fields **L, P, T, W and X**, together with **A and H**. Email or similar communication reduces the information subsequently transmitted by VHF. The Danish instructions also accept these advance particulars by mobile telephone. [R1, Annex 2, supplementary procedure 1](#r1)

For an approaching ship, advance reports may be sent after entering the Danish exclusive economic zone. They must precede arrival within BELTREP's approximate **20 NM VHF range**. Within that range, the published alternative is VHF reporting when crossing the entry line. [R1, Annex 2, supplementary procedure 2](#r1) [R2, Annex §3.5.2](#r2)

The 20 NM distance describes approximate radio coverage, not an additional surveyed reporting boundary. The separate departure arrangement below applies to ports and anchorages within that range. [R1, Annex 2, supplementary procedures 2–3](#r1)

### 3.2 Northbound passage

Northbound ships entering across **RS** or **RSW** initially use **Sector 2, VHF 11**. An entry report is due no later than crossing the applicable external line. [R1, §§3(4)–5, Annexes 1 and 3-A](#r1)

| Stage | Required action |
| --- | --- |
| Entry across RS or RSW | Contact **Belt Traffic on VHF 11**, no later than crossing the line. [R1, §3(4), Annex 1](#r1) |
| Entry information | Give the ship's name, maximum air draught, deadweight tonnage and entry line. Supply remaining required particulars not already reported through an accepted method. [R1, Annex 2](#r1) [R2, Annex §3.1.4](#r2) |
| Crossing 55°35′.00 N northbound | Change the sector working channel from **11 to 74**. The sector crossing itself does **not** require a verbal report. [R1, Annex 1, procedure 2](#r1) [R2, Annex §3.2](#r2) |
| Continuing in Sector 1 | Maintain the required watch on **VHF 74 and 16**. Report applicable changes as described in Section 6. [R1, §8(2), Annex 2, supplementary procedure 5](#r1) |

RS and RSW are alternative entry lines, not successive reporting points. A sector change applies only where the passage crosses the sector boundary. [R1, §§4–5 and Annex 3-A](#r1)

### 3.3 Southbound passage

Southbound ships entering across **RN** or **RW** initially use **Sector 1, VHF 74**. An entry report is due no later than crossing the applicable external line. [R1, §§3(4)–5, Annexes 1 and 3-A](#r1)

| Stage | Required action |
| --- | --- |
| Entry across RN or RW | Contact **Belt Traffic on VHF 74**, no later than crossing the line. [R1, §3(4), Annex 1](#r1) |
| Entry information | Give the ship's name, maximum air draught, deadweight tonnage and entry line. Supply remaining required particulars not already reported through an accepted method. [R1, Annex 2](#r1) [R2, Annex §3.1.4](#r2) |
| Crossing 55°35′.00 N southbound | Change the sector working channel from **74 to 11**. The sector crossing itself does **not** require a verbal report. [R1, Annex 1, procedure 2](#r1) [R2, Annex §3.2](#r2) |
| Continuing in Sector 2 | Maintain the required watch on **VHF 11 and 16**. Report applicable changes as described in Section 6. [R1, §8(2), Annex 2, supplementary procedure 5](#r1) |

RN and RW are alternative entry lines. Remaining within one sector does not create a channel-transfer event. [R1, §§4–5 and Annex 3-A](#r1)

### 3.4 Departure from a port or anchorage

A participating ship must report before departure from a port or anchorage inside BELTREP. The minimum VHF particulars include the ship's name, maximum air draught and deadweight tonnage. [R1, §3(4), Annex 2, opening provisions](#r1)

For departures within the area or its 20 NM VHF range, advance reports may be sent **one hour before departure**. The advance report includes the applicable A, H, L, P, T, W and X particulars. It does not replace the VHF report required before an internal departure. [R1, Annex 2, supplementary procedure 3 and opening provisions](#r1) [R2, Annex §3.5.3](#r2)

A routine report on leaving the reporting area has not been confirmed in the reviewed instructions. This limitation does not establish an exemption from further reports requested by VTS.

<a id="section-4"></a>

## 4. Information to report

The reporting format contains **15 code groups**. Fields have different transmission methods and conditions; they are not all repeated in every radio call. [R1, Annex 2](#r1)

| Code | Information and applicable condition |
| --- | --- |
| A | Ship's name, MMSI, call sign and IMO number where applicable. The ship's name must also be given by VHF. [R1, Annex 2, A and opening provisions](#r1) |
| B | Date and time in UTC, using a six-digit day, hour and minute group. [R1, Annex 2, B](#r1) |
| C | Position in latitude and longitude. Exact coded precision requires reconciliation between the Danish and IMO formats. [R1, Annex 2, C](#r1) [R2, Appendix 3, C](#r2) |
| E | True course, expressed as three digits. [R1, Annex 2, E](#r1) |
| F | Speed in knots. The IMO format specifies knots and tenths. [R1, Annex 2, F](#r1) [R2, Appendix 3, F](#r2) |
| G and I | Previous port, destination and ETA. AIS port entries use UN/LOCODE; the ETA uses the date/time convention under B. [R1, Annex 2, G and I](#r1) |
| H | Expected entry date, UTC time and reporting line. Required when the relevant particulars are sent in advance. [R1, Annex 2, H](#r1) |
| L | Intended route through BELTREP, identified using the published route codes below. [R1, Annex 2, L](#r1) |
| O | Maximum present draught in metres. [R1, Annex 2, O](#r1) |
| P | Cargo particulars. Dangerous goods are reported by IMO class, with total tonnes for each class. [R1, Annex 2, P](#r1) |
| Q or R | Q: defects, damage or limitations affecting navigation or manoeuvring. R: pollution released or dangerous goods lost overboard. Applicable reports must use VHF. [R1, Annex 2, Q/R and supplementary procedure 4](#r1) |
| T | Address and contact particulars through which detailed cargo information can be obtained. [R1, Annex 2, T](#r1) |
| U | Maximum air draught in metres and deadweight tonnage, including relevant tows and floating equipment. Give these particulars by VHF even when previously supplied. [R1, Annex 2, U](#r1) |
| W | Total number of persons on board. Send by email or similar means, or give by VHF at entry or before internal departure. [R1, Annex 2, W and footnote](#r1) |
| X | Bunker fuel type and estimated quantity for ships of **1,000 GT and over**. Give total tonnes for each fuel type. [R1, Annex 2, X](#r1) |

The X threshold concerns **ship gross tonnage**, not the quantity of fuel carried. A ship of exactly 1,000 GT is included. [R1, Annex 2, X](#r1)

### AIS and advance information

Correct and updated Class A AIS data can supply **A, B, C, E, F, G and I, and O**. The Danish implementation directs **W** through non-AIS reporting, despite the AIS option in the IMO table. No AIS-only persons-on-board report is assumed here. [R1, Annex 2, opening provisions and W footnote](#r1)

At entry, the ship's name and U particulars remain compulsory by VHF, together with the entry line. Applicable Q or R information must also be given by VHF. Other information remains reportable when the permitted alternative method has not supplied it. [R1, Annex 2](#r1) [R2, Annex §3.1.4](#r2)

### Route codes under L

| Code | Meaning |
| --- | --- |
| RN / RW / RS / RSW | Northern, western, southern and south-western reporting lines. [R1, Annex 2, L](#r1) |
| DW-T3 | Deep-water route between Hatter Rev and Hatter Barn. [R1, Annex 2, L](#r1) |
| TSS-T5 | Traffic separation scheme At Hatter Barn. [R1, Annex 2, L](#r1) |
| BE | East Bridge, Route T. [R1, Annex 2, L](#r1) |
| BW | West Bridge. [R1, Annex 2, L](#r1) |
| DW-T4 | Deep-water route off the east coast of Langeland. [R1, Annex 2, L](#r1) |
| RH | Route Hotel. [R1, Annex 2, L](#r1) |
| KAL FJ | Kalundborg Fjord anchorage. [R1, Annex 2, L](#r1) |

The report describes the master's intended route. These codes do not prescribe a universal track through the area. [R1, Annex 2, L](#r1)

<a id="section-5"></a>

## 5. Communications and watchkeeping

| Purpose | Channel or contact |
| --- | --- |
| Radio call sign | **Belt Traffic**. [R1, §6 and Annex 1](#r1) |
| Sector 1, north of 55°35′.00 N | **VHF 74** working channel. [R1, §5 and Annex 1](#r1) |
| Sector 2, south of 55°35′.00 N | **VHF 11** working channel. [R1, §5 and Annex 1](#r1) |
| Listening watch | The applicable sector channel **and VHF 16**. [R1, §8(2) and Annex 1](#r1) |
| Information, assistance and reserve channel | **VHF 10**, as directed by VTS. [R1, Annex 1](#r1) |
| Telephone | **+45 5837 6868**. [R3, Contact information](#r3) |
| Email | **vts@beltrep.org**. [R3, Contact information](#r3) |

English is the working language; Danish may be used in special circumstances. Ship-to-ship exchanges about navigational intentions should use the relevant BELTREP working channel. [R1, Annex 1, procedures 3–4](#r1)

VTS announces broadcasts on VHF 16 and the sector channels before directing ships to the broadcast channel. [R1, §8(1)](#r1)

The provider links an **Expected Transit Request (ETR)** service. Its current form, required fields and acknowledgement procedure were not accessible for verification. No report was submitted during this research. The published VHF reporting duties remain applicable. [R3, Reporting Procedures and ETR link](#r3)

The IMO scheme provides standby arrangements and notices of reduced VTS capability following equipment failure. Shipboard radio-failure procedures require separate current confirmation; no substitute calling sequence is supplied here. [R2, Annex §8](#r2)

<a id="section-6"></a>

## 6. Special circumstances

### Changes, defects and pollution

The master must inform Great Belt VTS immediately when navigational status or previously reported information changes. Q or R reports must be transmitted by VHF. This duty applies during either direction of passage. [R1, Annex 2, supplementary procedures 4–5](#r1)

These are conditional reports. They are separate from the channel change at the sector boundary. [R1, Annex 1, procedure 2; Annex 2, supplementary procedures 4–5](#r1)

### Bridge passages

| Passage | Principal restrictions |
| --- | --- |
| East Bridge, BE | Air draught must be **less than 65.00 m**. Ships of 20 m LOA and over must use the TSS lanes between Korsør and Sprogø. [R1, §10(1)–(2)](#r1) |
| West Bridge, BW | Deadweight must be **below 1,000 tonnes** and air draught **below 18.00 m**. Ships of 50 GT and over must use the marked navigation spans. [R1, §12(1)–(2)](#r1) [R2, Annex §6.5.1](#r2) |
| West Bridge, direction | Northbound ships use the eastern navigation span; southbound ships use the western span. [R1, §12(3)](#r1) |

The bridge-height figures are not a vessel-specific clearance calculation. Published span clearances are referenced to mean water level, and the remaining spans have different clearances. [R1, §§9(2) and 11(2)–(3)](#r1)

Mooring to either bridge or anchoring beneath it requires prior VTS permission. The same applies to diving or unnecessary occupation of the navigation passages beneath either bridge. [R1, §13](#r1)

This summary does not reproduce every span restriction, fishing prohibition or local crossing restriction. Small-craft and sailing-vessel arrangements require the complete bridge provisions and current instructions.

### Routeing and pilotage context

Ships drawing more than **13 m** should use the deep-water route between Hatter Rev and Hatter Barn. The IMO scheme recommends the At Hatter Barn TSS for ships drawing **13 m or less**. These are draught-dependent routeing recommendations, not reporting exemptions. [R2, Annex §§6.2.2–6.3.1](#r2)

The national guide reproduces the recommendation for local pilotage on Route T for ships drawing **11 m or more**. It also covers ships carrying INF-Code materials irrespective of size or draught. Port-bound compulsory pilotage requires a separate assessment. [R5, §7.3, Great Belt paragraphs 3–4, PDF pages 37–38](#r5)

Special reporting arrangements may be authorised for ferries crossing Sector 1. This is not a general ferry exemption. [R2, Annex §3.6.1](#r2)

<a id="section-7"></a>

## 7. Boundaries and reporting locations

The published reporting geometry uses **WGS 84**. External lines connect the points in the listed order. These are reporting boundaries, not passage waypoints. [R1, §4](#r1) [R2, Annex §2.2](#r2)

| Line | Ordered points | Geographical description |
| --- | --- | --- |
| RW | 1 → 2 | Fyn to the east coast of Samsø. [R1, §4](#r1) |
| RN | 2 → 3 → 4 | Samsø, the vicinity of Marthe Flak, and Sjællands Odde. [R1, §4](#r1) |
| RS | 5 → 6 → 7 → 8 | Stigsnæs, Omø and eastern Langeland. [R1, §4](#r1) |
| RSW | 9 → 10 | Western Langeland to Thurø Rev buoy. [R1, §4](#r1) |

| Point | Reference | Latitude | Longitude |
| --- | --- | --- | --- |
| 1 | Korshavn, Fyn | 55° 36′.00 N | 010° 38′.00 E. [R1, §4](#r1) [R2, §2.2](#r2) |
| 2 | East coast of Samsø | 55° 47′.00 N | 010° 38′.00 E. [R1, §4](#r1) [R2, §2.2](#r2) |
| 3 | Near Marthe Flak | 56° 00′.00 N | 010° 56′.00 E. [R1, §4](#r1) [R2, §2.2](#r2) |
| 4 | Sjællands Odde | 56° 00′.00 N | 011° 17′.00 E. [R1, §4](#r1) [R2, §2.2](#r2) |
| 5 | Gulfhavn, Stigsnæs | 55° 12′.00 N | 011° 15′.40 E. [R1, §4](#r1) [R2, §2.2](#r2) |
| 6 | Ørespids, Omø | 55° 08′.40 N | 011° 09′.00 E. [R1, §4](#r1) [R2, §2.2](#r2) |
| 7 | South of Ørespids | 55° 05′.00 N | 011° 09′.00 E. [R1, §4](#r1) [R2, §2.2](#r2) |
| 8 | Snøde Øre, Langeland | 55° 05′.00 N | 010° 56′.10 E. [R1, §4](#r1) [R2, §2.2](#r2) |
| 9 | South of Korsebølle Rev | 55° 00′.00 N | 010° 48′.70 E. [R1, §4](#r1) [R2, §2.2](#r2) |
| 10 | Thurø Rev buoy | 55° 01′.20 N | 010° 44′.00 E. [R1, §4](#r1) [R2, §2.2](#r2) |

**Position references:** R1 §4, PDF pages 1–2; R2 Annex §§2.2.1–2.2.4, PDF page 3. The E longitude notation follows the English IMO source. [R1, §4](#r1) [R2, Annex §2.2](#r2)

The sector boundary is the parallel **55°35′.00 N** within the reporting area. Crossing it requires a channel change, not a routine verbal report. [R1, §5 and Annex 1](#r1) [R2, Annex §3.2](#r2)

**No plotting approval is given.** Current chart corrections, feature positions and graphic checks remain outstanding. No operational map has been produced.

<a id="section-8"></a>

## 8. Operational limitations

### Change taking effect on 1 December 2026

Resolution **MSC.332(90)/Rev.1** replaces the existing IMO system at **0000 UTC on 1 December 2026**. Its revised X field adds applicable convention insurance and civil-liability certificate information. The instruments identified are the 1992 CLC, 2001 Bunkers Convention and 2007 Nairobi WRC. [R6, operative paragraphs 1–4; Appendix 3, X](#r6)

That addition is not included in the current X field above. This entry requires revision before the implementation date. The certificate provisions have their own applicability; they must not inherit the bunker-reporting threshold automatically. [R6, operative paragraph 2; Appendix 3, X](#r6)

### Outstanding verification

Full reconciliation with current Danish notices, radio-signal publications and the national amendment history remains outstanding. The ETR workflow, precise position encoding, routine exit reporting and shipboard communication-failure arrangements require confirmation.

The source geometry has been transcribed, but not approved for use in a navigational graphic. Independent evidence review, marine approval and publication approval have not been completed.

<a id="section-9"></a>

## 9. References

All sources below were accessed on **3 October 2026**. Access dates do not establish that every subsequent notice has been checked. PDF page numbers refer to file order. Danish provisions are translated or paraphrased for this entry; the Danish text remains authoritative.

<a id="r1"></a>

**R1. Danish Maritime Authority.** *Bekendtgørelse om skibsmeldesystemet BELTREP og sejlads under Østbroen og Vestbroen i Storebælt.* Order no. 820, 26 June 2013, effective 1 July 2013. Principal sources: §§2–13; Annexes 1–3. [Authentic Danish Order](https://www.retsinformation.dk/eli/lta/2013/820/pdf).

<a id="r2"></a>

**R2. International Maritime Organization.** Resolution *MSC.332(90)*, adopted 22 May 2012. Amended BELTREP system implemented 1 July 2013. Cited provisions: Annex §§2–6 and 8; Appendices 1–3. [Resolution](https://wwwcdn.imo.org/localresources/en/KnowledgeCentre/IndexofIMOResolutions/MSCResolutions/MSC.332(90).pdf).

<a id="r3"></a>

**R3. Danish Defence, Royal Danish Navy.** *BELTREP – Reporting Procedures.* Provider webpage; publication date not stated. Cited sections: Reporting Procedures, Participating Vessels, Contact information and links. [Provider instructions](https://www.forsvaret.dk/da/organisation/soevaernet/civile-opgaver/beltrep/).

<a id="r4"></a>

**R4. Danish Maritime Authority.** *Mandatory Ship Reporting Systems (MSRS) and Vessel Traffic Services (VTS).* Official overview; publication date not stated. Used for continuous operation and current VTS operator. [Official overview](https://www.dma.dk/safety-at-sea/safety-of-navigation/mandatory-ship-reporting-systems-msrs-and-vessel-traffic-services-vts).

<a id="r5"></a>

**R5. Danish Emergency Management Agency.** *Navigation Through Danish Waters*, version 16.0, February 2025. Cited provision: §7.3, Great Belt recommendations, PDF pages 37–38. [National navigation guide](https://www.soefartsstyrelsen.dk/Media/638743469510433298/Navigation%20through%20Danish%20Water%20version%2016.0%202025.pdf).

<a id="r6"></a>

**R6. International Maritime Organization.** Resolution *MSC.332(90)/Rev.1*, adopted 22 May 2026. Implementation: 0000 UTC, 1 December 2026. Used for the future-change notice only, not current reporting instructions. [Revised resolution](https://wwwcdn.imo.org/localresources/en/KnowledgeCentre/IndexofIMOResolutions/MSCResolutions/MSC.332(90)%20Rev.1.pdf).

## Appendix A. Editorial evidence and review record

Scope: author research and workflow test. No independent or marine approval. The current user instruction authorises this second writing pilot before artwork gates are complete.

### A1. Source and storage record

Nine responses were captured; eight contain usable documents. The ETR response is a shell, not a verified form. Exact originals and mechanical derivatives are in Actions artefact 11270632198, expiring 2 November 2026; see source_catalogue.json.

### A2. Evidence ledger

| Evidence | Source | Exact locator | Supported subject |
| --- | --- | --- | --- |
| EV-IDENTITY | P02-DK820 | §§4–6, PDF pp.1–2 | Great Belt VTS operates BELTREP; central/northern Great Belt and Hatter Barn; call sign Belt Traffic. |
| EV-PROVIDER | P02-DMA-VTS | BELTREP and SOUNDREP; Vessel Traffic Service in the Fehmarn Belt (operator paragraph) | 24-hour operation; Naval Command under Danish Defence Command. |
| EV-FUNCTION | P02-DK820 | §8(1), PDF p.2 | Traffic/navigation information; individual assistance with start/end notification; suitable anchorages. |
| EV-PART | P02-DK820 | §3(1), PDF p.1 | GT >=50 OR air draught >=15.0m. |
| EV-PLEASURE | P02-DK820 | §3(2), PDF p.1 | Pleasure craft: hull length <15m OR GT<50. |
| EV-STATE | P02-DK820 | §3(3), PDF p.1 | Specified State ships exempt from reporting, not all local navigation rules. |
| EV-BRIDGE-SCOPE | P02-DK820 | §2(4), PDF p.1 | Bridge navigation provisions §§9–13 apply to all ships. |
| EV-ENTRY | P02-DK820 | §3(4), PDF p.1 | Report no later than external entry-line crossing; internal departures require prior reporting. |
| EV-MINVOICE | SRC-020 | Annex §3.1.4, PDF p.4 / Annex20 p.3 | Voice remains compulsory for ship name, air draught, DWT and entry line even after AIS/advance delivery. |
| EV-DELIVERY | P02-DK820 | Annex2 opening provisions and W footnote, PDF pp.6–7 | AIS fields exclude W under Danish implementation; always voice A ship name and U; Q/R voice if applicable. |
| EV-ADVANCE | P02-DK820 | Annex2 supplementary procedures1–2, PDF p.7 | Advance A,H,L,P,T,W,X after Danish EEZ entry and before approximate 20NM VHF range; otherwise voice at entry. |
| EV-ADV-PORT | P02-DK820 | Annex2 supplementary procedure3, PDF p.7 | Advance reporting one hour before departure for ports/anchorages within the 20NM VHF range. |
| EV-DEPART | P02-DK820 | §3(4); Annex2 opening provisions, PDF pp.1,6 | Before internal departure, report by VHF; retain name and U even if advance data supplied. |
| EV-UPDATE | P02-DK820 | Annex2 supplementary procedures4–5, PDF p.7 | Immediate updates to navigational status or earlier particulars; Q/R always voice when applicable. |
| EV-SECTOR | P02-DK820 | §5 and Annex1 procedure2, PDF pp.2,5 | Sector line55°35′.00N; sector1 north,sector2 south; change to appropriate channel. |
| EV-NO-TRANSFER-REPORT | SRC-020 | Annex §3.2, PDF p.4 / Annex20 p.3 | Sector crossing requires frequency change but no verbal report. |
| EV-CHANNELS | P02-DK820 | Annex1 table, PDF p.5 | Sector1 74; sector2 11;10 information/assistance/reserve;16watch/announcements. |
| EV-WATCH | P02-DK820 | §8(2); Annex1 procedure1, PDF pp.2,5 | Relevant working channel and16continuouswatch. |
| EV-LANGUAGE | P02-DK820 | Annex1 procedures3–4, PDF p.5 | English; Danish in special circumstances. Ship-to-ship intentions should use sector channel. |
| EV-BROADCAST | P02-DK820 | §8(1), PDF p.2 | Announcements on16andsector channels before designatedbroadcast channel. |
| EV-PHONE | SRC-008 | Contact information and links / Great Belt VTS and links | +45 5837 6868 |
| EV-EMAIL | SRC-008 | Contact information and links / Great Belt VTS and links | vts@beltrep.org |
| EV-ETR | SRC-008 | Reporting Procedures; Expected transit request hyperlink | Provider links ETR; minimum VHF contact stillrequired. Linkedform not substantivelyretrieved. |
| EV-FAILURE | SRC-020 | Annex §8, PDF p.10 / Annex20 p.9 | Published shore backup and reduced capability notice provisions; no current shipboard fallback assumed. |
| EV-GEOMETRY | SRC-020 | Annex §§2.2–2.2.4, PDF p.3 / Annex20 p.2 | Ten listed points; WGS84 expressly identified. Published notation retained. |
| EV-LINES | P02-DK820 | §4, PDF pp.1–2; Annex3-A, PDF p.9 | RW 1-2; RN2-3-4;RS5-6-7-8;RSW9-10; preserve line geometry. |
| EV-DIRECTIONS | P02-DK820 | Annex2 coded route examples, PDF p.8; Annex3-A, PDF p.9 | NB and SB source examples plus boundary/sector chart. Alternative entries not successive reports. |
| EV-ROUTES | P02-DK820 | Annex2 L and coded-route examples, PDF pp.6–8 | Published identifiers describe intended route, not universal mandated track. |
| EV-BRIDGE-E | P02-DK820 | §10(1)–(2), PDF p.2 | Air draught<65m;LOA>=20m useTSSlanes; smallcraft/sailingdetailnotfullycovered. |
| EV-BRIDGE-W | P02-DK820 | §12(1)–(3), PDF p.3 | DWT<1000 andairdraught<18m;GT>=50markedspans;NB eastern/SBwestern. |
| EV-BRIDGE-W-AND | SRC-020 | Annex §6.5.1, PDF p.8 / Annex20 p.7 | Both DWT<1000t and air draught<18m required. |
| EV-CLEARANCE | P02-DK820 | §§9(2),11(2)–(3), PDF pp.2–3 | Span clearances at mean water level; other spans differ; not ship-specific clearanceapproval. |
| EV-UNDER-BRIDGE | P02-DK820 | §13, PDF p.3 | Prior VTS permission for mooring/anchoring underbridges,diving/unnecessaryoccupationunderpassages. |
| EV-HATTER | SRC-020 | Annex §§6.2.2–6.3.1, PDF p.7 / Annex20 p.6 | Draught>13m deepwaterrecommendation; <=13mTSSrecommendation. |
| EV-PILOT | SRC-039 | §7.3, Great Belt paragraphs3–4, PDF pp.37–38 | RouteT pilotage recommendation draught>=11m andINFcargoirrespectivesize/draught. Notcompletecompulsorypilotageassessment. |
| EV-FERRY | SRC-020 | Annex §3.6.1, PDF p.6 / Annex20 p.5 | Specialreportingarrangements may beauthorised for crossingferriesinsector1; nogeneralexemption. |
| EV-FUTURE | P02-IMO332REV1 | Operative paragraphs1–4, PDF p.2 / Annex29 p.1; Appendix3 X,PDF p.16 / Annex29 p.15 | Revised system from2026-12-01T00:00:00Z; X adds applicable insurance/civilliabilitycertificate information. Not current beforethen. |
| EV-F01 | P02-DK820 | Annex2, item A, PDF p.6 | Ship name, MMSI, call sign and IMO number where applicable. Ship name always by VHF. |
| EV-F02 | P02-DK820 | Annex2, item B, PDF p.6 | Report date and time in UTC; six-digit DDHHMM group. |
| EV-F03 | P02-DK820 | Annex2, item C, PDF p.6 | Latitude and longitude. Exact coded precision remains unresolved under G03. |
| EV-F04 | P02-DK820 | Annex2, item E, PDF p.6 | True course, three digits. |
| EV-F05 | P02-DK820 | Annex2, item F, PDF p.6 | Speed in knots. IMO specifies knots and tenths. |
| EV-F06 | P02-DK820 | Annex2, item G and I, PDF p.6 | Previous port, destination and ETA; UN/LOCODE ports via AIS and UTC ETA. |
| EV-F07 | P02-DK820 | Annex2, item H, PDF p.6 | Expected entry date, UTC time and reporting line. Required when sending the relevant fields in advance. |
| EV-F08 | P02-DK820 | Annex2, item L, PDF p.6 | Intended route using published BELTREP route identifiers. |
| EV-F09 | P02-DK820 | Annex2, item O, PDF p.7 | Maximum present draught in metres. |
| EV-F10 | P02-DK820 | Annex2, item P, PDF p.7 | Cargo and dangerous goods; total tonnes per IMO class. Dangerous-goods detail when carried. |
| EV-F11 | P02-DK820 | Annex2, item Q or R, PDF p.7 | Defects, damage or limitations affecting navigation/manoeuvring; pollution or dangerous goods lost overboard. Applicable cases always VHF; changes immediately. |
| EV-F12 | P02-DK820 | Annex2, item T, PDF p.7 | Contact details for obtaining cargo information. |
| EV-F13 | P02-DK820 | Annex2, item U, PDF p.7 | Maximum air draught in metres and deadweight tonnage, including applicable tow/floatingequipment. Always VHF, even if already sent. |
| EV-F14 | P02-DK820 | Annex2, item W, PDF p.7 | Total number of persons on board. Danish implementation: email/similar or VHF; do not rely on AIS alone. |
| EV-F15 | P02-DK820 | Annex2, item X, PDF p.7 | Bunker fuel types and estimated total tonnes per type. Ships of 1,000 GT and over only. |
| EV-F-SPEED | SRC-020 | Appendix3 F, PDF p.14 / Annex20 p.13 | Speedin knotsandtenths. |

### A3. Open gaps

**G01: Complete current-notice and national amendment reconciliation (BLOCKER, OPEN).** Provider and adopted instruments checked; current Danish notice series and complete ALRS amendment chain not obtained. Next action: Obtain current notice set and corrected radio-signal entry; reconcile before release.

**G02: ETR form and acknowledgement procedure (ERROR, OPEN).** Provider link confirmed, but captured target is a 1,125-byte application shell. Form contents and submission acceptance not verified. Next action: Inspect permitted rendered form/provider instructions without submitting a report.

**G03: Position encoding (ERROR, OPEN).** Danish Annex2 C says four/five digits; IMO Appendix3 C says five/six. No invented precision convention. Next action: Seek current operational reporting-format clarification.

**G04: Durable source archive and permissions (BLOCKER, OPEN).** Exact originals held in temporary artefact/local workspace; artefact expires 2 November2026. Public full-copy republication not assessed. Next action: Transfer to authorised durable source store and verify all hashes before expiry.

**G05: Independent, marine and artwork approval (BLOCKER, OPEN).** All reviews in this test are author-side; no map, PDF or named independent reviewer. Next action: Review exact packet; obtain marine approval and graphic checks before release.

**G06: Exit reporting and shipboard radio-failure implementation (ERROR, OPEN).** Reviewed scheme does not establish a complete routine exit or shipboard radio-failure sequence. No absence conclusion. Next action: Confirm current provider requirements; keep unknowns qualified.

### A4. Source discrepancies

**C01: W transmission (AUTHOR_RESOLVED_PENDING_INDEPENDENT_REVIEW).** Use explicit national implementation; do not assert present equipment incapability as independently measured fact.

**C02: Contact email (AUTHOR_RESOLVED_PENDING_INDEPENDENT_REVIEW).** Use live operating-provider address; historical address retained in evidence, not guide instructions.

**C03: English translation identifier (AUTHOR_RESOLVED_PENDING_INDEPENDENT_REVIEW).** Authentic Danish identifier820; English typo not silently accepted as identity. English file is comparison aid only.

**C04: C digit encoding (OPEN).** G03; state latitude/longitude but no invented resolution.

### A5. Review boundary

The five-stage prompt assumes existing independent findings. None exists for this new pilot. Author findings and two author-side re-proofs are recorded separately; the independent stage remains NOT_STARTED. Source acquisition, rendering and hashing ran in the recorded Actions job. Semantic research, original writing and language review are not automated by that job.

A provisional prose workspace was drafted before the YAML ledger was serialised. The first committed dossier is reconciled to the ledger. This ordering deviation is recorded for the workflow test; future jobs should require a committed evidence-first checkpoint.
