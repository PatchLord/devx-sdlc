# Depth, novelty, and shaping the process to the project

How much apparatus a project carries, how long a leash a single ticket gets, and which rules bend for six
common project shapes. Read it when you scope work, and again when you grade a ticket.

Three questions decide how much process a piece of work carries. They are answered at different times, by
different people, and they do not substitute for each other.

1. **What does a mistake cost?** Answered once per project, in Solutioning, and written into the SOW. It sets
   the apparatus around the work.
2. **How much of this has been done before?** Answered per ticket, when the spec is approved. It sets the
   length of the leash inside that apparatus.
3. **What shape is the project?** Answered once. It bends the detail of some stages without touching the loop.

```
 ┌─ COST OF A MISTAKE ────────────────┐  ┌─ HOW WELL-TRODDEN ─────────────────┐
 │  decided once, in Solutioning      │  │  decided per ticket, at the spec   │
 │  recorded in the SOW               │  │  recorded in the spec file         │
 │  sets the APPARATUS                │  │  sets the LEASH                    │
 │  Light · Standard · High           │  │  trodden · novel here · novel      │
 └────────────────────────────────────┘  └────────────────────────────────────┘
        raises or lowers the gates              changes step size and who
        and the environments around it          reads what, not the gates
```

## What never bends

**The loop, the size ceiling and the gate discipline are the same at every depth, for every novelty grade, in
every project shape.** One ticket, one branch, one pull request, one merge. The spec is the branch's first
commit and an ancestor of every implementation commit. The `size` check warns above 300 lines or 10 files and
fails above 400 or 20. Weakening a gate lands in its own commit. Every review finding gets a disposition,
fixed or dismissed in writing. Status is derived from git and CI events, never written by the agent. No
session holds production credentials. [The build loop](04-build-loop.md) is where all of that is argued.

Those cost nothing, and they are what make the work reviewable at all, so no depth buys anything by dropping
them. Everything below is about what surrounds them.

## Axis one: what a mistake costs

Four questions, and none of them is "how big is this project".

- **What breaks, and who feels it?** Nobody, only us, the client's staff, or the client's customers.
- **Can it be undone?** A page we redeploy is not the same as data we have moved, emails we have sent, or a
  binary already in a store.
- **Does it involve money, or sensitive or regulated data?** That creates duties even when nothing is broken.
- **How long will it live?** Something running for three years needs documentation and tests that a two-week
  demo does not.

A 40-line script that deletes production rows needs more care than a 40,000-line internal dashboard. Size and
type are the wrong inputs. Consequence is the input.

| | **Light** | **Standard** | **High** |
|---|---|---|---|
| When it applies | nothing to undo, no money, no personal data | real users, recoverable mistakes | money, personal data, or cannot be undone |
| Loop, 400/20 ceiling, gate-change commits, spec ancestry | yes | yes | yes |
| Required checks on `main` | `size`, `gates`, `spec`, `verify` | `size`, `gates`, `spec`, `verify`, `review` | the same five |
| Review agent | runs, advisory | required check | required check |
| Approving reviews required | 1 | 1 | 2 on protected paths |
| Human review on the PR | protected paths, via `CODEOWNERS` | protected paths | protected paths, second reviewer named in Setup |
| Changed-line coverage | not measured | 80% (`--min 80` in `verify.yml`) | 80%, plus mutation on core logic |
| Environments | dev only | dev and uat | dev, uat, production defined in code before it is provisioned |
| Monitoring | none | errors, searchable logs, alarms on error rate, p95, p99, saturation | plus an audit trail of who changed what |
| Data outside production | whatever it is | masked or synthetic, masked as part of the load | masked or synthetic; any dry run on live records runs under production's access controls with no agent session attached |
| Release Check | skipped | the standing list in `docs/release-checklist.md` | plus load test, threat model or penetration test, restore drill with the restore time recorded |
| Launch | deploy it | the checklist | rehearsed, with hypercare that has an end date |
| Support | none | the rhythm | plus someone on call, with a runbook per alert |
| The six numbers | counted | counted | counted |

