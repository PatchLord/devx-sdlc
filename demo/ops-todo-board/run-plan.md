> **The client is fictional. The engineering is not.** Marigold Living, Dev Rawat, Priya Menon, Anjali Sharma
> and Karan Iyer are invented. Everything downstream of the SOW — the repository, the gates, the CI, the code,
> the tests — is real work under real checks. No artefact in the engineering half is simulated: a test either
> runs or it does not.

# The run plan

This document decides how the Ops To-Do Board gets built, and it exists because the obvious answer — start at
ticket one and work forwards — destroys the most valuable output of the whole exercise.

## What starting requires, and what it does not

Three things are still unproven and only one person can supply them. It is worth being exact about what each
one actually blocks, because "we are blocked" has been doing more work than it deserves:

| Missing | Blocks | Does not block |
|---|---|---|
| `PERIMETER_TOKEN` (fine-grained, `Administration: read`) | the `perimeter` check | every other gate |
| `ANTHROPIC_API_KEY` | the `review` check | every other gate |
| A second reviewer | proving code-owner review can be **passed** | proving it is enforced — already demonstrated |

None of them blocks stage 0 or stage 1 below. That is the reason to start now rather than wait: **the first two
stages of this run need nothing that does not already exist.**

## Three stages, and why the order is forced

The exhibit this run exists to produce is the same feature built twice — same agent, same model, only the
process removed. [First run](../../docs/19-first-run.md) says to run the ungoverned control **first**, and
names the reason: build the governed version first and you are writing the control already knowing where the
defects are, which is laundered evidence in a different costume.

Executing that instruction surfaced a problem in it. The control ticket is **A-29** — *a person can add a task
in their own words, from the board, and it appears* — chosen because it is where our own pilot failed: nine
write hooks and zero buttons. But A-29 sits at ticket three. It needs a schema, an authorisation model and a
board that renders. Run it cold on an empty repository and the agent builds an entire application, and the two
branches are no longer the same ticket.

So the order is:

### Stage 0 — the shared baseline

Tickets one and two: schema, teams, authorisation, and the read side of the store signals. Both later branches
are cut from the same commit, so anything in the baseline is common ground and cannot favour either side.

### Stage 1 — the control, blind

From baseline commit `B`, a session receives **the plain ask and nothing else**:

> The ops team needs to be able to add their own tasks to the board.

That wording is the whole validity of the experiment. A-29's real text names the artefact that proves it — *a
browser test that clicks the button, types into the field, submits, and finds the task on the board under the
author's name; the screen, not the endpoint.* Hand the control that sentence and it passes trivially, because
the criterion **is** the gate. What a normal ticket looks like is one line from a person who wants the feature,
and that is what the control gets.

No `CLAUDE.md`, no skills, no spec, no criteria, no gate output. The branch is preserved and **never merged.**

### Stage 2 — the governed run

From the same commit `B`, A-29 in full: spec first and alone in its commit, board entry second, implementation
third, every criterion carrying the artefact that proves it, every check running.

## A correction to the rule as written

The rule says *before the process exists in that repository*. Executing it shows the phrasing is wrong in a way
that matters, and the doc has been amended.

What the control must lack is **the criteria** — knowledge of where the defects are. What it must **not** lack
is infrastructure. If the baseline already carries a browser-test harness, the control inherits it, and that
biases the experiment against us. Deliberately. A control that had no way to write a browser test and therefore
did not write one has demonstrated nothing about process; a control that had the harness sitting there, ready,
and still shipped no button is a far stronger exhibit than one we handicapped.

**Blind to the criteria, not deprived of the tools.**

## The tickets

| # | Ticket | What it produces that answers a question somebody will ask |
|---|---|---|
| 1 | Schema, teams, authorisation. Contracts frozen first | a class A escalation and a walked code-owner review — *can the agent touch dangerous things?* |
| 2 | Read the store signals | timeout and retry lints firing on a live dependency, and a committed fixture — *does it handle production concerns?* |
| 3 | **A-29, the write path** | the control/governed pair, and a screenshot against a criterion — *how do I know it is actually done?* Let it arrive **over the ceiling** so the size gate fires and the split is on the record |
| 4 | Phase 2 — dates and timezones | a *modified* existing test, so the `gates.yml` asymmetry fires; and a non-empty divergence field, because the Phase 1 design said nothing about timezones |
| 5 | Phase 2 — notifications | a class A irreversible action, the stub decision, and send-once idempotency — *what stops it doing something it cannot undo?* |

Tickets 1 and 2 can start immediately. Ticket 2's *live* half needs a Shopify dev store; its fixture half does
not, and the fixture is what the gate reads.

## Predictions, registered before the control runs

Written down now so the narrative cannot be fitted to the result afterwards. Each will be marked hit or missed
against what actually happens.

| | Prediction | Confidence |
|---|---|---|
| **1** | The control ships A-29 with no browser test | high |
| **2** | **The control's add-task path works correctly when a person clicks it by hand** | high |
| **3** | The governed run's first branch is rejected by `spec` — wrong branch name, or the spec not the first commit | high |
| **4** | At least one acceptance criterion turns out to be unprovable and has to be escalated as class B | medium |
| **5** | The size gate fires on ticket 3 and the change is split | medium |

Prediction 2 is the one that costs us something, and it is registered deliberately. The argument this run makes
is **not** that the ungoverned version is bad — it usually is not:

> The ungoverned version might be perfectly fine. **You have no way to know which one you got.**

If the control comes out clean, that is the claim being demonstrated rather than a result to explain away.

## The rules, as commitments

- **Do not coach the implementing agent.** It gets the spec and the standard. If someone tells it "add a
  timeout here", the run demonstrates that person's prompting rather than the process.
- **Nothing gets tidied before it is shown.** The most valuable output is what got blocked. A run in which
  nothing was blocked demonstrates a system that does not block.
- **Count the shortcuts.** Every `--admin` merge, every self-approval, every skipped check, recorded as it
  happens. The proof repository ran up two in eleven pull requests; a shortcut count that only ever reads zero
  is a number nobody should believe.
- **One person is playing several roles**, and that must be stated rather than discovered. Where a self-approval
  stands in for a second reviewer, the gate was fictional for that pull request.

## What would make this run a failure

Registered on the same principle as the predictions.

- **Every check green on every pull request.** That is the wall-of-red problem inverted, and it means the gates
  are not reading the work.
- **The control and the governed branch are indistinguishable and we cannot say why that is fine.** The framing
  above has to hold under a hostile question, not just in this document.
- **The board goes stale.** `scripts/board.mjs --check` regenerates the HTML and fails if it drifts, so this one
  is a fact rather than a matter of diligence — but the entries themselves can still rot into a graveyard if
  they lack terminal states.
- **Five tickets get described as proving the process works.** They show the mechanisms fire. Whether the
  process survives a quarter is [E2](../../research/experiments.md), and it takes a real project and real time.
