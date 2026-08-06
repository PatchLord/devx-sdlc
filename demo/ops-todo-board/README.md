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
| [`docs/sow.md`](docs/sow.md) | **v1.0** — all 19 required changes applied. 32,000 words, and that is a problem in itself; see below |
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

**And the honest problem with the result: it is 32,000 words.** v0.9 was 13,000. Every addition was demanded
by a reviewer and every one is defensible on its own, and the aggregate is a document a founder will not
read. Disclosure has a length budget, and past some point disclosure becomes concealment — the sentence you
most need someone to see is now on page forty. That is a genuine finding about the process, not a
complaint about the reviewers, and it is the next thing to fix.

The revision document is incomplete and says so: the agent that produced it was truncated mid-output, so the
revised sections 1–10 do not exist. Recorded rather than quietly regenerated, because a gap that is named
costs less than one that is smoothed over.

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

The four blocking changes get made, the SOW is re-issued for signature, and only then does anything get
built. The board for this project lives in `tasks/board.md` once the repository exists.
