# When it goes wrong

A catalogue of the failures we have actually hit. Read an entry when something is stuck; read the lot once
before your first project so you recognise the shapes.

Every entry has four parts: symptom, cause, fix, and the check. The last matters most — a fix without a
check means you read the same entry again next quarter. Some entries end by naming a check we have not built.
Writing that down is honest. Writing it as though the check exists is the failure this document set is
about.

## The agent loops on a red gate

**Symptom.** The same job fails four, six, nine times. Every commit message says "fix tests". The diff grows
and nothing new is proven.

**Cause.** An agent handed a failing check treats it as a puzzle with an unlimited budget. Each retry looks
locally reasonable, and nothing tells it what it has spent. Attempt nine feels the same from the inside as
attempt one.

**Fix.** Stop the session. Diff the last green commit against the first red one. The cause is nearly always
one of three: the spec was wrong about the shape of existing code, a fixture is stale, or the check tests
something this ticket was never scoped to satisfy. All three are conversations, not code.

**The check.** [CLAUDE.md and the implement agent](07-repository.md) carry the same sentence: after two
attempts, stop and ask. Two, not three, because the second attempt is where an agent stops fixing the cause
and starts negotiating with the symptom. Stripe caps its own one-shot agent loop at "at most two" CI runs,
the same number arrived at independently. This is instruction, not enforcement: nothing counts retries and an
agent can ignore the rule. What makes the cost visible is that every attempt is a pushed commit, so a session
that looped nine times says so on the pull request.

## The spec turns out to be too thin mid-implementation

**Symptom.** The implementing agent asks a question the spec should have answered. Or it guesses, and tells
you afterwards.

**Cause.** Explore read the design document and not the code. A spec naming no file paths and no existing
patterns was written from prose about the system rather than from the system. That is why the [spec
template](08-templates.md) has a section called "What the code looks like now": it cannot be written without
opening files.

**Fix.** Revise the spec in a commit of its own and re-approve it. Do not answer in chat and carry on — the
next session will not have had that conversation. If more than one or two answers are missing, the spec is
not thin, it is wrong. Throw the branch away and re-run `/spec`.

**The check.** The second step of `spec.yml`, "A spec revised mid-flight is visible", names every commit
after the first that touched the spec file and warns that the existing approval was of the earlier text; see
[enforcement](06-enforcement.md) for the code. It warns rather than fails on purpose: revising a spec
mid-flight is legitimate, and failing the build for it would teach people to do it silently. The cost is
real — a warning can be scrolled past.

## The ticket exceeds the ceiling halfway through

**Symptom.** `size` fails: exceeds the ceiling of 400 lines / 20 files.

**Cause.** Usually the ticket was two tickets and nobody noticed at cutting time. Occasionally it is one
ticket with an unavoidable surface — a rename touching every caller, a regenerated client.

**Fix.** Split it. Land the part that stands alone, open a second ticket with its own spec for the rest. That
is the answer nine times in ten. If it genuinely cannot be split, a tech lead — not the developer, not the
agent — adds the `size-override` label and the pull request says why.

**The check.** `size.yml` measures `git diff --numstat base...head` with lockfiles, snapshots, generated
files and migration SQL excluded. It warns above 300 lines or 10 files, fails above 400 or 20, and triggers
on `labeled` so the override re-runs the job rather than needing a push. It reads the timeline API for who
applied the label and fails if that is the author: a self-applied override is a bypass in an override's
clothes. The label is a record, not an exit — overrides count as shortcuts in [the six
numbers](11-measurement.md). Honest limit: 400/20 is our judgement, not a measurement, and it should move
once we can see at what size our reviewers stop finding anything.

## A gate genuinely needs weakening

**Symptom.** A check is wrong. A lint rule fights a framework convention, or a test asserts behaviour the
client has since changed.

**Cause.** Gates are written before the code they will meet, so some will be wrong. A process that cannot
admit that produces workarounds instead of changes, and workarounds are invisible.

