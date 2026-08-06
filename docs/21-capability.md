# Capability — the half that produces

[Enforcement](06-enforcement.md) is the half that refuses. [Orientation](20-orientation.md) is the half that
informs. This document is the third one, and we built it last because we had argued ourselves out of building
it at all: **the half that produces.**

## What the measurement said

Counted in the starter on 6 August 2026, before any of this existed:

| | |
|---|---|
| `scripts/` | 6,710 lines |
| `.github/workflows/` | 1,422 lines |
| everything generative — three subagents, four skills, two commands, `CLAUDE.md` | **6,158 words** |
| a knowledge layer | none, of any kind |

`awslabs/aidlc-workflows`, measured the same way, carries 92,982 words across 14 agents, 32 stages and 59
knowledge files — roughly fifteen times our generative content. [Finding 71](../research/findings.md) is the
entry.

Nine-tenths refusal is not strictness. **It is a repository that can tell an agent it is wrong and cannot tell
it what right looks like.**

## The defect, in one case

`.github/workflows/criteria.yml` refuses an acceptance criterion whose evidence cell does not resolve. The
resolver behind it, `scripts/lib/criteria.mjs`, takes three forms — a path, a path plus a literal string
inside that file, or a URL — and refuses everything else. It refuses hardest the cells that read most like
diligence: `verified`, `tested`, `confirmed`, `manual`, a tick. That is a good check, and it is the check the
rest of this standard has wanted since [why this exists](01-why.md).

The teaching for it already existed on the day the gate shipped. `docs/design/criteria/_template.md` carries
five worked rows in exactly the form the resolver wants — `CO-1` through `CO-5`, one of them deliberately
weaker than the others so a reader can see the difference. And it was reachable from nothing. No skill named
it, no line of `CLAUDE.md` pointed at it, and `criteria.yml` does not read that directory. An agent meeting
the gate learned that it had failed, learned the same thing again on the next push, and had nowhere to go in
between.

**So the defect was never a missing lesson. It was a lesson with no way in.**

Part of the repair is two lines at the end of the resolver's own failure output:

```
  Five worked examples:  docs/design/criteria/_template.md
  The rules, in full:    the `acceptance-criteria` skill
```

Printed on every refusal, because a failing check is the one moment the reader is guaranteed to be looking,
and a teacher that has to be remembered is a teacher that is not read.

Generalised, and this is [finding 70](../research/findings.md): **a gate with no paired capability is a
rejection service.** It says no, repeatedly, and nothing it prints leads anywhere.

## The audit that follows

The obligation the finding creates is mechanical. For every check, name the thing that helps produce what it
demands — and where nothing does, say so in the same column as the ones that do.

| Check | What it demands | What helps produce it |
|---|---|---|
| `size.yml` | a diff under 400 lines and 20 files | `build-loop` step 1; `respond-to-review` → `references/size.md` |
| `spec.yml` | the spec first, alone, with a board entry and a `Resolution` on close | `write-a-spec`; `docs/specs/_template.md` |
| `criteria.yml` | an evidence cell that resolves | `acceptance-criteria` — **this row was empty when the gate shipped** |
| `gates.yml` | no commit mixing a gate change with implementation | `respond-to-review` → `references/gates.md`; `house-rules` |
| `verify.yml` | seven sub-gates wired and green | `respond-to-review` → `references/verify.md` |
| `review.yml` | a diff a reviewer can act on | `REVIEW.md`, which is the review agent's instructions |
| `red-on-base.yml` | a test that fails at the base commit | `acceptance-criteria`, route 2 — write the failing test first |
| `evidence.yml` | artefacts under `.evidence/<TICKET-ID>/` | `operate-app` |
| `promote.yml` | a release checklist with evidence in every row | `docs/release-checklist.md` |
| `scan.yml` | scanning switched on at the host | nothing, and nothing should — it grades host configuration, not a diff |
| `perimeter.yml` | every workflow classified required, advisory or not-a-gate | nothing. A person classifies; see [host and pipeline](09-host-and-pipeline.md) |
| the depth grade | the right apparatus for the cost of being wrong | **nothing in the starter.** [Depth](05-depth.md) is the teaching and it lives here, in this standard, where no session reads it |

Four rows were empty when the audit ran: the criteria resolver, the learning loop, the next-step loop, and
the depth grade. Two of those four were mechanisms built that same day and given no caller at all. Three now
have a skill. The fourth still does not, and printing that in the same column as the others is the whole
reason the column exists — a row that quietly promotes an unpaired gate is the defect
[the artefacts](17-artefacts.md) catalogues.

## Why we had built none of it

The cause was our own ledger, read backwards. [Finding 59](../research/findings.md) says standing agent
context is **generative, not preventative** — twenty design rules in a live project's `CLAUDE.md` did not
stop four accessibility rules being switched off inside a feature commit. We took that as *context is weak*
and stopped writing any.

It says the opposite. Context cannot prevent, and generation is precisely what it is for. State the division
so it cannot be misread a second time:

> **Prevention is a gate's job. Production is context's job. Neither substitutes for the other.**

Every failure this standard has recorded sits on one side or the other of that line. A rule written in prose
and counted as enforcement is the first error, and it is the one [enforcement](06-enforcement.md) exists to
stop. A gate shipped with nothing that teaches the shape it wants is the second, and until now nothing here
stopped it.

## Not volume — loading

The reference implementation's 92,982 words are the wrong answer to the right question, because most of them
are prose loaded whether or not the session needs them. The research round converged on one answer and it is
not about volume: **it is about loading.** Three properties of the mechanism decide the whole design.

| Property | What follows from it |
|---|---|
| A skill's `description` is loaded on every session; its body is not | the description is the only part with a guaranteed reader, so it carries the trigger and nothing else |
| Descriptions share one small slice of the context window, and are **dropped** when that slice overflows | a skill added carelessly can silence one already there. The description budget is spent, not free |
| A body, once loaded, stays for the rest of the session | loading a file the session did not need is not a small waste. It is a permanent one |

Measured in this starter: **533 words of descriptions, paid on every session. 11,067 words of `SKILL.md`
bodies, paid when a situation matches one. 19,329 words of side files, paid only when a `SKILL.md` sends the
reader to a specific one.** The whole layer is about thirty thousand words and a session that needs none of
it pays five hundred.

Four rules hold that shape, and they are the difference between a capability layer and ninety thousand words
of prose.

**1. Short `SKILL.md`, detail in side files.** The longest here is 1,390 words and the shortest 779. A
`SKILL.md` states the rule, the shape that satisfies it, what checks it, and where the detail lives. Nothing
that a reader would only need once is in it.

**2. One level of reference, and never a chain.** A `SKILL.md` names a side file; a side file does not send
the reader onward to a third. There is exactly one exception in the ten:
`.claude/skills/acceptance-criteria/refusals.md` runs the resolver against
`.claude/skills/acceptance-criteria/examples.md`, which is two hops from the description. It is allowed
because `examples.md` is a fixture the reader executes rather than prose the reader reads — it is
deliberately half wrong, so `node scripts/lib/criteria.mjs` on it exits 1 by design. Peer side files do
cross-reference each other, which is one hop and not a chain.

