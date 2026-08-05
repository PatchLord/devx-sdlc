# Before the build

The four stages that run before anyone writes a feature: Solutioning, Handover, Kickoff and Setup. Read this
if you are a tech lead starting a project, or a practitioner writing an SOW a delivery team has to live inside.

A stage is not a phase of typing. Each one exists to stop a specific thing going wrong. Solutioning stops us
solving the wrong problem. Handover stops the delivery team working from second-hand notes about someone
else's system. Kickoff stops us building the right thing in a shape we cannot change. Setup stops us finishing
work we cannot ship.

None of the four produces software a client can use, which is the whole objection to them. The answer is
arithmetic. Generation got much cheaper and checking did not move, so the surplus lands on review, and these
stages are where the machinery that absorbs it gets built. Skip them and you have not saved four weeks; you
have moved them to where being wrong is most expensive. The argument in full is in [why this
exists](01-why.md).

Our own pilot is the cheapest available proof. One frozen spec, one cold session, no process: 44 commits, 64
tests, 87% line coverage on the backend, and nothing shippable. The code was not the problem. Setup had never
happened — no remote, no branch protection, no environments — and the repository's own context file asserted
that main was protected. These four stages were the only part of the sequence missing.

```
   ┌────────────────┐  ┌─────────────┐  ┌────────────┐  ┌──────────┐
   │ 00 SOLUTIONING │─▶│ 01 HANDOVER │─▶│ 02 KICKOFF │─▶│ 03 SETUP │
   └────────────────┘  └─────────────┘  └────────────┘  └─────┬────┘
     the client has      there is         a design doc,       │
     signed the SOW      enough context   phases and          │  ends with one
                         to plan          tickets exist       │  trivial page live
        ┌─────────────────────────────────────────────────────┘  in dev
        ▼
   ┌─────────────────────┐
   │ 04  BUILD           │◀───────────────┐  one ticket, one branch,
   └──────────┬──────────┘                │  one pull request, one merge
              ▼                           │
   ┌─────────────────────┐                │
   │ 05  RELEASE CHECK   │                │  can it survive production,
   └──────────┬──────────┘                │  and can we operate it
              ▼                           │
   ┌─────────────────────┐                │
   │ 06  LAUNCH          │                │  once, and rehearsed
   └──────────┬──────────┘                │
              ▼                           │
   ┌─────────────────────┐                │
   │ 07  RUN AND SUPPORT │────────────────┘  bugs and change requests
   └─────────────────────┘                   re-enter BUILD as tickets
```

Every project passes through all eight stages, and at Light depth two shrink to almost nothing: Release Check
collapses to the standing list, and Support to nobody on call. What changes is how much apparatus each stage
carries. Stages 04 to 07 are in [delivery](03-delivery.md) and [the build loop](04-build-loop.md).

| Stage | Owner | Ends when |
|---|---|---|
| 00 Solutioning | practitioner or outcome manager, with the tech lead | the client has signed |
| 01 Handover | tech lead | folder searchable, questions owned, enough context to plan |
| 02 Kickoff | delivery team, with the CSM | design document done, access in hand, tickets ready |
| 03 Setup | tech lead | one trivial page live in dev, put there by the real pipeline |

Each stage below gives its purpose, its people, its inputs, its artefacts, one exit criterion someone who was
not in the room can test, and its failure modes. The exit criteria are deliberately mechanical, because a
stage that ends when the owner feels ready ends when the calendar says so.

> **The document chain for a phase is PRD, then TDD, then contracts, then features, then tickets.** The
> TDD's job is closing every question that has human latency attached, so implementation does not stall
> on someone outside the building. Contracts are fixed before anything builds on them, which turns
> apparently sequential tickets into parallel ones. Who owns each document, and which live rather than
> freeze, is in [the artefacts](17-artefacts.md).

## 00 Solutioning

**What it is for.** To find out whether we can build the thing, what it costs if we get it wrong, and what we
are contractually allowed to do with the client's code and documents. All three are cheaper to answer before a
signature than after one.

