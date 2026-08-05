# The build loop

The complete per-ticket procedure: seven steps from ticket to merge, and the three agent roles that run
them. This is the document a developer lives in — read it once end to end, then keep it open at the step
you are on.

Build, test and deploy are one loop, run once per ticket, not three stages in a row. One ticket, one branch,
one pull request, one merge, and nothing in `main` that did not come through it. All of it sits inside stage
04; what comes before is in [before build](02-before-build.md), what comes after in
[delivery](03-delivery.md).

The loop exists for one reason. Generation got dramatically cheaper and review did not move at all, so the
constraint moved from writing code to checking it. A 2026 telemetry study covering 22,000 developers measured
where the surplus lands: median time in review up 441.5%, incidents per pull request up 242.7%. Every rule
below tries to keep the checking side of that ratio from collapsing, and each is stated with its cost,
because a rule whose cost you cannot see is a rule people route around.

## One kind of ticket, and two ceilings

There is one unit of work. A phase holds features; a feature is a label over a group of tickets whose
acceptance criteria already sit in the design document; the ticket is the only thing anybody works on. When a
feature's tickets are all merged there is something to demo. A group of tickets that cannot be demoed is not
a feature, it is a folder.

**A ticket is sized by how much a person can read: 300 changed lines and 10 files as the target, 400 lines
and 20 files as a hard failure.** The `size` check measures the whole pull request against its base — not per
commit — warns between 300 and 400, and exits 1 above 400 or 20. Its code is in
[enforcement](06-enforcement.md).

The reason is not the agent's capacity. It is ours. Past some size a reviewer stops reading and starts
approving, and a review that has become a rubber stamp is indistinguishable from no review while still
producing a green check. That argument gives a direction, not a number: **300 is our judgement and we have
not measured it.** The measurement that would replace it is not how many lines a reviewer can read but the
size at which they stop finding anything, and we have not run it. Treat 300 as the current setting of a dial,
not as a finding.

Three details matter operationally.

**Size to the review, not to the clock.** Two days of agent work is thousands of lines. A ticket scoped as
"about two days" holds ten or more readable units and will fail the ceiling every time.

**Generated content is a separate class.** The check excludes `*.lock`, `bun.lockb`, `package-lock.json`,
`pnpm-lock.yaml`, `yarn.lock`, `*.snap`, `**/generated/**`, `*.generated.*` and `**/migrations/**/*.sql`.
Lockfiles and vendored code get their own pull request and are checked for reproducibility rather than read.
The excluded migrations line is the uncomfortable one: SQL migrations are the most dangerous thing in most
repositories and they do not count towards the ceiling. What covers them instead is `CODEOWNERS` — migrations
are a protected path, so they need a second named person however few lines they are. Delete one of these
exclusions and you are adding review you were not doing; add one and you are removing review you were.

**Over the ceiling, the answer is to split the ticket.** There is an escape: a `size-override` label, and the
pull request must say why splitting was impossible. It is deliberately a label rather than an agent decision.
The check reads the repository's label events to find who applied it and fails if that is the pull request's
own author — an override you granted yourself is a bypass, not an override — and it also fails if no
labelling event can be found at all. What it still cannot do is tell a tech lead from any other account with
write access. The record in the pull request is the audit trail, and the audit trail is the only thing making
the override honest.

## The seven steps