The last row is deliberate. Counting is cheaper than any gate in the table, and it is the only thing that can
later tell us the table was wrong, so it does not scale with depth. The numbers are in
[measurement](11-measurement.md).

### Light has to be defined tightly

Otherwise everything becomes Light. **The test is what a mistake costs, not who sees it.** A public marketing
page with nothing behind it is Light. The same page with an email capture is not, because it now holds
personal data and there is a deletion obligation attached to it. A tool five people use internally is not
Light if one of its buttons issues a refund. An internal script is not Light if it writes to the production
database.

Depth is a project answer, but the protected set is per path, so a Light project that acquires one payment
path does not stay Light for that path. The honest move is usually to raise the whole project, because a
repository with one High path and no uat has nowhere to test it.

Depth is decided in Solutioning and written into the SOW, because it changes the risk and the price. If the
answers change later, depth goes up with them. It never quietly goes down, and it is re-checked quarterly in
Run and Support, because scope creep is the usual way a Standard project becomes a High one without anybody
deciding. Both stages are in [before build](02-before-build.md) and [delivery](03-delivery.md).

### What Light actually costs, said plainly

Light is not the same product with fewer checks. The law in [why this exists](01-why.md) says otherwise: **the
agent builds to the shape of the check, so a weaker gate gives you a different, smaller product.** The pilot's
admin panel shipped nine write hooks — create, update and delete for three resources — and zero buttons, zero
forms and zero submit handlers. The write side existed at every layer except the one a user touches, because
the gate it chose for itself was "the page renders", and a page with no Create button renders perfectly.
Requirements backed by a config file, a hook or a test landed 8 of 8. Requirements written only as prose
landed 0 of 7.

So choosing Light is choosing to receive less than you specified, in a shape nobody predicted. That is fine
when a mistake costs nothing. It is not a discount on the same output.

Two rules therefore hold even at Light, and neither costs an environment. Each acceptance criterion names the
artefact that will prove it. And a ticket with an interface is not done until something operated it — a
browser test that clicks the flow, or a named person who did, with a screenshot.

### How depth is applied, exactly

There is no depth switch. The expectations live in `perimeter.yml`, in a file `CODEOWNERS` protects, for the
reason that workflow states about itself: a config file an agent can edit is not an expectation, it is a
suggestion. Changing depth means editing named lines and getting a code owner to approve the diff. Both files
are inlined in [enforcement](06-enforcement.md) and [the repository](07-repository.md).

| Depth | The exact edits from the starter as shipped |
|---|---|
| **Light** | In `perimeter.yml`, `REQUIRED_CHECKS="size gates spec verify"`. Delete the `review` job or leave it un-required. Delete the "Coverage on changed lines" step in `verify.yml`. |
| **Standard** | Nothing. The starter ships Standard: `REQUIRED_CHECKS="size gates spec verify review"`, `REQUIRED_APPROVALS=1`, `--min 80`. |
| **High** | `REQUIRED_APPROVALS=1`. Add the mutation job and the audit trail. Both are *to build*: no tool, threshold or definition of core logic is settled, so High depth today means the rest of its column plus a written commitment to these two. Name the second reviewer in Setup — a devx engineer from outside the project where the team is smaller than three. |

Whichever you pick, the host must actually enforce it. On `main`: required contexts matching
`REQUIRED_CHECKS`, `strict = true` so a branch cannot merge stale, at least one approving review with code
owner review required and stale reviews dismissed, linear history required, conversation resolution required,
force pushes and deletions off. The exact settings, and the token `perimeter.yml` needs to read them, are in
[host and pipeline](09-host-and-pipeline.md).

