#!/usr/bin/env python3
"""Does each starter file appear in the doc set, in full, exactly once?

Called by check-docs.sh. Prints "N|<stale>|<not-once>" on one line.

The previous version of this check probed a single line per file and therefore passed while an inlined copy
was stale — the probe line had not changed, so a drifted body was invisible. The docs inline each file
verbatim, so the honest test is whole-body containment.
"""
import os, pathlib

S = pathlib.Path(os.environ.get("STARTER", "../devx-starter"))
docs = {p.name: p.read_text() for p in pathlib.Path("docs").glob("*.md")}

n, stale, notonce = 0, [], []
for src in sorted(S.rglob("*")):
    if not src.is_file() or ".git" in src.parts:
        continue
    rel = str(src.relative_to(S))
    # board.html is generated from board.md by scripts/board.mjs. Inlining a derivative would mean
    # maintaining a copy of a copy, which is the drift the generated view exists to avoid.
    if src.name == ".gitkeep" or rel == "tasks/board.html":
        continue
    n += 1
    body = src.read_text().rstrip("\n")
    if not body.strip():
        continue
    hits = [name for name, text in docs.items() if body in text]
    if len(hits) == 1:
        continue
    if hits:
        notonce.append(f"{rel}({len(hits)})")
    else:
        # Not present in full. Locate where it probably lives so the message is actionable.
        lines = [l for l in body.split("\n") if len(l) > 28]
        probe = lines[len(lines) // 2] if lines else None
        where = [nm for nm, tx in docs.items() if probe and probe in tx]
        stale.append(f"{rel}->{where[0] if where else 'ABSENT'}")

print(f"{n}|{' '.join(stale)}|{' '.join(notonce)}")
