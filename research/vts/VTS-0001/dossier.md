---
schema_version: "1.0-draft"
vts_id: VTS-0001
study_id: PILOT-01
region_code: BIS
project_class: Core
research_state: HOLD
provenance: MIXED_HELD_AND_LIVE_SOURCE_RESEARCH

guide_area:
  area_id: P01-AREA
  publication_title: "Channel VTS / CALDOVREP: directional reporting research sample"
  official_service_name: Channel VTS
  region_code: BIS
  countries: [United Kingdom, France]
  associated_service_ids: [VTS-0001]
  related_tss_ids: [TSS-0038]
  geographical_scope: "NE-bound and SW-bound through-transits and approach reporting. Harbour-entry and crossing variants are not fully developed."
  authority: "UK and French maritime authorities; current administrative titles require publication review."
  provider: "Dover MRCC and CROSS Gris-Nez"
  evidence_ids: [EV-IDENTITY]

participation:
  applicability_as_published: "All vessels of 300GT and over"
  exemptions_as_published: "Whatever their nationality, naval vessels are also exempt from reporting"
  requirement_strength: MANDATORY
  evidence_ids: [EV-THRESHOLD, EV-EXEMPT]

reporting_objects:
  - object_id: OBJ-WEST
    official_name: null
    graphic_label: Western reporting line
    geometry_type: LINE
    geometry_as_published: "Line from the Royal Sovereign light tower, through the Bassurelle Light Buoy (at its assigned position of 50°32’.8N, 000°57’.8E) to the coast of France."
    datum_as_published: null
    sector_id: null
    evidence_ids: [EV-NE]
  - object_id: OBJ-EAST
    official_name: null
    graphic_label: Eastern reporting line
    geometry_type: LINE
    geometry_as_published: "Line drawn from North Foreland Light (51° 23’N; 001° 27’E) to the border between France and Belgium (51° 05’N; 002° 33’E)."
    datum_as_published: null
    sector_id: null
    evidence_ids: [EV-SW]

communications:
  - contact_id: COM-GRISNEZ
    recipient: CROSS Gris-Nez
    call_sign: Gris-Nez Traffic
    communication_method: VHF voice
    calling_channel: "13"
    working_channel: "13"
    listening_watch: null
    alternative_method: null
    evidence_ids: [EV-NE]
  - contact_id: COM-DOVER
    recipient: Dover MRCC
    call_sign: Dover Coastguard
    communication_method: VHF voice
    calling_channel: "11"
    working_channel: "11"
    listening_watch: null
    alternative_method: null
    evidence_ids: [EV-SW]

