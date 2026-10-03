---
schema_version: 1.0-draft+channel.1
vts_id: VTS-0001
study_id: PILOT-01
region_code: BIS
project_class: Core
research_state: HOLD
provenance: MIXED_HELD_AND_LIVE_SOURCE_RESEARCH
guide_area:
  area_id: P01-AREA
  publication_title: 'Channel VTS / CALDOVREP: directional reporting research sample'
  official_service_name: Channel VTS
  region_code: BIS
  countries:
  - United Kingdom
  - France
  associated_service_ids:
  - VTS-0001
  related_tss_ids:
  - TSS-0038
  geographical_scope: Standard NE-bound and SW-bound through-transits, approach reporting, conditional navigation
    changes and English ITZ notification. Special-operation variants are outside this sample, not exempt from their
    rules.
  authority: UK and French maritime authorities; current administrative titles require publication review.
  provider: Dover MRCC and CROSS Gris-Nez
  evidence_ids:
  - EV-IDENTITY
participation:
  applicability_as_published: All vessels of 300GT and over
  exemptions_as_published: Whatever their nationality, naval vessels are also exempt from reporting
  requirement_strength: MANDATORY
  evidence_ids:
  - EV-THRESHOLD
  - EV-EXEMPT
reporting_objects:
- object_id: OBJ-WEST
  official_name: null
  graphic_label: Western reporting line
  geometry_type: LINE
  geometry_as_published: Line from the Royal Sovereign light tower, through the Bassurelle Light Buoy (at its assigned
    position of 50°32’.8N, 000°57’.8E) to the coast of France.
  datum_as_published: null
  sector_id: null
  evidence_ids:
  - EV-NE
- object_id: OBJ-EAST
  official_name: null
  graphic_label: Eastern reporting line
  geometry_type: LINE
  geometry_as_published: Line drawn from North Foreland Light (51° 23’N; 001° 27’E) to the border between France
    and Belgium (51° 05’N; 002° 33’E).
  datum_as_published: null
  sector_id: null
  evidence_ids:
  - EV-SW
communications:
- contact_id: COM-GRISNEZ
  recipient: CROSS Gris-Nez
  call_sign: Gris-Nez Traffic
  communication_method: VHF voice
  calling_channel: '13'
  working_channel: null
  listening_watch: null
  alternative_method: null
  evidence_ids:
  - EV-NE
  - EV-CARGO-OPTION
  delivery_option_ids:
  - OPT-CONFIDENTIAL-CARGO
  gap_ids:
  - G04
  channel_role_note: Calling channel retained from MGN 364 sections 3.10-3.11. A separate working-channel assignment
    is not asserted.
- contact_id: COM-DOVER
  recipient: Dover MRCC
  call_sign: Dover Coastguard
  communication_method: VHF voice
  calling_channel: '11'
  working_channel: null
  listening_watch: null
  alternative_method: null
  evidence_ids:
  - EV-SW
  - EV-CARGO-OPTION
  delivery_option_ids:
  - OPT-CONFIDENTIAL-CARGO
  gap_ids:
  - G04
  channel_role_note: Calling channel retained from MGN 364 sections 3.10-3.11. A separate working-channel assignment
    is not asserted.
- contact_id: COM-CHANNEL-ITZ
  recipient: Channel VTS
  call_sign: null
  communication_method: null
  calling_channel: null
  working_channel: null
  listening_watch: null
  alternative_method: null
  delivery_option_ids: []
  gap_ids:
  - G08
  evidence_ids:
  - EV-ITZ-MGN
report_types:
- report_type_id: RT-CALDOVREP
  official_name: CALDOVREP
  fields:
  - field_id: FLD-01
    sequence: 1
    code_as_published: A
    information_required: Vessel name, radio call sign and IMO identifier; MMSI may identify a transponder report.
    requirement_strength: MANDATORY
    applicability_condition: MMSI alternative concerns transponder reporting.
    evidence_ids:
    - EV-F01
  - field_id: FLD-02
    sequence: 2
    code_as_published: B
    information_required: Reporting date and time.
    requirement_strength: MANDATORY
    applicability_condition: null
    evidence_ids:
    - EV-F02
  - field_id: FLD-03
    sequence: 3
    code_as_published: C or D
    information_required: 'Position: latitude/longitude, or true bearing and distance from an identified landmark.'
    requirement_strength: MANDATORY
    applicability_condition: Alternative position expressions; not two compulsory position reports.
    evidence_ids:
    - EV-F03
  - field_id: FLD-04
    sequence: 4
    code_as_published: E
    information_required: Course referenced to true north.
    requirement_strength: MANDATORY
    applicability_condition: null
    evidence_ids:
    - EV-F04
  - field_id: FLD-05
    sequence: 5
    code_as_published: F
    information_required: Vessel speed.
    requirement_strength: MANDATORY
    applicability_condition: null
    evidence_ids:
    - EV-F05
  - field_id: FLD-06
    sequence: 6
    code_as_published: G
    information_required: Departure port.
    requirement_strength: MANDATORY
    applicability_condition: null
    evidence_ids:
    - EV-F06
  - field_id: FLD-07
    sequence: 7
    code_as_published: I
    information_required: Destination port with arrival estimate.
    requirement_strength: MANDATORY
    applicability_condition: null
    evidence_ids:
    - EV-F07
  - field_id: FLD-08
    sequence: 8
    code_as_published: O
    information_required: Current draught.
    requirement_strength: MANDATORY
    applicability_condition: null
    evidence_ids:
    - EV-F08
  - field_id: FLD-09
    sequence: 9
    code_as_published: P
    information_required: Cargo; add dangerous-goods quantity and IMO class when applicable.
    requirement_strength: MANDATORY
    applicability_condition: Dangerous-goods particulars depend on cargo carried.
    evidence_ids:
    - EV-F09
  - field_id: FLD-10
    sequence: 10
    code_as_published: Q or R
    information_required: Report structural, cargo or equipment defects, damage or deficiencies. Also report other
      circumstances disrupting normal navigation under SOLAS or MARPOL.
    requirement_strength: MANDATORY
    applicability_condition: Preserve applicable defects and circumstances; no assumed nil-report convention.
    evidence_ids:
    - EV-F10
  - field_id: FLD-11
    sequence: 11
    code_as_published: T
    information_required: Contact address for dangerous-cargo particulars.
    requirement_strength: MANDATORY
    applicability_condition: Dangerous-cargo information purpose; nil-report handling not established.
    evidence_ids:
    - EV-F11
  - field_id: FLD-12
    sequence: 12
    code_as_published: W
    information_required: Total number of persons aboard.
    requirement_strength: MANDATORY
    applicability_condition: null
    evidence_ids:
    - EV-F12
  - field_id: FLD-13
    sequence: 13
    code_as_published: X
    information_required: Miscellaneous information. Apply the condition to its individual subitem, not the entire
      X group.
    requirement_strength: MANDATORY
    applicability_condition: null
    evidence_ids:
    - EV-F13
    condition_scope: SUBITEMS_ONLY
    subitems:
    - subitem_id: X-BUNKERS
      sequence: 1
      information_required: Estimated amount and characteristics of bunker fuel.
      condition_mode: CONDITIONAL
      condition:
        parameter: bunker_fuel_tonnes
        operator: GT
        value: 5000
        unit: tonnes
      requirement_strength: MANDATORY
      evidence_ids:
      - EV-F13
    - subitem_id: X-NAVIGATION
      sequence: 2
      information_required: Navigational conditions.
      condition_mode: NO_ADDITIONAL_CONDITION
      condition: null
      requirement_strength: MANDATORY
      evidence_ids:
      - EV-F13
- report_type_id: RT-CHANGE
  official_name: null
  fields:
  - field_id: FLD-CHANGE
    sequence: 1
    code_as_published: Q or R
    information_required: Changed navigation circumstances, particularly defects and other circumstances under Q/R.
    requirement_strength: UNKNOWN
    applicability_condition: The source says should. No new formal report title or full-repeat requirement is asserted.
    evidence_ids:
    - EV-CHANGE
