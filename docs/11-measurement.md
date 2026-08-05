# Measurement: the six numbers

This document defines the only six things we count, where each one comes from, and how each one can be
made to lie. Read it if you are setting up the tracker, or if you are about to cut something for time.

## Why we count at all

Nobody is going to hand us a trustworthy figure for this. The strongest current evidence is a May 2026
meta-analysis pooling 23 studies and 27 effect sizes: productivity at g = 0.33, 95% confidence interval
0.09 to 0.58. Real, moderate, and — the decisive moderator — larger in controlled experiments and
**smaller in open-source and enterprise settings**, which is to say smaller in conditions like ours.
Microsoft's early-2026 rollout across tens of thousands of engineers saw adopters merge about 24% more
pull requests, sustained over four months rather than decaying as novelty; the authors say themselves
that a merged pull request is a proxy for output and not for value. Faros' 2026 telemetry across 22,000
developers, each organisation compared against its own low-adoption baseline, measures time-in-review
up 441.5% and incidents per pull request up 242.7%.

An early-2025 trial found experienced developers 19% slower on their own repositories while believing
they were 20% faster. That measured early-2025 tools, and its follow-up was redesigned rather than
published because developers increasingly declined to take part if they might have to work without AI.
There is no control arm available any more and there will not be one.

The conclusion is not a number. It is that the clean comparison is gone, the effect in our conditions
is moderate at best, and our own sense of whether the process is working is not evidence. So: six
numbers. Four say whether the loop is running. Two say what came out of it. None of them is lines of
code, because lines of code is the one quantity the agent can produce without limit.

## The three fields the tracker must carry from day one

Most of what follows can be reconstructed from git and the host API after the fact. Commit times, check
conclusions, merge times, review states and resolved conversations all persist. Three fields do not
exist anywhere unless something writes them down as they happen.

1. **Who found each defect** — the review agent, the tech lead at feature review, QA on uat, the client
   at the demo, or production. Nobody remembers in March who found the January bug, and the defect
   ticket records the fix, not the finder.
2. **Promotion and release timestamps** — when this exact artefact first reached dev, uat and
   production. Deployment records get pruned, and a re-deploy of the same artefact overwrites the
   answer to "when did it first arrive".
3. **Stage entry and exit dates** — every tracker overwrites the current status. The moment a ticket
   moves from *in review* to *merged*, how long it sat in review is gone unless a row was written.

Numbers five and six are made entirely of those fields, and number two is half made of them. Until a
tracker integration exists — it is one of the *to build* rows, so the instrumentation arrives last — a
tech lead records them by hand, one row per ticket and one per release. A spreadsheet with the columns
named below is enough. The apparatus is not the point; the columns existing from the first ticket is
the point.

## 1. How often a human changes something

**Definition.** Three separate rates, never averaged: specs a person altered or rejected before
approving, over specs approved; features sent back at feature review, over features judged;
gate-touching diffs that produced a comment, a revert or a ticket, over gate-touching diffs read. Below
roughly one in ten, that gate is ceremony, and we want to know in week three rather than in the
post-mortem.

**Where the data is.** The spec is the branch's first commit — see [the build loop](04-build-loop.md) —
so a change to it before approval is a diff on `docs/specs/<TICKET-ID>.md` inside the same pull
request. Feature-review send-backs are the defect and blocker tickets whose finder field says *tech
lead*. Gate diffs are read in a daily batch, so the count is kept by the person doing the reading.

**Bad readings, both ends.** Zero of twenty specs changed means approval is a button, not a judgement.
Nine of ten changed means the design document is not doing its job and every ticket is rediscovering
the same gaps — a different failure with the same fix, which is to correct the design document rather
than the spec.

**How it is gamed.** Reword a sentence and log a change. That is why the record names which part
changed — scope, an acceptance criterion, or the approach — and not merely that a diff existed. The
weakness we cannot close: a genuine approval and a rubber stamp are byte-identical on the host. This
number sees whether anything changed, never whether anything was read.

## 2. How long a ticket waits

**Definition.** From picked up to **running in dev** — not to merge. A feature that is not deployed is
not finished, so merge is the wrong place to stop the clock. Recorded in segments, because the total
tells you nothing about what to fix: waiting for answers to the agent's questions, waiting for spec
approval, waiting for the required checks to conclude, waiting for merge after green, waiting for the
dev deploy.

**Where the data is.** Most segment boundaries already exist: the spec commit's timestamp, the
check-suite conclusion times, the merge commit, and the deployment event emitted by the deploy workflow
in [host and pipeline](09-host-and-pipeline.md). Two are human — when someone picked the ticket up, and
when the questions were answered. Those two are the stage entry and exit fields.