report_types:
  - report_type_id: RT-CALDOVREP
    official_name: CALDOVREP
    fields:
      - {field_id: FLD-01, sequence: 1, code_as_published: "A", information_required: "Vessel name, radio call sign and IMO identifier; MMSI may identify a transponder report.", requirement_strength: MANDATORY, applicability_condition: "MMSI alternative concerns transponder reporting.", evidence_ids: [EV-F01]}
      - {field_id: FLD-02, sequence: 2, code_as_published: "B", information_required: "Reporting date and time.", requirement_strength: MANDATORY, applicability_condition: null, evidence_ids: [EV-F02]}
      - {field_id: FLD-03, sequence: 3, code_as_published: "C or D", information_required: "Position: latitude/longitude, or true bearing and distance from an identified landmark.", requirement_strength: MANDATORY, applicability_condition: "Alternative position expressions; not two compulsory position reports.", evidence_ids: [EV-F03]}
      - {field_id: FLD-04, sequence: 4, code_as_published: "E", information_required: "Course referenced to true north.", requirement_strength: MANDATORY, applicability_condition: null, evidence_ids: [EV-F04]}
      - {field_id: FLD-05, sequence: 5, code_as_published: "F", information_required: "Vessel speed.", requirement_strength: MANDATORY, applicability_condition: null, evidence_ids: [EV-F05]}
      - {field_id: FLD-06, sequence: 6, code_as_published: "G", information_required: "Departure port.", requirement_strength: MANDATORY, applicability_condition: null, evidence_ids: [EV-F06]}
      - {field_id: FLD-07, sequence: 7, code_as_published: "I", information_required: "Destination port with arrival estimate.", requirement_strength: MANDATORY, applicability_condition: null, evidence_ids: [EV-F07]}
      - {field_id: FLD-08, sequence: 8, code_as_published: "O", information_required: "Current draught.", requirement_strength: MANDATORY, applicability_condition: null, evidence_ids: [EV-F08]}
      - {field_id: FLD-09, sequence: 9, code_as_published: "P", information_required: "Cargo; add dangerous-goods quantity and IMO class when applicable.", requirement_strength: MANDATORY, applicability_condition: "Dangerous-goods particulars depend on cargo carried.", evidence_ids: [EV-F09]}
      - {field_id: FLD-10, sequence: 10, code_as_published: "Q or R", information_required: "Faults or other circumstances affecting normal navigation under SOLAS or MARPOL.", requirement_strength: MANDATORY, applicability_condition: "Preserve applicable defects and circumstances; no assumed nil-report convention.", evidence_ids: [EV-F10]}
      - {field_id: FLD-11, sequence: 11, code_as_published: "T", information_required: "Contact address for dangerous-cargo particulars.", requirement_strength: MANDATORY, applicability_condition: "Dangerous-cargo information purpose; nil-report handling not established.", evidence_ids: [EV-F11]}
      - {field_id: FLD-12, sequence: 12, code_as_published: "W", information_required: "Persons carried aboard.", requirement_strength: MANDATORY, applicability_condition: null, evidence_ids: [EV-F12]}
      - {field_id: FLD-13, sequence: 13, code_as_published: "X", information_required: "Navigation conditions; bunker estimate and characteristics when bunker quantity exceeds 5,000 tonnes.", requirement_strength: MANDATORY, applicability_condition: "The bunker condition is greater than 5,000 tonnes of bunkers, not vessel GT.", evidence_ids: [EV-F13]}
  - report_type_id: RT-CHANGE
    official_name: null
    fields:
      - field_id: FLD-CHANGE
        sequence: 1
        code_as_published: "Q or R"
        information_required: "Changed navigation circumstances, particularly defects and other circumstances under Q/R."
        requirement_strength: UNKNOWN
        applicability_condition: "The source says should. No new formal report title or full-repeat requirement is asserted."
        evidence_ids: [EV-CHANGE]

directions:
  - direction_id: P01-NE
    direction_label: North-eastbound
    route_variant: Through-transit
    geographical_scope: "Approach to and transit through CALDOVREP. No approved track is supplied."
    vessel_applicability: "Ships of 300 GT and over, subject to applicable exemptions."
    reporting_events:
      - event_id: NE-ENTRY
        sequence: 1
        reporting_object_id: OBJ-WEST
        trigger_as_published: "Crossing the western reporting line"
        timing_as_published: "two (2) nautical miles before crossing"
        requirement_strength: MANDATORY
        vessel_applicability: "Ships of 300 GT and over, subject to applicable exemptions."
        contact_id: COM-GRISNEZ
        report_type_id: RT-CALDOVREP
        exceptions: "Naval and ferry arrangements require their stated conditions. AIS carriage is not treated as an automatic exemption."
        subsequent_action: null
        evidence_ids: [EV-NE, EV-THRESHOLD, EV-AMENDMENT, EV-EXEMPT]
      - event_id: NE-CHANGE
        sequence: 2
        reporting_object_id: null
        trigger_as_published: "whenever there is a change of navigational circumstance"
        timing_as_published: null
        requirement_strength: UNKNOWN
        vessel_applicability: "Participating vessel; conditional event, not a routine second report."
        contact_id: null
        report_type_id: RT-CHANGE
        exceptions: null
        subsequent_action: "Relevant shore station is the source wording. Recipient selection and urgency routing require G05 review."
        evidence_ids: [EV-CHANGE]
    spread:
      spread_id: P01-SPREAD-NE
      title: "Channel VTS / CALDOVREP: NE-bound"
      layout: DOUBLE_PAGE
      map_extent: null
      reporting_object_ids: [OBJ-WEST]
      reporting_event_ids: [NE-ENTRY, NE-CHANGE]
      graphics_dataset_path: null
      base_material_reference: null
      reproduction_permission_record: null
  - direction_id: P01-SW
    direction_label: South-westbound
    route_variant: Through-transit
    geographical_scope: "Approach to and transit through CALDOVREP. No approved track is supplied."
    vessel_applicability: "Ships of 300 GT and over, subject to applicable exemptions."
    reporting_events:
      - event_id: SW-ENTRY
        sequence: 1
        reporting_object_id: OBJ-EAST
        trigger_as_published: "Crossing the eastern reporting line"
        timing_as_published: "not later than crossing"
        requirement_strength: MANDATORY
        vessel_applicability: "Ships of 300 GT and over, subject to applicable exemptions."
        contact_id: COM-DOVER
        report_type_id: RT-CALDOVREP
        exceptions: "Naval and ferry arrangements require their stated conditions. AIS carriage is not treated as an automatic exemption."
        subsequent_action: null
        evidence_ids: [EV-SW, EV-THRESHOLD, EV-AMENDMENT, EV-EXEMPT]
      - event_id: SW-CHANGE
        sequence: 2
        reporting_object_id: null
        trigger_as_published: "whenever there is a change of navigational circumstance"
        timing_as_published: null
        requirement_strength: UNKNOWN
        vessel_applicability: "Participating vessel; conditional event, not a routine second report."
        contact_id: null
        report_type_id: RT-CHANGE
        exceptions: null
        subsequent_action: "Relevant shore station is the source wording. Recipient selection and urgency routing require G05 review."
        evidence_ids: [EV-CHANGE]
    spread:
      spread_id: P01-SPREAD-SW
      title: "Channel VTS / CALDOVREP: SW-bound"
      layout: DOUBLE_PAGE
      map_extent: null
      reporting_object_ids: [OBJ-EAST]
      reporting_event_ids: [SW-ENTRY, SW-CHANGE]
      graphics_dataset_path: null
      base_material_reference: null
      reproduction_permission_record: null