**3. A description that fires on the situation, not on the skill's own name.** This is the rule that is
easiest to get wrong and most expensive when it is wrong. `house-rules` is the test case: its description
opens *"Use before writing or changing code that touches money, a price, an amount or a currency; calls any
API, service or webhook; checks a session, role or permission…"* and the phrase *house rules* appears nowhere
in it. **An agent about to add a field to a payment form does not think to ask for "house rules".** It is
thinking about a payment form, so the description has to be about payment forms.

**4. Every claim in a skill says what checks it, or says that nothing does.** A capability that overstates
its own enforcement has manufactured the exact belief this standard exists to remove. `house-rules` opens
with the fact that `package.json` declares no `lint` script, so no lint runs in the starter at all and every
tier-1 label in `docs/production-ready.md` is a design intent rather than a fact. `capture-a-learning` says
that no workflow, hook or required check calls `scripts/learn.mjs`. `work-the-loop` says that
`scripts/next.mjs` refuses nothing.

## The ten skills

Verified by reading each one. The third column is the honest one.

| Skill | What it produces | What checks the output |
|---|---|---|
| `build-loop` | the seven-step order from ticket to merge, and what each step must produce before the next may begin | `spec.yml` on the commit order and the board entry, `size.yml` on the ceiling. Nothing checks that explore, approve or review happened at all |
| `write-a-spec` | `docs/specs/<TICKET-ID>.md`, committed first and alone | `spec.yml` on arrival order, `criteria.yml` on the table. **Nothing reads the prose, and none should** — a check that graded prose is a check an agent writes to. The three sections a person must write are held up by a code owner reading the file |
| `acceptance-criteria` | an evidence cell that resolves to a file, a file plus a string, or a URL | `scripts/lib/criteria.mjs`, run by `criteria.yml` over the spec and the pull request body, and by `scripts/next.mjs` before it will hand over `implement`. It checks resolution only — never whether the artefact proves the criterion, and a skipped test resolves as well as a real one |
| `work-the-loop` | the one next step on this branch, derived from the branch name, the commits, the board, the pull request and open escalations | nothing on the host. `scripts/next.mjs` reports and refuses nothing; `scripts/stop-guard.mjs` blocks a turn while the next step is the agent's, which constrains our session and not the host — tier 1, harness only |
| `respond-to-review` | a fix that addresses the cause of a red check rather than the check | `gates.yml` catches a gate change riding inside an implementation commit. **Nothing distinguishes a cause from a symptom** — a test rewritten until it passes and a bug fixed are identical to a green dashboard. The advisory `red-on-base.yml` is the only push-back |
| `escalate` | a graded request a person can answer in two minutes, and `log/events/YYYY-MM-DD-short-slug.md` | nothing. No check reads `log/`, and the weekly hour is its only reader. An escalation nobody raised leaves no trace anywhere |
| `operate-app` | `.evidence/<TICKET-ID>/` with a `manifest.md` that names what it could **not** prove | `evidence.yml` uploads what is there and **never fails for a missing artefact**, deliberately, because it cannot tell whether a ticket needed any. `scripts/next.mjs` emits `attach-evidence` when the pull request's table does not resolve |
| `house-rules` | code on the five surfaces where a mistake is not recoverable — money, outbound calls, the auth boundary, data writes, design tokens | `CODEOWNERS` by path pattern and `gates.yml`'s mixing rule, and neither knows what the code does. **No lint runs in this starter** — `package.json` declares `verify`, `scan:secrets`, `format:check`, `coverage:changed`, `setup`, `test:file` and `selftest`, and no `lint`. The skill's second section says so before it says anything else |
| `capture-a-learning` | appended lines in `docs/practices.md`, and a keep / revise / skip question put to a person | `node scripts/learn.mjs --self-test` passes 20 of 20, nine of them asserting a refusal — verified by running it. Nothing else: no workflow or hook calls `learn.mjs`, `docs/practices.md` does not exist in a fresh clone, and no check tells an append from a rewrite in a diff. `CODEOWNERS` on that path is the only mechanism outside the agent's reach |
| `garbage-collect` | a check that did not exist before, plus the migration of existing violations in the same pass | nothing, and here is why that is honest: the thing it produces *is* a check, so the output is enforcement rather than something to enforce. The count of `converted` dispositions in `log/events/` is the only evidence the loop converges, and `scripts/collect-week.mjs` prints how many comments it read so that "nothing to convert" cannot be confused with "nobody looked" |

## Honesty about the tier

**Not one of these ten skills prevents anything.** Every one is tier 3 by the ladder in
[enforcement](06-enforcement.md) — prose, loaded at the moment of a decision, which makes the right output
more likely and refuses nothing. The pilot measured that tier at zero of seven requirements present in
finished code.

That is not an argument against building it. It is the argument for building it **and not counting it**:

| Piece | Tier |
|---|---|
| a `SKILL.md` body an agent read before writing the code | not enforcement — nothing verifies it was read, or followed |
| the resolver naming its teacher in its failure output | not enforcement — it is the same refusal with a route out of it |
| `scripts/lib/criteria.mjs` refusing a cell | tier 1, on the host, through `criteria.yml` |
| `CODEOWNERS` on `docs/practices.md` and on `docs/design/criteria/` | tier 1, and only while the host requires owner review |
| `learn.mjs persist` refusing to rewrite or remove a line | tier 1, but **harness only** — a shell redirect into the file walks past it |

The last row is the shape to watch for. **Adding a practice is implementation; weakening or removing one is a
gate change** — a person, by hand, in its own commit, under an owner's review. A self-improving rule file plus
a loop that cannot stop is a loop able to lower its own bar, and nothing in a green run tells a new practice
from a weaker version of an old one.

## The six that are the standard

These six carry rules that a reader of this document has to see in full, because the exact words are what an
agent is given. The other four are inlined in [the repository](07-repository.md).

### `acceptance-criteria`

The pair for `criteria.yml`, and the row that was empty when that gate shipped. Note what it refuses to
pretend: it lists the words the resolver rejects, then says plainly that a skipped test and a test asserting
`true` both resolve, that a URL is matched and never fetched, and that a title assembled at runtime is a
false refusal. The section headed *At spec time the test does not exist yet* is the bind every session hits,
with three routes through it and the one that can be abused named as abusable.

`.claude/skills/acceptance-criteria/SKILL.md`

````markdown
---
name: acceptance-criteria
description: Use whenever you write or edit an acceptance criterion — in a spec, in a pull request body, in docs/design/criteria/ — and whenever the `criteria` check or `scripts/next.mjs` has refused a row. Gives the three cell forms that resolve, the exact words that are refused, and what to do with a criterion nothing can prove.
---

# Writing a criterion that resolves

`scripts/lib/criteria.mjs` asks one question of every row: **does this cell name something that exists
right now?** Three answers pass. Everything else is refused, and the cells that read most like diligence
are refused hardest — `verified` is the whole reason the resolver exists.

Run it on your own file before you push, and keep going until it exits 0:

```
node scripts/lib/criteria.mjs docs/specs/PULSE-123.md
```

It names the row, the line and the reason. The same resolver runs in `.github/workflows/criteria.yml` over
the pull request body and over `docs/specs/<TICKET-ID>.md`, and `scripts/next.mjs` will not hand you the
`implement` step while the spec's rows do not resolve.

## The three forms

| Form | Write the cell like this | It resolves because |
|---|---|---|
| A file | `` `scripts/board.mjs` `` | the path exists under the repository root and is a file |
| A file and the text inside it | `` `e2e/checkout.spec.ts` → "guest completes checkout" `` | the file exists **and** contains that literal string |
| A URL | `https://github.com/…/actions/runs/42` | the cell contains an `http(s)` token |