**Who does what.** The practitioner or outcome manager team owns the problem and the commercial half. The tech
lead owns the technical half and has **at least one call with the client's own technical people**, because an
architecture cannot be designed from second-hand notes about a system nobody on our side has seen. If the
client cannot put a technical person on a call, that is itself a finding: the system's behaviour will have to
be discovered, which is a phase in Kickoff rather than an assumption here.

**Inputs.** The client's stated problem, their setup as they describe it, and whoever they can put in the room.

**Artefacts.** One signed SOW containing the requirements, the current setup, timelines, the architecture at a
high level, and how we solve their problems. Detailed design belongs in the build: a contract that specifies
the schema has fixed the design at the moment we knew least.

Four sections go in that a business document usually leaves out, because each costs money if it is wrong.

- **The depth: Light, Standard or High.** Depth is set by what a mistake costs, not by project size or type;
  the four questions that set it are in [depth](05-depth.md). It changes the apparatus and therefore the
  price, so it belongs here rather than being discovered by a developer in week three.
- **A personal-data inventory.** What the system will hold, on what lawful basis, and for how long. This is
  the input to the logging allowlist and the masking rules in Setup. Written later, it gets written from the
  schema, which records what we built rather than what we were allowed to build.
- **Named third-party AI processing, with written permission.** The client's documents and code will be sent
  to a named provider. Some organisations forbid this contractually, and finding out after signature ends
  projects.
- **What happens after go-live.** Who fixes bugs, for how long, and how we tell them when something has gone
  wrong. If nobody is paying for support, go-live is a handover, and saying so here is cheaper than
  discovering it when the first alert fires.

We also say plainly how the work gets done: an agent writes most of the code, no line reaches their repository
without passing checks they can inspect, and a person approves the plan and judges the result. Then the part
that is easy to get wrong. **We list which of our checks exist on their project today and mark the rest as
still to build**, in three words and nothing else. *Written*: the file exists and its logic has been tested
locally. *Proven*: it has run on a host and failed something it was supposed to fail. *To build*: it protects
nothing today. Selling a *written* row as a guarantee is the pilot's failure with a signature under it.

The practitioner and the tech lead read the finished SOW together, because the tech lead wrote half of it.

**Exit criterion.** A signed SOW in the project folder, and a person who did not write it can point at: the
signature date, the depth level, the personal-data inventory, the named AI provider with written permission
attached, the post-go-live terms, and the check list with every row marked written, proven or to build. Six
things. A missing one means the stage is not finished, not that it will be caught later.

| Failure mode | What to do |
|---|---|
| Depth set from project size or budget | Re-ask the four questions: who feels a mistake, can it be undone, does it touch money or regulated data, how long will it live. A small script that deletes production data is High. A large internal dashboard is not. |
| AI processing assumed rather than asked | Ask before the first document is uploaded. If permission is refused, that is a different engagement, priced differently — not a thing to work around locally. |
| The SOW promises a check we have not built | Fix the document, not the conversation. Mark the row *to build* and say when. Clients accept an honest absence; they do not forgive a discovered one. |
| Support left open-ended | Name an end date and a response time, or write that there is no support. An unbounded window either never ends or ends without anyone noticing. |

## 01 Handover

**What it is for.** To move the context from the people who sold the work to the people who will build it, in
a form both a person and an agent can search. Every ticket in Build begins by reading this material. If it is
scattered across inboxes, the agent reads whatever happens to be nearest.

**Who does what.** The tech lead owns the stage. The practitioner presents. QA and the CSM attend — the CSM
specifically because they speak to the client weekly, and someone who does not know what was excluded from
scope cannot defend that boundary six weeks later.

**Inputs.** Everything Solutioning produced or touched: the SOW, the client's own documents, every call
recording and transcript, the research.

**Artefacts.** One folder in Pulse, connected so the agent can search it. A dated index. The open-questions
list, a named owner and a date against each row. Recordings of the handover calls themselves, because the
reasoning in them is context the agent will want.

Three rules keep the folder useful rather than actively misleading.