evidence:
  - {evidence_id: EV-IDENTITY, source_id: SRC-004, snapshot_id: SRC-004__20261002T163852Z__2e5ab12c2a39, source_locator: "About the Dover Strait; How Channel VTS works", supported_field_paths: [guide_area], wording_as_published: null, effective_from: null, effective_until: null, verification_state: AUTHOR_CHECKED}
  - {evidence_id: EV-THRESHOLD, source_id: SRC-005, snapshot_id: SRC-005__20261002T163852Z__1cafaed9fae8, source_locator: "Sections 3.7-3.9", supported_field_paths: [participation.applicability_as_published], wording_as_published: "All vessels of 300GT and over", effective_from: null, effective_until: null, verification_state: AUTHOR_CHECKED}
  - {evidence_id: EV-THRESHOLD-IMO, source_id: P01-IMO85, snapshot_id: null, source_locator: "Annex 2 section 1; PDF page 10 / printed Annex 16 page 9", supported_field_paths: [participation.applicability_as_published], wording_as_published: null, effective_from: null, effective_until: null, verification_state: AUTHOR_CHECKED}
  - {evidence_id: EV-EXEMPT, source_id: SRC-004, snapshot_id: SRC-004__20261002T163852Z__2e5ab12c2a39, source_locator: "Exemptions from the CALDOVREP scheme", supported_field_paths: [participation.exemptions_as_published], wording_as_published: null, effective_from: null, effective_until: null, verification_state: AUTHOR_CHECKED}
  - {evidence_id: EV-FERRY, source_id: P01-IMO85, snapshot_id: null, source_locator: "Annex 2 section 3.3, Crossing Traffic; PDF page 12 / printed Annex 16 page 11", supported_field_paths: ["conflicts[C03]"], wording_as_published: null, effective_from: null, effective_until: null, verification_state: AUTHOR_CHECKED}
  - {evidence_id: EV-NE, source_id: SRC-005, snapshot_id: SRC-005__20261002T163852Z__1cafaed9fae8, source_locator: "Section 3.11", supported_field_paths: ["reporting_objects[OBJ-WEST]", "communications[COM-GRISNEZ]", "directions[P01-NE].reporting_events[NE-ENTRY]"], wording_as_published: null, effective_from: null, effective_until: null, verification_state: AUTHOR_CHECKED}
  - {evidence_id: EV-SW, source_id: SRC-005, snapshot_id: SRC-005__20261002T163852Z__1cafaed9fae8, source_locator: "Section 3.10", supported_field_paths: ["reporting_objects[OBJ-EAST]", "communications[COM-DOVER]", "directions[P01-SW].reporting_events[SW-ENTRY]"], wording_as_published: null, effective_from: null, effective_until: null, verification_state: AUTHOR_CHECKED}
  - {evidence_id: EV-SW-TIMING, source_id: SRC-004, snapshot_id: SRC-004__20261002T163852Z__2e5ab12c2a39, source_locator: "Mandatory reporting - CALDOVREP: SW passage paragraph", supported_field_paths: ["conflicts[C04]"], wording_as_published: null, effective_from: null, effective_until: null, verification_state: AUTHOR_CHECKED}
  - {evidence_id: EV-AMENDMENT, source_id: P01-IMO251, snapshot_id: null, source_locator: "PDF page 2 paragraph 2; PDF page 3 clause 3 and Appendix", supported_field_paths: ["report_types[RT-CALDOVREP]"], wording_as_published: null, effective_from: "2008-05-01T00:00:00Z", effective_until: null, verification_state: AUTHOR_CHECKED}
  - {evidence_id: EV-OLD-LIST, source_id: SRC-004, snapshot_id: SRC-004__20261002T163852Z__2e5ab12c2a39, source_locator: "Mandatory reporting - CALDOVREP: report-content bullets", supported_field_paths: ["conflicts[C02]"], wording_as_published: null, effective_from: null, effective_until: null, verification_state: AUTHOR_CHECKED}
  - {evidence_id: EV-CHANGE, source_id: P01-IMO85, snapshot_id: null, source_locator: "Annex 2 section 3.3; PDF page 12 / printed Annex 16 page 11", supported_field_paths: ["report_types[RT-CHANGE]", "directions[P01-NE].reporting_events[NE-CHANGE]", "directions[P01-SW].reporting_events[SW-CHANGE]"], wording_as_published: null, effective_from: null, effective_until: null, verification_state: AUTHOR_CHECKED}
  - {evidence_id: EV-AIS, source_id: SRC-004, snapshot_id: SRC-004__20261002T163852Z__2e5ab12c2a39, source_locator: "Mandatory reporting - CALDOVREP: AIS and ALRS paragraphs", supported_field_paths: ["gaps[G04]"], wording_as_published: null, effective_from: null, effective_until: null, verification_state: AUTHOR_CHECKED}
  - {evidence_id: EV-RS, source_id: P01-TH-RS, snapshot_id: null, source_locator: "1 October 2023; deconstruction account", supported_field_paths: ["gaps[G02]"], wording_as_published: null, effective_from: null, effective_until: null, verification_state: AUTHOR_CHECKED}
  - {evidence_id: EV-FUTURE, source_id: P01-LIB-NCSR13, snapshot_id: null, source_locator: "PDF pages 1-2; Routeing measures / Ship Reporting System in Europe", supported_field_paths: ["gaps[G03]"], wording_as_published: null, effective_from: null, effective_until: null, verification_state: AUTHOR_CHECKED}
  - {evidence_id: EV-PORT, source_id: P01-DOVER-PORT, snapshot_id: null, source_locator: "VTS Information; Entry procedure", supported_field_paths: ["gaps[G03]"], wording_as_published: null, effective_from: null, effective_until: null, verification_state: AUTHOR_CHECKED}
  - {evidence_id: EV-F01, source_id: P01-IMO251, snapshot_id: null, source_locator: "PDF page 3 / printed Annex 29 page 2; clause 3 and Appendix, A item", supported_field_paths: ["report_types[RT-CALDOVREP].fields[FLD-01]"], wording_as_published: null, effective_from: "2008-05-01T00:00:00Z", effective_until: null, verification_state: AUTHOR_CHECKED}
  - {evidence_id: EV-F02, source_id: P01-IMO251, snapshot_id: null, source_locator: "PDF page 3 / printed Annex 29 page 2; clause 3 and Appendix, B item", supported_field_paths: ["report_types[RT-CALDOVREP].fields[FLD-02]"], wording_as_published: null, effective_from: "2008-05-01T00:00:00Z", effective_until: null, verification_state: AUTHOR_CHECKED}
  - {evidence_id: EV-F03, source_id: P01-IMO251, snapshot_id: null, source_locator: "PDF page 3 / printed Annex 29 page 2; clause 3 and Appendix, C or D item", supported_field_paths: ["report_types[RT-CALDOVREP].fields[FLD-03]"], wording_as_published: null, effective_from: "2008-05-01T00:00:00Z", effective_until: null, verification_state: AUTHOR_CHECKED}
  - {evidence_id: EV-F04, source_id: P01-IMO251, snapshot_id: null, source_locator: "PDF page 3 / printed Annex 29 page 2; clause 3 and Appendix, E item", supported_field_paths: ["report_types[RT-CALDOVREP].fields[FLD-04]"], wording_as_published: null, effective_from: "2008-05-01T00:00:00Z", effective_until: null, verification_state: AUTHOR_CHECKED}
  - {evidence_id: EV-F05, source_id: P01-IMO251, snapshot_id: null, source_locator: "PDF page 3 / printed Annex 29 page 2; clause 3 and Appendix, F item", supported_field_paths: ["report_types[RT-CALDOVREP].fields[FLD-05]"], wording_as_published: null, effective_from: "2008-05-01T00:00:00Z", effective_until: null, verification_state: AUTHOR_CHECKED}
  - {evidence_id: EV-F06, source_id: P01-IMO251, snapshot_id: null, source_locator: "PDF page 3 / printed Annex 29 page 2; clause 3 and Appendix, G item", supported_field_paths: ["report_types[RT-CALDOVREP].fields[FLD-06]"], wording_as_published: null, effective_from: "2008-05-01T00:00:00Z", effective_until: null, verification_state: AUTHOR_CHECKED}
  - {evidence_id: EV-F07, source_id: P01-IMO251, snapshot_id: null, source_locator: "PDF page 3 / printed Annex 29 page 2; clause 3 and Appendix, I item", supported_field_paths: ["report_types[RT-CALDOVREP].fields[FLD-07]"], wording_as_published: null, effective_from: "2008-05-01T00:00:00Z", effective_until: null, verification_state: AUTHOR_CHECKED}
  - {evidence_id: EV-F08, source_id: P01-IMO251, snapshot_id: null, source_locator: "PDF page 3 / printed Annex 29 page 2; clause 3 and Appendix, O item", supported_field_paths: ["report_types[RT-CALDOVREP].fields[FLD-08]"], wording_as_published: null, effective_from: "2008-05-01T00:00:00Z", effective_until: null, verification_state: AUTHOR_CHECKED}
  - {evidence_id: EV-F09, source_id: P01-IMO251, snapshot_id: null, source_locator: "PDF page 3 / printed Annex 29 page 2; clause 3 and Appendix, P item", supported_field_paths: ["report_types[RT-CALDOVREP].fields[FLD-09]"], wording_as_published: null, effective_from: "2008-05-01T00:00:00Z", effective_until: null, verification_state: AUTHOR_CHECKED}
  - {evidence_id: EV-F10, source_id: P01-IMO251, snapshot_id: null, source_locator: "PDF page 3 / printed Annex 29 page 2; clause 3 and Appendix, Q or R item", supported_field_paths: ["report_types[RT-CALDOVREP].fields[FLD-10]"], wording_as_published: null, effective_from: "2008-05-01T00:00:00Z", effective_until: null, verification_state: AUTHOR_CHECKED}
  - {evidence_id: EV-F11, source_id: P01-IMO251, snapshot_id: null, source_locator: "PDF page 3 / printed Annex 29 page 2; clause 3 and Appendix, T item", supported_field_paths: ["report_types[RT-CALDOVREP].fields[FLD-11]"], wording_as_published: null, effective_from: "2008-05-01T00:00:00Z", effective_until: null, verification_state: AUTHOR_CHECKED}
  - {evidence_id: EV-F12, source_id: P01-IMO251, snapshot_id: null, source_locator: "PDF page 3 / printed Annex 29 page 2; clause 3 and Appendix, W item", supported_field_paths: ["report_types[RT-CALDOVREP].fields[FLD-12]"], wording_as_published: null, effective_from: "2008-05-01T00:00:00Z", effective_until: null, verification_state: AUTHOR_CHECKED}
  - {evidence_id: EV-F13, source_id: P01-IMO251, snapshot_id: null, source_locator: "PDF page 3 / printed Annex 29 page 2; clause 3 and Appendix, X item", supported_field_paths: ["report_types[RT-CALDOVREP].fields[FLD-13]"], wording_as_published: null, effective_from: "2008-05-01T00:00:00Z", effective_until: null, verification_state: AUTHOR_CHECKED}

