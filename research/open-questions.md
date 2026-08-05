# Open questions

The frontier. What we know we do not know, so "how far through are we" has a number instead of a
feeling. A question leaves this file by being answered, by being deferred with a reason, or by being
declared not worth answering.

**Status:** `open` · `deferred` · `answered` (with where the answer landed) · `dropped` (with why).

---

## Blocking — the manual cannot be called final while these are open

| # | Question | Why it blocks | Status |
|---|---|---|---|
| B1 | Does any check actually fail on a host when it should? | 27 rows say *written*, none says *proven*. The whole document is about that difference. | open — see experiments E1 |
| B2 | Does the process survive one real project end to end? | Never run. §14 says so. Every claim about how it feels to work this way is untested. | open — E2 |
| B3 | Does the review agent find anything a person would have wanted found? | It is a required check on unflattering published evidence. If its dismissal rate is bad it should come off. | open — E3 |
| B4 | What is our own defect rate, split by who found it? | Number 5 has no baseline, so no reading of it means anything yet. | open — E4 |

## Commercial — absent from the manual entirely, and we are a services company

| # | Question | Why it matters | Status |
|---|---|---|---|
| C1 | What does a ticket cost in agent spend? | Zero mentions of cost per ticket in 72,000 words. We quote fixed-price work; if a ticket costs meaningfully more than a developer-hour of tokens, Solutioning needs to know. | open |
| C2 | How does agent-speed delivery interact with fixed-price quoting? | Zero mentions. If the same SOW now takes a third of the time, we either reprice or we have quietly increased margin, and neither is decided. | open |
| C3 | What do we owe a client on PCI or equivalent? | Payments appear 14 times, PCI zero. We build commerce. Our security story is protected paths plus a daily scan, which is thin for card data. | open |
| C4 | Does the evidence base even fit a services company? | Nearly every source is a product or enterprise engineering org with one long-lived codebase. We run many client codebases with handovers. The findings may not transfer. | open |
| C5 | Once building compresses, is the client's answer time the binding constraint on delivery? | The docs name a decision-maker and a response time in the Kickoff working agreement, but nowhere treat client decision latency as a constraint on *delivery time*. If a phase that took ten weeks now takes four, and the client still answers in three days, their turnaround becomes the dominant term in a timeline we already quoted. Ties directly to C2: a fixed price built on our old speed assumes a queue that no longer exists. Measurable from number 2, the wait number, if we split queueing into waiting-on-us and waiting-on-them. | open |

## Design — decided for now, but on judgement rather than evidence

| # | Question | Current answer | Status |
|---|---|---|---|
| D1 | Is 300 lines the right ceiling? | Judgement. What should be measured is the size at which reviewers stop finding anything. | open — E5 |
| D2 | Would mob elaboration beat our async handover? | Refuted as a doc edit; genuinely open as a way of working. Needs one trial, not an argument. | open |
| D3 | What would agent identity look like for us? | We have none. Sessions are anonymous and commit as a human. Fine with one supervised session, not fine beyond that. | open |
| D4 | Is two-reviewers-at-High workable via two CODEOWNERS entries? | Believed yes; never tried. There is no per-path approval count. | open |
| D5 | Is mutation testing worth its cost at High? | Currently *to build* and deliberately not first. | deferred until B1–B4 |
| D6 | Does the deskilling effect appear in our own numbers? | Three external sources say it should. Number 5's who-found-it split is a weak instrument for it. | open |
| D7 | Should we add structural tests — file-length caps, enforced layer dependency direction, one canonical implementation of shared helpers? | A class of check we do not have. The rationale is context efficiency rather than tidiness: an agent in a codebase where every corner looks alike carries transferable understanding, and its output becomes predictable. Needs per-project values, which is why it is a question. Reported to work at a frontier lab on a 1M-line codebase. | open |
| D8 | One review agent with several persona lenses, or several agents? | We ship one. The reported practice is one agent per persona — front-end architect, reliability, scalability — each primed with that persona's written standards, triggered on every push. Our own sources support the shape: four reviewer bots on one codebase never agreed on a single finding, so lenses find different things. Unknown for us: cost per pull request, and whether dismissal rates stay under the threshold when several agents comment. | open |
| D9 | Should garbage collection also run automatically? | We adopted the scheduled human hour. The source also runs background agents that scan for deviations, grade quality and open small refactoring pull requests, most reviewable in under a minute and automerged. Automerging agent-authored refactors is a bigger step than anything we currently allow, and it interacts with the protected set. | open |

## Coverage — areas we have not swept

| # | Area | Status |
|---|---|---|
| S1 | Services companies and agencies specifically, rather than product orgs | open |
| S2 | Mobile and app-store constraints; our stack section is thin here | open |
| S3 | Platform-constrained work — Shopify themes, hosted CMS — beyond the fixture rule | open |
| S4 | Regulated commerce: card data, KYC, consumer credit | open |
| S5 | What agencies charge for, and whether AI changes the unit sold | open |
