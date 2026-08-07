# Orientation — the half we did not build

Every check in this standard answers one question: **did the work that already happened meet the bar?** That
is verification, and it is what documents 04 through 12 describe.

There is a second question, and until now nothing here answered it: **where is this project, and what happens
next?** That is orientation. It is what a person supplies today by typing context into a fresh session, and it
is the half a nine-month-old agent workflow spends most of its tokens re-deriving.

The two are not variations of each other. Verification runs on a host, after a push, and refuses. Orientation
runs at the start of a session, before any work, and *informs*. A repository can be perfect at one and have
nothing at all for the other, which is what ours was.

## The mistake, named

This standard's own [finding 39](../research/findings.md) refused to build an autonomous runner, on the
grounds that it "removes a person typing two commands, about thirty seconds per ticket, and cannot be
validated because nothing has run on a host."

Both clauses have expired, and the first was wrong when it was written. The value was never thirty seconds of
typing. It is **holding position across a cold start** — a different mechanism that the finding never
evaluated, because it had been filed under convenience. The validation objection is gone: findings 60–64 are
dated host proofs.

The general lesson is worth more than the correction. **A feature described as convenience and a feature
described as a mechanism get priced differently, and the description is chosen by whoever writes the ticket.**
Finding 39 mispriced the work by accepting its own framing.

## What CLAUDE.md cannot do

The obvious answer to orientation is to write it down: put the process, the current state and the next step
into `CLAUDE.md`, which every session reads.

[Finding 59](../research/findings.md) is why that fails. **Standing context is generative, not preventative.**
Twenty design rules live in a `CLAUDE.md` that every session loads, and four accessibility rules were switched
off inside a feature commit anyway. Context makes an agent *produce* things. It does not make an agent
*refrain*, and it does not make an agent *know* — it makes knowing likely.

So a `CLAUDE.md` section headed "current status" is a probability. The whole point of the enforcement ladder is
that a probability is tier 3.

## Derive it; never store it

The reference implementation of this idea — `awslabs/aidlc-workflows` v2 — stores position in
`aidlc-state.md`, a markdown file with twenty fields, written by the model. Everything else in their design
follows from that one decision: because an LLM writes the state, the state must be defended, so there is a
PID-bound capability token, a `PreToolUse` shell-parsing guard, an artefact-existence guard, a reviewer-receipt
guard, a human-presence guard and a revision backstop — six mechanisms whose entire job is keeping one file
honest. Their own notes concede the file has no schema validator and that stage start is scraped from
LLM-authored text.

**Every input orientation needs is already an unforgeable fact.**

| Question | The fact that answers it |
|---|---|
| Which ticket? | the branch name |
| Is the spec committed first and alone? | `git rev-list --reverse --no-merges main..HEAD` |
| Is it in review? | `gh pr view --json state,reviewDecision` |
| Which checks are red? | `statusCheckRollup` |
| What did we already learn here? | the ticket's board entry **Findings** |
| Is a human owed an answer? | an open `log/events/` escalation |

None of those can be written by a model claiming a state it is not in. Derivation is not merely tidier than a
state file — **it deletes the attack surface that a state file creates**, and with it the six guards.

The rule the board already states covers this: *status is derived, never typed.* Orientation is that rule
applied to the session instead of to the table.

## What may be automated, and what may not

Automating a process is not one decision. It is three, and they have different owners. The cleanest statement
of the split is the one the reference implementation puts at the top of its learning tool:

| Layer | Owner | Property |
|---|---|---|
| detect, surface, route, **write** | a deterministic program | repeatable; no model in the path |
| does this contradict an existing rule? | the model | knowledge, one comparison, cheap to check |
| keep / revise / skip | **a person** | judgement, never delegated |

*No LLM call lives in the tool.* That sentence is the design.

Read it the right way round: **the mechanics are what get automated, and the questions are what get kept.**
Automating the flow does not mean asking a human less often — done properly it means asking *more* often and
more cheaply, because the agent no longer spends a turn working out whether it is allowed to ask.

## The window with no enforcement

Every gate in this standard lives on the host and is unreachable until a pull request exists. A mechanism that
holds a session in its loop therefore has a specific and dangerous consequence: **between the first
implementation commit and the pull request opening, the loop runs with nothing checking it.**

