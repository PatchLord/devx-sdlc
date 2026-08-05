# Why this exists

This document holds the reasoning the rest of the set assumes: the problem we are solving, the one law we
derived from our own pilot, and the five ideas that decide every argument the other documents do not cover.
Read it once. There is nothing here to implement.

## What this set is

These documents replace a single manual that grew to 72,000 words and stopped being read. Each one now stands
alone for its own job. Every configuration file the process depends on is reproduced in full somewhere in the
set — the agent definitions, the commands, the workflows, the scripts, the templates, the hook config — and
exactly once, with every other document linking to it rather than repeating it. Every threshold is given as
the number it actually is. The host settings are the exact API fields and values we set on a real protected
repository, not advice to "enable branch protection".

Two things this set is not. It is not an argument for adopting AI-assisted development. That decision is made,
and the interesting question is what has to be built around it. And it is not proven. Every check in
[enforcement](06-enforcement.md) carries a status, and the three values mean different things:

- **written** — the file exists and its logic is tested locally.
- **proven** — it has run on a host and failed something it should have failed.
- **to build** — the check protects nothing today.

Read that column literally. Never quote a *written* row to a client as a guarantee. This whole set is about
the gap between *written* and *proven*, and it is not exempt from it.

One decision needs stating here because four documents depend on it. `review` ships as a required check: the
starter sets `REQUIRED_CHECKS="size gates spec verify review"` in `perimeter.yml`, and that is the steady
state. During adoption only, you run it un-required until its dismissal rate justifies letting it block a
merge — [the runbook](12-runbook.md) gives the sequence. So "required" and "un-required at first" are both
correct, in that order. If you are past adoption and `review` is not in your required contexts, that is drift,
and the perimeter check will say so.

## The problem: generation got cheap, checking did not move

The 2026 evidence agrees on the shape of this and disagrees on the size. That is useful, because the shape is
what the process has to absorb.

| Finding | What it licenses | What it does not |
|---|---|---|
| May 2026 meta-analysis, 23 studies, 27 effect sizes: productivity **g = 0.33** (95% CI 0.09–0.58); gains larger in controlled experiments and **smaller in open-source and enterprise settings**; learning **g = 0.14**, interval spanning zero | The effect is real, moderate, and shrinks as conditions move towards ours | Any claim of a multiple; any claim that working through an agent builds engineering skill |
| Microsoft, early-2026 rollout across tens of thousands of engineers: adopters merged about **24% more pull requests**, sustained over four months | Output rises, and not as a novelty effect | That the extra pull requests carried proportional value — the authors say this themselves |
| 2026 report on **22,000 developers**: time in review up **441.5%**, incidents per pull request up **242.7%**, bugs per developer up **54%** | Where throughput rose, checking is where the damage landed | A causal claim per team; this is vendor telemetry against each org's own low-adoption baseline |
| April 2026, **19,450 pull requests**: agent-only-reviewed PRs merged at **45.20%** against **68.37%** human-only | That an agent reviewer is not a substitute for the human gate | That agent review is worthless; it says the merge rates differ, not which reviews were right |

Put together: more work arrives, it arrives at the one part of the sequence that did not get faster, and the
measured cost shows up as incidents and review time rather than as slower typing. Most advice about AI in
software development fails because it makes the fast part faster.

One number will be quoted at you. An early-2025 trial found experienced maintainers on their own large
repositories were **19% slower** with AI while believing they had been 20% faster. That measured early-2025
tools and is routinely presented as current. It is not. The follow-up was redesigned rather than published,
and the reason matters more than any figure in it: developers increasingly refused to take part in an arm
where they could not use AI, and some withheld exactly the tasks they most wanted AI for. The clean randomised
experiment is becoming impossible to run, because there is no longer a population willing to be the control
group. Nobody is going to hand you a trustworthy productivity number in either direction. That is the argument
for [the six numbers](11-measurement.md): your own counted data is the only kind you will get.

The concrete version, from our own pilot: the backend — schema, migration, scoring engine, catalogue, public
API, admin API — arrived as five commits totalling 2,789 lines, between 17:51 and 18:21. Reading 2,789 lines
properly takes most of a working day. That second figure is our estimate, not a measurement, and it is the
first number this process should replace with a counted one.

## The law: the agent builds to the shape of the check

We ran the experiment on ourselves before running it on a client's money. One frozen spec file, one cold
session, no process at all — no review gate, no checkpoints, deliberately. It produced a Bun/Hono/Prisma
backend, a Next.js quiz and a forked Medusa admin panel: 44 commits, 64 tests, 87% line coverage on the
backend. By the usual measures it went well.

Sort what it produced by what was checking it, and the split is clean:

```
  WHAT THE PILOT BUILT, SORTED BY WHAT WAS CHECKING IT

  gated  · backed by a config file, hook or test    │████████████████  8 of 8 present
  prose  · no check named anywhere                  │                  0 of 7 present
```