- report_type_id: RT-ITZ-DECISION
  official_name: null
  fields:
  - field_id: FLD-ITZ
    sequence: 1
    code_as_published: null
    information_required: Notify the decision to use the English ITZ, the intended route and reasons.
    requirement_strength: MANDATORY
    applicability_condition: Only when the master decides that circumstances warrant use of the English ITZ. Notification
      is not permission to breach Rule 10.
    evidence_ids:
    - EV-ITZ-MGN
    - EV-ITZ-DETAIL
directions:
- direction_id: P01-NE
  direction_label: North-eastbound
  route_variant: Through-transit
  geographical_scope: Approach to and transit through CALDOVREP. No approved track is supplied.
  vessel_applicability: Ships of 300 GT and over, subject to applicable exemptions.
  reporting_events:
  - event_id: NE-ENTRY
    sequence: 1
    reporting_object_id: OBJ-WEST
    trigger_as_published: Crossing the western reporting line
    timing_as_published: two (2) nautical miles before crossing
    requirement_strength: MANDATORY
    vessel_applicability: Ships of 300 GT and over, subject to applicable exemptions.
    contact_id: COM-GRISNEZ
    report_type_id: RT-CALDOVREP
    exceptions: Naval and ferry arrangements require their stated conditions. AIS carriage is not treated as an
      automatic exemption.
    subsequent_action: null
    evidence_ids:
    - EV-NE
    - EV-THRESHOLD
    - EV-AMENDMENT
    - EV-EXEMPT
    event_mode: ENTRY
    gap_ids: []
  - event_id: NE-CHANGE
    sequence: 2
    reporting_object_id: null
    trigger_as_published: whenever there is a change of navigational circumstance
    timing_as_published: null
    requirement_strength: UNKNOWN
    vessel_applicability: Participating vessel; conditional event, not a routine second report.
    contact_id: null
    report_type_id: RT-CHANGE
    exceptions: null
    subsequent_action: Relevant shore station is the source wording. Recipient selection and urgency routing require
      G05 review.
    evidence_ids:
    - EV-CHANGE
    event_mode: CONDITIONAL
    gap_ids:
    - G05
    recipient_as_published: relevant shore station
  - event_id: NE-ITZ-DECISION
    sequence: 3
    event_mode: CONDITIONAL
    reporting_object_id: null
    trigger_as_published: Masters deciding that circumstances warrant their use of the English ITZ, must report
      their decision to Channel VTS.
    timing_as_published: null
    requirement_strength: MANDATORY
    vessel_applicability: Masters deciding that circumstances warrant use of the English ITZ; not a routine through-transit
      report.
    contact_id: COM-CHANNEL-ITZ
    report_type_id: RT-ITZ-DECISION
    exceptions: Notification does not authorise use contrary to Rule 10(d).
    subsequent_action: null
    gap_ids:
    - G08
    evidence_ids:
    - EV-ITZ-MGN
    - EV-ITZ-DETAIL
  spread:
    spread_id: P01-SPREAD-NE
    title: 'Channel VTS / CALDOVREP: NE-bound'
    layout: DOUBLE_PAGE
    map_extent: null
    reporting_object_ids:
    - OBJ-WEST
    reporting_event_ids:
    - NE-ENTRY
    - NE-CHANGE
    - NE-ITZ-DECISION
    graphics_dataset_path: null
    base_material_reference: null
    reproduction_permission_record: null
  sequence_semantics: EDITORIAL_DISPLAY_ORDER_NOT_FIXED_ITINERARY
- direction_id: P01-SW
  direction_label: South-westbound
  route_variant: Through-transit
  geographical_scope: Approach to and transit through CALDOVREP. No approved track is supplied.
  vessel_applicability: Ships of 300 GT and over, subject to applicable exemptions.
  reporting_events:
  - event_id: SW-ENTRY
    sequence: 1
    reporting_object_id: OBJ-EAST
    trigger_as_published: Crossing the eastern reporting line
    timing_as_published: not later than crossing
    requirement_strength: MANDATORY
    vessel_applicability: Ships of 300 GT and over, subject to applicable exemptions.
    contact_id: COM-DOVER
    report_type_id: RT-CALDOVREP
    exceptions: Naval and ferry arrangements require their stated conditions. AIS carriage is not treated as an
      automatic exemption.
    subsequent_action: null
    evidence_ids:
    - EV-SW
    - EV-THRESHOLD
    - EV-AMENDMENT
    - EV-EXEMPT
    - EV-SW-TIMING
    timing_conditions:
    - condition_id: SW-TIME-MGN
      wording_as_published: not later than crossing
      evidence_ids:
      - EV-SW
    - condition_id: SW-TIME-MCA
      wording_as_published: when they’re in VHF radio range of North Foreland and before crossing the boundary line
        in the SW traffic lane.
      evidence_ids:
      - EV-SW-TIMING
    timing_summary: Within VHF range of North Foreland and before the eastern reporting line; MGN states no later
      than crossing.
    event_mode: ENTRY
    gap_ids: []
  - event_id: SW-CHANGE
    sequence: 2
    reporting_object_id: null
    trigger_as_published: whenever there is a change of navigational circumstance
    timing_as_published: null
    requirement_strength: UNKNOWN
    vessel_applicability: Participating vessel; conditional event, not a routine second report.
    contact_id: null
    report_type_id: RT-CHANGE
    exceptions: null
    subsequent_action: Relevant shore station is the source wording. Recipient selection and urgency routing require
      G05 review.
    evidence_ids:
    - EV-CHANGE
    event_mode: CONDITIONAL
    gap_ids:
    - G05
    recipient_as_published: relevant shore station
  - event_id: SW-ITZ-DECISION
    sequence: 3
    event_mode: CONDITIONAL
    reporting_object_id: null
    trigger_as_published: Masters deciding that circumstances warrant their use of the English ITZ, must report
      their decision to Channel VTS.
    timing_as_published: null
    requirement_strength: MANDATORY
    vessel_applicability: Masters deciding that circumstances warrant use of the English ITZ; not a routine through-transit
      report.
    contact_id: COM-CHANNEL-ITZ
    report_type_id: RT-ITZ-DECISION
    exceptions: Notification does not authorise use contrary to Rule 10(d).
    subsequent_action: null
    gap_ids:
    - G08
    evidence_ids:
    - EV-ITZ-MGN
    - EV-ITZ-DETAIL
  spread:
    spread_id: P01-SPREAD-SW
    title: 'Channel VTS / CALDOVREP: SW-bound'
    layout: DOUBLE_PAGE
    map_extent: null
    reporting_object_ids:
    - OBJ-EAST
    reporting_event_ids:
    - SW-ENTRY
    - SW-CHANGE
    - SW-ITZ-DECISION
    graphics_dataset_path: null
    base_material_reference: null
    reproduction_permission_record: null
  sequence_semantics: EDITORIAL_DISPLAY_ORDER_NOT_FIXED_ITINERARY