Making the agent unable to stop inside that window, without further bounds, produces an agent that cannot
stop, working from an unvalidated spec, outside the perimeter. Three bounds are load-bearing rather than
optional:

1. **A per-ticket ceiling on continuations**, persisted, not a per-turn counter. A counter keyed on a progress
   signature is reset by any `git commit --amend`.
2. **A wall-clock and token budget**, because neither of the above bounds spend.
3. **Refuse to enter `implement` at all** when the spec's acceptance criteria do not resolve to checks. An
   unprovable criterion is a class B escalation before it is code, not after.

The third is the one that matters most, and it is the cheapest: the resolver that decides whether a criterion
names a real test is the same one the criteria gate needs anyway.

## Honesty about the tier

Most of an orientation layer is **not enforcement**, and saying otherwise would repeat the error this standard
exists to prevent:

| Piece | Tier |
|---|---|
| deriving the next step | not enforcement — it reports; it refuses nothing |
| injecting position at session start | not enforcement — nothing verifies the model read it |
| holding the session in its loop | tier 1, **harness only** — it constrains our session, not the host |
| the criteria resolver, once required | tier 1, on the host |
| surfacing that the learning loop never ran | tier 2 — it makes an absence visible; a person still acts |

Only one of those lands on the perimeter. The rest are worth building and not worth counting, and a summary
table that quietly promotes them is the defect catalogued in
[the artefacts](17-artefacts.md).

## The failure mode to design against

A self-improving rule file plus an agent that cannot stop is **a loop that can lower its own bar.** If the
learning path can add a practice, it can add a weaker one, and nothing in a green run distinguishes the two.

The defence is the asymmetry already used for gate changes: **adding a practice is implementation; weakening
or removing one is a gate change** — its own commit, a code owner, and a human turn recorded against it. A
learning that contradicts a broader rule is rejected before it reaches disk rather than merged and reviewed
later.

## What a session should cost

Orientation earns its place on token economics, not elegance. A fresh session that must re-derive position
reads the board, the branch log, the pull request and the last few commits — thousands of tokens, every time,
with a chance of getting it wrong that no check catches. An injected summary is a few hundred tokens and
cannot be wrong, because it is derived from facts at the moment of injection.

That is the whole argument for it, and it is also the honest answer to *how do agents make delivery faster*:
not by removing people from the loop, but by removing the two most expensive things an agent does — working
out where it is, and building the wrong thing far enough to need rework.

## The inventory

Eleven files implement the layer. Each one's own header states its limits, and those limits are repeated here
rather than summarised away, because a reader deciding whether to trust a piece needs the limit in the same
place as the claim.

The tier column uses the ladder in [enforcement](06-enforcement.md): tier 1 is structural and cannot be
skipped, tier 2 is written down and a person acts on it, tier 3 is prose. **Only two of the eleven land on a
rung that refuses anything** — `stop-guard.mjs` on the harness and `self-test.mjs` on the host. That is not a
gap to be closed later. Informing a session and refusing a merge are different jobs, and a table that ran them
together would be the defect this standard exists to name.

| File | Tier, honestly |
|---|---|
| `scripts/next.mjs` | not enforcement — it reports and refuses nothing |
| `scripts/orient.mjs` | not enforcement — nothing verifies the model read it |
| `scripts/stop-guard.mjs` | tier 1, **harness only** |
| `scripts/human-turn.mjs` | not enforcement — it records; a consumer would have to refuse |
| `scripts/hook-health.mjs` | tier 2 when somebody runs it; nothing runs it for them |
| `scripts/learn.mjs` | not enforcement — append-only is a property of this file's write path, not a gate |
| `scripts/self-test.mjs` | tier 1, on the host — reached through `verify.mjs` |
| `scripts/lib/facts.mjs` | nowhere |
| `scripts/lib/board-parse.mjs` | nowhere |
| `scripts/lib/criteria.mjs` | a library. **Advisory** today: see below |
| `scripts/lib/entry.mjs` | nowhere |

### `scripts/next.mjs` — the derivation

