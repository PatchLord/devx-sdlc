# The first run: choosing it, and what will go wrong

A pre-mortem. [The runbook](12-runbook.md) says what to do and in what order; this says what will bite while
you do it, and how to pick the project so that the process is actually exercised rather than performed.

Most entries here are not error messages. [Troubleshooting](13-troubleshooting.md) covers the failures that
announce themselves. **The ones below mostly look like success**, which is why they need writing down before
anyone is under time pressure.

## Part 1 — choosing the vehicle

The instinct is a to-do app. It is not a bad instinct, and it beats a fresh copy of a client project. But
judge candidates against what the first run has to exercise, because a vehicle that fails one of these turns
a stage into ceremony:

| | What it has to do | Why |
|---|---|---|
| 1 | Be understood by everyone in the room in one sentence | Attention spent explaining the domain is attention not spent on the process |
| 2 | Contain **at least one genuinely hard design question** | Otherwise the TDD closes trivially, and every escalation is a question someone already knew the answer to |
| 3 | Touch the protected set naturally — auth, personal data, money, migrations | Class A escalation and code-owner review are otherwise never walked |
| 4 | Have a Phase 2 nobody planned for | Where the divergence field, existing-test changes and Pre-existing findings come from |
| 5 | Have **a screen a person types into** | The pilot's admin panel had nine write hooks and zero buttons. Read-only work hides the failure |
| 6 | Look like the work you actually sell | A demo that does not resemble client work does not transfer to client work |
| 7 | Be finishable | Five tickets, not fifty |

Three candidates, scored honestly:

| | Generic to-do | Ops task board for a merchant | Returns / RMA portal | Order tracking |
|---|---|---|---|---|
| Understood instantly | yes | yes | yes | yes |
| A genuinely hard question | only with shared lists | authorisation across teams | permissions, money, return windows | none |
| Touches the protected set | auth, personal data | auth, personal data, migrations | **+ money, refunds** | barely |
| A real external dependency | no | **yes — the store's API** | yes | yes |
| An irreversible action | no | **yes — reminder emails** | yes — refunds | no |
| Natural Phase 2 | due dates | due dates, timezones, reminders | exchanges, store credit | — |
| Somebody types into it | yes | yes | yes, twice | **no — read-only** |
| Looks like our work | **no** | **yes** | **yes** | yes |
| Finishable | yes | **yes** | one size bigger | yes |

**Order tracking fails on the criterion that killed the pilot** — it is read-only, and read-only work is
exactly how a process passes while proving nothing.

