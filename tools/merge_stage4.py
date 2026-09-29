"""Merge Stage 4 research findings (batches B10 to B34) into the v0.3 inventory.

Inputs:  research/stage4/raw/<group>.json  (one file per research group, A to G)
         data/archive/v0_2/Global_VTS_Inventory_v0_2.xlsx
Outputs: data/current/Global_VTS_Inventory_v0_3.xlsx
         data/current/Global_VTS_TSS_Candidates_v0_3.csv
         research/stage4/stage4_findings_v0_3.csv
         research/stage4/merge_log.md

Audit adjustments made at merge are listed in ADJUST and written to the log,
so every change from the raw research output is traceable.
"""
import copy
import csv
import glob
import json
import os
from datetime import date

import openpyxl
from openpyxl.worksheet.datavalidation import DataValidation

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "research", "stage4", "raw")
SRC_WB = os.path.join(ROOT, "data", "archive", "v0_2", "Global_VTS_Inventory_v0_2.xlsx")
OUT_WB = os.path.join(ROOT, "data", "current", "Global_VTS_Inventory_v0_3.xlsx")
OUT_CSV = os.path.join(ROOT, "data", "current", "Global_VTS_TSS_Candidates_v0_3.csv")
OUT_FIND = os.path.join(ROOT, "research", "stage4", "stage4_findings_v0_3.csv")
OUT_LOG = os.path.join(ROOT, "research", "stage4", "merge_log.md")
TODAY = "2026-09-29"
VERSION_LINE = "Version 0.3 | 29 September 2026 | Stage 4 first-pass research of B10 to B34 added. Not a verified worldwide census."

# ---------------------------------------------------------------------------
# Canonical identities for services and schemes found by more than one group,
# or already held in v0.2. Keys not listed receive new sequential IDs.
# ---------------------------------------------------------------------------
SERVICE_CANON = {
    "SVC-klang-vts": "VTS-004",
    "SVC-johor-vts": "VTS-005",
    "SVC-singapore-vts": "VTS-006",
    "SVC-vts-prince-william-sound": "VTS-009",
    "SVC-vts-puget-sound": "VTS-010",
    "SVC-vts-san-francisco": "VTS-011",
    "SVC-vts-los-angeles-long-beach": "VTS-012",
    "SVC-vts-houston-galveston": "VTS-013",
    "SVC-vts-new-york": "VTS-014",
}
SERVICE_ALIAS = {
    # Same service reported under two keys by different groups.
    "SVC-tsvts": "SVC-turkish-straits-vts",
    "SVC-ccg-mcts-victoria-vts": "SVC-ccg-mcts-cvts-juan-de-fuca",
}
SCHEME_CANON = {
    "RPT-straitrep": "SRS-004",
    "RPT-sf-ovmrs": "SRS-008",
}
SCHEME_ALIAS = {}

# Reporting arrangements that are routine reporting inside a VTS or port service.
# Project rule: record under the service, do not count as a separate scheme.
NOT_SEPARATE_SCHEMES = {
    "RPT-de-anlbv-inner-german-bight": "Reports under AnlBV Anlage Nr. 3.1 and SeeSchStrO section 58 are made to German Bight Traffic, a VTS. Recorded under the service as VTS reporting duties (national statute, not an IMO-adopted scheme).",
    "RPT-de-seeschstro-elbe": "SeeSchStrO section 58 reports on the Elbe approach are made to the VTS centres. Recorded under the service as VTS reporting duties.",
    "RPT-ca-vts-zones": "Reporting under the Canadian Vessel Traffic Services Zones Regulations (SOR/2025-275) is the reporting duty of the VTS zone. Recorded under the Fundy Traffic and Canso Traffic services.",
    "RPT-acp-signal-station-reports": "Approach reports to the Panama Canal Authority signal stations are port and canal arrival reporting. Recorded as an applicability note, not as a separate mandatory reporting scheme.",
}