**Fix.** Change the gate, in its own commit, with the reason in the commit message, reviewed by a code owner.
That is the whole procedure. Weakening a gate is allowed. Hiding one inside a feature commit is not.

**The check.** `gates.yml` walks every commit in the pull request and fails any one touching both a gate path
and an implementation path. Gate paths are the workflows, `lefthook.yml`, `CODEOWNERS`, `CLAUDE.md`,
everything under `.claude/` and `docs/design/criteria/`, the test and coverage configs, the three files in
`scripts/`, and any existing test modified or deleted. Adding a new test for new code counts as
implementation — that asymmetry is what makes a legal commit ordering exist. [CODEOWNERS](07-repository.md)
puts those paths behind `@devx/tech-leads`, and `perimeter.yml` asserts the host actually requires code owner
review, because a CODEOWNERS file without `require_code_owner_reviews` on the branch has no effect.

## The review agent floods a pull request

**Symptom.** Nineteen findings, three of them real. The developer skims once, then stops reading it at all.

**Cause.** Expected behaviour of the tool class, not a misconfiguration you can tune away. Across 19,450 pull
requests measured in April 2026, agent-only reviewed pull requests merged at 45.20% against 68.37% for
human-only review, and 12 of 13 agents averaged below a 60% signal ratio. A separate three-week head-to-head
of four reviewer bots on one codebase found 93.4% of flagged locations were raised by exactly one tool, with
no finding common to all four.

**Fix.** Dismiss the wrong ones in writing, one line each, on the pull request. Do not argue with a bot in
code: changing correct code to quiet a false positive is the worst outcome available. If the noise persists,
drop `review` from `REQUIRED_CHECKS` in `perimeter.yml` and let it run advisory — `review.yml`'s own failure
message says to do exactly that rather than let the job silently skip.

**The check.** Dismissal rate is number three of the six numbers, and the only thing deciding whether this
check keeps the right to block a merge. Our threshold: more than half the findings dismissed across a
fortnight and it comes off the required list — a judgement, not a measurement. Uber's reviewer earned its
place by benchmarking comment address rate, 65% against 51% for human comments, which is the shape of
evidence we lack. Requiring conversation resolution stops the opposite failure: a finding neither fixed nor
dismissed, merged past.

## CI is green but the feature does not work

**Symptom.** Every check passes. You open it in dev and the button is not there.

**Cause.** The agent builds to the shape of the check. In our pilot the admin panel shipped nine write hooks
and zero buttons, zero forms, zero submit handlers — the write side existed at every layer except the one a
human touches. Its own build report said why: it had chosen a render verification as that surface's gate, a
gate that could only see reads, and only reads got built. A weak gate does not give you the same product less
verified. It gives you a different, smaller product.

**Fix.** Do not patch the button in. Fix the criterion that was supposed to cover it, in
`docs/design/criteria/` where a code owner approves it, then the code. Patch the code alone and the same
class of hole arrives on the next screen, because what shaped the product has not changed.

**The check.** Three, none automatic, which is the honest position. The criterion names an artefact a person
could produce: a screenshot of the interaction, a real request and its response. The review agent's second
job is to ask whether the evidence proves the criterion or restates it. A person judges the feature running
in dev, not the diff. One hole worth naming: `verify.yml` emits a warning and exits 0 when
`coverage/lcov.info` is absent, so a test step that does not write lcov leaves the changed-line coverage gate
at `--min 80` non-existent and the pull request green. See [stack wiring](10-stack-wiring.md) for emitting
lcov.

## An agent used `--no-verify`

**Symptom.** You find it in `git reflog`, or in a commit carrying formatting the pre-commit hook rejects.