gaps:
  - gap_id: G01
    affected_field_paths: ["evidence[*].snapshot_id", assurance.independent_review_record]
    missing_information: Retained copies of the live-only sources
    reason: Two MCA sources are held; IMO and supporting originals were read live but are not in the frozen packet.
    severity: BLOCKER
    disposition: OPEN
    next_action: Obtain permitted review copies, snapshot IDs, hashes and required renders before independent packet review.
    resolution_evidence_ids: []
    decision_record: null
  - gap_id: G02
    affected_field_paths: ["reporting_objects[*].datum_as_published", "reporting_objects[OBJ-WEST]", "directions[*].spread"]
    missing_information: Current full reporting-line geometry, reference feature and datums
    reason: MGN gives a verbal western line and one assigned buoy position. Royal Sovereign topsides were removed in 2023.
    severity: BLOCKER
    disposition: OPEN
    next_action: Check corrected official chart/ALRS and competent authority. Do not substitute a buoy or infer endpoints.
    resolution_evidence_ids: []
    decision_record: null
  - gap_id: G03
    affected_field_paths: [assurance.subsequent_notices_check, "communications[COM-DOVER].call_sign"]
    missing_information: Complete notice/ALRS/French-instruction reconciliation and current UK call-name confirmation
    reason: MCA publishes Dover Coastguard while the service is branded Channel VTS. A 2026 meeting report flags future amendments.
    severity: BLOCKER
    disposition: OPEN
    next_action: Obtain current ALRS 6(1), official amendments and provider clarification where needed. Keep harbour Dover VTS separate.
    resolution_evidence_ids: []
    decision_record: null
  - gap_id: G04
    affected_field_paths: ["communications[*].listening_watch", "communications[*].alternative_method"]
    missing_information: Current listening-watch, AIS acceptance and alternative/failure communication details
    reason: MCA refers readers to ALRS and identifies Dover AIS capability without a complete field-level exemption procedure.
    severity: BLOCKER
    disposition: OPEN
    next_action: Acquire detailed instructions. Do not invent a universal AIS exemption or a routine exit or transfer report.
    resolution_evidence_ids: []
    decision_record: null
  - gap_id: G05
    affected_field_paths: ["directions[P01-NE].reporting_events[NE-CHANGE]", "directions[P01-SW].reporting_events[SW-CHANGE]"]
    missing_information: Exact recipient, obligation strength and urgency routing for conditional changes
    reason: Base IMO instrument says should and relevant shore station; current implementation not fully reconciled.
    severity: ERROR
    disposition: OPEN
    next_action: Check provider instructions and national duties; retain the trigger without inventing a normal second-report point.
    resolution_evidence_ids: []
    decision_record: null
  - gap_id: G06
    affected_field_paths: ["report_types[RT-CALDOVREP].fields"]
    missing_information: Full encoding, units, time standard and nil-report conventions
    reason: Field subjects established from amendment; this sample does not supply a fully encoded bridge message.
    severity: ERROR
    disposition: OPEN
    next_action: Check the current A.851-based format and provider/ALRS instructions before publishing a worked message.
    resolution_evidence_ids: []
    decision_record: null
  - gap_id: G07
    affected_field_paths: [assurance.marine_approval_record, assurance.artwork_check_record, assurance.release_record]
    missing_information: Independent evidence review, marine approval and graphic checks
    reason: This is an author research sample; no independent reviewer or released artwork exists.
    severity: BLOCKER
    disposition: OPEN
    next_action: Review the completed frozen packet and resolve findings before producing directional PDF prototypes.
    resolution_evidence_ids: []
    decision_record: null

