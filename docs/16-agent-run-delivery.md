# Agent-run delivery: the system works, humans answer

The target operating model for the delivery team. It changes one thing about how we work today, and that
one change has consequences throughout — so this document states the change, what has to be true for it
to be safe, and what does not exist yet.

Read this if you are on the delivery team. Solutioning, the SOW and the handover are unchanged and live
in [before the build](02-before-build.md); this is about what happens after a ticket exists.

## Why "work the way the frontier labs work" is not a target

It is worth settling this before the design, because it is the most natural way to frame the goal and it
does not survive contact with what the labs actually do.

**They disagree with each other on the single most important question.** OpenAI's Frontier team shipped
over a million lines in five months with **no human review before merge** — that is the stated headline
of their account. Anthropic shipped Code Review in March 2026 which **will not approve a pull request by
design**, dispatching parallel reviewers as a thorough first pass while a human retains final authority
on every merge. Same industry, same year, opposite answers on whether a person sees the code.

So the useful question is not *how do the labs work*. It is **which lab's situation resembles ours**, and
the answer is not ambiguous:

| | OpenAI Frontier team | Anthropic's engineers | devx |
|---|---|---|---|
| Who the software is for | an internal beta | external customers | clients, under contract |
| Consequence of shipping a defect | a colleague complains | a customer is affected | a client's revenue, and our reputation |
| Codebase | one, greenfield, five months old | many, long-lived | many, mostly someone else's |
| Commercial frame | none | product | fixed-price SOW |
| Human review before merge | none | **required, by design** | required |

We are in the third column, and on the question that matters we are in the same position as the second.
Copying the first would mean adopting the review posture of a team with no client and no contract.

**What does transfer is the mechanism, not the posture.** Skills that let an agent operate the project,
failure messages written as prompts, garbage collection, structural enforcement, evidence per criterion —
all of that is sound regardless of who the software is for. "Nobody reads the code before it merges" is
not a mechanism, it is a risk position, and it is theirs to take rather than ours.


## What changes

Today a person drives. They run `/spec`, answer its questions, approve the spec, run `/build`, look at
the evidence, merge, and then remember to start the next ticket. The agent executes steps; the human is
the scheduler.

That is backwards. Scheduling is the part a machine should do.

**In the target model the system drives and the human answers.** Something takes a ready ticket, runs
the whole loop, and raises a request whenever it reaches a point where a person is genuinely required.
The developer's job becomes answering those requests and judging finished work.

```
  TODAY                                   TARGET

  human ──▶ /spec                         ticket ready
  human ──▶ answers                             │
  human ──▶ approves                            ▼
  human ──▶ /build                        ┌──────────────┐        ┌───────────┐
  human ──▶ checks evidence               │ the runner   │───────▶│  human    │
  human ──▶ merges                        │ picks it up  │◀───────│  answers  │
  human ──▶ starts the next one           │ runs it      │  when  └───────────┘
                                          │ escalates    │  it needs a decision,
  the human is the scheduler              └──────┬───────┘  not on a schedule
                                                 ▼
                                          gates decide the merge
```

**This is not "remove the human".** Every gate stays exactly where it is — the spec is still approved by
a person before code exists, protected paths still need a second pair of eyes, the feature is still
judged running. What goes away is a person being the thing that remembers what happens next.

## The premise that makes it work, and the one that would break it

**Asking a human is free. Asking the same question twice is a bug.**

That sentence is the whole design. Take it in two halves, because the first half is what you asked for
and the second half is what stops it degrading.

**Asking is free — for the agent.** There is no budget on escalations and no virtue in a low count. An
agent that guesses to avoid interrupting you has done the worst possible thing: it has converted a
two-minute question into a day of wrong work and a review that has to catch it. So the instruction is not
"ask if you are unsure" — that leaves the decision to the agent, and the agent's confidence is exactly
what is unreliable. The instruction is: **if the situation falls into one of the classes below, stop and
ask, regardless of how confident you feel.**

