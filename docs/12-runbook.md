# The runbook

The order in which we switch this on, with one testable checkpoint per step, and what to do when a developer
joins a project already running it. Whoever is standing up a repository reads this with
[the repository](07-repository.md), [host and pipeline](09-host-and-pipeline.md) and
[stack wiring](10-stack-wiring.md) open beside them.

## The order, and why it is this order

**This is a sequence, not a schedule.** An earlier version of this document numbered the steps as days, and
that was a mistake worth naming: it invited people to ask which day they were on rather than what was already
true, and it implied that a step could be reached by waiting. Nothing here is reached by waiting. Do the whole
sequence in an afternoon or spread it over a month — the calendar is yours. What is not yours is the **order**,
because several of these steps make a later one impossible if taken in the wrong sequence, and two of them
deadlock the repository outright.

Most checkpoints are a check failing on purpose. A green check on a repository where nothing has ever been red
tells you only that nothing has been tried.

The whole ordering follows one rule: **turn on the check that tells the truth about the other checks first.**
Our pilot repository had an excellent CI pipeline that had run zero times, and a context file claiming branch
protection that did not exist. Every later check inherits its meaning from the perimeter being real. So the
perimeter goes on before it has anything to assert, in order that the first thing it does is fail.

| Step | What turns on | Checkpoint passes when |
|---|---|---|
| 1 | remote, runner, owners, tracker fields | `git remote -v` resolves; three tracker fields exist |
| 2 | **delete the gates you cannot wire** | `perimeter` classifies every workflow that remains |
| 3 | branch protection + `perimeter` | perimeter run #1 is **red**, run #2 is green |
| 4 | `size` required | a 500-line pull request cannot merge |
| 5 | `spec` required | a code-first branch cannot merge |
| 6 | `verify` + `gates` required | an uncovered line and a mixed commit both fail |
| 7 | `review` running, **not** required | a review comment is posted; merge is still possible |
| 8 | one internal project, eight tickets | every gate has failed at least once, for cause |
| 9 | `review` required, if its numbers earned it | 30 findings, dismissal under 1 in 3 over a rolling 20 |
| 10 | first client project, Standard depth | Setup ends with a page live in dev |

### The three orderings that are load-bearing

Not stylistic preferences. Each was found by nearly walking into it on a real host.

**Steps 1–2 before step 3, or you cannot repair what you broke.** Deleting the gates you cannot wire is
around 500 lines, which trips the size ceiling — correctly, because removed enforcement is the change class
that most deserves reading. But once protection is on, the override is a label that
[finding 61](../research/findings.md) proves an author cannot grant themselves. So the deletion happens
before protection, not after.

**A `CODEOWNERS` that resolves, before code-owner review is required.** GitHub ignores an owner it cannot
resolve, so a file naming a non-existent team silently protects nothing — and requiring review against it
deadlocks the branch, because the file that must approve its own repair is the broken one. The instinct is
the reverse order.

**The spec alone in the first commit, the board entry second, implementation third.** Two of our own rules
collide otherwise: `spec.yml` wants the spec to be the branch's first commit *and alone in it*, and also
wants a board entry to exist. `break-it` can never find this, because it tests each gate in isolation.

Before step 1, read [the first run](19-first-run.md). It is the pre-mortem for everything below — how to
choose a first project so the process is exercised rather than performed, and the two dozen things that will
bite while you run it. Most of them look like success, which is why they are worth reading before anyone is
under time pressure.

## Step 1 — the decisions no workflow can make for you

**A remote, on the host you intend to keep.** The pilot's entire failure was downstream of not having one.

**A runner.** Every job in the starter's nine workflow files says `runs-on: arm64`, which is a self-hosted
label. If you do not have that runner, change it to `ubuntu-latest` across all nine in one commit.
`.github/workflows/` is a protected path in [CODEOWNERS](07-repository.md), so that commit needs an owner's
review, and it must not be mixed with anything else or [the `gates` check](06-enforcement.md) will reject it.
Skip this and every check sits pending forever. Pending is not green and merge stays blocked, so the mistake
at least fails in the safe direction.

**Owners.** Replace `@devx/tech-leads` in `CODEOWNERS` with a real team slug holding at least two people. One
name means a fortnight of leave stops promotion to uat.

**Three tracker fields, before any ticket exists:** who found each defect, promotion and release timestamps,
and stage entry and exit dates. These are the three that cannot be reconstructed afterwards. Everything else
in [the six numbers](11-measurement.md) can be back-filled from git history; these cannot.