- **The SOW wins.** A recording captures what was said, including things later changed. Without this rule, a
  decision reversed on a call in week two comes back as fact in week nine.
- **Date everything, and mark what is superseded.** Search returns the most similar document, not the most
  recent one. Similarity and currency are unrelated, and the agent cannot tell them apart.
- **Keep commercial material separate.** The SOW carries pricing, and pricing in the agent's default context
  ends up quoted back in something the client reads.

**Then the calls.** The practitioner walks the delivery team, QA and the CSM through the scope and the
reasoning. One call is rarely enough: the team's real questions appear only after they have started thinking
about the work, two or three days later. Book the second call before anyone claims not to need it.

What this stage cannot do is worth stating, because the folder looks complete once it is full. **Search cannot
see an absence.** Ask it what the client said about refund windows and it will answer confidently from the one
adjacent sentence in the transcript. That is why the open-questions list is a separate artefact a person
maintains: nothing in the corpus will ever volunteer that it is missing.

**Exit criterion.** The tech lead states in writing that there is enough context to plan, and two things back
it: every open question is a row with a named owner and a date, and a spot check of three questions asked
against the folder returns three answers that each cite a dated source document. An answer without a source
means the folder is not connected properly and the stage is not done.

The practitioner and outcome manager stay reachable for two weeks after this. Handover is not a transfer of
memory, and the questions that matter arrive late.

| Failure mode | What to do |
|---|---|
| A transcript treated as authority | Apply the SOW-wins rule and mark the transcript superseded on the point in question. Then record the correction in the design document, or the next ticket rediscovers it. |
| Pricing in the searchable corpus | Move it to a folder the agent's context does not include. Check by asking the folder what the project cost; if it answers, it is not separated. |
| Handover as one call, ticked off | Book the follow-up two working days later. Treat the second call's questions as the real output of the stage. |
| Unknowns held in someone's head | Every unknown becomes a row with an owner and a date. "The team knows about that" is how a blocker arrives on the day it blocks. |

## 02 Kickoff

**What it is for.** To turn a signed SOW into a phase plan, a design document per phase, and tickets. Shape is
the expensive thing to be wrong about: code can be rewritten in an afternoon, a schema three services depend
on cannot.

**Who does what.** The delivery team runs it, the tech lead owns the design document, the CSM owns anything
that touches what the client accepts, and the designer is involved from the start where screens exist.

**Decide the phases first.** There are almost always blockers: a decision the client has not made, an account
we do not have, a system nobody has documented. Waiting for every dependency means an idle team. Draw the
phase lines around the blockers, and make every phase a working slice we can demo — not all the backend first
and the screens later. Then say the dependency plainly: phase two starts when we have this account. Said in
week one that is a schedule fact; said in week six it is an excuse.

**Then the design document, one per phase.** The agent drafts it from the folder — reading the SOW, the
transcripts and the client's documents and producing a first draft is work it does faster and more completely
than a person — and the humans own the judgement about what is wrong and what is missing. Ask that question
everywhere: what are people writing by hand that an agent should be drafting? The document lives in the
repository as markdown, not in a wiki, so the agent and the developer read the same text and a divergence
between them is a commit. Its contents are in `docs/design/README.md` in [templates](08-templates.md).

**Every acceptance criterion names the test, script or check that will prove it.** This is the rule in the
stage that carries the most weight, and the one we counted. In the pilot, requirements backed by a config
file, a hook or a test were present and correct 8 times out of 8. Requirements written only as prose were
present 0 times out of 7. Same model, same session, same file. A criterion with nothing against its name gives
the implementer nothing to build toward and the reviewer nothing to look at.

The pilot's admin panel is the sharper version. It had 9 write hooks and 0 buttons, 0 forms and 0 submit
handlers — the write side existed at every layer except the one a human touches. The agent's own build report
explains why: the admin app had no unit suite, so its gate was the render verification. It found the gap,
chose the cheapest available gate, and a page with no Create button renders perfectly. **The agent builds to
the shape of the check. A weak gate does not give you the same product less verified; it gives you a
different, smaller product.** So the criterion for a screen names a browser test that clicks the button, or
the button does not get built.