Prefer the second. It is the only form that says *which part* of the file, and it is the form a reviewer can
act on without opening anything else. A bare quoted title with no path also resolves, but only by searching
files whose path looks like a test — so a title living in `src/`, or in a language file outside `tests/`, is
invisible to that search. Name the path and the question does not arise.

A directory does not resolve. `docs/design/` is refused for being a directory; a file inside it is not.

**Never cite `.evidence/…` in the table.** It resolves on your machine and fails on CI, because `.gitignore`
excludes that directory and the runner's checkout does not contain it. Cite the test that produced the
artefact; the artefact itself belongs in `.evidence/<TICKET-ID>/manifest.md`, which is where `operate-app`
puts it and where `evidence.yml` uploads it from.

## The words that are refused

These are refused standing alone, and refused when the whole cell is made only of them plus filler:

> verified · verify · verifies · verification · done · tested · test · tests · testing · confirmed ·
> confirm · checked · check · yes · y · n/a · na · none · nil · ok · okay · pass · passed · passes ·
> passing · works · working · complete · completed · proven · proved · manual · manually · qa · qa'd ·
> good · fine · true · success · successful · ✓ · ✔ · ☑ · x

**Wrapping one does not help.** `` `verified` ``, `"verified"`, `**verified**`, `_verified_`,
`(verified)`, `[verified]`, `<verified>`, ``**`"verified"`**`` are all refused — the resolver strips matched
delimiter pairs repeatedly before it tests the word. It has to: quoting the word once defeated this check
completely, and that is the regression the resolver's own `--self-test` guards.

Describing the artefact in words is refused too. `Automated test with a sequence of readings; the ledger
extract showing the readings that were taken` is a good sentence and names no file — see `refusals.md` for
that one refused verbatim, with its fix.

## At spec time the test does not exist yet

This is the bind everybody hits. The spec is the branch's first commit, `next.mjs` wants its rows to resolve
before implementation starts, and the test you intend to write is not on disk. Three ways through, in order:

1. **Name a file that already exists.** Extending a suite the repository already has resolves today.
2. **Write the failing test first, then the row resolves.** The resolver reads text; it does not run
   anything. So the moment `e2e/checkout.spec.ts` exists containing `guest completes checkout`, that row
   resolves — red. This is the honest route and it is what `red-on-base` wants anyway.
3. **Nothing could ever prove it.** Then the row does not belong in the table. See below.

Route 2 is also the one you can abuse: a `test.skip` whose body asserts nothing resolves exactly as well as
a real test. The resolver cannot tell them apart and does not claim to.

## A criterion nothing can prove

That is a **class B escalation** — "a criterion cannot be proven as written; no artefact would settle it" —
and it is a question for a person *before* it is code. Use the `escalate` skill: raise it, and leave the
`log/events/` record.

Then the row leaves the criteria table and the fact goes under **What this will not verify** in the spec, in
words. Do not put the explanation in the evidence cell; a cell holding a sentence about why there is no
artefact is exactly what the resolver refuses, and it reads to everyone downstream as though the criterion
were still covered.

The other half of this, and the more common repair: the criterion is not unprovable, it is too broad. A
criterion promising "a full day's work" cannot be proven; the same criterion narrowed to the three actions
somebody actually recorded can. `worked-examples.md` has eight of these from a real annexe, with the weaker
version and the reason it was rejected.

## What this does not check, and none of these are small

- **Whether the artefact proves the criterion.** `| Totals are correct | README.md |` resolves, because the
  file is there. That judgement is the reviewer's, and the review agent is pointed at this column for it.
- **Whether the test asserts anything.** A skipped test, and a test called `checkout works` that asserts
  `true`, both resolve. `red-on-base` pushes back on a *changed* test; nothing pushes back on a skipped one.
- **Whether the URL is a 404.** It is matched, never fetched.
- **A title assembled at runtime** — ``it(`${name} works`)`` — is not found and reads as prose. That is a
  false refusal. Name the path instead of the title.
- **A table inside a fenced code block is invisible**, so a criteria table pasted into an example block is
  not read at all.
- **`docs/design/criteria/*.md` is not read by `criteria.yml`.** That file is checked by a person at
  Kickoff, counting empty cells and requiring zero. It is also a protected path in `gates.yml` and in
  `CODEOWNERS`: propose a change there, never approve one, and never in an implementation commit.
- **`criteria.yml` describes itself as advisory** until it has run on real work. Treat it as blocking
  anyway; a row that does not resolve is a row nobody can act on.

## The detail, when you need it

- `evidence-forms.md` — resolution order as the code does it, what counts as a path, what the bare-title
  search actually searches, and a resolving cell per kind of criterion: browser test, unit test, query,
  screenshot, endpoint, migration, alarm.
- `refusals.md` — every refusal shape with the resolver's real output pasted, and the fix for each.
- `worked-examples.md` — before/after criteria from `annexe-a.md`, including four where a weaker version was
  rejected and why.
````

### `work-the-loop`

The pair for the next-step deriver, which was built and given no caller. Its first three lines are the whole
skill; everything after is detail on them. The table of steps is precedence-ordered, so no step fires while an
earlier obligation is outstanding, and eight of the sixteen are marked as a person's — with a second table
naming, for five of those eight, the specific way an agent takes a step that is not its own.

`.claude/skills/work-the-loop/SKILL.md`

````markdown
---
name: work-the-loop
description: Use at the start of any session on a ticket, before choosing what to do next, and whenever a turn will not end, a hook pushes back, or you cannot tell where the branch stands. Covers `node scripts/next.mjs`, every step it can emit, the steps that are a person's, the commit order two of our gates disagree about, and when the loop lets go.
---

# Working a ticket here

**Run `node scripts/next.mjs`. Do the one thing it names. Run it again.**

The rest of this file is detail on that sentence.

The derivation stores nothing. It reads the branch name, the commits on the branch, `tasks/board.md`,
the pull request through `gh`, the criteria table in `docs/specs/<TICKET-ID>.md`, and open escalations in
`log/events/` — then returns exactly one directive. There is no state file to go stale, and no way to
report a position the repository is not actually in. Re-run it after every commit, every push and every
edit to the pull request; it is cheap, and it is never the previous answer.

Real output on `main` today:

```
$ node scripts/next.mjs
pick-ticket
  why:     the branch is "main" and no ticket id can be read from it
  do:      node scripts/board.mjs --index   # then: git checkout -B <TICKET-ID> origin/main
  waiting on: a person
```

## Every step it can emit

Precedence, top to bottom — the first condition that holds is the answer, so no step fires while an
earlier obligation is outstanding. `references/steps.md` has what to do for each one, with commands.

| Step | Whose | Fires when |
|---|---|---|
| `answer-escalation` | a person | an open escalation in `log/events/` names this ticket or no ticket |
| `pick-ticket` | a person | no ticket id can be read from the branch name |
| `write-spec` | **yours** | no commits, or no `docs/specs/<TICKET-ID>.md` |
| `fix-spec-order` | a person | the spec is not the branch's first commit, or not alone in it |
| `add-board-entry` | **yours** | `tasks/board.md` has no entry for the ticket |
| `resolve-criteria` | a person | a criterion names no evidence a script can resolve |
| `implement` | **yours** | spec in place, criteria resolve, no commit past the spec yet |
| `open-pr` | **yours** | work beyond the spec commit and no pull request |
| `split-ticket` | **yours** | the `size` check is red |
| `fix-red-check` | **yours** | any other check is red |
| `attach-evidence` | **yours** | the criteria table in the pull request **body** does not resolve |
| `address-review` | **yours** | `reviewDecision` is `CHANGES_REQUESTED` |
| `await-checks` | a person | checks are still running |
| `await-review` | a person | review has not been given |
| `merge` | a person | approved and green |
| `done` | a person | the pull request is no longer open |

