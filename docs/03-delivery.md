# Delivery: Build, Release Check, Launch, Run and Support

This document covers the four stages that repeat for as long as a project exists. Read it if you are a tech
lead running a release or a cutover, a developer wondering what happens after your ticket merges, or a CSM who
needs to know what a client is being promised after go-live.

The four stages before these — Solutioning, Handover, Kickoff, Setup — happen once, and they are in
[before the build](02-before-build.md). These four do not. Build runs per ticket, Release Check per release,
Launch once per audience change, Run and Support continuously. Everything Run and Support discovers comes back
in as a ticket, which is why this is drawn as a loop and not a line.

```
  ┌─────────────────────────┐
  │ 04 BUILD                │  per ticket    · exit: running in dev, with evidence
  └────────────┬────────────┘
               │  merged tickets accumulate on main
               ▼
  ┌─────────────────────────┐
  │ 05 RELEASE CHECK        │  per release   · exit: every line evidenced or waived in writing
  └────────────┬────────────┘
               │  a tagged artefact, approved on uat
               ▼
  ┌─────────────────────────┐
  │ 06 LAUNCH               │  per cutover   · exit: live, verified, hypercare closed
  └────────────┬────────────┘
               │
               ▼
  ┌─────────────────────────┐
  │ 07 RUN AND SUPPORT      │  continuous    · no exit; a rhythm that decays if unattended
  └────────────┬────────────┘
               │  every bug, change request and learning
               └────────────────────────────▶ re-enters 04 as a ticket
```

Three separations in that picture are deliberate, and each exists because the merged version fails a specific
way.

**Build, test and deploy are one stage, not three.** Drawn in a row, that is what people do: build everything,
test it later, deploy at the end. Defects then surface when they cost the most. A feature that is not deployed
is not finished, so the clock on a ticket stops when it is running in dev, not when it is merged.

**Some checks belong to a release, not a ticket.** A load test, a restore drill, a threat model. Running them
per ticket is absurd; leaving them unassigned means nobody runs them. They get their own stage so they have an
owner and a date.

**Deploying and launching are different.** Deploying happens several times a week and should be boring.
Launching happens once — data moves, a domain switches, customers are told — and for anything replacing a live
system it is the riskiest hour of the engagement.

Each stage below has the same six parts: purpose, who, inputs, artefacts, exit criterion, failure modes.

## 04 Build

| | |
|---|---|
| **Purpose** | Turn one ticket into a change that is specified, built, checked, reviewed and running in dev |
| **Who** | The developer with the agent. The tech lead judges the feature running. A code owner reviews if the change touches a protected path. QA is not here — QA works on uat |
| **Inputs** | The ticket in Pulse; the design document for the phase, with its acceptance criteria; the shared surfaces, frozen in Setup; committed fixtures; `CLAUDE.md`; the loop files in `.claude/`; the code as it actually is |
| **Artefacts** | `docs/specs/<ticket>.md` as the branch's first commit; one commit per step; a pull request with the template filled in; a written disposition against every review-agent finding; the change deployed to dev by the pipeline |
| **Exit** | Every acceptance criterion met with a named artefact against it, `size` `gates` `spec` `verify` `review` all green on the final commit, code-owner approval if a protected path was touched, every finding resolved, and the change running in dev |
| **Failure modes** | In [the build loop](04-build-loop.md) |

Everything about how this stage actually runs — the seven steps, the three agent roles and what each may
touch, `/spec` and `/build`, ticket sizing and the 300-line target against the 400-line ceiling, what to do
when the agent is wrong, and the eight ways the stage breaks — is in [the build loop](04-build-loop.md). The
checks that enforce it, with their complete code, are in [enforcement](06-enforcement.md). The only thing
worth repeating here is the boundary: one ticket, one branch, one pull request, one merge, and the stage is
not over when the merge lands. It is over when the change is running in dev with evidence against every
criterion. Numbers 1 through 4 of [the six numbers](11-measurement.md) all originate in this stage, and number
2 measures picked-up to running-in-dev precisely so a merge that sits undeployed still shows as waiting.