```
┌─ 1  CONTEXT  ·  agent ─────────────────────────────────────────────────────────────────┐
│ reads the ticket, docs/design/, docs/decisions/, docs/fixtures/,                       │
│ and the code as it is now — not as the design document says it is                      │
│ hands on: nothing. This step is reading.                                               │
└────────────────────────────────────────────────────────────────────────────────────────┘
                                             ▼
┌─ 2  QUESTIONS  ·  agent asks, developer answers ───────────────────────────────────────┐
│ everything unclear, contradictory, or better done another way,                         │
│ in one pass, before any code exists                                                    │
│ hands on: answers in the developer's own words                                         │
└────────────────────────────────────────────────────────────────────────────────────────┘
                                             ▼
┌─ 3  SPEC  ·  agent writes, developer approves ─────────────────────────────────────────┐
│ docs/specs/<TICKET-ID>.md — criteria, questions and answers,                           │
│ the patterns to follow, out of scope, how each criterion is proven                     │
│ hands on: the spec as commit 1 alone, approved ON THE HOST                             │
└────────────────────────────────────────────────────────────────────────────────────────┘
                                             ▼
┌─ 4  IMPLEMENT  ·  agent, unattended ───────────────────────────────────────────────────┐
│ its own steps, one commit each · checks on every commit                                │
│ two retries on a red check, then it stops and asks                                     │
│ hands on: gate changes in their own commits, size under 400/20                         │
└────────────────────────────────────────────────────────────────────────────────────────┘
                                             ▼
┌─ 5  VERIFY  ·  machine, then a second agent ───────────────────────────────────────────┐
│ the named check per criterion · something operated every write flow                    │
│ then the review agent, which neither explored nor wrote it                             │
│ hands on: every finding fixed or dismissed in writing                                  │
└────────────────────────────────────────────────────────────────────────────────────────┘
                                             ▼
┌─ 6  WRAP  ·  agent ────────────────────────────────────────────────────────────────────┐
│ fix the documents this change made wrong · route every learning                        │
│ fill in the pull request: evidence, and what it does not verify                        │
│ hands on: five green checks — size gates spec verify review                            │
└────────────────────────────────────────────────────────────────────────────────────────┘
                                             ▼
┌─ 7  MERGE → DEV  ·  pipeline, on green ────────────────────────────────────────────────┐
│ one human approval, code-owner approval on any protected path                          │
│ status derived from the merge, never written by an agent                               │
│ next: the ticket waits on its feature being judged in dev                              │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

Everything the person owes across the whole loop is four things: answer the questions once, in writing;
approve the spec on the host; operate the flow at step 5 if no browser test does; approve the pull request,
and approve again as code owner if it touches a protected path. Stopping a run that is going the wrong way is
allowed at any point and is not a duty. None of the four is reading every line.

## The three roles differ by tool permission

Three roles, in sequence, each with a fresh context. Not one agent doing everything, and not a swarm.

```
┌─ EXPLORE ──────────────┐    ┌─ IMPLEMENT ────────────┐    ┌─ REVIEW ───────────────┐
│ fresh context          │    │ fresh context          │    │ fresh context          │
│                        │    │                        │    │                        │
│ Read  Grep  Glob       │    │ Read  Grep  Glob       │    │ Read  Grep  Glob       │
│ Bash                   │    │ Bash                   │    │ Bash                   │
│ WebFetch               │    │ Write   Edit           │    │                        │
│ Write                  │    │                        │    │                        │
│                        │    │                        │    │                        │
│ no Edit — cannot       │──▶ │ no WebFetch — reads    │──▶ │ no Write, no Edit —    │
│ change a line of       │    │ committed fixtures,    │    │ cannot fix what it     │
│ code that exists       │    │ never the live system  │    │ finds, cannot merge    │
│                        │    │                        │    │                        │
│ writes ONE file:       │    │ writes code, tests,    │    │ writes one comment:    │
│ the spec, then stops   │    │ commits, the PR        │    │ its findings           │
└────────────────────────┘    └────────────────────────┘    └────────────────────────┘
            │                             │                             │
            ▼                             ▼                             ▼
    a person approves            the required checks           a person judges the
  the spec, on the host          decide, server-side              feature in dev
