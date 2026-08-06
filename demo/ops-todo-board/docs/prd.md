> **FICTIONAL DOCUMENT — CREATED FOR A DEMONSTRATION.** Marigold Living does not exist. Dev Rawat, Priya
> Menon, Anjali Sharma and Karan Iyer are invented, as is every date, order number and rupee figure. devx
> labs' process is real; this client and this engagement are not.

# Product Requirements Document — Ops To-Do Board, Phase 1

| | |
|---|---|
| **Version** | 1.0 |
| **Date** | 7 August 2026 |
| **Owner** | Anjali Sharma, delivery lead, devx labs |
| **Covers** | **Phase 1 only.** Phase 2 is December 2026 – January 2027 and is not approved by the SOW, so it appears in this document only in §5 |
| **Status** | **Frozen at issue.** Changes go through Anjali Sharma under sow-terms §12, because they change what Marigold accepts |
| **Written against** | SOW v1.0 and its annexes, as they stand for issue on 11 August 2026 |

## How to read this

This document says **what** phase 1 is and **why**, for the people who will use it. It is not the acceptance
criteria: **Annexe A holds all 39 of those and owns them**, and every requirement below points at the ones
that prove it rather than restating them. Where the two ever appear to disagree, Annexe A governs the test
and this document is wrong.

It is also not the SOW. The SOW is the commercial frame. **Nothing below promises more than the SOW sold**;
where drafting this document found a place where it would have, that place is in §6 as an open question with
an owner and a date, not in §4 as a requirement.

**Every requirement cites its source** — a BRD section, a SOW section, an annexe row, a numbered decision
from the discovery note of 6 August 2026, or a numbered decision from the frozen PRD-scoping note of
7 August 2026, cited as *PRD-scoping decision N* so it cannot be confused with a discovery decision. A
requirement with no source would be devx's assumption wearing Marigold's authority, so anything wanted but
unsourced is in §6 instead.

**Five pre-issue corrections in §6 (Q14 to Q18)** are defects in the SOW's own arithmetic and
cross-references. If any of them is resolved differently from how this document reads them, **this document
changes with the SOW** and Anjali Sharma reissues it.

---

## 1. What this phase is

Marigold's operations team of four works out of a WhatsApp group with about fourteen thousand messages in it,
a Google Sheet that is out of date by Thursday because it comes from a Monday export, and a paper list Priya
rebuilds from memory on Tuesdays. Work reaches that team by somebody noticing.

**Phase 1 is one shared to-do list those people see the same version of, on a phone as well as a laptop.** A
person adds a task in their own words. Priya puts exactly one name on it. That person completes it, and the
completion is a record of who and when, so Priya can put it back if it was not really done. On top of that
list, two signals from the Shopify store put work on it without anyone going to look: a product dropping
below a stock floor Marigold sets, and an order passing the dispatch promise Marigold has published. The
board reads from Shopify and never writes to it — it tells a human what to do, and the human does it in
Shopify under their own login.

**The date is conditional and the conditions belong in this paragraph rather than nine sections later.** It
is usable by four real people on real orders by **Friday 25 September 2026 — on two conditions, in
sow-terms §1's own words: read-only store access in Marigold's hands to devx's on 11 August (C-1), and this
SOW signed by 20 August. Every working day either is late is a working day off the eighteen available.**
§9.3 calls C-1 the most expensive single dependency in the document and prices a late answer **day for
day**. The date holds if the decisions in §9 of the terms are answered inside their stated windows — which
includes the twenty-seven open questions in §6 below, each with an owner and the window it has to be
answered in. One of those decisions has its consequence already agreed rather than argued in October: if
the fulfilment-clock question **D-1** is unanswered by **Friday 14 August**, the late-order signal covers
India-warehouse orders only in phase 1, the UK half moves to phase 2 and is priced into phase 2's re-quote,
₹0.9 lakh comes off the firm core, no date slips, and Dev signs it as a scope note on the day it fires.

**Three items follow by Friday 2 October**, which is what the signature document promises and the signature
document governs where it and the terms differ. **Two more — the sheet import and the mirror tab, R30 and
R31 below — are not quoted until 28 August and are capped at ₹2.2 lakh, and if the quote lands above the
cap Marigold drops the pair at no charge.** §2.1 lists five deferred rows against sow.md's three; that
disagreement is Q16 and it is corrected before the SOW issues, and whether the capped pair is already
inside the firm price is Q15. Marigold owns the repository, the hosting and every third-party account from
the first commit.

**Two things this phase is not, said here rather than in November.** It does not reconcile Shopify's stock
number with what is on the shelf, and the whole stock signal fires off that number. And it does not reduce
the count of late orders, because it fires after an order has already breached — it makes that number exist
and makes it trustworthy. Both are disclosed in sow-terms §6, rows N-11 and N-12, and both are recorded as
Dev Rawat's accepted risks in §15.

*Source: sow-terms §1, §2.1, §6 (N-3, N-11, N-12), §9.3, §11.1, §12, §15 risks 10 and 11; brd §2, §3, §4,
§6; sow.md "What we are building" and its reading path; annexe-d C-1, D-1; PRD-scoping decision 22.*

---

## 2. Who uses it, and what each of them does on a normal day

Seven people by mid-November, not four. That is Assumption 2 in Annexe D and decision 2 in the discovery
note, and it is the number the permission model is built for.

| Who | Their day, and what the board has to survive |
|---|---|
| **Priya Menon**, operations manager | Arrives around 9, sometimes 9:30 when her daughter's school bus is late. Opens Shopify orders, then the Stock Watch sheet, then WhatsApp. Makes a paper list between 10 and 11. Around 4pm eyeballs the orders list for what has not gone out. She is the only person who assigns and the only person who reopens, she accepts every release under sow-terms §7.3, and she is the decision-maker on how the board behaves. She asks "did you do that?" about twenty times a day and hates the sound of it |
| **Tarun**, packing and vendor calls | Stock tasks and the reorder calls land on him. He ticks things off before they are done — in his head "I will call them this evening" is done. Three of the four stockouts this year were marked handled. He runs the Monday export that fills the sheet, and nothing in this engagement retires it — Priya has said she will retire it once the floors import and the mirror tab exist, which are R30 and R31 and are not quoted until 28 August, so it survives this phase and Q11 carries the rest |
| **Rakesh**, warehouse floor | Starts at 07:00. No laptop, ever. An old, cheap phone on patchy signal at the Bhiwandi unit. He is the person for whom the board either works or does not exist, and he is the reason the device and network profile is written down before anything is built |
| **Anjali (care)**, customer support | Works UK evenings, because most UK customers write in Marigold's evening. She is how Marigold currently finds out an order is late — the customer tells her and she tells Priya. A digest sent at 08:00 IST reaches her at 02:30, which is why messages are held to her own morning |
| **Farhan Qureshi**, ops lead | Joins from September as Priya's named backup for behaviour decisions only. He has not been asked yet — that is D-4, due 21 August — and he will not have used the board |
| **Two named temp accounts** | November only, for the busiest eight weeks of Marigold's year. Individual accounts, same permissions, access ending the day they leave. Nobody is contracted to teach them |

**One thing about this table is unresolved and it is cheap now.** BRD §1 has Dev describing **two** people on
customer support and Priya describing **one**. Assumption 2 assumes one, and the accounts in C-9, every
role-to-action test in A-11 and the staff inventory in sow-terms §10.4 all sit on that. It is Q1 in §6.

*Source: brd §1, §2, §6a, §10; annexe-d Assumption 2, C-4, C-9, D-4, D-8; sow-terms §9.1, §7.3; discovery
decisions 1, 2, 3.*

---

## 3. How to read the requirements

Each row states **what** must be true, **why** it matters to one of the seven people above, **its source**,
and **which P1-\* outcome from sow-terms §2.1 it serves.** They are grouped by the user's job, not by
architecture. Where a requirement's outcome is one of the two pieces of work in sow-terms §2.0, it says S-1
or S-2 instead.

**What proves each one is in Annexe A and only in Annexe A.** The criterion numbers below are pointers, not
copies. A row states the outcome and the reason in this document's words; every threshold, list, field
enumeration and artefact stays in the annexe. That is deliberate: Annexe A sits on a protected path where only
a named person approves a change to a criterion, it already carries a named list of the four criteria narrowed
between v0.9 and v1.0, and §12 is the path for the next one. A second copy of a criterion in this document
goes wrong the first time the first copy is amended, and nobody would know which one a release was accepted
against.

