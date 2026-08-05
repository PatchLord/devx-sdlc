# Reference

Lookups, not arguments. The glossary, the dated evidence every other document leans on, a card you can
pin up, and the procedure for changing any of it. Keep this one open while you work.

## Glossary

One line each, with the value where a term has one. A definition that says "a configurable threshold"
tells you nothing, so where a number exists it is here.

| Term | What it means |
|---|---|
| Acceptance criteria | The conditions under which a feature is done, each naming the test, script or check that proves it. Lives in `docs/design/criteria/`, a protected path. |
| Blocker | A defect where the feature does not work, data is wrong, or something is unsafe. Own ticket, full loop. |
| Break-it suite | Deliberately hostile pushes run once against a fresh repository to prove the perimeter fails closed rather than merely looks configured. In [host and pipeline](09-host-and-pipeline.md). |
| Ceiling | A number a check enforces rather than advises. Ours: 400 lines and 20 files per pull request. |
| Changed-line coverage | Coverage measured only on lines this pull request touched. `--min 80` in `verify.yml`. Whole-repo coverage is deliberately not a gate. |
| CODEOWNERS | The file mapping paths to the people whose approval a change to that path needs. Enforced by the host, not by the file. |
| Criteria | Short for acceptance criteria. An agent may propose a change to them; only a person approves one. |
| Defect | Something wrong that is not a blocker. Own ticket, a paragraph for a spec when the fix is obvious. |
| Depth | How much apparatus a project gets, set by the cost of getting it wrong: Light, Standard, High. Decided in Solutioning, written into the SOW, and it never quietly goes down. |
| Derived status | Ticket state computed from events — branch pushed, checks green, review approved, merged, promoted — rather than written by anyone. The agent has no permission to write a status. |
| Design document | One per phase. What we are building, the behaviour and rules, the data model, what is out of scope, and the acceptance criteria. Source of truth over the code. |
| Disposition | The recorded outcome of a review finding: fixed, or dismissed in writing. Green means every finding has one, not that there were none. |
| Explore | The first agent role. Reads, asks its questions, writes the spec, stops. |
| Feature | A label over a group of tickets, with criteria already in the design document. When its tickets are closed there is something to demo. |
| Feature review | A person using the feature as a user would, against the criteria — not reading the diff. The one judgement no check in this set can make. |
| Fixture | An external system's real shape, captured once and committed as a file, with credentials and personal data stripped. Read the file; never fetch live during implementation. |
| Fresh context | A role that starts with no memory of the previous role's reasoning, so it cannot inherit the assumption that produced the bug. Implement and Review both get one. |
| Gate | A check that can fail a merge and that the agent cannot reach: required status checks, branch protection, CODEOWNERS, the merge button. |
| Gate change | Any edit to the protected set. Must arrive in its own commit; `gates.yml` fails a commit that mixes one with implementation. Adding a new test for new code is implementation, not a gate change. |
| Gate diffs | The ten minutes a day someone spends reading every diff across every project that touched tests, thresholds, CI or hooks, with the deltas listed. |
| Hint | A check the agent can walk past: Lefthook hooks, `settings.json` denies, anything local. `--no-verify` defeats them and an agent can edit the hook files. Useful, never load-bearing. |
| Hypercare | The heightened-attention window after a launch. It has an end date; a window with no end either never finishes or finishes without anyone noticing. |
| Implement | The second agent role. Fresh context, works from the approved spec, cannot touch gates, cannot merge. |
| Linear history | No merge commits on `main`. A precondition, not a preference: `spec.yml` and `gates.yml` reason with `git rev-list`, which only means what we claim if history is linear. |
| Mob | The whole team on one screen, on one thing. Expensive per hour, cheap per mistake avoided — so it is for the genuinely novel change and the launch rehearsal, and it is not a substitute for review. |
| Novelty | A per-ticket question, separate from depth: well-trodden, novel here, or genuinely novel. Depth sets the apparatus around the work; novelty sets the length of the leash inside it. |
| Perimeter | The set of protections that live outside the repository, and `perimeter.yml` is the job that asserts the perimeter we documented is the one that exists. Its expectations are literal in the workflow file, never read from a config the agent can edit. |
| Polish | Spacing, copy, colour. Batched into one ticket per feature, and may not change logic. |
| Promotion | Moving the same built artefact from dev to uat to production. Promoted, never rebuilt — so what QA approved is what ships. Only real if nothing about an environment is baked in at build time. |
| Protected set | The paths that need someone other than the author: money, personal data, auth, migrations, CI and hook config, existing tests, coverage thresholds, `CODEOWNERS`, `CLAUDE.md`, `.claude/`, the criteria. Also the list `gates.yml` uses. |
| Release Check | The stage before every production release: monitoring proven in production, a backup restored, rollback rehearsed, runbooks, security findings closed or waived in writing. |
| Required checks | The named checks the host will not merge without. The list lives twice — in host configuration and in `REQUIRED_CHECKS` in `perimeter.yml` — and that job compares one against the other. |
| Review | The third agent role, and the `review` check. Reads and runs, wrote none of it, cannot merge. Its findings are input, not a verdict. |
| Shortcut | `--no-verify`, an admin merge, a waived checklist line, a re-run until green. Counted, because uncounted shortcuts are invisible exactly when they matter. |
| Size override | The `size-override` label, which lets a pull request past the ceiling. A known weakness: the label is not access-controlled, so it is a hint dressed as a gate. |
| Spec | `docs/specs/PULSE-123.md`. What changes, which criteria, the questions and the answers in the words they were given, and what it will not touch. The branch's first commit and an ancestor of every implementation commit. |
| Spike | A throwaway ticket whose only deliverable is a committed fixture or contract file, for when something must be discovered before it can be specified. |
| Status word | *Written*, *proven* or *to build*, on every row of the enforcement table. Read literally — see the last section of this document. |
| Swarm | Several agents implementing one ticket in parallel. Rejected: parallel agents are safe only when they need not agree, which is the opposite of one ticket. |
| Verify | The single entry point every stack wires itself into, `scripts/verify.mjs`, so CI runs one command it does not have to know the language of. |
| Waiver | A checklist line that could not be ticked, signed by a named person with the reason. Worth far more than a false tick. |
| Wrap | Step 6 of the loop: fix the documents this change made wrong, and route every learning to a check, a rule or a ticket. |