## The steps that are a person's

`answer-escalation`, `pick-ticket`, `fix-spec-order`, `resolve-criteria`, `await-checks`, `await-review`,
`merge`, `done`. On all eight, `node scripts/next.mjs --assert` exits **0** and the Stop hook lets the
turn end.

That exit code is not permission. It is the loop declining to hold a session hostage to somebody who has
gone home — the work is still not yours. Five of the eight are ones an agent is tempted to take anyway,
and taking them is the failure this skill exists to prevent:

| Step | The failure | Do this instead |
|---|---|---|
| `pick-ticket` | inventing a ticket id and branching on it | read `tasks/board.md`, report what is open, stop |
| `fix-spec-order` | rebasing to move the spec commit | say the branch's history is wrong and stop. `git rebase*` is in the `ask` list in `.claude/settings.json`, so you cannot run it silently anyway |
| `resolve-criteria` | putting a word in the evidence cell so the resolver passes | escalate class B — the criterion cannot be proven as written. Only a person changes a criterion |
| `await-review` | reviewing your own work, or nudging it green | stop. `gh pr review*--approve*` is in the `deny` list |
| `merge` | merging because everything is green | stop. `gh pr merge*` is in the `deny` list |

Anything you stop on gets an escalation record: the `escalate` skill has the six classes and the file to
write in `log/events/`.

## The commit order two of our gates disagree about

Fixed, and rejected rather than warned about:

1. **`docs/specs/<TICKET-ID>.md` alone** — no board edit, no anything else in that commit.
2. **The board entry** and the regenerated index and view.
3. **Implementation**, one commit per step.

Two rules in `.github/workflows/spec.yml` collide unless they are ordered that way: *the spec is the
branch's first commit, alone* and *the ticket must have a board entry*. Put both in the first commit and
`spec.yml` fails. `facts.specFirst` reads the spec path out of that workflow rather than restating it, so
`write-spec` → `fix-spec-order` → `add-board-entry` is the same order the gate will judge you by.

The `PostToolUse` hook regenerates `tasks/board.html` and the index table in `board.md` on every write, so
step 2 is: edit the entry, then commit whatever the hook rewrote. Never hand-edit either generated block.

## Why a turn will not end

`scripts/stop-guard.mjs` runs on `Stop`. It re-derives position and blocks the turn while the next step is
**yours**, restating what is owed. If you see that text, you have not been overridden and nothing has gone
wrong: run `node scripts/next.mjs` and take the step it names.

It lets go four ways, so a stuck loop is not a trap: the next step is a person's; the position has not
moved across more than 2 consecutive blocks; more than 40 blocks on this ticket; or 240 minutes past the
first block. Any error at all also releases it. `references/loop-mechanics.md` has the counters, the
environment variables that move them, `--why`, `--reset`, and the `--json` contract field by field.

If a release fires while work is genuinely outstanding, that is a signal you are looping, not a licence to
walk away — say what is left in your closing message.

## What none of this checks

`next.mjs` **refuses nothing**. It reports, and a session is free to ignore it; the refusals live in the
workflows on the host and in the Stop hook. It cannot tell whether the code is any good, whether the spec
is right, or whether a criterion that resolves to a test is a criterion that test actually proves. Its
reading of a pull request is only as fresh as the last `gh` call. And it cannot see work that leaves no
trace in git, on the board or on the pull request — so a branch worked by hand outside these conventions
looks, correctly, like a branch with nothing done.

`scripts/orient.mjs` puts the same directive in front of a new session at `SessionStart`. It is not
enforcement either: nothing verifies that it was read. It is silent when the branch carries no ticket, so
no orientation text is not a fault.
````

### `write-a-spec`

The pair for `spec.yml`. The section that matters most is the one headed *Three sections are not yours to
write*, and it ends with the sentence a capability layer has to be willing to write about itself: **nothing
checks this.** No job reads a spec's prose, and none should — a check that graded prose is a check an agent
writes to.

`.claude/skills/write-a-spec/SKILL.md`

````markdown
---
name: write-a-spec
description: Use whenever you are writing, fixing or about to commit `docs/specs/<TICKET>.md` — starting a ticket, running /spec, a red `spec` or `criteria` check, or `node scripts/next.mjs` reporting write-spec, fix-spec-order, add-board-entry or resolve-criteria. Gives the order of operations the workflow enforces, the self-check that catches every mechanical failure before you push, and the sections you are not permitted to draft.
---

# Writing a spec

**A spec is a record of what was agreed before code existed.** `spec.yml` cannot check that a person
agreed — approval is a review on the pull request, not a field in the file. It checks the one thing that
makes approval mean anything: that the spec arrived **first**, alone, and has not moved since.

So getting it right first time is not tidiness. The two failures that cost most — a first commit that is not
the spec alone, and a criteria table corrected afterwards — are repaired only by rewriting history or by a
spec revision the workflow makes visible and a person has to approve again.

## Three sections are not yours to write

This is the most important line in this file. Drafting a plausible document is easy; reviewing a plausible
document is easy to do badly. Three things in a spec exist only as proof that a person actually read it:

| Spec section | Who writes it | Why not you |
|---|---|---|
| **Questions and answers** — the answers | the developer, in their own words | An answer you supplied is a question you did not ask |
| **Out of scope** | the developer | A scope boundary is escalation class A. You may propose; only a person decides |
| **What this will not verify** | the developer | If you write it, it will be the list you already know you covered |

You draft the **questions**. You may draft everything else in the template. If the answers, the
out-of-scope list or the will-not-verify list came from you, the review did not happen and the spec is
worth nothing to the agent that implements it.

Leave an unanswered question in place, marked, and stop. An unanswered question is a finding — see
`escalate`, class B. Never fill it with your best guess and never delete it because you worked around it.

**Nothing checks this.** No job reads the spec's prose, and none should — a check that graded prose is a
check an agent writes to. It is held up by a code owner reading the file, which is why the file is short.

## What the machine actually checks

Every row but the last is derived from `.github/workflows/spec.yml`. Nothing else in a spec is checked by
anything, anywhere.

| Rule | Where | Failure |
|---|---|---|
| Branch starts `^[A-Z][A-Z0-9]+-[0-9]+` | `spec.yml` | fails |
| `docs/specs/<TICKET>.md` exists at HEAD | `spec.yml` | fails |
| It is the branch's **first** commit and the **only** file in it | `spec.yml` | fails |
| `<TICKET>` has a `# <TICKET>` entry in `tasks/board.md` | `spec.yml` | fails |
| A `DONE` entry has a `## Resolution` section | `spec.yml` | fails |
| The spec was not edited in a later commit | `spec.yml` | **warns** — allowed, but re-approval is owed |
| Every criteria row names evidence that resolves | `criteria.yml` | job exits 1; that workflow's own header calls itself advisory until it has run on real work, so it may or may not block the merge |