**Cause.** Hooks are hints. `--no-verify` walks past them, `git stash` hides staged state, and
`permissions.deny` on `.claude/hooks/**` is not enforced, so an agent can edit its own enforcement hook. Both
were reported upstream and closed "not planned". One field report with reflog evidence has six consecutive
commits taking a suite from 104 passing to 63 failing this way, skipping gitleaks, lint-staged, Jest and
Playwright.

**Fix.** Nothing needs unwinding, because nothing merged on the hook. `verify.yml` runs `bun run verify` on
the host and `scripts/verify.mjs` runs the same six gates the hook would have — format, lint, types, tests,
coverage, build — failing rather than skipping when one is not wired in `package.json`. What needs handling
is the session: say the shortcut was taken, and count it.

**The check.** The perimeter, not the hook. `size`, `gates`, `spec`, `verify` and `review` are required
status checks with `strict` on, and force pushes and deletions are off; see [host and
pipeline](09-host-and-pipeline.md). `gates.yml` says plainly that a commit object holds no reliable marker
for a bypass, so its second step checks what one leaves behind: `continue-on-error: true` or `if: false`
added to a workflow, a step ending in `|| true` that swallows its whole command, and added skip markers such
as `.skip(`, `xit(`, `@pytest.mark.skip` or `t.Skip(`. Shortcuts are number four of the six, and an uncounted
shortcut is invisible at exactly the moment it matters.

## A migration collides with another branch

**Symptom.** Two branches each add a migration. The second merges and the schema is in an order neither was
tested in, or the runner refuses to start.

**Cause.** Migration files sort by name. Two branches will not agree on that order, and each was tested
against a database the other never touched.

**Fix.** One migration in flight at a time. The second branch rebases onto main after the first merges and
re-runs its migration against the resulting schema.

**The check.** `strict` forces a branch up to date with main before it can merge, so the second migration is
re-tested against the first rather than merged past it. CODEOWNERS puts `/migrations/` and
`/prisma/migrations/` behind a tech lead. Honest limit: `migrate.yml`, the job that would apply migrations
both from scratch and on top of main's schema, is on the to-build list. Until it exists, "one in flight" is a
convention two people can forget on the same afternoon.

## The tech lead's queue collapses into skimming

**Symptom.** Feature judgements take four minutes. Gate diffs get a glance. Nothing is refused.

**Cause.** On a small team one person holds the design document, every feature judgement, the daily gate
diffs, protected-path review and Release Check. A second name against each gate on a page does not put a
second head on the queue.

**Fix.** Move work, not standards. The second name on each human gate, decided at Setup — see [before the
build](02-before-build.md) — takes feature judgement for a named set of features. Cut tickets in flight
before cutting the depth of the check: a skim of ten is worth less than a real look at four.

**The check.** Number five, defects per merged ticket split by who found them. A skim shows up as defects
drifting from feature review towards QA and the client at a flat total. What it cannot see is a skim that
produces no defect anybody finds, and the wait-time number will not help, because a lead who is skimming
looks fast rather than slow. This is the failure we are least instrumented for — a standing weakness, not a
gap we are about to close.

## A client changes scope mid-phase

**Symptom.** A request arrives in a demo or a Slack thread and someone starts building it.

**Cause.** It looks small, and absorbing it into the ticket in flight looks faster than routing it.

**Fix.** The CSM first, because it changes what the client accepts and possibly what they pay. Then
`docs/design/` for the phase, and `docs/design/criteria/` if it changes acceptance. Then a ticket. Never a
paragraph added to a spec already being implemented — the ticket then satisfies criteria nobody approved,
and the phase boundary the estimate rested on is gone.

**The check.** `docs/design/criteria/*` is both a gate path in `gates.yml` and a CODEOWNERS path, so a
criteria edit cannot ride inside an implementation commit and cannot be approved by its author. An agent may
propose a criterion; only a person approves one. `spec.yml` warns when the spec moved after implementation
began, which is the trace scope creep leaves.

## The design document and the code have diverged