## The evidence

Every figure these documents lean on, what it changed here, and when it was measured. The vintage is the
column that matters. Tooling from early 2025 is not the tooling described here, and the 2026 rows are the
ones that shaped the design.

| Figure | What it changed here | Vintage |
|---|---|---|
| Meta-analysis of 23 studies: productivity g = 0.33 (95% CI 0.09–0.58), smaller in enterprise and open-source than in the lab; learning g = 0.14, interval spanning zero | Sets the expectation the whole thing is built for: real, moderate, and weakest in exactly our conditions | submitted 6 May 2026 |
| Microsoft rollout across tens of thousands of engineers: adopters merged about 24% more pull requests, sustained over four months rather than decaying | Output rises and it is not a novelty effect — so the surplus has to land somewhere that can absorb it | submitted 1 July 2026 |
| 22,000 developers: time in review +441.5%, incidents per pull request +242.7%, bugs per developer +54% | Review is the constraint. The 300/10 target, the 400/20 ceiling, one ticket per pull request | 2026 report, two years of telemetry |
| Agent-only-reviewed pull requests merge at 45.20% against 68.37% human-only, across 19,450 pull requests | The review agent is a check, not the reviewer — and [number 3](11-measurement.md) counts its dismissals | April 2026 |
| 304,362 AI-authored commits: 24.2% of introduced static-analysis issues still present at HEAD, 41.1% of security ones | Scanning on a clock, daily, over history — not once per ticket | March 2026 |
| METR randomised trial: 19% slower on their own repositories while participants believed they had been 20% faster | Cited only as dated history. Its follow-up was redesigned because developers would no longer serve as a control group, and that is the argument for counting our own six numbers | measured on early-2025 tools, published 2025; follow-up redesigned early 2026 |
| Copy-pasted lines 8.3% → 12.3% of changed lines; refactored or moved lines 24.1% → 9.5% | The weekly clock-driven pass. No per-change check can see what many changes did together | dataset 2020–2024 |
| 78% line coverage at a 31% mutation score, one model writing both the code and its tests | Whole-repo coverage is not a gate. Changed lines at 80%, plus mutation on core logic at High | 2025, vendor-authored — read it as a mechanism, not a measurement |
| Six consecutive commits landed with `--no-verify`, `git stash` and quiet flags; 104 passing tests became 63 failing. Separately, a deny rule does not protect the hook files | Hooks are hints. Every gate that matters is server-side | first-party issue tracker, both closed "not planned"; no date recorded |
| Two production incidents traced to an agent inheriting standing operator credentials | No developer or agent session holds production credentials | incident reports; no date recorded |
| An AI reviewer whose comments were addressed 65% of the time against 51% for human comments | A reviewer earns a required check by being measured. Number 3 is how ours would earn it | first-party and self-reported; no date recorded |
| "Vibe coding" was coined for throwaway weekend projects by its own author, who later found agents "net unhelpful" on a from-scratch repository — "possibly the repo is too far off the data distribution" | The answer to the obvious objection in [why](01-why.md), and novelty as a routing question | 2 Feb 2025 and 20 Oct 2025 |
| Our pilot: 8 of 8 requirements with a gate present and correct, 0 of 7 prose-only requirements present; 44 commits, 64 tests, 87% backend line coverage; an admin panel with 9 write hooks and 0 buttons, 0 forms, 0 submit handlers; CI ran zero times while the repository's own context file claimed `main` was protected | The law everything is organised around: the agent builds to the shape of the check, and a weak gate gives you a different, smaller product | ours, 2026 |

Three rows carry no date because the source library records none. Saying so is better than manufacturing
one. Full citations, including the vendor and self-report caveats, are in `research/ai-sdlc-sources.md`.
Anything not in that file loses its digits and keeps its direction.