**Every claim devx makes about its own checks is graded, and none of them is described as proven.** This is
sow.md's fourth thing to know before signing and it is not softer here: "Our process has been tested but has
never run end to end on a live repository, so **no check in this document is described as proven.** Each is
*written* — its logic tested against deliberately broken cases — or *to build*. Annexe B has every row and
its status. Anything sold to Marigold as stronger than that is an error we would want reported back." That
applies to every gate, alarm, protected path and approval named below. Where a requirement leans on a
mechanism that is *to build* or untried, the row says so in the row — R35 is the one where it matters most.
PRD-scoping decision 28 makes this the standing rule for every meeting and every release document in this
engagement, after the tech lead corrected the delivery lead on it in front of the client.

*Source: sow.md "Four things to know before signing" item 4; sow-terms §5.2, §5.3, §7.3, §13.3; annexe-b
(every row and its status); PRD-scoping decision 28.*

---

## 4. Requirements

### 4.1 Nobody who is not a user sees anything

| # | What must be true | Why | Source | Serves |
|---|---|---|---|---|
| **R1** | Every route the board serves refuses a request carrying no valid session, and the refusal leaks nothing a reader could use — **A-18 enumerates what "nothing" excludes**, and it enumerates the routes from the router rather than from a list somebody maintains | The board is reachable on the public internet and holds seven people's names, a record of what each of them did, and Marigold's order numbers. "Internal" describes who it is for, not who can reach it | sow-terms §2.1 P1-0, §4.1, §5.1; annexe-a A-18 | **P1-0** |
| **R2** | A person signs in as themselves; a session ends after a stated idle period and a stated absolute period, both written down with the reason for the number; and deactivating an account ends that account's live session | Two temps get accounts for a nine-day window in the busiest weeks of the year. An account that keeps working after the person has gone is the whole of the risk, and C-9 names the person who deactivates it | sow-terms §2.1 P1-0; annexe-a A-19; annexe-d C-9; discovery decision 3 | **P1-0** |
| **R3** | Who may do what: everyone with a session sees every task; the assignee or Priya completes; only Priya or her named backup assigns or reopens; a temp account has exactly the same shape as a permanent one | Everyone seeing everything is a decision, not an accident — it is Assumption 7, and it is what makes the board one list rather than four. The confirm-and-reopen limit is Priya's authority, which is how she knows what is going on. Whether the free-text body of a task is visible to all seven accounts is not settled and is Dev's — **Q13** | sow-terms §2.1 P1-0 and P1-5, Assumption 7; annexe-a A-11; discovery decision 3 | **P1-0**, **P1-5**, **P1-7** |

### 4.2 Priya's nine o'clock: one list, and putting things on it

| # | What must be true | Why | Source | Serves |
|---|---|---|---|---|
| **R4** | One board, one version of it, every user seeing every task, with unassigned tasks at the top so they cannot be quietly ignored | Priya's Manchester order sat six days because a message scrolled up and each of them thought the other had it. A list only stops that if it is one list | sow-terms §2.1 P1-1; brd §3, §6; discovery decision 4 | **P1-1** |
| **R5** | Rakesh can see the board, complete a task assigned to him, and add a task, at a device and network profile written down in the design document — **A-7's three actions at A-27's profile, which is narrower than "the board works" and deliberately so**; A-7 was cut back from a claim about a full day's work that no artefact demonstrates | Rakesh has no laptop and never will. This is the hardest platform requirement in the engagement and nobody has looked at the actual phone yet, which is why the profile is a written artefact and real-handset evidence is taken by 15 September, three weeks before last merge. **The 15 September evidence is substitutable, not certain: A-7's named fallback is the closest device buyable against D-8's answer, the substitution written into the release document, and the handset screenshot taken in the pre-window fortnight as a check rather than as the criterion** | sow-terms §2.1 P1-1, §9.3 (D-8); annexe-a A-7, A-27; annexe-d C-4, D-8; brd §6, §10 | **P1-1** |
| **R6** | A person can put their own work on the board, in their own words, from the board itself — **A-29 carries the action and requires it of the screen rather than of an endpoint** | Half of Priya's day is neither stock nor orders — it is "chase the courier about the damaged box in Pune". A board that only receives machine-raised work is not where her day lives. Whether adding a task and putting a name on it is one action from one screen on a phone is open — **Q12** | sow-terms §2.1 P1-4; annexe-a A-29; brd §6 | **P1-4** |
| **R7** | An unassigned task that has waited too long is visible as such on the board — **A-28 carries the age and what "flagged" means** | Priya is the only person who can confirm an assignment. The flag is what makes a backing-up queue visible. It is a mitigation and not a fix, and the SOW says so — see Q22 | annexe-a A-28; sow-terms §15 risk 12 | **no P1-\* row.** A-28 exists as a mitigation for §15 risk 12; P1-1 promises only that unassigned tasks sit at the top, which is R4 |
| **R8** | Priya can answer "what is unfinished right now and who has it" from one screen, without asking anyone, inside a minute — **timed once, with her doing it, per §2.1 P1-10**. **Displaceable: it is row 2 of §2.3's drop order and one of the two rows named in Q19 if P1-18 is bought** | It is Dev's fourth test and it is a number. A criterion that does not time it is a criterion about a screen existing. **Two cited documents disagree on how often it is timed: P1-10 says once and A-31's artefact column asks for the recording taken twice. The terms govern over an annexe, so the requirement above is once.** Reconciling the two before the SOW issues on 11 August is Anjali Sharma's; PRD-scoping decision 15 keeps A-31 as written and decision 16 moves the second recording out of 25 September to 8 October, and Priya has refused it inside that window — Q25 | sow-terms §2.1 P1-10, §2.3 (row 2); annexe-a A-31; brd §4.6, §5 test 4; PRD-scoping decisions 15 and 16 | **P1-10** |
| **R9** | A design brief accepted by Priya in writing before implementation tickets exist — **A-38 names what the brief has to cover, down to R5's profile** | There is no designer on this engagement and the SOW does not verify that the board is pleasant to use. Trello died here in nine days of being unpleasant. Changing a frame costs minutes; changing a built screen costs a ticket. **Her acceptance is of phone-width screens on an actual phone, twenty minutes, with Rakesh present for ten — or the release document states that her acceptance was of a document and not of a screen** | sow-terms §6 N-14; annexe-a A-38; brd §10 (Trello); PRD-scoping decision 17 | **P1-1** |
| **R10** | Something exists in the repository that a person who has never seen the board can be taught from — **A-39 names the two artefacts and what they have to cover** | Dev's fifth test is that one of his four can teach it to a new hire in fifteen minutes. devx does not verify that test and is not contracted to teach anyone — so the thing being taught has to exist in writing. Priya will do the teaching and has said she will not do it off the top of her head: the page and the walkthrough have to exist and she has to have read them before 8 October — that is the condition attached to the temps ask in **Q23** | annexe-c X-20; annexe-a A-39; sow-terms §11.1, §6 N-9; brd §5 test 5 | no P1-\* row; inside the firm core per §11.1 |

### 4.3 One name on every job, and telling that one person

