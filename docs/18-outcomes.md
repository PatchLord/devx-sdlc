# What this changes, and what it costs

The case for making a team work this way, against the honest alternative: a good developer with a good
agent and no process at all. Read this before asking anyone to adopt it, and before promising a client
anything.

Two things are kept separate throughout, because mixing them is how a process pitch loses the room:
**what holds by construction** — properties of the gates, true the day a repository is set up — and
**what we expect to move but have to measure.** The second list is projection. It is labelled as such.

## The one line

**"Done" stops being an opinion.**

Today it is a judgement each developer makes from memory, at speed, under delivery pressure. After this it
is a claim that someone who was not there can check.

## The alternative, described fairly

A capable developer with a capable agent is fast, and often the code is good. The failure is not
competence and it is not the model. It is that **nothing outside the developer's head decides when the
work is finished**, and four things follow from that:

**Quality tracks who picked up the ticket.** Two developers, same ticket, same agent, different standard —
because the standard lives in two different heads. There is no version of this that survives a team
growing.

**The agent builds to the shape of the check.** With no check, it builds to the shape of the prompt. A
weak gate does not give you the same product less verified; it gives you a *different, smaller* product.
That is the single most important finding behind this whole document set, and it is why the answer is
gates rather than encouragement.

**Nothing accumulates.** Every defect is paid for twice — once when it ships, once when the same class
ships again next month. Published evidence puts a number on the security case specifically: **41.1%** of
AI-introduced security issues survive the commit that introduced them. Nothing in a no-process workflow is
looking for the survivors.

**Review degrades exactly when it is needed.** Anthropic measured **16%** of pull requests in their own
engineering org receiving substantive feedback, because engineers were skimming to keep velocity. Skim
probability rises with diff size, and agent-written diffs are large by default.

None of that is an argument that developers are careless. It is an argument that **judgement applied at
speed, with nothing written down, is not a control** — and that the faster the building gets, the less of
a control it becomes.

## The same ticket, both ways

| | Developer + AI, no process | This process |
|---|---|---|
| What "done" means | The developer's read, that day | A criterion with an artefact against it |
| Where the standard lives | In someone's head | `docs/production-ready.md`, tiered by how it is enforced |
| Intent before code | In the chat, then gone | A spec, approved, as the branch's first commit |
| Can a check be weakened quietly | Yes, and invisibly | No — a gate change cannot ride inside an implementation commit |
| Can the checks be switched off | Yes, silently | No — one job asks the host what it enforces and compares |
| What a green build proves | That the tests that exist passed | That they passed *and* nobody touched what produces them |
| Fate of a review finding | Sometimes a fix, sometimes nothing | Fixed, or dismissed in writing. Never neither |
| Second occurrence of a defect | Same conversation again | A check, converted in the weekly hour |
| A new joiner's output | As good as their taste | As good as the standard, on day one |
| Stale design document | Discovered per ticket, forever | Surfaced once, fixed in the pull request that found it |
| What the client can be shown | A demo, and assurances | Evidence per criterion, and what was *not* verified |

## What holds by construction

Not projections. These are true the moment the repository is set up, and they are the reason to do this at
all even before any number moves:

| Output | Why it holds |
|---|---|
| Every merged change has written, approved intent that predates the code | The spec is the branch's first commit and an ancestor of every implementation commit |
| No check can be weakened invisibly | A modified test, a lowered threshold or a CI edit cannot ride inside an implementation commit |
| Every claim of done has an artefact | The criteria table's evidence column. An empty cell is prose, and "verified" is not evidence |
| Every review finding ends fixed or dismissed in writing | Required conversation resolution on the protected branch |
| The gates cannot be quietly abandoned | `perimeter.yml` reads the host's real configuration and fails when it stops matching what we claim |
| Every defect a person found leaves a check behind | The log, and the weekly hour that converts what recurred |

The last two are the ones that make this different from every process anyone has tried here before. Every
earlier attempt could be dropped silently, and eventually was. This one reports its own abandonment.

## What we expect to move

Projection, not evidence. Each row names the number it would show up in — see
[measurement](11-measurement.md) — and none of them is readable inside a quarter.

| The pain | What attacks it | Where it shows up | Honest expectation |
|---|---|---|---|
| Bugs keep arriving | Each defect a person finds becomes a check | Defects reaching a person, per ticket | A downward **trend** over a project, not a step change. This is the compounding one |
| Endless refactoring | Contracts frozen before anything builds on them; spec approved before code exists | Rework rate — **not currently one of the six** | Most rework is building against a shape that was never fixed |
| Nobody knows if it is production-ready | The standard is written down, tiered, and outside the person | Shortcuts taken | A new joiner reaches the standard on day one instead of in two years |
| Constant blockers | The TDD's real job is closing every question with human latency attached, before implementation | Ticket wait, split waiting-on-us and waiting-on-them | Blockers move from mid-build to pre-build, where they are cheap |
| Review churn | Tickets sized to what a person can actually review | Dismissal rate, and findings per pull request | Fewer round trips. At over 1,000 lines, **84%** of pull requests draw findings, averaging 7.5 each |
| Developers not knowing the system | The TDD is interrogated, and its open questions, risks and omissions cannot be agent-drafted | Divergence field, non-empty | Understanding without reading every line — the only version that survives agent-written code |