conflicts:
  - conflict_id: C01
    affected_fields: [participation.applicability_as_published]
    assertions:
      - {source_id: SRC-004, assertion: "Over 300 gross tonnes"}
      - {source_id: SRC-005, assertion: "300GT and over", evidence_ids: [EV-THRESHOLD]}
      - {source_id: P01-IMO85, assertion: "300 GT inclusive", evidence_ids: [EV-THRESHOLD-IMO]}
    disposition: AUTHOR_RESOLVED_PENDING_REVIEW
    decision: Use inclusive 300 GT threshold; specific MCA guidance agrees with the adopted participation clause. Preserve the discrepant summary.
    reviewer: null
  - conflict_id: C02
    affected_fields: ["report_types[RT-CALDOVREP]"]
    assertions:
      - {source_id: SRC-004, assertion: "Shorter summary includes route information and omits amended code groups.", evidence_ids: [EV-OLD-LIST]}
      - {source_id: P01-IMO251, assertion: "Explicit replacement of section 3.2 and summary section 4, effective 1 May 2008.", evidence_ids: [EV-AMENDMENT]}
    disposition: AUTHOR_RESOLVED_PENDING_REVIEW
    decision: Use the 13 amended groups for this sample. Do not retain L as mandatory from the old summary. Later amendments remain G03.
    reviewer: null
  - conflict_id: C03
    affected_fields: ["directions[*].reporting_events[*].exceptions"]
    assertions:
      - {source_id: SRC-004, assertion: "Regular scheduled ferries receive simplified treatment.", evidence_ids: [EV-EXEMPT]}
      - {source_id: P01-IMO85, assertion: "Special arrangements need ship-specific approval by both stations.", evidence_ids: [EV-FERRY]}
    disposition: AUTHOR_RESOLVED_PENDING_REVIEW
    decision: Do not turn the short summary into a blanket ferry exemption. Ferry routes are outside this through-transit sample.
    reviewer: null
  - conflict_id: C04
    affected_fields: ["directions[P01-SW].reporting_events[SW-ENTRY].timing_as_published"]
    assertions:
      - {source_id: SRC-004, assertion: "Within VHF range and before crossing.", evidence_ids: [EV-SW-TIMING]}
      - {source_id: SRC-005, assertion: "Not later than crossing.", evidence_ids: [EV-SW]}
    disposition: AUTHOR_RECONCILED_PENDING_REVIEW
    decision: Preserve both phrasings. Summary uses within range, before entry; YAML retains MGN timing. Do not infer a two-mile SW trigger.
    reviewer: null