| # | What must be true | Why | Source | Serves |
|---|---|---|---|---|
| **R11** | A rule proposes the name — stock to Tarun, packing to Rakesh, customer-facing to Anjali (care), money or vendors to Priya — and no task is assigned until Priya or her named backup confirms it. No task acquires a name any other way | This is the resolution of the first contradiction in BRD §11: the rule guesses, Priya agrees. She said the reason better than devx could — being the one who assigns is how she knows what is going on | sow-terms §2.1 P1-5; annexe-c X-7; brd §6, §11.1; discovery decision 4 | **P1-5** |
| **R12** | The assignee, and only the assignee, is messaged when a task lands on their name, and no automatic message goes to the Marigold Ops group on assignment — **A-5 carries the criterion and X-4 carries the decline** | This is the resolution of BRD §11's second contradiction. If every assignment reaches the group, Rakesh gets a message every time Priya assigns something to Tarun, on a bad signal, at the unit — and by Wednesday he mutes the group, which mutes the one message that was for him. That is how the shared calendar died | sow-terms §2.1 P1-8; annexe-a A-5; annexe-c X-4; brd §6, §11.2; discovery decision 8 | **P1-8** |
| **R13** | A message carries the task reference and the order number and never the free-text body of the task. Request logs and error reports are built from a field allowlist | Dev's first blocked item is that customer data does not go into this system. Nobody can stop Priya typing *the lady in Pune called twice, her number is* into a free-text box, so what is controlled is the exits — and the honest limit of that control is stated in sow-terms §10.4 | sow-terms §2.1 P1-8, §10.4, §6 N-10; annexe-a A-25; brd §12 block 1, §11.5 | **P1-8** |
| **R14** | No message is delivered into a recipient's night: one raised outside the declared waking window in that recipient's own local time is held and released in their own morning — **A-26 carries the hours, the release time and the clock-change case** | Anjali (care) works UK evenings. An assignment made at 08:30 IST reaches her at 03:00 otherwise, and the one person whose muted phone costs Marigold a customer is the one a notification design usually is not written for. **The window is one number for everybody and that is wrong for the two people who are awake outside it — a per-person window is Q9** | sow-terms §2.1 P1-8, P1-12; annexe-a A-26; brd §1 | **P1-8**, **P1-12** |
| **R15** | A message the provider rejected raises an alarm | The board is the record and a message is a convenience — devx cannot verify that a message was read or that it reached a handset at the unit. What it can verify is that a failure to send is noticed rather than silent | sow-terms §6 N-4; annexe-a A-36 | **P1-8**, **P1-12** |

### 4.4 Whether it was actually done

| # | What must be true | Why | Source | Serves |
|---|---|---|---|---|
| **R16** | Completion is a record and not a claim: who marked it done and when, Priya or her backup able to put it back, both events surviving — **A-6 carries the criterion** — and nothing deleted anywhere in the phase, which is X-5 | This is the Tarun problem, in Priya's own words: three of the four times Marigold ran out of something this year it was marked handled. She has had the conversation twice and has nothing to hold up | sow-terms §2.1 P1-7, Assumption 8; annexe-a A-6; annexe-c X-5; brd §6a; discovery decision 10 | **P1-7** |
| **R17** | A screen reporting reopens for a chosen week, by person — **A-17 carries the shape and the artefact**. The data behind it is captured from the first day completion exists | Priya wants the numbers, not an argument. Because the data is captured from day one, deferring the screen would not cost the history — which is also why deferring it is one of the four priced reductions in sow-terms §12 | sow-terms §2.1 P1-16, §12; annexe-a A-17; brd §6a | **P1-16** |
| **R18** | The board can be restored: a backup configuration with a stated recovery point, a restore path written as steps a person can follow without asking devx, and one timed restore actually performed in dev | The board is the sole record of the eight weeks Dev's verdict is taken over. The production restore *drill* is declined and the load test is not bought — that is X-11 — and this is what is not declined | annexe-a A-34; annexe-c X-11; sow-terms §11.1, §6 N-5 | **P1-7**, **P1-9** |

### 4.5 Low stock reaching Tarun without Priya going to look

| # | What must be true | Why | Source | Serves |
|---|---|---|---|---|
| **R19** | A product crossing below its floor produces exactly one open task, and the task carries the reading it came from — **A-1 states which fields and how the crossing is caused for the artefact** | This is the brass candle holders. Forty sold over a weekend, the sheet said thirty in stock, there were eleven, and nobody was looking at the sheet on a Saturday. The reading being on the task is what makes a wrong task traceable to a wrong reading instead of arguable | sow-terms §2.1 P1-2; annexe-a A-1; annexe-d C-13; brd §3, §4.1 | **P1-2** |
| **R20** | A product that stays below its floor across later readings does not produce a second task while the first is open — **A-2 carries the behaviour** | The behaviour is Priya's decision recorded in D-14, not a thing settled by whoever wrote the test, and A-2 says so itself. **See Q7** — she has refused to answer D-14 as posed, because neither one task nor two is what she needs, and a third option is on the table at Kickoff: the open task's reading updating, and something happening at zero. A-2's behaviour stands until she decides | sow-terms §2.1 P1-2; annexe-a A-2; annexe-d D-14; brd §15.3 | **P1-2** |
| **R21** | A stated maximum gap between the reading that saw the crossing and the task existing, with that number on the screen | Without a maximum, "a task appears by itself" is satisfied by a nightly poll and Priya's February happens again with better paperwork. The number is derived from the reading interval in D-3, whose fallback is in force at issue | sow-terms §2.1 P1-2; annexe-a A-20; annexe-d D-3 | **P1-2** |
| **R22** | Every product resolves to a floor without Priya typing one by hand for each: a category default, a per-product override, one screen where a sitting's worth can be changed at once, and new festive products inheriting their category default the day they are created — **A-8 and A-9 carry the counts** | The floors are in Priya's head and a few are in the margin of the sheet. She will sit down and do the ones that move — that is her afternoon in C-6, and it is on the critical path, because the board cannot raise a single stock task for a product with no floor. **The bulk screen is displaceable and it is the first row out: row 1 of §2.3's drop order, and one of the two rows named in Q19 if P1-18 is bought. Priya has conceded it is the right row to lose — category defaults plus a per-product override plus the sheet import by 2 October still leaves every product with a floor (PRD-scoping decision 9).** Whether a floor attaches to a product or a variant is open, and it decides how many numbers she types — **Q6** | sow-terms §2.1 P1-6, §2.3 (row 1); annexe-a A-8, A-9; annexe-d C-6; brd §6, §15.2; discovery decision 5; PRD-scoping decision 9 | **P1-6** |
| **R23** | An independent record of what the store said: every inventory reading, per product, timestamped, held apart from the board and appended to rather than edited — **A-10 carries the append-only criterion and the artefact that shows nothing moves rows out of it** | Dev's first success test as he wrote it compared the board against its own opinion of itself, so it passed hardest in exactly the case he was afraid of. This is the independent side. It is independent of the *board* and not of the *reader* — which is why R24 exists | sow-terms §2.1 P1-9, §6 N-2; annexe-a A-10; annexe-c X-9; brd §5 test 1; discovery decision 6 | **P1-9** |
| **R24** | The reader's four silent failures are each noticed by an alarm: it did not start, it processed zero rows, it ran twice, and a reading that failed and could not be retried is sitting in a queue. A cycle that ran twice does not double the ledger or the tasks | Both auto-signals hang off one reader. If it dies on 2 October the board looks calm, the ledger stops, and the two counts Dev is comparing agree perfectly again. A silent no-op is the most expensive way for this to fail | sow-terms §5.1; annexe-a A-21, A-22, A-23, A-24 | **P1-2**, **P1-3**, **P1-9** |
| **R25** | An agreed budget for how often the store is read, as a number with a named owner and a date, and an alarm that fires when it is crossed | Hammering Marigold's store during Black Friday is the one way an internal tool can hurt Marigold's customers. There is no load test in this depth and none is being bought, and this is what is offered in its place | sow-terms §6 N-5; annexe-a A-35; annexe-c X-11; brd §9 | **P1-2**, **P1-3** |

### 4.6 A late order being a number on a screen instead of a phone call

| # | What must be true | Why | Source | Serves |
|---|---|---|---|---|
| **R26** | An order passing its dispatch promise produces exactly one open task, and the task carries the clock that breached — **A-30 states which fields, and it is the criterion that demonstrates the task appears rather than that the count is right** | Marigold currently finds out from Anjali, who found out from the customer. The clock starts when the order is paid and stops when it is marked fulfilled, both as recorded in Shopify | sow-terms §2.1 P1-3, Assumption 5; annexe-a A-30; brd §2, §4.2 | **P1-3** |
| **R27** | The count of orders past dispatch promise is what devx is accountable for, and the screen states in words which orders it covers and which calendar it counts on — **A-3 carries the count's properties and its artefact** | Dev found out about last November's late orders in January, from a spreadsheet. What devx is accountable for is the number existing, being correct, being visible daily and covering what it claims — Marigold's own target is Marigold's, recorded as Dev's, and declined as a devx criterion. Which orders it covers is settled by D-1 by 14 August, and the calendar by D-12 and C-11 | sow-terms §2.1 P1-3, §6 N-3; annexe-a A-3; annexe-c X-8; annexe-d D-1, D-12, C-11; brd §3, §5 test 2; discovery decision 7 | **P1-3** |