```

**The roles are real because their tool lists differ.** A role that is only a name is a naming convention,
and a naming convention does not stop anything. Explore has `Write` but not `Edit`, so it can create the spec
file and cannot rewrite existing code. Implement has `Edit` but not `WebFetch`, so it works from committed
fixtures rather than from whatever an external system returned this afternoon. Review has neither `Write` nor
`Edit`: it reports and cannot fix, which is what keeps it from becoming a fourth implementer. The three
definitions live in [the repository](07-repository.md), which is why the loop is the same on every project
rather than something each developer re-derives.

Two honest limits. Explore holds `Bash`, and `Bash` can write files — the tool list shapes behaviour, it is
not a jail, and what actually stops explore from implementing is the `spec` check refusing a first commit
containing anything but the spec. And in CI the review agent runs with
`--allowed-tools "Read,Grep,Glob,Bash(git *),Bash(gh pr *)"`. `Bash(gh pr *)` is wider than "post one
comment"; the read-only claim there rests on the prompt, not the tool list, and it should be narrowed to
`gh pr view` and `gh pr comment`. That is a known gap, not a thing the file already handles.

Review is separate because a session reviewing its own work catches less than a fresh one does, and repeating
the self-review does not close the gap. The three run in sequence rather than in parallel: on focused coding
work a single well-prompted agent matches or beats multi-agent arrangements at a fraction of the cost, and
parallel agents are safe only when they do not need to agree with each other — the exact opposite of
implementing one ticket.

Underneath all three sits one session-level policy — the deny and ask lists in
[`.claude/settings.json`](07-repository.md). Read it for what it is: pattern matching over command strings.
`Bash(git push*origin main*)` does not match `git push origin HEAD:main`, and `Bash(gh pr merge*)` does not
stop a `gh api` call that merges. The file is also inside the agent's reach. What actually stops a push to
`main` is branch protection, in [host and pipeline](09-host-and-pipeline.md). The settings file removes
accidents; it does not remove the need for the perimeter.

## Step 1 — Context

The agent reads the ticket and its acceptance criteria, `docs/design/` for the phase, `docs/decisions/`,
`docs/fixtures/`, and the code as it currently is rather than as the document claims. The project folder is
there for questions of the form "what did the client actually say".

One rule governs anything from outside the repository: **needed once, fetch it; needed again, commit it.** An
external system's response shape, a design frame, a library's documented behaviour — the second time it
matters, it becomes a file in `docs/fixtures/` with credentials and personal data stripped before it lands.
Fetching live during implementation makes the result depend on which tools a developer happened to have
connected that day, and a failure like that cannot be reproduced. This is why implement has no `WebFetch` and
explore does.

## Step 2 — Questions, all at once

The agent asks everything it needs in a single pass, before writing anything. Not only where the design
document is unclear: also where the document and the code contradict each other, where something was never
specified, where a better approach is visible, and where the existing code looks wrong.

One pass is the point. Questions dribbled through the day cost a developer more attention than the ticket
saves, and an agent that has learned to interrupt will interrupt instead of reading.

The developer answers in writing, properly. **Where an answer corrects the design document, the document gets
corrected** — not only this ticket's spec. Skip that and the next ticket rediscovers the same divergence, and
the ticket after that one. A divergence found in exploration is the most valuable thing exploration produces,
because it is the one finding that pays out on every later ticket.

## Step 3 — The spec, and the three rules that make it load-bearing

The spec takes minutes to read, because the design document already holds the design. It is the handoff
between explore and implement, and three rules are what stop it being a formality. The template it is written
from, heading by heading, is in [templates](08-templates.md).

**One. It carries the questions and the answers in the words they were given.** Implement runs in a fresh
context and never sees the exploration conversation. An answer that is not in the spec did not happen. Not
paraphrased, either — a paraphrase is where a developer's "only for orders that already shipped" turns into
"for completed orders".

**Two. The approval is a state on the host, set by a person — never a field inside the spec file.** The agent
writes that file. A `status: approved` line in it is the agent approving itself, which is the same failure as
a self-maintained status board. In the starter, approval is an approving review on the pull request, backed
by a required approving review count of at least one on `main`.

**Three. The spec is the branch's first commit, alone, and an ancestor of every implementation commit.** The
`spec` check derives the ticket id from the branch name, requires `docs/specs/<TICKET-ID>.md` to exist at
HEAD, takes the first commit from `git rev-list --reverse --no-merges BASE..HEAD`, and fails unless that
commit changed exactly one file and that file is the spec. This closes the route the first two rules leave
open: implement freehand, then write a plausible spec afterwards. A spec written after the code is a
description of what was built, and the approval that gated it was approval of nothing. The same check warns —
does not fail — when the spec is edited in any later commit, because revising a spec mid-flight is
legitimate and revising it quietly is not.

That third check has a precondition, and it is why required linear history is not a style preference.
`git rev-list --no-merges BASE..HEAD` on a branch with merge commits pulls in commits that came from
somewhere else, and "the first commit on this branch" stops meaning what we claim. The same is true of the
per-commit gate-mixing check. Both reason with `rev-list`; linear history is what makes that reasoning sound.

**When the draft pull request opens, and who opens it.** With the spec commit, as a draft, by whoever ran
`/spec`. Approving the spec means an approving review on that draft pull request, which is why it must exist
before implementation starts. `/build` marks it ready for review when it finishes; it does not create it. One
consequence: stale-review dismissal means pushing implementation commits dismisses the spec approval, which
is correct — that approval was of a one-commit branch. The record stays in the review history, and the
approval that gates the merge is a separate one given against the finished work.

Two things these rules cannot do. **No check proves the spec was read** — a person can approve in four
seconds. And because stale reviews are dismissed, the approval visible at merge time is not the same object
as the spec approval, and nothing in CI compares their timestamps. A tech lead can compare them by hand:

```
gh pr view <n> --json reviews --jq '.reviews[] | "\(.submittedAt) \(.state) \(.author.login)"'
```

against `git log --format='%aI %h %s' main..HEAD`. That is a manual check, not a gate, and it is honest to
call it that. The alternative the `/build` command also accepts — a `spec-approved` label — is weaker,
because the `spec` check never asks who applied it. The deny list refuses `gh pr edit --add-label` to the
agent, but that is a hint in a file the agent can reach, not a permission on the host. Prefer the review
route.

## Step 4 — Implement, unattended

After approval the agent picks its own steps and commits one per step, pushing as it goes so progress is
observable and no single diff becomes unreadable. It stops to ask only before something critical or
irreversible. Nobody watches it work. How tight a leash it runs on is set by the spec's novelty answer and by
the project's depth tier, both in [depth](05-depth.md).

**What makes unattended work safe is not the instructions.** Instructions are advice; the agent can depart
from them and sometimes will. Three facts about the session are what make the failure modes survivable:

1. It holds no production credentials. Every serious agent-caused incident on record traces to standing
   access with no gap between deciding and doing, and the fixes that worked were credential scoping and
   environment isolation, not better prompts.
2. It cannot push to `main`. Branch protection, not the deny list.
3. It cannot approve and cannot merge. The approve and merge buttons are outside the repository.

So the worst realistic outcome of an unattended run is a bad branch. A bad branch costs the time it took to
produce and nothing else.

**Checks on every commit.** Format, lint, types, tests, coverage on the changed lines, a secret scan, and the
size ceiling. Locally these run as Lefthook hooks for speed; on the host they run as the required checks
`size`, `gates`, `spec`, `verify` and `review`. The local half is a hint — `--no-verify` walks straight past
it and an agent can edit the hook file — and the host half is the gate. Never confuse the two.

**Two retries, then ask.** A red check means fix the cause and try again; after two attempts the agent stops
and asks the developer. An agent looping on a failing gate burns budget without producing evidence, and
worse, a long enough loop eventually finds the option that makes the check quieter rather than the code
right. Two is a budget guess, not a measured optimum. If you tune it, tune it down.

**One migration in flight at a time.** Migration files sort by name, and two branches each adding one will
not agree on the order they were tested in. A second branch adding a migration rebases onto the first before
it merges. This one has no check today — a `migrate` workflow, which would apply migrations from scratch and
on top of `main`'s schema, is not written. Until it exists this is a convention a person tracks, which means
it will be broken at some point, and the cost when it is broken is a production migration order nobody ever
ran.

### Gate changes go in their own commit

**Weakening a check is allowed. Hiding it inside a feature commit is not.** The `gates` check walks every
commit in the pull request and fails any commit that touches both a gate path and an implementation path. The
gate paths are the workflow files, `lefthook.yml` and `.lefthook/`, `CODEOWNERS`, `CLAUDE.md`, `.claude/`,
`docs/design/criteria/`, the three scripts in `scripts/`, and the test-runner, linter and coverage
configuration files. It also fails a pull request that adds `continue-on-error: true` or `if: false` to a
workflow, adds a trailing `|| true` that swallows a whole step, or adds `.skip(`, `.todo(`, `xit(`,
`xdescribe(`, `@pytest.mark.skip` or `t.Skip(`.

The rule that makes the whole thing workable is an asymmetry: **adding a new test for new code is
implementation. Modifying or deleting an existing test is a gate change.**

Without that asymmetry there is no legal commit ordering at all. Suppose every test file counted as a gate.
Then a commit containing only tests lands red — the code they test does not exist yet — and a commit
containing only implementation fails changed-line coverage, because nothing covers it. The two must be in one
commit, and if tests are gates then that commit is illegal. The asymmetry is what makes a ticket committable:
new tests ride with the code they test, and the moment you touch a test that already existed, that is a
separate commit with a separate conversation.

Recognising "a test file" is anchored on filename suffixes and directory names, never on substrings: the
obvious version classifies `src/attestation.ts` as a test and lets a source file ride along in a gate-only
commit.

The same reasoning is why size and changed-line coverage are measured **on the whole pull request against
`main`**, never per commit. The `verify` check runs changed-line coverage with a floor of 80 percent, and it
has a hole worth knowing: if your test step emits no `coverage/lcov.info` the step warns and passes, so on a
project that has not wired coverage output the gate does not exist. [Stack wiring](10-stack-wiring.md) is
where you close that.

The failure this guards against is not hypothetical. Agents have been observed deleting most of a test suite
and reporting success, hardcoding values to match assertions, and editing a workflow to drop the failing job,
with the pipeline green throughout. In one documented 2026 run, 104 passing tests became 63 failing ones
across six commits that used `--no-verify`, stash and quiet flags. **Green CI is not evidence when the agent
can edit CI.** Which is why gate-touching diffs are read by a person daily, with the deltas named: test count
84 to 61, coverage floor 85 to 70, a job removed, an assertion loosened in a test that stayed.

Whole-repo coverage is not a gate here. One worked example reports a suite at 78% line coverage scoring 31%
on mutation testing with the same model writing both sides — a percentage that high is easy to reach and says
almost nothing about whether the assertions mean anything.

## Step 5 — Verify the output, not just the tests

Each criterion named its check in the spec. Verification is producing that artefact: the named test with its
name, the screenshot compared against the design frame, the actual response from the actual endpoint, the
query output. **Nobody writes "verified" as prose.** The word is a claim; a name is a thing someone else can
go and look at.

**A ticket with an interface is not done until something has operated it.** Either a browser test clicks the
flow, or a named person did and attached the screenshot. "It renders" is not the same check and does not
catch the same class of failure.

That rule comes straight out of our own pilot, and it is the most instructive thing in it. The admin panel
shipped with 9 write hooks and 0 buttons, 0 forms and 0 submit handlers — the write side existed at every
layer except the one a human touches. It was not a capability problem: the same model in the same session
wrote a complete working write flow elsewhere in the same build, with validation, a disabled-until-valid
control and a submit. The explanation is in the agent's own build report, which notes that the admin app had
no unit suite and that its gate was therefore the render verification. It chose a gate that could only see
reads, and only reads got built.

**The agent builds to the shape of the check. A weak gate does not give you the same product less verified;
it gives you a different, smaller product.** Sort the pilot's requirements by how they were expressed and the
same law shows up as arithmetic: 8 of 8 requirements that had a gate were present and correct, 0 of 7 written
only as prose were present at all. That is one project of ours with no control group, not a published
measurement — it is the reason we believe the rule, not proof of it.

The operational consequence: **write flows are enumerated as separate criteria.** "Manage questions" is one
line in a spec and at minimum eight flows in reality — create, edit, delete, the error case on each, the
empty state, and whether you can log in to do any of it. If it is not enumerated it is not checked, and if it
is not checked it will not be built. For work with no interface — a worker, a pipeline, an integration — the
criterion names a query or an output file and the screenshot rule does not apply; running it against real
data and reading the output is the same rule in a different medium.

Then the review agent reads the finished ticket in a fresh context, ordering its findings so the gate surface
comes first. The `review` workflow **fails rather than skips** when `ANTHROPIC_API_KEY` is absent, which is
deliberate: a review job that quietly does nothing produces a green check for work nobody read, and that is
worse than having no review job at all.

Its findings are input, not verdicts. **A finding the developer believes is wrong is dismissed in writing on
the pull request**, not argued with in code. A check with no honest exit trains people to satisfy it rather
than answer it. And the state we require is not "no findings" but "every finding has a disposition, fixed or
dismissed" — enforced by required conversation resolution on `main`. A reviewer that says nothing scores
perfectly and catches nothing, so absence of findings can never be the passing condition.

We hold this agent at arm's length on purpose. Across 19,450 pull requests measured in 2026, those reviewed
only by agents merged at 45.20% against 68.37% for human-only review, and 12 of 13 agents averaged below a
60% signal ratio; an independent three-and-a-half-week run of four reviewer bots on one codebase found they
never converged on a single finding. The counterexample is instructive rather than reassuring: Uber's
reviewer earned its place by measurement, benchmarking its comments at a 65% address rate against 51% for
human comments. Ours has no such number yet, which is exactly why dismissals are one of the six numbers in
[measurement](11-measurement.md), and why the review check starts un-required and becomes required only once
its dismissal rate has earned it.

## Step 6 — Wrap

Two jobs, both cheap and both routinely skipped.

**Fix the documents this change made wrong.** Not "write documentation" — that produces volume. This is
narrower: the design document said the endpoint returned a list, the ticket made it paginated, so the design
document is now wrong and gets corrected.

**Route every learning to its destination.** A learning recorded only as prose will be discovered again by
the next agent on the next ticket.

| What was learned | Where it lands |
|---|---|
| Behaviour nobody specified | a test now, plus a *proposed* criterion in `docs/design/criteria/` for a person to approve |
| An external system's real shape | a fixture in `docs/fixtures/`, credentials and personal data stripped first |
| A decision with real alternatives | a record in `docs/decisions/`, from the decision template |
| Something that will trip every future agent | a rule in `CLAUDE.md` |
| The design document was wrong | the design document |
| Anything that moves scope | the CSM, before it moves |

Then the pull request body, from [the template](07-repository.md). It is short because each section is a
thing that vanished when it was optional: the ticket, the spec link, the criteria table with evidence against
every row, what was learned and where it landed, and what this does not verify. That last section is the one
to defend hardest. An account of the work that claims everything is checked is not an account of the work.

## Step 7 — Merge on green

Merge requires all five checks green — `size`, `gates`, `spec`, `verify`, `review` — with strict status
checks, so the branch must be up to date with `main` before it goes in. One approving review, code-owner
review so any protected path pulls in its named owner, every conversation resolved, linear history, and force
pushes off. The settings, and how to prove they are actually applied, are in
[host and pipeline](09-host-and-pipeline.md).

**The agent has no permission to write a status.** Ticket state is derived from what happened: branch pushed,
checks green, review approved, merged, promoted. This is not fussiness. Our own pilot maintained its own
board and marked its own work done, and agents report success most readily when handed a completion signal to
write to. Give an agent a status field and it will write to it; the only reliable fix is not to have one.

Merging is not the end of the clock. The measured number for a ticket stops at **running in dev**, not at
merge, because a feature that is not deployed is not finished. When a feature's whole set of tickets is
merged, the tech lead judges the feature — opened in dev, as a user, deciding whether it works and whether
the edge cases hold, not reading the diff. On approval the same build is promoted to uat, where QA tests it
and the client's decision-maker accepts it at the demo. Promoted, never rebuilt. That path is
[delivery](03-delivery.md).

After a merge, **a fix is a new ticket, never a reopened one.** A merged ticket is a historical fact, and
making *done* reversible means the board cannot be trusted. The new ticket records **who found the defect** —
the review agent, the tech lead, QA, the client, production — because that split is one of the six measured
numbers and it cannot be reconstructed later. And **every defect a person found leaves a check behind**:
correct the code, and add the check that would have caught it. Without the second half, the same class
arrives on the next feature.

## The loop as the agent reads it

All of this is in the repository as a skill, so the agent has it without being told and the process is the
same on every project. The committed version numbers the steps differently — it splits out the ticket and the
approval and folds context into explore. It describes the same path, the two numberings should be reconciled,
and until they are the file is what the agent actually reads, so the file wins. It is inlined in
[the repository](07-repository.md).

What this loop deliberately does not do — no parallel agents on one ticket, no human review of every pull
request, no whole-repo coverage gate, no rule saying "understand every line you ship" — is in
[limits](14-limits.md) with the reasoning, so nobody re-adds them believing they were overlooked.

> **The spec is written at development time, one ticket at a time — never in advance.** A spec's value
> is being accurate about the code as it is now, and one written nineteen tickets early describes a
> repository that will not exist. What *is* produced in advance is the contracts. See
> [the artefacts](17-artefacts.md) for why, and for which documents live and which freeze.

## How a developer actually spends the day

The loop above is what happens to a ticket. This is what happens to you, and it is a different shape
from how anyone worked two years ago. The short version: **you are not writing the code and you are not
reading all of it either.** You are deciding what gets built, supplying the context that makes a good
result likely, and checking the artefacts that prove it happened.

### The four things that are yours

1. **Answer the agent's questions**, once per ticket, in one pass. This is the half-hour that decides
   most of the outcome. Everything you do not say here, the agent guesses.
2. **Approve the spec.** Minutes, before any code exists. The cheapest possible moment to be wrong.
3. **Judge the feature running in dev** — not the diff. Does it work, do the edge cases hold, would a
   client accept it.
4. **Read the gate-touching diffs**, ten minutes a day, batched. Every diff across every project that
   changed a test, a threshold, CI or a hook.

Nothing else is yours by default. In particular, reading every line of agent-written code is not on the
list, and that is deliberate: sixty small tickets cannot each carry a line-by-line read, and on a
single-developer project there is nobody to do it. What compensates is that the checks are server-side,
a separate agent reviews every ticket, the diff is small enough to read when you do look, gate changes
are visible by construction, and the feature is judged as a working thing.

### What you should stop doing

**Booting the app to take a screenshot.** The `operate-app` skill exists so the agent produces the
evidence and you look at it. If you find yourself doing this by hand, the skill is missing something
for this project and that is the thing to fix.

**Writing the same review comment twice.** The second time is a signal, not a chore. Run
`garbage-collect`: name the class, put a lint or a structural test behind it, and migrate the existing
violations in the same pass. A reviewer is probabilistic; a lint is not.

**Typing "continue".** Worth stating as a rule of its own, because it is the most useful diagnostic you
have. *Every time you have to tell an agent to keep going, the harness failed to say what finishing
looks like.* Sometimes the answer is a skill, sometimes an acceptance criterion, sometimes a clearer
exit condition in the spec. It is almost never "the model is not good enough". Notice how often you do
it — the count going down is the clearest evidence the harness is maturing.

### The skills, and why there are few of them

Skills are how a project's operating knowledge reaches the agent without a person retyping it. The
starter ships three:

| Skill | What it absorbs |
|---|---|
| `build-loop` | The procedure in this document. Invoked implicitly by `/spec` and `/build` |
| `operate-app` | How to boot this project and drive it, and what evidence to produce |
| `garbage-collect` | How to turn a repeated correction into a check |

**Deliberately few, and deliberately deep.** The temptation is to add a skill per task; the better
investment is making these three better, because the local development setup changes often and a skill
is where that churn should be hidden. Done properly, the tooling underneath can be replaced without
anybody noticing — which is the sign the abstraction is in the right place.

Add a fourth only when there is a capability the agent genuinely lacks, not a task you could describe
in the ticket.

### One habit that makes everything else cheaper

**Make things the same.** One way to do a thing, one canonical helper, one shape for a module, one
programming language where you have the choice. Not for tidiness — for context. An agent working in a
codebase where every corner looks alike carries transferable understanding from one file to the next,
and the tokens it needs to produce are easier to predict. A codebase with four ways to make an HTTP
call spends the model's attention on deciding which one you meant.

The corollary is that large mechanical change is now cheap enough that a half-finished migration has no
excuse. If two patterns coexist because nobody finished, finish it.
