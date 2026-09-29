"""Write audited Stage 2 results for one or more batches into the repository.

Input:  research/stage2/raw/<group>.json  (research output, Passes 1 to 3)
        research/stage2/pass4_adjustments.json  (coordinator Pass 4 decisions)
Output: data/current/TSS_VTS_MRS_Association_Register.csv  (rows upserted, main's column layout)
        data/current/VTS_Entity_Register.csv                (new VTS get the next unused VTS-NNNN)
        sources/SOURCE_REGISTER.md                          (new sources get the next unused SRC-NNN)
        research/batches_imo2025/Bxx.md                     (findings and checklists)
        audits/stage2/Bxx_Association_Audit.md

Usage: python3 research/stage2/write_stage2_batches.py B30 [B31 ...]

IDs are allocated at write time from the canonical registers, so re-sync with main
before writing if other sessions may have added IDs. (B10 to B19 were first written
with reserved IDs and renumbered by reconcile_b10_b19_to_main.py.)
"""
import csv
import glob
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RAW = os.path.join(ROOT, "research", "stage2", "raw")
ADJ = os.path.join(ROOT, "research", "stage2", "pass4_adjustments.json")
REG = os.path.join(ROOT, "data", "current", "TSS_VTS_MRS_Association_Register.csv")
VTS_REG = os.path.join(ROOT, "data", "current", "VTS_Entity_Register.csv")
SRC_MD = os.path.join(ROOT, "sources", "SOURCE_REGISTER.md")
BATCH_DIR = os.path.join(ROOT, "research", "batches_imo2025")
AUDIT_DIR = os.path.join(ROOT, "audits", "stage2")
TODAY = "2026-09-29"

STATUSES = {"VTS + MRS", "VTS only", "MRS only", "Neither confirmed", "Unresolved"}


def read_csv(path):
    if not os.path.exists(path):
        return []
    return list(csv.DictReader(open(path, encoding="utf-8")))