### 4.7 The morning message, and the sheet Priya thinks in — landing by 2 October

These four requirements carry the five outcomes deferred from the 25th — P1-16's screen is R17 in §4.4 —
because eighteen working days will not hold all of it. **Three of the five sit inside the firm core, which
is the three items sow.md promises by 2 October. R30 and R31 are the other two: not quoted until 28 August
and capped at ₹2.2 lakh**; if the quote lands above the cap Marigold drops the pair at no charge and nothing
else in phase 1 moves. Two documents disagree about whether these two are already inside the firm price —
that is Q15 — and §2.1's five rows against sow.md's three is Q16.

| # | What must be true | Why | Source | Serves |
|---|---|---|---|---|
| **R28** | One digest a day, in the morning, saying what is outstanding and who has it, carrying task references and order numbers and never free text, and going nowhere else — **A-15 carries the criterion**. Each recipient receives it in their own morning per R14 | Priya gave up the per-assignment group message so that once a day everybody sees the same list and nobody can say they did not know. **What the channel and the addressee actually are is Q2** — P1-12 says one group message and A-15 says individual messages under D-2's fallback, which is in force at issue | sow-terms §2.1 P1-12; annexe-a A-15; annexe-d D-2, C-14 to C-17; brd §6; discovery decision 8 | **P1-12** |
| **R29** | A completed task leaves the live view after a stated period and stays in the database — **A-16 carries the period and P1-15 carries the distinction between leaving the screen and being destroyed** | Priya wants to open it and see only what is left; Dev wants to count across eight weeks. Those only fight if "clear out" means "destroy", and it does not. **The period in the criterion is contested by the person who asked for it — Q11.** She has said the stated period is how long a completed task should stay *findable*, not how long it sits on the first screen; and the second half of Q11 is whether she can find and reopen one that has left it without devx running a query, which decides whether BRD §6a works at all between 8 October and 5 December | sow-terms §2.1 P1-15; annexe-a A-6, A-16; brd §6, §6a, §11.3; discovery decision 10 | **P1-15** |
| **R30** | Floors typed in the Stock Watch sheet reach the board only on an explicit press, and the board reads back what it understood so a fat-fingered number is visible — **A-13 carries the criterion** | Priya is not typing her floors into a new screen at nine at night. She types them into the sheet, because that is where she thinks. One direction per cell: this is the sheet-to-board direction, floors only | sow-terms §2.1 P1-13, §11.1; annexe-a A-13; annexe-c X-3; brd §6; discovery decision 9 | **P1-13** |
| **R31** | A mirror tab in the sheet, written by the machine, with no cell in it a source of truth. The import path reads only the floors range. The vendor-payment tab and "Sheet1 (do not delete)" are never written to, ever | So Priya can see the board from inside the file she has had for three years. General two-way editing was declined by Priya herself on the two-sources-of-truth argument, not by devx on cost — see §5 | sow-terms §2.1 P1-14; annexe-a A-14; annexe-c X-3, X-6; brd §6; discovery decision 9 | **P1-14** |

### 4.8 Marigold owning it, and the two pieces of work that come before the board

| # | What must be true | Why | Source | Serves |
|---|---|---|---|---|
| **R32** | The repository is in Marigold's organisation from the first commit; the hosting and every third-party account are in Marigold's name, on Marigold's card, with Dev as owner and devx added as a member. **The consequence is stated with it, because it is the price of the arrangement: the perimeter reports and it cannot prevent** | Dev has done this the other way round once. The hosting account was in the agency's name and it took a month and a lawyer's letter to move it. **Every gate in §5 is then a setting on an account Marigold owns. Dev, or anyone at Marigold given administrator rights, can switch off a required check, relax branch protection or rotate the token devx's configuration job reads with, and devx's answer is that the job notices and says so the next time it runs — it cannot stop him. So C-21 names Dev as the only administrator, and if a gate is removed mid-phase devx stops merging on that repository the same working day, says in writing which gate went and what it was protecting, and does not resume until it is back or its removal is a written exception with his name and a revisit date.** Karan Iyer said this out loud to Dev in the room rather than leaving it in a section | sow-terms §2.1 P1-11, §5.5, §8.2, §11.6; annexe-a A-12; annexe-d C-21; brd §13; PRD-scoping decision 28 | **P1-11** |
| **R33** | A production environment exists, provisioned by 18 September — a week before the 25th, not on it — in a named region, and what runs there is the artefact the pipeline promoted rather than a rebuild | Four real people work real orders from 25 September and that does not happen in dev. Dev's own document forbids "we'll sort out production later" in those words. **There is no P1-\* outcome row for this** — see Q14, where the direction is decided (a P1-17 row is added before the SOW issues rather than the version history's claim being withdrawn) and the execution is not yet done | sow-terms §5.4, §11.1; annexe-a A-37; annexe-d §8.4 (18 Sep); brd §13; PRD-scoping decision 41 | no P1-\* row exists at issue; §5.4 |
| **R34** | The store's actual behaviour is measured and written down as a document with its method attached: how often inventory really changes on the SKUs that move, what the orders payload actually contains, and how late a UK fulfilment event arrives — against roughly ninety real UK orders. Done by hand, by Karan Iyer, with no agent session, field-limited at the query, and only after all four preconditions in §10.6 exist | Marigold has no technical person available and the freelancer who set the store up does not answer, so the store's behaviour has to be discovered rather than assumed. **This measurement handles Marigold's customers' personal data even though the board does not** — those are two different sentences, and the ordering of the preconditions is why. Dev offered the store token in the room on 7 August and Karan Iyer refused it, because an orders read returns live customer names, emails and addresses and the note governing it did not exist yet | sow-terms §2.0 S-1, §10.6; annexe-a A-32; annexe-d D-5, C-1, C-7, C-12; discovery decision 22; PRD-scoping decisions 19 and 20 | **S-1** |
| **R35** | The shapes everything else is built on are fixed in writing, on the protected path, with code-owner approval and Priya's written acceptance, before implementation tickets exist: who may see the board and how a person proves they are that person; who may see, complete, assign and reopen; what a task is; what a floor is; what starts and stops the dispatch clock. **The code-owner approval this leans on is not a proven gate and this row does not present it as one** | Code can be rewritten in an afternoon and a permission model four people's work sits on cannot. Freezing it for four people and arriving in November with seven is how every later ticket inherits the wrong shape. What "closed in the tool" counts as is settled here too, on the protected path and not in the living design document. **On the grading in §3: Annexe B records the mechanism that produces the second human as believed to work and never tried — there is no per-path approval count on the host, so it has to come from two owner entries — and §4.3 puts it in the same column as the two High rows devx declines outright, *to build*. §5.3's fourth Setup exit is the first time it will be demanded and satisfied on a real repository; §15 risk 5 calls it a belief until 21 August. Until that exit exists, every second-owner claim in this document is a claim about an untried mechanism, including the one that keeps a fortnight's leave from stalling a protected merge.** Karan Iyer's own signature condition is that the exit happens before the first feature ticket | sow-terms §2.0 S-2, §4.3, §5.3 (exit 4), §15 risk 5; annexe-a A-33; annexe-b ("Second human on protected paths"); annexe-d D-9, D-12, D-13, D-14; PRD-scoping decisions 28 and 29 | **S-2** |

**Requirement count: 35.**

---

## 5. What phase 1 deliberately does not do

The full list is 22 rows in Annexe C and 14 rows in sow-terms §6. What follows is what a founder or an
operations manager would otherwise assume, and it is here because an argument that was lost in August gets
raised again in October by somebody who has forgotten losing it.

### 5.1 The two Marigold pushed on in the room and did not get

**Two-way editing between the board and the Stock Watch sheet.** Priya asked for it in BRD §6 in as many
words — *if I type something in the sheet it shows up in the list, and if something changes in the list it
changes in the sheet, both directions, so they are never different.* It was **declined by Priya herself, on
the argument, not by devx on cost**: both directions means two systems that each believe they are right about
the same cell, and on one Thursday in November Tarun pastes a row while the board changes it, something wins,
and it is wrong half the time with no way to tell which half — on the day volume triples. What replaced it is
R30 and R31: one direction per cell, floors in on an explicit press, a machine-written mirror tab out, no cell
written by both. *(annexe-c X-3; discovery 10:27 and decision 9)*