Facts in, one directive out. Sixteen ordered steps, from `answer-escalation` through `implement` to `merge`,
and the first whose condition holds is the answer — so a later step never fires while an earlier obligation
is outstanding. Every step carries a `human` flag, and `--assert` exits non-zero only when the work owed is
the **agent's**. When a person is owed something it exits 0, because a loop that blocked on a review would
hold a session hostage to somebody who has gone home.

**It is not a gate. It reports, and a session is free to ignore it.** It cannot tell whether the code is any
good, whether the spec is right, or whether a criterion that resolves to a test is a criterion that test
actually proves.

### `scripts/orient.mjs` — the session brief

A `SessionStart` hook. It runs the derivation, formats it into a few lines — branch, ticket, next step, whose
turn it is, the pull request's state, and up to eight findings already established on the ticket — and hands
it over. It is **silent when the branch carries no ticket**, which is what keeps it from being resented: most
sessions in most repositories are not working a ticket, and a hook that narrates on all of them teaches
people to ignore it.

**Nothing anywhere verifies that the model read it, believed it, or acted on it.** Finding 59 is exactly that
standing context is generative rather than preventative, so this makes the right next step likely and never
certain. It also fails open and silent on every error, because a `SessionStart` hook that greets a new session
with a stack trace is a hook somebody removes.

### `scripts/stop-guard.mjs` — the only mechanism that makes "keep going" a property

A `Stop` hook. When the turn tries to end it runs the derivation, and if the next step is the agent's it
blocks the stop and restates what is owed. The reason text is an **on-task continuation, never an
instruction** — it names work already owed and nothing else. That is a security property rather than a style
preference: an override-shaped directive injected into a session is what a model's safety training refuses, so
phrasing it as a continuation means a buggy or tampered-with derivation can only push the session back toward
sanctioned work.

Four release conditions, because a `Stop` hook is the one thing in a repository that can trap a session, and
a trapped session is worse than a loop that quits early:

| Release | Why it is there |
|---|---|
| the next step is a person's | picking a ticket, an unprovable criterion, a review, a merge — the turn ends |
| a consecutive no-progress ceiling | the position has not moved between blocks, so the loop is spinning |
| a per-ticket total ceiling that never resets | the bound that survives everything else |
| a wall-clock budget from the first block | neither ceiling bounds spend |

The no-progress signature **excludes the commit sha on purpose.** A sha-based signature is reset by any `git
commit --amend`, which turns the ceiling into decoration. Any error at all also releases, and so does a
counter it cannot persist — the ceilings cannot bind without one, so a write failure is a reason to let go
rather than to block unbounded. State lives in `.claude/.loop/`, which is gitignored and does not exist until
the first block.

**It constrains our session and nothing else.** It is not a perimeter, it does not run on the host, and
`--no-verify`-style escapes are beside the point because a person can press Esc, which `Stop` hooks never see.
It cannot tell good work from bad; it knows only whether the derivation still reports an obligation. And it
cannot bound tokens directly — the wall-clock budget is a proxy and is labelled as one.

### `scripts/human-turn.mjs` — the presence ledger

GitHub already refuses a self-approval on the host: finding 61 records the real text, `Review Can not approve
your own pull request`. Nothing in a repository can reproduce that, because the host holds the identity. This
is the in-session twin, and it exists for the approvals that never reach a pull request at all — a mid-flight
spec revision, a continuation past a ceiling, a learning that would weaken a practice.

A `UserPromptSubmit` hook appends one line per human turn to `log/presence.jsonl`: timestamp, kind, branch,
ticket. **The prompt text is never read and this file has no way to reach it** — what the human said is a
different question from whether a human said anything, and only the second is being asked.

**The write fails open and the read fails closed, and that asymmetry is the design.** A hook that can trap a
session must always be able to let go, so every failure on the mint path is swallowed and the exit code is 0.
`hasHumanTurnSince` on an empty, absent or unreadable ledger returns false, because a gate asking for proof of
a human and finding none has its answer.

It does not prove **who** — there is no identity anywhere in it. And the ledger is a file in the working tree,
inside the agent's reach: one write appends a line indistinguishable from a real one. It is not enforcement on
its own; it becomes tier 1, harness only, the moment a consumer refuses on it, **and no consumer does yet.**

### `scripts/hook-health.mjs` — the middle state