# Audit adjustments made on review of the raw findings: (record_id, field, new_value, reason)
ADJUST = [
    ("TSS-0101", "vts_finding", "Unresolved",
     "Only evidence is a temporary 2023 ADNOC notice that does not state the Das VTIS area; not sufficient for current coverage. Das VTIS retained as a lead."),
    ("TSS-0067", "reporting_finding", "Unresolved",
     "Absence rests on a Ministry of Transport magazine article, not a formal complete list. Record the voluntary Cabo de Gata system; confirm absence of mandatory reporting against ALRS Vol 6 or IMO SN.1/Circ.",),
    ("TSS-0068", "reporting_finding", "Unresolved",
     "Absence rests on an enumerative magazine statement (researcher rated moderate confidence). Not sufficient for Confirmed absent."),
    ("TSS-0069", "reporting_finding", "Unresolved",
     "Absence rests on an enumerative magazine statement (researcher rated moderate confidence). Not sufficient for Confirmed absent."),
]


# ---------------------------------------------------------------------------
def load_groups():
    groups = {}
    for path in sorted(glob.glob(os.path.join(RAW, "*.json"))):
        g = os.path.splitext(os.path.basename(path))[0]
        groups[g] = json.load(open(path, encoding="utf-8"))
    return groups


def main(apply_adjustments):
    groups = load_groups()
    wb = openpyxl.load_workbook(SRC_WB)
    log = []

    # ---------------- sources: map group-local IDs to global SRC IDs --------
    ws_src = wb["Sources"]
    existing_src = {}
    last_src = 0
    for r in ws_src.iter_rows(min_row=7, values_only=True):
        if r[0]:
            existing_src[(r[3] or "").strip()] = r[0]
            last_src = max(last_src, int(r[0].split("-")[1]))
    src_map = {}  # (group, local id) -> SRC id
    src_rows = {}  # SRC id -> row data
    src_url = {}
    for g, d in groups.items():
        for s in d["sources"]:
            url = (s.get("url") or "").strip()
            if url in existing_src:
                sid = existing_src[url]
            else:
                last_src += 1
                sid = f"SRC-{last_src:03d}"
                existing_src[url] = sid
                src_rows[sid] = s
            src_map[(g, s["id"])] = sid
            src_url[sid] = url

    def gsrc(g, ids):
        out = []
        for i in ids or []:
            sid = src_map.get((g, i))
            if sid and sid not in out:
                out.append(sid)
        return out

    # ---------------- services ---------------------------------------------
    last_vts = max(int(r[0].split("-")[1]) for r in wb["VTS Services"].iter_rows(min_row=7, values_only=True) if r[0])
    svc_id = dict(SERVICE_CANON)
    svc_info = {}
    for g, d in groups.items():
        for s in d["services"]:
            key = SERVICE_ALIAS.get(s["key"], s["key"])
            if key not in svc_id:
                last_vts += 1
                svc_id[key] = f"VTS-{last_vts:03d}"
            info = svc_info.setdefault(key, {"groups": [], "rec": s, "src": []})
            info["groups"].append(g)
            info["src"] += [x for x in gsrc(g, s.get("source_ids")) if x not in info["src"]]
            if s.get("evidence_status", "").startswith("Confirmed"):
                info["rec"] = s  # prefer a confirmed description

    def sid_of(key):
        return svc_id[SERVICE_ALIAS.get(key, key)]

    # ---------------- reporting schemes ------------------------------------
    last_srs = max(int(r[0].split("-")[1]) for r in wb["Reporting Schemes"].iter_rows(min_row=7, values_only=True) if r[0])
    rpt_id = dict(SCHEME_CANON)
    rpt_info = {}
    for g, d in groups.items():
        for s in d["reporting_schemes"]:
            key = SCHEME_ALIAS.get(s["key"], s["key"])
            if key in NOT_SEPARATE_SCHEMES:
                continue
            if key not in rpt_id:
                last_srs += 1
                rpt_id[key] = f"SRS-{last_srs:03d}"
            info = rpt_info.setdefault(key, {"groups": [], "rec": s, "src": [], "svc": []})
            info["groups"].append(g)
            info["src"] += [x for x in gsrc(g, s.get("source_ids")) if x not in info["src"]]
            for k in s.get("operating_service_keys") or []:
                k = SERVICE_ALIAS.get(k, k)
                if k in svc_id and svc_id[k] not in info["svc"]:
                    info["svc"].append(svc_id[k])

    # ---------------- records ----------------------------------------------
    records = {}
    for g, d in groups.items():
        for r in d["records"]:
            r = dict(r)
            r["_group"] = g
            r["_audit"] = []
            records[r["record_id"]] = r

    if apply_adjustments:
        for rid, field, value, reason in ADJUST:
            rec = records[rid]
            old = rec.get(field)
            rec[field] = value
            rec["_audit"].append(f"{field}: {old} -> {value}. {reason}")
            log.append(f"- **{rid}** `{field}`: {old} -> {value}. {reason}")

    # Reclassify reporting that is VTS/port reporting (project counting rule).
    for rid, rec in records.items():
        keys = rec.get("reporting_scheme_keys") or []
        moved = [k for k in keys if k in NOT_SEPARATE_SCHEMES]
        if moved:
            rec["reporting_scheme_keys"] = [k for k in keys if k not in NOT_SEPARATE_SCHEMES]
            note = " ".join(NOT_SEPARATE_SCHEMES[k] for k in moved)
            rec["applicability_notes"] = ((rec.get("applicability_notes") or "") + " " + note).strip()
            if not rec["reporting_scheme_keys"] and rec["reporting_finding"] == "Confirmed present":
                rec["reporting_finding"] = "Unresolved"
                msg = f"reporting_finding: Confirmed present -> Unresolved. {note} No separate mandatory scheme evidenced."
                rec["_audit"].append(msg)
                log.append(f"- **{rid}** {msg}")

    # ---------------- write TSS Candidates ---------------------------------
    ws = wb["TSS Candidates"]
    hdr = [c.value for c in ws[6]]
    col = {h: i + 1 for i, h in enumerate(hdr)}
    rel_rows = []
    comp_rows = []
    for row in range(7, ws.max_row + 1):
        rid = ws.cell(row, col["Record ID"]).value
        if rid not in records:
            continue
        rec = records[rid]
        g = rec["_group"]
        vts_ids = [sid_of(k) for k in rec.get("vts_service_keys") or []]
        rpt_ids = [rpt_id[k] for k in rec.get("reporting_scheme_keys") or [] if k in rpt_id]
        srcs = gsrc(g, rec.get("source_ids"))

        def screening(finding, ids, info_of):
            if not ids:
                return finding
            names = ", ".join(ids)
            if finding == "Confirmed present":
                return f"Confirmed present: {names}"
            return f"{finding} (lead: {names})"

        ws.cell(row, col["VTS screening"]).value = screening(rec["vts_finding"], vts_ids, svc_info)
        ws.cell(row, col["Reporting screening"]).value = screening(rec["reporting_finding"], rpt_ids, rpt_info)
        ws.cell(row, col["Related service IDs"]).value = "; ".join(vts_ids) if rec["vts_finding"] == "Confirmed present" and vts_ids else None
        ws.cell(row, col["Related reporting IDs"]).value = "; ".join(rpt_ids) if rec["reporting_finding"] == "Confirmed present" and rpt_ids else None
        comps = rec.get("grouped_components") or []
        ws.cell(row, col["Record type"]).value = (
            f"Source entry; {len(comps)} parts recorded (structure only, not a scheme count)" if comps else "Source entry; single scheme on first-pass evidence"
        )
        ws.cell(row, col["Baseline status"]).value = (
            f"TSS identity {rec['tss_identity_status'].lower()} (first pass); operational status: {rec['operational_status']}. "
            "Official baseline reconciliation pending."
        )
        note_parts = [ws.cell(row, col["Grouping / reconciliation note"]).value]
        if rec.get("official_name") and rec["official_name"] != rec["source_label"]:
            note_parts.append(f"Official name found: {rec['official_name']}.")
        note_parts.append(rec.get("tss_identity_note"))
        ws.cell(row, col["Grouping / reconciliation note"]).value = " ".join(p for p in note_parts if p)
        ws.cell(row, col["Additional evidence IDs"]).value = "; ".join(srcs) or None
        ws.cell(row, col["Additional evidence URLs"]).value = "\n".join(src_url[s] for s in srcs if src_url.get(s)) or None
        if rec["vts_finding"] == "Confirmed present" or rec["reporting_finding"] == "Confirmed present":
            stage = "Initial association evidenced"
        elif vts_ids or rpt_ids:
            stage = "Association proposed"
        else:
            stage = "Researched; unresolved"
        ws.cell(row, col["Review stage"]).value = stage
        ws.cell(row, col["Last record check"]).value = TODAY

        # relationships
        for k in rec.get("vts_service_keys") or []:
            confirmed = rec["vts_finding"] == "Confirmed present"
            rel_rows.append([rid, sid_of(k),
                             "TSS associated with service" if confirmed else "TSS service research lead",
                             "Stage 4 first pass: primary evidence" if confirmed else "Lead; coverage not evidenced",
                             srcs, rec.get("vts_relationship_basis")])
        for k in rec.get("reporting_scheme_keys") or []:
            if k not in rpt_id:
                continue
            confirmed = rec["reporting_finding"] == "Confirmed present"
            if rpt_info[k]["rec"].get("participation") == "Voluntary":
                rel_rows.append([rid, rpt_id[k], "TSS within voluntary reporting scheme",
                                 "Stage 4 first pass; voluntary, excluded from mandatory totals",
                                 srcs, rec.get("voluntary_reporting") or rec.get("reporting_relationship_basis")])
                continue
            rel_rows.append([rid, rpt_id[k],
                             "TSS associated with reporting scheme" if confirmed else "TSS reporting research lead",
                             "Stage 4 first pass: primary evidence" if confirmed else "Lead; coverage not evidenced",
                             srcs, rec.get("reporting_relationship_basis")])
        for i, c in enumerate(comps, 1):
            comp_rows.append([f"{rid}-C{i}", rid, c, "; ".join(vts_ids) if rec["vts_finding"] == "Confirmed present" else None,
                              "; ".join(rpt_ids) if rec["reporting_finding"] == "Confirmed present" else None,
                              "Part named in adoption or authority source (first pass)",
                              "Non-additive structural part (lane, approach, precautionary area or sub-scheme). Not a separate TSS in any count until confirmed as a distinct scheme.",
                              "; ".join(srcs), "\n".join(src_url[s] for s in srcs if src_url.get(s)),
                              "Component-level VTS and reporting allocation not checked separately."])

    # extend review-stage validation
    ws.data_validations.dataValidation = []
    dv = DataValidation(type="list", formula1='"Candidate recorded,Association proposed,Initial association evidenced,System-level association only,Researched; unresolved,Fully audited"', allow_blank=False)
    dv.add("R7:R176")
    ws.add_data_validation(dv)

    # ---------------- append helpers ---------------------------------------
    def append_rows(sheet, rows):
        ws2 = wb[sheet]
        last = 6
        for r in range(7, ws2.max_row + 1):
            if ws2.cell(r, 1).value is not None:
                last = r
        style_row = last
        for i, values in enumerate(rows, 1):
            r = last + i
            for c, v in enumerate(values, 1):
                cell = ws2.cell(r, c)
                cell.value = v
                src = ws2.cell(style_row, c)
                if src.has_style:
                    cell._style = copy.copy(src._style)
            ws2.row_dimensions[r].height = ws2.row_dimensions[style_row].height
        end = last + len(rows)
        for t in ws2.tables.values():
            a, b = t.ref.split(":")
            t.ref = f"{a}:{''.join(ch for ch in b if ch.isalpha())}{max(end, last)}"
        return end

    linked_svc = {SERVICE_ALIAS.get(k, k) for r in records.values() if r["vts_finding"] == "Confirmed present" for k in r.get("vts_service_keys") or []}
    linked_rpt = {k for r in records.values() if r["reporting_finding"] == "Confirmed present" for k in r.get("reporting_scheme_keys") or []}

    # services
    svc_rows = []
    for key, info in svc_info.items():
        if svc_id[key] in SERVICE_CANON.values():
            continue
        s = info["rec"]
        lead = not s.get("evidence_status", "").startswith("Confirmed")
        svc_rows.append([
            svc_id[key], s["name"], s.get("area"), s.get("authority"), s.get("centre_sectors"),
            "Stage 4 research lead (not counted)" if lead else ("Core TSS screen" if key in linked_svc else "Additional coverage (no TSS link evidenced)"),
            "Lead only; service identity or coverage not established by primary source" if lead else "Service described by primary source (Stage 4 first pass)",
            "Not assigned", "; ".join(info["src"]), "\n".join(src_url[x] for x in info["src"] if src_url.get(x)),
            (s.get("note") or "") + (f" VHF (research note only, not for operational use): {s['vhf']}." if s.get("vhf") else ""),
            TODAY,
        ])
    svc_rows.sort(key=lambda r: r[0])
    svc_end = append_rows("VTS Services", svc_rows)

    # update existing services with Stage 4 note
    ws_s = wb["VTS Services"]
    canon_rev = {v: k for k, v in SERVICE_CANON.items()}
    for r in range(7, ws_s.max_row + 1):
        vid = ws_s.cell(r, 1).value
        if vid in canon_rev and canon_rev[vid] in svc_info:
            info = svc_info[canon_rev[vid]]
            extra = [x for x in info["src"] if x not in (ws_s.cell(r, 9).value or "")]
            if extra:
                ws_s.cell(r, 9).value = (ws_s.cell(r, 9).value or "") + "; " + "; ".join(extra)
            ws_s.cell(r, 11).value = (ws_s.cell(r, 11).value or "") + " Stage 4 (B10 to B34) checked TSS coverage; see Stage 4 Findings."

    # schemes
    rpt_rows = []
    for key, info in rpt_info.items():
        if rpt_id[key] in SCHEME_CANON.values():
            continue
        s = info["rec"]
        part = "Mandatory for applicable vessels" if s["participation"] == "Mandatory" else "Voluntary"
        lead = not str(s.get("evidence_status", "")).startswith("Confirmed")
        rpt_rows.append([
            rpt_id[key], s["name"], s.get("area"), part, "; ".join(info["svc"]) or None,
            ("Core TSS screen" if key in linked_rpt else "Additional coverage (no TSS link evidenced)") if part.startswith("Mandatory") else "Additional voluntary reporting",
            s.get("evidence_status"), "; ".join(info["src"]), "\n".join(src_url[x] for x in info["src"] if src_url.get(x)),
            ((s.get("imo_instrument") and f"IMO instrument: {s['imo_instrument']}. ") or "") + (s.get("note") or ""),
            TODAY,
        ])
    rpt_rows.sort(key=lambda r: r[0])
    append_rows("Reporting Schemes", rpt_rows)

    # scheme-to-service links for new schemes
    for key, info in rpt_info.items():
        if rpt_id[key] in SCHEME_CANON.values():
            continue
        for v in info["svc"]:
            rel_rows.append([rpt_id[key], v, "Reporting system served by", "Stage 4 first pass: primary evidence", info["src"], "Does not determine the number of guide entries."])

    # relationships
    ws_r = wb["Relationships"]
    last_lnk = max(int(r[0].split("-")[1]) for r in ws_r.iter_rows(min_row=7, values_only=True) if r[0])
    existing_pairs = {(r[1], r[2]) for r in ws_r.iter_rows(min_row=7, values_only=True) if r[0]}
    lrows = []
    for fr, to, rel, ev, srcs, note in rel_rows:
        if (fr, to) in existing_pairs:
            continue
        existing_pairs.add((fr, to))
        last_lnk += 1
        lrows.append([f"LNK-{last_lnk:04d}", fr, to, rel, ev, "; ".join(srcs), "\n".join(src_url[s] for s in srcs if src_url.get(s)), note])
    append_rows("Relationships", lrows)

    # sources
    srows = []
    for sid, s in sorted(src_rows.items()):
        cls = {"Primary": "Primary (Stage 4)", "Supporting": "Supporting (Stage 4)", "Lead only": "Lead only"}.get(s.get("evidence_class"), s.get("evidence_class"))
        srows.append([sid, s.get("title"), s.get("authority"), s.get("url"), s.get("date_shown"), cls,
                      f"Locator: {s.get('locator') or 'not recorded'}. Passage: {s.get('passage') or 'not recorded'}", TODAY])
    append_rows("Sources", srows)

    # components
    if comp_rows:
        append_rows("TSS Components", comp_rows)

    # ---------------- Stage 4 Findings sheet --------------------------------
    fhdr = ["Record ID", "Batch", "Group", "Source label", "Official name", "States", "TSS identity", "Identity note",
            "Operational status", "Components", "VTS finding", "VTS service IDs", "VTS basis", "Reporting finding",
            "Reporting scheme IDs", "Reporting basis", "Voluntary reporting", "Applicability notes", "Provisional complexity",
            "Complexity reason", "Source IDs", "Open questions", "Audit adjustments at merge"]
    frows = []
    for rid in sorted(records):
        rec = records[rid]
        g = rec["_group"]
        frows.append([
            rid, rec["batch"], g, rec["source_label"], rec.get("official_name"), rec.get("states"), rec["tss_identity_status"],
            rec.get("tss_identity_note"), rec["operational_status"], "; ".join(rec.get("grouped_components") or []) or None,
            rec["vts_finding"], "; ".join(sid_of(k) for k in rec.get("vts_service_keys") or []) or None, rec.get("vts_relationship_basis"),
            rec["reporting_finding"], "; ".join(rpt_id[k] for k in rec.get("reporting_scheme_keys") or [] if k in rpt_id) or None,
            rec.get("reporting_relationship_basis"), rec.get("voluntary_reporting"), rec.get("applicability_notes"),
            rec.get("provisional_complexity"), rec.get("complexity_reason"), "; ".join(gsrc(g, rec.get("source_ids"))),
            rec.get("open_questions"), " | ".join(rec["_audit"]) or None,
        ])
    wsf = wb.create_sheet("Stage 4 Findings", index=2)
    wsf["A1"] = "STAGE 4 FINDINGS | B10 TO B34"
    wsf["A3"] = "v0.3 | First-pass record research. Findings are research determinations, not operational guidance. Unresolved never means absent."
    tpl = wb["TSS Candidates"]
    for c in ("A1", "A3"):
        wsf[c]._style = copy.copy(tpl[c]._style)
    for i, h in enumerate(fhdr, 1):
        cell = wsf.cell(6, i, h)
        cell._style = copy.copy(tpl.cell(6, 1)._style)
    for r, vals in enumerate(frows, 7):
        for i, v in enumerate(vals, 1):
            cell = wsf.cell(r, i, v)
            cell._style = copy.copy(tpl.cell(7, 3)._style)
        wsf.row_dimensions[r].height = 90
    widths = [11, 7, 7, 30, 30, 20, 12, 50, 14, 30, 16, 16, 50, 16, 16, 50, 30, 40, 13, 30, 20, 45, 45]
    for i, w in enumerate(widths, 1):
        wsf.column_dimensions[openpyxl.utils.get_column_letter(i)].width = w
    wsf.freeze_panes = "B7"
    from openpyxl.worksheet.table import Table, TableStyleInfo
    t = Table(displayName="Stage4FindingsData", ref=f"A6:{openpyxl.utils.get_column_letter(len(fhdr))}{6 + len(frows)}")
    t.tableStyleInfo = TableStyleInfo(name="TableStyleMedium2", showRowStripes=True)
    wsf.add_table(t)

    # ---------------- Batches ----------------------------------------------
    wsb = wb["Batches"]
    audits = {a["batch"]: a for d in groups.values() for a in d["batch_audits"]}
    for r in range(7, wsb.max_row + 1):
        b = wsb.cell(r, 1).value
        if b in audits:
            a = audits[b]
            wsb.cell(r, 7).value = "Stage 4 first pass complete; batch audit closed" if a.get("closed") else "Stage 4 first pass complete; batch audit open"
            wsb.cell(r, 8).value = "Resolve unresolved items: " + (a.get("unresolved_items") or "see Stage 4 Findings")

    # ---------------- issues ------------------------------------------------
    issue_rows = [
        ["High", "Counting rule", "TSS-0046 to TSS-0049; TSS-0129 to TSS-0133; TSS-0160; TSS-0166; TSS-0169; TSS-0170; TSS-0151; TSS-0161",
         "Open", "Decide whether reporting duties inside a VTS or port service (US VTS/VMRS participation, Canadian VTS zone reports, Panama Canal approach reports) should ever count as a separate mandatory reporting scheme. v0.3 records them under the service.",
         "Changes the TSS-with-mandatory-reporting subtotal, not the VTS subtotal.", None],
        ["High", "Superseded schemes", "TSS-0085; TSS-0086", "Open",
         "Read COLREG.2/Circ.78 (implemented 1 June 2023) and confirm that both Odesa/Ilichevsk schemes were replaced by the combined Chornomorsk, Odesa and Pivdennyi scheme. Add the successor as a new record if confirmed.",
         "Two source rows may become one current scheme.", None],
        ["High", "Conflict-affected areas", "TSS-0087; TSS-0088; TSS-0099", "Open",
         "Record authority statements neutrally. Do not treat IMO adoption as evidence of current safe operation.",
         "Status remains Not established or Unresolved.", None],
        ["High", "Duplicates and grouping", "TSS-0050/TSS-0051; TSS-0055 to TSS-0058", "Open",
         "Vlieland North and Off Vlieland appear to be one IMO entry. West, North and East Friesland and Off Botney Ground are parts of the single 'Off Friesland' routeing system (COLREG.2/Circ.59 and Circ.66). Reconcile against Ships' Routeing before counting.",
         "Up to five source rows may collapse into two schemes.", None],
        ["Medium", "Source quality", "Records citing IMO circulars from third-party mirrors", "Open",
         "Some IMO COLREG.2 circulars were read on non-IMO hosts (national administrations, NOAA, document mirrors). Re-check against IMODOCS or Ships' Routeing.",
         "Identity findings stand but carry a source-host limitation.", None],
        ["Medium", "Possible duplicates", "TSS-0121/TSS-0122; TSS-0127/TSS-0128; TSS-0081/TSS-0082", "Open",
         "Compare geometry and adoption instruments to establish whether these source rows describe the same scheme.",
         "May reduce the TSS count.", None],
        ["Medium", "Naming", "TSS-0140; TSS-0150", "Open",
         "Pisco was adopted as Puerto San Martin (renamed 2004). Official spelling is Punta Arenas, not Puntas Arenas. Update names without changing IDs.",
         "Alias control; no count change.", None],
        ["High", "Regulatory change", "Canadian VTS zones (TSS-0130; TSS-0131; TSS-0169; TSS-0170)", "Open",
         "SOR/2025-275 replaced SOR/89-98 and the ECAREG regulations from 31 March 2026. Replace any ECAREG references and read the new text.",
         "Legacy ECAREG leads must not be counted.", None],
        ["High", "Source access", "Cuba (TSS-0152 to TSS-0158); Greece; Spain; Mexico; Russia; Australia", "Open",
         "Official sites failed or were not found. Use ADMIRALTY List of Radio Signals Vol 6 and national radio-aids publications to close these gaps.",
         "Largest block of unresolved VTS findings.", None],
        ["Medium", "Future change", "ADRIREP (TSS-0073 to TSS-0077)", "Open",
         "MSC.598(111) amends ADRIREP from 1 December 2026. Record the rules in force on the study cut-off date separately from the amended rules.",
         "Applicability text will change after the inventory date.", None],
        ["Medium", "Derived coverage", "TSS-0075; TSS-0107 to TSS-0114; TSS-0129; TSS-0132; TSS-0133; TSS-0160; TSS-0167", "Open",
         "Coverage was derived by comparing official coordinates or charts rather than an explicit authority statement. Specialist review before any operational drafting.",
         "Findings stand as first-pass determinations.", None],
    ]
    ws_i = wb["Issues"]
    last_iss = max(int(r[0].split("-")[1]) for r in ws_i.iter_rows(min_row=7, values_only=True) if r[0])
    irows = []
    for vals in issue_rows:
        last_iss += 1
        irows.append([f"ISS-{last_iss:03d}"] + vals)
    iss_end = append_rows("Issues", irows)
    ws_i.data_validations.dataValidation = []
    dvi = DataValidation(type="list", formula1='"Open,Closed"', allow_blank=False)
    dvi.add(f"E7:E{iss_end}")
    ws_i.add_data_validation(dvi)

    # ---------------- overview ---------------------------------------------
    import re
    ends = {}
    for n in wb.sheetnames:
        for t in wb[n].tables.values():
            ends[n] = int("".join(ch for ch in t.ref.split(":")[1] if ch.isdigit()))
    ov = wb["Overview"]
    for row in ov.iter_rows():
        for c in row:
            if isinstance(c.value, str) and c.value.startswith("="):
                def fix(m):
                    sheet = m.group(1)
                    return f"'{sheet}'!{m.group(2)}7:{m.group(3)}{ends.get(sheet, m.group(4))}"
                c.value = re.sub(r"'([^']+)'!\$?([A-Z]+)\$?7:\$?([A-Z]+)\$?(\d+)", fix, c.value)
    ov["A1"].value = "GLOBAL VTS | INVENTORY v0.3"
    ov["A27"].value = "v0.3 adds first-pass Stage 4 research for B10 to B34 (125 source rows): TSS identity, VTS and mandatory reporting findings, with primary sources."
    ov["A29"].value = "Merge audit downgraded one VTS finding and three 'Confirmed absent' findings, and reclassified VTS and port reporting duties under their services. See Stage 4 Findings and research/stage4/merge_log.md."
    ov["A31"].value = "Services and schemes marked Lead only are research leads and are excluded from counted totals. Unresolved never means absent."
    ov["A33"].value = "B01 to B09 remain at v0.2 screening level. The official baseline (Ships' Routeing 2025, UKHO Notice 17) is still unreconciled."
    last = ends["Stage 4 Findings"]
    rng = lambda col: f"'Stage 4 Findings'!{col}7:{col}{last}"
    block = [
        ("STAGE 4 FIRST PASS: B10 TO B34", None),
        ("Records researched", f"=COUNTA({rng('A')})"),
        ("TSS identity confirmed", f'=COUNTIF({rng("G")},"Confirmed")'),
        ("VTS: confirmed present", f'=COUNTIF({rng("K")},"Confirmed present")'),
        ("VTS: unresolved", f'=COUNTIF({rng("K")},"Unresolved")'),
        ("VTS: confirmed absent", f'=COUNTIF({rng("K")},"Confirmed absent")'),
        ("Mandatory reporting: confirmed present", f'=COUNTIF({rng("N")},"Confirmed present")'),
        ("Mandatory reporting: unresolved", f'=COUNTIF({rng("N")},"Unresolved")'),
        ("Mandatory reporting: confirmed absent", f'=COUNTIF({rng("N")},"Confirmed absent")'),
        ("Withdrawn or superseded", f'=COUNTIF({rng("I")},"Withdrawn/superseded")'),
        ("Counted VTS services in register (excludes leads)", f'=COUNTA(\'VTS Services\'!A7:A{ends["VTS Services"]})-COUNTIF(\'VTS Services\'!F7:F{ends["VTS Services"]},"Stage 4 research lead (not counted)")'),
    ]
    for i, (label, formula) in enumerate(block):
        r = 40 + i
        ov.cell(r, 1).value = label
        ov.cell(r, 1)._style = copy.copy(ov["A15" if i == 0 else "A16"]._style)
        if formula:
            ov.cell(r, 7).value = formula
            ov.cell(r, 7)._style = copy.copy(ov["G16"]._style)

    # ---------------- sheet header lines -----------------------------------
    for ws3 in wb.worksheets:
        v = ws3["A3"].value
        if isinstance(v, str) and v.startswith("Version 0.2"):
            ws3["A3"].value = v.replace("Version 0.2", "Version 0.3", 1)
        elif isinstance(v, str) and v.startswith("v0.2"):
            ws3["A3"].value = v.replace("v0.2", "v0.3", 1)

    wb.save(OUT_WB)
    return wb, records, frows, fhdr, log, svc_id, rpt_id, svc_info, rpt_info, groups


if __name__ == "__main__":
    wb, records, frows, fhdr, log, *_ = main(True)
    with open(OUT_FIND, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(fhdr)
        w.writerows(frows)
    ws = wb["TSS Candidates"]
    with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        for r in ws.iter_rows(min_row=6, max_row=176, values_only=True):
            w.writerow(["" if v is None else v for v in r])
    with open(OUT_LOG, "w", encoding="utf-8") as f:
        f.write("# Stage 4 merge log (v0.3)\n\nChanges made to the raw research output during the merge audit.\n\n")
        f.write("\n".join(log) + "\n")
    print("ok", len(records), "records;", len(log), "adjustments")