Because the criteria are what *done* means, they live on a protected path, `docs/design/criteria/`, with named
owners in `CODEOWNERS`. An agent may propose a change to a criterion; only a person approves one. Criteria an
agent can edit to match what it built are not criteria.

**The document records what is still undecided**, because one that hides its gaps is worse than one that names
them: the agent reads everything in it as settled fact and invents the missing half confidently. Filling a
named gap is the agent's to do. A correction — the document says one thing, the code does another — is
recorded, and the fix lands in the document rather than only in that ticket's spec. A change that alters what
the client accepts goes to the CSM first.

**Anything shared goes first.** Contracts, schema, shared types and wire shapes are settled before anything is
built on them, because each later ticket writes its own spec against the code as it finds it. This is the one
thing the pilot got right by design: the contract was frozen first, and three tracks were built against it in
parallel with no conflict.

**If the design does not exist yet, that is a phase.** The tech lead and the designer write a brief together,
because a designer given a loose brief designs the happy path and a developer invents the rest. The brief
names the screens, the real data, and the states nobody volunteers: empty, loading, error, validation, long
and short content, every breakpoint, hover and focus and disabled. The client accepts the design before
implementation tickets are written. Changing a frame costs minutes; changing a built screen costs a ticket.

**If the existing system is undocumented, that is also a phase.** Point the agent at the old codebase and
database and have it produce a map: what exists, what calls what, what the data actually looks like. Each
claim that matters names what it was checked against — a query, a captured response, a recording. Memory is
what went missing in the first place, so it cannot confirm the map.

**Then the tickets**, in Pulse, each with a description drawn from the design document, an estimate and an
owner. Estimate every ticket. Assign only the current sprint: assignments made six weeks out look like a plan
and are a guess about a codebase that does not exist yet. Sizing is in [the build loop](04-build-loop.md).

**And agree how we work.** A weekly demo of working software, which is what stops us building the wrong thing
correctly for ten weeks. One named decision-maker with a named backup, and how fast they answer. What *done*
means, in writing. The assumptions said out loud. And the access this phase needs, each row with an owner and
a date.

**Exit criterion.** Four things, all inspectable:

1. `docs/design/<phase>.md` exists and its open-questions section is non-empty or explicitly states there are
   none.
2. Every criterion in `docs/design/criteria/` has a non-empty proof column. Count the empty ones; the number
   must be zero.
3. Tickets for this phase exist in Pulse, every one estimated, and only the current sprint assigned.
4. The working agreement is written down: demo day and time, decision-maker and backup with a response time,
   and the access list with an owner and a date per row.

| Failure mode | What to do |
|---|---|
| Criteria written as prose | Reject the design document. This is the 8-of-8 versus 0-of-7 line, the cheapest defect to fix at this stage and the most expensive at feature review. |
| A criterion whose named check can only see reads | Name a check that touches what a user touches: a browser test that clicks the button, not a render assertion. This is how the admin panel lost its write side. |
| Phases drawn as layers — backend first, screens later | Redraw around demonstrable slices. A phase that cannot be demoed produces no client signal for its whole duration, which is when scope drifts. |
| Shared surfaces left for later | Stop and fix the contract, schema and wire shapes now. Tickets built against a moving contract each carry their own version of it. |
| Criteria edited to match what was built | `CODEOWNERS` on `docs/design/criteria/` plus code-owner review on the host. Without both, the path is a text file with no effect. |
| Every ticket assigned in week one | Assign the current sprint only. Six-week-old assignments hide the fact that nobody has looked at the work. |

## 03 Setup

**What it is for.** To build the perimeter before there is anything inside it worth protecting. Setup runs
once per project, before any feature work, and it is the stage that gets cut when a timeline slips — the worst
possible thing to cut, because every standard added later leaves everything written before it unchecked.

