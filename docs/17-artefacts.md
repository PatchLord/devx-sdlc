# The documents, and what happens to each

Every artefact the process produces, who owns it, whether it lives or freezes, and how one becomes the
next. Read this if you are unsure which document a piece of information belongs in, or why a spec is
written at development time rather than in advance.

The stages are in [before the build](02-before-build.md) and the per-ticket procedure is in
[the build loop](04-build-loop.md). This document is about the artefacts themselves.

## The chain

```
  SOW ──▶ PRD ──▶ TDD ──▶ contracts ──▶ features ──▶ tickets ──▶ spec ──▶ code
   │       │       │          │            │            │          │
   │       │       │          │            │            │          └── written at development
   │       │       │          │            │            │              time, never in advance
   │       │       │          │            │            └── one branch, one PR, under 300 lines
   │       │       │          │            └── a TDD section. big, meaningful, demo-able
   │       │       │          └── shared surfaces, fixed before anything builds on them
   │       │       └── every client question closed. LIVING.
   │       └── what and why, for a phase
   └── commercial frame, and the depth level
```

## The rule that settles most arguments

> **A spec is a record. A TDD is a description. Records are never updated; descriptions always are.**

A spec captures what was agreed before code existed. If implementation proves it wrong, that is a
*finding* — recorded in the pull request, not edited into the spec. Editing it destroys the only evidence
that the approval was of something specific.

A TDD describes the system. When it stops matching the system, it is wrong and gets fixed.

## Each artefact

| Artefact | Owner | Drafted by | State | Notes |
|---|---|---|---|---|
| **SOW** | practitioner / OM, tech lead signs | people | frozen | Carries the depth level and what the client was told about which checks exist |
| **PRD** | tech lead or CSM | people | frozen | Changes go through the CSM, because they change what the client accepts |
| **TDD** | tech lead | agent drafts, developer interrogates | **living** | Its job is closing questions, not documentation |
| **Contracts** | tech lead | agent drafts, one review | living, protected path | API shapes, schema, shared types, module boundaries |
| **Acceptance criteria** | code owner | agent proposes | protected path | Each names the artefact that proves it |
| **Production-ready standard** | tech lead | grows weekly | living | Project-level, not per phase. `docs/production-ready.md` |
| **REVIEW.md** | the team | edited freely | living | Review criteria, so changing them needs no agent edit |
| **Spec** | the developer | explore agent | **frozen at approval** | Branch's first commit, ancestor of every implementation commit |
| **Decision records** | whoever decided | either | append-only | Superseded, never corrected |
| **Release checklist** | tech lead | people | one per release | Three columns, and the third is not optional |
| **Escalation & defect log** | the named weekly person | agent appends escalations, a script appends the rest | append-only, rows close | `log/`. Only reader is the weekly hour |

## Why there is no learnings document

It is the obvious thing to add and it is the wrong artefact. By the tier scheme in
[enforcement](06-enforcement.md) it is tier 3 — prose — which is the tier our own pilot measured at 0 of 7.

It is also worse than merely weak, because it gives a learning somewhere legitimate to go that is not a
check. "I logged it in learnings.md" feels like completion. That is the same failure as writing a rule in
prose instead of a lint, except it looks like process compliance. And it has no exit condition, so it only
grows and nothing is ever removed from it.

Learning already has three homes, and each has a reader:

| Kind of learning | Where it goes | Who reads it |
|---|---|---|
| About the **code** — this pattern is always wrong here | a lint rule or a structural test | the machine, every push |
| About **how to work** — the agent keeps not knowing X | `CLAUDE.md`, a skill, `REVIEW.md` | the agent, every run |
| About **why we decided** — the reasoning behind a check | a decision record, and the commit that added the check | whoever runs `git log` on the lint |

`CLAUDE.md` and the skills are the real learning document: they are the only files in the system with a
guaranteed reader on every run. So the useful question when someone wants to write a lesson down is *which
skill does this belong in* — and if the answer is none, it probably was not a lesson.

The third row is the one people reach for a learnings document to solve: losing the *why*, so that someone
deletes a lint in six months because it looks arbitrary. That is what `garbage-collect` step 5 is for. The
reasoning attached to the change beats the reasoning in a central document, because it is findable from the
thing itself.

### What the log is instead