A registered hook looks identical from the outside whether it fires on every call or has never run once. So
each hook script calls `beat()`, which touches one file under `.claude/.hooks-health/`, and `--check` reads
the registrations out of `.claude/settings.json` and prints one line per hook:

| State | What it means | Exit |
|---|---|---|
| NEVER INSTALLED | the registered script is not in the tree, so it can never run | **1** |
| INSTALLED BUT NEVER FIRED | registered, present, no heartbeat — the dangerous state | 0 |
| FIRING | a heartbeat, recent enough | 0 |

Only the first fails, and that restraint is the point. A fresh clone has fired nothing, so failing on NEVER
FIRED would put a red X on every repository nobody worked in today — the wall of red finding 63 is about,
after which a real failure is indistinguishable from noise. Two further states, EXTERNAL and UNRESOLVED, exist
only so NEVER INSTALLED can keep meaning *proven absent* rather than *could not be resolved*.

It cannot tell a hook that ran from a hook that ran and did its job, because `beat()` is called by the script
itself. It correlates registration to heartbeat by basename, so a script that beats under another name reads
as NEVER FIRED for ever. It reads `.claude/settings.json` only. And **nothing in the starter invokes
`--check`** — no workflow, no hook, no `package.json` script — so today it is a report waiting for a person to
run it.

### `scripts/learn.mjs` — the three-layer ritual

The deterministic half of the learning loop, and it owns exactly one of the three layers named above: detect,
surface, route, **write**. `surface` proposes candidates from `log/events/` and the board's Findings; something
else asks the model its one contradiction question; a person answers keep, revise or skip; `persist` writes
what came back. **No LLM call lives in the tool.**

`persist` can only append. A self-improving practice file plus an agent that cannot stop is a loop able to
lower its own bar, so the asymmetry used for gate changes is applied mechanically: adding a practice is
implementation, weakening or removing one is a gate change. It refuses, exit 1, if a selection would rewrite
or delete a line already on disk, if the id is one `surface` did not produce, or if `keep` is anything other
than the boolean `true` or `false` — `keep: "skip"` is a truthy string, and reading it as a keep writes a
practice nobody chose, in the one direction an append-only file cannot take back. The practices file it
appends to does not exist until the first kept learning.

**It is not enforcement.** Both halves live in the repository and neither is a required check. The append-only
guarantee holds only for writes that go through this file; a session that edits the practices file directly is
stopped by `CODEOWNERS` plus a required review on the host, or by nothing. It also cannot tell a good practice
from a bad one — the heading routing is keyword matching, deliberately crude, and unmatched text goes to
Unsorted rather than to the nearest guess.

### `scripts/self-test.mjs` — the most useful line in this document

Ten files under `scripts/` carried a `--self-test` block when this was written. One grep across
`package.json`, `lefthook.yml`, `scripts/verify.mjs` and every workflow found a **single** invocation:

```
$ grep -rn "self-test" package.json lefthook.yml scripts/verify.mjs .github/workflows/
.github/workflows/red-on-base.yml:49:  run: node scripts/red-on-base.mjs --self-test
```

**Nine suites, several hundred assertions, never executed.** `scripts/lib/board-parse.mjs` says in its own
header that its self-test "is the only thing standing between a silent change in how an entry is read and both
of them being quietly wrong" — and by that sentence, nothing was standing there. A test no runner invokes is a
comment that happens to be syntactically valid, and it rots exactly like a comment, invisibly, because a suite
that is never run is never seen to fail.

This runs every suite it can find — twelve of them today, which is the point of the next paragraph.
**Discovery is by inspection, not by a list**, because a hand-written list
is the same defect in a different hat: the next script arrives, nobody edits the list, and that is precisely
how nine of them ended up unwired. A file opts in by comparing something against the quoted literal
`"--self-test"` anywhere in its executable source. Comments are stripped first, and the literal must be
quote-hugged, and each half of that rule exists for a caught false positive — a header documenting the
pattern, and a usage string mentioning the flag. Files with **no** suite are reported as a separate count and
never fatally, because silence about an untested file is how a file stays untested. Discovering nothing at all
fails: reporting green for zero suites is the original defect.

