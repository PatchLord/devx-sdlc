# The templates

Seven files in the starter repository are templates: text with holes in it. This document gives each one
complete, says what makes it work, and names the way people most often fill it in wrongly.

Templates are the cheapest part of this process to install — copy six files — and the easiest part to satisfy
dishonestly. So each one is built the same way: every field asks for something that cannot be produced by
guessing. "Name the file and section." "Name the artefact." "The constraint, not the benefit." A field an
agent can satisfy from the shape of the field alone is a field that will be satisfied that way, and you will
not notice, because the output will look correct.

## What actually enforces these

Be clear about how little of it is machine-checked.

| Template | Who fills it | What a machine checks | What nothing checks |
| --- | --- | --- | --- |
| `docs/design/README.md` | tech lead, at Solutioning | nothing | all of it |
| `docs/design/criteria/_template.md` | a person; the agent proposes | the `gates` job: a criteria edit cannot share a commit with implementation. CODEOWNERS: it needs an owner's approval | whether the criterion is provable |
| `docs/specs/_template.md` | explore agent, person approves | the `spec` job: the file exists at `docs/specs/<TICKET>.md`, is the branch's first commit, and is alone in it | the content of every field |
| `docs/decisions/_template.md` | whoever made the call | nothing | all of it |
| `docs/fixtures/README.md` | agent | `scripts/scan-secrets.mjs` at pre-commit, known patterns only | whether the fixture still matches the live system |
| `docs/release-checklist.md` | tech lead | nothing | every row |
| `tasks/board.md` | whoever raises a ticket | `spec.yml` reads the ticket id out of the branch name | whether an entry ever reaches a terminal state |

Five of the seven are checked by no machine at all. That is not an oversight we intend to close. A CI job that
graded prose would be a job the agent writes to, and we already know what that produces — the agent builds to
the shape of the check. These templates are held up by a code owner reading them, which is why they are short
enough to read. The jobs named above live in [enforcement](06-enforcement.md); `CODEOWNERS` lives in
[the repository](07-repository.md).

They appear below in the order a project fills them in.

## The design document guide

`docs/design/README.md`

```markdown
# Design documents

The source of truth for what we are building. Kept here, in markdown, in the repository — so the agent
reads the same text the developer does, and a divergence between the two is a visible commit rather than
a discrepancy between a wiki and reality.

One document per phase. Written before the tickets are cut, updated whenever a ticket proves it wrong.

## What one contains

- What we are building and for whom
- The decisions already made, and the ones deliberately deferred
- The shapes: data, contracts, the external systems and what they actually return
- What is out of scope for this phase

## The rule that keeps it alive

When exploration finds the document and the code disagree, **the fix lands in the document** — not only
in that ticket's spec. A design document that is only ever read is a design document that is quietly
wrong, and every ticket after this one pays for it again.

## `criteria/`

Acceptance criteria live in `criteria/`, protected by `CODEOWNERS`. An agent may propose a change to
them; only a code owner approves one. Criteria you can edit to match what you built are not criteria.
```

The document lives in the repository rather than a wiki for one reason: the agent must read the same bytes
the developer does, and staleness must show up as a diff. A wiki page that drifted from the code drifts
silently. A markdown file that drifted from the code gets corrected in a commit someone can see.

The bullet worth arguing for is "the ones deliberately deferred". An agent reads an unmarked gap as settled
fact and fills it — plausibly, confidently, and without telling you. A gap marked as open becomes a question
in the spec instead. Writing "we have not decided how refunds interact with store credit" costs one line and
converts a silent invention into a conversation.

**How it goes wrong.** The rule that keeps it alive is the one that lapses. Exploration finds a divergence,
records it in the ticket's spec, and stops there because the spec is what gets reviewed. The document stays
wrong and the next four tickets each rediscover the same thing. The fix lands in both places or the finding
was wasted.

## The acceptance criteria template

`docs/design/criteria/_template.md`

