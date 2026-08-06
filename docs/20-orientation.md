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