It runs suites; it does not judge them. A suite that asserts nothing and exits 0 is reported PASS, and no
amount of aggregation can tell that apart from a real one — this makes an unrun suite impossible, not a weak
one. It is reached from `verify.mjs`'s gate list, which `verify.yml` runs as a required check, so it is tier 1
on the host. Its own header still says it is unwired; that sentence is now out of date, which is the direction
a limit should drift.

### `scripts/lib/facts.mjs` — the fact collector

One function that reads the facts everything above it derives from: the branch, whether the first commit is
the spec alone, whether a pull request exists and what its checks and review decision say. **It never throws
and never hangs.** No git repository, no `gh`, no network, a detached HEAD, an empty repository: each degrades
to an empty or a null with `error` naming which fact could not be collected. Every subprocess carries a hard
timeout and a timeout is treated as absence, because the realistic hang is a `gh` call against a dead network
and a session that cannot start is worse than one that starts uninformed.

Absence is not a verdict, and that distinction is most of the file's value: a git that never answers and a git
that is not installed are each reported as exactly that, never as "not a git repository".

It reads `.github/workflows/spec.yml` to learn what a spec path is rather than deciding for itself, so if that
workflow stops declaring one it refuses instead of guessing. It cannot see branch protection — that is
`perimeter.yml`'s job. Its pull request facts are one snapshot. **Its tier is nowhere.** Calling a fact
collector enforcement would be the promotion this document exists to refuse.

### `scripts/lib/board-parse.mjs` — one parser, briefly two

`scripts/board.mjs` parsed `tasks/board.md` inline, which was right while it was the only reader. Orientation
needs the same entries, and a second parser of one file is the drift refused everywhere else: two parsers
agree on the day they are written and disagree the first time an entry's shape changes.

**The extraction that existed to delete a second parser created a third.** `board.mjs` kept a byte-identical
copy after this file was extracted, and nothing failed, because copies agree on the day they are made. It
imports the module now, and its own suite carries a case that reads its source and fails the moment a copy
reappears — the only kind of case that can catch a duplicate, since a behavioural one cannot.

It tracks fences, because `tasks/board.md` documents an entry's shape by showing one inside a fenced block,
and that sample's heading matches the entry pattern exactly. It reads structure, never meaning: a **State** of
`in progres` comes back as the string somebody typed. And it cannot see inside a fence anywhere, so a code
sample under a `## Findings` heading is dropped — asserted rather than fixed, because the generated board view
is compared byte-for-byte against a parse and quietly starting to keep those lines would fail `--check` on a
board nobody had edited. Three consumers, no tier.

### `scripts/lib/criteria.mjs` — the resolver, and its two defects

One question per row: does this cell name a file that exists, a test that exists, or a URL — answered for
every row before it reports. This is finding 47's countermeasure at the front of the process as well as the
end: `| Rollback tested | verified | |` reads as diligence and contains nothing.

Two defects a review found in it, both of which defeated the thing the file exists to do:

**The claim word was tested with its wrappers still on.** The markdown strip removed only `**`, `__` and `~~`,
so `` `verified` `` — how anybody writing markdown types a word they mean literally — never matched the
anchored refusal, fell through to the test-file substring search, and matched a fixture containing `it("email
is verified after signup", ...)`. The cell resolved. The gate reported evidence for a row that named none.

**It read one table and reported on all of them.** Table selection was `candidates.find((c) => c.named) ??
candidates[0]`, which took the first structurally-matching table and discarded every later one — so a `##
Scope` table headed `| Item | Check |` matched by luck and shadowed the real table under an explicit
acceptance-criteria heading. It now resolves every table in the winning precedence tier and concatenates the
rows, because picking is what produced the bug and a spec that splits criteria over two tables is ordinary.

It proves an artefact is named and exists. **It cannot read the artefact and tell you it proves the
criterion** — `| Totals are correct | README.md |` resolves, because the file is there. That judgement is a
person's, which is why the review agent is pointed at this column. It does not run the test it finds or fetch
the URL it accepts, so a named test that asserts nothing and a 404 both pass. It skips fenced blocks, safe
only because a missing table is a refusal rather than a pass.

**Its own tier is a library's: it decides and reports and refuses nothing.** `.github/workflows/criteria.yml`
calls it, and `perimeter.yml` classifies `criteria` as **advisory** — so today it runs, it reports, and merging
ignores it. It becomes tier 1 the day that check joins the required list, and not before.