```markdown
# Acceptance criteria — <phase or feature name>

One file per feature, named after it: `checkout-guest.md`, not `criteria-2.md`. This path is protected by
`CODEOWNERS`: an agent may propose a change here, only a code owner approves one.

The proof column is the whole point. A criterion with an empty proof column is prose, and prose is the class
of requirement that does not get built. `spec.yml` does not check this — a person does, at Kickoff, by
counting the empty cells and requiring the count to be zero.

## Criteria

| ID | The criterion | How it will be proven | Status |
|---|---|---|---|
| CO-1 | A guest can complete checkout without an account | `e2e/checkout.spec.ts` → "guest completes checkout" | proven |
| CO-2 | An expired card shows the retry path, not a generic error | `e2e/checkout.spec.ts` → "expired card offers retry" | proven |
| CO-3 | The order total matches the cart total to the paisa | `checkout.total.test.ts` → "total matches cart" | proven |
| CO-4 | A failed payment leaves no order row | `checkout.rollback.test.ts` → "no order on failure" | to build |
| CO-5 | The empty-cart state offers a way back to the catalogue | screenshot against frame 12 of the design | to build |

**ID** — stable and short. Specs and pull requests cite it, so renumbering breaks history.

**How it will be proven** — the named test, script, query or frame. Not "tested", not "verified", not "QA to
confirm". If you cannot name the artefact, you have not finished writing the criterion, and that is the
finding: either the criterion is vague or nobody knows how it would be checked.

**Status** — `to build` or `proven`. Only the merge of the ticket carrying its evidence moves a row to
`proven`. Nobody edits this column to make a report look better; it describes what exists.

## Deliberately not covered by this phase

List what a reader would reasonably assume is included and is not. This is the cheapest place in the whole
process to prevent an argument, and it is the section people skip.

## Changed after approval

| Date | Row | What changed | Who approved |
|---|---|---|---|

A criterion changing is normal — the work teaches you something. A criterion changing *silently* means the
definition of done moved after the client agreed to it.
```

The proof column is the whole point, and everything else in the file is scaffolding around it. A criterion
with an empty proof cell is prose. Prose is the class of requirement that does not get built — our own pilot
put a number on it. One frozen spec through one cold session with no process around it produced 44 commits,
64 tests and 87% line coverage on the backend. Of the requirements that had a config file, a hook or a test
attached, 8 of 8 were present in the finished code. Of the requirements written only as prose, 0 of 7 were
(ours, 2026). Same spec, same session, same model. The only variable was whether the requirement named
something checkable.

So the discipline is arithmetic, not judgement: at Kickoff, count the cells in the proof column that are
empty, and refuse to start until the count is zero. Nothing in CI does this. `spec.yml` checks that a spec
file exists and arrives alone; it cannot read a table and tell you a cell is hand-waving. A person counts.

This path is also the only template with real enforcement behind it, and it takes three independent pieces to
work. `CODEOWNERS` lists `/docs/design/criteria/` in the protected set, so an edit needs a code owner's
review. On the host, `require_code_owner_reviews = true` makes that binding and `dismiss_stale_reviews = true`
stops an approval carrying over to a later push that edits the criteria — both in
[the host and pipeline](09-host-and-pipeline.md). And the `gates` job classifies `docs/design/criteria/*` as a
gate path, so a criteria change cannot share a commit with implementation; it arrives alone, where a reviewer
sees it. Remove any one of the three and the other two stop meaning what we claim.

**How it goes wrong.** Teams keep criteria in the ticket tracker and paste them into the design document
body. Both copies then sit outside `criteria/`, outside CODEOWNERS, and outside the gate-mixing check — so the
agent can quietly adjust the target to match what it built, and nothing objects. The path is the protection;
prose in a document body is not. The second failure is renumbering IDs during a tidy-up, which breaks every
spec and pull request that cited them.

## The spec template

`docs/specs/_template.md`

```markdown
# <TICKET-ID> — <one line, no "and">

> Written by the **explore** agent. Read and approved by a person before any code.
> The agent that implements this will not have the conversation that produced it. Anything not
> written here did not happen.

## What this ticket does

One or two sentences. If you need "and", this is more than one ticket.

## Acceptance criteria

Copied from the ticket, unchanged. An agent may **propose** a change to these; only a person approves one.

- [ ] …
- [ ] …

## How well-trodden is this?

Pick one. This is not about how hard the work is — it is about how much of it the model has seen
before, which is a different thing and a better predictor of where it will quietly go wrong.

- **Well-trodden** — a CRUD endpoint, a form, a standard integration, a pattern already in this repo twice.
  Long leash. Review the evidence, not every line.
- **Novel here** — new to this codebase, but ordinary elsewhere. Name the pattern being introduced and
  why the two that exist did not fit.
- **Genuinely novel** — a new algorithm, an unusual constraint, a domain rule with no precedent.
  Short leash: smaller steps, a human reading the diff and not only the evidence, and the reasoning
  written down in `docs/decisions/` because next time nobody will remember why.

## What the code looks like now

The patterns this work must follow, with file paths. A spec that could have been written without
reading the code is not a spec.

## Where the design document and the code disagree

Name the file and section. A divergence is the most valuable thing exploration produces — it means the
document went stale and every later ticket would have rediscovered it. The correction lands **in the
document**, not only here.

If there was none, say so.

## Questions and answers

In the developer's words, not paraphrased.

**Q:**
**A:**

## The plan

Steps, at the level of one commit each. Not code.

## Out of scope

What someone might reasonably assume is included and is not.

## How each criterion will be proven

| Criterion | How it will be proven |
| --- | --- |
| … | the named test / the screenshot / the response |

Never "verified". Name the artefact.

## What this will not verify

Say it now, before anyone has a reason to leave it out.
```

