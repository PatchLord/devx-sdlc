#!/usr/bin/env python3
"""Is every starter file accounted for in the doc set?

Called by check-docs.sh. Prints "N|<stale>|<not-once>|<unmentioned>" on one line.

WHAT THIS CHECKS, AND WHY IT CHANGED
------------------------------------
The original rule was: every starter file appears in the docs IN FULL, exactly once. That was right when the
starter was twenty short files, and it caught a real defect — an earlier version probed one line per file and
so stayed green while nine inlined copies were stale.

It stopped being right at ninety files. Inlining the orientation and capability layers verbatim would have
added 78,265 words to a 107,000-word standard, most of it .mjs source, and produced a document nobody can
read in order to protect a copy nobody should be keeping.

So the PURPOSE is kept and the MECHANISM is split. The purpose was never "the docs contain a copy" — it was
**nothing enters the starter invisibly**. Two ways to satisfy that, and which one applies depends on whether
the file's CONTENT is the standard or merely an implementation of it:

  INLINE     The content IS the rule, and a reader has to see the exact text to know what is enforced. A
             workflow's `run:` block, CODEOWNERS, settings.json, lefthook.yml, package.json, a template, a
             skill's SKILL.md. These are checked by whole-body containment, exactly as before.

  MENTIONED  The content is an implementation of a rule stated elsewhere. A reader needs to know the file
             exists, what it does and what it cannot do — not its 6,730 words of source. These are checked by
             the file's PATH appearing in the docs at least once. Adding a script without the docs
             acknowledging it still fails.

This is a weakening, and calling it anything else would be the failure this repository warns about. What
makes it defensible is that the property being dropped is "the docs are a byte-exact mirror of the starter",
which was never the property anyone needed, and the property being kept is the one that catches the real
mistake: a file arriving with nothing said about it.

The honest cost, stated: a MENTIONED file's BODY can now drift from its description in the docs, and this
check will not notice. What catches that instead is the file's own `--self-test` plus `scripts/self-test.mjs`
in the starter, which the docs' description has no way to contradict for long.

Also: the walk now respects .gitignore. It did not, and three one-byte hook heartbeat files under
.claude/.hooks-health/ — machine-local, gitignored, regenerated on every run — were being demanded as
inlined content.
"""
import os, pathlib, subprocess

S = pathlib.Path(os.environ.get("STARTER", "../devx-starter"))

# Content that IS the standard. Matched against the starter-relative path.
# Anything not matching here is MENTIONED rather than inlined.
INLINE_PREFIXES = (
    # All of .github/, not only workflows/. Scoping this to workflows/ was a real defect: the pull request
    # template IS the standard — it is what a pull request must contain — and it was inlined in 07-repository.md
    # while being classified MENTIONED, so an edit to it went stale and this check reported ok. The rule is
    # about whether the CONTENT is the standard, and nothing about .github/ that is not a workflow fails it.
    ".github/",
    ".claude/skills/",      # a skill is prose that shapes behaviour — but see SKILL_BODY_ONLY below
    ".claude/agents/",
    ".claude/commands/",
    "docs/",                # templates and the tier-1 rules
    "tasks/board.md",
    # The escalation schema and its template. A record format is a standard: a reader who cannot see the exact
    # fields cannot write one, and every entry in log/events/ is read by scripts/learn.mjs.
    "log/",
)
INLINE_EXACT = {
    "CLAUDE.md", "CODEOWNERS", "REVIEW.md", "lefthook.yml", "package.json",
    ".claude/settings.json", "commitlint.config.js", ".gitignore",
    ".editorconfig", ".gitattributes", "README.md",
}
# Inside a skill directory only the SKILL.md is the standard. Side files exist precisely so that detail is
# loaded on demand rather than carried by every reader — and that argument applies to the human reader of the
# docs as much as to a session. Naming them is enough.
SKILL_BODY_ONLY = True


def tracked(root: pathlib.Path):
    """Files git would keep. Falls back to a filesystem walk outside a repository."""
    try:
        out = subprocess.run(
            ["git", "-C", str(root), "ls-files", "--cached", "--others", "--exclude-standard"],
            capture_output=True, text=True, timeout=20, check=True,
        ).stdout
        return [root / line for line in out.splitlines() if line]
    except Exception:
        # No git, no timeout budget, or a broken index: walk instead, and lose only the .gitignore filtering.
        return [p for p in root.rglob("*") if ".git" not in p.parts]


def wants_inline(rel: str) -> bool:
    if rel in INLINE_EXACT:
        return True
    if SKILL_BODY_ONLY and rel.startswith(".claude/skills/"):
        return rel.endswith("/SKILL.md")
    return rel.startswith(INLINE_PREFIXES)


docs = {p.name: p.read_text() for p in pathlib.Path("docs").glob("*.md")}
alltext = "\n".join(docs.values())

n, stale, notonce, unmentioned = 0, [], [], []

for src in sorted(tracked(S)):
    if not src.is_file():
        continue
    rel = str(src.relative_to(S))
    # board.html is generated from board.md by scripts/board.mjs. Inlining a derivative would mean maintaining
    # a copy of a copy, which is the drift the generated view exists to avoid.
    if src.name == ".gitkeep" or rel == "tasks/board.html":
        continue
    try:
        body = src.read_text().rstrip("\n")
    except UnicodeDecodeError:
        continue  # a binary asset: nothing to inline and nothing to compare
    if not body.strip():
        continue
    n += 1

    if not wants_inline(rel):
        # MENTIONED: the path has to appear somewhere in the docs. A new script cannot arrive unremarked.
        if rel not in alltext:
            unmentioned.append(rel)
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

print(f"{n}|{' '.join(stale)}|{' '.join(notonce)}|{' '.join(unmentioned)}")