Exact error text, and the recovery for each, are in `spec-yml.md` beside this file. Read it when one goes
red — not before.

## The order, which is fixed

Two of our own rules collide unless they are ordered: *the spec is the first commit, alone* and *the ticket
must be on the board*. So:

```bash
git checkout -B PULSE-142-guest-checkout origin/main   # id first, then any slug
# write docs/specs/PULSE-142.md from docs/specs/_template.md
node scripts/lib/criteria.mjs docs/specs/PULSE-142.md  # must exit 0 BEFORE you commit
git add docs/specs/PULSE-142.md                        # this path and nothing else
git commit -m "docs(PULSE-142): spec"
# now the board entry, and only now
git add tasks/board.md tasks/board.html
git commit -m "docs(PULSE-142): board entry"
```

`git add -A` and `git commit -a` are how this rule gets broken. Writing any file fires a `PostToolUse`
hook that runs `node scripts/board.mjs --index && node scripts/board.mjs --html`, so by the time you commit
the spec there are usually modified board files in the tree. Stage the one path. Run `git status -sb` first
if you are unsure.

## The criteria table

`criteria.yml` resolves the **spec's** table as well as the pull request's, and `next.mjs` refuses to enter
implementation while it does not resolve. The rules for what makes an evidence cell resolve are in the
`acceptance-criteria` skill. They are stated once, there — do not re-derive them here.

Four things are specific to the spec file and are not in that skill:

**Fill exactly one table.** The resolver concatenates the rows of every criteria table in the file. Copy
the criteria into `## Acceptance criteria` as the bulleted list the template shows, and put the resolvable
table under `## How each criterion will be proven`. Put a table in both and every row in both must resolve.

**Delete the template's placeholder row.** `| … | the named test / the screenshot / the response |` is
refused — verified: the untouched template fails `criteria.mjs` with *no test file under root contains "the
named test / the screenshot / the response"*.

**Get it right before the first commit.** Fixing the table afterwards is a spec revision, which `spec.yml`
warns about and which invalidates the approval that was given to the earlier text.

**A named test may sit on disk without being in the spec commit.** The resolver reads the working tree, not
git — verified: an untracked `e2e/checkout.spec.ts` resolves its row. So when the test does not exist yet,
write the failing test, leave it out of `git add`, and commit the spec alone; the test arrives in the
implementation commit that follows. What breaks is opening the pull request before that commit exists, because
`criteria.yml` resolves the spec against the merge commit and the file will not be there. The routes through
this bind are in `acceptance-criteria`.

## Check it yourself, before the commit and before the push

```bash
node scripts/lib/criteria.mjs docs/specs/<TICKET>.md   # every row; names the row and why
node scripts/next.mjs                                  # what is still owed on this branch
```

Run the first, read the error, fix the row, run it again. Only commit when it exits 0 — it is the same
resolver `criteria.yml` runs, so a pass here is a pass there.

The second reproduces `spec.yml`'s first-commit rule locally, from the same source: `scripts/lib/facts.mjs`
reads the rule out of the workflow rather than restating it. After the spec commit it should report
`add-board-entry`, and after the board commit `implement`. `work-the-loop` covers every other step it can
emit and which of them are a person's.

One local hook fires before either: `pre-commit` runs `bun run format:check` on staged markdown, and in the
starter as shipped that script is a stub that exits 1. If it fails on a spec you have not touched since, that
is the stub and not your file — wire the formatter. Do not reach for `--no-verify`.

## What none of this reaches

`spec.yml` proves the spec came first. It cannot tell you the spec is any good, that the patterns it names
are the right ones, that the plan is achievable, or that a criterion resolving to a test is a criterion that
test proves. `worked-spec.md` beside this file is one complete filled example, including how an unanswered
question and an unprovable criterion are left visible rather than quietly closed.
````

### `house-rules`

Not paired with a gate at all, and that is why it is here. `docs/production-ready.md` is the standard; a
standard is read when somebody thinks to read it, and nobody thinks to read one while adding a field to a
payment form. This is the same rules arriving at the moment the code is written — and its second section
exists to stop the reader trusting a tier number that the repository does not yet honour.

`.claude/skills/house-rules/SKILL.md`

````markdown
---
name: house-rules
description: Use before writing or changing code that touches money, a price, an amount or a currency; calls any API, service or webhook; checks a session, role or permission, or adds a dev bypass; runs a migration, seed or backfill, or anything writing to a database it did not create; retries an operation or puts one on a queue or schedule; or sets a colour, spacing, radius or type value. Gives the rule for that surface, the shape that violates it, the shape that satisfies it, and whether anything here checks it.
---

# The rules for the surfaces where a mistake is not recoverable

`docs/production-ready.md` is the standard. It is a document, so it is read when somebody thinks to read
it — and nobody thinks to read a standard while adding a field to a payment form. This skill is the same
rules, arriving at the moment the code is being written.

## Read this before you trust a tier number

`docs/production-ready.md` labels most of these rules **tier 1 — lint or structural test**. In this
repository, right now, that is a design intent and not a fact:

- `package.json` declares `verify`, `scan:secrets`, `format:check`, `coverage:changed`, `setup`,
  `test:file`, `selftest`. It does **not** declare `lint`, `typecheck`, `build`, `test` or
  `test:coverage`.
- `scripts/verify.mjs` requires all five. With them absent it exits 1 on "Not every gate is wired"
  rather than reporting green — which is correct, and it also means **no lint runs here at all.**
- There is no `src/`, no `migrations/`, and no lint configuration of any kind in the tree.

So a tier-1 label on a line below means *the check is the deliverable*. Until the project wires it, the
rule is prose, and prose is the class of requirement our own pilot measured at 0 of 7 present in
finished code against 8 of 8 for requirements with a check attached.

Say which of these you satisfied and which you could not verify. Do not report a rule as met because you
followed it — that is the claim `scripts/lib/criteria.mjs` refuses in an evidence cell, for the same reason.

## Which file to read

Load the one for the surface you are touching. They do not overlap; reading a second one you do not need
costs you and buys nothing.

| You are about to | Read |
|---|---|
| Store, add, display, discount, tax or refund an amount of money | `money.md` |
| Call an API, a webhook or another service; retry something; put work on a queue or a schedule | `outbound-calls.md` |
| Check a session, role or permission; add a dev bypass or impersonation; expose an endpoint; log a field | `auth-boundary.md` |
| Write a migration, a seed, a backfill, or any script that connects to a database | `data-writes.md` |
| Set a colour, spacing, radius, font size, or add a component that renders one | `design-tokens.md` |

Anything a person can see or click also needs evidence that something operated it — that is the
`operate-app` skill, not this one.

## Two rules that apply to all five

**Name the path so `CODEOWNERS` covers it.** Protection here is by path pattern, not by intent. The
protected patterns are `/src/**/payment*/`, `/src/**/billing*/`, `/src/**/auth*/`, `/src/**/pii*/`,
`/migrations/`, `/prisma/migrations/`. Money code in `src/lib/pricing/` is outside every one of them and
merges with no owner review. So either put it under a directory the pattern matches, or add your path to
`CODEOWNERS` — which is itself a gate path, so it is **its own commit**.