The same split appears inside one application. The admin panel had nine write hooks — create, update and
delete for questions and root causes, plus login — and not one was called from any page. Zero buttons, zero
forms, zero submit handlers, no login screen. The write side existed at every layer except the one a human
touches. The read side, where a wired hook is visible on screen, had 8 of 9 hooks working. It was not a
capability problem: the same model in the same session wrote a complete write flow in the customer quiz —
validation, a disabled Next button, submit, report page — and the only difference between that flow and the
nine that do not exist is that the quiz had a Playwright test clicking through it.

The agent said so in its own committed build report: it noted the admin app had no unit suite and picked the
render verification as its substitute gate. It found the gap, reasoned about it, and chose a check. A page
with no Create button renders perfectly. Every step in that sequence is defensible and the result is an admin
panel you cannot type into.

One more finding from the same repository, because it generalises worst. Its own context file stated that main
was protected and a red pull request could not merge. There was no remote. CI had run zero times. Nothing in
that sentence was a lie anyone told; from inside a repository, a check that is written down and a check that
is wired up look identical.

> **The agent builds to the shape of the check. A weak gate does not give you the same product less verified.
> It gives you a different, smaller product.**

So a check is not a filter applied to finished work. It is a specification of what the work will be. "We will
review it at the end" cannot recover this, because by the end the thing you meant to review was never written.

The honest status of that law: one uncontrolled run, n=1, no comparison arm. It is an existence proof of a
failure mode and a measured split within a single build. It is not an effect size, and these documents never
use it as one. It earns its place because it explains where every check in the set is pointed.

## The five ideas

When these documents do not cover your situation, reason from these. Each states what it costs, because a rule
whose cost is hidden gets dropped the first week it is inconvenient.

### 1. Speed is not the constraint. Checking is.

So the unit of work is set by what a person can check, not by what an agent can produce. Concretely: a ticket
is under 300 lines and 10 files, and CI fails the pull request above 400 lines or 20 files. Past some size a
reviewer stops reading and starts approving, and a review that has become a rubber stamp is indistinguishable
from no review while still producing a green check. What this costs: throughput is now capped by review
capacity rather than by generation, which feels like deliberately going slower. The weakness is that 300 is
our judgement. The argument gives a direction, not a number. It should move as soon as we can measure the diff
size at which our own reviewers stop finding anything. [The build loop](04-build-loop.md) holds the sizing
rules; the ceiling is enforced in [enforcement](06-enforcement.md).

### 2. If something is not checked, it will be skipped.

Anything genuinely required is either an automatic check that fails the build, or a line on a checklist that a
named person signs with a link to evidence. Anything else is a wish. This bites hardest on security,
monitoring, backups and load testing, because a missing feature is obvious and a missing backup is not. What
this costs: writing the check is several times more work than writing the sentence, so this idea forces you to
either build enforcement or admit the requirement is unenforced. We take the second option in several places,
and each time we say so in the same line rather than leaving you to assume.

### 3. A check that is documented but absent is worse than one never promised.

Everyone downstream then reasons from a guarantee that does not exist — including the agent, which reads your
context file as fact, and including the client, if it went into a statement of work. So the checks themselves
get checked: a workflow asks the host API what it is actually enforcing and fails when that diverges from what
the repository claims. What this costs: that workflow needs a fine-grained token with `Administration: read`,
which is one more secret to manage, and it can only see configuration. It cannot see whether a human read the
spec they approved. Nothing can see that, ever, and these documents say so wherever the question comes up.
The perimeter and its token live in [host and pipeline](09-host-and-pipeline.md).

### 4. Done means there is an artefact.

A test result, a screenshot compared against the design frame, a trace, a signed line with a link. Not a
status update saying it is done. Agents report success they have not earned, and most readily when handed a
completion signal to write to — a self-maintained status board is exactly that. Our pilot marked its own work
done. So ticket state is computed from what happened: branch pushed, checks green, review approved, merged,
promoted. What this costs: derived status needs a tracker integration, and that integration is realistically
the last thing anyone builds. Until it exists a person records the timestamps by hand, and
[measurement](11-measurement.md) names the three fields that cannot be reconstructed later.

### 5. There are two ways to get this wrong, and they pull in opposite directions.

Hand an agent something large and vague and you get thousands of lines nobody reads. Keep all the thinking
human and use the agent only to type, and the work that actually consumes time never got faster. So ask at
every step: *what are people writing by hand here that an agent should be drafting?* — and separately, *what
did we hand over without a check attached?* What this costs, and it is the honest weakness of the whole set:
no gate detects either failure. This one is judgement. It is an idea rather than a check because we could not
find a way to make it one.

## Where to go next

If you want to know what the process does, read [the lifecycle before build](02-before-build.md) and then
[delivery](03-delivery.md). If you want to know how much of it a given project gets, that is decided by cost
of failure rather than by size or type, in [depth](05-depth.md).

If you are setting this up, go to [the runbook](12-runbook.md). It gives the dated order, and the order is not
the reading order in one respect: the host configuration goes on `main` before anything else, including files
you have already committed. Until it is set, every workflow in the repository is advisory, because the
workflows live where an agent can edit them and branch protection does not.