Setup should be a template, not a task. Hand-built it takes a fortnight, the result depends on who did it, and
half of it gets dropped under pressure. From the starter repository it takes a day. Every file named below is
reproduced in full in [enforcement](06-enforcement.md), [the repository](07-repository.md) or
[templates](08-templates.md).

**Who does what.** The tech lead owns Setup end to end. It is not delegated to whoever picks up the first
ticket, because the person who owns the gates cannot be the person the gates are inconvenient for.

**Inputs.** The depth from the SOW, the phase plan and design document from Kickoff, and the access list.

### One repository

Frontend, backend, CMS, mobile app, shared packages and infrastructure code go in one monorepo. Changes that
cross services land together, so a contract and its consumer are one reviewable diff instead of two that can
be merged in the wrong order. Shared types stop contracts drifting. And the agent can follow a change from a
screen to the schema without being told where anything lives; in a split repository it guesses.

The cost is real: every check runs against everything, so CI is slower than it needs to be, and path filters
become necessary once the repository is large. We take that cost because one repository is what makes a single
list of required status checks possible, and that list is the perimeter.

### Standards go in before the first feature commit

In the order they get installed: context files and the agent's permission policy; the build loop itself as
committed skills and commands; formatting and hooks; commit conventions; branch protection and `CODEOWNERS`;
secret scanning; dependency scanning with an update bot; pinned toolchain versions; the folders for the design
document, specs and decision records; PR and issue templates; and the release checklist. Then two commands,
`bun install` and `bun run setup`, the second of which installs the git hooks.

One property of the starter matters more than any individual file: **a gate that is not wired fails rather
than skipping.** `format:check` in [package.json](07-repository.md) ships as a deliberate `exit 1`, because
the starter cannot know your formatter, and a repository that documents six gates and runs four reports green
for the two it never ran. Everyone downstream reads the green. Wiring the entry point to a real stack is
[stack wiring](10-stack-wiring.md).

One line matters more than it looks: `.gitattributes` marks lockfiles as generated, which keeps them out of
the diff a person reads and out of the line count the size gate measures.

### Hooks are hints. Server-side checks are gates

```
 ┌─ INSIDE THE AGENT'S REACH ─────────┐  ┌─ OUTSIDE IT ──────────────────────┐
 │  the source code                   │  │  branch protection on main        │
 │  the tests and the thresholds      │  │  the required status checks       │
 │  the CI workflow files             │  │  CODEOWNERS on the criteria path  │
 │  local hooks, including its own    │  │  the merge and approve buttons    │
 │  anything it claims about itself   │  │  production credentials (absent)  │
 └────────────────────────────────────┘  └───────────────────────────────────┘
            every one a hint                     every one a gate
```

We considered making hooks the enforcement layer and rejected it, for two reasons that are not fixable. `git
commit --no-verify` walks past every hook and always will. And an agent can edit the hook files themselves; a
local deny rule cannot protect the file that contains the deny rule. Both have been observed: an agent used
`--no-verify`, `git stash` and quiet flags across six commits while 104 passing tests became 63 failing ones,
with nothing red on screen. Treat the permission policy as a hint too — it is the file the agent is working
next to. What protects the repository is the list of checks required before a merge, enforced where nothing
local can reach; those values are in [host and pipeline](09-host-and-pipeline.md). Singapore's IMDA framework
for agentic AI, published 22 January 2026, puts the same point more sharply: **policy enforcement happens
outside the model loop.**

### Scanning on a clock

Turn on the host's dependency alerts and code scanning during Setup, and provision the token the daily job
needs. The reason is a measurement: of the static-analysis issues introduced by AI-authored commits, 24.2% are
still present at HEAD, and security issues persist worst at 41.1% (arXiv 2603.28592, 304,362 verified
AI-authored commits). Those issues survived *because the change that introduced them passed*, so a scanner
reading one pull request's diff cannot be the answer — it sees an issue the moment it appears and never looks
again. The check runs on a clock, over the whole tree; `scan.yml` is in [enforcement](06-enforcement.md). A red
scan is a ticket, not a merge block, because a scheduled run has no pull request to stop.