**A second person, and this one is structural rather than preferable.** One person filling every role
approves their own specs, their own criteria changes and their own pull requests. `CODEOWNERS` becomes
decoration, the perimeter check passes while protecting nothing, and the central gate — never approve your
own work — is fictional. If a second reviewer genuinely is not available for the first run, say so in
writing when reporting the result, because an unstated invalidity is how a trial becomes folklore.

**What claim the first run is meant to support.** Decide it before starting, because it decides whether you
are allowed to tidy up before showing anyone. *The process catches what unstructured work does not* is
provable in a fortnight. *The process is faster* is not, at any ticket count you will reach — and the first
person who asks about sample size wins that argument. Pick the first, and then the most valuable thing you
can show is what got blocked.

## Step 2 — delete the gates you cannot wire

This step exists because of the one failure mode this standard is least able to survive: a check list where
every row is red.

The starter ships more gates than a new repository can satisfy. `review` needs an API key. `verify` needs six
package scripts wired to a real stack. `deploy` and `promote` need environments. Each of those fails loudly
rather than skipping — deliberately, because a gate that quietly does nothing shows a green check for work
nobody read. But **"wired and broken" and "not wired yet" render as the same red X**, and six permanent
failures teach everyone to stop reading the list. After that, a real failure is indistinguishable from noise.

So delete what you cannot wire *now*, and record it as owed. `perimeter.yml` makes the deletion visible rather
than quiet: every workflow must appear in exactly one of `REQUIRED_CHECKS`, `ADVISORY_CHECKS` or
`NOT_A_GATE`, asserted in **both** directions — an unclassified workflow fails the perimeter, and so does a
classified name whose file has gone. You cannot delete a gate and forget that you did.

**Checkpoint: `perimeter` accounts for every workflow file that remains, and the pull request template's check
list has no permanent reds.** On the repository where this was worked out, deleting five unwirable gates took
it from six reds per pull request to all-green — with the only remaining block being the review requirement,
which is the one that *should* block.

Then wire them back one at a time, each with the checkpoint from its own step below. A gate added because
somebody got the key today is a normal change; a gate that has been red since the repository was created is
furniture.

## Step 3 — branch protection, and the check that reads it

Clone the starter, `bun install`, `bun run setup` — that installs the Lefthook hooks, which are hints and not
gates — then push to `main`. Add the `PERIMETER_TOKEN` secret: a fine-grained token with
`Administration: read`. `GITHUB_TOKEN` cannot read branch protection, and if the secret is absent the job
fails rather than skipping.

Then, before setting any protection at all, run `perimeter` by hand via `workflow_dispatch`.

**Pass condition, run #1: the job is red, reporting that `main` has no branch protection at all and every gate
in the repository is advisory.** If it is green, or skipped, stop — you have reproduced the pilot and the rest
of this runbook is theatre. That red run is the artefact proving the perimeter check works. The green one that
follows proves nothing on its own. Paste both run URLs into the project's setup notes.

**Before you set anything: check that `CODEOWNERS` names something that resolves.** The starter ships a
placeholder team, and GitHub silently ignores an owner it cannot find — so the file protects nothing while
looking like it does. Worse, requiring code-owner review against a broken file is unrecoverable: the file
that would have to approve its own repair is the broken one, and no pull request can merge. Land a working
`CODEOWNERS` first, then require the review. This was found by nearly doing it in the wrong order.

Now set protection on `main` to exactly this:

- `required_status_checks.strict = true`
- `required_pull_request_reviews.required_approving_review_count = 1`
- `require_code_owner_reviews = true`, `dismiss_stale_reviews = true`
- `required_linear_history.enabled = true`
- `required_conversation_resolution.enabled = true`
- `allow_force_pushes.enabled = false`, `allow_deletions.enabled = false`
- `enforce_admins.enabled = true`

Linear history is a precondition, not a preference. `gates.yml` walks
`git rev-list --reverse --no-merges BASE..HEAD` commit by commit, and `spec.yml` asserts the spec is the
branch's first commit. A merge commit inside a branch makes both reason about an order nothing was tested in.
The checks still pass; what they proved is no longer what we claim they proved. Conversation resolution is
what turns "every finding gets a disposition" from a sentence in these documents into something the merge
button enforces. [Host and pipeline](09-host-and-pipeline.md) has the full settings and the reasoning behind
each.