**The check you leave behind lands differently depending on what it is.** `gates.yml` fails any commit
that mixes a gate path with implementation, and it classifies these as gate paths:
`.github/workflows/*`, `lefthook.yml`, `CODEOWNERS`, `CLAUDE.md`, `.claude/*`,
`docs/design/criteria/*`, `biome.json`, `.eslintrc*`, `eslint.config.*`, `ruff.toml`, jest/vitest/bunfig
config, and the named scripts `verify.mjs`, `scan-secrets.mjs`, `changed-line-coverage.mjs`, `board.mjs`,
`break-it.mjs`, `red-on-base.mjs`.

| The check you are adding | Where it can go |
|---|---|
| A new test for new code | the implementation commit — an added test path is implementation |
| A new script, e.g. `scripts/check-money.mjs` | the implementation commit passes `gates.yml`, but `/scripts/` is in `CODEOWNERS`, so it needs an owner's review |
| A lint config — `biome.json`, `eslint.config.*`, `ruff.toml` | **its own commit.** Adding it beside implementation fails `gates.yml` |
| Editing an existing test, a threshold, or CI | its own commit, and say why. Never beside implementation |

Note the gap, because it is real: `gates.yml` does not list `stylelint.config.*`, `.stylelintrc*` or any
Tailwind config. `CODEOWNERS` does list the stylelint ones. So turning a stylelint rule off inside a
feature commit passes the mixing check and is caught only by an owner reading the diff. If you wire a
linter whose config file is not in that list, adding it to `is_gate_path` in `.github/workflows/gates.yml`
is part of wiring it.

## What actually enforces anything in this repository today

Everything else in the tables below reduces to one of these, or to nothing.

| Mechanism | What it really does | Where it stops |
|---|---|---|
| `gates.yml` — mixing check | Fails a PR when one commit changes a gate path and implementation | Only the paths listed above. Only on a pull request |
| `CODEOWNERS` | Forces review by a second person on the protected patterns | Path patterns only. Needs `require_code_owner_reviews` on the host — `perimeter.yml` is what checks that |
| `scripts/scan-secrets.mjs` | Pre-commit, staged lines, 11 known key shapes | A hint, not a gate. `--no-verify` walks past it, and it only knows the shapes in its list |
| `scan.yml` | Daily, reads the host's Dependabot and code-scanning alerts; fails if scanning is off | Nothing to do with your diff |
| `REVIEW.md` step 3 | The review agent walks the tier-2 lines of `docs/production-ready.md` | Judgement, so probabilistic. Written down and auditable, not binding |
| `.claude/settings.json` | Denies force-push, pushes to main, `gh pr merge`, `--no-verify`; asks on `rm -rf`, and on edits to workflows, `CODEOWNERS`, `CLAUDE.md`, `.claude/**`, `docs/design/criteria/**`, `scripts/lib/**` | Your session only. It constrains you, not CI, and not a person |

## What this skill cannot do

It cannot make an unchecked rule hold. Standing context and skill bodies are **generative** — they make
the right thing more likely — and they are not **preventative**. A live project had twenty design rules in
standing context and still shipped a 69-file feature commit that switched four accessibility lint rules
off; the defect one of them exists to catch was fixed nineteen days later.

So when you find a rule here that nothing checks, the response is not to be careful. It is to leave a
check behind — `garbage-collect` is the procedure — or to say plainly, in the pull request, that this one
is unverified.
````

### `capture-a-learning`

The pair for the learning loop. It is the clearest statement of the three-owner split from
[orientation](20-orientation.md): the deterministic half writes, the model performs one comparison, and a
person decides keep / revise / skip. The tool contains no model call, which is the design. Read the closing
section for why the path can only ever append.

`.claude/skills/capture-a-learning/SKILL.md`

````markdown
---
name: capture-a-learning
description: Use when a ticket closes, when filling a pull request's "What we learned" section, or when an escalation or review finding should become a durable practice. Runs `scripts/learn.mjs surface`, asks the one contradiction question against `docs/practices.md`, puts keep/revise/skip to a person, then calls `persist`.
---

# Capture a learning

`scripts/learn.mjs` is the deterministic half of the learning loop and it contains no model call. That is
the design, not an omission — automating this is three decisions with three different owners:

| Layer | Owner | |
|---|---|---|
| detect, surface, route, **write** | `scripts/learn.mjs` | no model anywhere in the path |
| does this contradict an existing practice? | **you** | one comparison. Not a decision |
| keep / revise / skip | **a person** | never delegated |

You perform the middle row and hand over to the third. You do not decide what is kept, and you do not write
`docs/practices.md` yourself — `persist` does, and only ever by appending.

## When to run it

- **After a ticket closes.** `surface` reads the **Findings** of board entries whose State begins with
  `DONE`. Before that, the ticket has not finished teaching and its findings are not candidates.
- **At the pull request's "What we learned that was not in the design document" section.** The entry is
  usually not DONE yet there, so `surface` shows your `log/events/` files and none of this ticket's board
  findings. That is the tool behaving correctly, not a gap to work around.
- **Not on a schedule.** The weekly hour belongs to `garbage-collect`, which turns a repeated correction
  into a *check*. This records a decision, which is a different thing.

## 1 — Surface

```bash
node scripts/learn.mjs surface
```

Read-only. Candidates as JSON on stdout, notes on stderr, exit 0. In the starter as it ships, the real
output is:

```
[]
note: log/events/ holds no event files, so nothing was logged to learn from.
note: no candidates. Either nothing was logged this cycle, or nothing is being logged.
```

Read that literally. An empty set straight after closing a ticket that had findings means the ticket left no
trace in `log/events/` or in a DONE entry's Findings — and that absence is the more valuable thing to report,
because it is why next month's session rediscovers the same thing.

With material on disk, one object per candidate:

```json
[
  {
    "id": "ev-05a60ddb",
    "source": "log/events/2026-08-05-quiet-test.md",
    "text": "a new test asserted nothing and still reported full coverage on the lines it touched",
    "proposed_heading": "Testing",
    "existing_related": ["Testing"]
  }
]
```

`id` is a hash of source plus text, which is what makes a re-run a no-op. `proposed_heading` is first-match
keyword routing, deliberately crude and yours to overwrite; unmatched text routes to `Unsorted` rather than
to the nearest guess. `existing_related` is headings sharing two significant words — **it cannot tell
agreement from contradiction**, which is exactly the comparison the tool is not allowed to make. A candidate
already written keeps appearing on every later run; that noise is the price of `persist` being idempotent.

## 2 — The one question

Read `docs/practices.md`, starting with the headings named in `existing_related`. Per candidate, exactly one
of three verdicts. You report it; you do not act on it.

| Verdict | What it looks like | What you write |
|---|---|---|
| **New** | nothing on file speaks to this subject | the proposed line, under a heading |
| **Covered** | a line on file already says it | quote that line, propose skip |
| **Contradicts** | a line on file says the opposite, or the candidate is the weaker of the two | quote **both** lines verbatim and stop |

The third verdict is why this step exists. A kept candidate that contradicts a line on file leaves
`docs/practices.md` holding two rules, and the weaker one is what anybody in a hurry follows. `persist`
compares ids, not meaning, so it cannot see this, and nothing else in the repository can either. If you
cannot tell whether two lines conflict, say so — an unresolved comparison handed to a person is a working
answer; a guess is not. `contradiction-check.md` here has the worked comparisons and how to word a line so
it can be checked later.