Two things carry this template. The first is the file-path requirement under "What the code looks like now":
a spec that could have been written without opening the repository has not explored anything, and the
requirement makes that visible in one glance. The second is the proof table, for the same reason the criteria
file has one — 8 of 8 against 0 of 7.

### The well-trodden field

It is there because the useful question before handing work to a model is not "how hard is this" but "how
much of this has it seen". Those come apart constantly. A payment webhook handler is hard and extremely
well-trodden. A bespoke pro-rata rule from a client's spreadsheet is easy and has no precedent anywhere.

The failure modes differ too, which is why the answer changes how you review. On well-trodden work the model
produces the standard solution — usually right, and wrong in standard ways your tests already cover. On
genuinely novel work it produces something with the *texture* of a solution: plausible naming, plausible
structure, a confident build report — and wrong in a way no generic test catches. The field's only job is to
set the leash before anyone is invested in the outcome. On **genuinely novel**, a human reads the diff, not
just the evidence pack. [Depth by cost and novelty](05-depth.md) covers what else changes with the answer.

Its weakness is structural and worth saying plainly: the explore agent picks the value, and it has an
incentive toward **well-trodden**, because that is the label that asks least of it afterwards. The approving
human should treat a **well-trodden** claim on work that introduces a pattern not already in this repository
twice as the single thing in the spec most worth overriding.

**How it goes wrong.** The most common failure is the criteria section. The agent copies the acceptance
criteria and improves them on the way past — tightening wording, merging two, dropping one it judged
redundant. Diff that block against `docs/design/criteria/` before approving; it takes ten seconds and it is
the difference between criteria and suggestions. Second is "Where the design document and the code disagree"
left blank because nothing looked wrong. Blank and "none" are different claims, and only one of them says
exploration looked. Third is the proof table filled with mechanisms rather than artefacts — "unit test"
instead of `payments/refund.test.ts::refunds a partial capture`. If the artefact does not have a name yet,
the ticket is not specified yet.

## The decision record

`docs/decisions/_template.md`

```markdown
# <NNNN> — <the decision, as a statement>

**Date:** YYYY-MM-DD · **Status:** accepted | superseded by <NNNN>

## What we decided

One sentence, in the present tense.

## Why

The constraint that made this the answer. Not the benefits — the constraint. In six months the
benefits will be obvious and the constraint will be forgotten, and that is when someone undoes this.

## What we chose against, and why not

The option a reasonable person would raise. If you cannot name one, you did not have a decision.

## What this costs us

Every decision costs something. Naming it here is how we notice when the cost outgrows the reason.

## What would make us revisit this

A condition, not a date.
```

Five short sections, and four of them exist to stop the record being an advertisement. The load is carried by
"Why". The constraint outlives the benefit in usefulness and dies first in memory, so the record is written
against forgetting rather than for onboarding.

Records matter more here than on a team of only humans, because agents read this folder. An undocumented
decision gets re-litigated by every future session that notices the code looks odd — and a session that
re-litigates it does not argue with you, it just quietly writes the other thing.

**How it goes wrong.** People write benefits under "Why" — "this gives us better separation of concerns" —
which reads fine and prevents nothing. The test: could someone who disagreed with the decision have written
your "Why" sentence and still disagreed? If yes, it is a benefit, not a constraint. The second failure is a
date under "What would make us revisit this". A date arrives whether or not anything changed, so the review
is theatre. Write "when a second consumer needs this data" or "if p99 on the batch job exceeds 30s".

## The fixtures rule

`docs/fixtures/README.md`

```markdown
# Fixtures

The real shapes of things outside this repository: an API's actual response, a webhook payload, a
document the client sent, a page we scraped once.

## The rule

Needed once — fetch it. Needed again — commit it here and read the file.

Never fetch live during implementation. It makes the result depend on which tools happened to be
connected that day, and it makes a passing test a statement about someone else's uptime.

## Before it lands

Strip real credentials and real personal data. Replace them with obviously fake values — `pre-commit`
scans for the patterns, but it is a hint, not a gate, and it only catches the shapes it knows.

Name the file after what it is and where it came from: `stripe-webhook-payment_intent.succeeded.json`,
not `response.json`.
```

"Needed once, fetch it; needed again, commit it" is the entire policy. It exists because an implementation
run that reaches the network is not reproducible: re-run it next week with a different MCP server connected
and you get different code from the same spec.

The security note is deliberately honest about its own limit. `scripts/scan-secrets.mjs` runs at pre-commit
and matches known key shapes. It will miss a bearer token in a header format it does not recognise, and
`--no-verify` walks past it entirely. It reduces accidents. It does not make the folder safe.

**How it goes wrong.** People hand-trim a captured response down to the fields they care about. The fixture
then tests the code against a shape the vendor never sends, and the missing field that breaks production is
exactly the one that was cut. Commit the whole payload with values redacted, not the payload with keys
removed. The second failure is naming: `response.json` in a folder of twelve files tells the next reader
nothing about which system it came from or when.