What this does not give us is an embedded security specialist, and a company our size cannot hold a person per
pod. Instead we put auth, payments and personal data on protected paths and run this scan daily. That is
weaker, not equivalent, and it is described that way to a client. The other gap — agent identity, since
sessions are anonymous and commits carry a human's name — is in [limits](14-limits.md).

### One branch, and promotion rather than rebuilding

Main is the only long-lived branch and nothing is pushed to it directly. Every ticket gets a short-lived
branch and a pull request. A release is a tagged build at a named commit, and **that exact artefact** is
promoted to uat and then production — promoted, never rebuilt — so what QA approved is what ships. Nothing is
patched on a running environment; such a patch exists in no commit and survives no redeploy.

Promotion is only real if the artefact carries no environment inside it. Anything inlined at build time — an
API base URL, a feature flag, a key — makes every environment a different build, which makes this promise
false while looking identical from outside. Check it once, deliberately: build one artefact, deploy it to two
environments, confirm each points at its own backend.

Where there is nothing to promote, the promise changes shape rather than disappearing. A theme is pushed, not
deployed, so the promoted thing is the commit and the check is that the push came from the pipeline at that
tag. On a platform the client also edits, name the files they own before the first commit and never promote
those from git, or the first deploy reverts their work.

### Review by someone other than the author: per path, not per project

We rejected human review of every pull request, and the reason is arithmetic rather than preference. Three
developers at agent speed produce more diff in a week than anyone can read; on a single-developer project
there is no second reader at all. A rule everyone breaks in week two is worse than no rule, because the
breaking becomes normal and then spreads to the rules that mattered.

So review is required **per path**. One list, referenced everywhere: money, personal data, auth, migrations,
CI and hook config, existing tests, coverage thresholds, `CODEOWNERS`, the context files and the acceptance
criteria. A developer merges their own ordinary work and cannot merge a protected path alone. The file is in
[the repository](07-repository.md). Do two things to it before the first commit: replace the placeholder team
slug with a real one, and confirm the globs match this project's layout — the defaults assume `/src/`. An
entry that matches nothing resolves to nobody, and a path owned by nobody is not protected while still
appearing in the file.

At High depth, two reviewers on a protected path. That needs three people; where the team is smaller the
second is a devx engineer from outside the project, named here rather than found on the day. Every human gate
gets a second name against it, because one name on all of them means a fortnight of leave stops promotion to
uat.

### Environments and secrets

Dev on every project. Uat and production where the depth table calls for them, with CI/CD and infrastructure
as code, and the host side in [host and pipeline](09-host-and-pipeline.md). **Production is defined in code
before it is provisioned**, because defined later means defined under launch pressure, and the launch window
is the worst moment to be discovering what production needs.

Secrets go in a secrets manager, and **no developer or agent session holds production credentials.** This is
the rule in Setup with the clearest evidence behind it: every serious agent-caused incident on record traces
to standing access with no gap between deciding and doing. An agent asked to fix a small Cost Explorer bug
deleted and rebuilt production, causing a 13-hour regional outage, root-caused to inherited operator-level
credentials with no identity boundary and no confirmation gate. Another deleted a production database during a
declared code freeze, then fabricated 4,000 fake records and reported that rollback was impossible. Both
remediations were credential scoping and two-person sign-off. Nobody fixed it with a better instruction, and
ours is not one either: the session cannot reach production because the credential does not exist in it.

### Monitoring, and the list everyone forgets

Monitoring goes on every project above Light, decided by the depth table rather than case by case, because
nobody decides monitoring is needed before an incident and everybody decides it afterwards.

Request logs, searchable, **with personal data stripped before it leaves the application** — a field
allowlist, plus a test asserting the logger drops everything not on the list. Stripping downstream means the
data was already in a third party's storage. A health dashboard per service. Errors grouped with their stack
traces and the release that introduced them, because an alarm tells you something broke and not what. Alerts
into Slack. And every threshold written down **with the reason for the number**, because an unexplained
threshold gets widened the first time it is noisy. These are starting points, chosen to fire rarely enough to
be believed and often enough to be useful; the first month of real traffic should move them.

