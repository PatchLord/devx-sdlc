# Ops To-Do Board — a simulated engagement

**Everything here is fictional.** Marigold Living does not exist. Priya Menon, Dev Rawat, Anjali Sharma and
Karan Iyer are invented, as is every order number, date and rupee figure. The *process* is real; the client
and the engagement are not.

**What it is, in one sentence: a shared to-do list for a small team.** Add a task, assign it to a person,
mark it done, put it back if it was not. Due dates that mean the same afternoon to everybody, and one
reminder before something is late.

Three things are bolted onto that core, and they are there to make the *process* work hard rather than to
make the product clever: some tasks appear by themselves when the store says something changed, so there is
a live external dependency with timeouts and retries; who may complete or reassign whose task is a real
permission question no code can answer; and sending a reminder cannot be undone, so it is a dangerous path
needing a second reviewer. A plain single-user to-do list would exercise none of that, and the front half of
the process would be theatre.

These are the stage 00 Solutioning artefacts, produced to demonstrate the
[AI SDLC](https://github.com/PatchLord/devx-sdlc) end to end on a project shaped like real client work: an
ops task board for a merchant's team, tasks raised from real store signals, assigned to a person, completed
by a person.

## The current state, which is the point

**The SOW is not signed.** The tech lead returned it unsigned with four blocking changes. That is not a
failure of the exercise — it is the exercise producing its intended output, and it is the most useful thing
in this folder.

| Artefact | State |
|---|---|
| [`docs/brd.md`](docs/brd.md) | Client brief, v1.1. Theirs. Still contains the contradiction the meeting did not resolve |
| [`docs/meetings/2026-08-06-discovery.md`](docs/meetings/2026-08-06-discovery.md) | Frozen. Where the contradictions surfaced |
| [`docs/sow.md`](docs/sow.md) | **v1.0, the agreement** — 1,100 words, everything you need to decide whether to sign |
| [`docs/sow-terms.md`](docs/sow-terms.md) | the full wording, 23,000 words |
| [`docs/annexes/`](docs/annexes/) | six annexes — criteria, check statuses, exclusions, obligations, AI use, depth |
| [`docs/archive/sow-v1.0-monolithic.md`](docs/archive/sow-v1.0-monolithic.md) | the same document before the split, kept as evidence of the failure mode |
| [`docs/reviews/2026-08-06-sow-tech-lead.md`](docs/reviews/2026-08-06-sow-tech-lead.md) | The verdict and the four blocking changes |
| [`docs/reviews/2026-08-06-sow-hostile.md`](docs/reviews/2026-08-06-sow-hostile.md) | Adversarial review of both documents |
| [`docs/reviews/2026-08-06-what-the-reviews-changed.md`](docs/reviews/2026-08-06-what-the-reviews-changed.md) | What the reviews forced, including risks accepted with a name against them |
| [`docs/reviews/2026-08-06-sow-revisions-partial.md`](docs/reviews/2026-08-06-sow-revisions-partial.md) | Partial. Commercial terms, signatures and accepted risks, which the draft lacked |

## The revision, and the thing it exposed

All 19 required changes landed, and both verifiers agreed the four blocking ones closed properly — the
data-protection sentence is now graded at three different strengths with three artefacts; discovery's
sequence is inverted so the permission and the data-handling note are preconditions of the first store read;
authentication arrived as an outcome whose criterion enumerates routes *from the router* rather than from a
hand-written list; and the webhook receiver got authenticity, freshness and a second owner.

Neither verifier would sign it, and both found the same material defect independently: **§14 and §15 were
referenced nine times and did not exist.** The revision also introduced a contradiction of exactly the class
that got v0.9 returned — §11.1 sold "production provisioned from code" while §5.4 twice declines that as a
High row we are not buying. Eight further fixes were applied by hand afterwards: the two missing sections
spliced in, that contradiction removed, three wrong cross-references, a version-history date that had copied
the wrong row's date, a floor/ceiling pair that omitted a priced option, a decision dated after the
agreement it decides, and one weekday that was wrong (11 August 2026 is a Tuesday).

**And the honest problem with the result: it was 32,000 words.** v0.9 was 13,000. Every addition was demanded
by a reviewer and every one is defensible on its own, and the aggregate was a document a founder would not
read — the sentence you most need someone to see ends up on page forty.

**Fixed by splitting rather than by cutting. Nothing was removed**, and that is verified mechanically rather
than asserted: all 325 table rows and every one of the 146 identifiers (`A-`, `N-`, `X-`, `C-`, `D-`, `S-`,
`P1-`, `P2-`) from the monolithic version appear in the split set. The check found two real losses on the
first attempt — a whole section my split script skipped because it sits before §1, and a column I had trimmed
from two rows — and both were restored.

The reading path is now **1,100 words → 23,000 → 18,400**, in that order, with each tier pointing at the
next. That is how contracts are normally built: a short agreement plus schedules.

One diagnosis worth keeping, because it is not a formatting problem. **The document is long because the
process has unclosed gaps.** Pages of it exist to disclose that we cannot prove originality of agent-written
code (R2), that our read-and-transmit position is half written (R1), and that no check has been proven on a
host (B1). Closing those would shorten this document more than any editing pass.

The revision document is incomplete and says so: the agent that produced it was truncated mid-output, so the
revised sections 1–10 do not exist. Recorded rather than quietly regenerated, because a gap that is named
costs less than one that is smoothed over.

**One more defect, and the client found it.** §15 carries eighteen accepted risks. The two-page agreement said
thirteen, split seven / two / four, when §15 actually carried seven / two / nine. Two rows in it were both
numbered 13 — the same risk about the Google Sheet, written twice — so nineteen rows counted to eighteen and
nobody noticed either number was wrong. An agent playing Dev Rawat found it by reading his own signature block
in §13.1 and counting what he was being asked to sign for. Both verifiers had read §15 and neither had counted
it. That is the cost of a two-page summary of a 23,000-word document, and it is not an argument against the
summary: it is that every number in the short version is a copy with no link back to the thing it counts, so
it goes stale silently while the long version stays correct. The reader most likely to check is the one
signing. Fixed by merging the duplicated row, correcting the counts, and making §13.1 say why its list of six
is shorter than the nine in §15 instead of reading as a third count.

## The four blocking changes, because they are the demonstration

1. **A data-protection sentence that the document itself contradicts.** §10.4 promised that a customer's
   personal data "never enters a model prompt". §10.2, nine hundred words earlier, admits there is no
   removal of personal data from prompts "as a mechanism rather than a habit". A client reads both at the
   same strength.
2. **The first piece of work would have handled client personal data before the policy existed.** Discovery
   measures fulfilment lag against roughly ninety real orders by 14 August. The engagement's data-handling
   note is drafted on 18 August, and the client's written permission had no date at all. A store read
   returns customer names, emails and shipping addresses.
3. **Phase 1 had no authentication criterion.** The criteria exhaustively covered which role may do what,
   and nothing asserted that a person who is not a user sees nothing. The criteria began at "everyone sees
   every task", which assumes the answer to the question nobody asked.
4. **The phase-2 webhook receiver proved idempotency and not authenticity.** A public endpoint that creates
   work for four people, with no criterion for rejecting a forged payload.

None of those is a typo. Each is the kind of thing that is discovered in October by a client rather than in
August by a reviewer.

## What passed

The tech lead checked for it specifically: **no row in the SOW says *proven*, and there is no
defect-reduction, velocity or improvement percentage anywhere in it.** The document says our process has not
run end to end on a host, states what that means for every check it lists, and names the route from
*written* to *proven*.

His signature block refuses two things outright — selling High depth while two of its rows are still to
build, and any warranty that agent-written code is provably original. The second is an open question in the
standard, and the process surfaced it in a commercial document rather than leaving it to be found in a
contract review.

## What happens next

The four blocking changes landed in v1.0 above, so the front half is done and the build is what remains.
**How it gets built is [`run-plan.md`](run-plan.md)**, and the non-obvious part of it is the order: the
ungoverned control branch is cut before the governed one, from a shared baseline, and is given the plain ask
rather than the acceptance criterion. That document also registers five predictions and four failure
conditions in advance, so the result cannot be fitted to a narrative afterwards.

Signature is the gate on starting, and it is the reviewer's to give — in this engagement that is one person
playing several roles, which the run plan commits to stating rather than letting it be discovered.

The board for this project lives in `tasks/board.md` once the repository exists.
