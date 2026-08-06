#!/usr/bin/env python3
"""Refresh an inlined copy in docs/ from the starter, by finding the fenced block it belongs to.

Used when a starter file that the docs inline verbatim has changed. Rather than trusting a hand-edit to find
the right fence — the docs contain hundreds of fenced blocks and several are near-identical workflow files —
this scores EVERY fenced block in the doc set against the new content and refuses unless one is a clear
winner. The margin matters: on a previous resync the correct block scored 0.64-0.90 and the runner-up scored
0.00-0.17, so a clear winner is the normal case and an unclear one means something needs a person.

  python3 scripts/resync-inlines.py            # report what it would do
  python3 scripts/resync-inlines.py --write    # do it

It never creates a block. A file the docs do not inline yet has to be placed by a human who decides which
document it belongs in and writes the prose around it — that is a judgement, and guessing at it would put
a 6,000-word script in an arbitrary chapter.
"""
import difflib, os, pathlib, re, subprocess, sys

S = pathlib.Path(os.environ.get("STARTER", "../devx-starter"))
WRITE = "--write" in sys.argv
MIN_SCORE = 0.45   # below this, no block is plausibly the same file
MIN_MARGIN = 0.15  # the winner must be clearly ahead of the runner-up

FENCE = re.compile(r"^(```+)[^\n]*$", re.M)


def blocks(text):
    """(start_of_content, end_of_content, content) for every fenced block."""
    out, lines, i = [], text.split("\n"), 0
    while i < len(lines):
        m = re.match(r"^(`{3,})", lines[i])
        if not m:
            i += 1
            continue
        tick = m.group(1)
        j = i + 1
        while j < len(lines) and not lines[j].startswith(tick):
            j += 1
        out.append((i + 1, j, "\n".join(lines[i + 1 : j])))
        i = j + 1
    return out


def stale_files():
    res = subprocess.run(
        ["python3", "scripts/check-inlines.py"], capture_output=True, text=True,
        env={**os.environ, "STARTER": str(S)},
    ).stdout.strip()
    # ABSENT entries are included. check-inlines guesses a file's home from ONE probe line, so a file whose
    # middle line changed reports ABSENT even though its old copy is sitting in a document — which is the same
    # single-line heuristic check-inlines itself was rewritten to stop trusting. The similarity scorer below
    # does not need the probe, and its score-plus-margin test is what refuses when a file genuinely is not
    # there. Filtering on the probe here made resync silently skip exactly the files it was written for.
    stale = res.split("|")[1].split()
    return [s.split("->")[0] for s in stale]


did = 0
for rel in stale_files():
    new = (S / rel).read_text().rstrip("\n")
    scored = []
    for doc in sorted(pathlib.Path("docs").glob("*.md")):
        text = doc.read_text()
        for a, b, content in blocks(text):
            r = difflib.SequenceMatcher(None, content, new).ratio()
            scored.append((r, doc, a, b, content))
    scored.sort(key=lambda x: -x[0])
    if not scored:
        print(f"  SKIP  {rel}: no fenced blocks anywhere")
        continue
    best, runner = scored[0], (scored[1] if len(scored) > 1 else (0, None, 0, 0, ""))
    r, doc, a, b, _ = best
    if r < MIN_SCORE or (r - runner[0]) < MIN_MARGIN:
        print(f"  REFUSE {rel}: best {r:.2f} in {doc.name}, runner-up {runner[0]:.2f} — too close to be sure")
        continue
    print(f"  {'WRITE' if WRITE else 'would'} {rel} -> {doc.name} lines {a}-{b} (score {r:.2f}, next {runner[0]:.2f})")
    if WRITE:
        lines = doc.read_text().split("\n")
        doc.write_text("\n".join(lines[:a] + new.split("\n") + lines[b:]))
        did += 1

print(f"\n  {did} refreshed" if WRITE else "\n  dry run; pass --write")