**Bad reading.** Any single segment holding the median, and specifically a gate whose queue time
exceeds the ticket's own working time while, over the same window, that gate has caught nothing. A gate
that catches little while people wait days for it is worse than the same gate answered in an hour.

**How it is gamed.** The clock starts when someone claims the ticket, so claiming late shortens it.
Stage entry and exit dates are what stop that: the wait simply appears one column to the left, in the
backlog, where it is still visible.

## 3. How often review-agent findings are dismissed

**Definition.** Findings dismissed in writing, divided by findings raised, rolling over the last twenty
pull requests rather than per pull request. Alongside it, a second line that matters as much: the share
of pull requests where the reviewer raised nothing at all.

**Where the data is.** The review agent posts one review comment with a severity and a location per
finding. Required conversation resolution on main — set in
[host and pipeline](09-host-and-pipeline.md) — means every thread must end resolved, so each finding
has exactly one of three fates: a commit that fixes it, a written dismissal, or a resolution with no
reply. Count the third separately. It is a finding with no disposition wearing the costume of one.

**Bad reading.** We start by treating a sustained dismissal rate above roughly one in three as saying
the reviewer has not earned the right to block a merge. That threshold is our judgement and not a
measurement; what makes it usable is that it moves on data we are already collecting. The published
baseline is not flattering — across 19,450 pull requests, those reviewed only by agents merged at
45.20% against 68.37% for human-only review, and 12 of 13 agents averaged below a 60% signal ratio
(April 2026). Zero findings across many pull requests is the other bad reading: a reviewer that says
nothing scores perfectly and catches nothing.

**How it is gamed.** Apply a trivial fix instead of writing a dismissal, and accuracy looks better than
it is. Resolve the thread silently and it vanishes. Both are why the three fates are counted separately
and why dismissals are read where the gate diffs are read.

**How it is collected.** `scripts/collect-week.mjs` counts them, which is the reason `REVIEW.md` requires
a dismissal to begin `Dismissed:` — nothing else in a pull request distinguishes *this finding was wrong*
from ordinary discussion, and a rate nobody can compute is a rate nobody acts on. The same run prints how
many comments it read, so a clean week and a broken collector do not look identical.

## 4. How often a shortcut is taken

**Definition.** A count, per week, of every event in this list: a workflow that gained
`continue-on-error: true`, `if: false`, or a step ending in `|| true`; a test newly marked `.skip(`,
`.todo(`, `xit(`, `xdescribe(`, `@pytest.mark.skip` or `t.Skip(`; a check suite re-run more than once
with no new commit; a merge with a failing required check; a release-checklist line waived; a change to
branch protection.

**Where the data is.** The first two are exactly what the gates workflow greps for in the pull request
diff — the patterns and the code are in [enforcement](06-enforcement.md). It works that way because a
bypass leaves no marker in the commit object: the job catches what a bypass tends to leave behind, not
the bypass. Re-runs and admin merges come from the host API and its audit log. Waivers are lines in
`docs/releases/<version>.md`, written against [the release checklist](08-templates.md).

**Bad reading.** Any admin merge at all. Any week where re-runs without a commit exceed a couple. A
cluster of all three inside one release window, which is what a team under launch pressure produces.

**How it is gamed — and it does not need to be.** `git commit --no-verify` is invisible. So is `git
stash` used to hide staged state. An agent has been observed landing six consecutive commits that way,
taking a suite from 104 passing to 63 failing, with hooks configured the whole time. **This number is a
floor, not a total.** The honest statement is that it counts shortcuts that left an artefact. That is
also the price of leaving admin enforcement off on branch protection: defensible on a small team where
one person would otherwise be locked out of their own repository, but it converts "cannot" into
"countable", and the count only helps if someone reads it.

## 5. How many defects reach a person, per merged ticket

**Definition.** Defect and blocker tickets opened after the merge of the work that caused them, divided
by tickets merged in the same window, split by who found them: review agent, tech lead at feature
review, QA on uat, client at the demo, production. Per merged ticket and not per week, so it does not
move just because throughput did. A pre-merge finding on the ticket's own pull request is number three,
not this — the review agent appears here only when it finds, on some later pull request, something that
belongs to already-merged work.

**Where the data is.** The finder field, written when the ticket is opened. Because the fix is always a
new ticket and never a reopened one, the link from defect to origin is a real edge in the tracker
rather than a memory.

**Bad reading.** The total staying flat while the split drifts from QA towards the client and
production. That is a gate decaying, not a quiet week, and it is the only shape in these six numbers
that says a gate is being used and still catching nothing useful. Polish tickets swelling while defects
fall is the same event described more politely.