assurance:
  research_cutoff_utc: "2026-10-02T16:46:33+00:00"
  subsequent_notices_check: "PARTIAL: MCA pages and targeted amendment search consulted; complete ALRS/UKHO/French notice reconciliation outstanding. See G03."
  independent_review_record: null
  marine_approval_record: null
  artwork_check_record: null
  release_record: null
production:
  research_revision: "0.1.0-author-sample"
  schema_revision: "1.0-draft"
  style_sheet_revision: null
  effort_record: author_check.json
  pdf_output_paths: []
---

# Channel VTS / CALDOVREP

**Research sample 0.1.0 | 2 October 2026 | HOLD: not for navigation or publication**

## 1. Scope

One service, VTS-0001, with separate north-eastbound and south-westbound through-transit research.
This is not a passage plan or a complete operational guide.
Core classification and TSS-0038 association are inherited inventory records, not newly certified findings.

Channel VTS is jointly operated from Dover MRCC and CROSS Gris-Nez. [SRC-004, About the Dover Strait]
Port of Dover's harbour VTS is a different service. Its port-entry procedures are excluded. [P01-DOVER-PORT, VTS Information]

## 2. Directional entry reports

These are published instructions recorded for research, pending the holds below. This is not a bridge-use reporting card.

| Direction | Published entry trigger | Published recipient / voice channel | Evidence |
|---|---|---|---|
| NE-bound | Two NM before the western reporting line | Gris-Nez Traffic / VHF 13 | SRC-005, 3.11 |
| SW-bound | Within VHF range of North Foreland, before entry; MGN says no later than crossing | Dover Coastguard / VHF 11 | SRC-004, Mandatory reporting; SRC-005, 3.10 |

