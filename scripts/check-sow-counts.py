#!/usr/bin/env python3
"""Does every count in the two-page agreement match the thing it counts?

Called by check-docs.sh. Prints one line per rule, and exits non-zero on a mismatch.

WHY THIS EXISTS. The demo engagement ships a 1,100-word agreement and a 23,000-word terms document, and the
short one is what a founder actually reads. Every number in it is a HAND-COPIED SUMMARY of something in the long
one, with no link back to what it counts — so it goes stale silently while the long version stays correct, and
the reader most likely to check is the one being asked to sign.

That is not hypothetical. It happened three times in this one document:

  - "Thirteen risks ... seven / two / four by Dev Rawat" while §15 held nineteen rows split seven / two / ten —
    and two of those rows were both numbered 13, which is how nineteen counted to eighteen and nobody noticed
    either number was wrong. Found by an agent playing the client, reading his own signature block. Two
    adversarial verifiers had read §15 and neither had counted it.
  - "Thirteen things" about §6, which holds fourteen (N-1 to N-14) — and §6's own preamble says it grew by four
    rows in the last revision, so fourteen was intended and the summary was one short.
  - Earlier, §14 and §15 were referenced nine times and did not exist at all.

A summary of a long document is the right shape. An UNCHECKED summary of a long document is a liability, and the
fix is not to stop summarising — it is to make the copy fail loudly when it drifts.

WHAT THIS CANNOT DO. It counts rows; it cannot tell whether a row belongs where it is, whether two rows are
secretly the same risk written twice (the defect above), or whether a spelled-out number describes something
this file does not model. Anything it does not model is invisible to it, so a rule added to the agreement
without a rule added here is unchecked — which is the same failure one level up. Adding a countable claim to
the agreement means adding it here.
"""
import os, pathlib, re, sys

WORDS = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
    "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
    "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20,
}

ROOT = pathlib.Path(os.environ.get("DEMO", "demo/ops-todo-board"))
AGREEMENT = ROOT / "docs/sow.md"
TERMS = ROOT / "docs/sow-terms.md"


def section(text, heading_re):
    """The body of one numbered section, up to the next heading at the same depth or shallower."""
    lines = text.split("\n")
    start = next((i for i, l in enumerate(lines) if re.match(heading_re, l)), None)
    if start is None:
        return None
    depth = len(re.match(r"#*", lines[start]).group(0))
    for i in range(start + 1, len(lines)):
        m = re.match(r"(#+)\s", lines[i])
        if m and len(m.group(1)) <= depth:
            return "\n".join(lines[start + 1 : i])
    return "\n".join(lines[start + 1 :])


def claimed(text, pattern):
    """The spelled-out number in a claim, as an int. None when the claim is not there at all."""
    m = re.search(pattern, text, re.I)
    if not m:
        return None
    return WORDS.get(m.group(1).lower())


def main():
    if not AGREEMENT.exists() or not TERMS.exists():
        print(f"  {'sow counts':<38} skipped — no {AGREEMENT}")
        return 0

    agreement = AGREEMENT.read_text()
    terms = TERMS.read_text()
    fails = 0

    # Each rule: a name, the claim to find in the agreement, and how to count the real thing in the terms.
    rules = [
        (
            "§6 exclusions",
            r"\b(\w+) things, each written down",
            lambda: len(re.findall(r"^\|\s*\*\*N-\d+", section(terms, r"^## 6\.") or "", re.M)),
        ),
        (
            "§15 accepted risks",
            r"\b(\w+) risks were argued",
            lambda: len(re.findall(r"^\d+\.\s", section(terms, r"^## 15\.") or "", re.M)),
        ),
        (
            "§11.6 payment milestones",
            r"\b(\w+) milestones",
            # Table rows minus the header and its separator.
            lambda: max(0, len([l for l in (section(terms, r"^### 11\.6") or "").split("\n") if l.startswith("|")]) - 2),
        ),
        # The annexe count lives in README.md, not in the agreement — the agreement only ever says "in Annexe A".
        # So the claim is checked where it is actually made. A rule pointed at the wrong file reports "no claim
        # found", which is how this one was caught: the check told the truth about itself on its first run.
        (
            "annexes (README)",
            r"\b(\w+) annexes",
            lambda: len(list((ROOT / "docs/annexes").glob("*.md"))),
            ROOT / "README.md",
        ),
    ]

    for rule in rules:
        name, pattern, counter = rule[0], rule[1], rule[2]
        where = rule[3].read_text() if len(rule) > 3 and rule[3].exists() else agreement
        want = claimed(where, pattern)
        if want is None:
            print(f"  {name:<38} no claim found in the agreement — rule is dead, remove it or fix the wording")
            fails += 1
            continue
        got = counter()
        if want == got:
            print(f"  {name:<38} ok ({got})")
        else:
            print(f"  {name:<38} MISMATCH: the agreement says {want}, the terms hold {got}")
            fails += 1

    # Duplicated numbers inside §15, which is the defect that made the count wrong in the first place and which
    # a total on its own would never have caught: nineteen rows numbering to eighteen looks correct from either end.
    nums = re.findall(r"^(\d+)\.\s", section(terms, r"^## 15\.") or "", re.M)
    dupes = sorted({n for n in nums if nums.count(n) > 1})
    if dupes:
        print(f"  {'§15 numbering':<38} DUPLICATE row number(s): {', '.join(dupes)}")
        fails += 1
    else:
        print(f"  {'§15 numbering':<38} ok (no duplicates across {len(nums)} rows)")

    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