**Trend, never a target.** Whoever finds a defect classifies it — the finder, and whether it is a
blocker, a defect or polish. A target on this number is met by reclassifying, and reclassification
leaves no trace. So it is read as a direction over months, never quoted as a figure to hit, and never
in anyone's objectives.

## 6. How long accepted work waits to go live

**Definition.** Per release, not per ticket: from the demo at which the client accepted a feature to
the release that put it in production, with the stage it sat in recorded — waiting on other work, on
Release Check, on a launch window, on the client. Per ticket this would mostly measure how fast the
client answers. Per release it measures how much finished work we are holding.

**Where the data is.** The acceptance date, recorded at the demo by hand. The release date, from the
git tag and the dated `docs/releases/<version>.md`. The promotion timestamps for the artefact in
between, from the promote workflow in [host and pipeline](09-host-and-pipeline.md).

**Bad reading.** The median rising release over release while number two is flat or falling. That is
the whole failure these documents exist to prevent, in one line: the loop got faster and
[the sequence around it](03-delivery.md) did not. This is the only number here that can show it,
because every other one stops before the part that would absorb the gain.

**Trend, never a target.** Whoever records the acceptance sets the start of the clock, and we decide
what goes in a release. Both are levers on the number that are not levers on reality.

| # | Already in git or the host | Recorded by a person until the integration exists |
|---|---|---|
| 1 | spec diffs, review states, resolved threads | which part of the spec changed; gate-diff outcomes |
| 2 | commit, check, merge and deploy times | picked-up date; questions-answered date |
| 3 | review comments, thread resolutions | nothing |
| 4 | workflow diffs, re-runs, audit log, waiver lines | nothing |
| 5 | defect tickets and their links | **who found it**, and its class |
| 6 | tags, release files | **acceptance date, promotion timestamps, stage dates** |

## What the six together can and cannot detect

```
┌─ WHAT THE SIX CAN SEE ───────────────┐  ┌─ WHAT THEY CANNOT ───────────────────┐
│  a gate that never changes anything  │  │  whether an approval was read        │
│  a gate whose queue is its real cost │  │  a skim that produces no defect      │
│  a reviewer nobody believes          │  │  a defect class nobody looks for     │
│  a shortcut that left an artefact    │  │  a bypass that left nothing behind   │
│  defects moving between finders      │  │  which change caused which movement  │
│  accepted work waiting for a release │  │  what sixty tickets did together     │
└──────────────────────────────────────┘  └──────────────────────────────────────┘
```

Number five bought us something we did not have before. The most likely way this process fails on a
small team is the tech lead's queue collapsing and feature judgement quietly becoming a skim of the
pull request — which is exactly the review we decided not to rely on. A skim now shows up: defects
drift from the feature review towards QA and the client while the total holds. **What it still cannot
see is a skim that produces no defect anybody ever finds.** And number two will not help, because a
lead who is skimming looks fast rather than slow.

Three more limits, stated so nobody reasons past them. A defect class nobody in the chain is equipped
to find reads as zero defects — an unexamined authorisation hole is indistinguishable here from a
correct one. What many changes did together is invisible to all six, because each is scoped to a ticket
or a release; that is what the scheduled scans are for. And these numbers cannot attribute. We have no
control arm and, per the redesigned follow-up, we are not going to get one, so six numbers moving
together tell us where to look and never what caused it. [Limits](14-limits.md) has the longer list.

## The candidate seventh: rework

Not one of the six, and it should be if the pain a team most wants proved solved is *endless refactoring*.
Neither number five nor number two sees it: work that gets redone because it was built against a shape that
was never fixed produces no defect and no wait, only cost.

**Definition, if it is added.** Tickets reopened, or substantially redone within a phase, over tickets
merged. "Substantially" needs a written line — a second pull request touching more than half the same files
is a defensible one, and it is countable from git rather than from anyone's memory.

**Decide before the first ticket, or not at all.** Like who found each defect, it cannot be reconstructed
afterwards: reopening is only visible if reopening is recorded at the time, and a ticket quietly superseded
by a new one leaves nothing behind. The contracts-first rule and the spec-before-code rule are both aimed
squarely at this number, so leaving it unmeasured means the two most expensive parts of the process go
unevaluated.

## If something is cut for time, cut a gate

A gate we have not built yet is a known absence. Everyone downstream can reason about it, and it can be
added in an afternoon. A number we never started counting is an answer we cannot get back — the three
day-one fields have no source anywhere else, and a trend that starts in month four cannot describe
months one to three.

So the order of sacrifice is fixed: **the counting survives, the gates give way.** If that feels
backwards, it is worth remembering that the gates are a hypothesis about what protects us, and the
counting is the only thing that will ever tell us whether the hypothesis was right.