**Rework is missing from the six numbers.** If "so much refactoring" is the pain most worth proving
solved, it has to be added before the first ticket — tickets reopened or substantially redone. It cannot
be reconstructed afterwards.

## The commercial output

Easy to miss, and for a services company it may be the most valuable one: **you can show a client what was
verified and what was not**, per ticket and per release. The release checklist's third column exists so
that "what this release does not verify" is something handed over deliberately rather than discovered in a
support thread three weeks later.

It also gives Solutioning something to sell that competitors mostly cannot: not *we use AI*, which is now
table stakes, but *here is what we check, here is what we can prove, and here is what we deliberately do
not claim.*

## What it costs

Stated plainly, because a pitch without this is not credible:

- **About a day of setup per repository**, and **a real hour every week** that has to be defended when it
  is inconvenient. That hour is the entire convergence mechanism. Skipped, this becomes paperwork that
  never pays back.
- **More human decisions per ticket, not fewer.** Escalations are welcome by design; the goal is that each
  *class* of question is eliminated once, not that people are interrupted less. Anyone selling this as
  "less involvement" is selling something else.
- **The first two weeks feel slower**, because a spec now precedes code and the payback is later.
- **A second person is structurally required.** One person filling every role approves their own specs,
  their own criteria and their own pull requests, which makes `CODEOWNERS` decoration and the central gate
  fictional.

## What it will not do

- It will not make bad requirements good.
- It will not compress delivery in proportion to how much it compresses building. The typing gets faster;
  the deciding does not. Expect the constraint to move to **how fast questions get answered — possibly to
  the client.** That is still progress, because a visible constraint can be fixed and "we are behind"
  cannot.
- It will not help a throwaway spike, and should not be forced onto one. That is what the Light depth
  level is for — see [depth](05-depth.md).
- It will not produce a readable number next month. At three tickets the six numbers are a sanity check.
  **Anyone quoting a percentage improvement in the first fortnight is making it up.**

## What we cannot yet claim, as of writing

Nothing here has run end to end. Four blocking questions in
[`research/open-questions.md`](../research/open-questions.md) are all the same question in different
clothes: no check has been proven to reject anything on a real host, the process has never survived a real
project, the review agent's dismissal rate is unknown, and we have no defect baseline.

The pilot evidence we do have is narrow but pointed, and it is the reason the whole approach is structural
rather than advisory: requirements with a check behind them arrived **8 of 8**; requirements written only
as prose arrived **0 of 7**.

Until the first real project has run, the correct sentence in front of a client is *this is how we work*,
never *this is proven to reduce defects by X*. See [limits](14-limits.md) for the full list of what we do
not know.

## The sentence for a sceptical executive

**It makes quality a property of the process instead of a property of whoever happened to pick up the
ticket** — and that is the only version of quality control that survives most of the code being written by
an agent.

## The questions you will be asked

Written down because the case is won or lost here rather than in the presentation, and because an answer
invented in the room is an answer nobody can hold us to later. Where we do not have an answer, the entry
says so and names the open question — **a stated gap costs less than a confident guess that turns out
wrong in front of a client.**

### From an executive

**"How much does this slow us down?"**
Ticket one is slower, visibly. After that the front half does not *add* work, it *moves* work earlier —
questions that used to surface mid-build surface before code exists, where they are cheap. What we cannot
promise is a throughput gain: the typing got faster and the deciding did not, so expect the constraint to
move to how fast questions get answered. That is still progress, because a visible constraint is fixable
and "we are behind" is not.

**"What does the AI itself cost per ticket?"**
Unmeasured, and that is a hole rather than a defence — see C1 in
[`research/open-questions.md`](../research/open-questions.md). Capture it from the first ticket of the
first project; it cannot be reconstructed. Anyone quoting a figure before then is guessing.

**"Can we charge for this?"**
Not as a line item. What it gives Solutioning is something competitors mostly cannot say: not *we use AI*,
which is table stakes, but *here is what we check, here is what we can prove, and here is what we
deliberately do not claim.* The release checklist's third column — what this release does **not** verify —
is the part clients remember, because nobody else volunteers it.

**"If the models keep getting better, is this wasted work?"**
The opposite. The law this is built on is about checking, not about model quality: a better model produces
more plausible code faster, which raises the volume arriving at the one part of the sequence that did not
speed up. Every capability improvement makes the checking layer more load-bearing, not less.

