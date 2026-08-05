# AI SDLC

A software development lifecycle for teams where agents write most of the code and people stay
accountable for it. Nineteen documents, a working set of enforcement gates, and the research behind both.

It exists because of one finding, which everything else follows from:

> **An agent builds to the shape of the check.** A weak gate does not give you the same product less
> verified — it gives you a *different, smaller* product.

So this is built out of gates rather than guidance. Where a rule could not be enforced, it says so and
names the tier it is stuck at.

## Start here

| If you want | Read |
|---|---|
| The five-minute version | [`docs/README.md`](docs/README.md) |
| Why any of this | [`docs/01-why.md`](docs/01-why.md) |
| The per-ticket loop | [`docs/04-build-loop.md`](docs/04-build-loop.md) |
| Every check, with its code | [`docs/06-enforcement.md`](docs/06-enforcement.md) |
| What it changes, and what it costs | [`docs/18-outcomes.md`](docs/18-outcomes.md) |
| **What it does not do** | [`docs/14-limits.md`](docs/14-limits.md) |

## Honest status

**Nothing here has run end to end.** Four blocking questions in
[`research/open-questions.md`](research/open-questions.md) are the same question in different clothes: no
check has been proven to reject anything on a real host, the process has never survived a real project,
the review agent's dismissal rate is unknown, and there is no defect baseline.

The evidence that does exist is narrow and pointed — in one internal pilot, requirements with a check
behind them arrived **8 of 8**, and requirements written only as prose arrived **0 of 7**. That asymmetry
is the entire argument for the approach, and it is not the same thing as proof that the approach works.

Read [`docs/14-limits.md`](docs/14-limits.md) before believing any of it.

## Layout

```
docs/       19 documents. The conclusions
research/   sources, an adjudication ledger, open questions, experiments. The working-out
scripts/    check-docs.sh — verifies the set after any edit
```

`docs/` describes a companion starter repository, inlined in full across
[`docs/06-enforcement.md`](docs/06-enforcement.md),
[`docs/07-repository.md`](docs/07-repository.md) and
[`docs/08-templates.md`](docs/08-templates.md) — every file, with the reasoning. Nothing is hidden behind
a private dependency: you can reconstruct the whole thing from these documents.

`scripts/check-docs.sh` runs seven checks over the set, including that every percentage traces to a cited
source. It skips the starter-inlining check when the starter is not alongside.

## Research conventions

Figures are verified against the primary source, not against the blog quoting the talk. Claims that did
not survive verification are recorded as refuted in `research/findings.md` rather than deleted, because
the refutations are more useful than the acceptances.

`research/` also contains the commercial questions this process has not answered — pricing, margin, what
we owe a client on PCI. They are published open because an unanswered question that everyone can see is
worth more than a confident answer nobody checked.

## Licence

No licence yet, which means default copyright. If you want to use any of it, open an issue and ask.