## The release checklist

`docs/release-checklist.md`

```markdown
# Release checklist — <version> to <environment>

Copy this into `docs/releases/<version>.md` and fill it in. One file per release, committed.

**Build once, promote.** One artefact, built at a named commit, moved dev → uat → prod. Never rebuilt
per environment — a rebuild makes the thing you tested and the thing you shipped two different things.

- **Tag:** `v…`  **Commit:** `…`  **Build id:** `…` (the 12-char id from the deploy run, not the branch)
- **Promoting from:** uat  **to:** production

| Event | Timestamp (UTC) |
|---|---|
| Client accepted the last feature in this release | |
| Promoted to uat | |
| Promoted to production | |

Those three are not bookkeeping. Number 6 in the manual — how long accepted work waits to go live — is
computed from them, and it cannot be reconstructed once the runs age out. Fill them in as each happens.

## What is in it

| Ticket | What changed | Pull request |
| --- | --- | --- |
| | | |

## Verification

Three columns, and the third is not optional. "Verified" in the middle column with an empty third
column means nobody checked.

| Item | How it was verified | Evidence |
| --- | --- | --- |
| The same artefact that passed uat | build id matches | |
| Migrations run forward on a copy of prod data | | |
| Migrations roll back, or are documented as one-way | | |
| Acceptance criteria for every ticket in this release | | |
| The paths a user actually takes still work | | |
| Error and latency dashboards exist for what changed | | |
| Secrets and config present in the target environment | | |
| Third-party rate limits and quotas allow for this | | |
| Rollback tested, not assumed | | |

## What this release does not verify

Say it. Someone will read this file during an incident.

## Rollback

The exact command or action, and who can run it. Not "redeploy the previous version" — the command.

## Who was told

- [ ] CSM, in words the client can read
- [ ] The person on call
```

The file says "Number 6 in the manual"; that is the sixth of [the six numbers](11-measurement.md), how long
accepted work waits to go live.

### The three timestamps

They look like bookkeeping and they are not. *Client accepted the last feature in this release*, *promoted to
uat*, *promoted to production* — the gap between the first and the last is the sixth number, per release, and
it is the one number in the set that measures the part of delivery nobody owns. Work that is finished, tested
and accepted, sitting still.

They have to be written down as they happen because they cannot be recovered afterwards. Acceptance happens
in a conversation, a call or a ticket comment, and it leaves no artefact with a reliable time on it. The two
promotions do leave one — the `deploy` and `promote` runs in
[the host and pipeline](09-host-and-pipeline.md) — but workflow run history ages out on a retention window,
and once it has, the timestamp is gone for good. There is no archaeology that recovers it. If the file is not
committed on the day, the number does not exist for that release, and the series has a hole in it that will
still be there a year later when someone asks whether we got faster.

### The evidence column

The other design choice carrying this file. A two-column checklist collapses into a column of ticks within
three releases — that is not cynicism, it is what checklists do once the same person fills one in for the
fourth time. The third column asks for a thing rather than a claim, and a thing is harder to produce from
memory. "Verified" in the middle column with an empty third column means nobody checked.

**How it goes wrong.** The Evidence column gets "see PR" or "done in the deploy channel". Evidence is a link
to a specific run, a specific screenshot, a pasted build id — something that still resolves in nine months
during an incident, when the channel has scrolled and the PR is one of four hundred. The other standard
failure is "Rollback tested, not assumed" ticked because a rollback path exists in principle. Ticking that row
means you ran it, on this artefact. [Delivery](03-delivery.md) covers where in Release Check this happens.

## The pull request template

Not inlined here — it lives in [the repository](07-repository.md) with the rest of the `.github/` and
`.claude/` files. It belongs in this argument anyway, because it closes the chain the other templates open.

The criteria file names how each criterion *will* be proven. The spec copies that promise per ticket. The pull
request template is the same table with a third column added, showing the artefact that actually proves it.
Same rows, one more column — which is what makes a dropped criterion obvious instead of a matter of whether
anyone remembers. The other field worth knowing about is "What we learned that was not in the design
document", which requires a destination per item, because a learning recorded only in a pull request
description is a learning that is gone.

What is deliberately absent from that template is any field the agent can tick to declare the ticket done.
Ticket status is written by the pipeline on merge, never by the agent, because an agent given a completion
signal writes to it.

## `docs/production-ready.md` — what good enough actually means

The answer to "is this ready to ship?", written down so it stops being a judgement each developer makes
from memory at speed. This is the template; the project-specific slots at the bottom must be filled during
Setup, and leaving them blank is how a standard becomes decoration.