## 05 Release Check

| | |
|---|---|
| **Purpose** | Build asked whether each feature is right. This asks whether the system can survive production and whether we can operate it |
| **Who** | The tech lead with QA. The CSM is told the outcome, in words the client can read |
| **Inputs** | The tag, the commit and the build id of the artefact QA approved on uat; the tickets in the release; the previous release file; monitoring output; the project's depth row |
| **Artefacts** | `docs/releases/<version>.md`, committed — one file per release, from the template installed in Setup; the restore record with its time; a runbook per alert; every waiver, signed with a name |
| **Exit** | Every line has an evidence link or a named written waiver, and the artefact being promoted is byte-for-byte the one that passed uat |
| **Failure modes** | Below |

**Most of this should already be running.** This stage reads results and decides. If somebody is building a
load-test harness by hand for the first time, that is a Setup failure surfacing late, not a Release Check
task.

Every release, regardless of depth: production runs the same infrastructure code as dev and uat. The build
released is the one QA approved — promoted, never rebuilt, because a rebuild makes the thing you tested and
the thing you shipped two different artefacts. The promote mechanism is in
[host and pipeline](09-host-and-pipeline.md). Monitoring proven *in production*: an error reaches the tracker,
a log line is searchable, an alert reaches a person. A backup taken and restored to a named place with the
time recorded, because that is the number a client asks for and the restore is the actual test — a backup
nobody has restored is a belief. Rollback rehearsed, stating whether this release contains a schema change and
which case was rehearsed, because rolling code back is not rolling data back. A runbook for every alert.
Security findings fixed or waived in writing.

Then whatever depth requires: a load test against the numbers in the design document, a threat model or
penetration test, accessibility and performance budgets, a data migration dry run. At Light this whole stage
is skipped. At Standard it is the standing list. At High it adds the load test, the threat model and the
restore drill. The rows are in [depth](05-depth.md).

The file itself is `docs/release-checklist.md`, copied to `docs/releases/<version>.md` per release; it is
inlined in [templates](08-templates.md). Three rules make it worth having, and all three are about honesty
rather than completeness.

**Three columns, and the third is not optional.** Item, how it was verified, link to the evidence. Nobody
writes *verified* as prose. "Verified" in the middle column with an empty third column means nobody checked,
and it is the most common way a checklist becomes decoration. The nine standing items are the ones a release
can plausibly break: the artefact identity, migrations forward, migrations back or documented as one-way, the
acceptance criteria for every ticket, the paths a user actually takes, dashboards for what changed, secrets
and config in the target environment, third-party quotas, and rollback tested rather than assumed.

**Lines are marked as each thing is done, not in one sitting before go-live.** A restore drill cannot be
started and finished inside a launch window. A checklist filled in top to bottom on the morning of the release
is a record of somebody's confidence, not of any work. The same applies to the three timestamps at the head of
the file — client acceptance, promotion to uat, promotion to production. Number 6 is computed from them and
cannot be reconstructed once the pipeline runs age out, so they are filled in as each event happens or they
are lost.

**A line that cannot be ticked is waived in writing by a named person.** An honest waiver is worth far more
than a false tick. The waiver survives into the incident three weeks later, where it tells whoever is on call
what was never checked — and the "what this release does not verify" section exists for exactly that reader.

**The first release is bigger than the rest.** Production gets stood up, the first restore is drilled, the
first runbooks are written, the load-test numbers get a baseline. Later releases re-check only what the change
could have affected. Planning the first release as if it were a later one is how the restore drill gets pushed
past go-live and then never happens.

Failure modes: the artefact is rebuilt for production rather than promoted, so what shipped is not what QA
approved; rollback is documented as "redeploy the previous version" rather than as the exact command and who
may run it; a schema change ships with a code rollback rehearsed and a data rollback assumed; a waiver appears
with no name against it; the checklist is written into a wiki page instead of `docs/releases/`, so no release
can be compared to the last one. And one this stage genuinely cannot see: it verifies that the system survives
the load and the failures we thought of. Nothing here catches a class of failure nobody listed. That limit is
recorded in [limits](14-limits.md) rather than hidden.

