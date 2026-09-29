"""Fold the B10 to B19 Stage 2 results (branch work) into main's canonical registers.

- Register rows are written in main's column layout; vts_coverage goes into vts_boundary_basis.
- Branch VTS IDs (VTS-0101 onward) are renumbered to the next unused IDs in VTS_Entity_Register.csv.
- Branch source IDs (SRC-Bxx-nn) are renumbered to the next unused SRC-NNN and appended to
  sources/SOURCE_REGISTER.md; the branch-only sources/Stage2_Source_Register.csv is then removed.
- References in batch files, audits and the interim report are rewritten with the new IDs.
The ID mapping is saved to research/stage2/id_mapping_b10_b19.csv for traceability.
"""
import csv
import io
import os
import re
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TODAY = "2026-09-29"


def show(ref, path):
    return subprocess.run(["git", "-C", ROOT, "show", f"{ref}:{path}"], capture_output=True, check=True).stdout.decode("utf-8")


def rows(text):
    return list(csv.DictReader(io.StringIO(text)))


def main():
    reg_path = "data/current/TSS_VTS_MRS_Association_Register.csv"
    main_reg_text = show("origin/main", reg_path)
    main_fields = next(csv.reader(io.StringIO(main_reg_text)))
    main_reg = rows(main_reg_text)
    mine = rows(show("HEAD", reg_path))
    my_vts = rows(show("HEAD", "data/current/VTS_Service_Register.csv"))
    my_src = rows(show("HEAD", "sources/Stage2_Source_Register.csv"))
    ent_path = os.path.join(ROOT, "data", "current", "VTS_Entity_Register.csv")
    ent = rows(open(ent_path, encoding="utf-8").read())
    ent_fields = list(ent[0].keys())
    src_md_path = os.path.join(ROOT, "sources", "SOURCE_REGISTER.md")
    src_md = open(src_md_path, encoding="utf-8").read()

    # ---- ID maps ----
    next_vts = max(int(r["vts_id"][4:]) for r in ent) + 1
    vts_map = {}
    for r in sorted(my_vts, key=lambda r: r["vts_id"]):
        vts_map[r["vts_id"]] = f"VTS-{next_vts:04d}"
        next_vts += 1
    next_src = max(int(m) for m in re.findall(r"^### SRC-(\d{3})", src_md, re.M)) + 1
    src_map = {}
    for r in sorted(my_src, key=lambda r: (r["batch"], r["source_id"])):
        src_map[r["source_id"]] = f"SRC-{next_src:03d}"
        next_src += 1

    def remap(text):
        if not text:
            return text
        text = re.sub(r"VTS-01\d\d", lambda m: vts_map.get(m.group(0), m.group(0)), text)
        return re.sub(r"SRC-B\d\d-\d\d", lambda m: src_map.get(m.group(0), m.group(0)), text)

    # ---- register ----
    mine_ids = {r["tss_id"] for r in mine}
    clash = [r["tss_id"] for r in main_reg if r["tss_id"] in mine_ids]
    assert not clash, f"main already has rows for {clash}"
    # main's rows TSS-0008 to TSS-0010 carry an empty trailing column; drop it
    out = [{k: v for k, v in r.items() if k is not None} for r in main_reg]
    for r in mine:
        row = {k: remap(r.get(k, "")) for k in main_fields}
        cov = r.get("vts_coverage")
        if cov == "partial" and row["vts_boundary_basis"]:
            row["vts_boundary_basis"] = "Partial coverage. " + row["vts_boundary_basis"]
        out.append(row)
    out.sort(key=lambda r: r["tss_id"])
    with open(os.path.join(ROOT, reg_path), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=main_fields, lineterminator="\n")
        w.writeheader()
        w.writerows(out)

    # ---- VTS entities ----
    src_by_id = {r["source_id"]: r for r in my_src}
    for r in sorted(my_vts, key=lambda r: r["vts_id"]):
        sids = [s for s in r["source_ids"].split("; ") if s]
        ent.append({
            "vts_id": vts_map[r["vts_id"]], "vts_name": r["vts_name"], "area_label": r["area_description"],
            "authority_or_jurisdiction": r["authority"], "centre": r["centre"], "sectors": r["sectors"],
            "service_status": "Operational (see evidence)", "evidence_status": r["operational_evidence"],
            "source_ids": "; ".join(src_map[s] for s in sids), "source_urls": "; ".join(src_by_id[s]["url"] for s in sids),
            "accessed_date": TODAY,
            "notes": f"Stage 2 canonical addition from {r['first_batch']} (branch ID {r['vts_id']}).",
        })
    with open(ent_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=ent_fields, lineterminator="\n")
        w.writeheader()
        w.writerows(ent)

    # ---- sources ----
    blocks = []
    for r in sorted(my_src, key=lambda r: src_map[r["source_id"]]):
        passage = (r["passage"] or "").replace("\n", " ").strip()
        blocks.append(
            f"### {src_map[r['source_id']]} — {r['title']}\n\n"
            f"- Authority: {r['authority']}.\n"
            f"- URL: {r['url']}\n"
            f"- Evidence class: {r['source_class']}.\n"
            f"- Edition or date: {r['date_or_edition'] or 'not shown'}.\n"
            f"- Accessed: 29 September 2026.\n"
            f"- Use ({r['batch']}): {r['supports']}\n"
            f"- Locator: {r['locator'] or 'not recorded'}.\n"
            + (f"- Passage: \"{passage}\"\n" if passage else "")
        )
    src_md = src_md.rstrip("\n") + "\n\n" + "\n".join(blocks)
    open(src_md_path, "w", encoding="utf-8").write(src_md)
    os.remove(os.path.join(ROOT, "sources", "Stage2_Source_Register.csv"))
    os.remove(os.path.join(ROOT, "data", "current", "VTS_Service_Register.csv"))

    # ---- rewrite references ----
    paths = [os.path.join(ROOT, "research", "batches_imo2025", f"B{n}.md") for n in range(10, 20)]
    paths += [os.path.join(ROOT, "audits", "stage2", f"B{n}_Association_Audit.md") for n in range(10, 20)]
    paths.append(os.path.join(ROOT, "audits", "stage2", "Interim_Report_B10_B19.md"))
    for p in paths:
        t = open(p, encoding="utf-8").read()
        t = remap(t)
        t = t.replace("Sources are listed in `sources/Stage2_Source_Register.csv` (IDs", "Sources are listed in `sources/SOURCE_REGISTER.md` (renumbered from")
        t = t.replace("`data/current/VTS_Service_Register.csv`", "`data/current/VTS_Entity_Register.csv`")
        t = t.replace("`sources/Stage2_Source_Register.csv`", "`sources/SOURCE_REGISTER.md`")
        open(p, "w", encoding="utf-8").write(t)

    with open(os.path.join(ROOT, "research", "stage2", "id_mapping_b10_b19.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["branch_id", "canonical_id"])
        for k, v in list(vts_map.items()) + list(src_map.items()):
            w.writerow([k, v])
    print("VTS", vts_map)
    print("sources", len(src_map), min(src_map.values()), "to", max(src_map.values()))
    print("register rows", len(out))


if __name__ == "__main__":
    main()