evidence:
- evidence_id: EV-IDENTITY
  source_id: SRC-004
  snapshot_id: SRC-004__20261002T163852Z__2e5ab12c2a39
  source_locator: About the Dover Strait; How Channel VTS works
  supported_field_paths:
  - guide_area
  wording_as_published: null
  effective_from: null
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-THRESHOLD
  source_id: SRC-005
  snapshot_id: SRC-005__20261002T163852Z__1cafaed9fae8
  source_locator: Sections 3.7-3.9
  supported_field_paths:
  - participation.applicability_as_published
  wording_as_published: All vessels of 300GT and over
  effective_from: null
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-THRESHOLD-IMO
  source_id: P01-IMO85
  snapshot_id: null
  source_locator: Annex 2 section 1; PDF page 10 / printed Annex 16 page 9
  supported_field_paths:
  - participation.applicability_as_published
  wording_as_published: null
  effective_from: null
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-EXEMPT
  source_id: SRC-004
  snapshot_id: SRC-004__20261002T163852Z__2e5ab12c2a39
  source_locator: Exemptions from the CALDOVREP scheme
  supported_field_paths:
  - participation.exemptions_as_published
  wording_as_published: null
  effective_from: null
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-FERRY
  source_id: P01-IMO85
  snapshot_id: null
  source_locator: Annex 2 section 3.3, Crossing Traffic; PDF page 12 / printed Annex 16 page 11
  supported_field_paths:
  - conflicts[C03]
  wording_as_published: null
  effective_from: null
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-NE
  source_id: SRC-005
  snapshot_id: SRC-005__20261002T163852Z__1cafaed9fae8
  source_locator: Section 3.11
  supported_field_paths:
  - reporting_objects[OBJ-WEST]
  - communications[COM-GRISNEZ]
  - directions[P01-NE].reporting_events[NE-ENTRY]
  wording_as_published: null
  effective_from: null
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-SW
  source_id: SRC-005
  snapshot_id: SRC-005__20261002T163852Z__1cafaed9fae8
  source_locator: Section 3.10
  supported_field_paths:
  - reporting_objects[OBJ-EAST]
  - communications[COM-DOVER]
  - directions[P01-SW].reporting_events[SW-ENTRY]
  - directions[P01-SW].reporting_events[SW-ENTRY].timing_conditions[SW-TIME-MGN].wording_as_published
  wording_as_published: null
  effective_from: null
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-SW-TIMING
  source_id: SRC-004
  snapshot_id: SRC-004__20261002T163852Z__2e5ab12c2a39
  source_locator: 'Mandatory reporting - CALDOVREP: SW passage paragraph'
  supported_field_paths:
  - conflicts[C04]
  - directions[P01-SW].reporting_events[SW-ENTRY].timing_conditions[SW-TIME-MCA].wording_as_published
  - directions[P01-SW].reporting_events[SW-ENTRY].timing_summary
  wording_as_published: null
  effective_from: null
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-AMENDMENT
  source_id: P01-IMO251
  snapshot_id: null
  source_locator: PDF page 2 paragraph 2; PDF page 3 clause 3 and Appendix
  supported_field_paths:
  - report_types[RT-CALDOVREP]
  wording_as_published: null
  effective_from: '2008-05-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-OLD-LIST
  source_id: SRC-004
  snapshot_id: SRC-004__20261002T163852Z__2e5ab12c2a39
  source_locator: 'Mandatory reporting - CALDOVREP: report-content bullets'
  supported_field_paths:
  - conflicts[C02]
  wording_as_published: null
  effective_from: null
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-CHANGE
  source_id: P01-IMO85
  snapshot_id: null
  source_locator: Annex 2 section 3.3; PDF page 12 / printed Annex 16 page 11
  supported_field_paths:
  - report_types[RT-CHANGE]
  - directions[P01-NE].reporting_events[NE-CHANGE]
  - directions[P01-SW].reporting_events[SW-CHANGE]
  wording_as_published: null
  effective_from: null
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-AIS
  source_id: SRC-004
  snapshot_id: SRC-004__20261002T163852Z__2e5ab12c2a39
  source_locator: 'Mandatory reporting - CALDOVREP: AIS and ALRS paragraphs'
  supported_field_paths:
  - gaps[G04]
  wording_as_published: null
  effective_from: null
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-RS
  source_id: P01-TH-RS
  snapshot_id: null
  source_locator: 1 October 2023; deconstruction account
  supported_field_paths:
  - gaps[G02]
  wording_as_published: null
  effective_from: null
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-FUTURE
  source_id: P01-LIB-NCSR13
  snapshot_id: null
  source_locator: PDF pages 1-2; Routeing measures / Ship Reporting System in Europe
  supported_field_paths:
  - gaps[G03]
  wording_as_published: null
  effective_from: null
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-PORT
  source_id: P01-DOVER-PORT
  snapshot_id: null
  source_locator: VTS Information; Entry procedure
  supported_field_paths:
  - gaps[G03]
  wording_as_published: null
  effective_from: null
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-F01
  source_id: P01-IMO251
  snapshot_id: null
  source_locator: PDF page 3 / printed Annex 29 page 2; clause 3 and Appendix, A item
  supported_field_paths:
  - report_types[RT-CALDOVREP].fields[FLD-01]
  wording_as_published: null
  effective_from: '2008-05-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-F02
  source_id: P01-IMO251
  snapshot_id: null
  source_locator: PDF page 3 / printed Annex 29 page 2; clause 3 and Appendix, B item
  supported_field_paths:
  - report_types[RT-CALDOVREP].fields[FLD-02]
  wording_as_published: null
  effective_from: '2008-05-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-F03
  source_id: P01-IMO251
  snapshot_id: null
  source_locator: PDF page 3 / printed Annex 29 page 2; clause 3 and Appendix, C or D item
  supported_field_paths:
  - report_types[RT-CALDOVREP].fields[FLD-03]
  wording_as_published: null
  effective_from: '2008-05-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-F04
  source_id: P01-IMO251
  snapshot_id: null
  source_locator: PDF page 3 / printed Annex 29 page 2; clause 3 and Appendix, E item
  supported_field_paths:
  - report_types[RT-CALDOVREP].fields[FLD-04]
  wording_as_published: null
  effective_from: '2008-05-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-F05
  source_id: P01-IMO251
  snapshot_id: null
  source_locator: PDF page 3 / printed Annex 29 page 2; clause 3 and Appendix, F item
  supported_field_paths:
  - report_types[RT-CALDOVREP].fields[FLD-05]
  wording_as_published: null
  effective_from: '2008-05-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-F06
  source_id: P01-IMO251
  snapshot_id: null
  source_locator: PDF page 3 / printed Annex 29 page 2; clause 3 and Appendix, G item
  supported_field_paths:
  - report_types[RT-CALDOVREP].fields[FLD-06]
  wording_as_published: null
  effective_from: '2008-05-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-F07
  source_id: P01-IMO251
  snapshot_id: null
  source_locator: PDF page 3 / printed Annex 29 page 2; clause 3 and Appendix, I item
  supported_field_paths:
  - report_types[RT-CALDOVREP].fields[FLD-07]
  wording_as_published: null
  effective_from: '2008-05-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-F08
  source_id: P01-IMO251
  snapshot_id: null
  source_locator: PDF page 3 / printed Annex 29 page 2; clause 3 and Appendix, O item
  supported_field_paths:
  - report_types[RT-CALDOVREP].fields[FLD-08]
  wording_as_published: null
  effective_from: '2008-05-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-F09
  source_id: P01-IMO251
  snapshot_id: null
  source_locator: PDF page 3 / printed Annex 29 page 2; clause 3 and Appendix, P item
  supported_field_paths:
  - report_types[RT-CALDOVREP].fields[FLD-09]
  wording_as_published: null
  effective_from: '2008-05-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-F10
  source_id: P01-IMO251
  snapshot_id: null
  source_locator: PDF page 3 / printed Annex 29 page 2; clause 3 and Appendix, Q or R item
  supported_field_paths:
  - report_types[RT-CALDOVREP].fields[FLD-10]
  wording_as_published: null
  effective_from: '2008-05-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-F11
  source_id: P01-IMO251
  snapshot_id: null
  source_locator: PDF page 3 / printed Annex 29 page 2; clause 3 and Appendix, T item
  supported_field_paths:
  - report_types[RT-CALDOVREP].fields[FLD-11]
  wording_as_published: null
  effective_from: '2008-05-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-F12
  source_id: P01-IMO251
  snapshot_id: null
  source_locator: PDF page 3 / printed Annex 29 page 2; clause 3 and Appendix, W item
  supported_field_paths:
  - report_types[RT-CALDOVREP].fields[FLD-12]
  wording_as_published: null
  effective_from: '2008-05-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-F13
  source_id: P01-IMO251
  snapshot_id: null
  source_locator: PDF page 3 / printed Annex 29 page 2; clause 3 and Appendix, X item
  supported_field_paths:
  - report_types[RT-CALDOVREP].fields[FLD-13]
  - report_types[RT-CALDOVREP].fields[FLD-13].subitems[X-BUNKERS]
  - report_types[RT-CALDOVREP].fields[FLD-13].subitems[X-NAVIGATION]
  wording_as_published: null
  effective_from: '2008-05-01T00:00:00Z'
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-CARGO-OPTION
  source_id: P01-IMO85
  snapshot_id: null
  source_locator: Annex 2 section 3 opening paragraph, PDF page 11; section 5, PDF page 13
  supported_field_paths:
  - report_delivery_options[OPT-CONFIDENTIAL-CARGO]
  wording_as_published: null
  effective_from: null
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-ITZ-MGN
  source_id: SRC-005
  snapshot_id: SRC-005__20261002T163852Z__1cafaed9fae8
  source_locator: Section 3.4
  supported_field_paths:
  - communications[COM-CHANNEL-ITZ].recipient
  - report_types[RT-ITZ-DECISION]
  - directions[P01-NE].reporting_events[NE-ITZ-DECISION]
  - directions[P01-SW].reporting_events[SW-ITZ-DECISION]
  wording_as_published: null
  effective_from: null
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-ITZ-DETAIL
  source_id: SRC-004
  snapshot_id: SRC-004__20261002T163852Z__2e5ab12c2a39
  source_locator: Inshore traffic zones, final notification paragraph
  supported_field_paths:
  - report_types[RT-ITZ-DECISION].fields[FLD-ITZ].information_required
  wording_as_published: null
  effective_from: null
  effective_until: null
  verification_state: AUTHOR_CHECKED