## 06 Launch

| | |
|---|---|
| **Purpose** | Change who is exposed to the system, once, in a rehearsed window |
| **Who** | The tech lead with the CSM |
| **Inputs** | The signed release checklist; the migration dry run; the URL map; the comms the CSM has agreed with the client; the rollback trigger numbers |
| **Artefacts** | A runsheet with each step, its checkpoint and its owner; the go/no-go decision with a name and a timestamp; migration verification counts and spot checks; promotion and release timestamps; a hypercare end date, and a written note when it closes |
| **Exit** | Live, verified against the numbers agreed beforehand, hypercare run to its end date and closed in writing |
| **Failure modes** | Below |

Launch fires when the audience changes, not when the code changes. Once for a new product; once per cutover.

**Everything that can be decided in advance is decided in advance**, because the launch window is the worst
moment in a project to decide anything: there is time pressure, the client is watching, and turning back feels
like personal failure. Agreed and written down before the day:

| Decision | Agreed before the day |
|---|---|
| Go or no-go | Who calls it, judged against the signed checklist rather than a feeling |
| Rollback trigger | In numbers — error rate, p95 latency, a failed checkout — and who calls it without asking anyone |
| Order of operations | Every step with a checkpoint after it |
| Cover | Who is awake, for how long, and how to reach them |
| Comms | What customers and support are told, by whom, and when |
| Freeze | What is frozen, from when, and how it is enforced |

A freeze that is only announced is not a freeze. Ours is enforced the same way everything else is: branch
protection stays on, `allow_force_pushes` and `allow_deletions` remain false, and no session — human or agent
— holds production credentials. The settings are in [host and pipeline](09-host-and-pipeline.md). The reason
is on record: the Replit agent deleted a production database *during a declared code freeze*, then fabricated
4,000 user records and claimed rollback was impossible. Announcements do not constrain agents. Scoped
credentials do.

For a cutover, three more things, and this is where most of the risk actually lives.

**The migration is run and verified** — row counts, spot checks, and a person reading the records that matter.
Counts alone confirm that rows arrived, not that they are right.

**The old system stays up.** For a cutover, the real rollback is pointing the domain back, and that only works
if the thing it points to is still running. Tearing it down on launch day converts a five-minute rollback into
a restore. Decommissioning is a separate decision on a separate date, after the system has run without
incident for a period the client agreed to.

**The URL map with its redirects**, and the top pages checked after the switch. For a store, lost rankings are
lost revenue, and the loss is slow enough to notice that it is usually the client who notices it.

A cutover runsheet looks like this — times relative to the window opening, one checkpoint per step:

```
  T-0    freeze              ──▶  last commit id recorded, all five checks green on it
  T+10   migration           ──▶  row counts match source, 20 records read by a person
  T+25   domain switch       ──▶  new system serving, old system still running and reachable
  T+35   redirect check      ──▶  top 50 URLs return 200 or 301, none return 404
  T+45   smoke               ──▶  one real login, one real order, one real refund path
  T+60   go / no-go          ──▶  go: customers and support told · no-go: point the domain back
```

Then hypercare, **and it has an end date**. A window with no end either never finishes or finishes without
anyone noticing, and the difference matters commercially: hypercare is staffed, and support may not be sold at
all. It closes with a written note saying what happened during it and what landed as a permanent check.

Failure modes: a decision that should have been pre-agreed gets made inside the window; go is called on a
feeling rather than against the checklist; the old system is decommissioned the same day; the URL map exists
but nobody checks it after the switch; support hears about the launch from a customer; hypercare quietly turns
into unpaid indefinite support.

## 07 Run and Support

