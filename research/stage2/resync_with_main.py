"""Re-sync this branch's Stage 2 batches with origin/main when both sides have allocated IDs.

Run after `git merge --no-commit origin/main` has stopped on conflicts in the shared registers.
Usage: python3 research/stage2/resync_with_main.py B10 B11 ... (the batches owned by this branch)

- data/current/TSS_VTS_MRS_Association_Register.csv: main's rows verbatim, plus this branch's rows
  for the listed batches (main wins if both have a row).
- data/current/VTS_Entity_Register.csv: main's rows verbatim, plus this branch's VTS rows whose notes
  say "Stage 2 canonical addition from Bxx" for a listed batch, renumbered after main's highest ID.
- sources/SOURCE_REGISTER.md: main's text verbatim, plus this branch's source blocks whose
  "- Use (Bxx)" line names a listed batch, renumbered after main's highest SRC.
- Every reference in this branch's batch files, audits and the renumbered rows is rewritten.
The mapping is appended to research/stage2/id_mapping_resync.csv.
"""
import csv
import io
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REG = "data/current/TSS_VTS_MRS_Association_Register.csv"
ENT = "data/current/VTS_Entity_Register.csv"
SRC = "sources/SOURCE_REGISTER.md"


def show(ref, path):
    return subprocess.run(["git", "-C", ROOT, "show", f"{ref}:{path}"], capture_output=True, check=True).stdout.decode("utf-8")


def split_rows(text, key_re):
    head, body = text.split("\n", 1)
    parts = [x for x in re.split(rf"\n(?={key_re})", body.rstrip("\n")) if x.strip()]
    return head, parts


def main(batches):
    batches = set(batches)
    ours, theirs = "HEAD", "origin/main"

    # ---- sources ----
    main_src = show(theirs, SRC)
    my_src = show(ours, SRC)
    main_ids = set(re.findall(r"^### (SRC-\d{3})", main_src, re.M))
    next_src = max(int(x[4:]) for x in main_ids) + 1
    blocks = re.findall(r"^### SRC-\d{3}.*?(?=^### |\Z)", my_src, re.S | re.M)
    src_map, my_blocks = {}, []
    for b in blocks:
        m = re.search(r"^- Use \((B\d\d)\)", b, re.M)
        if not m or m.group(1) not in batches:
            continue
        old = re.match(r"### (SRC-\d{3})", b).group(1)
        new = f"SRC-{next_src:03d}"
        next_src += 1
        src_map[old] = new
        my_blocks.append(b.rstrip("\n") + "\n")  # heading renumbered once, by remap() at write time

    # ---- VTS entities ----
    head, main_ent = split_rows(show(theirs, ENT), r"VTS-\d{4},")
    _, my_ent = split_rows(show(ours, ENT), r"VTS-\d{4},")
    main_vts = {x[:8] for x in main_ent}
    next_vts = max(int(x[4:8]) for x in main_vts) + 1
    vts_map, my_ent_rows = {}, []
    for row in my_ent:
        m = re.search(r"Stage 2 canonical addition from (B\d\d)", row)
        if not m or m.group(1) not in batches:
            continue
        old = row[:8]
        if "Canonical normalisation of legacy" in row:
            # legacy v0.2 service: keep its fixed ID; if main already holds it, keep main's row
            if old not in main_vts:
                my_ent_rows.append(row)
            continue
        new = f"VTS-{next_vts:04d}"
        next_vts += 1
        vts_map[old] = new
        my_ent_rows.append(row)

    def remap(text):
        text = re.sub(r"SRC-\d{3}(?!\d)", lambda m: src_map.get(m.group(0), m.group(0)), text)
        return re.sub(r"VTS-\d{4}", lambda m: vts_map.get(m.group(0), m.group(0)), text)

    # ---- write sources and entities ----
    open(os.path.join(ROOT, SRC), "w", encoding="utf-8").write(
        main_src.rstrip("\n") + "\n\n" + "\n".join(remap(b) for b in my_blocks))
    open(os.path.join(ROOT, ENT), "w", encoding="utf-8").write(
        head + "\n" + "\n".join(main_ent + [remap(r) for r in my_ent_rows]) + "\n")

    # ---- register ----
    rhead, main_reg = split_rows(show(theirs, REG), r"TSS-\d{4},")
    _, my_reg = split_rows(show(ours, REG), r"TSS-\d{4},")
    tss_batch = {f"TSS-{n:04d}": f"B{(n - 1) // 5 + 1:02d}" for n in range(1, 225)}
    rows = {x[:8]: x for x in main_reg}
    for x in my_reg:
        if tss_batch[x[:8]] in batches and x[:8] not in rows:
            rows[x[:8]] = remap(x)
    open(os.path.join(ROOT, REG), "w", encoding="utf-8").write(rhead + "\n" + "\n".join(rows[k] for k in sorted(rows)) + "\n")

    # ---- batch files and audits ----
    for b in sorted(batches):
        for p in (f"research/batches_imo2025/{b}.md", f"audits/stage2/{b}_Association_Audit.md"):
            fp = os.path.join(ROOT, p)
            if os.path.exists(fp):
                t = open(fp, encoding="utf-8").read()
                open(fp, "w", encoding="utf-8").write(remap(t))
    for p in ("audits/stage2/Interim_Report_B10_B19.md",):
        fp = os.path.join(ROOT, p)
        if os.path.exists(fp):
            t = open(fp, encoding="utf-8").read()
            open(fp, "w", encoding="utf-8").write(remap(t))

    mp = os.path.join(ROOT, "research", "stage2", "id_mapping_resync.csv")
    new_file = not os.path.exists(mp)
    with open(mp, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n")
        if new_file:
            w.writerow(["previous_id", "resynced_id"])
        for k, v in list(vts_map.items()) + list(src_map.items()):
            if k != v:
                w.writerow([k, v])
    print("VTS", vts_map)
    print("sources", len(src_map), (min(src_map.values()), max(src_map.values())) if src_map else "")


if __name__ == "__main__":
    main(sys.argv[1:])