**It is not free for the human, and pretending otherwise is how this fails.** Anthropic measured the
consequence inside their own engineering org before building anything to fix it: **only 16% of pull
requests received substantive feedback, because engineers were skimming rather than reviewing in order to
keep velocity.** That is the same failure as our 300-line ceiling, in a different place. A person
answering thirty requests a day is answering the last ten badly, and a badly answered escalation is worse
than none because it carries authority.

So volume tolerance is not enough on its own. Two things ration human attention without discouraging the
agent from asking:

**Grade every request.** Borrowing the shape Anthropic settled on for review findings: **Blocking** —
work stops until answered. **Worth knowing** — answer when you get to it, the agent proceeded on a stated
assumption. **Pre-existing** — this was already true before the ticket, logged, not this ticket's problem.
Only Blocking interrupts. The other two accumulate and get read in the weekly hour.

**Route by class, not by project.** If every request queues to the developer holding the ticket, you have
rebuilt the bottleneck with extra steps. Class A commercial questions go to whoever owns the SOW.
Criteria changes go to a code owner. Class C taste questions go to the tech lead. Class D — the system is
wrong — goes to whoever owns the gate. The developer answers B and E, which is the majority and the part
they are best placed to answer.

**Asking twice is a bug.** If the same question arrives on three tickets, the answer was missing from
somewhere durable — the design document, a skill, a lint, the context file. Three conversations is the
symptom; a missing piece of written context is the cause. So every escalation is logged, and the weekly
garbage-collection hour reads the log and asks which of last week's questions should never have needed
asking.

Concretely: the agent writes one file into `log/events/` when it escalates, `scripts/collect-week.mjs`
pulls the week's findings, dismissals and spec questions off the host, and the hour walks whatever is
still `open`. The classes and the record are in the `escalate` skill; the schema, and why this is
deliberately not a learnings document, are in [the documents](17-artefacts.md). Nothing there depends on
anyone remembering to write it down except the defects — which is the point, because a process that
depends on remembering stops in the first busy week.

That is what makes the volume of escalations acceptable. It is not that we tolerate interruptions
forever; it is that each *class* of interruption gets eliminated once while each *instance* is welcome.
The count should fall over a project's life because the codebase and its documents get more legible,
never because anyone was discouraged from asking.

## When an agent must call a human

Six classes. This list is the contract: an agent is not exercising judgement about whether to escalate,
it is matching a situation against these. Two properties matter — it is **auditable** (you can ask
whether an escalation belonged to a class) and it is **falsifiable** (you can ask whether something
that should have escalated did not).

### A — Authority. The agent does not have the standing to decide.

Hard stop. Nothing proceeds.

- Anything that changes what the client accepts: an acceptance criterion, a scope boundary
- Anything with commercial consequence: timeline, cost, what is in or out of a phase
- Any change on the protected set: payments, personal data, auth, migrations, CI or hook config,
  existing tests, coverage thresholds, `CODEOWNERS`, context files
- Anything irreversible: a production write, a data migration, sending email or notifications,
  publishing to a store, deleting anything a person did not ask to be deleted
- Spending past the ticket's token budget

### B — Ambiguity that changes the work.

Ask, then pick up a different ticket while you wait.

- The design document and the code disagree. This is the most valuable escalation there is, because it
  means the document has gone stale and every later ticket would rediscover it
- A criterion cannot be proven as written — there is no artefact that would settle it
- The spec does not answer something you must decide in order to proceed
- Two patterns already in the codebase both apply and they imply different designs

### C — Judgement that cannot be encoded.

- Does this look right. Does it feel right to use
- Would this client accept this, given what we know about them
- Is this the right trade-off here

No check will ever settle these, which is why they are a class rather than a gap to be closed.

### D — The system is wrong, not the code.

Hard stop, and the most under-reported class.

- A check fails and you believe the check is incorrect
- A gate blocks something that should be allowed
- Two rules cannot both be satisfied

An agent that quietly works around a wrong gate has taught us nothing and left the gate wrong. Say so.

### E — Novel territory.

- Work with no precedent in this codebase and none in the design document
- Anything graded *genuinely novel* — see [depth](05-depth.md). Models are least reliable where the
  training data is thinnest, and least likely to signal it