**Symptom.** Specs keep reporting "no divergence", and the same question gets asked and answered on three
tickets in a row.

**Cause.** The correction landed in the ticket's spec and not in the document. Specs are per ticket, so a
correction living in one is invisible to the next agent, which re-derives it or gets it wrong.

**Fix.** The correction lands in `docs/design/`, in the same pull request, and the spec points at it. Where
the document now describes a different system rather than a stale one, stop cutting tickets from it and
rewrite the section with the tech lead first.

**The check.** Weak, and worth saying so. The [spec template](08-templates.md) has a mandatory section,
"Where the design document and the code disagree", and CLAUDE.md tells the agent a divergence is the most
valuable thing it can report. Both are prompts, not gates. The check we have not built: fail a pull request
whose spec fills that section and whose diff never touches `docs/design/`.

## Someone quotes a check we have not built

**Symptom.** A row from the enforcement table appears in a client conversation, a README or an internal
answer without its status. "Main is protected, a red pull request cannot merge."

**Cause.** Our pilot's context file contained that exact sentence while there was no remote and CI had run
zero times. Nobody noticed, including someone checking the build every five minutes. From inside the
repository, a written check and a running check look identical.

**Fix.** Correct the claim the same day, in the document that made it. If a client heard it, the CSM tells
them. Read the status column literally: *written*, *proven* and *to build* are three different things, and
only *proven* means the check ran on a host and failed something it was meant to fail. [What this does not
do](14-limits.md) exists for the same reason.

**The check.** `perimeter.yml`, the only check that tells you the truth about the others. It asks the host
API what main enforces and compares that to `REQUIRED_CHECKS="size gates spec verify review"` and
`REQUIRED_APPROVALS=1`, both written in the workflow file rather than read from a config an agent can edit.
It runs `0 7 * * 1` — Monday morning, so a weekend change is found before the week's work lands on it —
and on every push to main touching the workflows, CODEOWNERS or CLAUDE.md. A missing `PERIMETER_TOKEN` fails
the job rather than skipping it, because a perimeter check that skips when unconfigured is the failure it
exists to catch.

## The escalation rule

One ladder. Each rung has a trigger, a person and a deadline, because an escalation with no deadline is a
thing that gets mentioned eventually.

| Trigger | Goes to | When |
|---|---|---|
| Two failed attempts at the same check | the developer | in the session, before a third attempt |
| The spec cannot answer a question | the developer | before guessing |
| A gate needs weakening, or a `size-override` | the tech lead | same day, as its own commit |
| Anything that changes what the client accepts | the CSM, then the design document | before the work starts |
| A feature fails review or QA twice | the tech lead and the CSM | before a third round of patches |
| A secret found, or production behaving oddly | revoke or rotate first, ticket second | same day |

The second rung from the bottom is the one people skip. Three rounds of patches on one feature is not a code
problem — the design document is wrong about the feature, and patching will not reach that. Every human gate
has a second name for a reason: one name on all of them means a fortnight of leave stops promotion to uat.

## The convergence rule

**Every defect a person found leaves a check behind.** Not a lesson, not a note in a retro. A check.

So every fix has two halves: correct the code, and add the thing that would have caught it — a test, a
criterion in `docs/design/criteria/`, a fixture, a rule in CLAUDE.md, a line in the release checklist. If QA
found it, then either no criterion covered that behaviour or one claimed to and its evidence restated the
criterion instead of proving it. Neither is fixed by the code change alone. The ticket records who found it,
because that split is what number five counts.

Where a defect genuinely cannot leave a check behind — somebody looked at a screen and saw it was ugly —
write down what cannot be seen, and where. Worse than a check, far better than a silent gap.

This is what makes the process falsifiable. If a second round of QA on a feature finds much less than the
first, the checks are working. If a third finds as much as the first, the problem is not the developer and
not the agent: it is the design document, and no check bolted onto the code fixes a document that describes
the wrong system.
