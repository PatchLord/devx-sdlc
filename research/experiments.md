# Experiments

The evidence we do not have and nobody will hand us. Each entry states the hypothesis, what result
would falsify it, and what we would change if it did. An experiment without a falsifier is a demo.

Ordered by how much they would tell us per hour spent.

---

## E1 — Do the gates actually reject anything?

**Hypothesis.** Every check fails the thing it claims to catch, on a real host.

**Method.** Push the starter to a repository, apply the protection in part 9, then break it on purpose:
a pull request over 400 lines; a commit mixing a gate change with source; a branch with no spec; a
branch where the spec is the second commit; the `size-override` label applied by the author; code-owner
review switched off.

**Falsified if.** Any of those six merges, or any check passes when it should fail.

**Then what.** A check that cannot reject is not a check, and its row moves from *written* to *to build*.

**Cost.** An afternoon. **Status.** **half done, 2026-08-05.** The offline half is built and passing:
`scripts/break-it.mjs` runs 30 cases against the gates' real scripts — every rejection above except the two
that are host facts — plus the legal version of each change, which is what proves a check discriminates
rather than merely refuses.

It found a fourth defect, and this one had shipped. The pathspec exclusions in `size.yml` used
`**/bun.lockb` without `glob` magic, so git's wildmatch required a slash before the filename and a lockfile
**at the repository root was never excluded**. Every dependency change would have counted thousands of
lines against the ceiling and failed `size` for a reason the comment above it says is excluded. Root-level
`*.snap`, `generated/` and `migrations/` leaked the same way. Fixed with `,glob` on all nine patterns,
verified against real paths.

Writing it also surfaced a command-injection hole that no gate could have caught: `spec.yml` interpolated
`github.event.pull_request.head.ref` straight into bash, and git permits `; $ \` ( ) | &` in a branch name.
On a persistent self-hosted runner that is remote code execution, not a spoiled build. Both steps now take
it through `env`.

The harness was then mutation-tested — the substring `is_test_path` and the self-granted override were
reintroduced one at a time, and each was caught by exactly the case written for it. A suite that passes
because it tests nothing looks identical to one that works, so this step is not optional.

**Still open, and only a host can close it:** that a red check blocks a merge, that code-owner review is
enforced, that force-pushes are refused, that stale approvals are dismissed, and that these files are valid
Actions YAML. B1 stays open until the suite in [host and pipeline](../docs/09-host-and-pipeline.md) runs
against a real repository.

---

## E2 — Does the process survive one real project?

**Hypothesis.** A low-depth internal project can run all eight stages and the full loop without the
process being abandoned or quietly bypassed.

**Method.** One internal project, Light or Standard depth. Count every shortcut taken and every gate
overridden, honestly, as they happen.

**Falsified if.** The team routes around the process more than twice, or Setup does not end with
something deployed by the real pipeline.

**Then what.** Whatever got bypassed is either wrong or too expensive. Both are findings.

**Cost.** One project. **Status.** not started.

---

## E3 — Does the review agent earn a required slot?

**Hypothesis.** Its findings are dismissed less than one time in three, over a rolling twenty pull
requests.

**Method.** Run it un-required from day one. Record every finding and its disposition.

**Falsified if.** Dismissal exceeds one in three, or it produces nothing on pull requests where a human
later found a defect.

**Then what.** It comes off the required list and becomes advisory. Published evidence would not be
surprised.

**Cost.** Free, if counting starts immediately. **Status.** not started — and it is unrecoverable if we
begin counting late.

---

## E4 — What is our baseline defect rate?

**Hypothesis.** Defects reaching a person, per merged ticket, is stable enough that a change in it
means something.

**Method.** Record who found every post-merge defect from the first ticket: review agent, tech lead,
QA, client, production.

**Falsified if.** The rate is so noisy at our ticket volume that no trend is readable within a quarter.

**Then what.** Number 5 is not usable at our scale and should be dropped rather than watched.

**Cost.** One tracker field. **Status.** not started. Cannot be reconstructed later.

---

## E5 — Where does review actually stop working?

**Hypothesis.** There is a diff size beyond which reviewers stop finding anything, and 300 lines is
near it.

**Method.** Record diff size against defects found in review, per pull request, over one project.

**Falsified if.** Findings per pull request do not fall with size, or the inflection is far from 300.

**Then what.** Move the ceiling to where the evidence puts it. §14 already says it is judgement.

**Cost.** Free alongside E4. **Status.** not started.

---

## E6 — Can evidence be made machine-falsifiable rather than merely green?

**Hypothesis.** For a bug fix, re-running the new test at the base commit and requiring an
**assertion-level** failure — a captured expected/actual pair, not a collection, import or compile error —
is buildable on our stack and catches tests that assert nothing.

**Why it is an experiment and not an edit.** ADS-1's version of this is its strongest idea and our nearest
equivalent is a `REVIEW.md` line, which is tier 2 and probabilistic. It was refuted as an immediate change
(finding 42) for build-cost reasons, not because the principle is wrong: it needs a machine-readable test
report per harness, a disposition for unsupported cases, and `verify.mjs` currently hard-fails on any missing
GATES script. Its sibling, red-on-stub, is conceded broken by ADS-1's own hostile review.

**Method.** On one repository, one language, one test runner. Take ten merged bug fixes; for each, check out
the base commit, apply only the test, and record whether it fails and *how* — assertion, compile error, or
pass. No gate, no workflow. Just the distribution.