Each entry event links to the CALDOVREP report type in YAML.
The NE two-mile trigger must not be copied to SW traffic.
The second event in each direction is conditional on changed navigation circumstances, not a routine second position report.
[P01-IMO85, Annex 2, 3.3]

## 3. Required information

MSC.251(83) expressly replaces the original CALDOVREP report-content clause and summary.
Its 13 code groups are A, B, C or D, E, F, G, I, O, P, Q or R, T, W and X.
The amendment took effect on 1 May 2008. [P01-IMO251, PDF pages 2-3, adoption paragraph 2 and Annex clause 3/Appendix]

Each YAML field has its own evidence reference and source item locator.
The field descriptions are paraphrases, not a complete encoded radio message.
The bunker condition in X concerns more than 5,000 tonnes of bunker fuel, not vessel gross tonnage.
[P01-IMO251, Appendix, X]

The current MCA summary is shorter than the amended list. Copying that summary alone would omit reporting information.
This discrepancy is retained in C02. [SRC-004, Mandatory reporting; P01-IMO251, clause 3/Appendix]

## 4. Exceptions and conditions

Participation starts at 300 GT inclusive. Specific MCA guidance and the adopted clause agree.
The shorter MCA webpage instead says over 300 GT. C01 preserves that distinction.
[SRC-005, 3.8; P01-IMO85, Annex 2, 1; SRC-004, Mandatory reporting]