### F — Repeated failure.

- A gate has gone red twice on the same cause

Two attempts, then stop. Looping on a red check burns budget and produces no evidence.

## What a good request looks like

An escalation that a person cannot answer in two minutes has failed. The format:

```markdown
**Ticket** PULSE-142   **Class** B — ambiguity that changes the work
**Blocked on** one decision

The design document says a guest checkout keeps the cart for 30 days. `cart.service.ts:88` expires it
after 7, and has since the first commit. Both are defensible and they produce different work.

- If 30 days is right: the change is a config value and one migration for existing rows.
- If 7 days is right: the design document is wrong, and criterion CO-7 needs rewording, which is a
  criteria change and therefore yours.

**Not blocked:** I have finished CO-1 through CO-4 and pushed them. This is the last item.
**My read, if it helps:** 7 days, because it predates the document and nobody has complained.
```

Four things make it answerable: the class, the specific decision, the consequence of each answer, and
what is *not* blocked. The agent's own read comes last and is optional — useful for speed, dangerous if
it becomes the thing you approve without reading.

## The runner

What replaces the person who remembers what happens next.

**Trigger.** A ticket moving to *ready* in the tracker. Not a schedule — schedules run work that is not
ready and skip work that is.

**Before it starts a ticket:**

| Precondition | Why |
|---|---|
| The ticket has acceptance criteria, each naming its proof | Otherwise the agent is inventing the definition of done |
| Its spec is approved, or the ticket is at the spec stage | The spec gate is not something a runner may skip |
| No other in-flight ticket touches the same migration | Migration files sort by name; two branches will not agree on order |
| Concurrency is below the cap | Below |
| The project's token budget for the day is not spent | Below |

**Concurrency cap.** Start at **three** concurrent tickets per project. The limit is not compute, it is
merge-conflict probability and the human queue: three tickets escalating at once is answerable, ten is a
person drowning. Raise it when the escalation log shows you are idle waiting, not before.

**What it may never do.** Hold production credentials. Push to main. Approve anything. Merge anything.
Change the protected set. Start a ticket at *genuinely novel* without a human already in the loop.

**When it stops.** On any class A, D or F escalation, that ticket halts and the others continue. If
every in-flight ticket is halted, the runner stops starting new ones — that state means the project is
blocked on people, and starting more work makes it worse rather than better.

**Where it runs is not built** — and on reflection it should not be built first. Unattended agents need
somewhere to run, a queue, credentials scoped away from production, and a notification path. None of that
exists.

But it is worth being honest about what the runner actually buys: it removes a person typing two
commands. That is perhaps thirty seconds per ticket. Against that it costs infrastructure, a new failure
surface, and it cannot be validated, because the thing it would drive has never run on a host at all.

Ranked by human attention saved per unit of work to build it, the runner is fourth:

| | Saves | Status |
|---|---|---|
| 1. Evidence the agent produces itself | booting an app and screenshotting it, on every UI ticket | **built** — the `operate-app` skill |
| 2. Graded and routed escalations | the wrong person being interrupted, and the skim at request twenty | to build, and it is cheap |
| 3. Garbage collection converting repeat questions into context | the same question being answered three times | procedure built, the log is not |
| 4. The runner | typing `/spec` and `/build` | to build, and expensive |

Build in that order. A runner driving an unproven loop that escalates to an unrouted queue would
industrialise whatever is currently wrong.

## The core, and the space for domain

Every project gets the same core. Projects differ, so they extend it. The rule for which is which:

> **If two projects would write it differently, it is domain. If they would write it the same, it is
> core, and it belongs in the starter repository rather than in one project.**

| | Core — every project, from the starter | Domain — this project only |
|---|---|---|
| **Agents** | explore, implement, review | a Shopify theme agent, a Medusa admin agent, a data-migration agent |
| **Skills** | `build-loop`, `operate-app`, `garbage-collect` | how to boot *this* app, seed *this* data, query *this* store, drive *this* admin |
| **Checks** | size, gates, spec, verify, review, perimeter, scan, evidence | lints bespoke to this codebase, structural rules for its layers |
| **Docs** | this set | the design document, decision records, criteria |