**An automatic message to the Marigold Ops group every time a task is assigned.** Also asked for in BRD §6 —
*send it to the group as well so everyone can see, so there is no "I didn't know."* Declined in the room,
because the same document says the shared calendar died from pinging. Replaced by one message to the assignee
and one digest a day. *(annexe-c X-4; brd §11.2; discovery 10:19 and decision 8)*

### 5.2 Also out, with the reason

| | |
|---|---|
| **Any write to the Shopify store, in either phase**, and any devx Shopify staff account or theme access | Dev's block, and devx agrees with it. Read scopes only. A store write is one of the two triggers that reopen the depth level, so it is a different project rather than a favour *(X-1, X-2; brd §12 block 2)* |
| **Automatic assignment without Priya's confirmation** | The rule guesses; she agrees *(X-7; R11)* |
| **Reconciling Shopify's stock number with what is on the shelf** | A warehouse problem. The entire stock signal fires off the number Priya has said in writing is wrong, and Dev carries that knowingly *(X-21, N-11, §15 risk 10)* |
| **A warning before an order breaches its dispatch promise** | Priced at ₹1.1 lakh as P1-18, **not bought**, and it displaces work from the 25 September set rather than adding to it. Dev's decision, open — Q19 *(X-22, N-12, §11.1)* |
| **Dev's own success test 1, as he wrote it** | Declined **as an instrument**, in the meeting, with his agreement. As written it compares the count of products that crossed their floor against the count of tasks raised — and the only thing that can count crossings is the same component that raises tasks, so a missed crossing is missing from both sides and the two numbers agree perfectly. It passes hardest in exactly the case he is afraid of. Replaced by the independent reading ledger, which is R23 — and R23's rationale carries the narrowing: the ledger is independent of the *board*, not of the *reader* *(X-9; brd §5 test 1; R23, R24)* |
| **Marigold's own past-promise target as a devx acceptance criterion** | Declined as devx's. It stays Marigold's business target, recorded as Dev's. devx will not accept a criterion whose outcome depends on how fast Tarun answers his phone *(X-8; discovery decision 7)* |
| **A load test, and a rehearsed production restore drill** | Not in Standard depth and not bought. Backups, a written restore path and one timed dev restore are *not* declined — R18 *(X-11, N-5, §15 risk 4)* |
| **Deleting anything** | Archive is a view. Priya's laptop struggling is a reason to trim the sheet mirror, not to lose the history Dev counts *(X-5; decision 10)* |
| **The sheet's vendor-payment tab and "Sheet1 (do not delete)"** | Marigold's, never touched *(X-6)* |
| **Retiring the Monday export Tarun runs** | It survives this phase, so Marigold runs two systems that can disagree. X-18 records that nobody asked; **Priya was asked on 7 August and said yes — conditional on the floors import and the mirror tab existing, which are R30 and R31, the pair nobody has quoted.** So the answer now waits on money rather than on the question being put — Q11 *(X-18, N-13, §15 risk 13)* |
| **Any integration with the Leicester 3PL's own systems** | devx reads what the 3PL puts into Shopify and does not connect to them *(X-17)* |
| **Support, on-call, or anyone answering at 23:00 on 23 November** | Not in scope unless a §11.4 option is bought. If none is, **8 October is a handover, not a go-live**, and Anjali Sharma says so out loud on the day — Q20 *(X-19, D-7)* |
| **Training the two temps** | Their accounts are in scope; someone teaching them is not. R10 is what exists instead, and it is not training *(X-20, §15 risk 17)* |
| **Returns and refunds; anything a customer can see or receive; barcode scanning; purchasing, forecasting or vendor purchase orders; replacing Shopify** | Marigold's own BRD §16. A task may say "call Kalyan Ceramics about the grey bowls" and nothing more *(X-12 to X-16)* |
| **High depth** | Declined by devx, not by Marigold, because three of its rows are *to build* on devx's side and devx will not price a written commitment as a running check. Two are declined outright — mutation testing and the audit trail. **The third is the second named approver on a protected path, which is the mechanism R35 leans on: believed to work, never tried, and now the fourth thing Setup has to produce before a feature ticket starts** *(X-10, §4.3, §5.3; annexe-b)* |

### 5.3 Not in this phase because they are Phase 2

Due dates that mean the same afternoon to everybody, a reminder before something is late, and signals arriving
live instead of on a schedule are **Phase 2, December 2026 to January 2027, and the SOW does not approve
them.** They are named here so nobody reads their absence as an omission. Phase 2 does not fit before
8 October and devx is not going to pretend it does — Dev wrote that if devx claims it does, he will assume
devx has not understood the freeze. *(sow-terms §2.2; brd §7)*

**And one row that leaves phase 1 on a date, not on a preference.** If **D-1** is unanswered on **Friday
14 August**, the **UK half of the late-order signal** moves to phase 2: the signal covers India-warehouse
orders only, the board says on screen which orders those are, **₹0.9 lakh comes off the firm core**, and the
UK work is priced into phase 2's re-quote rather than arriving there free. No date slips, N-3 goes into every
release document, and Dev signs it as a scope note on the day it fires. It is row 4 of §2.3's drop order and
the only row there that was agreed in the room in advance, so it costs no new argument and no new signature.
If the reason it is unanswered is devx's own slip rather than Marigold's on C-1 or C-2, a date moves instead
and Anjali Sharma names which. R27 carries the screen honestly; this is the scope and the money.
*(sow.md "What we are building"; sow-terms §2.3 row 4, §12's scope-reduction table, §6 N-3, §9.3; annexe-d
D-1; PRD-scoping decision 22)*

### 5.4 What will not be verified

All fourteen rows are in sow-terms §6 and every one of them goes into every release document. The ones that
change what somebody should expect on 25 November: nothing built here can see a change made inside the
Shopify admin until the next read (N-1); anything that dips below its floor and recovers between two readings
did not happen as far as the board is concerned (N-2); a UK order's dispatch clock is not verified unless D-1
resolves in time (N-3); a message being read, or reaching a handset at the unit, is not verified (N-4);
behaviour under festive load is not verified (N-5); the shelf is not reconciled (N-11); phase 1 is not claimed
to move the late-order count (N-12); the sheet and the Monday export both survive (N-13); and the board is not
verified to be pleasant to use (N-14).

**That is nine of the fourteen, chosen for what they change on 25 November. All fourteen bind, and the five
not summarised above are these:** Marigold's freeze does not literally cover an internal board, so no feature
deploys after 8 October and a defect fix inside 8 October to 5 December needs Dev's sign-off per fix (N-6); a
test and the code it covers can share the same misunderstanding, because both are written by the same kind of
session, and the answer is partial and stated as partial (N-7); **devx cannot verify that agent-written code
contains nothing reproducing third-party code — no licence-compatibility check, no copyleft check, no
verbatim-reproduction detection (N-8)**; devx does not verify Marigold's business outcomes, including Dev's
fifteen-minute teach test and his own past-promise target (N-9); and what a person types into a free-text task
is neither verified nor filtered (N-10). N-8 is the one a reader of this document would otherwise not meet at
all, so it has §5.5 to itself.

### 5.5 The half of this that is about how the code gets written

**An agent writes most of the code, and three parts of devx's position on that are not finished.** This is
sow.md's second thing to know before signing. It is here because this document is what Marigold accepts, and
a PRD that never mentions it presents a cleaner product than the SOW sold.

**Originality is not warranted, and the refusal is on the signature page.** There is no licence-compatibility
scan, no copyleft check and nothing that detects a generated block reproducing third-party code, so devx
cannot demonstrate that agent-written code is original — that is N-8 — and Karan Iyer will not sign
Marigold's standard clause as written, because a warranty nobody can test is worse for Marigold than a
qualified one. What goes to Marigold's adviser is a qualified clause plus a plain description of what devx
actually does: the code is reviewed by a fresh session and by a person, it arrives in pieces small enough to
read, and third-party dependencies are scanned for known vulnerabilities. **That is not originality and devx
will not call it that.** *(sow-terms §6 N-8, §10.3; annexe-d D-6; PRD-scoping decision 36)*