**A generic to-do app fails on one criterion only, and it is repairable.** The to-do part was never the
problem; *looks like the work you sell* was. An **ops task board for a merchant's team** — tasks raised from
real store signals like low stock or an order past its fulfilment SLA, assigned across a team, completed by a
person — is still understood in one sentence, and it is the kind of internal tool we actually build. That one
reframe buys an external dependency the agent must handle (timeouts, retries, a committed fixture), a real
authorisation question (who may see and complete whose team's tasks), and in Phase 2 an irreversible action:
**sending a reminder email is on the class A list verbatim**, which forces the stub decision to be escalated
rather than assumed, and makes send-once idempotency something you can demonstrate rather than describe.

What it does not exercise is *money is integers in the smallest unit*. That is an acceptable loss — the point
is not to fire every tier-1 line, it is that the standard visibly bites somewhere, and authorisation is the
line the standard itself calls its highest-value one.

**A returns portal is the better vehicle.** Everybody understands returns; it is unmistakably commerce work;
and it is loaded with questions no code can answer. Partial returns. Refund to the original payment method
or store credit. Who may see whose order. What happens when the return window closed yesterday in the
customer's timezone but not in ours. It makes two tier-1 lines from
[the standard](08-templates.md) real rather than theoretical: *money is integers in the smallest unit* and
*anything retryable is idempotent or carries an idempotency key*.

It also produces the single best escalation available: **a refund is irreversible, so calling a real payment
API in a demo is a class A hard stop.** The correct answer is to stub it, and watching that decision get
escalated rather than assumed is worth more than any green check.

**To-do with shared lists stays a legitimate fallback** if the first run has to be smaller. Shared lists are
not decoration — they force authorisation rather than authentication, which the standard calls its
highest-value line. A plain single-user to-do app fails criterion 2 outright, and then the whole front half
of the process is theatre.

### Choose the tickets backwards from the questions

Mechanism coverage is the floor. If the run is also a demonstration, go one step further and pick each ticket
for **the artefact it will produce that answers a question somebody is going to ask.** Five tickets, worked
out backwards:

| # | The ticket | What it produces that answers a question |
|---|---|---|
| 1 | Schema, teams, authorisation. Contracts frozen first | A class A escalation and a walked code-owner review — *can the agent touch dangerous things?* |
| 2 | Read signals from the real external system | Timeout and retry lints firing on a live dependency, and a committed fixture — *does it handle production concerns?* |
| 3 | The write path a person uses | A screenshot against a criterion — *how do I know it is actually done?* Let this one arrive **over the ceiling** so the size gate fires and the split is on the record |
| 4 | Phase 2: dates and timezones | A modified existing test, so the gate asymmetry fires; and a genuinely non-empty divergence field, because the Phase 1 design said nothing about timezones |
| 5 | Phase 2: notifications | A class A irreversible action, the stub decision, and send-once idempotency — *what stops it doing something it cannot undo?* |

**Run the ungoverned control on the write-path ticket**, not on the easiest one. That is where our own pilot
failed: nine write hooks and zero buttons, the write side present at every layer except the one a human
touches, because the gate it was given could only see reads. If an ungoverned agent reproduces that on the
same ticket where the governed branch had to attach a screenshot of a person completing the action, the most
persuasive exhibit in the room is the organisation's own history repeating next to the version that caught it.

## Part 2 — what will go wrong, in the order you will meet it

### Setting up the host

**Every check sits pending forever.** The workflows say `runs-on: arm64`, a self-hosted label. If those
runners are not available to the repository, nothing runs, nothing reports, and merge stays blocked. It
fails safe but it looks broken. Check before anything else.

**Branch protection may not be available at all.** On a private repository, protection and rulesets depend
on the plan. Discovering this after writing the SOW is worse than discovering it in the first ten minutes.

**`CODEOWNERS` naming a team that does not exist** silently blocks every merge, because code-owner review
can never be satisfied. The error message is not helpful. Use a slug that resolves.

**Required contexts cannot be named before they have run once.** This is a genuine chicken-and-egg and
[host and pipeline](09-host-and-pipeline.md) opens with the fix: one throwaway pull request first.

**`review` fails rather than skips when its key is missing** — deliberately, because a review job that
quietly does nothing shows a green check for work nobody read. Expect it, and either add the key or remove
the job and its required context together.

**`PERIMETER_TOKEN` needs a fine-grained token with `Administration: read`.** Some organisations block
fine-grained tokens by policy. Without it, `perimeter` fails — correctly, because a perimeter check that
skips when unconfigured is the exact failure it exists to catch.

### The front half — SOW, PRD, TDD, contracts

**The client answers too fast.** Whoever plays the client will answer in thirty seconds, and that hides the
thing most likely to bind real delivery: client decision latency. [Open question C5](../research/open-questions.md)
is about exactly this. Deliberately hold one answer for a day and watch what the team does — that is the
most informative hour of the whole run.

**The TDD gets approved unread.** An agent drafts a plausible document, a person skims it, and now
instructions nobody agreed to carry authority. The defence is in [the artefacts](17-artefacts.md): the open
questions, the risks, and what we are deliberately not doing **cannot be agent-drafted.** If those three
sections came from the agent, the review did not happen.

**An acceptance criterion that cannot be proven.** "The list should feel fast" will appear. It is a class B
escalation, and someone has to notice — an unprovable criterion silently becomes an unverified one, and the
evidence column gets filled with prose.

**Contracts frozen on the wrong shape.** The permission model is the risk: freeze it wrong and every ticket
inherits it. Freeze it late and the tickets serialise. There is no safe option, only a visible one — put the
reasoning in a decision record so the next person knows it was a choice.

**The client changes scope mid-run.** They will, because that is what clients do. Good: it exercises the
path where a PRD change goes through the CSM rather than into a spec. Do not shortcut it because it is a
demo.

### Tickets and specs

**Branch names will be wrong.** `spec.yml` requires `^[A-Z][A-Z0-9]+-[0-9]+`, and an agent left alone will
create `feature/returns-form`. The check rejects it before looking for a file, which is correct and will
still surprise everyone the first time.

**The agent will write code before committing the spec.** The spec must be the branch's first commit and an
ancestor of every implementation commit. Any session that starts editing first produces a branch that cannot
be made legal without a rebase. Expect this on ticket one.

**A merge commit inside a branch breaks two checks at once.** `gates` and `spec` both reason with
`git rev-list`, so linear history is a precondition rather than a preference. Squash merges are fine; a merge
commit mid-branch means both checks reason about an order nothing was tested in.

**A ticket will be too big.** The size gate fires, and the right answer is to split — which costs demo time
and is the correct thing to do anyway. Budget for it happening at least once.

**In Phase 1, the spec's "patterns already here" section is thin**, because there are barely any patterns
yet. That is honest and it is also why Phase 2 matters.

### Implementation

**`verify` may pass while checking nothing.** It is stack-specific and has to be wired during Setup. An
unwired `verify` is the most dangerous state in this whole document: a required green check that proves
nothing, on every pull request. If it cannot be wired in time, **remove it from the required contexts** —
the documents' own rule is to cut a gate rather than fake one.

**Changed-line coverage on a repository with no tests.** The first file has no baseline, and a ratio over
zero changed lines is not a number. Confirm the script's behaviour on an empty case before relying on the
threshold.

**Evidence needs project-specific skills that do not exist yet.** `operate-app` is generic; it cannot boot
*your* app, seed *your* data, or drive *your* forms. Until someone writes those three, every UI criterion
resolves to prose — and prose in the evidence column is the failure the column exists to prevent.

**Screenshots need a running app**, which means captured locally into `.evidence/` and committed, not
produced in CI. Decide that before the first UI criterion, not during it.

**A stub with a real credential in it.** Fixtures for a payment provider are exactly where a live token gets
pasted. `scan-secrets.mjs` should catch it; verify that it does rather than assuming.

**An agent will route around a wrong gate instead of reporting it.** Class D is the most under-reported class
precisely because working around a check is easier than arguing with one. If nothing in the run produced a
class D escalation, that is a finding about the run, not a clean bill of health.

### Review and release

**The dismissal convention will be forgotten.** A finding dismissed without the `Dismissed:` prefix is
invisible to `collect-week.mjs`, and the dismissal rate — one of the six numbers, and the thing that decides
whether the review agent keeps its required slot — becomes uncomputable. Unrecoverable after the fact.

**Someone will approve quickly to keep the demo moving.** This is the measured failure, not a hypothetical:
Anthropic found only **16%** of pull requests getting substantive feedback under velocity pressure. A demo
creates exactly that pressure, and an approval given to keep things moving is the demo lying about itself.

**`REVIEW.md`'s project-specific section will be empty**, so the reviewer works from the generic standard and
finds generic things.

**The release checklist's third column asks for a restore drill.** On a demo database, either do it and
record the time, or write plainly that it was skipped. Do not leave the cell looking satisfied.

**`deploy.yml` and `promote.yml` need environments and somewhere to push an artefact.** If the first run has
neither, those two workflows go unexercised — which is fine, as long as nobody claims build-once-promote is
proven.

## Part 3 — the failures that look like success

The dangerous class. Everything above announces itself; these do not.

**Every ticket chosen from the easy pile.** Five comfortable tickets produce five green runs and teach
nothing. Choose for mechanism coverage — see [the runbook](12-runbook.md).

**No escalation was logged.** An empty `log/events/` after five tickets does not mean nothing was asked. It
means the record was skipped, and the weekly hour has nothing to converge on.

**Nothing was ever blocked.** If no gate went red for a real cause, the gates were not tested. Any check that
has never gone red is indistinguishable from one that cannot.

**Cost went unmeasured.** [C1](../research/open-questions.md) is a zero-mention hole, and "what does a ticket
cost in agent spend" is the first question anyone commercially minded asks. Capture it per ticket as you go;
it cannot be reconstructed.

**One person played every role.** Then specs, criteria changes and pull requests were all self-approved, and
the central gate was fictional for the entire run. Say so if it happened.

**The run was tidied before being shown.** The most valuable output is what got blocked. A demonstration in
which nothing was blocked is a demonstration of a system that does not block.

## Part 4 — if the first run is also a demonstration

Showing it to an executive changes the design of the run, and two of the changes are non-obvious.

**Run the ungoverned control FIRST, cold, before the process exists in that repository.** The most
persuasive exhibit is the same feature built twice — same agent, same model, only the process removed — but
the comparison is only honest if the control ran without knowing where the defects would be. Build the
governed version first and you are writing the control already knowing the answers, which is the laundered
evidence problem in a different costume.

**Do not bet the demonstration on the ungoverned version being visibly bad.** It often is not. An
ungoverned agent frequently produces good code, and if the room sees two acceptable branches the argument
collapses — unless the claim was framed correctly to begin with:

> The ungoverned version might be perfectly fine. **You have no way to know which one you got.**

The governed run is what produces the evidence that answers *which*. Framed that way the exhibit holds even
when both branches are near-identical, because what is on display is not better code — it is knowing. That
framing also removes the temptation to rehearse, which is the failure named above.

Two smaller consequences. **Walk the artefacts rather than coding live**: a live session is fragile and
proves less than a real engagement's outputs. And **state the sample size yourself** before anyone asks —
five tickets show the mechanisms work and show nothing about whether the process survives a quarter.

The questions that follow are the part worth preparing, and they are in
[outcomes](18-outcomes.md#the-questions-you-will-be-asked) — executive, developer, client and technical,
with the honest answers, including the four places where the honest answer is that we do not know yet.

## Part 5 — what to say afterwards

Whatever happened, the honest framing is fixed in advance: **five tickets show that the mechanisms work. They
do not show that the process survives a project.** That is [E2](../research/experiments.md), it takes a real
project, and no ticket count you reach in a fortnight substitutes for it.

Report the numbers with their sample size attached, name every role that was doubled up, and list what went
unexercised. [Limits](14-limits.md) is the tone to aim for.