**Falsified if.** Fewer than about half fail by assertion at base. If most fail by compile error, the gate
would be satisfiable by tests that assert nothing, which is worse than not having it — ADS-1's own reviewer
reached exactly this conclusion about its net-new half.

**Then what.** If the distribution is good, it becomes a sixth gate scoped to one language with a published
support matrix and a first-class N/A disposition, never a tech-lead waiver — because routine waivers on a
check labelled non-negotiable teach the org that blocking checks are negotiable. If it is bad, the principle
stays at tier 2 in `REVIEW.md` and this is recorded as settled.

**Cost.** An afternoon on existing history, and it needs no host. **Status.** **DONE, 6 August 2026 —
hypothesis supported, and it produced a better mechanism than the one it was testing.**

### Result: 11 of 12 failed by assertion

Subject: `iamkun/dayjs`, a public repository — chosen over a client project deliberately, so the result is
citable and anyone can re-run it. Twelve commits whose message begins `fix` and which touch both `src/` and
`test/`, from 2023 onward. For each: check out the parent, bring in **only** the test files from the fix, run
those files, classify the failure. Raw output in [`e6-results.tsv`](e6-results.tsv); harness and `TZ` pinning
described below because dayjs tests are timezone-sensitive.

| Verdict | Count |
|---|---|
| **ASSERTION** — the test ran and its assertion disagreed | **11** |
| **COLLECTION** — the suite could not load | 1 |
| PASS-AT-BASE — the test does not catch the bug it claims to | 0 |

Verified rather than trusted, on two of the twelve. `fefdcd4b6` at base produces a real captured pair —
`Expected "2023-10-28T17:00:00Z"`, `Received "2023-10-28T21:00:00Z"` — and the control the harness did not
originally run confirms the same file passes 13 of 13 once the fix is applied. So the finding is fail-at-base
*and* pass-at-fix, which is what the gate actually requires.

### The single exception is the whole point

`6a42e0d73` is labelled `fix: Add NegativeYear Plugin support` and it **adds a new file**. At the base commit
the test cannot resolve `../../src/plugin/negativeYear`, so it fails with `Cannot find module`. It is a
feature wearing a `fix:` label, and it is the only one of the twelve that behaved that way.

**So the discriminator is not the language, and it is not the test runner. It is whether the change modifies
existing behaviour or introduces a new symbol.** That reframes the mechanism:

> A bug fix, by definition, changes behaviour that already exists — so its test compiles and loads at the
> base commit and fails on the value. A change that adds a new export is not a bug fix in this sense, however
> its commit message is worded.

### What this changes about how to build it

ADS-1's own correction asked for a per-language support matrix and routed unsupported cases through a
tech-lead waiver — while elsewhere warning that routine waivers on a check labelled non-negotiable "spend the
one budget of gate credibility". This result removes that tension, because **the N/A case can be decided
mechanically instead of by a person**:

- Run the new test at the base commit.
- If it fails with an **assertion** and a captured expected/actual pair: the proof is stored, the gate is
  satisfied.
- If it fails because an import or symbol **does not exist at base**: this is not a behaviour fix, the gate
  records **N/A with the unresolved import as the reason**, and no waiver is involved.
- If it **passes**: the gate fails, and it has caught the thing it exists to catch — a test shipped with a
  fix that does not detect the bug. None of the twelve did this, which is worth knowing and is not the same
  as it never happening.

No support matrix is needed for that. The three outcomes are distinguishable from the test runner's own
report on any runner that separates a load failure from an assertion failure, which jest, vitest and pytest
all do.

### What this does not establish

- **One repository, one language, no compile step.** dayjs is pure functions over dates. A compiled language
  would surface the new-symbol case as a compile error rather than a module-resolution error — the same
  bucket, reached differently — but the behaviour case should be identical.
- **The selection is biased toward the answer, and deliberately so.** Filtering for `fix:` commits that touch
  both source and tests selects for exactly the class red-on-base targets. That is the correct population to
  measure, and it is *not* evidence about what fraction of all commits the gate can cover.
- **n = 12.** Enough to kill the hypothesis had most failed on collection; not enough to put a percentage in
  front of a client, and none appears in these documents.
- `TZ` was pinned to `America/New_York`. dayjs's own test script runs four timezones, so a different pin
  could move an individual case, though not the assertion-vs-collection split.

**Then what, now that it is answered. BUILT, 6 August 2026.** `red-on-base.yml` and
`scripts/red-on-base.mjs` in the starter, with the four verdicts above and the mechanical N/A. Not in
`REQUIRED_CHECKS`: it reports and merging ignores it until it has produced findings on real work, the same
rule `review` follows.

Proven three ways, because a gate nobody has watched reject anything is indistinguishable from one that
cannot. Its classifier is self-tested against **real captured runner output**, including the two outputs from
this experiment, and that self-test runs in CI. And it was run end to end against three throwaway
repositories: a genuine bug — a discount applied before tax instead of after — classified ASSERTION and
passed the gate; a commit adding a new module classified NOT-A-BEHAVIOUR-FIX and passed; and a commit
declaring `fix(ship):` whose test only asserted `typeof === "number"` **failed the gate**, which is the case
it exists for.

Building it found one defect that no amount of self-testing would have: the gate read **its own stored proof
back as a test file**, because `.evidence/red-on-base/test_total.test.js.txt` matches a test-path pattern. In
a repository that gitignores `.evidence/` it would never have surfaced; in one that does not, the gate would
have reported verdicts on its own output. Selection is now restricted to source extensions with `.evidence/`
excluded, and the reason is in the script.