**Whether Marigold's own repository carries a permanent record that a session wrote the code is Dev's
decision, not devx's.** The repository is Marigold's from the first commit, so a commit trailer is a
permanent, discoverable record sitting in an asset Marigold may later show a buyer, an auditor or the next
agency — and it is not reversible in any real sense, because Marigold's own branch protection forbids the
force push it would take. **The default is that no such record is written.** D-11 is answered before the
first commit rather than before the first release, and if it is unanswered on the day Setup starts devx
writes no trailer and holds the internal side-table — a decision made in Dev's absence that he can change
going forward and not backward. That it is effectively permanent either way is recorded as his risk.
*(sow-terms §10.7, §15 risk 15; annexe-d D-11; PRD-scoping decision 36)*

**The policy on what an agent may read and transmit is half written.** The engagement note that closes it,
D-5, is a precondition of the first read of Marigold's store rather than a document that follows it — which
is the whole reason R34's preconditions are ordered the way they are, and why Karan Iyer refused a store
token Dev offered him in the room. *(sow.md "Four things to know before signing" item 2; sow-terms §10.6;
annexe-d D-5, C-7, C-12; annexe-e; PRD-scoping decisions 19 and 20)*

---

## 6. Open questions

Every one has an owner and a date. Those carried from the SOW keep their D-\* or C-\* number so the window is
the same window. Those that arrived with the prepared positions of 7 August 2026 are new here and are marked
as such — **a new one is a change request under sow-terms §12, priced within two working days, and it costs
either a named row from §2.3's drop order or a place in phase 2.** None of them is a requirement in §4.

**The frozen PRD-scoping note of 7 August 2026 is the record of that meeting and it numbers the same
twenty-seven items Q1 to Q27, so the two documents resolve to each other. Where this document and that note
differ on a number, an owner or a date, the note is the record and this document is corrected against it by
Anjali Sharma under §12.** Twenty-seven is also the count the date in §1 depends on: each of these is
answered inside its stated window or the date moves.

### 6.1 Who the users are, and what gets measured

| # | Question | Owner | Date |
|---|---|---|---|
| **Q1** | Is there a **second customer-support person**? BRD §1 has Dev saying two and Priya saying one, and the BRD says out loud that the two paragraphs do not match. Assumption 2 assumes one, and C-9's accounts, A-11's exhaustive role-to-action tests and the staff inventory in §10.4 all sit on it. This is the contradiction discovery did not close | **Dev Rawat** | **Fri 21 Aug 2026**, and before S-2's shapes are signed in Setup *(brd §1, §11; annexe-d Assumption 2)* |
| **Q2** | **What ships on 2 October: one message to the Marigold Ops group, or individual messages?** P1-12 says a group message; A-15 says the channel is per D-2 *whose fallback is in force at issue — individual messages, not a group message*. If it is individual, what replaces "nobody can say they didn't know", which is the only reason Priya gave up the per-assignment group message in X-4 | **Karan Iyer** (the fact), **Anjali Sharma** (the document) | **D-2's date, Tue 11 Aug 2026**, restated in writing at Kickoff *(sow-terms §2.1 P1-12; annexe-a A-15; annexe-d D-2; annexe-c X-4)* |
| **Q3** | **Dev's third success test against the 08:00 digest.** Test 3 says that if there is still an 8am roll call in WhatsApp this failed regardless of what the code does — and P1-12 is an automated 08:00 message. Priya's answer in the room was "it is not a roll call if I am not asking anyone anything"; the only thing standing between the two sentences is that remark in a frozen note, and §14 hands the judgement of test 3 to Priya, who asked for the digest. **Dev to write the distinction in his own words, or the test stands as written** | **Dev Rawat**, with Priya Menon | **before Kickoff, Mon 24 Aug 2026** *(brd §5 test 3; discovery 10:19; sow-terms §14; reviews/2026-08-06-sow-hostile.md)* |
| **Q4** | **What it is fair to measure in November.** BRD §11 point 4 is still open — Dev asked directly, "tell me what it is fair to measure", and no document answers it. Decision 7 split accountability and X-8 declined the target as a devx criterion, but splitting accountability is not answering the question. If D-1 fires on 14 August the population the number is measured over changes six weeks before the window opens | **Anjali Sharma**, one page | **at Kickoff, Mon 24 Aug 2026** *(brd §11.4, §17.2; sow-terms §6 N-12; annexe-c X-8; annexe-d D-1)* |
| **Q5** | **Last November's late-order figure, computed out of Shopify's own order history against whatever calendar rule D-12 settles**, so November 2026 is a comparison and not only a baseline. **New on 7 August; nothing in the SOW, the terms or the annexes covers historical orders.** It is a §12 change request | **Anjali Sharma** to price; **Dev Rawat** to decide | **priced within two working days of the request** *(new; brd §3; annexe-d D-12)* |

### 6.2 How the board behaves — settled at Kickoff or not at all

| # | Question | Owner | Date |
|---|---|---|---|
| **Q6** | **Is a floor per product or per variant?** A-1 says "a product whose stock crosses below its floor"; A-8 says "~60 authored by hand … 200 new SKUs inheriting"; BRD §1 says about nine hundred SKUs counting every size and colour separately, which is how the store counts them. It decides how many numbers Priya types in her afternoon and whether a task can tell Tarun which colour to ring the vendor about | **Karan Iyer** with **Priya Menon** | **at Kickoff, 24 Aug 2026**, before A-33 is signed *(annexe-a A-1, A-8; brd §1)* |
| **Q7** | **D-14, with a third option on the table.** When a product is already below its floor with an open task and the number drops further or hits zero, does the open task's reading update, and does anything happen at zero? Priya has said she will not answer D-14 as posed — one task or two — because neither is what she needs. A-2's behaviour stands until she decides | **Priya Menon** | **at Kickoff** *(annexe-a A-2; annexe-d D-14; brd §15.3)* |
| **Q8** | **Reassignment.** Moving an already-assigned task from one person to another in one action, and telling the old assignee it is off their name. **It is absent from all 39 criteria** — A-4 proves assigning an unassigned task, A-6 proves complete-and-reopen, A-11 sets who may assign, and none of them reaches this. Priya does it fifteen times on a Diwali day, and a task moved without the old assignee being told is the Manchester order rebuilt in software. **New on 7 August** | **Priya Menon** to specify; **Anjali Sharma** to route and price | **at Kickoff**; priced within two working days *(new; annexe-a A-4, A-6, A-11; brd §3)* |
| **Q9** | **A per-person waking window** instead of A-26's fixed hours — 07:00 for Rakesh, who starts then, and later than 21:00 for Tarun in the festive weeks, when packing runs past 22:00. As written the criterion protects Anjali's night with a number that is wrong for the two people who are awake. **New on 7 August** | **Karan Iyer** with **Priya Menon** | **at Kickoff** *(new; annexe-a A-26; brd §1)* |
| **Q10** | **Who sets the digest's send time, and is Priya's 08:00 IST?** She said eight because eight is when the roll call happens, not because eight is when she reads anything — she is at a desk around 9, sometimes 9:30. **New on 7 August** | **Priya Menon** | **at Kickoff** *(new; annexe-a A-15; brd §2)* |
| **Q11** | **How long a completed task stays on the live view, and whether Priya can find and reopen one that has left it.** Two halves. She has said seven days is how long it should stay *findable*, not how long it sits on the first screen. And A-6 proves reopening a task in front of her, while A-16's "remains queryable" may mean devx runs a query — in which case during 8 October to 5 December she cannot do it at all, and BRD §6a does not work in the eight weeks it was written for. Also: **Priya was asked in the room on 7 August whether to retire Tarun's Monday export and said yes**, conditional on the floors import and the mirror tab existing — P1-13 and P1-14, the pair not quoted until 28 August. X-18's "nobody asked" is discharged and the answer now waits on money | **Priya Menon** (behaviour), **Karan Iyer** (whether it needs devx) | **at Kickoff** *(annexe-a A-6, A-16; annexe-c X-18; sow-terms §2.1 P1-15, §11.1, §6 N-13; brd §6, §6a)* |
| **Q12** | **Is adding a task and putting a name on it one action from one screen on a phone?** A-29 proves typing a task and A-4 proves assigning one. If they are two screens, then Priya's twenty thoughts a day are forty jobs and the twentieth goes into WhatsApp instead. **New on 7 August** | **Priya Menon** with **Karan Iyer** | **at Kickoff** *(new; annexe-a A-4, A-29; brd §6, §10)* |
| **Q13** | **Whether the free-text body of a task should be visible to all seven accounts, including the two temps.** Assumption 7 and A-11 say everyone with a session sees every task; §10.4 says keeping a customer's details out of a model prompt is an instruction to four named people. Priya will type a customer's phone number into that box, because that is how she chases a courier. A-25 keeps it out of logs, error reports and messages — it does not touch the screen. **New on 7 August, and it is Dev's to decide because it touches customer data** | **Dev Rawat** | **at Kickoff** *(new; sow-terms Assumption 7, §10.4, §6 N-10; annexe-a A-11, A-25; brd §11.5, §12)* |