Two of those rows are preconditions rather than preferences. Linear history: `gates.yml` walks
`git rev-list BASE..HEAD` commit by commit and `spec.yml` asserts ancestry, and a merge commit inside a branch
makes both of them reason about an order nothing was ever tested in. Conversation resolution: it is what turns
"every finding gets a disposition" from a sentence into a merge condition. `enforce_admins` is the one row it
is defensible to leave false on a small team, and the cost is exact — the perimeter then holds only as long as
everyone chooses to respect it, and the shortcut count in [measurement](11-measurement.md) is the only thing
that will notice when someone stops.

Deleting the review job at Light is a real deletion, not a skip. `review.yml` fails when `ANTHROPIC_API_KEY`
is absent and says why: *"Either add the secret, or delete this job and remove 'review' from the required
checks in perimeter.yml so the repository stops claiming a review it does not do."* A job that quietly passes
when unconfigured is the pilot's failure with a green tick on it.

Two things look like depth dials and are not. **Whole-repo coverage is never the gate at any depth** — a 78%
suite scoring 31% on mutation passes it, and the same model wrote both halves. We measure the lines this pull
request changed. And **hooks are never the enforcement layer**: `--no-verify` walks past them, and an agent
can edit `lefthook.yml` itself, which is why that file is in `CODEOWNERS`.

> **Two reviewers on a protected path is not an approval count, and cannot be.**
> `required_approving_review_count` is repository-wide — checked against the live API, whose protection object
> has no per-path equivalent. Setting it to 2 would demand two approvals on every trivial ticket, which is the
> arithmetic [the build loop](04-build-loop.md) rejects. What delivers it instead: list **two teams or two
> individuals** for the protected paths in `CODEOWNERS`, since code-owner review requires an approval per
> matching owner entry. The count stays at 1 and the second pair of eyes comes from the owner list. If your
> host cannot do that either, then High depth's second reviewer is a convention a tech lead enforces by hand,
> and it belongs in the *to build* column rather than being described as a gate.

## Axis two: how well-trodden the work is

This one is asked per ticket, and it is not a question about difficulty. It is a question about how much of
this work exists a thousand times over in public code.

The mechanism is that models are strongest on what the training data holds densely and weakest on what it
holds thinly, and **the weakness is not announced.** Output for a problem with no precedent looks exactly as
fluent, as confident and as well-commented as output for a CRUD endpoint. There is no confidence signal to
read, which is why this has to be a routing decision made in advance rather than a reaction to something the
agent says.

The evidence is consistent about the direction, and it is about setting a leash rather than proving a number.
Agents score above 74% on SWE-bench Verified; on the harder, contamination-resistant successor drawn from 41
maintained and commercial repositories, top agents stay under 45% pass@1. The pooled productivity effect
across 23 studies is g = 0.33 (95% CI 0.09 to 0.58, May 2026) — moderate, not a step change — and its decisive
moderator is setting: gains are larger in controlled experiments and smaller in open-source and enterprise
contexts, which is the same distributional story from a different direction. Stripe, running over a thousand
agent-authored pull requests a week, states plainly that iterating on a mature high-stakes codebase is much
harder than greenfield demos. METR's trial found 19% slower while participants believed they were 20% faster —
that measured early-2025 tools, and its follow-up was redesigned rather than published because developers
would no longer serve as a control group, so it dates the finding rather than refreshing it. The clearest
statement of cause is an anecdote, not a study: on a from-scratch machine-learning training repository, agents
were "net unhelpful, possibly the repo is too far off the data distribution". The cause named is
distributional, not difficulty. One anecdote sets a leash length; it does not set an apparatus.

`docs/specs/_template.md` carries the question as a required section — "How well-trodden is this?" — so it is
answered before any code exists, in the document a person approves. The template is in
[templates](08-templates.md).