`enforce_admins` is the one where leaving it false is defensible on a team of three, because an admin who
cannot merge a hotfix at 22:00 will find another way and you will not hear about it. The cost is exact:
`perimeter.yml` drops that line to a warning, and the perimeter then holds only as long as everyone chooses to
respect it. That choice belongs to a named person recorded in the setup notes, not to whoever is tired.

Two details that will otherwise cost you an afternoon. **Do not require `perimeter` as a pull request status
check** — it runs on a Monday 07:00 UTC schedule, on push to `main`, and on dispatch, never on pull requests,
so requiring it blocks every pull request permanently. And on day 1, set `REQUIRED_CHECKS` in `perimeter.yml`
to `"size"` alone. Never to the empty string: the host refuses `strict: true` with no contexts, and a
perimeter with nothing to assert is the exact failure these documents exist to prevent. You are not
weakening the check, you are making it claim only what is true today. Each later day adds one name back.

**And delete the workflows you cannot wire today.** This is the instruction people skip, and skipping it
produces the one thing worse than a missing gate: five or six checks failing on every pull request forever,
because they were installed before anything satisfied them. A wall of red teaches everybody to stop reading
the list, and after that a real failure is indistinguishable from the noise — which is this whole
repository's failure mode arriving through the back door.

So a gate you cannot satisfy gets **deleted**, in its own commit, with the reason, and recorded as *to
build* in `README.md`. `perimeter.yml` makes that safe rather than quiet: every workflow file must appear in
exactly one of its three lists — `REQUIRED_CHECKS`, `ADVISORY_CHECKS`, `NOT_A_GATE` — and every name in
those lists must have a file. So a workflow nobody classified fails the perimeter, and so does a name we
still claim while its file is gone. You cannot forget in either direction.

Typical day 1 on a fresh repository: `verify` has no stack scripts, `review` has no API key, `scan` has no
alerts enabled, `deploy` and `promote` have no environments. That is five deletions and five *to build*
rows, and the pull request board then shows only checks that mean something.

**Pass condition, run #2: green, printing `The perimeter matches.`**

## Step 4 — the size ceiling

Reviewability is what every human gate downstream depends on, so it goes on before any of them.

Branch `DEVX-1-size-probe`, commit 500 lines of anything, open a pull request. Read the `size` job's log
specifically: it should name 500 lines against the ceiling of 400 lines / 20 files. `spec` will also be red;
ignore it today. Then add `size` to the host's required contexts and to `REQUIRED_CHECKS`, and re-run
perimeter.

**Pass condition: the pull request shows `size` red and the merge button is unavailable.** If merge is
available, the context name on the host does not match the workflow's `name:` field.

Two known holes, and you should be able to recite both. `size` excludes lockfiles, `*.snap`,
`**/generated/**`, `*.generated.*` and `migrations/**/*.sql`, so a 4,000-line generated diff passes. Every
line on that exclude list is review you are not doing, which is why the list stays short. And the
`size-override` label lets a tech lead pass a pull request over the ceiling — deliberately a person's
decision, refused when the author labels their own pull request, and counted as a shortcut in
[the six numbers](11-measurement.md).

## Step 5 — the spec gate

Now that diffs are small, make them planned. Two probes: a branch named in lowercase, which must fail on the
ticket id; and a branch whose first commit is code and whose second is the spec, which must fail on the spec
not being the branch's first commit alone. Then require `spec` and add it to `REQUIRED_CHECKS`.

**Pass condition: both probes red for the stated reason, and a well-formed branch green.**

Say the limit out loud, because it will be quoted at a client. `spec.yml` proves the spec came first. It
cannot prove a person read it. Approval is a review state on the host, and `perimeter.yml` checks that the
host is configured to require one. Whether anyone read the spec is not observable by anything, ever. Do not
write "spec reviewed" anywhere as though it were evidence.

## Step 6 — verify and gates

`verify` fails until you wire it. The starter's `format:check` script is literally an echo followed by
`exit 1`, on purpose: a repository that documents six gates and runs four reports green for the two it never
ran. Wire `format:check`, `lint`, `typecheck`, `test`, `test:coverage` and `build` for your stack — that is
what [stack wiring](10-stack-wiring.md) is for — then `verify` as the chain of them. `test:coverage` must emit
`coverage/lcov.info`, because if that file is absent the changed-line step prints a warning and exits 0. The
gate does not fail; it ceases to exist. The threshold is 80% on changed lines, measured across the whole pull
request against `main`, never per commit.

