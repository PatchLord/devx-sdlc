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
