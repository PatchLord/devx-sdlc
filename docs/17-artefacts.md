# The documents, and what happens to each

Every artefact the process produces, who owns it, whether it lives or freezes, and how one becomes the
next. Read this if you are unsure which document a piece of information belongs in, or why a spec is
written at development time rather than in advance.

The stages are in [before the build](02-before-build.md) and the per-ticket procedure is in
[the build loop](04-build-loop.md). This document is about the artefacts themselves.

## The chain

```
 (BRD) ──▶ SOW ──▶ PRD ──▶ TDD ──▶ contracts ──▶ features ──▶ tickets ──▶ spec ──▶ code
   ┆        │       │       │          │            │            │          │
   ┆        │       │       │          │            │            │          └── written at development
   ┆        │       │       │          │            │            │              time, never in advance
   ┆        │       │       │          │            │            └── one branch, one PR, under 300 lines
   ┆        │       │       │          │            └── a TDD section. big, meaningful, demo-able
   ┆        │       │       │          └── shared surfaces, fixed before anything builds on them
   ┆        │       │       └── every client question closed. LIVING.
   ┆        │       └── what and why, for a phase
   ┆        └── commercial frame, and the depth level
   └── OPTIONAL, and theirs not ours. Often it does not exist
```

**The BRD is optional.** Plenty of engagements arrive as a conversation, a Slack thread, or a call with no
document at all, and demanding one before we will engage is a good way to lose the work.

**And we cannot assume it comes from them.** Often the client has no document and no appetite for writing
one, so *we* write it — from the call, the thread, whatever exists — and send it back. That is normal agency
work and it is not a worse starting position.

So the rule is not about authorship. **Who typed it does not matter; whether the client confirmed it in
writing does.** A BRD we drafted and they never answered is our assumptions wearing their authority, which is
the most expensive document in an engagement — every later scope argument gets settled by pointing at
something they never agreed to.

What is **not** optional is that *something the client has confirmed records what they asked for, before our
SOW exists.* Their document, or ours confirmed by them. Either way the SOW must not be the first written
account of their own requirements, because then there is nothing to check it against and every later argument
about scope becomes an argument about memory.

**When a BRD does arrive, it arrives imperfect, and we do not tidy it.** It will be vague where they have not
thought something through, it will contain a contradiction between two things they want, and it will usually
ask for at least one thing that is a bad idea. Those three properties are the *input* to Solutioning, not
defects to correct before work starts. Surfacing them is what the SOW and the discovery meeting are for, and
a BRD with no problems in it means somebody has already rewritten the client's thinking into ours.

## The rule that settles most arguments

> **A spec is a record. A TDD is a description. Records are never updated; descriptions always are.**

One clarification, because our own checks are more permissive than that sentence and an outside review
caught the gap. "Never updated" means *never quietly* updated. Revising a spec mid-flight is legitimate —
the exploration was wrong, or the work taught you something — and `spec.yml` handles it by **warning**
rather than failing, on the rule that the existing approval was of the earlier text and needs renewing. The
prohibited thing is the silent edit, not the edit. Same for a frozen meeting note: a correction is appended
under its own date, never written over what was recorded.

A spec captures what was agreed before code existed. If implementation proves it wrong, that is a
*finding* — recorded in the pull request, not edited into the spec. Editing it destroys the only evidence
that the approval was of something specific.

A TDD describes the system. When it stops matching the system, it is wrong and gets fixed.

## Each artefact

| Artefact | Owner | Drafted by | State | Notes |
|---|---|---|---|---|
| **BRD** | the client confirms it, whoever wrote it | them, or us from a conversation | optional. Frozen once confirmed | Their written confirmation is the record, not our draft |
| **SOW** | practitioner / OM, tech lead signs | people | frozen | Carries the depth level and what the client was told about which checks exist |
| **PRD** | tech lead or CSM | people | frozen | Changes go through the CSM, because they change what the client accepts |
| **TDD** | tech lead | agent drafts, developer interrogates | **living** | Its job is closing questions, not documentation |
| **Contracts** | tech lead | agent drafts, one review | living, protected path | API shapes, schema, shared types, module boundaries |
| **Acceptance criteria** | code owner | agent proposes | protected path | Each names the artefact that proves it |
| **Production-ready standard** | tech lead | grows weekly | living | Project-level, not per phase. `docs/production-ready.md` |
| **REVIEW.md** | the team | edited freely | living | Review criteria, so changing them needs no agent edit |
| **Spec** | the developer | explore agent | **frozen at approval**, revised only visibly | Branch's first commit, ancestor of every implementation commit. `spec.yml` warns when it changes after implementation began |
| **Board** | the team | whoever raises a ticket | living, entries reach a terminal state | `tasks/board.md`. **This is the tracker**, in the repo |
| **Decision records** | whoever decided | either | append-only | Superseded, never corrected |
| **Release checklist** | tech lead | people | one per release | Three columns, and the third is not optional |
| **Discovery meeting notes** | delivery lead | people | frozen, append a correction | Where the BRD's contradictions surface. Carries the agreed decision-maker and response time |
| **Escalation & defect log** | the named weekly person | agent appends escalations, a script appends the rest | append-only, rows close | `log/`. Only reader is the weekly hour |

