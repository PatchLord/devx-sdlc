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

**Cost.** An afternoon. **Status.** not started. This is the cheapest experiment we have and it unblocks
every claim in part 6.

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