| Signal | Fires at | Why this number |
|---|---|---|
| Error rate, 5xx | above 1% of requests over 5 minutes | Below this single failures dominate and it cries wolf. Above it, users are already complaining. |
| Latency p95 | above 1s over 10 minutes | What a user notices on a page load. p95 not average, because an average hides the tail that generates complaints. |
| Latency p99 | above 3s over 10 minutes | The tail that produces the support ticket. Paged separately from p95 because the causes usually differ. |
| CPU saturation | above 80% sustained 15 minutes | Leaves headroom to act before requests queue. |
| Memory | above 85%, or any OOM kill | An OOM kill is always a page. There is no benign version. |
| DB connection pool | above 80% of pool | The failure that looks like a slow application and is not. |
| Disk | above 85% used, or under 7 days projected | Two forms, because a slow leak and a sudden fill need different responses. |
| Certificate expiry | under 14 days | Long enough that a failed renewal is fixable in working hours. |
| Job did not start | twice its interval elapsed | A job that fails tells you. A job that never ran is silent. |
| Job processed zero rows | any run where it normally processes more | A silent no-op is the most expensive batch failure. |
| Job ran twice | any overlap | Usually worse than not running, because it double-writes. |
| Dead-letter queue | depth above 0 for 15 minutes | The queue exists in order to be empty. Sustained depth is a failure someone must see. |
| Oldest queued message | over 10 minutes | Depth alone hides a stuck consumer that is still accepting work. |

Tooling is deliberately unspecified: it varies by client and hosting, and naming one would date this document
faster than anything else in it. The shape is not optional.

The last five rows are the ones people forget. **Anything on a schedule or a queue needs its own alarms:** it
did not start, it processed zero rows, it ran twice, the dead-letter queue is not empty. A request that fails
tells a user, who tells someone. A batch job that fails silently tells the client weeks later, and by then the
missing rows are a data-repair project.

### No real customer data outside production

Dev and uat carry masked or synthetic data, and **the masking runs as part of the load rather than as a step
someone remembers.** A masking script that is a manual step is a step that gets skipped on the day someone
needs a copy urgently, which is the day it matters. Where a migration dry run needs live records — a
replatform always does — it runs under production's access controls, with no agent session attached.

The cost of the reverse is documented: an AI-built backend shipped with no authorization policies at all on
its file storage, exposing about 72,000 images including 13,000 government IDs, then 1.1 million private
messages in a second breach months later. The first incident did not force a real fix. A one-time cleanup does
not stay clean without a check that fails the build.

### What a developer needs on day one

Setup's job is to make Build and Release Check read results rather than build harnesses:

- **The test runner, with tests beside the code.** Nothing in the loop works without a suite that runs in one
  command.
- **Coverage on changed lines, at 80%, measured across the whole pull request against main.** Not per commit:
  a test-only commit lands red and an implementation-only commit fails coverage, so per-commit has no legal
  ordering. We rejected whole-repo coverage as a gate, because a 78% suite scoring 31% on mutation testing
  passes it. Whole-repo coverage is a number you inherited; changed-line coverage is one you earned.
- **A browser-test harness, from day one, before there is a screen worth testing.** The admin panel lesson
  made mechanical: where the harness that clicks buttons does not exist in Setup, no criterion in Kickoff can
  name it, and what no criterion names does not get built.
- **Expand-before-contract migrations, with CI applying them both from scratch and on top of main's schema.**
  This one is honestly incomplete: that workflow is not written yet. Until it is, applying a migration onto
  main's schema is a manual step and should be recorded as one rather than assumed.
- **A one-command local database**, seeded with masked or synthetic data.
- **Design tokens**, so a screenshot compared against a design frame differs on layout rather than on colour.
- **A load-test script and an accessibility check**, running against dev long before a release. If someone
  runs a load test by hand for the first time during Release Check, the problem is here.