- evidence_id: EV-FORMAT-ROUTE
  source_id: P01-A851
  snapshot_id: null
  source_locator: Appendix paragraph 2, PDF pages 7-9; read with P01-IMO85 Annex 2 section 3.1
  supported_field_paths:
  - gaps[G06]
  wording_as_published: null
  effective_from: null
  effective_until: null
  verification_state: AUTHOR_CHECKED
gaps:
- gap_id: G01
  affected_field_paths:
  - evidence[*].snapshot_id
  - assurance.independent_review_record
  missing_information: Retained originals and permitted storage for six live-only sources, including newly catalogued
    A.851(20).
  reason: Two MCA sources are held. Remaining consulted sources lack permitted retained originals. Rights and access
    are tracked separately.
  severity: BLOCKER
  disposition: OPEN
  next_action: Confirm an authorised archive and applicable reproduction rights; capture actual bytes and renders,
    then issue a new packet.
  resolution_evidence_ids: []
  decision_record: null
- gap_id: G02
  affected_field_paths:
  - reporting_objects[*].datum_as_published
  - reporting_objects[OBJ-WEST]
  - directions[*].spread
  missing_information: Current full reporting-line geometry, reference feature and datums
  reason: MGN gives a verbal western line and one assigned buoy position. Royal Sovereign topsides were removed
    in 2023.
  severity: BLOCKER
  disposition: OPEN
  next_action: Check corrected official chart/ALRS and competent authority. Do not substitute a buoy or infer endpoints.
  resolution_evidence_ids: []
  decision_record: null
- gap_id: G03
  affected_field_paths:
  - assurance.subsequent_notices_check
  - communications[COM-DOVER].call_sign
  missing_information: Complete notice/ALRS/French-instruction reconciliation and current UK call-name confirmation
  reason: MCA publishes Dover Coastguard while the service is branded Channel VTS. A 2026 meeting report flags future
    amendments.
  severity: BLOCKER
  disposition: OPEN
  next_action: Obtain current ALRS 6(1), official amendments and provider clarification where needed. Keep harbour
    Dover VTS separate.
  resolution_evidence_ids: []
  decision_record: null
- gap_id: G04
  affected_field_paths:
  - communications[*].listening_watch
  - communications[*].alternative_method
  - communications[COM-GRISNEZ].working_channel
  - communications[COM-DOVER].working_channel
  missing_information: Current watch, working-channel roles, AIS acceptance, non-verbal cargo delivery implementation
    and failure procedures.
  reason: The limited confidential-cargo option is now recorded. Current delivery addresses, accepted fields and
    procedures remain unconfirmed.
  severity: BLOCKER
  disposition: OPEN
  next_action: Acquire detailed instructions. Do not invent a universal AIS exemption or a routine exit or transfer
    report.
  resolution_evidence_ids: []
  decision_record: null
- gap_id: G05
  affected_field_paths:
  - directions[P01-NE].reporting_events[NE-CHANGE]
  - directions[P01-SW].reporting_events[SW-CHANGE]
  missing_information: Exact recipient, obligation strength and urgency routing for conditional changes
  reason: Base IMO instrument says should and relevant shore station; current implementation not fully reconciled.
  severity: ERROR
  disposition: OPEN
  next_action: Check provider instructions and national duties; retain the trigger without inventing a normal second-report
    point.
  resolution_evidence_ids: []
  decision_record: null
- gap_id: G06
  affected_field_paths:
  - report_types[RT-CALDOVREP].fields
  missing_information: Full encoding, units, time standard and nil-report conventions
  reason: A.851(20), Appendix paragraph 2, is an identified format source. Current CALDOVREP implementation, amendments
    and nil conventions remain unchecked.
  severity: ERROR
  disposition: OPEN
  next_action: Retain and reconcile A.851(20) and amendments with current provider/ALRS instructions. Do not import
    generic final-report events.
  resolution_evidence_ids: []
  decision_record: null
- gap_id: G07
  affected_field_paths:
  - assurance.marine_approval_record
  - assurance.artwork_check_record
  - assurance.release_record
  missing_information: Independent evidence review, marine approval and graphic checks
  reason: This is an author research sample; no independent reviewer or released artwork exists.
  severity: BLOCKER
  disposition: OPEN
  next_action: Review the completed frozen packet and resolve findings before producing directional PDF prototypes.
  resolution_evidence_ids: []
  decision_record: null
- gap_id: G08
  affected_field_paths:
  - communications[COM-CHANNEL-ITZ]
  - directions[P01-NE].reporting_events[NE-ITZ-DECISION]
  - directions[P01-SW].reporting_events[SW-ITZ-DECISION]
  missing_information: Current operational recipient selection, contact method and timing for the English ITZ notification.
  reason: MCA identifies Channel VTS and the reporting subject; the exact event-handling detail is not stated in
    the reviewed clause.
  severity: BLOCKER
  disposition: OPEN
  next_action: Obtain current provider implementation before presenting this conditional event as a complete bridge
    instruction.
  resolution_evidence_ids: []
  decision_record: null
conflicts:
- conflict_id: C01
  affected_fields:
  - participation.applicability_as_published
  assertions:
  - source_id: SRC-004
    assertion: Over 300 gross tonnes
  - source_id: SRC-005
    assertion: 300GT and over
    evidence_ids:
    - EV-THRESHOLD
  - source_id: P01-IMO85
    assertion: 300 GT inclusive
    evidence_ids:
    - EV-THRESHOLD-IMO
  disposition: AUTHOR_RESOLVED_PENDING_REVIEW
  decision: Use inclusive 300 GT threshold; specific MCA guidance agrees with the adopted participation clause.
    Preserve the discrepant summary.
  reviewer: null
- conflict_id: C02
  affected_fields:
  - report_types[RT-CALDOVREP]
  assertions:
  - source_id: SRC-004
    assertion: Shorter summary includes route information and omits amended code groups.
    evidence_ids:
    - EV-OLD-LIST
  - source_id: P01-IMO251
    assertion: Explicit replacement of section 3.2 and summary section 4, effective 1 May 2008.
    evidence_ids:
    - EV-AMENDMENT
  disposition: AUTHOR_RESOLVED_PENDING_REVIEW
  decision: Use the 13 amended groups for this sample. Do not retain L as mandatory from the old summary. Later
    amendments remain G03.
  reviewer: null
- conflict_id: C03
  affected_fields:
  - directions[*].reporting_events[*].exceptions
  assertions:
  - source_id: SRC-004
    assertion: Regular scheduled ferries receive simplified treatment.
    evidence_ids:
    - EV-EXEMPT
  - source_id: P01-IMO85
    assertion: Special arrangements need ship-specific approval by both stations.
    evidence_ids:
    - EV-FERRY
  disposition: AUTHOR_RESOLVED_PENDING_REVIEW
  decision: Do not turn the short summary into a blanket ferry exemption. Ferry routes are outside this through-transit
    sample.
  reviewer: null
- conflict_id: C04
  affected_fields:
  - directions[P01-SW].reporting_events[SW-ENTRY].timing_as_published
  assertions:
  - source_id: SRC-004
    assertion: Within VHF range and before crossing.
    evidence_ids:
    - EV-SW-TIMING
  - source_id: SRC-005
    assertion: Not later than crossing.
    evidence_ids:
    - EV-SW
  disposition: AUTHOR_CORRECTED_PENDING_REVIEW
  decision: Both source wordings are retained in the canonical SW event timing_conditions. timing_summary supplies
    the combined display instruction. No two-mile SW condition is inferred.
  reviewer: null