Two disciplines keep that from sprawling.

**Few and deep.** The temptation is a skill per task. The better investment is making the three core
skills better, because local tooling churns constantly and a skill is where that churn should hide. A
domain skill is doing its job when the tooling underneath can be replaced and nobody notices.

**Domain agents are narrow by construction.** A domain agent exists because a body of knowledge is too
large to carry in every context — how Shopify's checkout extensions actually behave, how a Medusa admin
route is wired. It does not exist to be a second implementer. Same tool restrictions as the core roles:
if it writes code, it cannot merge; if it reviews, it cannot write.

**Anything a second project needs gets promoted to the starter, by pull request.** That is how the core
grows, and it is the only way it should.

## What "production ready" means as checks

Not a slogan. Here is what we enforce, and honestly where it sits against a typical shop.

| Check | Typical? | What it buys |
|---|---|---|
| Format, lint, types, tests, build | common | table stakes |
| Coverage **on changed lines**, not whole-repo | uncommon | a number you earned rather than inherited |
| Every criterion carries a **named artefact** | rare | "verified" as prose stops being acceptable |
| A **browser artefact** for anything with an interface | rare | "it renders" stops counting; a page with no button renders fine |
| **Gate changes cannot hide** inside a feature commit | almost nobody | the class of change no other check can see |
| A **fresh session reviews** every ticket | uncommon | a session reviewing its own work catches less |
| The **host is asked** whether it enforces what we claim | almost nobody | the failure that started all of this |
| **Scheduled scan over HEAD**, not per diff | some | 41.1% of AI-introduced security issues survive the commit that introduced them |
| An artefact is **promoted, never rebuilt** | uncommon | what QA approved is what ships |
| **Mutation testing** | rare | *to build* |
| **Structural tests** — layer direction, file size, one canonical helper | rare | *to build*, see D7 in open questions |

Where we exceed typical is not the number of checks. It is two specific ideas: **evidence is required
per criterion**, and **the checks are themselves checked**. Most shops have more linting than us and
neither of those.

## What this costs

An honest gap, and it is the first thing to measure. Nothing in our documents currently says what a
ticket costs in tokens, and this model spends more than the one it replaces: escalations are cheap for
the human and not free for the budget, three concurrent tickets is three times the burn, and a scheduled
scan and a review agent run whether or not they find anything.

For fixed-price work that is a commercial question, not a technical one. Until we have a real number,
the runner's daily token budget per project is the control, and the number goes in the SOW.

## Before any of this runs

Named plainly, because a document describing a system that does not exist is the failure this whole set
is about.

| | Status |
|---|---|
| The six escalation classes, in the agent definitions | to build — a change to the three role agents |
| The escalation format, and a channel a human actually watches | to build |
| An escalation log, and the weekly hour reading it | the hour exists in [delivery](03-delivery.md); the log does not |
| The runner: queue, triggers, concurrency, budget | **to build, and it is the big one** |
| Somewhere for unattended agents to run, without production credentials | to build |
| Token cost per ticket | not measured |
| Everything in [enforcement](06-enforcement.md) | *written*, none *proven* on a host |

## What this revises

This document changes the human-attention model. Specifically, in
[the build loop](04-build-loop.md):

- **"Questions, all at once, in one pass"** was written to avoid interrupting a developer all day. Under
  this model that constraint is wrong: ask when you discover the need. Batching questions means guessing
  at the ones you have not yet hit.
- **The four things a person does** stay exactly as they are. They are gates, and gates do not move.
  What is added is a fifth: answer escalations, which arrive when they arrive.
- **"Every time you type continue, the harness failed"** still holds and gets sharper here. Under this
  model you should never type continue, because the runner does not need telling — if a ticket is
  stopped, it is stopped on a class, and a class has an answer rather than a nudge.

Nothing else in the set changes. The stages, the gates, the depth axes, the six numbers and the limits
are all unaffected: this is a change to who initiates, not to what is checked.