What makes it usable rather than aspirational is that **every line carries how it is enforced.** Tier 1 is
a lint or structural test and cannot be skipped. Tier 2 is a review criterion, so it is probabilistic but
written down and auditable. Tier 3 is prose, which loses to context pressure. Tier 3 is a queue rather
than a resting place: anything sitting there for a month either becomes a lint or gets deleted, because a
standard nobody enforces is worse than none — it lets everyone believe the ground is covered.

One rule for how it grows: **something went wrong twice, so it became a rule.** Not from a blog post, not
from someone's preference. A line added because it seemed sensible is a line nobody will defend when it
fails a build at six in the evening.

```markdown
# What production ready means here

The answer to "is this good enough to ship?" — written down, so it stops being a judgement each developer
makes from memory at speed.

This exists because the failure it prevents is measurable. In our own pilot, requirements backed by a
config file, a hook or a test came out **8 of 8** present and correct. Requirements written only as prose
came out **0 of 7**. An agent makes several hundred small choices per ticket about things nobody
specified, and it makes them differently every time. This file is where those choices get made once.

## How each line is enforced, and why the order matters

Three tiers, and the tier is part of the rule:

| Tier | Form | Why it is stronger |
|---|---|---|
| **1 — Lint or structural test** | code that fails the build | Cannot be skipped, cannot be forgotten, and the failure message can tell the agent the fix |
| **2 — Review criterion** | a line in `REVIEW.md` the review agent reads | Needs judgement, so it is probabilistic — but it is written down and auditable |
| **3 — Prose** | a paragraph here or in a skill | Weakest. Loses to context pressure. Use only where neither of the above can reach |

**Move rules up the tiers over time.** Anything sitting at tier 3 for a month is a candidate for the
weekly hour: either it can become a lint, or nobody actually cares about it and it should be deleted.
A standard nobody enforces is worse than no standard, because it lets everyone believe it is covered.

## Network and data

| | Rule | Tier |
|---|---|---|
| ☐ | Every outbound call has an explicit timeout. No exceptions, including internal services | **1** — lint on the client wrapper |
| ☐ | Retries with backoff on anything transient, and only on idempotent operations | **1** |
| ☐ | Anything retryable is idempotent, or carries an idempotency key | **2** |
| ☐ | Input is parsed and typed at the edge, then trusted inwards. No validation scattered through layers | **1** — no `unknown` or `any` past the boundary |
| ☐ | Every list endpoint has pagination and a hard maximum | **2** |
| ☐ | No N+1 queries on any path a user waits for | **2** |
| ☐ | Money is integers in the smallest unit. Never a float, anywhere | **1** — lint the type |
| ☐ | Timezones explicit. Store UTC, convert at the edge, never rely on server locale | **2** |
| ☐ | Migrations expand before they contract, and are reversible or documented as one-way | **1** — CI applies them from scratch and onto main's schema |

## Anything that writes to a database it did not create

| | Rule | Tier |
|---|---|---|
| ☐ | Every dev-only or destructive script refuses a target it was not pointed at deliberately: a protected `APP_ENV`/`NODE_ENV`, or a database host the project has not declared local. It refuses an absent connection string rather than guessing, takes its opt-out from a named env var that IaC sets for one environment only, and prints the target it accepted | **1** |
| ☐ | The check reads the connection string the command will *actually* use — with a pooler, `migrate reset` and `db push` use the direct URL, not the pooled one | **1** |
| ☐ | The test suite refuses a deployed environment's **server**, not merely its schema. Assert it in the per-worker setup file, not only where the runner builds its config, so a regressed `env` block fails loudly | **1** |
| ☐ | A guard whose job is to refuse is tested by spawning the real entry point with a scrubbed environment and a host that cannot resolve — so a **deleted** guard fails instead of quietly connecting | **1** |

Which hosts count as local is project-specific: record them under "Project-specific" below. Where local
development does not reach the database over loopback, say so there and name what replaces the host rule —
otherwise every developer sets the opt-out permanently in `.env` on day one and only the `APP_ENV` half
survives.

**This is on the list because of a live incident, not a blog post.** On a client project a dev seed's
delete-then-recreate of access grants emptied `access_grants` on the dev database. The only thing standing
between that same code path and production was a comment saying "NOT for prod" and one Terraform ternary
(`RUN_SEED = environment == "dev"`) — so one mistyped container environment variable was enough. Publicly
reported incidents match the shape: a `DATABASE_PUBLIC_URL` believed to be a demo environment was
production, followed by a forced reset and a demo seed, with backups not scheduled.

Note what this rule reaches that the credential-absence rule does not. "No session holds production
credentials" is sound and it says nothing about a script running *inside* a deployed container, which holds
that credential by design because our own infrastructure gave it one.

## When things fail

| | Rule | Tier |
|---|---|---|
| ☐ | Every dependency has a defined behaviour when it is down — degrade, queue, or fail loudly. Never hang | **2** |
| ☐ | Errors surfaced to a user say what to do next, not what went wrong internally | **2** |
| ☐ | Internal error detail never reaches a client response | **1** |
| ☐ | Cache invalidation is named wherever caching is added. If you cannot say what invalidates it, do not add it | **2** |

## Security

| | Rule | Tier |
|---|---|---|
| ☐ | Authorisation checked, not only authentication. Being logged in is not permission | **2** — and the highest-value line in this file |
| ☐ | Any path that substitutes for authentication — dev bypass, impersonation, a seeded session — is gated on an explicit **allow-list** of environment names, never a deny-list: unset or unknown means off. On any environment that is deployed it needs a held secret, not a header alone | **1** where such a path exists — the artefact is a test asserting the unset environment is disabled, and one naming the deployed-dev case; **n/a** otherwise |
| ☐ | No personal data in logs. Stripped before it leaves the application, not in the log pipeline | **1** where a field allowlist exists, **2** otherwise |
| ☐ | Secrets from the environment. Never in code, never in a fixture, never in a test | **1** — `scan-secrets.mjs`, and host push protection |
| ☐ | Rate limits on anything publicly reachable | **2** |
| ☐ | Dependencies with known criticals do not stay open | **1** — `scan.yml`, daily |

**Why the bypass line carries two clauses.** The allow-list closes only unset and unknown values. A live
project set its dev opt-ins from infrastructure "for the dev environment only" and then deployed that
environment to a container app — so on that host `dev` was *in* the allow-list, and a bare header minted a
principal with no secret required. A checklist ticked at the allow-list and stopped has not asked the
question that matters.

And the variable itself may not be a trust boundary at all. A published advisory documents `NODE_ENV` being
**inlined to `"development"` by the bundler** in a production build, so a block guarded by
`if (process.env.NODE_ENV !== 'production')` ran in production. An allow-list on a build-time-substitutable
value fails the same way as a deny-list.

## Anything with an interface

| | Rule | Tier |
|---|---|---|
| ☐ | Empty, loading, error and long-content states exist for every view. Not just the happy path | **2** — and evidence per state |
| ☐ | Keyboard reachable, focus visible, inputs labelled, contrast sufficient | **1** where an a11y linter covers it, **2** otherwise |
| ☐ | Every write flow is a separate acceptance criterion — create, edit, delete, and the error case on each | **2** |
| ☐ | Something has operated the flow. A browser test, or a person with a screenshot | **1** — the criterion names its artefact; `operate-app` produces it |

That last one is the rule this project exists to enforce. "It renders" is a different check: a page with
no Create button renders perfectly.

## Being able to run it

| | Rule | Tier |
|---|---|---|
| ☐ | An error reaches the tracker with the release that introduced it | **2** |
| ☐ | A log line is searchable, and personal data is already gone | **2** |
| ☐ | Anything on a schedule or a queue alerts on **did not start**, **processed zero rows**, and **ran twice** | **2** |

The queue and schedule line is the most commonly missed and the most expensive. A request that fails
tells a user immediately. A batch job that fails silently tells the client weeks later.

## Making things the same

| | Rule | Tier |
|---|---|---|
| ☐ | One canonical implementation of each shared concern — HTTP client, async helpers, date handling, money | **1** — structural test |
| ☐ | New code follows the pattern already here. If two patterns exist, that is a finding, not a choice | **2** |
| ☐ | Dependency direction between layers is enforced, not conventional | **1** — structural test |

Not tidiness. An agent working in a codebase where every corner looks alike carries understanding from
one file to the next and produces predictable output. Four ways to make an HTTP call spends the model's
attention on guessing which one you meant.

## Project-specific — fill these in during Setup

The lines above are close to universal. These are not, and leaving them blank is how a standard becomes
decoration.

- **Latency budget:** p95 under ___ ms, p99 under ___ ms, on these paths: ___
- **Supported browsers and devices:** ___
- **Data retention:** ___ , and what gets deleted on request: ___
- **Compliance obligations:** ___ (PCI, GDPR, sector-specific)
- **The canonical implementations for this codebase:** HTTP ___ , async ___ , dates ___ , money ___
- **Hosts that count as local for destructive scripts:** ___
- **What we deliberately do not do here, and why:** ___

## What this file cannot do

It cannot tell you whether the feature is the right feature, whether a client will accept it, or whether
a trade-off was correct. Those are judgements, they stay with a person, and no amount of checklist
removes them.

It also cannot catch a rule that was written but never enforced — which is why every line above carries
its tier, and why tier 3 is a queue rather than a resting place.

## How this file grows

Only one way, and it is the weekly hour: **something went wrong twice, so it became a rule.** Not from a
blog post, not from someone's preference, not from a standard read somewhere. A line added because it
seemed sensible is a line nobody will defend when it fails a build at 6pm.

Every line here should be traceable to something that actually broke.
```

