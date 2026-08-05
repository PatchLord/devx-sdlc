# The devx AI SDLC

How we build software with agents, and the checks that make it safe to. Twenty short documents rather than
one long one, because nobody reads a 92,000-word file.

**Read this page first.** It is five minutes and it is enough to hold the shape in your head.

---

## The whole thing in five minutes

**The law everything follows from.** An agent builds to the shape of the check. A weak gate does not
give you the same product less verified — it gives you a different, smaller product. In our own pilot,
of the requirements backed by a config file, a hook or a test, 8 of 8 were present and correct. Of the
requirements written only as prose, 0 of 7 were.

**Why a process at all.** Generation got cheap; checking did not move. Across tens of thousands of
engineers in early 2026, adopters merged about 24% more pull requests — while a 2026 report on 22,000
developers found time in review up 441.5% and incidents per pull request up 242.7%. More arrives, and
it arrives at the one part of the sequence that did not get faster.

**Eight stages per project.**

```
  00 Solutioning → 01 Handover → 02 Kickoff → 03 Setup
                                                  ↓   ends with something actually deployed
       ┌──────────────────────────────────────────┘
       ↓
  04 Build ──→ 05 Release Check ──→ 06 Launch ──→ 07 Run and Support
       ↑                                                    │
       └────────────────────────────────────────────────────┘
              bugs and change requests re-enter Build as tickets
```

**One loop per ticket, inside stage 04.** Context → questions → spec → *a person approves* →
implement → verify → wrap → merge. One ticket, one branch, one pull request, one merge.

**Three agent roles, in sequence, never in parallel.** They are real because their tool lists differ,
not because they have names. Explore reads and writes one file, the spec, then stops. Implement writes
code but cannot merge, cannot push to main, and cannot touch a test it did not add. Review cannot write
at all.

**A ticket is sized to the review, not the clock.** 300 lines and 10 files is the target; CI fails
above 400 or 20. Past some size a reviewer stops reading and starts approving, and a rubber stamp is
indistinguishable from no review while still producing a green check.

**Hooks are hints. Gates live on the host.** An agent can run `--no-verify` and can edit the hook files
themselves, so nothing local is load-bearing. What protects the repository is the set of checks required
before a merge, enforced where nothing local can reach.

**Depth runs on two axes.** What a mistake costs sets the apparatus — Light, Standard, High. How
well-trodden the work is sets the leash, and that one is asked per ticket.

**Six numbers, four about the loop and two about what came out of it.** Human intervention rate, ticket
wait time, review-agent dismissal rate, shortcuts taken, defects reaching a person, and how long
accepted work waits to go live.

**And the honest part.** Nothing here has run on a host. Every check is *written*, none is *proven*. Read
that word literally wherever you meet it, and never quote a *written* row to a client as a guarantee.

---

## Where to go next

**Setting up a new project** → [the runbook](12-runbook.md), with [the repository](07-repository.md),
[host and pipeline](09-host-and-pipeline.md) and [stack wiring](10-stack-wiring.md) open beside it.

**Joining a project that already runs this** → [why](01-why.md), then
[the build loop](04-build-loop.md), then [troubleshooting](13-troubleshooting.md).

**Scoping or selling work** → [why](01-why.md), [before build](02-before-build.md) for Solutioning and
Handover, and [depth](05-depth.md) to decide what the project needs.

**Deciding how delivery should work, and where it is going** → [agent-run delivery](16-agent-run-delivery.md).

**Deciding whether to believe any of this** → [limits](14-limits.md), then the evidence table in
[reference](15-reference.md).

**Something is broken** → [troubleshooting](13-troubleshooting.md).

---

## The documents

| | | Read when |
|---|---|---|
| [01](01-why.md) | Why this exists, and the five ideas | Once, before anything else |
| [02](02-before-build.md) | Stages 00–03: Solutioning to Setup | Starting a project |
| [03](03-delivery.md) | Stages 05–07: Release Check to Run and Support | Approaching a release |
| [04](04-build-loop.md) | The build loop and the three roles | Every ticket. The one developers live in |
| [05](05-depth.md) | Depth, novelty, and six project shapes | Scoping, and per ticket |
| [06](06-enforcement.md) | Every check, with its code | Setting up, or when a gate argues with you |
| [07](07-repository.md) | Every repository file | Standing a repository up |
| [08](08-templates.md) | Every template | Writing a spec, a decision record, a release |
| [09](09-host-and-pipeline.md) | Host settings, deploy and promote, the break-it suite | Setting up, once per repository |
| [10](10-stack-wiring.md) | Wiring the gates to your stack | Setting up, once per project |
| [11](11-measurement.md) | The six numbers | Day one, then monthly |
| [12](12-runbook.md) | The dated plan, and onboarding | Adopting this, and each new joiner |
| [13](13-troubleshooting.md) | Named failures and their fixes | When something goes wrong |
| [14](14-limits.md) | What this does not do and what we do not know | Before believing it, and before selling it |
| [15](15-reference.md) | Glossary, evidence, summary card | Lookups |
| [16](16-agent-run-delivery.md) | Agent-run delivery: the target operating model | Deciding how the delivery team should work |
| [17](17-artefacts.md) | The documents, and what happens to each | Unsure where information belongs, why a spec is written late, or why there is no learnings document |
| [18](18-outcomes.md) | What this changes against AI with no process, and what it costs | Asking a team to adopt it, or telling a client what they get |
| [19](19-first-run.md) | Choosing the first project, and what will go wrong | Before the first run, and before the demo |

Research in progress — sources, adjudicated findings, open questions and experiments — lives in
[`../research/`](../research/README.md). These documents are the conclusions; that folder is the
working-out.

If you want one file to search or print: `cat docs/*.md > /tmp/manual.md`.