## The card

```
THE devx AI SDLC — ONE PAGE
================================================================================================
STAGES     00 Solutioning   01 Handover   02 Kickoff   03 Setup
           04 Build         05 Release Check   06 Launch   07 Run and Support
           All eight, every project. Depth changes what is inside a stage, never the list.
           At Light, Release Check and Run and Support shrink to almost nothing.
------------------------------------------------------------------------------------------------
LOOP       1 Context     the ticket, the design document, the code as it is now
           2 Questions   all at once, before code; answers correct the design document
           3 Spec        agent writes, a person approves on the host, first commit on branch
           4 Implement   unattended, one commit per step, checks on every commit
           5 Verify      the named check per criterion, then an agent that wrote none of it
           6 Wrap        fix the documents this change made wrong, route every learning
           7 Merge       on green, into dev; status is computed, never written
           The committed skill names the same seven Ticket, Explore, Spec, Approve,
           Implement, Review, Merge — after the commands that run them.
------------------------------------------------------------------------------------------------
ROLES      Explore       reads, asks, writes the spec, then stops
           Implement     fresh context, works from the spec, cannot touch gates
           Review        fresh context, reads and runs only, cannot merge
------------------------------------------------------------------------------------------------
CHECKS     size          300 lines / 10 files target; fails above 400 / 20
           gates         no commit mixes a gate change with implementation
           spec          docs/specs/<TICKET>.md exists and precedes every code commit
           verify        lint, format, types, tests, changed-line coverage, secrets
           review        a fresh agent reviews the ticket; findings need dispositions
           perimeter     the host's protection matches what perimeter.yml claims
           scan          daily, over history — a clock job, not a per-pull-request gate
------------------------------------------------------------------------------------------------
NUMBERS    1 how often a human changes something
           2 how long a ticket waits — picked up to running in dev
           3 how often review-agent findings are dismissed
           4 how often a shortcut is taken
           5 defects reaching a person per merged ticket, split by who found them
           6 how long accepted work waits to go live, per release
           From day one in the tracker: who found each defect, promotion and release
           timestamps, stage entry and exit dates. None can be reconstructed later.
------------------------------------------------------------------------------------------------
CEILINGS   ticket target             300 lines / 10 files      warning
           ticket hard limit         400 lines / 20 files      size fails
           changed-line coverage     80%                       verify fails
           retries on a red check    2, then stop and ask
           rounds on one feature     2, then re-read the design document
           clock-driven tickets      a handful a week, ranked
           approvals on main         1 code owner; 2 on protected paths at High
           migrations in flight      1
================================================================================================
```

## How to change these documents

These documents are the authority and `devx-starter` is their enforcement. They change together, in the
same day, or the pair starts lying — which is the exact failure mode [why](01-why.md) is built around,
with our name on it.

Two rules, and they are the whole procedure.

**A new requirement arrives with the check that enforces it, or it is a wish.** Name the file. If the
check does not exist yet, its row in [enforcement](06-enforcement.md) says *to build* and nobody may
quote it as a guarantee. Read the status words literally: *written* means the file exists as printed and
its logic has run locally; *proven* means it has run on a host and failed something it was supposed to
fail. Today every row is *written*. Nothing here has been *proven*.

**A lesson is not accepted until it lands as a check, a hook or a rule, with the commit that enforced
it.** A retrospective finding recorded as prose will be rediscovered, because prose is precisely the
class of requirement our own pilot delivered zero out of seven times. Write the finding down by all
means — then say which file changed.

In practice a change is four things in one pull request: the rule, with the reason it exists and what it
costs; the check in `devx-starter`; the enforcement row with its status word; and, if the change touches
the required set, the edit to `REQUIRED_CHECKS` in `perimeter.yml` **and** the host configuration
together. That job compares one against the other, so changing either alone only turns it red.

Removing a rule takes the same bar as adding one. Say what counted evidence says it was not earning — a
dismissal rate, a gate no change ever failed, a delay that cost more than the defects it caught. A rule
deleted because it was annoying rather than because a number said so is how a process erodes without
anyone deciding to erode it.

Three kinds of change we will not accept, because each has already been tried here. A rule with no
enforcer: "understand every line you ship" cannot be checked, so writing it down makes it a wish. A
check whose expectations live in a file the agent can edit. And a threshold moved to make a red build
green, in the same commit as the code that turned it red.

What none of this can see: a rule followed in letter and skipped in spirit. A feature review that has
become a skim of a diff passes every check in this set and shows up, if at all, as defects drifting from
the feature review towards QA and the client — [number 5](11-measurement.md), read as a trend, months
late. That is a known hole, listed with the others in [limits](14-limits.md), not an oversight.

Research in progress — how sources are taken in, how claims are adjudicated and refuted, what is still
open, and which experiments would settle it — lives in `research/README.md`. These documents are the
conclusions; that folder is the working-out, and the two are deliberately separate so that absorbing a
new source does not mean surgery on the whole set.