### 6.3 Defects in the SOW's own arithmetic, to fix before it issues on 11 August

| # | Question | Owner | Date |
|---|---|---|---|
| **Q14** | **There is no P1-17 row.** The terms' version history claims "a named production environment with a promotion criterion (P1-17)" as a v1.0 addition. §2.1 runs P1-0 to P1-16 and no P1-17 exists anywhere. Production is real — §5.4, §11.1's includes list, and A-37 — but the outcome Dev was told was added is not in the list of outcomes. **R33 above therefore cites §5.4 and not an outcome number.** Direction decided at PRD-scoping decision 41: the P1-17 row is added rather than the version history quietly corrected, because production has a criterion, a date and a place in the includes list and Dev was told an outcome was added. Nothing about the money moves. The execution is before issue | **Anjali Sharma** | **before v1.0 issues, Tue 11 Aug 2026** *(sow-terms version history, §2.1, §5.4, §11.1; annexe-a A-37; PRD-scoping decision 41)* |
| **Q15** | **§2.1 says the 2 October block is "inside phase 1's price"; §11.1 puts P1-13 and P1-14 outside the firm ₹11.6 lakh, unquoted until 28 August, capped at ₹2.2 lakh.** Two sections disagree about whether ₹2.2 lakh of work is already paid for, and sow.md's cost table follows §11.1 | **Anjali Sharma** | **before v1.0 issues** *(sow-terms §2.1, §11.1; sow.md)* |
| **Q16** | **sow.md says "three items following by Friday 2 October"; §2.1's deferred list has five rows, P1-12 to P1-16.** Both are defensible — three are in the firm core — but the signature document governs, and a reader counting five against a promise of three reads it as scope arriving unpriced | **Anjali Sharma** | **before v1.0 issues** *(sow.md; sow-terms §2.1)* |
| **Q17** | **The risk count and the non-verification count, one fixed and one not.** The risk count was the defect Dev found in an evening: the summary page told him thirteen risks with four in his name while §15 as printed carried nineteen rows with ten in his name, the number 13 used twice on two rows saying nearly the same thing about the sheet and the Monday export, and the version history said eighteen — on a page that governs, which would have silently discarded six risks carried in his name. **It is conceded in full at PRD-scoping decision 2 and corrected for issue: sow.md, §15 and the version history now reconcile at eighteen rows — seven Karan Iyer, two Anjali Sharma, nine Dev Rawat — and §13.1's six things he signs to have been told sit inside the nine.** Dev's condition at decision 3 is that he does not sign while the two documents disagree, and this is what discharges it. **What is not fixed is the other count: sow.md says thirteen things will not be verified and §6 has fourteen rows, N-1 to N-14** — see §5.4, which carries all fourteen | **Anjali Sharma** | **before v1.0 issues, and before signature on 20 Aug** *(sow.md; sow-terms §6, §13.1, §15, version history; PRD-scoping decisions 2 and 3)* |
| **Q18** | **Two more reference defects.** The annexe letters collide: §10.1, §10.6 and §13.1 use "Annexe A" for the model-provider annexe and "Annexe B" for Dev's written reply, and §9.2/§11.1 use "Annexe C" for the 5 August envelope approval — while the folder has A as the acceptance criteria, B as the checks and C as the exclusions. **C-7, a precondition of all work on Marigold's material, is defined as a "written reply to Annexe A" and resolves to 39 acceptance criteria.** And in §15, risk 17 cites X-21 for the untaught temps when they are X-20, and risk 16 cites X-20 for English-only when it is D-13 and §3. Direction decided at PRD-scoping decision 40: the prose is corrected to name each attached document by its title rather than by a letter, and the folder is not renumbered because the folder is what readers have. The two wrong cross-references are fixed with it | **Anjali Sharma** with **Karan Iyer** | **before v1.0 issues** *(sow-terms §9.2, §10.1, §10.6, §11.1, §13.1, §15; annexe-d C-7; annexes A, B, C; PRD-scoping decision 40)* |

### 6.4 Money, and the shape of the 25 September set

| # | Question | Owner | Date |
|---|---|---|---|
| **Q19** | **P1-18, the pre-breach warning at ₹1.1 lakh: bought or not — and if bought, which named row leaves the 25 September set.** It displaces work rather than adding to the ceiling. On §2.3's own never-dropped line, the only rows left that could go are P1-6's bulk-edit screen and P1-10's dedicated view; that reading needs confirming in the scope note before Dev authorises it, not in the third week of September. If it stays unbought, Dev accepts in writing that the November figure is a baseline and not a result | **Dev Rawat** to decide; **Anjali Sharma** to name the displaced row | **at Kickoff, 24 Aug 2026** *(sow-terms §11.1, §2.3, §6 N-12, §14; annexe-c X-22)* |
| **Q20** | **Which after-go-live option, A at ₹1.6 lakh, B at ₹2.9 lakh, C at ₹55,000 a month, or D at zero** — with the honest difference between A and B stated plainly, since B buys someone who diagnoses and waits for morning rather than someone who merges alone at 02:00. Under D there is no fix path at all through the freeze | **Dev Rawat**; **Anjali Sharma** priced it | **before signature, Thu 20 Aug 2026** *(sow-terms §11.4; annexe-d D-7; annexe-c X-19)* |
| **Q21** | **The running-cost levers priced side by side, so the ceiling decision is a decision.** The band tops out ₹11,000 above Marigold's stated monthly ceiling and the overrun is recorded as Dev's risk while the levers sit with devx. The two levers are the read interval — which trades directly against the blind window in N-2 and therefore against the November number's error bar — and email in place of the messaging provider. **Nobody has yet asked Dev to choose one.** Note also that the ceiling breach is in §11.3 and §13.1 but not on the two-page document that gets repeated to Anjali Sen and Ravi Menon | **Karan Iyer** to price the trade; **Dev Rawat** to choose | **Fri 21 Aug 2026**, reported at that week's demo *(sow-terms §11.3, §6 N-2, §15 risk 18, §13.1; brd §8)* |
| **Q22** | **§15 risk 12 carries Dev's name and is about Priya's button.** Nowhere does the document record whether the person the risk is about accepts it. Priya's position, stated in preparation: she accepts it for a normal week and refuses it for 12 October to 30 November and for Tuesday and Thursday afternoons. Two candidate answers exist and both are §12 changes — a second confirmer who is in the building, or a window in which Tarun and Anjali (care) may pull an unassigned task onto their own name and it shows in the digest as self-assigned. **The second is not "a computer telling Rakesh to do something", so it does not reopen X-7 as written — but it is a change to the permission model in A-11 and therefore to S-2's shapes** | **Anjali Sharma** to record Priya's position and price both; **Dev Rawat** to decide | **before signature**, priced within two working days *(sow-terms §15 risk 12, §9.1; annexe-a A-11, A-28; annexe-d D-4; annexe-c X-7)* |
| **Q23** | **The remaining asks from 7 August that trace to nothing in the SOW.** Each is a §12 change request and each costs a named row from §2.3 or is phase 2: a note and a promised date recorded on a task when Tarun calls a vendor (a note alone if the date is the expensive part, because dates are P2-1); a way for Rakesh to say the shelf disagrees with the reading, and a count of how often he says it by November, so risk 10's size is knowable; Hindi, which Karan Iyer corrected in the room from "the four screens Rakesh touches" to the whole surface plus a switch plus somebody who can check the words that decide what Rakesh presses, against D-13's English-only fallback; half an hour with the two temps in the first week of November, against X-20, priced as a half-day because nobody travels to Bhiwandi for thirty minutes; an adoption number for the pre-window fortnight — tasks created and closed per person — since N-14 and A-38 are the whole of the current answer on adoption, **with the checkpoint itself already agreed at no charge as a named agenda item on the demos of 30 September and 7 October, and "allowed to stop and change something" refused as written, because after last merge changing something means displacing something and nothing left in the set is off §2.3's never-dropped line**; and **P2-1, due dates, moved into phase 1**, refused as a phase-1 requirement at PRD-scoping decision 10 with the reason — due dates change what a task is, which is a shape frozen in S-2 before any ticket exists — and priced as a change request. Dev did not accept that refusal and did not withdraw the ask | **Anjali Sharma** to price each; the deciding level is §12 step 3 | **priced within two working days of each request** *(new; annexe-d D-13; annexe-c X-20, X-21; sow-terms §6 N-14, §15 risks 10, 16, 17, §2.2 P2-1, §2.3; PRD-scoping decisions 10 and 38)* |