| | **Well-trodden** | **Novel here** | **Genuinely novel** |
|---|---|---|---|
| What it is | CRUD endpoint, form, standard integration, a pattern already in this repo twice | ordinary elsewhere, new to this codebase | new algorithm, unusual constraint, a domain rule with no precedent |
| Ticket size target | the standard 300 / 10 | 300 / 10 | aim at 150 lines and expect the ceiling to bind |
| Spike first | no | only if an external system's behaviour is involved | usually, and its only deliverable is a committed fixture or contract file |
| The spec must also carry | nothing extra | the pattern being introduced and why the two that exist did not fit | the alternatives considered, which then becomes a record in `docs/decisions/` |
| What a person reads | the evidence and the seams | the evidence, plus the diff where the new pattern lands | the diff itself, not only the evidence |
| Tests | as the criteria name them | one test per seam between old pattern and new | expected values computed by hand, not by the model that wrote the code |

Two arguments sit behind the odd-looking rows. **"Novel here" is about entropy, not risk** — the failure it
prevents is a third way of doing the same thing arriving with no explanation, which costs nothing this week
and leaves every later ticket ambiguous about which pattern to follow. And **at genuinely novel, tests written
by the same session as the code prove agreement rather than correctness**, which is the 78%-coverage-at-31%-
mutation problem in miniature. Hand-computed expected values are the cheapest escape from it.

The honest weakness of this axis: nobody can measure distance from the training data, so the grade is a
judgement, and the explore agent proposes it — an agent asked whether work is familiar answers from the same
distribution that makes it wrong. Treat "well-trodden" in a spec as a claim to check, not a finding. One
`git grep` for the pattern it says already exists twice settles it. The 150-line target is judgement in
exactly the way 300 is: the direction is argued, the number is not measured.

Novelty changes attention and step size. It changes no gate. No ticket is so novel that it merges without a
spec ancestor, and none so familiar that it skips one.

### The two axes are independent

| | Well-trodden | Novel here | Genuinely novel |
|---|---|---|---|
| **Light** | long leash, read the evidence | name the pattern; still no coverage floor, so expect gaps | rare, and the honest question is why it is Light |
| **Standard** | the default case, most tickets | spec names the pattern, seam tests | short steps, a person reads the diff, decision record |
| **High** | full apparatus, long leash inside it | full apparatus, plus the pattern argument | slowest work we do: spike, small steps, two reviewers on the protected path |

The bottom-right cell is where projects lose weeks. The top-left is where the throughput gain lives. The
mistake to avoid is collapsing the two axes into one dial — "important work, be careful" — which applies
ceremony to CRUD and a long leash to the one algorithm nobody understands.

## Six project shapes

The eight stages hold for everything we build. Six shapes change the detail. In each case depth still comes
from what a mistake costs. Shape never sets depth.

### Greenfield

The shape where the numbers look best and the pilot's failure is most likely. No existing code constrains the
agent, so every ticket in week one is at least "novel here": there are no patterns to follow, and the first
ticket to touch a concern sets one.

*Bends:* the undocumented-system phase does not exist. Decision records carry the weight that pattern-matching
carries later, because there is nothing to match yet. Shared surfaces — contracts, schema, shared types, wire
shapes — are frozen before anything is built on them, which was the one thing the pilot got right by design
and which let three tracks proceed with no conflict.

*Never bends:* Setup ends with one trivial page live in dev, put there by the real pipeline. This is the rule
greenfield projects skip, and skipping it is how you get a repository whose CI has run zero times while its
own context file claims branch protection.

### Brownfield with an undocumented system

Mapping it is a phase, not a task inside the first ticket. The agent reads the old codebase and database and
produces a map, and **each claim that matters names what it was checked against** — a query, a captured
response, a recording. Memory is what went missing in the first place, so memory cannot be what confirms the
map.

*Bends:* standards discovery comes before spec-writing, so specs reference the patterns that exist rather than
the patterns we would prefer. A one-line fix in legacy code does not get a full spec pipeline, it gets a
paragraph — what shrinks is the length of the spec, not its existence. Tickets are scoped by subsystem,
because a large repository exhausts the context window before a spec can be written, and a spec written from a
truncated read is worse than no spec.