## `REVIEW.md` — the review criteria, owned by the team

Separate from the standard on purpose. The standard says what good means; this says how the reviewer
works. It lives at the repository root and is edited freely, so changing what gets reviewed never means
editing an agent definition.

Two things in it do most of the work. **The gate surface is checked first**, because every other check in
the repository can be edited by whoever is submitting the change — that makes the reviewer the only line
on that one class. And **every finding is graded** Important, Nit or Pre-existing, because ungraded
findings mean a human reads all of them and therefore reads none properly. Pre-existing never blocks: a
pull request that touched a file is not responsible for everything in it, and treating it otherwise
teaches people to avoid touching anything.

This is the shape Anthropic arrived at after measuring only 16% of their own pull requests receiving
substantive feedback under velocity pressure. With criteria written down, engineers marked under 1% of
findings incorrect — which says a reviewer with written standards is a different thing from a bot.

```markdown
# Review criteria

What the review agent checks, and how it grades what it finds. Owned by the team and edited freely —
changing what gets reviewed should not mean editing an agent definition.

The standard itself is `docs/production-ready.md`. This file is the reviewer's operating instructions.

## Order of attention

Look in this order. The first two are the ones no other check can see.

**1. The gate surface.** Did this change weaken a check? An existing test modified or deleted, a
threshold lowered, an assertion loosened in a test that stayed, a CI job removed or made non-blocking, a
lint rule disabled. Report these first and separately. Every other check in this repository can be
edited by whoever is submitting the change, which makes this the one class where the reviewer is the only
line.

**2. Evidence against criteria.** For each acceptance criterion, does the named artefact exist and does
it prove the criterion — or does it merely restate it? A screenshot of a page is not evidence that a flow
works. A test named after a behaviour is not evidence it asserts that behaviour.

**3. The standard.** Walk `docs/production-ready.md` and check the tier-2 lines. The tier-1 lines are
already enforced by lints and structural tests; do not spend attention re-checking them.

**4. Correctness.** Logic, edge cases, error paths.

**5. What is missing.** A criterion with no evidence. A path no test reaches. An error case nobody
handled. A state that exists in the design and not in the code.

## Grading

Every finding gets one of three. This matters more than the finding itself, because ungraded findings
mean a human reads all of them and therefore reads none of them properly.

**Important** — fix before merge. It is wrong, unsafe, or it breaks a criterion. If you are unsure
whether something is Important, it is not.

**Nit** — worth saying, not worth blocking. Naming, structure, a clearer way. The author may dismiss it
without justifying that.

**Pre-existing** — this was already true before the change. Report it once so it is visible, never block
on it. A pull request that touched a file is not responsible for everything in that file, and treating it
otherwise teaches people to avoid touching anything.

## How to report

State the file and line. Say what is wrong, then what would be right. A finding the author cannot act on
without asking what you meant has cost more than it saved.

Findings the author believes are wrong are **dismissed in writing** on the pull request, in a comment
beginning `Dismissed:`. That is a legitimate outcome. The check is green when every finding has a
disposition — fixed or dismissed — not when there were none. A reviewer who finds nothing scores
perfectly and catches nothing.

The prefix is not ceremony: `scripts/collect-week.mjs` counts dismissals to compute the dismissal rate,
and nothing else in a pull request distinguishes "this finding was wrong" from ordinary discussion. A
dismissal rate above roughly one in three means the reviewer is costing more attention than it saves, and
without the prefix nobody would ever find that out.

Do not manufacture findings. A reviewer that invents work teaches everyone to ignore it, which is worse
than one that occasionally misses something.

## What not to review

- Formatting, import order, anything a formatter owns
- Anything a tier-1 lint already enforces
- Style preferences not written in `docs/production-ready.md` — if it matters, put it in the standard;
  if it is not in the standard, it is not a finding
- Whether the feature is the right feature. That is a human judgement made before this point

## Project-specific criteria

Add lines here during Setup, and after the weekly hour. Each one should be traceable to something that
actually went wrong.

- ___
```