Probe all three failure modes. Add a file with an uncovered exported function and confirm the run fails at 80.
Make one commit that edits an existing test and a source file together, and confirm `gates` reports that it
mixes a gate change with implementation. Add `continue-on-error: true` to a workflow in a branch and confirm
`gates` fails it. Then require both checks and add both to `REQUIRED_CHECKS`.

**Pass condition: three deliberate reds, then green, with `coverage/lcov.info` visible in the run.**

`gates` catches tests that *became* weaker. It cannot catch a test that was always weak. A 78% suite at a 31%
mutation score passes everything here, which is exactly why whole-repo coverage is not a gate for us.

## Step 7 — the review agent, running and not required

Add `ANTHROPIC_API_KEY`. `review.yml` posts one comment per pull request through the review agent, with tools
limited to `Read,Grep,Glob,Bash(git *),Bash(gh pr *)` — it cannot write. Leave `review` out of the host's
required contexts and out of `REQUIRED_CHECKS`.

That second half is the point. If the perimeter claims a review the merge button does not require, the
repository is lying in the direction the pilot lied. Un-required is honest. Un-required and undeclared is not.

**Pass condition: a pull request carries a review comment, and merge is possible with the `review` job red.**

Start counting dismissals from the first finding. We have no measured accuracy for this reviewer, and the
published picture is unflattering: across 19,450 pull requests (April 2026), those reviewed only by an agent
merged at 45.20% against 68.37% for human-only review. That is why it blocks nothing yet.

## Step 8 — one internal project, end to end

Not client work. The point is to find out what these documents got wrong while nobody is paying for the
answer. Pick something whose cost of being wrong is Light — nothing to undo, no money, no personal data — and
still run the gate set you intend to sell at Standard. The loop, the size ceiling and the gate discipline
never change with [depth](05-depth.md); the internal project exists to exercise the gates, not to right-size
them.

**It must not be greenfield, and this is the constraint most likely to be got wrong.** A fresh toy project —
the to-do app that everyone reaches for — exercises almost nothing this process was built to catch. There are
no existing tests to weaken, so [the gates check](06-enforcement.md)'s central asymmetry never fires. There
is no stale design document, so the divergence field is empty by construction and the one defence that
matters goes untested. There are no patterns already in the codebase, so the explore agent's job is vacuous
and every ticket grades *well-trodden*. Nothing is pre-existing, so that grade is never used. The result is a
green run that proves the happy path is green, which is the exact failure these documents spend their length
warning about.

Pick something with **history, warts and tests somebody else wrote.** An internal project that already
exists and is already disappointing is the ideal first target — and it has the second advantage of making
the comparison legible to whoever is deciding whether to adopt this, because the counterfactual is already
deployed rather than imagined.

Three more constraints on what you pick. It must contain **at least one screen a person types into**, with an
acceptance criterion naming a screenshot or a script. The pilot's admin panel had nine write hooks and zero
buttons, zero forms, zero submit handlers: the write side existed at every layer except the one a human
touches, because the gate it was given could only see reads. It must include **at least one ticket on a
CODEOWNERS-protected path**, so the code-owner review route is walked before a client depends on it. And at
least one ticket must **modify a test that already existed** — otherwise the distinction the whole gate set
turns on, that new tests are implementation and changed tests are a gate change, is never once exercised.

Choose the tickets for **mechanism coverage rather than for what is most broken**. One that touches a
protected path forces a class A escalation. One where the code and the documentation disagree forces a class
B and puts something in the divergence field. One that is genuinely too large either forces a split at the
size ceiling or proves the ceiling is in the wrong place, and both are findings.

Eight tickets minimum across two features, including one spike whose only deliverable is a committed fixture.
Then run [the release checklist](08-templates.md) into `docs/releases/v0.1.0.md` even though the depth table
skips Release Check at Light, including one backup restored to a named place with the time recorded. You
cannot rehearse a restore drill for the first time inside a client's launch window.

**Pass condition: every required check has failed at least once for a real cause, the release file has an
evidence link in every third column, and the Monday cron shows a `perimeter` run nobody triggered.** Any check
that has never gone red across eight tickets is a check you have not tested.

**If you are showing this to anyone, show the blocks.** The instinct is to rehearse until the run is clean,
and it destroys the only evidence worth presenting. A demonstration in which nothing was ever blocked is a
demonstration of a system that does not block. The interesting frames are a gate refusing something with a
failure message the agent then self-heals from, an escalation arriving and being answered in two minutes, the
divergence field non-empty with the design document fixed in the same pull request, and one honest gap in the
evidence. Nobody is impressed by an agent writing code; that is table stakes now.

## Step 9 — the review agent's decision point