**`docs/practices.md` does not exist in a fresh clone, and nothing in this repository reads it** — no gate,
no hook, no skill loads it. A practice here is a decision recorded where a code owner will see it, not
enforcement. If the learning needs teeth, that is `garbage-collect`: a lint, a structural test, a required
check, or a rule in `CLAUDE.md`.

## 3 — Put it to a person

One message, one block per candidate:

```markdown
**Learning candidates** — 2 surfaced. keep / revise / skip on each.

**`ev-05a60ddb`** · new · from `log/events/2026-08-05-quiet-test.md`
> a new test asserted nothing and still reported full coverage on the lines it touched

Proposed, under **Testing**: A test that asserts nothing is a coverage report. Every new test names the
behaviour it would fail on.
Nothing under Testing speaks to assertion-free tests; the heading matched on shared wording, not the rule.

**`bd-4cad0179`** · contradicts · from `tasks/board.md#PULSE-142`
> The retry wrapper had no timeout, so a hung upstream held the request open
On file, under Operational: `- Retries are bounded by the caller's deadline, not by a per-call timeout`
Two rules for the same call. I have not chosen between them.
```

Then wait. **Nothing checks that a person answered.** `persist` writes `keep: true` identically whether it
came from a person or from you, and afterwards the two are indistinguishable on disk. What notices is the
code-owner review on the commit, which is after the fact. Asking is the cheap half — do not skip it because
the tool would not catch you.

A practice that would change what the client accepts, or weaken something already on file, is `escalate`
class A and leaves a `log/events/` record.

## 4 — Persist

```bash
SEL="${TMPDIR:-/tmp}/learn-selections.json"   # a hand-off, not an artefact. Nothing in .gitignore covers it
node scripts/learn.mjs persist --selections "$SEL"
```

One row per candidate you asked about — `{id, keep, heading, text}`, `keep` a real boolean. Any bad row
refuses the whole batch and writes nothing, because a half-written decision looks exactly like a decision
made properly. `selections.md` in this directory has the shape and every refusal.

```
appended ev-05a60ddb under "Testing"
appended bd-4cad0179 under "Operational" (new heading)
skip     ev-697ef041 — not written
```

Then close the loop on the source: an event whose learning was kept gets its `disposition:` set in
`log/events/`, per `log/README.md`. `persist` does not touch those files.

## Why it can only ever append

**Adding a practice is implementation. Weakening or removing one is a gate change.**

A self-improving rule file plus an agent that cannot stop is a loop able to lower its own bar: if this path
can add a practice, it can add a weaker version of one already there, and nothing in a green run tells those
apart — the run is green either way. Append-only takes that move off the board, so the file can be trusted
without anyone auditing every write.

`persist` refuses, exits 1 and writes nothing when a selection would rewrite a line, move one to another
heading, remove one, name an id `surface` did not produce, or carry a `keep` that is not a real boolean.
Those refusals are the tested half: `node scripts/learn.mjs --self-test` passes 20/20, and nine of its
twenty cases assert a refusal.

**What none of this enforces.** No workflow, hook or required check calls `scripts/learn.mjs`, so skipping
this ritual makes nothing go red. The guarantee covers only writes that go through `persist`: an `Edit` to
`docs/practices.md` raises an `ask` prompt from `.claude/settings.json`, a shell redirect into it raises
nothing, and `gates.yml` does not treat the file as a gate path — so no check tells an append from a rewrite
in a diff.

The one mechanism outside the agent's reach is `CODEOWNERS`, which puts `/docs/practices.md` under
`@devx/tech-leads`, and even that only bites if the host requires owner review. Removing a practice is a
person editing the file by hand, in its own commit, under that review. There is no flag here that does it,
and it is not your call to make.
````

### `respond-to-review`

The pair for every red check at once, and the one skill whose subject is a temptation rather than a
procedure. Its second table lists six thoughts an agent has reasoned its way into — *this test was already
flaky*, *the lint rule is wrong about this line*, *it only needs `continue-on-error` until this lands* — and
names each as what it actually is. The real example at the end is the commit that `gates.yml` exists because
of.

`.claude/skills/respond-to-review/SKILL.md`

````markdown
---
name: respond-to-review
description: Use when a check on the pull request is red, when a reviewer asked for changes, or when `node scripts/next.mjs` says fix-red-check, split-ticket, address-review or attach-evidence. Names the usual cause and the legitimate fix for each red check, and the point at which this stops being yours.
---

# Something came back red

**Fix the cause. Never the check.**

A red check is a claim about the code. Making the claim go away without changing the code — deleting the
test, lowering the threshold, adding a skip, turning a lint rule off, adding a label — leaves the defect
and removes the thing that would have found it next time. That is the one failure mode this file exists to
prevent, and it is the failure mode an agent under pressure reaches for first.

Making a check quieter is sometimes the right answer. It is never the right answer *in this commit*. It is
a **gate change**: its own commit, a reason in the body, and a code owner's approval. `references/gates.md`
has how to land one.

## Start by reading the actual failure

Not the check name. The step that failed, and its output.

```bash
node scripts/next.mjs                 # which step is owed, and whether it is yours
gh pr checks <PR>                     # which checks are red
gh run view <RUN-ID> --log-failed     # the failing step's output, which names the cause
```

Guessing the cause from the check name is how a `verify` failure gets "fixed" by editing a test when the
red was `format:check`.

## What each one means, and what to do

| Red check, or `next.mjs` step | The usual cause | The legitimate fix | Detail |
|---|---|---|---|
| `size` / `split-ticket` | one ticket described with an "and" | split the branch into two. The override is a **label**, and the author cannot apply it | `references/size.md` |
| `spec` / `fix-spec-order` | the spec is not the branch's first commit, alone | usually a rebase — **a person decides**, not you | `references/spec.md` |
| `gates` | a gate change rode along in an implementation commit | split the commit; the gate change goes alone | `references/gates.md` |
| `verify` | one of seven sub-gates, or one of three other steps | find *which* before touching anything | `references/verify.md` |
| `criteria` / `resolve-criteria` | a cell says `verified` where an artefact belongs | rewrite the cell to name the artefact | the `acceptance-criteria` skill |
| `attach-evidence` | the artefact that would prove a criterion does not exist yet | produce it, then rewrite the row | the `operate-app` skill produces it; `acceptance-criteria` shapes the cell |
| `address-review` | a graded finding has no disposition | fix it, or dismiss it in writing | `references/reviewer.md` |

Two things about the colours before you start working one.

**Only four of these block the merge.** `size`, `gates`, `spec` and `verify` are required. `review`,
`red-on-base`, `evidence` and `criteria` are advisory — they report, and merging ignores them. So a red
advisory check is something you fix because it is true, not because it is in your way. That split is
asserted in `.github/workflows/perimeter.yml`; do not infer it from the page.

**`evidence` going green means nothing about evidence.** `evidence.yml` deliberately never fails for
missing artefacts — it cannot tell whether a ticket needed any, and a check that guessed would teach people
to screenshot nothing. It uploads what is there and says plainly when there is nothing. The person reading
the criteria table decides. `attach-evidence` from `scripts/next.mjs` is the signal that fires instead.

## The temptation, and what it actually is

Every row here is something an agent has reasoned its way into. The reasoning is the tell.

| The thought | What it actually is | Do this instead |
|---|---|---|
| "This test was already flaky" | deleting evidence that a behaviour works | reproduce the flake, or say in the PR that you could not, and leave the test |
| "80% changed-line coverage is unreasonable here" | lowering a threshold inside a feature | write the test, or say plainly which lines are uncovered and why |
| "The lint rule is wrong about this line" | switching a rule off for the repository | suppress the single line with a comment naming the reason, or raise it as a gate change |
| "It only needs `continue-on-error` until this lands" | turning a gate into a decoration | let it stay red and say so; a red advisory check is an honest state |
| "The diff is big because the refactor was necessary" | a ticket that was two tickets | split the branch |
| "I'll add the `size-override` label so this can move" | a bypass — `size.yml` reads who applied it | ask a tech lead, in writing, with the reason splitting failed |

**The real one.** A project with twenty design rules in its agent context, a doctrine document, and a
bespoke pre-push guard shipped one commit titled `feat(us2): six masters — REST API + React UI, wired end
to end`, touching 69 files, which among them turned four accessibility rules off in `biome.json`. One was
`noLabelWithoutControl`. Nineteen days later a commit titled "associate every form label with its control"
fixed the defect that rule exists to catch — and found the labels had never been associated anywhere in
the product. Nothing there was a missing lint. The lint existed, and was switched off inside a commit
nobody was going to read configuration in. `gates.yml` exists because of that commit.

## Two attempts, then it is not yours

Fix the cause and push. If the same check goes red a second time on the same cause, stop. That is
class F in the `escalate` skill: looping on a red gate burns budget and produces no evidence.

Stop immediately, without a second attempt, when:

- you believe the check itself is wrong — class D, the most under-reported class, and working around a
  wrong gate quietly leaves the gate wrong
- the fix requires touching a protected path: an existing test, a threshold, CI or hook config,
  `CODEOWNERS`, `CLAUDE.md`, `.claude/`, or `docs/design/criteria/`
- the fix requires reordering the spec commit — `scripts/next.mjs` marks `fix-spec-order` as a person's
  step because it cannot be done without a rebase of what was already approved. Splitting a mixed
  implementation commit on your own branch is *not* this case, and is yours
- a criterion cannot be proven by any artefact — class B, and it is cheaper to ask now than after the
  implementation exists

Leave the record: `log/events/YYYY-MM-DD-short-slug.md`, schema in `log/README.md`. Write it even when the
answer arrives in a minute — an easy question is the kind most likely to be asked again, and that file is
the only thing that will notice.

## What this repository cannot check about your response

Say these out loud rather than relying on them being caught.

- A gate change that arrives **alone**, in its own commit, passes `gates.yml` completely. Deleting a test
  in a gate-only commit is legal to the checks. The only thing standing there is a reviewer reading the
  diff, which is why the gate surface is item 1 in `REVIEW.md`.
- `gates.yml`'s protected-path list is a literal list. `biome.json`, `.eslintrc*`, `eslint.config.*` and
  `ruff.toml` are on it; `stylelint.config.*` is not — that one is caught by `CODEOWNERS` alone.
- `continue-on-error`, `if: false` and a trailing `|| true` are detected only in `.github/workflows/**`.
  The skipped-test patterns are detected repository-wide.
- Nothing checks that your fix addressed the cause rather than the symptom. A test rewritten until it
  passes and a bug fixed look identical to a green dashboard. `red-on-base.yml` is the only check that
  pushes back on it, and it is advisory.
````

## The side files, named and not copied

Twenty files sit beside those ten. They are named here and their contents are not, and the reason is the
argument this document has just made. A side file exists so that its detail is loaded at the moment it is
needed and not before. **That property is worth exactly as much to the reader of a standard this long as it is
to a session** — copying nineteen thousand words of on-demand detail into a document that is read in order
would make every reader pay what the design exists to let them skip, and it would put `money.md` on a page
four hundred lines from anywhere, rather than in the starter where somebody is writing a price.

`scripts/check-inlines.py` encodes the same split: a `SKILL.md` is checked by whole-body containment, and
everything beneath it by its path appearing at least once. The property kept is that nothing enters the
starter unremarked. The property dropped is that the docs mirror the starter byte for byte, and the cost of
dropping it is stated rather than hidden — **a side file's body can now drift from what this document says
about it, and nothing will notice.** `scripts/self-test.mjs` covers the suites under `scripts/`; it does not
read skill prose. The `SKILL.md` that names a side file is the only thing that will ever contradict it.

**`acceptance-criteria`** — the resolver's three forms in the order the code tries them, every refusal with
the real output pasted, and before-and-after criteria from a real annexe:

- `.claude/skills/acceptance-criteria/evidence-forms.md`
- `.claude/skills/acceptance-criteria/refusals.md`
- `.claude/skills/acceptance-criteria/worked-examples.md`
- `.claude/skills/acceptance-criteria/examples.md` — the fixture, deliberately half wrong

**`house-rules`** — one file per surface, and they do not overlap, so reading a second one you do not need
costs you and buys nothing:

- `.claude/skills/house-rules/money.md`
- `.claude/skills/house-rules/outbound-calls.md`
- `.claude/skills/house-rules/auth-boundary.md`
- `.claude/skills/house-rules/data-writes.md`
- `.claude/skills/house-rules/design-tokens.md`

**`write-a-spec`** — the workflow's exact error text with the recovery for each, and one complete filled spec
including how an unanswered question is left visible:

- `.claude/skills/write-a-spec/spec-yml.md`
- `.claude/skills/write-a-spec/worked-spec.md`

**`work-the-loop`** — what to do for each step the deriver can emit, and the counters that let the loop go:

- `.claude/skills/work-the-loop/references/steps.md`
- `.claude/skills/work-the-loop/references/loop-mechanics.md`

**`respond-to-review`** — one file per red check, reached only when that check is the one that is red:

- `.claude/skills/respond-to-review/references/size.md`
- `.claude/skills/respond-to-review/references/spec.md`
- `.claude/skills/respond-to-review/references/gates.md`
- `.claude/skills/respond-to-review/references/verify.md`
- `.claude/skills/respond-to-review/references/reviewer.md`

**`capture-a-learning`** — the worked contradiction comparisons, and the selections file with every refusal:

- `.claude/skills/capture-a-learning/contradiction-check.md`
- `.claude/skills/capture-a-learning/selections.md`

The four remaining skills — `build-loop`, `escalate`, `garbage-collect`, `operate-app` — have no side files.
Each is under a thousand words and each states its whole rule in its body. That is the target shape, not an
omission: a skill needs a side file when a reader would need one part of it and not the others, and none of
those four splits that way.

## What this layer does not fix

Three things, and none of them is small.

**It cannot make an unchecked rule hold.** `house-rules` lists the five surfaces where a mistake is not
recoverable and, in this starter, nothing lints any of them. A session that reads it produces the right thing
more often. That is the whole claim.

**Nothing verifies that a skill was loaded.** The description fires on a match against the situation, and the
match is a model's judgement. A session that never loads `acceptance-criteria` meets `criteria.yml` exactly as
it did before this document existed — with one difference, which is that the refusal now names the file to
read.

**A capability can go stale against the gate it pairs with.** Every check named in the ten bodies is a literal
path or a literal rule copied from a workflow, and `scripts/lib/facts.mjs` reads two of those rules out of
`.github/workflows/spec.yml` rather than restating them. The rest are restatements, and a restatement is a
copy. When a gate changes and its skill does not, the skill is confidently wrong, which is
[worse than saying nothing](17-artefacts.md).