## `tasks/board.md` — the tracker

Adopted from a live project rather than designed. Its three load-bearing headings are Findings, When picked
up, and a Resolution that records what did **not** change — none of which a tracker field has room for.

The rule at the bottom is the one that keeps it from becoming a graveyard: every entry reaches a terminal
state, and the test for that is mechanical rather than a matter of opinion.

````markdown
# Board

Every ticket, in the repository. **This is the tracker** — not a copy of one, and not a to-do list beside
one. There is no external tool holding a different answer.

Three reasons it lives here rather than in a tool:

- **The agent can read it.** A session reads this file on every run. It cannot read a tracker without an
  integration, and an integration on the critical path of a keystroke fails during the one incident where
  you need it most.
- **One writer, so nothing drifts.** A ticket's state is a diff with an author and a date. There is no
  second place holding a different answer.
- **Status is derived, not typed.** A branch exists, a pull request is open, a merge happened. Nobody moves
  a card.

And the cost, stated plainly: **people who do not use git cannot see this.** Delivery, the CSM and the
client have no view of it. If they need one, generate it — the repo writes, the tool displays, never the
other way round. If someone starts typing status into the tool, you now have two answers and the tool's is
the one that will be quoted at you.

<!-- board:index -->

| | Ticket | | State | Blocked by |
|---|---|---|---|---|
| ✓ | `PULSE-000` | example, delete this | DONE (2026-08-06) |  |