### 6.5 Dates, capacity and the record

| # | Question | Owner | Date |
|---|---|---|---|
| **Q24** | **Do the eighteen working days survive Marigold's own calendar?** They were counted without C-11 in hand. **C-11 is a list of dates Priya writes — including the Sundays and the days the Bhiwandi unit is actually shut, which are not the public holidays — and it now arrives before Kickoff rather than at it (PRD-scoping decision 23).** Two dates are already visible: **2 October, the last-merge date carrying the deferred outcomes, is Gandhi Jayanti**, and Dev agreed to it on the understanding that it left five clear days before the freeze; 15 August falls inside the pre-signature window. If the arithmetic comes back short, features come out in §2.3's order and Dev hears it in August, whichever way it comes out | **Anjali Sharma**; **Priya Menon** for C-11 | **C-11 before Kickoff**; result at that week's demo *(annexe-d C-11, §8.4; sow-terms §2.3; PRD-scoping decisions 23 and 26)* |
| **Q25** | **Priya's September hours, added up week by week, and the floors afternoon booked as a date rather than "inside the first fortnight".** Load-bearing in ten places and budgeted in one: C-10's two hours a week plus the Wednesday demo, C-6's floors afternoon, C-4's handset details, C-11's calendar, C-13's stock adjustment on 18 September, A-7's handset screenshot by 15 September, A-31's two timed recordings, A-33's sign-off, A-38's design-brief acceptance, and §7.3 acceptance of the 25 September release. All inside the five weeks the festive SKUs go up. **Priya has refused the second A-31 recording being taken between 25 September and 8 October; it is taken in the week of the 25th or in the first week of December, and A-31 itself stands as written (PRD-scoping decisions 15 and 16).** She has also refused to accept the design brief on the strength of a document — R9 carries that condition — and C-13 now has her name and an agreed time on it | **Anjali Sharma** | **at Kickoff, 24 Aug 2026** *(annexe-d C-4, C-6, C-10, C-11, C-13, §8.4; annexe-a A-7, A-31, A-33, A-38; sow-terms §7.3; PRD-scoping decisions 15, 16, 17, 24, 25)* |
| **Q26** | **Whether anything of Marigold's went through a model between 6 and 11 August.** §10.6 states in prose that nothing of Marigold's had been uploaded when the SOW was drafted, and that the discovery notes and the SOW were written from the BRD and the recording. Dev's condition in BRD §12 is the provider named in writing before the first upload, his permission is dated the 11th, and the version history says v1.0 was drafted from his BRD on the 6th. He has asked for it confirmed in writing before he signs, and he named it the one condition that was not theoretical | **Karan Iyer** | **before signature, Thu 20 Aug 2026** *(brd §12; sow-terms §10.1, §10.6, version history)* |
| **Q27** | **A frozen record of the PRD-scoping meeting of 7 August 2026 was owed, and it now exists** — `docs/meetings/2026-08-07-prd-scoping.md`, frozen on the day, on the same terms as the discovery note: corrections appended with a date and an author, never edited in. **It discharges this row at issue**, and it is the record every *PRD-scoping decision N* citation in this document resolves to. It stays in the list so those citations resolve to a numbered row rather than to nothing. This document was drafted from the four prepared positions before the note existed; where the two differ on a number, an owner or a date, **the note is the record and this document is corrected against it** | **Anjali Sharma** | **discharged 7 Aug 2026**, ahead of its date of Thu 20 Aug 2026 *(docs/meetings/2026-08-07-prd-scoping.md, "Status of this record" and Q27; discovery note "Status of this record")* |

---

## 7. What would make this phase a failure even if every requirement shipped

Stated plainly, because every one of these is survivable if it is expected and expensive if it is a surprise.

**Nobody opens it.** Trello died here in nine days because it was a second place to look, and a second place
to look is a dead thing. All 35 requirements can pass with four people still settling the day in WhatsApp.
The SOW does not verify that the board is pleasant to use, there is no designer, and the whole of the current
answer is a design brief accepted in writing before tickets exist, on a real phone with Rakesh in the room
for ten minutes of it. That is a good answer and it is not the whole answer — Q23 carries the adoption
number, and it has to be looked at inside the pre-window fortnight. The checkpoint for looking at it is
agreed at no charge and is a named agenda item on the demos of 30 September and 7 October. What that
checkpoint is not is a licence to change something: after last merge on 2 October, changing something means
displacing something, and nothing left in the set is off §2.3's never-dropped line. It is the last date on
which a row can come out with Dev's eyes open, which is a real decision and not the one he asked for.

**It becomes the second place to look rather than the first.** The sheet survives by Priya's own choice and
Tarun's Monday export survives because nobody asked to retire it, so for at least one phase Marigold runs two
systems that can disagree. Nothing on a task carries a date in this phase, because dates are Phase 2. A list
that cannot tell you what is for today is a list you stop opening.

**Priya is the throughput limit on the days it matters.** She is the only person who confirms an assignment
and the only person who reopens. On the morning thirty orders breach at once, thirty tasks sit there until
she has pressed a button thirty times, and on a Tuesday afternoon she is at the unit. An ageing flag tells
her a queue is backing up; it does not clear it. If Q22 lands as "no change", the board is behind by
lunchtime on the days that count and the four of them finish the day in the group chat — which is Dev's third
test failing by design rather than by code.

**The November number arrives as a baseline nobody agreed was a baseline.** Phase 1 fires after a breach, so
it makes the late-order count exist and makes it trustworthy and cannot reduce it. If P1-18 stays unbought
and Q4 is never answered, the 25 November review is an argument about whether Marigold was mis-sold rather
than a reading of six tests.

**The first task is wrong and Priya stops believing the board.** The stock signal fires off Shopify's number,
which Priya has said in writing disagrees with the shelf, and reconciliation is out of scope by Dev's choice.
She will disbelieve a number she cannot reconcile exactly once, and then stop looking. The same failure is
available through the dispatch clock: an order paid at 18:00 on the Friday before a holiday Monday breaching
at 18:00 on Sunday, because C-11's calendar was wrong or late.

**The reader dies quietly and the board looks calm.** Both auto-signals hang off one scheduled reader. If it
stops on 2 October, no reading is written, no task is raised, and the two counts Dev compares in November
agree perfectly. That is why R24 is four alarms with their own test runs and not a monitoring intention.

**Rakesh cannot use it, and it is found out too late.** Nobody has looked at his phone yet. If the real
handset fails the profile after last merge on 2 October, the fix is January — which is what the 15 September
evidence date exists to prevent, and it only works if C-4 lands on 21 August.

**Priya's floors afternoon lands late.** The board cannot raise a single stock task for a product with no
floor. If C-6 slips into late September, the 25th demonstrates on category defaults only and the pre-window
fortnight stops being a test of anything.

**Nobody bought a fix path, and 8 October passes as though it were a go-live.** Under Option D nobody is
watching the alarms through the eight weeks in which every operational weakness Marigold has turns into a
refund, and no fix path exists at all. That is survivable as a decision and not as a discovery, which is why
Anjali Sharma says it out loud on the day.

---

**FICTIONAL — see the notice at the top of this document.**