| | |
|---|---|
| **Purpose** | Keep a live system from decaying, and route what production teaches back into the process |
| **Who** | The tech lead with the CSM. Someone on call where depth is High |
| **Inputs** | Alerts and error trends; dependency pull requests; scanner output; cost reports; the runbooks; client-raised issues |
| **Artefacts** | Tickets — every bug and change request goes through Build like everything else; new runbooks; new checks; commits to the starter repository; the monthly report to the client |
| **Exit** | None. This is a rhythm, and the only honest end is the end of the contract |
| **Failure modes** | Below |

Nothing that goes wrong here is dramatic. Dependencies fall behind, costs drift, alerts get ignored, documents
go stale, anything vendored moves on without us. **A live system decays unless something actively resists
it.**

What this stage contains depends on what was sold. If nobody is paying for support, go-live is a handover, and
we say that out loud at go-live rather than discovering it when the first alert fires at 2am.

| | |
|---|---|
| **Daily** | Alerts answered. The board moved by real events, not by anyone's assertion |
| **Weekly** | Dependency pull requests merged. Error trends read — the trend, not the count, and one hour converting the week's repeated corrections into checks |
| **Monthly** | Costs reviewed. A report to the client. Runbooks checked against reality |
| **Quarterly** | Restore drill repeated. Vendored dependencies given a decision. Depth re-checked |

**An alert that fires and gets ignored is fixed or deleted.** There is no third option. An alert nobody acts
on trains everyone to ignore the next one, and a stack full of those is worse than no alerting because it
looks like coverage. "Fixed" means the threshold moved to a value with a reason written next to it, or the
underlying condition was resolved. "Deleted" means the alert is gone and we know we are not watching that.
Both are honest. Leaving it firing is not.

**Scanning runs on a clock, not once.** Across 304,362 AI-authored commits, 24.2% of introduced
static-analysis issues were still present at HEAD, and security issues persisted worst at 41.1%. A scan at
merge time sees the commit in front of it. A scheduled scan sees what accumulated. The scheduled job is
`scan.yml` in [enforcement](06-enforcement.md).

**The loop closes here, as a check and not as a lesson.** What production teaches goes to one of four places:
a check, a runbook, the design document, or the starter repository so the next project inherits it. A lesson
is not accepted until it lands somewhere with a commit reference. This is the same rule the process applies to
itself — a new requirement arrives with the check that enforces it, or it is a wish. We rejected writing down
"understand every line you ship" for exactly this reason: it is unenforceable, so putting it in a document
makes it a wish with official standing. The cost of not closing the loop is documented too. An AI-built
backend shipped with no authorization policies at all, exposed roughly 72,000 images including 13,000
government IDs, and then exposed 1.1 million private messages months later. The first incident did not force a
structural fix.

Number 6 of [the six numbers](11-measurement.md) lives here: how long accepted work waits to go live, per
release — from the demo where the client accepted a feature to the release that put it in production, with the
stage it sat in recorded. It is the only number that can see the failure this whole process is exposed to,
which is that a faster typist in the middle of a sequence does not make the sequence faster. Every other
number stops before the part that would absorb the gain. The current headline evidence says the gain is real
but conditional: a May 2026 meta-analysis of 23 studies puts productivity at g = 0.33, 95% CI 0.09 to 0.58,
and explicitly smaller in enterprise and open-source settings than in the lab.

Three fields must be in the tracker from day one, because they cannot be reconstructed afterwards: **who found
each defect** (number 5 is meaningless without the split), **promotion and release timestamps** (number 6 is
computed from them), and **stage entry and exit dates**. Until the Pulse integration exists, a tech lead
records them by hand. If anything is cut for time, cut it from the gates and not from the counting. A gate we
have not built is a known absence. A number we never started counting is an answer we cannot get back.

Failure modes: alerts accumulate unacted-upon until the stack is decoration; dependency pull requests pile up
until upgrading is a project; runbooks describe a system that no longer exists; costs are noticed on an
invoice; something vendored is frozen by neglect rather than by decision; a production bug is fixed directly
on the environment instead of as a ticket, which puts main and production out of sync silently; and support
that nobody is paying for gets absorbed by whoever answers first. Named symptoms with their fixes are in
[troubleshooting](13-troubleshooting.md).