_0 open, 1 done. Regenerate with `node scripts/board.mjs --index`._

<!-- /board:index -->

## Seeing it, and keeping it honest

The index at the top is generated from the entries below — run `node scripts/board.mjs --index` and commit
the result. It lives *in this file* on purpose. A separate dashboard, or an HTML board, is a second place
holding the same truth: the project this board was adopted from keeps a `dag-board.html` and has a written
lesson that exists only because the agent kept forgetting to update it. One writer, one representation. If
delivery wants a picture, generate it on demand and throw it away.

Two things are checked rather than trusted:

| | Where | Tier |
|---|---|---|
| The branch's ticket has an entry here, and a DONE entry has a Resolution | `spec.yml`, on every pull request | **1** — gated |
| Ids unique, blockers exist, every DONE entry resolved | `scripts/board.mjs --check`, pre-push | 2 — a hint, `--no-verify` walks past |

## Scale limit

One file is right up to roughly five or six people. Past that, concurrent edits to the same file conflict
constantly and the honest move is one file per ticket under `tasks/` with this same shape. Do not wait for
the conflicts to become normal before splitting.

## Ticket ids

Minted here, in ascending order, and never reused. Check the highest id in this file before minting; a
duplicate id makes two branches resolve to one spec and `spec.yml` cannot tell them apart.

The branch is named after it: `PULSE-123-short-slug`. `spec.yml` reads the id from the branch to find
`docs/specs/PULSE-123.md`, so the id is load-bearing rather than cosmetic.

`PULSE` is a placeholder. **Choose the project's own prefix during Setup** — it must match
`^[A-Z][A-Z0-9]+-[0-9]+`, which is what `spec.yml` looks for. Whatever you pick, put it in `CLAUDE.md` so
the agent stops inventing branch names.

## The shape of an entry

Copy this. Every heading earns its place, and the last two are the ones people skip and should not.

```markdown
# PULSE-123 — one line, no "and"

**State** open | in progress | blocked | DONE (YYYY-MM-DD)
**Depth** light | standard | high   ·   **Raised by** a person, a review, an incident, another ticket
**Blocked by** PULSE-101 — omit the line when nothing blocks it

## Goal

What changes for whom. Two sentences.

## Background — what is already in place

The files and mechanisms that exist today, with paths. Written so whoever picks this up in three weeks
does not have to rediscover the shape of the code.

## Plan

- [x] Something finished, with the file it landed in
- [ ] Something not

## Findings

**Verified, not speculative** — and say which. A finding you have reproduced is worth ten you suspect.
Give the file and line. If something reads like a defect and turned out not to be, record that too:
"reversed lunch IS already rejected today — verified — it just has no test pinning it" saves the next
person the same hour.

## When picked up

The concrete next actions, specific enough to start from cold. Decisions that need a person go here as
questions, not as assumptions.

## Resolution — written when it closes

What actually changed, and **what did not**. The second half is the part that matters:

- what the obvious fix would have got wrong, if you found that out
- what you deliberately left alone, and why
- what remains open, named, so closing this ticket does not silently close it
```

## The rule that keeps this file honest

**Every entry reaches a terminal state.** `DONE` with a resolution, or deleted with a reason. An entry
that only accumulates is how a board becomes a graveyard nobody opens — and once nobody opens it, adding
to it is worse than not writing it down, because it feels like the work was captured.

The test is mechanical: `git log --numstat -- tasks/board.md` should show deletions as well as additions.
A file that has only ever grown has no exit condition, whatever its entries say.

## Deferred work is not a lesser ticket

When a ticket surfaces adjacent work that is genuinely out of scope, it gets an entry here — verified, with
its findings — rather than being crammed into the current pull request past the size ceiling, or mentioned
once in a review comment and lost.

That is the difference between a board and a to-do list. A to-do list holds what somebody intends to do. A
board holds **what is known about work not yet done**, which is worth far more, and is the thing that
otherwise lives only in the head of whoever found it.

---

# PULSE-000 — example, delete this

**State** DONE (2026-08-06)
**Depth** light · **Raised by** setting the repository up

## Goal

Show the shape. Delete this entry once a real one exists.

## Resolution

Nothing shipped. It is here so the first person to add an entry has something to copy rather than a
template to interpret.
````