## Why there is no learnings document

It is the obvious thing to add and it is the wrong artefact. By the tier scheme in
[enforcement](06-enforcement.md) it is tier 3 — prose — which is the tier our own pilot measured at 0 of 7.

It is also worse than merely weak, because it gives a learning somewhere legitimate to go that is not a
check. "I logged it in learnings.md" feels like completion. That is the same failure as writing a rule in
prose instead of a lint, except it looks like process compliance. And it has no exit condition, so it only
grows and nothing is ever removed from it.

### Where that argument was too strong — corrected 6 August 2026

A live client project (250 commits, spec-kit driven) keeps both a `tasks/lessons.md` and a board, and the
two behaved differently enough to settle this:

| | added | deleted | commits |
|---|---|---|---|
| its board | +326 | **−9** | 6 |
| its lessons file | +61 | **0** | 3 |

**The claim about exit conditions survives, measured.** Nothing has ever been removed from that lessons
file. The board resolves entries in place; the lessons file only accumulates.

**The claim that a learnings document is the wrong artefact does not survive**, and the reason is what its
entries contain. Every one is an *agent-behaviour* correction, not a code pattern: the shell's working
directory persists between calls so a "not found" is not proof of absence; never describe a client-side
control as making invalid input impossible, only as constraining it; when code changes, sweep the whole plan
document rather than the flagged block, because those documents contain executable recipes and a half-fixed
one is a regression generator.

**None of those can be a lint.** There is no rule that catches *I concluded a file did not exist after
searching from the wrong directory.* Our own table above says learning about how to work belongs in
`CLAUDE.md`, a skill or `REVIEW.md` — and a lessons file is the staging area for exactly that. So the
correct rule is narrower than the one we wrote:

> A learnings document is the wrong home for anything a check could enforce. For corrections that **no
> check can express**, it is the right home — provided each entry has somewhere to go afterwards.

That last clause is the whole of it, and it generalises past learnings files:

**An append-only document is safe when every entry has a terminal state, and a graveyard when it does not.**
The log has dispositions. The board has Resolutions. A lessons file with neither only grows, and the test is
mechanical rather than a matter of opinion — `git log --numstat` on the file should show deletions. So a
lessons file is legitimate with one addition: each entry is either **promoted** into `CLAUDE.md` or a skill
and removed, or **closed** as a one-off. That promotion is work for the weekly hour, alongside converting
repeated corrections into checks.

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

## The board, and why the tracker can live in the repository

Every document here says *always work from a ticket* and none of them said where the ticket lives. We
assumed a tracker. A live project answered it differently — the tracker is a file in the repo — and the
argument for that is stronger than the one we had:

| | A tool | `tasks/board.md` |
|---|---|---|
| The agent can read it | only through an integration | **on every run, for free** |
| Number of writers | two, and they drift | one |
| Status | typed by a person | derived: a branch exists, a pull request merged |
| A change to a ticket | an edit nobody reviews | a diff with an author and a date |
| Non-engineers can see it | **yes** | no |
| Cross-repo milestones | **yes** | no |

The first row is the one that decides it for agent-run delivery. Our own strongest principle is that the
only documents with a guaranteed reader are the ones in the repository — that is why `CLAUDE.md` and the
skills carry what they carry. A tracker fails that test, and an integration that puts a third-party service
on the critical path of a keystroke fails during exactly the incident where you need it.

The last two rows are the real cost and they are not small. **Delivery, the CSM and the client cannot see a
markdown file.** If they need a view, generate it: the repository writes, the tool displays, never the
reverse. The moment somebody types status into the tool there are two answers, and the tool's is the one
that gets quoted back at you.

**One file works to about five or six people.** Past that, concurrent edits conflict constantly and it
becomes one file per ticket with the same shape. Split before the conflicts feel normal.

### What an entry carries that a ticket usually does not

Three headings do the work, and they are the ones a tracker's fields do not have room for:

**Findings — verified, not speculative.** What has actually been reproduced, with file and line, kept
distinct from what is suspected. Including the negative results: *this reads like a defect and is not, it
just has no test pinning it* saves the next person the same hour.

**When picked up.** The next actions, specific enough to start cold, with the decisions a person must make
left as questions rather than quietly assumed.

**Resolution, written when it closes — including what did *not* change.** What the obvious fix would have
got wrong. What was deliberately left alone. What remains open, named, so closing the ticket does not
silently close it too.

That third heading is the one worth insisting on. A ticket that closes with only a list of what shipped
loses the more useful half: the live project's own entry records that three of nine apparent defects were
not defects, and that the obvious automatic fix *would have papered over two of them.* No tracker field
would have held that, and it is exactly what the next person needs.

### Deferred work has somewhere to go now

Our pull request template lists where a learning lands: a test, a fixture, a decision record, the design
document, a rule in `CLAUDE.md`, the CSM. **Verified adjacent work that is deliberately out of scope was on
none of those lists**, so it either bloated the pull request past the size ceiling or evaporated in a review
comment. It goes on the board, as its own entry, with its findings.

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