assurance:
  research_cutoff_utc: '2026-10-03T07:36:34.513647+00:00'
  subsequent_notices_check: PARTIAL. Existing MCA pages and cited IMO material rechecked for this correction. Complete
    ALRS, UKHO and French notices reconciliation remains G03.
  independent_review_record: null
  marine_approval_record: null
  artwork_check_record: null
  release_record: null
production:
  research_revision: 0.2.1-author-correction
  schema_revision: 1.0-draft+channel.1
  style_sheet_revision: null
  effort_record: effort.csv
  pdf_output_paths: []
report_delivery_options:
- option_id: OPT-CONFIDENTIAL-CARGO
  report_type_id: RT-CALDOVREP
  subject_scope: Commercially confidential cargo information only, not the entire CALDOVREP report.
  method_as_published: non-verbal means
  timing_as_published: prior to entering the system
  requirement_strength: VOLUNTARY
  implementation_state: CURRENT_DETAILS_UNRESOLVED
  current_delivery_address: null
  gap_ids:
  - G04
  evidence_ids:
  - EV-CARGO-OPTION
scope_exclusions:
- exclusion_id: EX-SMALL
  subject: Complete reporting procedures for vessels below 300 GT.
  basis: SRC-005 section 3.9 remains a specific conditional-reporting lead. No universal exemption is asserted.
  approval_state: PROPOSED_FOR_MARINE_REVIEW
- exclusion_id: EX-TOW
  subject: Complete tug and long-tow reporting procedures.
  basis: SRC-005 section 5.1(iv) contains best-practice early and continued reporting advice. It is not applied
    to every vessel.
  approval_state: PROPOSED_FOR_MARINE_REVIEW
- exclusion_id: EX-FERRY
  subject: Ferry, harbour-entry, joining and crossing route variants.
  basis: P01-IMO85 Annex 2 section 3.3 includes port-departure and ship-specific ferry arrangements. These remain
    outside the bounded through-transit example.
  approval_state: PROPOSED_FOR_MARINE_REVIEW
- exclusion_id: EX-RECREATION
  subject: Recreational and dive-support operations.
  basis: SRC-005 section 6.4 contains a specific notification recommendation. Separate research is required for
    this vessel/activity scope.
  approval_state: PROPOSED_FOR_MARINE_REVIEW
---

# Channel VTS / CALDOVREP

**Directional reporting guide | Research revision 0.2.1-author-correction | Presentation proforma-1**

> **DRAFT / HOLD. Not for navigation or publication.**
> Reporting details below are inherited research findings, not newly approved instructions.
> Current notices, communications, plotting geometry and independent marine review remain outstanding.
> Consult the limitations beside each affected item and the complete checks in Section 9.

## Contents

1. Service overview
2. Participation and applicability
3. Reporting arrangements by direction
4. Information required
5. Communications and watchkeeping
6. Conditional and exceptional reporting
7. Reporting locations and graphic requirements
8. References
9. Outstanding checks and editorial notes

Research and review records appear in Appendix A.

## 1. Service overview