`garbage-collect` triggers on **the same correction twice**. Nothing recorded the first occurrence — human
memory was the mechanism, and it does not scale past one person or one week. Two of the six numbers in
[measurement](11-measurement.md) were uncomputable for the same reason.

| | A learnings document | The log |
|---|---|---|
| Written | when someone feels they learned something | every time the event happens |
| Content | insight, prose | one row: date, kind, what happened, disposition |
| Read by | nobody | the weekly hour, and only then |
| Produces | more prose | a check, or a deletion |
| A row is done when | never | it has a disposition |

Nearly all of it is extracted rather than typed, because anything that depends on someone remembering to
write it down does not get written down. Review findings, dismissals, what the design document got wrong
and the questions a spec asked are all already recorded in pull requests. **Defects found after merge are
the one hand-written entry**, and they are worth the keystrokes: a defect that reached a person is the only
measurement here that cannot be gamed.

## Why the TDD is the document that matters most

Its purpose is not to describe. It is to **close every question that has human latency attached** —
client answers, third-party behaviour, access, credentials — so implementation does not stall waiting for
someone outside the building. That is the real return on the time spent, and it is a better answer to the
blocker problem than any amount of chasing.

It is also where a developer's understanding of the system comes from. Which produces the risk worth
taking seriously:

**A stale TDD is worse than no TDD.** Someone who has read it believes they know where a symptom points,
and points the agent confidently at the wrong part of the system. Not knowing is recoverable; being
confidently wrong is not, and it is invisible from the inside.

So the pull request template carries **"what the design document got wrong."** Empty is fine. Not empty
means the TDD is fixed in that pull request or a linked one. That one field is the whole defence.

### Which parts a person must write

An agent drafting the TDD from the PRD is much faster, and it should. But reviewing a plausible document
is far easier to do badly than writing one — approve an unread design and you have encoded instructions
nobody agreed to.

So three sections cannot be agent-drafted, because writing them requires actually understanding the
system: **the open questions, the risks, and what we are deliberately not doing.** They are the proof the
review was real.

## Why the spec is written at development time

Three options were considered: all specs at TDD close, only the unblocked ones, or one at a time during
development. The third wins on two counts.

**Accuracy.** A spec's value is being right about the code as it is *now* — that is what makes it
load-bearing for the implementing agent. Ticket 20's spec written today describes a repository that will
not exist once nineteen tickets have changed it. Handing an agent a confident description of the wrong
codebase is worse than handing it nothing, because it will not go looking.

**Reviewability.** Twenty-five specs is a batch review, and batch review is where the skim lives.
Anthropic measured only 16% of their own pull requests getting substantive feedback under velocity
pressure. An unread approved spec is the worst artefact in the process: the agent now has authority for
instructions nobody actually agreed to.

## Why contracts go first, and what that buys

The one thing produced at TDD close rather than per ticket. Not the specs — the **shared surfaces**: API
shapes, schema, shared types, module boundaries. One document, one review, and it is reviewable because
it is one thing.

**It converts sequential dependencies into parallel ones.** Most tickets that look blocked on each other
are blocked on *not knowing what shape an earlier ticket will produce*. Fix the shape and they
parallelise. Our own pilot is the evidence: freezing the contract first and building three tracks against
it was the single thing that went right, with no conflicts.

If you have twenty-five tickets and five look workable, do contracts and count again.

## Features and tickets are different units

The unit of meaning and the unit of review are not the same thing, and conflating them is expensive.

A **feature** is a TDD section: big, meaningful, demo-able. A **ticket** is one branch, one pull request,
under 300 lines. A ticket is not a unit of meaning — it is a unit somebody can actually check.

The evidence for keeping tickets small is unusually consistent. On pull requests over 1,000 lines,
**84% receive findings averaging 7.5 issues** — big diffs are where defects live. Engineers skim rather
than review to keep velocity, and skim probability rises with size. And OpenAI's Frontier team
restructured their codebase specifically to make pull requests smaller, because merge conflicts at 3.5
pull requests per engineer per day were unmanageable.

## When a document is blocked work

A developer waiting on a client should not write specs for far-future tickets — those go stale. The work
that does not go stale: **contracts, committed fixtures, test scaffolding, and domain skills.** Those hold
their value regardless of when the blocker clears.