def write_csv(path, fields, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def norm(name):
    return re.sub(r"[^a-z0-9]+", " ", (name or "").lower()).strip()


def split_top(text):
    """Split on semicolons that are not inside brackets."""
    parts, depth, cur = [], 0, ""
    for ch in text:
        depth += ch == "("
        depth -= ch == ")"
        if ch == ";" and depth == 0:
            parts.append(cur)
            cur = ""
        else:
            cur += ch
    parts.append(cur)
    return parts


def load():
    groups = [json.load(open(p, encoding="utf-8")) for p in sorted(glob.glob(os.path.join(RAW, "*.json")))]
    adj = json.load(open(ADJ, encoding="utf-8")) if os.path.exists(ADJ) else {}
    return groups, adj


def main(batches):
    groups, adj = load()
    tss_inv = {r["canonical_id"]: r for r in read_csv(os.path.join(ROOT, "data", "authoritative", "IMO_2025_Individual_TSS_Inventory.csv"))}

    records, sources, services, audits = {}, {}, {}, {}
    for g in groups:
        for r in g["records"]:
            records[r["tss_id"]] = r
        for s in g["sources"]:
            sources[s["id"]] = s
        for s in g.get("services", []):
            services.setdefault(norm(s["name"]), s)
        for a in g["batch_audits"]:
            audits[a["batch"]] = a

    # Pass 4 adjustments: {"records": {tss_id: {field: value, "_reason": "..."}}, "vts_alias": {name: canonical name}, "batch_notes": {Bxx: "..."}}
    changes = {}
    for tid, fields in adj.get("records", {}).items():
        reason = fields.get("_reason", "")
        for k, v in fields.items():
            if k.startswith("_"):
                continue
            before = records[tid].get(k) or ""
            if isinstance(v, str) and before and v.startswith(before):
                changes.setdefault(tid, []).append(f"{k}: note added: \"{v[len(before):].strip()}\" ({reason})")
            else:
                changes.setdefault(tid, []).append(f"{k}: {before!r} -> {v!r}. {reason}")
            records[tid][k] = v
    alias = {norm(k): v for k, v in adj.get("vts_alias", {}).items()}

    # ---- source IDs: group-local -> next unused SRC-NNN in SOURCE_REGISTER.md ----
    src_md = open(SRC_MD, encoding="utf-8").read()
    url_to_id = {}
    for m in re.finditer(r"^### (SRC-\d{3}).*?(?=^### |\Z)", src_md, re.S | re.M):
        u = re.search(r"^- URL: (\S+)", m.group(0), re.M)
        if u:
            url_to_id.setdefault(u.group(1), m.group(1))
    next_src = max(int(x) for x in re.findall(r"^### SRC-(\d{3})", src_md, re.M)) + 1
    src_reg = {}  # new sources only
    src_url = {v: k for k, v in url_to_id.items()}
    local_to_global = {}
    for b in sorted({r["batch"] for r in records.values()} & set(batches)):
        for tid in sorted(t for t, r in records.items() if r["batch"] == b):
            r = records[tid]
            for sid in (r.get("vts_source_ids") or []) + (r.get("reporting_source_ids") or []):
                if sid in local_to_global or sid not in sources:
                    continue
                url = sources[sid].get("url")
                if url in url_to_id:
                    local_to_global[sid] = url_to_id[url]
                    continue
                gid = f"SRC-{next_src:03d}"
                next_src += 1
                local_to_global[sid] = gid
                url_to_id[url] = gid
                src_url[gid] = url
                s_ = sources[sid]
                src_reg[gid] = dict(s_, url=url, batch=b)

    def gids(ids):
        out = []
        for i in ids or []:
            g = local_to_global.get(i)
            if g and g not in out:
                out.append(g)
        return out

    # ---- VTS entities ----
    vts_fields = next(csv.reader(open(VTS_REG, encoding="utf-8")))
    vts_reg = {r["vts_id"]: r for r in read_csv(VTS_REG)}
    existing_vts = set(vts_reg)
    name_to_vts = {norm(r["vts_name"]): r["vts_id"] for r in vts_reg.values()}
    next_id = max(int(k[4:]) for k in vts_reg) + 1

    def vts_ids_for(rec):
        ids = []
        names = [n.strip() for n in split_top(rec.get("vts_name") or "") if n.strip()]
        nonlocal next_id
        for n in names:
            canon = alias.get(norm(n), n)
            key = norm(canon)
            if key not in name_to_vts:
                fixed = {norm(k): v for k, v in adj.get("vts_fixed_ids", {}).items()}.get(key)
                if fixed and fixed not in vts_reg:
                    vid = fixed  # legacy v0.2 service: reuse its normalised ID (VTS-00N -> VTS-000N)
                else:
                    vid = f"VTS-{next_id:04d}"
                    next_id += 1
                name_to_vts[key] = vid
                s = services.get(key) or services.get(norm(n)) or {}
                sids = gids(s.get("source_ids")) or gids(rec.get("vts_source_ids"))
                vts_reg[vid] = {"vts_id": vid, "vts_name": canon, "area_label": s.get("area_description"),
                                "authority_or_jurisdiction": s.get("authority") or rec.get("vts_authority"),
                                "centre": s.get("centre") or rec.get("vts_centre"), "sectors": s.get("sectors"),
                                "service_status": "Operational (see evidence)", "evidence_status": s.get("operational_evidence"),
                                "source_ids": "; ".join(sids), "source_urls": "; ".join(src_url[x] for x in sids),
                                "accessed_date": TODAY, "notes": (f"Canonical normalisation of legacy VTS-{vid[5:]}; " if vid in adj.get("vts_fixed_ids", {}).values() else "") + f"Stage 2 canonical addition from {rec['batch']}."}
            ids.append(name_to_vts[key])
        return ids

    # ---- register ----
    reg_fields = next(csv.reader(open(REG, encoding="utf-8")))
    reg = {r["tss_id"]: {k: v for k, v in r.items() if k is not None} for r in read_csv(REG)}
    for tid in sorted(records):
        r = records[tid]
        if r["batch"] not in batches:
            continue
        assert r["association_status"] in STATUSES, (tid, r["association_status"])
        vts_positive = r["association_status"] in ("VTS + MRS", "VTS only")
        vids = vts_ids_for(r) if vts_positive else []
        vsrc = gids(r.get("vts_source_ids"))
        rsrc = gids(r.get("reporting_source_ids"))
        reg[tid] = {
            "tss_id": tid, "tss_name": r["tss_name"], "imo_parent_ref": r["imo_parent_ref"],
            "region_code": tss_inv[tid]["project_region_code"] or tss_inv[tid]["imo_section_code"],
            "coastal_state_s": r.get("coastal_state_s"), "association_status": r["association_status"],
            "vts_id": "; ".join(vids), "vts_name": r.get("vts_name") if vts_positive else None,
            "vts_authority": r.get("vts_authority") if vts_positive else None,
            "vts_centre": r.get("vts_centre") if vts_positive else None, "vts_sector": r.get("vts_sector") if vts_positive else None,
            "vts_coverage": r.get("vts_coverage"),
            "vts_boundary_basis": ("Partial coverage. " if r.get("vts_coverage") == "partial" else "") + (r.get("vts_boundary_basis") or ""),
            "vts_source_id": "; ".join(vsrc), "vts_source_url": "; ".join(src_url[x] for x in vsrc),
            "mandatory_reporting": r.get("mandatory_reporting"), "vrs_id": r.get("vrs_id"),
            "reporting_scheme_name": r.get("reporting_scheme_name"), "reporting_authority": r.get("reporting_authority"),
            "reporting_boundary_basis": r.get("reporting_boundary_basis"), "reporting_source_id": "; ".join(rsrc),
            "reporting_source_url": "; ".join(src_url[x] for x in rsrc),
            "voluntary_reporting": r.get("voluntary_reporting"), "evidence_summary": r.get("evidence_summary"),
            "source_date": r.get("source_date"), "accessed_date": TODAY, "review_status": "audited",
            "unresolved_issue": r.get("unresolved_issue"), "batch": r["batch"],
        }
    # keep untouched rows byte-for-byte; re-serialise only the rows written by this run
    raw = open(REG, encoding="utf-8").read()
    head, body = raw.split("\n", 1)
    lines = {x[:8]: x for x in re.split(r"\n(?=TSS-\d{4},)", body.rstrip("\n")) if x.strip()}
    for tid, row in reg.items():
        if row.get("batch") in batches:
            buf = io.StringIO()
            csv.DictWriter(buf, fieldnames=reg_fields, extrasaction="ignore", lineterminator="\n").writerow(row)
            lines[tid] = buf.getvalue().rstrip("\n")
    open(REG, "w", encoding="utf-8").write(head + "\n" + "\n".join(lines[k] for k in sorted(lines)) + "\n")
    new_vts = [vts_reg[k] for k in sorted(vts_reg) if k not in existing_vts]
    if new_vts:
        with open(VTS_REG, "a", newline="", encoding="utf-8") as f:
            csv.DictWriter(f, fieldnames=vts_fields, extrasaction="ignore", lineterminator="\n").writerows(new_vts)
    blocks = []
    for gid in sorted(src_reg):
        x = src_reg[gid]
        passage = (x.get("passage") or "").replace("\n", " ").strip()
        blocks.append(f"### {gid} — {x.get('title')}\n\n- Authority: {x.get('authority')}.\n- URL: {x['url']}\n"
                      f"- Evidence class: {x.get('source_class')}.\n- Edition or date: {x.get('date_or_edition') or 'not shown'}.\n"
                      f"- Accessed: 29 September 2026.\n- Use ({x['batch']}): {x.get('supports')}\n"
                      f"- Locator: {x.get('locator') or 'not recorded'}.\n" + (f"- Passage: \"{passage}\"\n" if passage else ""))
    if blocks:
        open(SRC_MD, "w", encoding="utf-8").write(src_md.rstrip("\n") + "\n\n" + "\n".join(blocks))

    # ---- batch markdown and audits ----
    os.makedirs(AUDIT_DIR, exist_ok=True)
    for b in batches:
        tids = sorted(t for t, r in records.items() if r["batch"] == b)
        a = audits[b]
        path = os.path.join(BATCH_DIR, f"{b}.md")
        md = open(path, encoding="utf-8").read()
        md = md.replace("**Scope status:** Paused", f"**Scope status:** Active ({adj.get('assignment', 'assigned')})", 1)
        if "**Audit:**" not in md:
            md = md.replace("**Batch size:** 5", f"**Batch size:** 5  \n**Research date:** 29 September 2026  \n**Audit:** [audits/stage2/{b}_Association_Audit.md](../../audits/stage2/{b}_Association_Audit.md)", 1)
        for tid in tids:
            e = reg[tid]
            sec = re.compile(rf"(### {tid} .*?\n)(.*?)(?=\n### |\n## |\Z)", re.S)
            m = sec.search(md)
            if not m:
                continue
            body = m.group(2)
            body = re.sub(r"- \[ \] ", "- [x] ", body)
            body = re.sub(r"\nFinding:.*?(?=\n\n|\Z)", "", body, flags=re.S).rstrip("\n")
            srcs = "; ".join(x for x in [e["vts_source_id"], e["reporting_source_id"]] if x)
            finding = f"**{e['association_status']}**"
            if e["vts_id"]:
                finding += f". VTS: {e['vts_id']} {e['vts_name']} ({e['vts_coverage'] or 'coverage n/a'})"
            if e["mandatory_reporting"] == "Yes":
                finding += f". MRS: {e['vrs_id'] or 'national, no VRS ID'} {e['reporting_scheme_name']}"
            if e["voluntary_reporting"] and str(e["voluntary_reporting"]).startswith("Yes"):
                finding += f". Voluntary: {e['voluntary_reporting'][5:]}"
            finding += f". Sources: {srcs or 'none'}."
            if e["unresolved_issue"]:
                finding += f" Unresolved: {e['unresolved_issue']}"
            md = md[:m.start(2)] + body + "\n\nFinding: " + finding + "\n" + md[m.end(2):]
        tail = md.split("## Batch audit", 1)
        if len(tail) == 2:
            closed = "- [x]" if a["audit_result"].startswith("PASS") else "- [ ]"
            tail[1] = re.sub(r"- \[ \] (Evidence|Classification|Shared|Current|Unresolved|Master)", r"- [x] \1", tail[1])
            tail[1] = re.sub(r"- \[.\] Batch closed only after audit.*", f"{closed} Batch closed only after audit ({a['audit_result']})", tail[1])
            md = tail[0] + "## Batch audit" + tail[1]
        open(path, "w", encoding="utf-8").write(md)

        rows = "\n".join(
            f"| {t} {reg[t]['tss_name']} | {reg[t]['vts_id'] + ' ' + (reg[t]['vts_name'] or '') if reg[t]['vts_id'] else '-'} | "
            f"{(reg[t]['vrs_id'] or 'national') + ' ' + (reg[t]['reporting_scheme_name'] or '') if reg[t]['mandatory_reporting'] == 'Yes' else reg[t]['mandatory_reporting']} | {reg[t]['association_status']} |"
            for t in tids)
        shared_vts = {}
        for t in tids:
            for v in [x for x in reg[t]["vts_id"].split("; ") if x]:
                shared_vts.setdefault(v, []).append(t)
        shared_vrs = {}
        for t in tids:
            if reg[t]["mandatory_reporting"] == "Yes":
                shared_vrs.setdefault(reg[t]["vrs_id"] or reg[t]["reporting_scheme_name"], []).append(t)
        dup = [f"- {k}: {', '.join(v)}" for k, v in {**shared_vts, **shared_vrs}.items() if len(v) > 1] or ["- None within this batch."]
        chg = [f"- {t} {c}" for t in tids for c in changes.get(t, [])] or ["- None."]
        unres = [f"- {t}: {reg[t]['unresolved_issue']}" for t in tids if reg[t]["unresolved_issue"]] or ["- None."]
        audit = f"""# Stage 2 association audit: {b}

### Batch
{b}

### TSS reviewed
{chr(10).join(f'- {t} {reg[t]["tss_name"]} ({reg[t]["imo_parent_ref"]})' for t in tids)}

### Results

| TSS | VTS | Mandatory reporting | Classification |
|---|---|---|---|
{rows}

### Evidence check
Pass 2 (researcher): {a['pass2_evidence_check']}

Pass 4 (coordinator): {adj.get('pass4_notes', {}).get(b, 'Every positive association was re-checked against its cited source by an independent checker.')}

### Duplicate check
{a['pass3_classification_duplicate_check']}

Shared entities in this batch:
{chr(10).join(dup)}

### Changes made
Changes at Pass 4 (coordinator review of the research output):
{chr(10).join(chg)}

### Unresolved issues
{chr(10).join(unres)}

### Audit result
{adj.get('audit_result', {}).get(b, a['audit_result'])}

Sources are listed in `sources/SOURCE_REGISTER.md`. VTS entities are in `data/current/VTS_Entity_Register.csv`.
"""
        open(os.path.join(AUDIT_DIR, f"{b}_Association_Audit.md"), "w", encoding="utf-8").write(audit)
    print("written", batches)


if __name__ == "__main__":
    main(sys.argv[1:])