**"Why not just trust our senior engineers?"**
Because the failure is measured and it is not about competence. Anthropic found only **16%** of pull
requests in their own engineering org getting substantive feedback under velocity pressure, and skim
probability rises with diff size while agent diffs are large by default. A senior skimming 900 lines and a
senior reviewing 900 lines are byte-identical on the host.

**"What if a competitor ships faster without any of this?"**
They will, until the first incident on a client's revenue. That is the honest answer and it is worth saying
out loud rather than pretending the trade does not exist. What this buys is not speed; it is that we can
tell a client what was verified.

**"Does this survive us growing to twenty engineers?"**
The gates and the depth tiers do, because they are per-repository and per-diff rather than per-person. Two
things do not scale by themselves: the weekly hour needs a named owner or it stops happening, and reviewer
attention is the binding constraint — which raises the question of who becomes able to review, and we have
no mechanism for that. See R5.

**"What stops this becoming bureaucracy?"**
A real risk, and the two things holding it back are deliberate. Anything sitting at tier 3 for a month
either becomes a check or gets deleted. And a gate that has never caught anything is supposed to die: the
runbook's pruning decision exists so the standard can shrink. Every governance regime without a shrinking
mechanism grows until it is routed around.

### From a developer

**"Do I have to write specifications now?"**
The agent drafts it; your job is to interrogate it. Three sections cannot be agent-drafted, because writing
them requires understanding the system: the open questions, the risks, and what we are deliberately not
doing. If those three came from the agent, the review did not happen.

**"Am I just going to be approving AI output all day?"**
That is the failure mode this is designed against, which is why escalations route by class rather than all
queueing to whoever holds the ticket. You answer ambiguity and novel territory. Commercial questions go to
whoever owns the SOW, criteria changes to a code owner, taste to the tech lead, and a wrong gate to whoever
owns the gate.

**"What if a gate is wrong?"**
Say so — that is class D, and it is the most under-reported class precisely because working around a check
is easier than arguing with one. Gate removal has a defined path: evidence that it never caught anything, a
named remover, and concurrence where it protects a live client surface.

**"Will I stop learning if the agent writes everything?"**
We do not have a good answer. `14-limits.md` cites the survey — 16% of senior engineers say juniors fully
understand the code they submit, against 85% of juniors saying AI improves their understanding — and then
provides no mechanism. Recorded as R5, open. Anyone claiming this is solved is selling something.

**"Is this more meetings?"**
No meetings are added. One hour a week, one named person, and the questions that used to become meetings
get closed in the design document instead.

### From a client

**"Do you use AI on our code?"**
Yes, and it is named in the SOW with written permission before any engagement starts. What we do **not**
yet have written down is the harder half: what an agent may *read* and transmit, checked against your MSA
and DPA, subprocessor restrictions, retention and residency. That is R1, it is open, and it needs an answer
before the next engagement rather than during it.

**"Is the code you deliver original? Our contract says it must be."**
We cannot currently prove it. There is no licence-compatibility scan, no copyleft check, and no detection
of verbatim third-party reproduction in generated code. R2, open, and it is the failure class that ends a
relationship rather than costing a sprint. Do not answer this one confidently in a room.

**"How do I know the work is actually finished?"**
Every acceptance criterion names the artefact that proves it — a test, a screenshot, a query output, a run
URL — and an empty cell fails the release. Alongside it you get what the release does *not* verify, which
is the more useful document.

**"What happens when something breaks?"**
Rollback tested rather than assumed, with the time recorded. With one honest caveat: where we do not own
the pipeline — a live theme, a client-controlled deploy — **merge is exposure**, and a rollback rehearsal
has no environment to happen in. That is R4, and on those surfaces the answer today is weaker than it
sounds.

### From a technical evaluator

**"What actually stops the agent bypassing this?"**
Nothing in the repository does, and we do not pretend otherwise. Hooks are hints — `--no-verify` walks past
them and an agent can edit the hook files. What holds is the set of checks the host refuses to merge
without, plus one job that reads the host's real configuration back and fails when it stops matching what
the repository claims. That check is the one that makes every other check's claim honest.

**"Is 300 lines not arbitrary?"**
It is judgement, and the documents say so. What is measured is the direction: over 1,000 lines, **84%** of
pull requests draw findings, averaging 7.5 each. E5 exists to move the number to wherever our own evidence
puts it.

**"What if the tests and the code share the same misunderstanding?"**
Nothing here catches that at low consequence, and no standard we have read does either. Proving a test
*can* fail catches a missing proof, not a wrong one. Our partial answer — expected values computed by hand
rather than by the model that wrote the code — is currently keyed to novelty, which nobody can measure,
when the property that predicts damage is consequence. D11, open.

**"How much of this is running versus written down?"**
Ask this of us and of anyone else presenting a standard. Our answer: the gate logic is proven to reject and
to discriminate by an offline harness that is itself mutation-tested, and the host half — a red check
actually blocking a merge — was still unproven at the time of writing. Every row that says *written* rather
than *proven* means exactly that.