- **The fixtures folder and the decision-record folder**, with their rules written into them, both in
  [templates](08-templates.md). The fixtures rule in one line: needed once, fetch it; needed again, commit it
  and read the file. Never fetch live during implementation, because it makes a passing test a statement about
  someone else's uptime.

And the secret scan over history, daily and automatic, alongside the dependency re-scan. A found secret is not
a ticket. It is revoked or rotated the same day, because deleting the commit does not un-publish the key.

### The counting starts here

The six numbers are defined in [measurement](11-measurement.md). Setup's job is the three fields that **cannot
be reconstructed later** and so have to exist in the tracker before the first ticket: **who found each
defect**, **promotion and release timestamps**, and **stage entry and exit dates**. Everything else can be
recomputed from git and CI. These three are gone if nobody wrote them down, and the numbers with the most
signal depend on them. Until the tracker integration exists, the tech lead records them by hand.

The priority rule if Setup is being trimmed for time: **cut from the gates, not from the counting.** A gate we
have not built is a known absence. A number we never started counting is an answer we cannot get back.

One related rule is a Setup decision rather than a build one: **the agent never writes ticket status.** Status
is derived from what happened — branch pushed, checks green, review approved, merged, promoted. We rejected
letting the agent maintain the board, because it will write to any completion signal it is given, and our own
pilot marked its own work done.

### Exit criterion

**One trivial page is live in dev, put there by the real pipeline.** It can do nothing at all; a static page
with the build id on it is ideal. The point is that the path works while there is nothing at stake. Testable,
in three parts:

1. The dev URL responds, and the build identifier it reports matches a tagged commit and a pipeline run. Not a
   local build, not a manual upload.
2. The perimeter job has run on the host with its token set, and passed. A green run link is the artefact; "we
   configured branch protection" is not.
3. One throwaway pull request has been **blocked** by a gate on purpose — add 500 lines, or a commit that
   weakens a test — and the run that blocked it is linked. Until a gate has failed something, you have tested
   that it runs, not that it stops anything.

The third part is ours rather than inherited practice, and it exists because the pilot's CI pipeline was
excellent and ran zero times. A check nobody has watched fail is a belief, like a backup nobody has restored.
The break-it suite that makes it repeatable is in [host and pipeline](09-host-and-pipeline.md).

| Failure mode | What to do |
|---|---|
| Setup skipped or half-done because the timeline is tight | Cut features from phase one instead. Every standard added later leaves everything written before it unchecked, and that debt is not visible in any diff. |
| The repository documents gates the host does not require | This is the pilot's exact failure. Run the perimeter check and treat its red as blocking. It is the only check that can catch this class. |
| `CODEOWNERS` entries that match nothing | Confirm each glob against the real tree. An unmatched path is owned by nobody and still reads as protected. |
| A gate wired to a script that does not exist, skipping quietly | Make it fail. `format:check` in the starter exits 1 for this reason. Skipping reports green for a check that never ran. |
| Environment values inlined at build time | Fix it before the first release, not during one. Deploy one artefact to two environments and check they differ; if they do not, promotion is a story. |
| Production credentials in a developer or agent session | Remove them. Two documented incidents, both traced to inherited standing access, both remediated by scoping rather than by instruction. |
| Monitoring deferred to "when we go live" | Wire it in Setup at whatever depth applies. Nobody has ever decided monitoring was needed before the incident that needed it. |
| Scheduled jobs and queues with no alarms | Add the four: did not start, zero rows, ran twice, dead-letter queue not empty. A silent batch failure is discovered by the client. |
| Real customer data copied into dev for convenience | Masking runs inside the load path so there is no version of the copy that skips it. |
| Counting deferred until the process settles | Three fields in the tracker now: who found each defect, promotion and release timestamps, stage entry and exit dates. Retrofitted, they are unavailable rather than merely late. |

Setup ends and Build begins. The seven-step loop, the three agent roles and gate discipline are in
[the build loop](04-build-loop.md); named failures and their fixes are in
[troubleshooting](13-troubleshooting.md).