*Never bends:* changed-line coverage rather than whole-repo coverage, which matters most here. A legacy repo
with no tests fails a whole-repo floor on day one, and the first thing anyone does is lower the floor — a gate
change that ratchets in one direction forever.

### Replatform or cutover

The undocumented-system phase and Launch *are* the project. Most of the risk is in the hour of the switch, not
in the code. Depth is High almost by definition, because the data moves and moving data cannot be undone.

*Bends:* Release Check gains a migration dry run with reconciliation counts and spot checks by a person who
knows what the records should say. The checklist line "Migrations roll back, or are documented as one-way"
stops being paperwork and becomes the decision the rollback plan is built on. The old system stays up, because
the real rollback for a cutover is pointing the domain back, and that only works if the thing it points at is
still running. The URL map and its redirects are a deliverable, with the top pages checked after the switch,
because for a store lost rankings are lost revenue and slow to notice.

*Never bends:* no real customer data outside production, and the one exception — the dry run on live records —
runs under production's access controls with no agent session attached.

### Mobile, with store review

There is no per-pull-request preview, and a queue we do not control sits between merge and users.

*Bends:* Release Check batches into fewer, larger releases, which makes this the shape where the sixth number
in [measurement](11-measurement.md) — how long accepted work waits to go live — is expected to be worst, and
it is the only number that will show it. "Rollback rehearsed" means rehearsing a halted staged rollout and,
where the client's risk needs it, a server-side kill switch and a forced-update path, because a shipped binary
cannot be redeployed away. The release checklist gains the submitted build id, since the artefact under review
is the one promoted.

*Never bends:* the ceiling and the loop, and the rule that a ticket with an interface is not done until
something operated it — on a device or a simulator, recorded.

### No user interface at all

A pipeline, a worker, an integration.

*Bends:* "judge the feature running" means running it against realistically shaped data and reading the
output, not looking at a screen. Criteria name a query, a file or a response rather than a frame, and the
screenshot rule does not apply.

*Never bends:* something still has to operate it end to end. And the enumeration rule transfers. On a screen we
enumerate write flows, because "manage questions" is one line of spec and eight flows in reality; here we
enumerate the failure modes nobody volunteers, each as its own criterion — it did not start, it processed zero
rows, it ran twice, the dead-letter queue is not empty. A request that fails tells a user. A batch job that
fails silently tells the client weeks later, which is why those four are criteria and not monitoring wishes.

### A platform we do not control

A Shopify theme, a hosted CMS. Part of the code lives where our checks cannot reach.

*Bends:* the committed-fixture rule matters more, not less. Capture the platform's actual response and payload
shapes once, into `docs/fixtures/`, and build against the files, because a test that fetches live is a
statement about someone else's uptime. Where there is nothing to promote, because a theme is pushed rather
than deployed, the promoted thing is the commit and the check is that the push came from the pipeline at that
tag. The files the client edits in the platform's own admin are named before the first commit and never
promoted from git.

*Never bends:* one repository, one branch, spec first, the ceiling. And the honest limit, stated rather than
papered over: **nothing we run can see a change made in the platform's admin interface.** The mitigation is
the ownership list and a diff of the platform's own files before each release, not a check. If that hole
matters to the client, it goes in the SOW as a hole.

## What none of this can see

All three answers are judgements, not measurements. Depth is a judgement recorded in the SOW, novelty is a
judgement recorded in the spec, and shape is the only one that is obvious. The thing that would tell us
whether we graded correctly is the fifth number in [measurement](11-measurement.md): defects reaching a
person, per merged ticket, split by who found them. It only answers the question if the depth and the novelty
grade are on the ticket when it is created, because neither can be reconstructed once the work is merged and
the reasoning is gone.

So the day-one requirement is small and easy to miss: **the ticket carries its depth and its novelty grade as
fields.** If tickets graded well-trodden turn out to produce as many escaped defects as tickets graded
genuinely novel, the grading is noise and this whole axis is ceremony — and that is a result we would want in
week six, not a conclusion nobody can reach because the field was never there.