Naval vessels are exempt under the MCA summary. [SRC-004, Exemptions: Naval vessels]
Ferry special arrangements require ship-specific approval by both stations under the original scheme.
They must not become a blanket exemption. [P01-IMO85, Annex 2, 3.3, Crossing Traffic]

Smaller vessels have separate conditional reporting guidance, not universal mandatory participation in this sample.
[SRC-005, 3.9; P01-IMO85, Annex 2, 1]
Dover AIS capability does not establish a universal exemption from voice reporting. Details remain G04.
[SRC-004, Mandatory reporting: communications paragraphs]

## 5. Geometry and artwork

Both reporting boundaries remain lines. No missing endpoint, assumed datum or approved track has been invented.
[SRC-005, 3.10-3.11]

The western description still references Royal Sovereign light tower. Trinity House records its topsides removal in October 2023.
That does not itself relocate or cancel the reporting line. Its current charted reference needs checking before drawing.
[P01-TH-RS, 1 October 2023; SRC-005, 3.11]

No graphic or PDF spread has been produced. The two spread records define intended output scope only.

## 6. Source pack and currency

Two MCA HTML originals and mechanical text extractions are held in the repository.
The capture log records retrieval times, byte counts and SHA-256 values.
The author read their relevant archived sections against the live authority pages.
No independent evidence review has occurred.

The IMO resolutions and supporting sources were inspected live but are not archived in this packet.
Their snapshot IDs remain null. Permitted retained copies are a review prerequisite, not an assumed possession.

The Liberian Registry's NCSR 13 account flags proposed CALDOVREP changes for later MSC adoption.
It is a prospective change lead, not authority to add new reporting duties now.
[P01-LIB-NCSR13, PDF pages 1-2, Routeing measures / Ship Reporting System in Europe]

Current ALRS, the full UKHO/French notices chain and current call-name convention require reconciliation before release.
No claim is made that all applicable reporting requirements have been exhausted.

## 7. Review disposition

Four author dispositions address the threshold, amended report content, ferry treatment and SW timing.
Seven open gaps remain in YAML, covering retained evidence, geometry, notices, communications, conditional updates, formatting and approval.

HOLD is a publication-research state. It does not change the existing 76-service inventory.
The next gate is a complete retained source packet and independent evidence/marine review before directional PDF production.

## 8. Sources and records

See `source_catalogue.json` for URLs, titles, issuers, dates, locators and held/live-only status.
P01-prefixed source IDs are pilot-local; reconcile them with the shared register before wider production.
Existing global IDs SRC-004 and SRC-005 are retained.

`packet.json` records exact research/source inputs and explicit missing originals.
`author_check.json` records structural checks and limitations; it is not independent approval.
The source-first protocol and YAML specification continue to apply.