### `scripts/lib/entry.mjs` — one answer to "am I the program?"

Every script here both exports functions and has a command line. Node offers no `import.meta.main`, so each
author invented the check, and **three of four inventions were wrong** — the same bug written four times in
one afternoon:

| File | What went wrong |
|---|---|
| `scripts/lib/criteria.mjs` | guarded its CLI block and forgot its `--self-test` block, so `node next.mjs --self-test` ran criteria's suite, printed criteria's score and exited on criteria's result. Three scripts looked tested. None were |
| `scripts/human-turn.mjs` | computed its guard 156 lines below the block that needed it, so importing the module while your own argv said `--self-test` ran its whole suite and then killed you |
| `scripts/learn.mjs` | had no guard at all. Importing it printed a usage error and exited 2 |
| both of the above | compared `import.meta.url` against a raw `process.argv[1]`. Node resolves symlinks for the main entry and not for argv, so through a symlink the two never match, the guard says "not the program", and the file exits 0 having done nothing |

The last row is the reusable lesson, and it is why this is one shared function rather than a convention. **A
gate that exits 0 silently is worse than a gate that crashes**, and the failure was invisible in a green run
from either end: the suite that never ran printed nothing, and the CLI that did nothing returned success.
`isEntry` realpaths both sides, answers false when it cannot prove the file is the program — wrongly believing
you are a library costs a missing CLI, wrongly believing you are the program runs a CLI inside somebody else's
process — and every top-level argv branch in every script is gated on it, not only the obvious one at the
bottom.

It cannot tell you a caller's intent, and it says nothing about whether a file *should* have a command line. A
library that reads argv at import time is making decisions for a program it knows nothing about, and the fix
for that is to not do it rather than to guard it better.

### What this layer still cannot do

Four limits, and the last one is why stop-guard's bounds are load-bearing rather than optional.

**It cannot see work that leaves no trace in git, on the board or on the pull request.** A branch whose author
did everything by hand outside the conventions looks, correctly, like a branch with nothing done. Every fact
underneath is unforgeable precisely because it is a by-product of the tools, and the cost of that property is
that work done outside the tools is invisible.

**Its reading of a pull request is only as fresh as the last `gh` call.** The facts are one snapshot. A check
that went red a second ago is still green here, a review submitted mid-turn is not in the derivation, and a
timeout against a dead network is reported as absence rather than as a state.

**Nothing checks that a session acted on any of it.** The injection, the findings, the named next step: all of
it is context, and context is generative. The two pieces that constrain rather than inform are stop-guard,
which is harness only, and the required checks on the host, which are not part of this layer.

**Between the first implementation commit and the pull request opening, no gate on the host can see the loop at
all.** Every gate in this standard is reached through a pull request, and inside that window there is not one.
So the mechanism that keeps a session in its loop runs, in that window, with nothing checking it — which is
why the per-ticket ceiling, the wall-clock budget and the refusal to enter `implement` on unresolved criteria
are the three bounds that have to hold, and why weakening any of them is a gate change rather than a tuning
decision.

### `scripts/setup-check.mjs` — tier 2, and the reason the rest can be trusted

Reads what the host actually is: the three branches, which one is default, protection on each, auto-delete on
merge, and whether `CODEOWNERS` names an owner that resolves. `unset` fails. **`unknown` does not**, because an
unreadable host is not a configured one and calling it configured is the class of lie this file exists to
prevent.

The derivation consumes only its two cheapest questions — a placeholder owner, and missing branches — since
`orient` runs at every session start and six `gh` calls would tax it for ever, including the thousands of
sessions after setup is finished. The full audit is what the `set-up-repo` skill runs.

**What it cannot do:** tell whether a protection rule is the RIGHT one, only that one exists. And it reads
protection for all three branches where `perimeter.yml` reads one — so the continuous check is narrower than the
setup-time check, which is stated in the perimeter's own header rather than left as an assumption.

One defect worth keeping, because it is the shape that recurs: the first version reported
`✓ dev, uat and prod are protected` for a repository that had none of them. The loop skipped missing branches,
so the empty set made `every()` true. **A vacuous pass is worse than no check** — it answers confidently and
wrongly, and the reader stops looking.
