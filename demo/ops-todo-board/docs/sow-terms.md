**FICTIONAL DOCUMENT — CREATED FOR A DEMONSTRATION.** Marigold Living does not exist. Dev Rawat, Priya Menon, Anjali Sen, Farhan Qureshi, Ravi Menon, Tarun, Rakesh, Anjali (customer care), Kalyan Ceramics, the Leicester 3PL, Anjali Sharma, Karan Iyer, Nikhil Barve, Sneha Raut, Imran Shaikh, Deepa Kulkarni, and every date, order number and rupee figure below are invented for a simulated engagement. Third-party model-provider names are withheld deliberately: in a real SOW the provider is named in writing in Annexe A and the client's written reply is attached as Annexe B, and naming one in a fictional document would attach a real company to an invented engagement. devx labs' process is real; this client, this engagement, these prices and these dates are not.

# Statement of Work — Ops To-Do Board: full terms

| | |
|---|---|
| **Client** | Marigold Living (fictional) |
| **Supplier** | devx labs |
| **Version** | **1.0 — issued to Marigold** |
| **Date** | 11 August 2026 |
| **Written by** | Anjali Sharma, delivery lead, devx labs |
| **Reviewed and signed by** | Karan Iyer, tech lead, devx labs. He returned v0.9 unsigned on 6 August 2026 over four blocking changes and one failure of this document's own completeness test |
| **Stage** | 00 Solutioning |
| **Inputs** | BRD v1.1, 6 August 2026 (Marigold's own document) · Discovery meeting notes, 6 August 2026, frozen · Tech-lead review of v0.9, 6 August 2026 · Adversarial review of the same draft, 6 August 2026 |
| **Annexes issued with this document** | **A** — the named third-party model provider, its retention terms and its processing region. **B** — Dev Rawat's written reply accepting Annexe A, dated and timed |
| **Status of this version** | Issued to Marigold. Nothing in it is offered or agreed until the signatures in §13 are on it |

> **v0.9 was returned unsigned, and this is what that produced.** Karan named four things he would otherwise have been in a room explaining: a data-protection sentence in §10.4 that §10.2 admitted was untrue nine hundred words earlier; a work sequence that read ninety of Marigold's real UK orders four days before the note governing uploads existed; a phase-1 login and a phase-2 webhook receiver that were both in scope with no criterion and no place on the protected list; and no criterion anywhere for the thing the whole board hangs off — a scheduled reader — failing silently. It also failed the completeness test below, on item 4. All five are closed in this version. Where closing one meant writing down something Marigold will not enjoy reading — that we cannot demonstrate originality of agent-written code, that we cannot prevent a gate being switched off inside an account we do not own, that keeping what Priya types out of a model prompt is an instruction to four named people rather than a mechanism — it is written down rather than smoothed. **One thing survived every edit untouched, and Karan checked for it specifically: no row in this document says *proven*, and no percentage of defect reduction, velocity or improvement of any kind appears anywhere in it.**

---

## How to read this

**This is the full terms document.** The two-page agreement that gets signed is
[`sow.md`](sow.md); it carries the price, the dates, the four things Marigold must know before signing, and
the signature lines. This document is everything behind it, and it is the one to consult when a question
turns on wording. It is the whole engagement: what you get, what you do
not, what we will not verify, what we need from you and when, what it costs, and who carries which risk.

Six annexes hold the detail — every acceptance criterion, every check and its status, the full exclusion
list, the full obligation and decision tables, the AI-use inventory and the depth reasoning. **Nothing was
removed in the split.** They are there to be consulted, not read end to end, and where an annexe and this
document disagree, **this document governs**.

| | |
|---|---|
| [Annexe A](annexes/annexe-a.md) | Acceptance criteria — every one, with the artefact that proves it |
| [Annexe B](annexes/annexe-b.md) | The checks, and whether each is *written*, *proven* or *to build* |
| [Annexe C](annexes/annexe-c.md) | Out of scope, all twenty-two |
| [Annexe D](annexes/annexe-d.md) | What we need from Marigold, with dates, and the open decisions |
| [Annexe E](annexes/annexe-e.md) | AI use: the data inventory, the preconditions, what our position does not cover |
| [Annexe F](annexes/annexe-f.md) | Depth, the compensating controls, and what reopens the decision |

An earlier version of this document was a single 32,000-word file. It is kept at
[`archive/sow-v1.0-monolithic.md`](archive/sow-v1.0-monolithic.md) because it is evidence of a real failure:
every addition in it was demanded by a reviewer and defensible alone, and the aggregate was unreadable.

## How to check this document is complete

Our own process says a person who did not write the SOW must be able to point at six things. They are here, in this order, so nobody has to trust that they exist. The fourth column is new: v0.9 listed all six and satisfied five, and the tech lead would not sign past a test he put in the process himself.

| # | The thing | Where | Satisfied at issue |
|---|---|---|---|
| 1 | The signature date | §13 | Yes, with the reason it is that date rather than a later one |
| 2 | The depth level, with its reasoning | §4 | Yes — and §4.3 now records the one place this project sits outside our own table, with the name of the person who accepted that |
| 3 | The personal-data inventory | §10.4 | Yes, and it no longer states as fact a control §10.2 says we do not have |
| 4 | The named third-party AI provider, with written permission attached | §10.1, Annexe A, Annexe B | **The row that failed in v0.9.** Annexe A carried a placeholder and Dev's written reply was outstanding. Annexe B is that reply, dated and timed, attached to this issue. In this fictional rendering the provider's name is redacted and §10.1 says so in those words |
| 5 | What happens after go-live | §11.4 | Priced, with the fix path inside the freeze window described rather than implied. Which option Marigold buys is Dev's, and if it is D then 8 October is a handover |
| 6 | The list of our checks, every row marked *written*, *proven* or *to build* | §5.2 | Yes. No row says *proven*, and the sentence above the table says why |

A missing one means Solutioning is not finished. It does not mean it will be caught later. v0.9 is the evidence that the test works: it was missing one, and it did not get signed.

---

## 1. The engagement, in one paragraph

devx labs will build Marigold Living an internal task board for the operations team. It is a shared to-do list for a small team, and that is the order to read it in. One board the named users see the same version of, on a phone as well as a laptop. A person adds a task in their own words. Priya assigns each task to one named person, that person completes it, and every completion is recorded with who did it and when, so Priya can put it back if it was not really done. Nobody who is not a user sees any part of it. Then, on top of that list, two signals from the Shopify store put work on it without anyone going to look — a product dropping below a stock floor Marigold sets, and an order passing the dispatch promise Marigold has published — which is what stops the board being a second place to look and makes it the thing worth opening at nine in the morning. The board reads from Shopify and never writes to it: it tells a human what to do, and the human does it in Shopify under their own login. **Phase 1 is usable by four real people on real orders by 25 September 2026 — on two conditions, and they belong in this paragraph rather than nine sections later: read-only store access in Marigold's hands to ours on 11 August (C-1), and this document signed by 20 August. Every working day either is late is a working day off the eighteen available, and what comes out of the set if that happens is ranked in §2.3 rather than argued in the third week of September.** It is finished changing before Marigold's freeze — last merge Friday 2 October, last deploy 8 October. Phase 2, in December and January, adds due dates that mean the same thing in India and the UK, reminders before something is late rather than after, and a live feed from the store so signals arrive as they happen instead of on a schedule. Marigold owns the repository, the hosting and every third-party account from the first day.

That paragraph is written to be repeated to Anjali Sen and to Ravi Menon without either of them reading anything else. Which is exactly why the two conditions are inside it: the people who approve the money are the people most likely to hear the date and never the conditions attached to it.

---
## 2. Scope, by phase, as outcomes

Each row is an outcome — a thing that is true when we are finished — not a task. What proves each one is in §7, **including the two rows in §2.0 that devx added to its own scope.** Work we put in the price is not exempt from the rule we wrote about criteria.

### 2.0 Before the board: two named pieces of work

These are not overhead and they are not free. Both came out of discovery.

| | The outcome | Why it is scope and not a task inside the first ticket |
|---|---|---|
| **S-1** | **The store's actual behaviour is measured and written down**: how often inventory really changes on the ~60 SKUs that move, what the orders data actually contains, and how late a UK fulfilment event arrives relative to the order being paid — measured against roughly 90 real UK orders, not taken on anyone's word. **This measurement handles Marigold's customers' personal data.** A Shopify orders read returns names, email addresses and shipping addresses. The board does not ingest them; this piece of work does handle them, and those are two different sentences | Marigold has no technical person available. The freelancer who set the store up does not answer. Our process expects at least one call with the client's own technical people, and where there is not one, the system's behaviour has to be *discovered*. Discovery has a duration; an assumption does not, until it is wrong in October |
| **S-2** | **The shapes everything else is built on are fixed first**: who may see the board at all and how a person proves they are that person; who may see, complete, assign and reopen a task; what a task is; what a stock floor is; what the dispatch clock starts and stops on | Code can be rewritten in an afternoon. A permission model that four people's work sits on top of cannot. Freezing this for four people and arriving in November with seven is how every later ticket inherits the wrong shape |

**One thing about S-1 that v0.9 had the wrong way round, said plainly because the correction is the useful part.** §10.4 says the board does not ingest customer data. That is true of the board. The first thing this engagement does is read ninety of Marigold's real UK orders, and that handles customer names, email addresses and shipping addresses. In v0.9 the measurement happened on 14 August and the note governing what may be uploaded to a model provider was drafted on the 18th — so the engagement would have touched Marigold's customers' data four days before the policy for it existed, in the phase most likely to have an agent session attached. The order is now the other way round, and as a precondition rather than a plan:

- **Dev's written reply to Annexe A (C-7) and the engagement data-handling note (D-5) are both in place before the token in C-1 is used.** D-5 is drafted 7 August and signed before 10 August, not on the 18th.
- **The measurement is done by hand, by Karan Iyer, against a field-limited query** — the fields the measurement needs and no others — **with no agent session attached.** If that changes, it is a change Dev signs.
- **No captured real payload is committed as a fixture.** Our own fixture rule would otherwise put real customer records into Marigold's repository permanently, where the review job transmits every diff containing them. Fixtures are hand-synthesised from the payload's *shape*. The extract lives outside every agent-readable path and has a deletion date recorded. The rule is in §10.
- **If C-7 and D-5 are not both in place, S-1 does not start**, and the date in §1 moves rather than the rule bending.

That sequence is why our own process now dates the AI-processing permission ahead of *discovery* rather than ahead of the *build*. "The product does not ingest customer data" can be true of the product and false of the work that precedes it, and this document is where we found that out about ourselves.

### 2.1 Phase 1 — the board, by 25 September 2026

Usable by Priya, Tarun, Rakesh and Anjali (care) on real orders. Farhan joins from September.

The order of the rows below is the order the product is: the login boundary, then the shared list a person works from, then the two store signals that make the list worth opening, then ownership. v0.9 put the two auto-created signals above "a person can add a task themselves", which reads as though ingestion is the product. It is not. This is a shared to-do list for a small team; a person creating and completing a task is the core, and the signals are what make it useful. **Nothing has moved in or out of scope in this reordering, and the numbers are the ones v0.9 gave these outcomes** — they are deliberately not resequenced, because §7's criteria, §2.3's drop order and Marigold's own reading of the draft all point at them, and a tidier column would break every reference to it.

| # | Outcome |
|---|---|
| **P1-0** | **Nobody who is not a user sees anything.** Every route on the board refuses a request that carries no valid session; a person signs in as themselves; a session expires; and closing an account — a temp's, on the day the festive window ends — ends that person's access. This is an outcome and not an assumption: the board is reachable on the internet and holds seven people's names, a record of what each of them did and when, and Marigold's order numbers. **v0.9 had no such row**, and §7.1 now opens with the criteria for it |
| **P1-1** | **One board all users see the same version of.** Everyone sees every task. Unassigned tasks sit at the top so they cannot be quietly ignored. Works on a phone, including Rakesh's, at the signal quality of the Bhiwandi unit — against a device and network profile that is written down, and subject to that profile's own criterion in §7.1 and to D-8. (v0.9 said "subject to A-8" here. A-8 is the stock-floors criterion. It was a wrong cross-reference on the row that carries the hardest platform requirement in the document) |
| **P1-4** | **A person can add a task themselves**, in their own words, because half of Priya's day is neither stock nor orders. §7.1 names a browser test that fills the form and presses the button. A screen with no criterion that clicks it is exactly how our own pilot shipped nine write paths and no buttons — the story §4.2 tells Marigold as a reason to buy Standard |
| **P1-5** | **Every task carries exactly one person's name, and it got there because Priya put it there.** A rule proposes the name — stock to Tarun, packing to Rakesh, customer-facing to Anjali (care), money or vendors to Priya — and nothing is assigned until Priya, or her named backup, confirms it. No person is told to do anything by a computer |
| **P1-7** | **Completion is a record, not a claim.** Who marked a task done, and when. Priya, or her backup, can put it back. Nothing is deleted, in this phase or the next |
| **P1-8** | **The person whose name is on a task is told, once, when it lands.** Nobody else is told. The message carries the task reference and the order number and **never the free text of the task**, so what a person types into the board cannot leave it through a message. And a message that would arrive in the middle of the recipient's night is held and delivered at 08:00 in that person's own day: Anjali (care) works UK evenings, and an assignment made at 08:30 IST reaches her at 03:00 otherwise — the one person whose muted phone costs Marigold a customer is the one the notification design was not written for. There is no automatic message to the group on assignment — that is the decision in §3, row X-4, and the reason is in it |
| **P1-10** | **Priya can answer "what is unfinished right now and who has it" in under a minute without asking anyone.** "Under a minute" is a number, so it is timed once with a named person doing it and the recording kept — §7.1 |
| **P1-2** | **A task appears by itself when a product drops below its floor**, without anyone opening a sheet or a screen. The longest acceptable gap between the reading that saw the crossing and the task existing is a number in §7.1's criterion, not whatever the schedule happens to do — otherwise "by itself" is satisfied by a nightly poll and Priya's February happens again with better paperwork. How often we read is D-3 |
| **P1-6** | **Stock floors exist for every product without Priya typing 900 numbers.** A default per category, a per-product override, and one screen where forty can be changed in a sitting. The ~200 new festive SKUs inherit their category default the day they are created |
| **P1-3** | **A task appears by itself when an order passes its dispatch promise.** The clock starts when the order is paid and stops when it is fulfilled. What "its dispatch promise" covers — India-warehouse orders only, or India and UK — is settled by D-1 in §8, not by this document. What the clock counts against — elapsed hours or working days, which end of Marigold's published 3–5 days for the UK, and the days the unit is shut — is a separate open decision in §8 with a stated fallback, and whichever it is, the screen says so in words next to the number. Priya will disbelieve a number she cannot reconcile exactly once, and then stop looking at it |
| **P1-9** | **An independent record of what the store said.** Every inventory reading we take, per product, with a timestamp, appended and never edited, never archived, held apart from the board. This is what makes it possible to ask *did the board miss a crossing* rather than asking the board whether it missed anything. It is independent of the **board**; it is **not** independent of the **reader** that writes it, and v0.9 overstated that. If the reader stops, there is no reading and no task and the two counts agree perfectly again — which is why the reader's four failure modes are acceptance criteria in §7.1 rather than monitoring wishes |
| **P1-11** | **Marigold owns everything from day one.** Repository in Marigold's organisation from the first commit; hosting and every third-party account in Marigold's name, on Marigold's card, with Dev as owner and devx added as a member. What that costs us in enforcement, and what we do about it, is §5.5 |

**Landing by Friday 2 October 2026** (last merge — v0.9 said 3 October, which is a Saturday), inside phase 1's price, deferred from the 25th because eighteen working days will not hold all of it:

| # | Outcome |
|---|---|
| **P1-12** | **One message to the Marigold Ops group each morning at 08:00 IST**: what is outstanding and who has it. It carries task references and order numbers, never free text. Anjali (care) receives her copy at 08:00 in her own day rather than at 02:30 in her night — one digest, two send times. Channel subject to D-2 in §8; the path to being able to send the first message at all is Marigold's, and it is in §8.2 with dates against it |
| **P1-13** | **Stock floors can be typed in the Stock Watch sheet and imported**, on an explicit press, with the board reading back what it understood so a fat-fingered number is visible |
| **P1-14** | **A mirror tab in the sheet, written by the machine**, so Priya can see the board from inside the file she thinks in |
| **P1-15** | **Completed tasks leave the screen after seven days.** They leave the *screen*. They stay in the database |
| **P1-16** | **A screen showing, for a chosen week, what was marked done and later put back, by person.** The data behind it is captured from the first day of P1-7, so choosing not to build the screen would not have cost the history |

### 2.2 Phase 2 — December 2026 to January 2027

**Standard depth does not simply carry across this boundary.** §4's four questions are asked again, in writing, before the first phase-2 ticket, because P2-3 introduces an endpoint anyone on the internet can post to and that is a different answer to the first question than "Marigold's own staff". If the answers move, the depth moves with them, and it only moves up.

| # | Outcome |
|---|---|
| **P2-1** | **A due date means the same afternoon to everyone who reads it.** A task due "end of Tuesday" is unambiguous to Rakesh starting at 07:00 IST and to Anjali (care) working a UK evening, and the board shows each person the deadline in their own day |
| **P2-2** | **A reminder arrives before something is late**, not after. Once per task. A reminder that has been sent cannot be unsent, so this path is treated as a dangerous path: it is on the protected list in §5.1, it needs a second reviewer, and send-once behaviour is a criterion with an artefact against it |
| **P2-3** | **Signals arrive live.** The store tells the board when something changed, instead of the board asking on a schedule. The receiver is a public endpoint that creates work for seven people, so it is on the protected list in §5.1 alongside the notification path, and authenticity is a criterion and not an assumption: an unsigned or mis-signed payload is rejected **and counted**, and a valid payload replayed outside its freshness window is rejected. Those sit in §7.2 next to the idempotency criterion v0.9 already had — which proved that a signal arriving twice does not produce two tasks and proved nothing at all about who sent it. This narrows — it does not remove — the blind window described in §6, row N-2 |
| **P2-4** | **The reading ledger records which signals arrived live and which came from a scheduled read**, so the November verdict's error bar and the January one are comparable rather than merely different |

Phase 2 does not fit before 8 October and we are not going to pretend otherwise. Dev's own document says that if we claim it does, he will assume we have not understood the freeze. He is right.

### 2.3 If the 25 September set has to shrink, this is the order

v0.9 said features would come out "named at the time". That is the sentence that becomes an argument in the third week of September, so it is a lookup instead. The rule above it is unchanged and is in §5.3: **features come out, Setup stays.**

**Never dropped, at any amount of pressure:** Setup and the four proofs in §5.3 · **P1-0** · **P1-1** · **P1-2** · **P1-4** · **P1-5** · **P1-7** · **P1-9** · **P1-11**. Below that line the board stops being the product and Marigold has bought a demo.

| Out first | What comes out | What Marigold still has | Why it is this one |
|---|---|---|---|
| **1** | P1-6's bulk-edit screen — forty floors in a sitting | Category defaults and per-product override, so every product still resolves to a floor; the sheet import in P1-13 does the same job by 2 October | It is a convenience over a path that already works. Costs Priya an evening, costs the board nothing |
| **2** | P1-10's dedicated view | The board itself, filtered by person. The question is still answerable, less quickly | The outcome is a minute, not a screen. Dev's own test 4 can still be run against the board |
| **3** | P1-8's message on assignment | The board, the unassigned pile at the top of it, and the 08:00 digest from 2 October | The row most likely to be forced out rather than chosen: its channel depends on D-2 and on Marigold-side verification and template approval nobody controls. If it goes, it goes for that reason and not to buy time |
| **4** | P1-3's UK half | India-warehouse late orders, with the screen saying in words which orders it covers | Already agreed in the room as D-1's consequence, so it costs no new argument and no new signature |

Anything on this list coming out is a scope note Dev signs on the day it happens, at the Wednesday demo, with the reason. §12 is the path. It is not a silent omission and it is not discovered in October.

---
## 3. Explicitly out of scope

Two kinds of row: things Marigold said they were not asking for, and things that were discussed and declined. The second kind is the useful kind, so the reason is written next to each.

> The full table — **22 rows** — is in [Annexe C: Out of scope, in full](annexes/annexe-c.md). Nothing was dropped in the split.

---
## 4. Depth: **Standard**

Depth is how much apparatus the work carries. It is set by **what a mistake costs** — not by budget, not by SKU count, not by how important the project feels. Four questions set it, and Marigold should be able to argue with each answer.

### 4.1 The four questions, answered for this project

| Question | Answer here |
|---|---|
| **What breaks, and who feels it?** | Marigold's own staff. No Marigold customer has any reason to open the board and none of their data is ingested into it. But **"internal" describes who it is for and not who can reach it** — the board is on the public internet, which is why P1-0 exists and why the login boundary is on the protected list in §5.1. Two failures, then. The realistic one is a task nobody sees, which is what happens today, every day, in a WhatsApp group. The other is somebody who is not a user reading seven people's names and a record of what each of them did |
| **Can it be undone?** | Mostly. In phase 1 the board only reads from Shopify, so a bug cannot change stock, cancel an order or edit a product, and a bad screen is redeployed. In phase 2, one thing cannot be undone: a reminder that has been sent. And one thing cannot be undone in either phase, which v0.9 did not say because it only asked the question about deploys — **disclosure.** A personal-data store on the internet that shows the wrong person the wrong thing cannot be un-shown by a redeploy. That is the irreversibility that bears on this project, and it is why the login boundary and the personal-data paths carry a second human rather than a note |
| **Does it touch money, or sensitive or regulated data?** | No money. No customer personal data ingested from Shopify into the board — though S-1's measurement handles it, per §2.0, and that distinction is the whole of change 2 from the tech-lead review. It does hold **staff personal data** — four to seven people's names and phone numbers, and a record of what each of them did and when, including the reopen statistics in P1-16 |
| **How long will it live?** | Years. This replaces a paper list and a group chat, so it is not a two-week demo and the documentation and tests should assume a new person reading them in 2028 |

### 4.2 Why not Light

Light is for work where a mistake costs nothing to undo and there is no personal data. Two things rule it out. It holds staff personal data with a monitoring purpose attached, which creates duties even on a day when nothing is broken. And it will live for years, which is what makes a missing test expensive later rather than never.

There is a second reason, and it is the one worth reading. Light is not the same product with fewer checks. Our own observation on an internal pilot, on a sample of fifteen requirements in one session: requirements that named a config file, a hook or a test behind them arrived **8 times out of 8**; requirements written only as prose arrived **0 times out of 7**. The admin panel in that pilot shipped nine write paths and zero buttons — the write side existed at every layer except the one a person clicks — because the check it was given could only see whether a page rendered, and a page with no Create button renders perfectly. That is a count on a small sample and it is **not a prediction about Marigold's project**. What it changed is how we write acceptance criteria, which is §7. Choosing Light here would mean choosing to receive less than was specified, in a shape nobody predicted, on a board whose whole point is a screen people type into.

Keeping those two counts in a document a client reads was **Karan Iyer's call, and it is recorded as a risk with his name on it.** He expects "8 out of 8" and "0 out of 7" to be quoted back at us out of context by somebody who never reads the qualifying sentence, and prefers that to removing the only evidence we actually have.

### 4.3 Why not High — and the one place this project sits outside our own table

Our own depth table says High applies where there is **money, personal data, or something that cannot be undone.** Three limbs. §4.1 answers the middle one **yes**. §4.2 then uses that same fact to rule out Light. v0.9's version of this section ruled High out on the other two limbs — "High is where money moves, or where something cannot be undone. Neither is true of phase 1" — and never came back to the middle one. That is not an argument that beat our table; it is a limb going missing between two sections of the same document, and Marigold's adviser will read D-10 with that table in front of them.

So, properly. **The personal-data limb of our own test is met and we are still recommending Standard. That is a deviation from our own table, it is recorded here as a deviation, and Karan Iyer accepted it** — it is in this document's accepted-risk section with his name against it, not glossed. The compensating controls he accepted it on, so that Marigold can argue with each:

- No money moves, in either phase.
- No customer personal data is ingested into the board (§10.4). The one activity that handles it is S-1, governed separately, done by hand, with no agent session attached (§2.0).
- No write reaches the store in either phase (X-1), so no mistake of ours changes stock, an order, or a product.
- The personal dataset is four to seven of Marigold's own staff, listed in an inventory with a purpose and a retention period next to it, and the people it is about are told it exists.
- uat exists, so a change is exercised somewhere real before it reaches the people using it.
- The paths where being wrong is expensive — the login boundary, personal data, permissions and authorisation, migrations, phase 2's notification path and its receiver, and the gates themselves — carry a code-owner review by someone other than the author.
- Request logs carry a field allowlist, with a test asserting the logger drops everything not on it.
- Dev and uat carry invented data only, with no masking step for anyone to skip.

**Two named triggers reopen this, rather than a quarterly review happening to notice:** any write to the Shopify store, and any ingestion of customer data into the board. Either is a different answer to a question in §4.1, and depth goes up with it and never quietly down.

Then what High would have added — and here v0.9 oversold one row, which is change 7 from the tech-lead review. Three of High's additions are real and we can operate them: a second environment and its running cost; a load test; and a restore drill with the restore time written down. **The second named approver on a protected path is not one of them.** There is no per-path approval count on the host to set — the setting is repository-wide, and demanding two approvals on every trivial ticket is arithmetic we reject elsewhere in this document — so it has to come from two owner entries on the protected paths, and our own record of that mechanism says *believed to work, never tried*. It therefore belongs in the same column as the two rows we decline outright: **to build**, until it has been demanded and satisfied once on a real repository. That is why it is now the fourth thing Setup has to produce before a feature ticket starts (§5.3).

That matters at Standard too, and not only in the column we are declining. The second code owner named in §13.4 exists so that a fortnight's leave cannot stall a protected merge, and that arrangement rests on the same untried mechanism. §5.2 was honest about the dependency; v0.9's §4.3 was not, and a client reads the confident sentence.

The two we decline outright are unchanged. Mutation testing — checking that the tests would actually fail if the code were wrong — and a full audit trail of who changed what are **to build** on our side: no tool, no threshold, and no settled definition of what counts as core logic. Buying High today would mean paying for a written commitment on those rather than a running check, and we are not selling that.

So: **Standard**, with one exception carried forward — **phase 2's notification path is treated as a dangerous path when we reach it**, because a message that has been sent cannot be unsent. That means a second reviewer on it, and send-once behaviour named as a criterion with an artefact. And with §4's four questions re-asked at the start of phase 2 rather than Standard being carried across the boundary, per §2.2.

### 4.4 What Standard buys, and what High would have cost

> The full table — **9 rows** — is in [Annexe F: Depth, and why not High](annexes/annexe-f.md). Nothing was dropped in the split.

Depth is re-checked if the answers change. It goes up with them and it never quietly goes down. Two triggers are named in §4.3. One event is scheduled rather than triggered: **the four questions are asked again, in writing, at the start of phase 2**, because a public endpoint that creates work for seven people is a different answer to the first question, and because any phase-2 write to the store would be a different answer to the second.

---
## 5. What we check before anything ships — and the honest status of it

### 5.1 What we do, in plain language

Agents write most of the code on this engagement. That is stated plainly in §10 and it is why this section exists at all: when generation gets cheap and checking does not, the thing worth buying is the checking.

- **One repository, in Marigold's organisation, from the first commit.** Nothing is pushed straight to the main branch. Every piece of work gets its own branch and its own pull request. That the main branch is protected at all is a setting on Marigold's account, not something we can impose — §5.5.
- **Intent is written down before the code exists.** Each piece of work starts with a short spec that a person approves, and that spec has to be the branch's first commit and an ancestor of every code commit on it. **What is enforced is ancestry, not chronology.** v0.9 said intent "cannot be back-dated", and that is not true as written: commit dates are trivially settable and a branch that started with code can be rebased into legality. The honest sentence, and the one that is worth something: **a branch where the code came first cannot merge without being rebuilt, and the rebuild is visible.**
- **A change cannot quietly weaken the things that check it.** If a pull request edits an existing test, a coverage threshold, the pipeline configuration or the acceptance criteria, that edit has to sit in its own commit where a reviewer can see it. It cannot ride inside a change to the product.
- **Small pieces.** A pull request warns above 300 changed lines or 10 files and fails above 400 or 20. Going over is a person's decision, taken by someone other than the author. The reason is not tidiness: on large diffs, reviewers skim, and skimming and reviewing look identical afterwards.
- **Format, lint, types, tests and build run as one command**, locally and again on the server, and that command **fails rather than skips** when something is not wired. A repository that documents six checks and runs four reports green for the two that never ran.
- **80% coverage on the lines this change touched** — not on the whole repository. A whole-repository number is one you inherited; a changed-lines number is one you earned.
- **A fresh agent session reviews every diff** with no memory of having written it, and every finding it raises ends either fixed or dismissed in writing. Never neither.
- **A second human on the paths where being wrong is expensive**: **authentication and the session boundary**, personal data, permissions and authorisation, phase 2's notification path, **phase 2's webhook receiver**, database migrations, the pipeline configuration, existing tests, coverage thresholds, and the acceptance criteria themselves. An agent may propose a change to a criterion; only a named person approves one, or criteria become a description of whatever got built. Two of those entries are new in this version, and both were in scope in v0.9 with no place on this list. And the mechanism that produces the *second* human is itself unproven — see §5.2 and Setup exit 4.
- **Secrets and known vulnerabilities are scanned on a clock**, over the whole tree, not only on the diff — because an issue introduced by a change that passed is invisible to anything that only reads new changes.
- **One job asks the hosting platform what it actually enforces and fails when that stops matching what this document claims.** This is the check that makes the other checks' claims honest. Our own pilot's context file asserted that its main branch was protected; there was no remote and the pipeline had run zero times. **That job reports. It cannot prevent** — §5.5.
- **No developer or agent session holds production credentials.** The session cannot reach production because the credential does not exist in it. That is not an instruction to the agent; it is an absence — and because it was an absolute in v0.9 with no status row anywhere, it now has one in §5.2 that says exactly how far the absence goes and what it does not cover.
- **A weekly demo of working software.** Wednesdays, 09:30 IST, 30 minutes, recorded, avoiding Dev's Tuesday and Thursday afternoons. Software doing something, not a deck and not a percentage complete.

**§5.1 names the surfaces. §7 is where each becomes a criterion with an artefact against it, and three of them are new in this version.** A protected path with nothing in §7 asserting anything about it is a line in a text file — the same failure §5.2's ownership row describes from the other direction. So, written out here so that a reader can check it rather than trust it, §7 must carry:

1. **The login boundary** (§7.1) — every route on the board refusing a request with no valid session, enumerated from the router rather than sampled; the sign-in boundary driven in a browser; session expiry; and a closed account's session ending. v0.9's permissions criterion began at "everyone sees every task", which assumed the answer to the question nobody asked.
2. **The scheduled reader's four failure modes, as four criteria** (§7.1) — it did not start, it processed zero rows, it ran twice, the failed-signal queue is not empty — each with the alarm's own test run as its artefact. Both of the board's auto-signals hang off that reader, and if it dies on 2 October the board looks calm.
3. **The phase-2 receiver's authenticity** (§7.2) — an unsigned or mis-signed payload rejected and counted, and a valid payload replayed outside its freshness window rejected.

If any of those is absent from §7 when this document is signed, then this section is describing a perimeter the criteria do not have, and that is worth catching before signature rather than in a release document in October.

### 5.2 The honest status of every one of them

Read the status words literally.

- **Written** — the file exists and its logic has been exercised away from a live host.
- **Proven** — it has run on a host **and failed something it was supposed to fail**.
- **To build** — it protects nothing today.

**Nothing in this table says *proven*, and that is not modesty.** Our process has not run end to end on a host. The middle column has been changed since v0.9, which said "at Setup" on nine rows — a commitment wearing a status's clothes, in a table whose entire purpose is status. It now says what is true on **11 August 2026**, which for almost every row is *nothing*, because Marigold's repository does not exist yet. What each becomes is Setup's job; when Setup runs is in §8's schedule; and the four things that prove Setup actually finished are in §5.3. The right-hand column is the honest state of the mechanism itself, on our side, today.

> The full table — **16 rows** — is in [Annexe B: The checks, and the honest status of each](annexes/annexe-b.md). Nothing was dropped in the split.

### 5.3 The one place this stops being a written claim

Setup does not end when the files are in place. It ends with **four** things Marigold can look at:

1. One trivial page — a build identifier and nothing else — **live in dev, put there by the real pipeline**, with the build id matching a tagged commit and a pipeline run.
2. The job that reads the host's configuration back has run on the host and passed, with a link to the run.
3. **One throwaway pull request has been deliberately blocked by a check**, with a link to the run that blocked it.
4. **One pull request on a protected path has had a code-owner review demanded of it and satisfied**, by the second owner rather than the author, with a link to the run. New in this version, and it exists for two reasons. An ownership pattern that matches nothing is owned by nobody while still reading as protected, and a group named in that file which does not resolve blocks every merge with an error message that explains nothing. Until this has happened once, every protected-path sentence in §5.1, §7 and §12 is decoration. It is also the only thing that will tell us whether the two-owner mechanism §4.3 and §13.4 both rely on works at all.

The third and fourth are the ones that matter. Until a check has been watched failing, we have tested that it runs, not that it stops anything — the same way a backup nobody has restored is a belief. **When those four exist, we will re-issue the table in §5.2 with the rows that moved and the run links against them.** That is the only route from *written* to *proven* on this project, and it happens before the first feature ticket, not after the freeze.

Setup is also the stage that gets cut when a timeline slips, and it is the worst possible thing to cut: every standard added later leaves everything written before it unchecked, and that debt appears in no diff. If the 25 September date comes under pressure, **features come out of phase 1 and Setup stays** — in the order ranked in §2.3, so that nobody has to negotiate it in the third week of September. That is a commitment in this document, not a preference.

### 5.4 Production, named

Standard depth buys dev and uat. Four real people work real orders from 25 September, and that does not happen in dev. v0.9 said "Environments: dev and uat", proved one page live *in dev*, and promised four people on real orders — three sentences that do not fit together, and Dev's own document forbids "we'll sort out production later" in those words. So:

- **There is a production environment**, provisioned by **Friday 18 September 2026** — a week before the 25th, not on it — in a region named in the design document before anything is provisioned, and inside the running-cost band in §11.3.
- **Karan Iyer provisions it and owns it.** At Standard it is **not** defined in code before it is provisioned. That is High's row and we are not claiming it, and the cost of not buying it is exact rather than rhetorical: an environment set up by hand can be reproduced only by the person who set it up, from notes, and that person is one person. It is a hole we are describing, not one we are hiding.
- **What runs there is the artefact that was promoted, not a rebuild.** §7.1 carries the criterion and its artefact: the build identifier live in production matches a tagged commit, a pipeline run, and the same artefact that passed in uat.
- **Nothing is patched on it by hand.** The deploy identity belongs to the pipeline; no person and no session holds it. That is what §5.1's credentials rule means in practice, and §5.2's row for it says how far that goes.
- **A defect fix inside 8 October – 5 December reaches production only with Dev's sign-off per fix**, per §6 row N-6, through the same gates as any other change.

### 5.5 The perimeter reports. It cannot prevent

Every gate in §5.1 is a setting or a token on a repository Marigold owns, in Marigold's organisation, on Marigold's card, with Dev as owner. That is what P1-11 buys and we are not proposing to change it. What has to be said out loud is the consequence, because v0.9 said "it is a setting on Marigold's repository" and stopped there:

**Dev — or anyone at Marigold given administrator rights — can switch off a required check, change branch protection, or rotate the token our configuration job reads with. Our answer is that the job *reports* it, the next time it runs. It cannot prevent it.** There is no version of this in which a supplier's document enforces something inside a client's account, and a document that implies otherwise is describing a perimeter it does not have.

Three things instead of that implication:

- **One named administrator on the repository: Dev Rawat**, and nobody else, per §8.2. A gate is not removed by somebody who did not know it was a gate.
- **A gate removed mid-phase stops merges the same working day**, and it is said at the Wednesday demo rather than worked around. Merging past a missing gate is our own pilot's failure with a client's name on it.
- **The one exception in this engagement is named as an exception** — the hand-maintained ticket status in §5.2's last row, with Karan Iyer's name on it — so that a non-conforming corner of this project is a recorded decision rather than a silent hole. If a second one appears, it gets a row and a name in the same way.

And the honest limit of this whole section, which is the same shape twice: **nothing we run can see a change made inside the Shopify admin** (§6, N-1), and **nothing we run can stop a change made inside Marigold's repository settings.** Both are holes. Both are in this document as holes rather than as things we quietly hope nobody tests.

---
## 6. What we will **not** verify, and how Marigold will know

Every release hands Marigold a document with three columns: what was checked, how, and the artefact that proves it. A fourth section on the same page says **what this release does not verify**. Nobody volunteers that section, which is exactly why it is in the template — someone reads that file during an incident, and the useful half is the half about what nobody looked at.

Some of these are known today and can be written down before a line of code exists. This list grew by four rows between v0.9 and v1.0 rather than shrinking, and where a row is a risk somebody accepted rather than a gap we closed, **that person is named in the row**.

| # | What will not be verified | How Marigold will know |
|---|---|---|
| **N-1** | **Nothing we build can see a change made inside the Shopify admin.** If someone edits a product, a price or an inventory count in Shopify itself, our board finds out next time it asks. This is a hole, not a design choice | Named in every release document for the life of the engagement, and named here. Phase 2's live feed narrows it; it does not close it, because a live feed can be missed or delayed — which is what A-44 is for |
| **N-2** | **Anything that dips below its floor and recovers between two readings did not happen, as far as the board is concerned.** Priya's brass candle holders on a Saturday are exactly this shape | The reading ledger, P1-9, makes the gap *visible*: the interval between readings is in the data, so the number Dev takes in November arrives with its own error bar instead of pretending it has none. The interval is D-3, and D-3's fallback interval is **in force at issue** rather than promised — so the size of this window is a number in this document today, not one that arrives later |
| **N-3** | **We do not verify that a UK order's dispatch clock is accurate** unless D-1 resolves in time. The 3PL's fulfilment event is what stops the clock, and nobody at Marigold can say when it arrives | If D-1 slips, phase 1's late-order signal covers India-warehouse orders only, the board says so on the screen, and it is a signed scope note rather than an October discovery |
| **N-4** | **We do not verify that a message was read, or that it reached a handset at the Bhiwandi unit.** Patchy signal, an old handset and a muted app are outside anything we can check. **Narrowed from v0.9:** the provider does return a send status, and pretending otherwise threw away a cheap alarm | The board is the record. A message is a convenience. If a task's only existence is a message, we have rebuilt the group chat. What we now also do: a send the provider rejected raises an alarm — **A-36** — so a failure to send is noticed rather than silent. Delivered-to-provider is a different claim from read-by-Rakesh, and only the first has an artefact |
| **N-5** | **We do not verify how the board behaves under Diwali load.** A load test is not in Standard depth and is not being bought — X-11. **Karan Iyer's accepted risk**, recorded in §15 | Instead: an agreed budget for how often we read the store, which in v0.9 appeared in four places with nobody's name on it. It now has an owner, a date and an alarm — **A-35**, Karan Iyer, agreed with Dev before 25 September — so the one way an internal tool can hurt Marigold's customers is bounded by a number both sides agreed and watched by something that fires |
| **N-6** | **Marigold's freeze does not literally cover this board**, because the freeze is written about things customers can reach and the board is internal. We do not think that was intended | Made explicit instead: no feature deploys after 8 October; a defect fix inside 8 October – 5 December needs Dev's sign-off per fix, by the path described in §11.4; and the read budget above |
| **N-7** | **We cannot cheaply verify that a test and the code are not sharing the same misunderstanding.** Both are written by the same kind of session, so a wrong test and a wrong implementation can agree and both look green | Partial answer, stated as partial: on the parts that matter, expected values are computed by hand rather than by the thing that wrote the code — A-18, A-40 and A-17 all name hand-computed values. No standard we have read solves this at reasonable cost, and we are not claiming to. **Karan Iyer's accepted risk**, in the middle of our own value proposition, recorded in §15 |
| **N-8** | **We cannot verify that agent-written code contains nothing that reproduces third-party code.** No licence-compatibility check, no copyleft check, no verbatim-reproduction detection | §10.3, and it is the reason we cannot sign Marigold's originality warranty as written |
| **N-9** | **We do not verify Marigold's business outcomes.** Not the under-3% target, not the 90 minutes a day, not the fifteen-minute teach test | X-8. We verify that the numbers those judgements need exist, are correct, and cover what they claim to cover. The judgement is Marigold's, and the meeting at which it is made is in §14 rather than in nobody's calendar |
| **N-10** | **What a person types into a free-text task is not verified or filtered.** See §10.4 | Stated in §10.4 rather than promised away, and A-25 keeps that field out of the logs, the error reports and the messages — which is a smaller claim than filtering it and the one that has artefacts |
| **N-11** | **We do not verify that Shopify's stock number matches the shelf.** Priya wrote this down as her own first question — the site's number and the shelf's number disagree, and Rakesh will say the shelf is right — and the entire stock-floor signal fires off Shopify's number | Disclosed here, where a founder reads it, instead of being resolved in our favour inside an assumptions list, which is what v0.9 did. Reconciliation is a warehouse problem and it is excluded in X-21. What the board does instead: state which number it read and when, so a wrong task is traceable to a wrong reading rather than argued about. **Dev Rawat's accepted risk**, recorded in §15 |
| **N-12** | **We do not claim phase 1 moves the count of orders past dispatch promise, and we are saying so before Dev measures it in November.** P1-3 fires *after* an order has breached. Nothing in phase 1 tells anyone an order is *about* to be late — due dates and reminders are P2-1 and P2-2, in December | The honest sentence Dev asked for directly in his own document: **phase 1 makes the number exist and makes it trustworthy; it cannot be expected to reduce it, because it only fires after the breach.** The thing that could move it is a pre-breach warning, which is P1-18 — a phase-1-sized piece of work nobody proposed in the room, now priced and **not bought**. If it stays unbought, the November figure is a baseline and not a result, and §14 says so on the day. **Dev Rawat's decision, still open** |
| **N-13** | **We do not verify that the sheet and the Monday export stop being used.** P1-14 keeps a mirror tab alive and X-18 keeps Tarun's Monday export running | Dev's sixth test is about Priya's 90 minutes, and two scope decisions point away from it. Both were asked for: the mirror by Priya, on the argument, and the export by nobody — it survives because nobody agreed to retire it. Recorded so November is a lookup rather than an argument. **Dev Rawat's accepted risk**, recorded in §15 |
| **N-14** | **We do not verify that the board is pleasant to use.** There is no designer on this engagement, and "it works" and "somebody will use it every day for three years" are different claims | The predecessor product died of being unpleasant, so this is disclosed rather than assumed away. What we do instead is a named artefact and a named person, not a design practice: the design brief in **A-38** — every screen's empty, loading, error and validation state, and every breakpoint down to A-27's device profile — accepted by Priya in writing **before implementation tickets exist**, plus design tokens in Setup so a screen can be compared against a frame at all |

---
## 7. How the work is accepted

The rule that carries the most weight in this document: **every acceptance criterion names the artefact that will prove it.** A criterion with prose in that column fails a release rather than passing it. "Verified" is not evidence, and neither is "we tested it manually".

The criteria live in the repository on a protected path with named owners. An agent may propose a change to one. Only a named person approves one. Criteria an agent can edit to match what it built are not criteria.

**The criteria added at v1.0 are appended rather than renumbered.** A-1 to A-17 still mean what they meant in v0.9, so anything already written against them still resolves; the new phase-1 rows run from A-18, and phase 2's five original rows moved to A-40 to A-44 to make room. Where a v0.9 criterion promised more than its artefact showed, it has been narrowed rather than left broad, and the four corrections are listed by name after §7.3 so a reader comparing the two versions can find them.

### 7.1 Phase 1

> The full table — **39 rows** — is in [Annexe A: Acceptance criteria](annexes/annexe-a.md). Nothing was dropped in the split.

### 7.2 Phase 2

**Before the first phase-2 ticket, §4's four questions are asked again rather than carried forward.** Standard was set against a board that only reads, on the public internet behind a login. Phase 2 adds an endpoint anyone on the internet can post to, which creates work for seven people — that is a different answer to *what breaks and who feels it*, and it may be a different depth. Karan Iyer re-answers the four in writing at the start of phase 2, and the answer goes to Dev before any of it is built. **The receiver's path joins the protected set in §5.1 alongside the notification path**, and A-47 is what demonstrates it.

> The full table — **8 rows** — is in [Annexe A: Acceptance criteria](annexes/annexe-a.md). Nothing was dropped in the split.

### 7.3 How Marigold accepts a release

In v0.9, acceptance was a property of our own paperwork, signed by our own QA. That is structurally the same thing as a "QA phase" with no artefact behind it, which is the line on an old invoice Dev is still angry about. So there is a client side to it, and it is short enough to use.

| Step | What happens |
|---|---|
| **1. We offer the release** | With its document: what was checked, how, the artefact, and what this release does not verify. **Every criterion in the release has a non-empty artefact cell or the release is not offered.** Imran Shaikh signs that the artefacts are the artefacts, which is a devx signature and is not acceptance |
| **2. Marigold accepts, at the right level** | **Priya Menon signs for behaviour. Dev Rawat signs for anything touching data or store access** — the same split as §9.1, so nobody is asked to accept something outside what they decide |
| **3. Three working days** | Priya may extend once, by three more, by saying so. No form |
| **4. A rejection names the criterion** | And what about the artefact does not satisfy it. That is a rejection we fix inside the price. "It does not feel right" is a legitimate thing to want and a different thing to want: it is a change request under §12, priced, not argued about |
| **5. Silence accepts** | If nothing arrives inside the window and no extension was asked for, the release is accepted. **That is deemed acceptance and it is Anjali Sharma's term, disclosed rather than buried** — a release accepted by silence in Diwali week, inside Dev's own three-to-four-day window, is the risk it creates, and Priya's single extension is the whole of the mitigation. It is in §15 with my name on it |

*Corrections made in this section between v0.9 and v1.0, named so a reader comparing the two can find them: **A-7** promised "a full day's work" and now says what its artefact shows; **A-10** promised "never archived" with nothing behind that half and now names the job inventory; **A-3** was broader than a hand-check that read the same Shopify timestamp as the machine, and now carries a check against something outside Shopify; **A-7's cross-reference to A-8** — the stock-floors criterion — is corrected to **A-27**, the device and network profile. The same wrong reference to A-8 appears in §2.1's P1-1 and is corrected there, in that section. A-11's opening clause was not a wrong reference but a wrong assumption, and it is rewritten above.*

---
## 8. Assumptions, dependencies, and what we need from Marigold

### 8.1 Decisions still open at the time of writing

Each has an owner, a date, what it blocks and what happens if it slips. These are not caveats; they are the shape of the plan.

> The full table — **15 rows** — is in [Annexe D: Obligations and decisions, in full](annexes/annexe-d.md). Nothing was dropped in the split.

**D-2 and D-3 are Karan's own, they are due the day v1.0 issues, and they have no float on the path to signature.** So neither is written here as a promise that it will be closed. Each carries a fallback that is **in force at issue**: if Monday's answer never arrives, this document still describes a working system at a stated cost, and nothing in §8.4 moves. An answer that does arrive improves a number and changes A-15, A-20 or §11.3 — never a date and never a scope row.

### 8.2 What we need from Marigold, and by when

> The full table — **23 rows** — is in [Annexe D: Obligations and decisions, in full](annexes/annexe-d.md). Nothing was dropped in the split.

**The perimeter reports; it cannot prevent.** Every check in §5 is a setting on an account Marigold owns. That is the right way round for ownership — it is what X-1 and P1-11 are for — and the uncomfortable way round for control, so we are saying the consequence out loud rather than leaving §5.2's "it is a setting on Marigold's repository" to be read as a detail. Dev can turn off a required check, relax branch protection, add a second administrator, or rotate the token in C-19, and our answer is that the job in §5 **notices and tells him**. It cannot stop him. Therefore: **C-21 names him as the only administrator**, so there is one person to ask; and if a gate is removed mid-phase we **stop merging on that repository the same working day**, say in writing which gate went and what it was protecting, and do not resume until it is back — or until its removal is recorded as a written exception with his name on it and a date it is revisited. That is the same shape as the one exception this document already carries: hand-maintained ticket status in §5.2, named as an exception in that word rather than left as a quiet hole.

### 8.3 Assumptions

Stated so that a wrong one is a change request rather than an argument.

1. The warehouse is in **Bhiwandi**. The Pune reference in the BRD was the vendor cluster.
2. Users at go-live: **Priya, Tarun, Rakesh, Anjali (care)**; **Farhan** from September; **two named temp accounts** in November. **Seven by mid-November, not four.**
3. Shopify remains the system of record for products, inventory and orders, and remains where customer data lives and is governed. **This does not assume Shopify's number matches the shelf.** Priya raised that disagreement in writing, it is not resolved by this document, and it is disclosed in N-11 rather than settled in our favour inside this list — which is what v0.9 did.
4. Shopify's own read APIs, rate limits and event behaviour do not change materially during the engagement, **on the version pinned in C-22**. A sunset inside the freeze is a change request with a date on it, not a surprise.
5. The dispatch clock starts when an order is paid and stops when it is marked fulfilled, both as recorded in Shopify.
6. Marigold's published promises are 48 hours to dispatch for India and 3–5 days for the UK. **What those figures mean against a calendar — 3 or 5, elapsed or working, Sundays and holidays in or out — is D-12, and is not assumed here.**
7. **Everyone with a session sees every task.** Visibility is an authorisation decision (A-11) sitting on top of an authentication boundary (A-18, A-19), which v0.9 had in neither scope nor criteria. If visibility changes to per-team, the permission model changes, and the permission model is the one shape everything else sits on.
8. Nothing is deleted in either phase.
9. Hosting is in a region Marigold's adviser is content with; the region is named in the design document before anything is provisioned, and production is named in §5.4 rather than left to be decided under launch pressure.
10. Marigold has, or will nominate, an adviser for the legal questions in D-6, D-10, D-11 and D-15. We will not give a legal opinion on any of them.
11. The estimate that running cost fits inside ₹35,000 a month holds only with D-2 and D-3 answered. Until then, §11.3's messaging line and its database line are estimates and are labelled as ones.
12. **The dates in §8.4 assume C-1 on 11 August and signature by 20 August.** Both conditions are stated in §1's paragraph, next to the 25 September promise, rather than nine sections away from it.

### 8.4 The dated schedule

v0.9 contained no dates for its own stages while "eighteen working days" was load-bearing in two sections. Here they are, so a slip is arithmetic rather than a conversation. The arithmetic is the one Anjali Sharma did in the room at 10:56: signature realistically the 20th, then Kickoff and Setup, a feature ticket starting on the 1st or 2nd of September, and eighteen working days to the 25th.

> The full table — **22 rows** — is in [Annexe D: Obligations and decisions, in full](annexes/annexe-d.md). Nothing was dropped in the split.

Two dates in this table are ours to miss and nobody else's: 7 and 10 August. If they slip, S-1 does not start, and every date below them moves day for day. That is stated here rather than in §9.3 because it is the only row in the schedule where the dependency is devx's.

---
## 9. Decisions: who, how fast, and what a late answer costs

Answer speed is a delivery constraint here, not a courtesy note. With building compressed, Marigold's turnaround may set the timeline rather than our capacity — Dev wrote this down himself instead of telling us he was very responsive, which is the most useful thing in his document.

### 9.1 Who decides what

| Area | Decision-maker | Backup |
|---|---|---|
| **How the board behaves** — states, who gets what, what a floor means, wording, workflow | **Priya Menon** | **Farhan Qureshi**, same authority, behaviour only — subject to D-4 |
| **Money** | **Dev Rawat** | none. Not delegable |
| **Anything touching customer data** | **Dev Rawat** | none |
| **Anything touching store access** | **Dev Rawat** | none |
| **Repository and hosting settings** — turning a check on or off, branch protection, who else administers it | **Dev Rawat**, as the only named administrator per C-21 | none. A second administrator is a change to this row, not a convenience |
| **Accepting a release** | **Priya Menon** for behaviour; **Dev Rawat** for anything touching data or store access — §7.3 | Priya may extend the window once |
| **What Marigold accepts** — any change to an acceptance criterion | Priya proposes; **Anjali Sharma** routes it; a devx code owner approves the change in the repository | — |

### 9.2 Agreed response times

| Who | Their commitment |
|---|---|
| **Priya** | Same working day if it reaches her before 18:00 IST |
| **Dev** | Small decisions inside his 09:30 and 21:00 IST windows, about four hours. Anything needing thought, 24–48 hours. **Not Tuesdays or Thursdays 11:00–18:00 IST.** **12 October – 30 November: three to four working days** for anything not on fire |
| **Money over ₹1.5 lakh** | Plus Anjali Sen, London: two working days, three across her Friday |
| **Money over ₹5 lakh** | Plus Ravi Menon: **one week, not compressible** |
| **devx labs** | Anything Marigold asks: same working day. Anything we owe with a date on it: that date, or a message before it saying why not |
| **devx labs, 8 Oct – 5 Dec** | **The Indian festive season is our team's leave as well as Marigold's peak, and v0.9 promised same-day answers across it with nobody named to give them.** Named cover: **Nikhil Barve to 8 November, Deepa Kulkarni from 9 November**, with **Karan Iyer** reachable throughout and **Anjali Sharma** covering the week of 9 November. If Option A or B in §11.4 is bought, its response time is that named person's obligation on the day, not a rota nobody wrote down. If anyone in that list changes, Marigold is told before it matters |

**The rule both sides agreed:** any money decision is raised in the week it is first foreseen. One raised in week five that was visible in week two gets a no on principle, even where a yes was available in week two.

**On the fee itself, the week-long path has already been spent.** Anjali Sen and Ravi Menon approved the **₹18–26 lakh envelope in writing on 5 August** — Annexe C — so what Dev signs is a number inside an approval that already exists, and signature is not waiting on Ravi Menon a second time. That is why this document arrives on the 11th rather than the 15th, and why §8.4 can put signature on the 20th at all. **Any change that takes the fee outside that envelope re-enters the week-long path and cannot be compressed** — which is what §12's scope-cut table is for, and why a change with a money consequence is raised in the week it is first seen rather than the week it is needed.

### 9.3 What happens to the timeline when an answer is late

| Situation | What we do | What it costs |
|---|---|---|
| An answer we need to keep building is late | We move to work that does not go stale: shared shapes, hand-synthesised payload shapes committed as fixture files, test scaffolding, project-specific tooling. We do **not** write specs for far-future work, because those describe a codebase that will not exist | Nothing, for about three days. Beyond that, dependent work slips **day for day**, and the slip is reported at the Wednesday demo with the waiting split into waiting-on-us and waiting-on-them |
| **D-5 or C-12 late — and this one is ours** | Nothing of Marigold's is uploaded and the C-1 token is not used, so **S-1 does not start**. We do not proceed on the argument that a read is harmless | Same shape as C-1 being late, except the delay is devx's and Karan Iyer owns it. It is in §8.4 as our own two dates for that reason |
| **C-1 (store access) late** | S-1 cannot start, so we cannot measure, so we cannot answer D-1, so the late-order signal has no agreed contract | The **most expensive single dependency in this document.** Every working day C-1 is late is a working day off the eighteen available before 25 September |
| **D-1 unanswered on 14 August** | The UK late-order signal moves to phase 2 and the board says on screen what it covers | No date slip. A scope reduction Dev signs, per the agreement in the meeting, with the price change in §12's table rather than a scope cut Marigold pays full price for |
| **C-18 to C-23 late** | Setup cannot finish. A gate that cannot be turned on is not a gate, and §5.3's four exit proofs cannot be produced at all | **Setup does not shrink**, so this comes off the eighteen working days before 25 September, day for day. Four of these five rows are settings, not work, and each is a ten-minute job on the day somebody looks |
| **C-14 to C-17 late or refused** | The message set moves to email, on the fallback that is already in force in D-2, and the board states which channel it is using | No date slip and no scope loss. It is a worse channel for Rakesh, who opens one app, and that is the whole of the cost. Meta verification can be refused for reasons neither side controls, which is why the fallback is written now |
| **C-6 (Priya's floors) late** | Phase 1 demonstrates on category defaults only | The 25 September set exists but has little to raise a task about, which makes the pre-window fortnight a weaker test than it should be |
| **D-8 (the handset) late** | A-27's profile is set from the closest device we can buy and labelled as an assumption in the release document | If the real phone fails that profile after 2 October, the fix is January. A-7's 15 September date exists to make this discoverable while it is still fixable |
| Signature after 20 August | Kickoff and Setup shift with it. **Setup does not shrink** | Features come out of the 25 September set **in the ranked order in §2.3**, not "named at the time" — one working day of scope per working day of delay |
| Anything late inside 12 October – 30 November | Expected, and planned for at three to four working days | Deliberately nothing is scheduled to need Dev in that window except a defect-fix sign-off, a release acceptance under §7.3, and the 90-day review on 25 November |

---
## 10. AI use on this engagement

### 10.1 What we do, stated plainly

**An agent writes most of the code on this engagement.** A person approves the plan before code exists, and a person judges the result. No line reaches Marigold's repository without passing the checks in §5, which Marigold can inspect in their own repository at any time.

**Marigold's material will be sent to a named third-party model provider.** The provider, its data retention terms and the region the processing happens in are named in **Annexe A**, which is issued with this document. **Nothing of Marigold's — not a document, not a line of code, not a store response — is uploaded until Dev has replied in writing that the annexe is acceptable, checked against Marigold's data processing agreement.** "We will confirm that later" is not available; Dev said so, and it is also our own rule. That reply is **Annexe B**, attached to this version, dated and timed, because the whole value of the rule is the line it draws in time.

**And the permission is dated ahead of discovery, not ahead of the build.** This is the change v0.9 needed most and the one that is invisible until somebody looks for it. The first thing this engagement does is read Marigold's real orders to measure how their systems actually behave — which handles live customer names, email addresses and shipping addresses — and v0.9 had that read happening on 14 August with the note governing it drafted on the 18th. So Annexe B, the processor agreement in C-12 and the data-handling note below are **preconditions of S-1**, all of them dated before the read access in C-1 exists. §10.6 says what S-1 handles, who does it, and what is done to the extract afterwards.

*In this fictional document, Annexe A carries a placeholder where the real provider name, retention terms and region go, and Annexe B carries a placeholder signatory. In a real engagement both are filled before the document is issued, because an unnamed provider makes this section unsignable and an undated permission makes it unenforceable.*

### 10.2 What our position does **not** yet cover

Naming this is not a disclaimer. A client document that hides a known gap is worse than one that names it, because the gap gets discovered at the worst possible moment and everything else in the document is re-read as marketing.

**The permission half is written. The read half is not.** We have the part Dev asked for: the provider is named, he signs, and until he signs nothing moves. What we have **not** finished writing down is what an agent may *read* and transmit — there is no per-engagement matrix saying these repositories yes, these logs no, production data never, checked line by line against a client's data processing agreement; no removal of personal data from prompts and session transcripts as a mechanism rather than a habit; no stated position of our own on how long a provider retains a session or which region it sits in beyond what the provider's terms say; and nothing written about how an agent is used at 23:00 during an incident, which is the case §11.4 sells. That is a known gap on our side, it is recorded as an open question in our own research, and it needs an answer **before** this engagement rather than during it.

What Marigold is therefore buying, and what closes it: **a written data-handling note for this engagement** — which repositories, which documents, what never enters a session, retention, region, **and what happens during an incident** — signed by Karan Iyer and by Dev. It is D-5 in §8, Karan owns it, and its dates moved in this version because the sequence in v0.9 did not work: **drafted Friday 7 August, signed before Monday 10 August, and in force before the store access in C-1 is used.** It is no longer a Kickoff deliverable, because Kickoff is after the first read.

**One thing the note cannot do, and does not claim: it is an instruction to named people, not a mechanism.** Nothing in our pipeline inspects a prompt. That is why §10.4 separates what the system enforces from what people are told, and why this section stays in the document after the note is signed rather than being replaced by it.

### 10.3 The originality warranty

**Marigold's standard clause — "all deliverables are original work, free of third-party intellectual property" — cannot be signed as written, and we are saying so before signature rather than after a dispute.**

We have no licence-compatibility scan, no copyleft check, and nothing that detects a generated block reproducing third-party code verbatim. So we cannot demonstrate originality on agent-written code. **A warranty we cannot stand behind is worse for Marigold than a qualified one**, because at the moment it matters they would be holding a promise nobody can test.

What we will put in front of Marigold's adviser instead: a qualified clause, plus a plain description of what we actually do — the code is reviewed by a fresh session and by a person, it arrives in pieces small enough for a person to read, and third-party dependencies are scanned for known vulnerabilities and kept current. **That is not the same thing as originality and we are not going to call it that.** D-6 is the path; it is Marigold's adviser's call, not ours.

One thing to read next to it: the provenance decision in §10.7 is evidence in exactly the dispute a qualified clause creates, which is why the two questions go to the same adviser in the same conversation rather than one being settled by engineering while the other waits.

### 10.4 Personal-data inventory

What the board holds, why, and for how long. This is the input to the logging rules and to the invented-data rule in §10.5, which is why it is written now rather than derived from the schema later — a schema records what we built, not what we were allowed to build.

> The full table — **7 rows** — is in [Annexe E: AI use, in full](annexes/annexe-e.md). Nothing was dropped in the split.

Four things about this table are load-bearing.

**We will not write "the board holds no customer data", because that sentence is not true.** The board does not *ingest* customer data from Shopify, and it **can still receive customer data from a human being** — nobody can stop Priya typing *the lady in Pune called twice, her number is* into a free-text box, and a rule in a document does not stop a person typing. What we do about it is three different things at three different strengths, and they are separated below because a client reads all three at the same strength unless somebody separates them. v0.9 did not, and that single sentence is why this document was returned unsigned.

- **Logs — a mechanism, with an artefact.** Request and application logs carry a field allowlist, and a test asserts the logger drops everything not on it. The artefact is that test, and it is A-25 in §7.1. Stripping downstream would mean the data was already in a third party's storage.
- **Error reports — the same mechanism, and a criterion that v0.9 did not have.** Error payloads leave the application to a third-party tracker, so the allowlist has to cover the payload and not only the log line. A-25's second half raises a failure inside a request carrying free-text task content and asserts the captured payload contains none of it. Before this version that half of the sentence was a claim with nothing behind it, which is worse than a gap because it reads identically to the half that is real.
- **Model prompts — an instruction to named people. Not a mechanism, and we are not going to describe it as one.** Nothing in our pipeline inspects a prompt; §10.2 says so in our own words. What is actually true is smaller and still worth having. The instruction is that the free-text column of the task table is never read into a session, and it is given to four named people: **Karan Iyer, Nikhil Barve, Sneha Raut and Imran Shaikh.** It is made mostly unnecessary by an absence rather than by a rule — dev and uat hold invented rows only (§10.5), and no developer or agent session holds a production credential (§5.1), so there is no ordinary route by which a sentence Priya typed reaches a prompt. The route that remains is a person reading a production row into a session while fixing something at 23:00. That is a real hole, it is an open question in our own research, and it is closed by the data-handling note in §10.2 and the fix path in §11.4 — **as an instruction with a named owner, not as a control the system enforces.**

**The staff data is the unambiguously personal dataset in this project**, and the reopen statistics are performance monitoring of a named employee. Marigold may have that; it is not a side effect nobody declared. It goes in this inventory with a purpose next to it, and **the people it is about are told it exists.** Priya's position, recorded: she would rather Tarun knew, because half the point is being able to hold something up. Marigold's obligations on it are D-10, for Marigold's adviser. Karan is not giving a legal opinion on a call and will not give one in this document, and the decision to hold it at all is recorded as **Dev's**.

**Deletion is from the live database. Backups are not edited, and we are not going to imply they are.** v0.9 said staff phone numbers were "deleted when the account is closed" two rows above admitting that free-text content persists in backups, which is the same inconsistency §10.2 exists to prevent, in miniature. The honest version is in the table: removed from the live database on closure, present in backups until those age out at 35 days, and that number is the backup schedule rather than a promise made for this row.

**And the table was wrong about its own data flow, which is worth saying rather than quietly fixing.** v0.9 put free-text content in "the board database and its backups" and stopped, while P1-8 messages an assignee and P1-12 sends a digest every morning — so free text would have been leaving the board daily, to a third-party messaging provider, in the one table this document leans on hardest. The fix is a criterion rather than a note: messages carry a task reference, the order number and a name, and the message-content criterion in §7.1 asserts that no free-text field appears in an outbound message body. What still leaves the board is order numbers, which is what D-2 has to answer the third part of — Dev asked whether sending order numbers into a group is consistent with his own section 12, and v0.9 dropped that half of his question.

### 10.5 Invented data, and no masking script

**Development and test environments carry invented customers only.** Not masked copies of real ones — invented.

Dev anticipated the usual answer and rejected it correctly: a masking script somebody has to remember to run is a script that gets skipped on the busy day, which is the day it matters. Our answer is not a better script. **There is nothing to skip, because the board's schema has no customer data in it to mask.** That is a stronger position than a masking rule, and it is only available because of the decision in X-1 and the inventory above.

Two limits on it, both stated rather than assumed. The free-text column can hold customer data a person typed, so the schema has no customer *field* rather than no possible customer data; that is the subject of §10.4 and not of this rule. And this rule covers dev and uat — **S-1's discovery read is neither**, which is the gap v0.9 left and §10.6 closes.

### 10.6 S-1 handles Marigold's customer personal data. The board does not

Both halves of that sentence are true and v0.9 only carried the second one. A store read returns customer names, email addresses, phone numbers and shipping addresses, so the first piece of work in this engagement handles the client's customer personal data. Saying "not ingested" and stopping was true of the product and false of the work that precedes it.

**What has to be true before S-1 starts**, all of it earlier than the read and none of it during it:

| # | Precondition | By |
|---|---|---|
| 1 | **Annexe B** — Dev's written reply accepting Annexe A's named provider, retention terms and processing region, dated and timed (C-7) | before C-1 |
| 2 | **The engagement data-handling note** (D-5), drafted 7 August, signed by Karan and Dev | before Mon 10 Aug 2026 |
| 3 | **A controller and processor agreement** between Marigold and devx covering staff data and, via free text, customer data (C-12, D-15) | before the C-1 token is used |
| 4 | **Read-only store access** (C-1), read scopes only, token in Marigold's secrets manager | Tue 11 Aug 2026 |

Only then does the measurement happen, and it is **12 to 14 August**, which is why the note is dated the 7th rather than the 18th.

**How it is done, named rather than described in general terms:**

- **The query is field-limited at the request.** We ask for order id, created and paid timestamps, financial status, fulfilment timestamps, fulfilment location, and line SKUs and quantities. We do not ask for name, email, phone or address. Where a response returns fields we did not ask for, they are dropped before anything is written down — and **that dropping is a person's step, not a mechanism**, which is the tier language in §10.2 applied to our own discovery work.
- **Karan Iyer does it by hand, with no agent session attached.** He runs the query, reads the output, and writes counts and latencies into the S-1 write-up. No part of the extract is read into a session, and the write-up carries numbers rather than records. If that changes — if any part of S-1 needs an agent session — it stops and D-5 is amended first.
- **The extract lives outside every agent-readable path.** Not in Marigold's repository, not in the engagement folder the agent searches, not in a ticket. It sits on Marigold's own storage, and its deletion date is recorded on the day it is created.
- **Fixtures are hand-synthesised from payload shapes. Never a captured real payload.** This is a deliberate exception to our own fixture rule — *needed once, fetch it; needed again, commit it and read the file* — because that rule would put real customer records into Marigold's repository permanently, where the review job in §5.1 transmits every diff containing them. The exception is named as an exception and **Karan Iyer carries it**: the cost is that a fixture is a shape somebody wrote rather than a shape the store returned, and a mistake in the shape is a mistake in every test that reads it.

**What has been uploaded, and when.** Dev's condition attaches to the first document, and he is entitled to know how this one was written. Nothing of Marigold's had been uploaded when this document was drafted: the discovery notes and this SOW were written by Anjali Sharma and Karan Iyer from the BRD and the recording, and Marigold's own BRD states that no AI tool wrote theirs. Annexe B is timed for exactly this reason — it is the line before which nothing moved. After it, **every upload of Marigold's material is one row in an upload log** kept in the engagement folder: what, when, why, by whom. That log is a person writing a row and not a mechanism, it is handed to Marigold at the 90-day review, and Karan owns it.

### 10.7 Provenance in a repository Marigold owns

Not in v0.9 at all, which is the omission that would have been hardest to explain later.

An agent writes most of the code, and the repository is Marigold's from the first commit. So whatever we put in a commit trailer is a **permanent, discoverable record that AI authored their deliverable**, sitting in an asset Marigold may later show a buyer, an auditor, or the next agency. It is not reversible in any real sense: rewriting history changes every commit id, and Marigold's own branch protection forbids the force push it would take.

Two shapes are available and they are not equivalent. Provenance in the commit trailers, in Marigold's repository, permanently. Or provenance in an internal side-table keyed by commit id, held by devx, discoverable by Marigold on request and by nobody else. The first is more honest to a future reader of the repository; the second keeps a contracts decision out of an asset's permanent record.

**This is a contracts question and it is Dev's, with his adviser — D-11 in §8.** It is not engineering's to default, which is precisely what would have happened: the tool has a default, and a default chosen by whoever wired the pipeline is a permanent disclosure decision made by nobody. It also interacts with D-6, because those trailers are evidence in the dispute a qualified originality clause exists to survive.

What we do until he answers: **no provenance trailer is written, and D-11 is answered before the first commit** — before Setup, not before the first release. If it is unanswered on the day Setup starts, we hold the side-table and write no trailer, and Dev should read that as a decision made in his absence which he can change going forward and not backward. The risk that it is effectively permanent either way is recorded as **Dev's**.

---
## 11. Commercials

### 11.1 The fee

v0.9 quoted a band on phase 1 and presented a total. Both are gone, and the reason is in §11.2: the band was narrower than the uncertainty the same section names, and the total was the one figure Marigold's accountant would have held us to.

| | Price | Includes |
|---|---|---|
| **Phase 1 core** — S-1, S-2, Kickoff, Setup, P1-0, the 25 September set, and P1-12, P1-15 and P1-16 by Friday 2 October | **₹11.6 lakh, firm** | Discovery and measurement of the store per §10.6, the design brief and the design document, the perimeter and the pipeline, production provisioned and owned per §5.4 — **by hand, not from code, which §5.4 states as a hole rather than a feature** — authentication, all of §2.1 except P1-13 and P1-14, the acceptance artefacts in §7.1 including the four scheduled-reader alarms and the backup and restore work, the engagement data-handling note, Deepa Kulkarni at six hours a week, weekly demos |
| **P1-13 and P1-14** — the sheet import, and the machine-written mirror tab | **Not quoted until Friday 28 August. Capped at ₹2.2 lakh** | Quoted after S-1 and after we have opened the file (C-5). If the quote lands above the cap, Marigold drops the pair at no charge and nothing else in phase 1 moves |
| **Phase 2** — December 2026 to January 2027 | **Indicative ₹6.0 – 7.5 lakh. Not approved by this document** | All of §2.2, including the notification path and the receiver treated as dangerous paths, and the artefacts in §7.2. Re-quoted at the close of phase 1, when we know whether phase 2 inherited the UK dispatch work |
| **Priced, and not bought** | **P1-18, the pre-breach warning: ₹1.1 lakh** | The one phase-1-sized thing that could move the late-order number — see N-12. It displaces something from the 25 September set. Dev's decision, and open at signature |

**There is no Total row in this document, and its absence is the change Ravi Menon should notice first.** A total that adds a firm number, a capped later quote, an indicative phase and an unchosen support option is a single figure with four different kinds of certainty inside it, and it would be quoted back at us as a commitment. What Marigold is exposed to in 2026, as arithmetic rather than as one word: **₹11.6 lakh firm**, plus **up to ₹2.2 lakh** decided on 28 August, plus **₹0, ₹1.6 lakh or ₹2.9 lakh** depending on §11.4 — so **₹11.6 lakh at the floor and ₹16.7 lakh if everything is bought at its ceiling.** P1-18 at ₹1.1 lakh is deliberately outside that arithmetic because it **displaces** work from the 25 September set rather than adding to it — if it is bought, the ceiling does not move and the scope does. Phase 2's indicative figure sits on top of that and is not approved here. Both ends are inside Marigold's ₹18–26 lakh envelope, and the envelope itself was approved in writing on 5 August — **Annexe C**.

**Rework allowance, stated rather than implied: four engineering days per phase are included** for changes arising from our own misreading of an agreed criterion, and for the second attempt at anything the Wednesday demo shows we built to the wrong understanding. Those days are inside the price. They are not a change-request path and Marigold is not asked to approve them; they exist because assuming zero rework is how the first correction gets presented as a failure.

**And a disclosure about that allowance, because the frozen notes say this document wins.** It was never discussed in the meeting of 6 August. It reads as generosity and it also functions as a cap on our remediation of our own misreadings, classified by us, since §12 step 2 routes pricing through the delivery lead. Marigold may strike it and pay for rework as it arises; if Priya disputes a rework-versus-change classification, the classification is hers to escalate and not ours to settle. It is kept in the document with this paragraph attached rather than removed, because removing it makes the first honest correction arrive as a change request — and the term is **Anjali Sharma's**, not something the meeting agreed.

### 11.2 Why one firm number, one cap, and one indicative figure

Dev asked for one number and gave us an eight-lakh envelope to put it in. What he is getting is **one firm number for the work we understand, a capped quote deferred to the day we will understand the next piece, and an indicative figure marked as not approved** — which is a narrower commitment than v0.9's band on the part that matters and an honest absence on the part that does not.

The reason is specific, not commercial hedging. **We have no measured baseline.** Our process has not run end to end on a real project, so we have no figure for how long a ticket takes under it, and no figure for what the agent spend on a ticket costs. Quoting to a precision we do not have is exactly how the first honest correction looks like a failure — and Marigold has already paid for eleven weeks of green status reports followed by an admin screen whose buttons did nothing. A number we would revise is worse than a shape we will hold.

**Which is also the argument against v0.9's band.** A band of a lakh and a half on phase 1 sat next to a paragraph saying we had not opened the spreadsheet two outcomes depend on, had not measured the store, did not know the message channel's cost, and had never run the process end to end. A band narrower than the uncertainty it names is a point estimate with decoration on it. So the pieces we understand are quoted firm and carry the risk on our side, and the piece we have said in writing we have not looked at is not priced from inside it.

**The three lines we are least sure of**, which is what Dev asked for:

1. **The UK dispatch clock (D-1).** Whether the 3PL's fulfilment event is usable at all decides whether phase 1 has one late-order signal or two, and whether phase 2 inherits a piece of work nobody has scoped. This is the widest line in the estimate, and §12 now says what comes off the fee if it moves rather than leaving that to goodwill.
2. **The sheet import and mirror (P1-13, P1-14).** We have not opened the file. Four tabs, a fifth nobody understands, a vendor tab we must not touch, and three years of habits inside it. This is why they are not quoted until 28 August, under a cap, with a free drop.
3. **The message channel and its volume (D-2).** Karan will not quote a per-message cost from memory. D-2 was due the same day v1.0 issues with no float, so this document ships with its **fallback in force rather than a promise that it is closed**: the digest is a set of individual messages unless the API can address a group, and email is the named alternative if C-14 to C-17 do not land in time.

**On the approval path, since the fee crosses ₹5 lakh.** §9.2 puts anything over ₹5 lakh on Ravi Menon's week, which cannot be compressed. What makes signature possible without waiting on it is that the **₹18–26 lakh envelope was approved in writing on 5 August (Annexe C)** — so what Dev signs is a number inside an envelope his accountant has already approved, not a new number needing a new week. That is why this document explains its signature date rather than asserting one.

### 11.3 Running cost, against the ₹35,000 a month ceiling

v0.9's table priced two environments and left out five lines. It is rebuilt below, and the top of the band no longer fits under Marigold's ceiling. **That is the finding, not a formatting change.**

| Line | Estimate | Confidence |
|---|---|---|
| Hosting — dev, uat and **production** (§5.4) — and the board itself | ₹11,000 – 16,000 | Reasonable. Sized to seven users and this read volume. Higher than v0.9 because v0.9 priced two environments for a board four real people work on |
| Database, including backups and the reading ledger (P1-9) | ₹4,000 – 8,000 | **Estimate, pending D-3.** An append-only ledger over ~900 SKUs at an interval nobody has set is not a line anyone can call reasonable. The ledger is bounded by writing on change plus a per-cycle heartbeat rather than a row per SKU per read, which is what makes the top of this range a number rather than an order of magnitude |
| Error tracking, logs, alarms | ₹3,000 – 5,000 | Reasonable |
| **Messaging** | **₹4,000 – 9,000** | **Estimate, pending D-2, with the fallback in force.** Per-message pricing and whether the digest is one message or seven are both unresolved, and message volume is one of the two things that could break the ceiling |
| Git host — seats for the devx people in §13.4, pipeline minutes, secret and dependency scanning | ₹2,000 – 3,500 | Reasonable. Absent from v0.9 entirely, and every gate in §5 sits on it |
| Secrets manager, and the Sheets API for P1-13 and P1-14 | ₹500 – 1,500 | Reasonable |
| **The review agent's model spend, on Marigold's card** | **₹1,500 – 3,000** | **Estimate, and we have no baseline for it.** The fresh-session review in §5.1 is a required check on Marigold's repository, so it runs on Marigold's account. We do not have a measured cost per ticket, which is an open question on our side and is named as one rather than averaged into a confident figure |
| **Total** | **₹26,000 – 46,000** | **The top of this band is ₹11,000 above Marigold's ceiling** |

**Marigold is hearing this during solutioning, which is what Dev asked for, and it is his decision rather than ours to make quietly.** The levers, priced so the trade is arithmetic:

- **How often we read the store (D-3)** is the largest one, and it trades directly against the blind window in §6, row N-2 — a longer interval costs money and buys uncertainty in the November number.
- **The digest channel (D-2)**, where email in place of the messaging provider removes most of the messaging line and changes what the 08:00 message looks like.
- **The third environment**, which we will not propose removing: production is the thing four real people use from 25 September, and pricing it out is how v0.9 came to have no production at all.

The band's top being above the ceiling is recorded as **Dev's risk**, with the levers priced by us. We check it against real figures on **21 August**, once Setup has provisioned something and D-2 and D-3 are closed, and the check is reported at that week's demo whichever way it comes out.

### 11.4 After go-live — priced, so it exists as a decision

Nobody discussed this before the meeting. It is priced here because unpriced support does not exist, and if Marigold does not buy it then **8 October is a handover** and we will say that on the day.

| Option | What it is | Price |
|---|---|---|
| **A — Freeze-window cover, 8 Oct – 5 Dec** | A named person reachable in working hours, four-hour response inside the window; a defect fix prepared and taken to Dev for sign-off per fix, per §6 row N-6, on the fix path below; alarms routed to a channel devx watches, so a failure is something Marigold is told about rather than finds | **₹1.6 lakh for the window** |
| **B — A plus out-of-hours** | As A, plus one named person and one named backup reachable outside working hours through the window, with a written note per alarm saying what to do about it | **₹2.9 lakh for the window** |
| **C — Ongoing, Dec 2026 – Feb 2027** | Next-working-day response, defect fixes inside the phase-2 rhythm, and the depth question re-asked at the end of it | **₹55,000 a month** |
| **D — Nothing** | 8 October is a handover. Marigold holds the repository, the accounts and the documents. Nobody is watching the alarms, and no fix path exists — the paragraphs below describe something Marigold has not bought | **₹0**, and said out loud on the day |

There is no unbounded option. An open-ended support window either never ends or ends without anyone noticing.

**What a fix actually is, at 23:00 on 23 November.** v0.9 sold this window while §5.1 correctly forbids the access it needs, and never described the path between the two. Under A or B:

- **Production logs and rows are read through the tool, never read into a session.** The error tracker and the log search are how a person finds out what happened. Pasting a production task row into an agent session is the one route by which a sentence Priya typed reaches a model prompt, per §10.4, and it is the thing the instruction there forbids.
- **No agent session runs remediation against production. Ever, at any hour.** No session holds a production credential, so this is an absence rather than a rule (§5.1). Where a fix genuinely needs a production action a pipeline cannot take, that is a break-glass with **Dev's name on it**: he authorises it, a named devx person performs it, and it is written up the next working day.
- **A fix is a pull request through the same five checks, promoted rather than patched.** Spec ancestry, size, gate-change, verify, review — the same gates as a feature, because a hotfix is when they matter most. The deploy runs from the pipeline against the production environment named in §5.4; nothing is patched on a running environment, since such a patch exists in no commit and survives no redeploy.
- **Who reads the diff when the second reviewer is asleep. The answer is that it waits until the morning.** That is what a four-hour response inside working hours buys and what out-of-hours cover in B does not change: B buys someone who diagnoses, communicates and prepares, not someone who merges alone at 02:00. The only exception is Dev's break-glass above, and it is reviewed the next working day rather than retrospectively approved.
- **Every AI-assisted fix is reconstructable afterwards**: the spec commit, the diff, the review dispositions and the promotion record. That is what makes a post-incident conversation about the fix possible rather than a conversation about who remembers what.

**The data-handling note in §10.2 covers incidents, not only uploads**, and it is written that way because a support window is exactly where a policy about reading and transmitting gets tested at the worst hour.

### 11.5 Invoicing and the things Dev will not accept

- **Every hour invoiced maps to a ticket on a board Marigold can see.** No "QA phase" with no artefact behind it — that line item is the reason this bullet exists. **One honest qualification, because §5.2's last row says so:** ticket status is derived from what happened where the integration exists, and until it does the tech lead records it by hand. That is an exception to something our own process says never bends, it is named as an **exception** in §5.2 in that word, and **Karan Iyer** carries it. A hand-maintained board is weaker evidence than a derived one, and Marigold should read the invoice against the repository — the commits, the runs and the release documents — rather than against the board alone.
- **A weekly demo of working software, Wednesdays 09:30 IST, recorded.** Not a status deck, not a percentage complete. If a demo is skipped, the invoice for that week is Marigold's to question.
- **Named people, and no silent substitution.** §13.4 names them, with the hours that are funded. If anyone changes, Marigold is told **before** they notice it from the commits.
- **Marigold owns everything from the first commit** — repository, hosting, every third-party account, in Marigold's name, on Marigold's card, with Dev as owner. Not ours with him added.
- **No percentage of defect reduction, velocity, or improvement of any kind appears anywhere in this document, and none will appear in any document we hand over.** If Marigold finds one, it is a mistake, and we would like it sent back.

### 11.6 The commercial half v0.9 left out

Absent from v0.9 entirely rather than merely uncertain: when money is paid, what happens if either side stops, who owns what and when, and which law reads the document. Each of these is cheap here and expensive in November.

| Milestone | What releases it | Share of the ₹11.6 lakh core |
|---|---|---|
| Signature | — | **20% — ₹2.32 lakh** |
| **Setup exit** | The four items in §5.3, each with its run link | **15% — ₹1.74 lakh** |
| **The 25 September set accepted** | The release document with a non-empty artefact against every criterion, its "what this does not verify" section written, and Marigold's acceptance per §7.3 | **30% — ₹3.48 lakh** |
| **Last merge, Friday 2 October** | The remaining phase-1 outcomes accepted the same way | **25% — ₹2.90 lakh** |
| **The 90-day review, 25 November 2026** | Held, with both sides' material in the room | **10% — ₹1.16 lakh, retained until then** |

- **Invoicing.** Monthly, on the first working day, against milestones reached in the month. Payable within 14 days. P1-13 and P1-14 are invoiced against their own acceptance once quoted on 28 August. §11.4, if bought, is invoiced at the start of its window.
- **The retention exists for one reason.** 10% held to the 90-day review means the meeting where this engagement is judged has both sides in it, which is the failure mode a review nobody scheduled produces: Dev holding six tests, devx holding satisfied criteria, and no conversation obliged to happen. It is booked on 25 November precisely because that date falls inside Dev's slow window and would otherwise not get booked.
- **Intellectual property.** Marigold owns the repository, the hosting and the accounts from the first commit (P1-11), and that is not the same thing as owning the copyright: **copyright in each deliverable assigns to Marigold on payment of the milestone containing it**, with a licence to use it in the meantime, so nothing is unusable while an invoice is outstanding. What we cannot assign is what we cannot demonstrate is ours to assign, which is §10.3 and D-6.
- **Confidentiality, both directions.** Marigold's material is not shown to another client, named in a case study, or used as an example without Dev's written agreement. Our own process documents, the perimeter files and the templates stay ours, licensed to Marigold for use in this repository.
- **Liability.** Capped at the fees paid under this SOW. The carve-outs that belong in a cap are for the two advisers to write; we are not drafting them here and we are not giving a legal opinion on them.
- **Termination, both ways, 14 days in writing.** Work completed and accepted is payable, in-flight tickets to the last merge are payable, and nothing else is. **Two working days of wind-down are free**: credentials handed back, documents and the open-questions list handed over, the repository left in a state a next agency can read. There is no exit fee and no notice period inside the freeze — if Marigold wants us gone on 20 November, the wind-down still happens.
- **Governing law.** devx is in India and Marigold sells into the UK, so this needs deciding rather than assuming. Our position is Indian law and the courts of Mumbai unless Marigold's adviser proposes otherwise before signature. Not a technical decision and not ours to settle.
- **Controller and processor.** devx processes staff personal data, and via free text may process customer personal data. That needs an agreement and not an inventory — §10.4 is an inventory. It is **D-15**, it is C-12 in §8.2, and it is in force before the C-1 token is used, which is the same precondition S-1 sits behind in §10.6.

---
## 12. Changing this mid-phase

Clients change their minds, and a process that treats that as a failure gets routed around. The path below is designed to be used, not to discourage use.

**One rule sits above the rest: a change that alters what Marigold accepts goes through the delivery lead and lands in the acceptance criteria before any code moves.** A criterion changed to match what got built is not a criterion.

| Step | What happens |
|---|---|
| **1. Say it** | To Anjali Sharma, at the Wednesday demo or in writing. No form. Nothing is refused for arriving informally |
| **2. We write it down and price it, within two working days** | What it changes, what comes out to make room if the date is fixed, what it costs **or what it takes off the fee**, and which acceptance criteria change. One page |
| **3. Marigold decides, at the right level** | Behaviour: Priya, or Farhan. Money over ₹1.5 lakh: Dev plus Anjali Sen, two working days. Over ₹5 lakh: plus Ravi Menon, a week, not compressible. Anything touching customer data or store access: Dev alone |
| **4. It becomes real in the repository** | The criteria change on their protected path, approved by a named person and not by an agent. The design document changes. Both are commits Marigold can read |
| **5. It appears in the release document** | Including in the "what this does not verify" section, if the change moved something out of what we check |

**A reduction in scope is a reduction in price, and here is the table rather than the goodwill.** v0.9 had no mechanism converting one into the other, which meant the widest line in its own estimate could move out of phase 1 at no benefit to Marigold.

| What comes out | What comes off the fee |
|---|---|
| **The UK half of the late-order signal**, if D-1 is unanswered on 14 August and the signal covers India-warehouse orders only | **−₹0.9 lakh** off the firm core. The UK work is then priced into phase 2's re-quote rather than arriving there free |
| **P1-13 and P1-14 dropped** after the 28 August quote, whether because the quote exceeds the cap or because Marigold prefers to keep typing floors in one place | **The whole cap. ₹0 charged**, and named in §11.1 as a free drop |
| **P1-12 moves off the messaging provider to email** because C-14 to C-17 do not land in time | **−₹0.35 lakh**, and the messaging line in §11.3 falls with it |
| **P1-16's reopen screen deferred to phase 2** | **−₹0.6 lakh.** The data behind it is still captured from the first day of P1-7, so deferring the screen does not cost the history |

Anything not in that table is priced on the path above within two working days, in both directions. **A scope reduction never leaves the fee unchanged**, and if we cannot find a reduction we say so in writing with the reason rather than letting the number stand by default.

**Three limits on the path:**

- **Money raised late gets a no on principle.** If a change with a money consequence was foreseeable in week two and arrives in week five, it gets a no even where a yes was available in week two. This is Dev's rule and we are adopting it, because the alternative is us absorbing his approval latency silently and then missing a date.
- **After Friday 2 October (last merge) and through 5 December, no change is a feature change.** A defect fix inside that window needs Dev's sign-off per fix and follows the path in §11.4. Anything else is January.
- **A change cannot buy back time by removing Setup.** If a date is at risk, features come out — **in the ranked order written down in §2.3, now, rather than "named at the time"**, because the sentence that defers the ordering is the sentence that becomes an argument in the third week of September. The perimeter stays. Every standard added later leaves everything written before it unchecked, and that debt appears in no diff and on no invoice.

---
## 13. Signatures

A signature on a document nobody can be held to is decoration. Each line below says what that person is answerable for.

### 13.1 For Marigold Living

**Dev Rawat, founder**

Signing for: the scope in §2 and §3 being the thing Marigold wants, including every declined item and its reason, and the ranked drop order in §2.3; the depth level in §4 and the price of the level above; the fee shape in §11.1 — a firm core, a capped quote on 28 August, an indicative phase 2 that this document does not approve, and **no total** — together with the payment schedule and the terms in §11.6; **that the running-cost band in §11.3 has a top above the ₹35,000 ceiling, and that the levers are his to pull**; the after-go-live option chosen in §11.4, including that Option D means no fix path exists; the acceptance path in §7.3, including deemed acceptance; the dependencies and dates in §8.2, and that a slip in them moves our dates as described in §9.3; **written acceptance of Annexe A's named model provider, its retention terms and its processing region — Annexe B**; that S-1 handles Marigold's customer personal data under §10.6, before the board exists and after the note in D-5 and the agreement in C-12 are in force; the provenance decision in D-11 and that it is effectively permanent either way; and that the staff data in §10.4 is held with the purpose stated and that the people it is about are told.

And signing to have been told, rather than to agree: that Shopify's number may not match the shelf and the stock signal fires off it anyway; that phase 1 cannot move the late-order percentage and P1-18 was priced and not bought; that Priya is the single confirm-and-reopen point with D-4 unresolved; that the sheet and the Monday export both survive; that the board is English only; and that nobody is contracted to teach the two temps. Each of those is recorded with **his** name on it, in the section it belongs to.

Signature: ________________  Date: ____________

*Anjali Sen (co-founder) and Ravi Menon (accountant) are on the approval path for the fee per §9.2. The ₹18–26 lakh envelope was approved in writing on 5 August — Annexe C — so what is signed here is a number inside it. Their approval is not a signature on this document.*

### 13.2 For devx labs — delivery

**Anjali Sharma, delivery lead**

Signing for: that this document says what was actually agreed in the meeting of 6 August 2026, including the parts Marigold did not want to hear; the dated schedule in §8.4 and the drop order in §2.3; the fee shape in §11.1 and the reasoning in §11.2, including that a band narrower than the uncertainty it names is not something I will put in front of Marigold's accountant; the commercial terms in §11.6; the working agreement in §9; that a change follows §12 and never arrives as a quietly edited criterion, and that a scope reduction comes off the fee; that Marigold is told before a named person changes rather than after; and that if the after-go-live option is D, I say out loud on 8 October that this is a handover.

And signing for the two terms in this document that are **mine** rather than the meeting's, both disclosed where they appear rather than in a covering note: **the rework allowance** in §11.1, which was never discussed on 6 August and which Marigold may strike; and **deemed acceptance after three working days** in §7.3, which can accept a release by silence in Diwali week and is mitigated only by Priya's single extension.

Signature: ________________  Date: ____________

### 13.3 For devx labs — technical

**Karan Iyer, tech lead**

I returned v0.9 unsigned. **The conditions I returned it for are in this document rather than in a covering note, which is the only form in which they are worth anything** — a condition in a covering note is a condition nobody reads in November.

Signing for: **every technical claim in this document being one I can stand behind, and every gap being named rather than smoothed.** Specifically —

- the depth level in §4, the personal-data limb of our own High test being **met** and the deviation named as a deviation with **my** name accepting it, and the two triggers that reopen it: any write to the store, and any ingestion of customer data;
- the status of every row in §5.2, including that **no row says *proven*** and why, that the middle column states today's truth with a date rather than "at Setup", and that High's second-approver mechanism is *to build* until Setup exit 4 has demanded and satisfied a code-owner review on a protected path;
- the list in §6 of what we will not verify, and that it goes into every release document;
- that the criteria in §7 each name an artefact, that a prose artefact fails the release, and that authentication, the scheduled reader's four silent failures and the phase-2 receiver's authenticity are criteria and not monitoring wishes;
- **the three different strengths in §10.4** — logs a mechanism with a test, error reports the same mechanism with a criterion this version added, and keeping the task table out of a model prompt an **instruction to four named people and not a mechanism**, closed by D-5. I will not sign a sentence that describes a habit as a control, and v0.9 contained one;
- the honest position in §10.2 that our read-and-transmit policy is half written, and the engagement data-handling note that closes it, drafted 7 August and signed before the store access is used;
- **§10.6** — that S-1 handles Marigold's customer personal data, that I do it by hand with no agent session attached, that the extract lives outside every agent-readable path with a recorded deletion date, and that hand-synthesised fixtures are a named **exception** to our own fixture rule which **I** carry;
- the other exception in this document, also in that word: **ticket status is hand-maintained** until the integration exists, which our own process says never bends, and **I** carry that too;
- the statement in §10.3 that **I cannot demonstrate the originality of agent-written code and will not sign a warranty saying I can**, in any form, however it is worded, and that no description of our review, our diff sizes or our dependency scanning is to be presented as originality;
- and that **no percentage improvement, no "proven" and no "guaranteed" appears in this document or in anything we hand Marigold.**

Two things this signature is conditional on, and they are conditions rather than preferences. **Deepa Kulkarni's six hours a week are funded inside §11.1 and named in §13.4** — without them I am the single point of failure on every protected merge while also owning the design document, the data-handling note and four measurements. And **D-2 and D-3 ship with their fallbacks in force**, as §11.2 and §11.3 state, rather than as a promise that they are closed.

If I cannot stand behind a sentence here, it changes before this document is issued. That is what this signature is for.

Signature: ________________  Date: ____________

### 13.4 The named people

| Who | Role | Signs for |
|---|---|---|
| **Anjali Sharma** | Delivery lead | This document, the commercial frame, the working agreement. The rework allowance and deemed acceptance are her terms |
| **Karan Iyer** | Tech lead | Every technical claim, the design document, the perimeter, the engagement data-handling note, and the S-1 measurement in §10.6. Code owner on the protected paths |
| **Nikhil Barve** | Senior engineer, phases 1 and 2 | — |
| **Sneha Raut** | Engineer, phase 1 | — |
| **Imran Shaikh** | QA | The acceptance artefacts and the release document, including its third column and its "what this does not verify" section |
| **Deepa Kulkarni** | Engineer from outside this project, **six hours a week funded inside §11.1** | Second code owner on the protected paths, so a fortnight's leave cannot stall a merge. She and Karan are the two owner entries that deliver a second reviewer where §5 calls for one |

If any of these people changes, Marigold is told before it shows up in the commit history.

---
## 14. The 90-day review — **Wednesday 25 November 2026, 14:00 IST, 90 minutes**

The meeting at which this engagement is judged existed in no signed document until now. Marigold's BRD is built around six tests taken at 90 days; the meeting was agreed in the room and then appeared nowhere. Without it, in late November Dev holds six tests, devx holds a stack of satisfied criteria, nobody scheduled the conversation, and the freeze plus Dev's own three-to-four-day latency window is running. That is how a phase ends with an angry client while every criterion passed.

**Attendees:** Dev Rawat, Priya Menon, Farhan Qureshi · Anjali Sharma, Karan Iyer, Imran Shaikh. Booked in Dev's diary at signature; it is inside his slow window on purpose, which is why it is booked now.

**What Marigold brings:** their own reading of the six tests in BRD §5 — including test 2a, test 3's roll-call judgement, which is Priya's alone to make, test 5 and test 6, all three of which devx does not verify (N-9).

**What devx brings:**

1. Every phase-1 criterion with its artefact, and the "does not verify" section of every release document.
2. **The reading ledger extract with its error bar** — the interval actually used, the number of cycles, and the cycles that were missed — so test 1's comparison has the two sides X-9 promised, and its dependence on the reader is stated rather than glossed.
3. **The alarm history**: every time A-21 to A-24, A-35 and A-36 fired, and what happened next.
4. The read budget against actual reads through the window.
5. **The defect log, split by who found each defect** — us, Marigold, or an alarm.
6. **The review agent's dismissal rate**, reported here rather than at a quarter, because it holds a required-check slot while its value is unmeasured (§15, risk 2).
7. The honest sentence in N-12, restated: what phase 1 could and could not move on test 2, and what it would take.

**Consequences, so it is a decision meeting and not a debrief:**

- A signed one-page record of the six tests' readings, both sides' names on it.
- **It is the input to phase 2's scope and its re-quote.** Phase 2 is not quoted before this meeting.
- **The 10% retention on phase 1 is released on it** (§11.6).
- **A test not met produces either a change request or a written "we are not doing this".** Nothing carries forward silently.
- Option C is decided here.
- The depth question is re-asked for phase 2 here, alongside §2.2's requirement.

---
## 15. Risks accepted rather than fixed — with a name against each

Not every finding gets fixed. These were argued and left, and each one has an owner so that if it goes wrong it was somebody's call rather than an accident.

**Carried by Karan Iyer, tech lead:**

1. **Standard depth on a system holding staff personal data**, including performance data about a named employee, against our own table that routes personal data to High. Accepted on the compensating controls in §4.3, with two named triggers that reopen it: any write to the Shopify store, and any ingestion of customer data into the board.
2. **The review agent keeps a required-check slot while its value is unmeasured.** We do not know its dismissal rate or whether it finds what a person would want found. It stays required, because a review job that quietly does nothing is worse, and the dismissal rate is reported at the 90-day review rather than at a quarter.
3. **N-7 stands as a partial answer.** Test and code can share a misunderstanding; hand-computed expected values are applied only on the parts that matter. A known hole in the middle of our own value proposition, signed knowingly.
4. **No load test before Diwali, and no production restore drill** (X-11). Compensated by the read budget with an alarm (A-35) and one timed dev restore (A-34). Both are purchasable.
5. **The second-owner mechanism is unproven until Setup proves it.** §5.3's fourth exit is the only thing standing between "protected path" and decoration, and until 21 August it is a belief.
6. **The pilot counts stay in a client document.** "8 times out of 8" and "0 times out of 7" are fifteen requirements in one session, correctly qualified in §4.2, and they will still be quoted back out of context. Better that than removing the only evidence we have.
7. **The hand-maintained ticket status** (§5.2, last row) is an exception to something our process says never bends, and §11.5's invoicing rests on it.

**Carried by Anjali Sharma, delivery lead:**

8. **Deemed acceptance after three working days** (§7.3) sits inside Dev's own slow window from 12 October. Mitigated by Priya's one extension. If a release is accepted by silence during Diwali, that term is mine.
9. **The rework allowance is a term Marigold never discussed**, disclosed in §11.1 with an invitation to strike it.

**Carried by Dev Rawat, founder — accepted by Marigold with the consequence written down:**

10. **Shopify's stock number may not match the shelf**, and the whole low-stock signal fires off it (N-11, X-21). Reconciliation is out of scope by his choice.
11. **Phase 1 cannot move the late-order percentage** (N-12), and P1-18 — the one thing that could, before December — is not bought.
12. **Priya is the single confirm-and-reopen point** until D-4 closes, and during Diwali her button is the board's throughput limit. A-28's ageing flag is a mitigation, not a fix.
13. **The sheet and the Monday export both survive** (N-13). P1-14 keeps a mirror tab alive and X-18 keeps Tarun's export running, so for at least one phase Marigold operates two systems that can disagree. Retiring either is a decision he has not made, and nothing in this engagement forces it.
13. **The Google Sheet stays alive**, with Tarun's Monday export (X-18) and a mirror tab (P1-14), which works against Marigold's own success test 6 (N-13).
14. **Per-person reopen statistics are performance monitoring of a named employee**, held with Priya's stated purpose and Tarun's knowledge, pending D-10.
15. **Provenance trailers in Marigold's own repository are effectively permanent either way** (D-11), and interact with the originality clause (D-6, §10.3).
16. **English only in phase 1** (X-20, D-13), for a warehouse hand in Bhiwandi.
17. **Two temps use this in the busiest eight weeks of the year with nobody contracted to teach them** (X-21).
18. **The running-cost ceiling binds** (§11.3): the top of the band is ₹46,000 against a ₹35,000 ceiling, and the lever is the read interval, which trades against the blind window in N-2.

---

### Version history

| Version | Date | What changed |
|---|---|---|
| 0.9 DRAFT | 6 August 2026 | First draft from BRD v1.1 and the frozen discovery notes. **Returned unsigned by the tech lead** on four blocking grounds, plus fourteen required changes, and read adversarially in parallel |
| **1.0** | **6 August 2026** | **Issued and signed.** Every required change applied; the accompanying changelog says which review demanded what. New in this version: authentication as an outcome with criteria (P1-0, A-18, A-19); a named production environment with a promotion criterion (P1-17, §5.4, A-37); four scheduled-reader alarm criteria (A-21 to A-24); the S-1 dataset governed before store access, with D-5 and C-12 moved ahead of C-1 (§10.6); the depth deviation recorded with its owner (§4.3); the dated schedule (§8.4); the drop order (§2.3); the 90-day review as a booked meeting with consequences (§14); Marigold's acceptance of every release (§7.3); the commercial and legal half (§12, §11.6); a firm price with the unopened work quoted later under a cap (§11.1); a running-cost band that admits it crosses the ceiling (§11.3); the phase-2 receiver's authenticity criteria (A-45 to A-47); and eighteen risks accepted with a name against each (§15). **Open at issue, with stated fallbacks rather than promises: D-2 (11 Aug), D-3, D-12, D-1, D-4 (14 Aug), D-6, D-8, D-10, D-11 (21 Aug), and the P1-13/P1-14 quote (28 Aug).** |

Where this document and the discovery meeting notes of 6 August 2026 disagree, **this document is the authority** — including on anything said in the recording that was later changed. Where this document and Marigold's amended BRD v1.1 disagree on what Marigold wants, **Marigold's document is the authority and we bring the difference to Dev rather than resolving it in an assumptions list.** That second sentence is new, and it is there because the draft resolved one of Priya's own open questions in our favour inside Assumption 3.

**FICTIONAL — see the notice at the top of this document.**
<<<END SOW>>>

---

### Version history

| Version | Date | What changed |
|---|---|---|
| **0.9 DRAFT** | 6 August 2026 | First draft from BRD v1.1 and the frozen discovery notes of the same day. **Not issued. Returned unsigned by Karan Iyer** on four blocking grounds: a data-protection sentence in §10.4 that §10.2 said was untrue; a work sequence that handled Marigold's customer personal data before the note governing it existed; authentication and the phase-2 receiver in scope with no criteria; and no criterion for the scheduled reader failing silently. It also failed this document's own completeness test, because Annexe A carried a placeholder and the written permission was outstanding |
| **1.0** | 11 August 2026 | Issued to Marigold with Karan's signature and **Annexe A** (provider, retention, region), **Annexe B** (Dev's written permission, dated and timed) and **Annexe C** (the 5 August envelope approval) attached. The four blocking changes closed, the fifteen further changes in the tech lead's review applied, and the adversarial review's findings taken on — production named, authentication an outcome with criteria, the 90-day review in the document, Marigold accepting releases, the commercial half written, the fee shape rebuilt and the total row removed. **Open at this version, deliberately and with fallbacks in force rather than promises:** D-1 (due 14 August, its consequence signed as a scope note and priced in §12); D-2 and D-3 (due 11 August, both shipping with the fallback named in §11.2 and §11.3); D-4, D-6, D-10, D-11 and D-15 with their owners and dates; the after-go-live option in §11.4 undecided; P1-13 and P1-14 unquoted until 28 August under a cap; and P1-18 priced and not bought |

Where this document and the discovery meeting notes of 6 August 2026 disagree, **this document is the authority** — including on anything said in the recording that was later changed.

**FICTIONAL — see the notice at the top of this document.**