Block on it when it has produced **at least 30 findings** and its dismissal rate is **under one in three over
a rolling twenty pull requests** — the same threshold and window [the six numbers](11-measurement.md) defines,
so there is one figure to argue about rather than three. Then add `review` to the required contexts and to
`REQUIRED_CHECKS`. Conversation resolution already forces every finding to end fixed or dismissed in writing.

That threshold is borrowed, not measured, and our own number should replace it. It comes from the only
reviewer that publicly earned trust by measurement: Uber's uReview, whose comments were addressed 65% of the
time against 51% for human comments — first-party and self-reported, which is a reason to treat it as a bar
rather than a benchmark. One in three dismissed is that bar restated for our counting. If the rate is worse,
the agent stays advisory and you tune its prompt. A required check people learn to click past is worse than an
advisory one they read.

## Step 10 — the first client project, at Standard

Standard, not High. High adds mutation floors on core logic, production defined in code, a load test, a threat
model, a restore drill and a second reviewer on protected paths. Doing all of that for the first time on the
same project where you are running the loop for the first time means two unproven things failing together and
no way to tell which one failed.

Setup is the starter plus the day 1–5 sequence, compressed into a day now that you have done it once, and it
ends the same way every [Setup](02-before-build.md) does: one trivial page live in dev, put there by the real
pipeline. The statement of work names the depth and names which checks exist on their project **today**,
marking the rest as still to build. Quoting a written-but-never-run check to a client is the pilot's failure
with a signature underneath it.

## Counting from day one

Five of the six numbers depend on a tracker integration that is not built. Until it is, a tech lead keeps one
sheet with one row per ticket — ticket id, picked up, spec approved, merged, running in dev, whether a human
changed something at the spec, at feature review and at the gate diffs, findings raised, findings dismissed,
shortcuts taken and which, defects raised after merge and who found each — and one row per release: accepted
at the demo, released, and the stage it sat in.

If anything in the gate sequence is cut for time, cut it from the gates and not from the counting. A gate we
have not built is a known absence. A number we never started counting is an answer we cannot get back. Read
all six as trends, never as targets: whoever finds a defect classifies it, so a target would be met by
reclassifying.

## What we deliberately do not turn on first

Mutation floors. Several reviewers voting. Parallel agents implementing one ticket. Human review of every pull
request. Hooks as the enforcement layer. Whole-repo coverage as a gate. Letting the agent write ticket status.
Reading the perimeter's expectations from a config file the agent can edit. Each is argued against in
[limits](14-limits.md) or where the relevant check is defined. The common thread: an apparatus that takes a
month to build cannot be cheaply abandoned when it turns out not to earn its cost.

## Onboarding one developer onto a project already running this

Roughly ninety minutes of reading, and the order matters more than the total.

1. [Why this exists](01-why.md) and [the build loop](04-build-loop.md). Nothing else from these documents yet.
2. The repository's `CLAUDE.md` and `.claude/skills/build-loop/SKILL.md`. These are what the agent has read. A
   developer who has not read them is surprised by what the agent refuses to do and reads that refusal as a
   bug.
3. `docs/design/` for the current phase, and its acceptance criteria under `docs/design/criteria/`.
4. The three most recently merged files in `docs/specs/` — not the template. The template says what a spec
   should contain; a merged spec shows what this project's specs actually contain.
5. `docs/decisions/`, then `CODEOWNERS`, so they know which paths they cannot merge alone.
6. The most recent file in `docs/releases/`, so they know what a release costs here.

They do not read the workflow files on day one. They will read `size.yml` the first time it fails them, which
is when the file means something. They do not get production credentials, on this project or any other.

Their first ticket is chosen, not claimed: well-trodden, no protected path, under 150 lines, with an
acceptance criterion that already names its check. Deliberately boring. They run `/spec TICKET-ID`, answer the
explore agent's questions in one pass, and **the tech lead approves that spec** — inverted from the usual
arrangement, for one ticket only, because reading someone else's answers is how you find out whether they were
specific enough. Then `/build TICKET-ID`, and their job while it runs is to answer, to stop it going the wrong
way early, and to refuse a shortcut that makes a check quieter instead of making the code right.

**Onboarding has worked when, within their first three tickets, all three of these have happened:** a spec was
sent back at least once; a required check went red and they fixed the cause rather than routing around it; and
they dismissed one review finding in writing. If none of the three happened, the tickets were too small or the
gates are not firing. Check the counting before you check the developer, and start at
[troubleshooting](13-troubleshooting.md).