| Item | Recorded position |
| --- | --- |
| Service | Channel VTS [R3 About the Dover Strait; How Channel VTS works](#r3) |
| Operating centres | Dover MRCC and CROSS Gris-Nez [R3 About the Dover Strait; How Channel VTS works](#r3) |
| Reporting system | CALDOVREP. [R3 About the Dover Strait; How Channel VTS works](#r3) [R2 commencement paragraph; Appendix (PDF pp.2–3)](#r2) |
| Study scope | Standard NE-bound and SW-bound through-transits, approach reporting, conditional navigation changes and English ITZ notification. Special-operation variants are outside this sample, not exempt from their rules. (Editorial scope.) |
| Authority detail | UK and French maritime authorities; current administrative titles require publication review. [R3 About the Dover Strait; How Channel VTS works](#r3) [G03](#g03). |

Channel VTS and Port of Dover harbour VTS are separate services. Harbour-entry procedures are outside this guide. [R7 VTS Information; Entry procedure](#r7)

## 2. Participation and applicability

**Standard participation:** All vessels of 300GT and over. [R1 §§3.7–3.9](#r1) [R4 Annex 2 §1](#r4)

**Naval vessels:** Whatever their nationality, naval vessels are also exempt from reporting. [R3 Exemptions](#r3)

**Ferry arrangements:** simplified reporting must not be treated as a blanket exemption. The original scheme requires ship-specific bilateral approval. [R4 Annex 2 §3.3, Crossing Traffic](#r4) [R3 Exemptions](#r3)

The shorter MCA summary uses a different threshold formulation. The inclusive threshold is retained; see C01 in Section 9. [R1 §§3.7–3.9](#r1) [R4 Annex 2 §1](#r4) [R3 Mandatory reporting](#r3)

### 2.1 Scope exclusions

These are proposed editorial exclusions, not exemptions from applicable reporting rules.

| Not fully developed in this sample | Research position |
| --- | --- |
| Complete reporting procedures for vessels below 300 GT. | The source remains a specific conditional-reporting lead. No universal exemption is asserted. [R1 §3.9](#r1) |
| Complete tug and long-tow reporting procedures. | The source contains best-practice early and continued reporting advice. It is not applied to every vessel. [R1 §5.1(iv)](#r1) |
| Ferry, harbour-entry, joining and crossing route variants. | The source includes port-departure and ship-specific ferry arrangements. These remain outside the bounded through-transit example. [R4 Annex 2 §3.3](#r4) |
| Recreational and dive-support operations. | The source contains a specific notification recommendation. Separate research is required for this vessel/activity scope. [R1 §6.4](#r1) |

## 3. Reporting arrangements by direction

The two directions are presented separately. Conditional notifications are not routine second or third reporting points.

### 3.1 North-eastbound transit

| Action or condition | Reporting arrangement | Reference |
| --- | --- | --- |
| Applicability | Ships of 300 GT and over, subject to applicable exemptions. | [R1 §§3.7–3.9](#r1) [R3 Exemptions](#r3) |
| Entry boundary | Western reporting line. Full description in Section 7. | [R1 §3.11](#r1) |
| When to report | two (2) nautical miles before crossing | [R1 §3.11](#r1) |
| Who to call | Gris-Nez Traffic; CROSS Gris-Nez. | [R1 §3.11](#r1) |
| Published calling channel | VHF 13. Further channel roles remain open under G04. | [R1 §3.11](#r1) |
| Information required | CALDOVREP information in Section 4, including each stated condition. | [R2 commencement paragraph; Appendix (PDF pp.2–3)](#r2) |

**During transit:** see Section 6 for conditional navigation-change and English ITZ notifications. [R4 Annex 2 §3.3](#r4) [R1 §3.4](#r1)

**Transfers and departure:** subsequent routine instructions are not established in this sample. Do not read this as “no report required”. See [G03](#g03)–[G05](#g05).

### 3.2 South-westbound transit

| Action or condition | Reporting arrangement | Reference |
| --- | --- | --- |
| Applicability | Ships of 300 GT and over, subject to applicable exemptions. | [R1 §§3.7–3.9](#r1) [R3 Exemptions](#r3) |
| Entry boundary | Eastern reporting line. Full description in Section 7. | [R1 §3.10](#r1) |
| When to report | Within VHF range of North Foreland and before the eastern reporting line; MGN states no later than crossing. | [R1 §3.10](#r1) [R3 Mandatory reporting, SW paragraph](#r3) |
| Who to call | Dover Coastguard; Dover MRCC. | [R1 §3.10](#r1) |
| Published calling channel | VHF 11. Further channel roles remain open under G04. | [R1 §3.10](#r1) |
| Information required | CALDOVREP information in Section 4, including each stated condition. | [R2 commencement paragraph; Appendix (PDF pp.2–3)](#r2) |

**During transit:** see Section 6 for conditional navigation-change and English ITZ notifications. [R4 Annex 2 §3.3](#r4) [R1 §3.4](#r1)

**Transfers and departure:** subsequent routine instructions are not established in this sample. Do not read this as “no report required”. See [G03](#g03)–[G05](#g05).


## 4. Information required

The table shows the report subjects retained in the amended CALDOVREP list. It is not a worked radio message. [R2 commencement paragraph; Appendix (PDF pp.2–3)](#r2)

**Open formatting checks:** units, time standard, encoding and nil-report handling remain under [G06](#g06).

| Code | Information required | Condition or qualification | Reference |
| --- | --- | --- | --- |
| A | Vessel name, radio call sign and IMO identifier; MMSI may identify a transponder report. | MMSI alternative concerns transponder reporting. | [R2 Appendix, item A (PDF p.3)](#r2) |
| B | Reporting date and time. | Not separately recorded. | [R2 Appendix, item B (PDF p.3)](#r2) |
| C or D | Position: latitude/longitude, or true bearing and distance from an identified landmark. | Alternative position expressions; not two compulsory position reports. | [R2 Appendix, item C or D (PDF p.3)](#r2) |
| E | Course referenced to true north. | Not separately recorded. | [R2 Appendix, item E (PDF p.3)](#r2) |
| F | Vessel speed. | Not separately recorded. | [R2 Appendix, item F (PDF p.3)](#r2) |
| G | Departure port. | Not separately recorded. | [R2 Appendix, item G (PDF p.3)](#r2) |
| I | Destination port with arrival estimate. | Not separately recorded. | [R2 Appendix, item I (PDF p.3)](#r2) |
| O | Current draught. | Not separately recorded. | [R2 Appendix, item O (PDF p.3)](#r2) |
| P | Cargo; add dangerous-goods quantity and IMO class when applicable. | Dangerous-goods particulars depend on cargo carried. | [R2 Appendix, item P (PDF p.3)](#r2) |
| Q or R | Report structural, cargo or equipment defects, damage or deficiencies. Also report other circumstances disrupting normal navigation under SOLAS or MARPOL. | Preserve applicable defects and circumstances; no assumed nil-report convention. | [R2 Appendix, item Q or R (PDF p.3)](#r2) |
| T | Contact address for dangerous-cargo particulars. | Dangerous-cargo information purpose; nil-report handling not established. | [R2 Appendix, item T (PDF p.3)](#r2) |
| W | Total number of persons aboard. | Not separately recorded. | [R2 Appendix, item W (PDF p.3)](#r2) |
| X | Bunker particulars and navigational conditions. See the separate subjects in Section 4.1. | Apply the bunker threshold only to the bunker particulars. | [R2 Appendix, item X (PDF p.3)](#r2) |

### 4.1 Field X: separate reporting subjects

The following labels are editorial descriptions, not additional official report codes.

| Subject within X | Condition | Reference |
| --- | --- | --- |
| Estimated amount and characteristics of bunker fuel. | Bunker fuel exceeds 5,000 tonnes. | [R2 Appendix, item X (PDF p.3)](#r2) |
| Navigational conditions. | Not subject to the bunker-quantity threshold. | [R2 Appendix, item X (PDF p.3)](#r2) |

Unknown bunker quantity remains a review question. It is not treated as zero or an automatic exemption.

### 4.2 Confidential cargo information

The original scheme provides an advance non-verbal option for commercially confidential cargo particulars. [R4 Annex 2 §§3, 5](#r4)

This concerns the cargo portion only, not the entire report. [R4 Annex 2 §§3, 5](#r4)

**Current delivery details remain unconfirmed.** No address or whole-report exemption is supplied. See [G04](#g04).

## 5. Communications and watchkeeping

| Purpose | Recipient / call sign | Calling channel | Other channel roles | Reference |
| --- | --- | --- | --- | --- |
| NE entry | CROSS Gris-Nez / Gris-Nez Traffic | VHF 13 | Working-channel assignment and listening watch not established: G04. | [R1 §3.11](#r1) |
| SW entry | Dover MRCC / Dover Coastguard | VHF 11 | Working-channel assignment and listening watch not established: G04. | [R1 §3.10](#r1) |
| English ITZ notification | Channel VTS | Not established: G08. | Recipient selection, method and timing remain open. | [R1 §3.4](#r1) |

AIS reception capability does not establish a universal exemption from voice reporting. [R3 Mandatory reporting, communications](#r3)

Current call-name, watch, transfer, failure and alternative-delivery details remain subject to [G03](#g03), [G04](#g04) and [G08](#g08).

## 6. Conditional and exceptional reporting

These notifications are conditional. Display order is not a schedule of calls.

### 6.1 Changed navigational circumstances

| Item | Recorded requirement |
| --- | --- |
| Trigger | Whenever navigational circumstances change. [R4 Annex 2 §3.3](#r4) |
| Information | Changed navigation circumstances, particularly defects and other circumstances under Q/R. [R4 Annex 2 §3.3](#r4) |
| Recipient | The relevant shore station. Exact selection remains open under G05. [R4 Annex 2 §3.3](#r4) |
| Strength | The source says should. No new formal report title or full-repeat requirement is asserted. [R4 Annex 2 §3.3](#r4) [G05](#g05). |

### 6.2 Decision to use the English ITZ

Notify the decision to use the English ITZ, the intended route and reasons. [R1 §3.4](#r1) [R3 Inshore traffic zones, final paragraph](#r3)

Only when the master decides that circumstances warrant use of the English ITZ. Notification is not permission to breach Rule 10. [R1 §3.4](#r1) [R3 Inshore traffic zones, final paragraph](#r3)

**Implementation gap:** exact current contact selection, method and timing remain [G08](#g08).

## 7. Reporting locations and graphic requirements

**Not approved for plotting.** Published descriptions are retained below. Missing endpoints or datum must not be inferred.

### 7.1 Western reporting line

Line from the Royal Sovereign light tower, through the Bassurelle Light Buoy (at its assigned position of 50°32’.8N, 000°57’.8E) to the coast of France. [R1 §3.11](#r1)

**Datum:** not stated in the recorded source clause. **Plotting:** blocked pending [G02](#g02).

### 7.2 Eastern reporting line

Line drawn from North Foreland Light (51° 23’N; 001° 27’E) to the border between France and Belgium (51° 05’N; 002° 33’E). [R1 §3.10](#r1)

**Datum:** not stated in the recorded source clause. **Plotting:** blocked pending [G02](#g02).

The western reference requires confirmation following the reported removal of Royal Sovereign lighthouse topsides. [R5 deconstruction account](#r5) [R1 §3.11](#r1)

That removal does not establish a replacement reporting line. No replacement position is supplied.

### 7.3 Artwork requirements

Keep reporting boundaries as lines. Direction arrows must not imply approved tracks. Show applicability and conditional notices beside the relevant callouts.

Map extent, base material, reproduction permissions and finished artwork remain unapproved. See [G02](#g02) and [G07](#g07).

## 8. References

References below identify the exact provisions used by this draft. A citation is not a claim that an unretained original is held.

“PDF page” refers to file-page order. Printed page numbers are retained in the underlying evidence ledger.

<a id="r1"></a>

### R1. MGN 364 (M+F) Amendment 2

**Issuer:** Maritime and Coastguard Agency. **Publication/update:** 2024-12-03.

[Original source](https://www.gov.uk/government/publications/mgn-364-mf-amendment-2-navigation-safety-traffic-separation-schemes-application-of-rule-10-and-navigation-in-the-dover-strait/mgn-364-mf-amendment-2-navigation-safety-traffic-separation-schemes-application-of-rule-10-and-navigation-in-the-dover-strait) · **Recorded access:** 2026-10-02.

**Source scope:** Sections 3.1, 3.4 and 3.7-3.11

**Retained:** original HTML and mechanical text extraction.

Original: `sources/archive/html/SRC-005__20261002T163852Z__1cafaed9fae8.html`.

Extraction: `sources/extracted/SRC-005__20261002T163852Z__1cafaed9fae8.txt`.

**Limitations:** Reporting-line datum and complete western geometry not stated in the cited paragraphs; current ALRS and notices require reconciliation

<a id="r2"></a>

### R2. Resolution MSC.251(83): amendments to CALDOVREP report content

**Issuer:** International Maritime Organization. **Publication/update:** 2007-10-08.

[Original source](https://wwwcdn.imo.org/localresources/en/KnowledgeCentre/IndexofIMOResolutions/MSCResolutions/MSC.251(83).pdf) · **Recorded access:** 2026-10-02.

**Source scope:** PDF page 3 / printed Annex 29 page 2, clause 3 and Appendix; PDF page 2 for entry into force

**Not retained:** consulted live in the earlier research; no original snapshot is held in this packet. See [G01](#g01).

**Limitations:** Permitted retained review copy and complete later-amendment reconciliation remain open

<a id="r3"></a>

### R3. Dover Strait crossings: Channel VTS

**Issuer:** Maritime and Coastguard Agency. **Publication/update:** 2024-02-01.

[Original source](https://www.gov.uk/government/publications/dover-strait-crossings-channel-navigation-information-service/dover-strait-crossings-channel-navigation-information-service-cnis) · **Recorded access:** 2026-10-02.

**Source scope:** About the Dover Strait; Mandatory reporting - CALDOVREP; Exemptions from the CALDOVREP scheme

**Retained:** original HTML and mechanical text extraction.

Original: `sources/archive/html/SRC-004__20261002T163852Z__2e5ab12c2a39.html`.

Extraction: `sources/extracted/SRC-004__20261002T163852Z__2e5ab12c2a39.txt`.

**Limitations:** Threshold wording is imprecise; report-content summary differs from the explicit IMO amendment

<a id="r4"></a>

### R4. Resolution MSC.85(70), Annex 2: CALDOVREP

**Issuer:** International Maritime Organization. **Publication/update:** 1998-12-07.

[Original source](https://wwwcdn.imo.org/localresources/en/KnowledgeCentre/IndexofIMOResolutions/MSCResolutions/MSC.85(70).pdf) · **Recorded access:** 2026-10-02.

**Source scope:** Annex 2 ONLY: PDF pages 10-13 / printed Annex 16 pages 9-12, sections 1-5

**Not retained:** consulted live in the earlier research; no original snapshot is held in this packet. See [G01](#g01).

**Limitations:** Annex 1 concerns US right whales and is excluded; Original section 3.2 is superseded by MSC.251(83); Old hardware and national-law descriptions are not reused as current rules; No reproducible retained original/render packet yet

<a id="r5"></a>

### R5. Royal Sovereign Lighthouse: stage one of deconstruction

**Issuer:** Trinity House. **Publication/update:** 2023-10-01.

[Original source](https://www.trinityhouse.co.uk/galleries/royal-sovereign-lighthouse-stage-one-of-deconstruction) · **Recorded access:** 2026-10-02.

**Source scope:** 1 October 2023; deconstruction account

**Not retained:** consulted live in the earlier research; no original snapshot is held in this packet. See [G01](#g01).

**Limitations:** Confirms topsides removal, not a new reporting-line location or cancellation

<a id="r6"></a>

### R6. Resolution A.851(20): ship-reporting format reference

**Issuer:** International Maritime Organization. **Publication/update:** 1997-11-27.

[Original source](https://wwwcdn.imo.org/localresources/en/KnowledgeCentre/IndexofIMOResolutions/AssemblyDocuments/A.851(20).pdf) · **Recorded access:** 2026-10-03.

**Source scope:** Appendix paragraph 2, PDF pages 7-9, especially B/C/D/E/F/I. Generic report schedules are not adopted as CALDOVREP duties.

**Not retained:** consulted live in the earlier research; no original snapshot is held in this packet. See [G01](#g01).

**Limitations:** Format-reference route only. No provider implementation, nil-report convention or new final-report duty inferred.

<a id="r7"></a>

### R7. Port of Dover: Dover VTS

**Issuer:** Dover Harbour Board. **Publication/update:** not recorded.

[Original source](https://www.portofdover.com/port-information/using-the-port/port-control-vts/) · **Recorded access:** 2026-10-02.

**Source scope:** VTS Information; Entry procedure

**Not retained:** consulted live in the earlier research; no original snapshot is held in this packet. See [G01](#g01).

**Limitations:** Port-entry source is excluded from CALDOVREP through-transit instructions

<a id="r8"></a>

### R8. IMO NCSR 13 Meeting summary

**Issuer:** Liberian Registry (LISCR), participating delegation. **Publication/update:** 2026-07-23.

[Original source](https://www.liscr.com/marketing/liscr/media/liscr/online%20library/maritime/ncsr-13-meeting-summary.pdf) · **Recorded access:** 2026-10-02.

**Source scope:** PDF pages 1-2, Routeing measures and Ship Reporting System in Europe

**Not retained:** consulted live in the earlier research; no original snapshot is held in this packet. See [G01](#g01).

**Limitations:** Prospective change lead, not an adopted IMO instrument or an in-force reporting instruction


## 9. Outstanding checks and editorial notes

Open checks remain visible here and beside the affected instructions. None is closed by this presentation change.

<a id="g01"></a>

### G01. Retained originals and permitted storage for six live-only sources, including newly catalogued A.851(20).

**Status:** OPEN. **Severity:** BLOCKER.

Two MCA sources are held. Remaining consulted sources lack permitted retained originals. Rights and access are tracked separately.

**Required action:** Confirm an authorised archive and applicable reproduction rights; capture actual bytes and renders, then issue a new packet.

<a id="g02"></a>

### G02. Current full reporting-line geometry, reference feature and datums

**Status:** OPEN. **Severity:** BLOCKER.

MGN gives a verbal western line and one assigned buoy position. Royal Sovereign topsides were removed in 2023.

**Required action:** Check corrected official chart/ALRS and competent authority. Do not substitute a buoy or infer endpoints.

<a id="g03"></a>

### G03. Complete notice/ALRS/French-instruction reconciliation and current UK call-name confirmation

**Status:** OPEN. **Severity:** BLOCKER.

MCA publishes Dover Coastguard while the service is branded Channel VTS. A 2026 meeting report flags future amendments.

**Required action:** Obtain current ALRS 6(1), official amendments and provider clarification where needed. Keep harbour Dover VTS separate.

<a id="g04"></a>

### G04. Current watch, working-channel roles, AIS acceptance, non-verbal cargo delivery implementation and failure procedures.

**Status:** OPEN. **Severity:** BLOCKER.

The limited confidential-cargo option is now recorded. Current delivery addresses, accepted fields and procedures remain unconfirmed.

**Required action:** Acquire detailed instructions. Do not invent a universal AIS exemption or a routine exit or transfer report.

<a id="g05"></a>

### G05. Exact recipient, obligation strength and urgency routing for conditional changes

**Status:** OPEN. **Severity:** ERROR.

Base IMO instrument says should and relevant shore station; current implementation not fully reconciled.

**Required action:** Check provider instructions and national duties; retain the trigger without inventing a normal second-report point.

<a id="g06"></a>

### G06. Full encoding, units, time standard and nil-report conventions

**Status:** OPEN. **Severity:** ERROR.

A.851(20), Appendix paragraph 2, is an identified format source. Current CALDOVREP implementation, amendments and nil conventions remain unchecked.

**Required action:** Retain and reconcile A.851(20) and amendments with current provider/ALRS instructions. Do not import generic final-report events.

<a id="g07"></a>

### G07. Independent evidence review, marine approval and graphic checks

**Status:** OPEN. **Severity:** BLOCKER.

This is an author research sample; no independent reviewer or released artwork exists.

**Required action:** Review the completed frozen packet and resolve findings before producing directional PDF prototypes.

<a id="g08"></a>

### G08. Current operational recipient selection, contact method and timing for the English ITZ notification.

**Status:** OPEN. **Severity:** BLOCKER.

MCA identifies Channel VTS and the reporting subject; the exact event-handling detail is not stated in the reviewed clause.

**Required action:** Obtain current provider implementation before presenting this conditional event as a complete bridge instruction.

### 9.1 Source conflicts and author dispositions

**C01 · AUTHOR_RESOLVED_PENDING_REVIEW**

Over 300 gross tonnes [R3](#r3)

300GT and over [R1 §§3.7–3.9](#r1)

300 GT inclusive [R4 Annex 2 §1](#r4)

**Author disposition:** Use inclusive 300 GT threshold; specific MCA guidance agrees with the adopted participation clause. Preserve the discrepant summary.

**C02 · AUTHOR_RESOLVED_PENDING_REVIEW**

Shorter summary includes route information and omits amended code groups. [R3 Mandatory reporting, content list](#r3)

Explicit replacement of section 3.2 and summary section 4, effective 1 May 2008. [R2 commencement paragraph; Appendix (PDF pp.2–3)](#r2)

**Author disposition:** Use the 13 amended groups for this sample. Do not retain L as mandatory from the old summary. Later amendments remain G03.

**C03 · AUTHOR_RESOLVED_PENDING_REVIEW**

Regular scheduled ferries receive simplified treatment. [R3 Exemptions](#r3)

Special arrangements need ship-specific approval by both stations. [R4 Annex 2 §3.3, Crossing Traffic](#r4)

**Author disposition:** Do not turn the short summary into a blanket ferry exemption. Ferry routes are outside this through-transit sample.

**C04 · AUTHOR_CORRECTED_PENDING_REVIEW**

Within VHF range and before crossing. [R3 Mandatory reporting, SW paragraph](#r3)

Not later than crossing. [R1 §3.10](#r1)

**Author disposition:** Both source wordings are retained in the canonical SW event timing_conditions. timing_summary supplies the combined display instruction. No two-mile SW condition is inferred.

### 9.2 Amendment and format follow-up

The catalogued NCSR 13 account is a prospective amendment lead, not an adopted instruction. [R8 PDF pp.1–2](#r8)

A.851(20) is the recorded format-reference route. Current implementation and nil conventions remain unconfirmed. [R6 Appendix §2 (PDF pp.7–9)](#r6)

## Appendix A. Research and review record

The operational YAML is unchanged from revision 0.2.1. This is presentation revision proforma-1.

No new source acquisition, current-notice check, independent review or publication approval is claimed.

The YAML, source catalogue and capture manifests remain the underlying evidence records. Reader labels R1–R8 are aliases, not replacement source IDs.

| Record | Location |
| --- | --- |
| Detailed correction and re-proof history | [Correction report](../../../reviews/vts/reports/PILOT-01__correction_reproof_2026-10-03.md) |
| Source catalogue | [source_catalogue.json](source_catalogue.json) |
| Exact review inputs | [packet.json](packet.json) |
| Presentation checks | [presentation_check.json](presentation_check.json) |
| Prospective effort ledger | [effort.csv](effort.csv) |

### A.1 Citation crosswalk

| Reader reference | Source ID |
| --- | --- |
| R1 | SRC-005 |
| R2 | P01-IMO251 |
| R3 | SRC-004 |
| R4 | P01-IMO85 |
| R5 | P01-TH-RS |
| R6 | P01-A851 |
| R7 | P01-DOVER-PORT |
| R8 | P01-LIB-NCSR13 |

### A.2 Complete evidence locator ledger

| Evidence ID | Reader citation | Exact recorded locator |
| --- | --- | --- |
| EV-IDENTITY | [R3 About the Dover Strait; How Channel VTS works](#r3) | About the Dover Strait; How Channel VTS works |
| EV-THRESHOLD | [R1 §§3.7–3.9](#r1) | Sections 3.7-3.9 |
| EV-THRESHOLD-IMO | [R4 Annex 2 §1](#r4) | Annex 2 section 1; PDF page 10 / printed Annex 16 page 9 |
| EV-EXEMPT | [R3 Exemptions](#r3) | Exemptions from the CALDOVREP scheme |
| EV-FERRY | [R4 Annex 2 §3.3, Crossing Traffic](#r4) | Annex 2 section 3.3, Crossing Traffic; PDF page 12 / printed Annex 16 page 11 |
| EV-NE | [R1 §3.11](#r1) | Section 3.11 |
| EV-SW | [R1 §3.10](#r1) | Section 3.10 |
| EV-SW-TIMING | [R3 Mandatory reporting, SW paragraph](#r3) | Mandatory reporting - CALDOVREP: SW passage paragraph |
| EV-AMENDMENT | [R2 commencement paragraph; Appendix (PDF pp.2–3)](#r2) | PDF page 2 paragraph 2; PDF page 3 clause 3 and Appendix |
| EV-OLD-LIST | [R3 Mandatory reporting, content list](#r3) | Mandatory reporting - CALDOVREP: report-content bullets |
| EV-CHANGE | [R4 Annex 2 §3.3](#r4) | Annex 2 section 3.3; PDF page 12 / printed Annex 16 page 11 |
| EV-AIS | [R3 Mandatory reporting, communications](#r3) | Mandatory reporting - CALDOVREP: AIS and ALRS paragraphs |
| EV-RS | [R5 deconstruction account](#r5) | 1 October 2023; deconstruction account |
| EV-FUTURE | [R8 PDF pp.1–2](#r8) | PDF pages 1-2; Routeing measures / Ship Reporting System in Europe |
| EV-PORT | [R7 VTS Information; Entry procedure](#r7) | VTS Information; Entry procedure |
| EV-F01 | [R2 Appendix, item A (PDF p.3)](#r2) | PDF page 3 / printed Annex 29 page 2; clause 3 and Appendix, A item |
| EV-F02 | [R2 Appendix, item B (PDF p.3)](#r2) | PDF page 3 / printed Annex 29 page 2; clause 3 and Appendix, B item |
| EV-F03 | [R2 Appendix, item C or D (PDF p.3)](#r2) | PDF page 3 / printed Annex 29 page 2; clause 3 and Appendix, C or D item |
| EV-F04 | [R2 Appendix, item E (PDF p.3)](#r2) | PDF page 3 / printed Annex 29 page 2; clause 3 and Appendix, E item |
| EV-F05 | [R2 Appendix, item F (PDF p.3)](#r2) | PDF page 3 / printed Annex 29 page 2; clause 3 and Appendix, F item |
| EV-F06 | [R2 Appendix, item G (PDF p.3)](#r2) | PDF page 3 / printed Annex 29 page 2; clause 3 and Appendix, G item |
| EV-F07 | [R2 Appendix, item I (PDF p.3)](#r2) | PDF page 3 / printed Annex 29 page 2; clause 3 and Appendix, I item |
| EV-F08 | [R2 Appendix, item O (PDF p.3)](#r2) | PDF page 3 / printed Annex 29 page 2; clause 3 and Appendix, O item |
| EV-F09 | [R2 Appendix, item P (PDF p.3)](#r2) | PDF page 3 / printed Annex 29 page 2; clause 3 and Appendix, P item |
| EV-F10 | [R2 Appendix, item Q or R (PDF p.3)](#r2) | PDF page 3 / printed Annex 29 page 2; clause 3 and Appendix, Q or R item |
| EV-F11 | [R2 Appendix, item T (PDF p.3)](#r2) | PDF page 3 / printed Annex 29 page 2; clause 3 and Appendix, T item |
| EV-F12 | [R2 Appendix, item W (PDF p.3)](#r2) | PDF page 3 / printed Annex 29 page 2; clause 3 and Appendix, W item |
| EV-F13 | [R2 Appendix, item X (PDF p.3)](#r2) | PDF page 3 / printed Annex 29 page 2; clause 3 and Appendix, X item |
| EV-CARGO-OPTION | [R4 Annex 2 §§3, 5](#r4) | Annex 2 section 3 opening paragraph, PDF page 11; section 5, PDF page 13 |
| EV-ITZ-MGN | [R1 §3.4](#r1) | Section 3.4 |
| EV-ITZ-DETAIL | [R3 Inshore traffic zones, final paragraph](#r3) | Inshore traffic zones, final notification paragraph |
| EV-FORMAT-ROUTE | [R6 Appendix §2 (PDF pp.7–9)](#r6) | Appendix paragraph 2, PDF pages 7-9; read with P01-IMO85 Annex 2 section 3.1 |

### A.3 Event-to-section crosswalk

| Event ID | Direction | Event type | Readable location |
| --- | --- | --- | --- |
| NE-ENTRY | North-eastbound | ENTRY | Section 3.1 |
| NE-CHANGE | North-eastbound | CONDITIONAL | Section 6.1 |
| NE-ITZ-DECISION | North-eastbound | CONDITIONAL | Section 6.2 |
| SW-ENTRY | South-westbound | ENTRY | Section 3.2 |
| SW-CHANGE | South-westbound | CONDITIONAL | Section 6.1 |
| SW-ITZ-DECISION | South-westbound | CONDITIONAL | Section 6.2 |
