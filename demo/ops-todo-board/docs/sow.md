**FICTIONAL DOCUMENT — CREATED FOR A DEMONSTRATION.** Marigold Living does not exist. Dev Rawat, Priya Menon, Anjali Sen, Farhan Qureshi, Ravi Menon, Tarun, Rakesh, Anjali (customer care), Kalyan Ceramics, the Leicester 3PL, Anjali Sharma, Karan Iyer, Nikhil Barve, Sneha Raut, Imran Shaikh, Deepa Kulkarni, and every date, order number and rupee figure below are invented for a simulated engagement. Third-party model-provider names are withheld deliberately: in a real SOW the provider is named in writing in Annexe A, and naming one in a fictional document would attach a real company to an invented engagement. devx labs' process is real; this client, this engagement, these prices and these dates are not.

# Statement of Work — Ops To-Do Board

| | |
|---|---|
| **Client** | Marigold Living (fictional) |
| **Supplier** | devx labs |
| **Version** | **0.9 DRAFT — pending tech-lead sign-off** |
| **Date** | 6 August 2026 |
| **Written by** | Anjali Sharma, delivery lead, devx labs |
| **To be reviewed and signed by** | Karan Iyer, tech lead, devx labs |
| **Stage** | 00 Solutioning |
| **Inputs** | BRD v1.1, 6 August 2026 (Marigold's own document) · Discovery meeting notes, 6 August 2026, frozen |
| **Status of this draft** | Not issued to Marigold. Karan has not read it. Nothing in it is offered or agreed until both devx signatures are on section 13 |

> **This draft is unsigned on purpose.** The version Marigold receives on Monday 11 August will be 1.0 and will carry Karan's signature. If he cannot stand behind a sentence here, the sentence changes before it leaves the building — that is what his signature is for, and section 13 says so in his own words.

---

## How to check this document is complete

Our own process says a person who did not write the SOW must be able to point at six things. They are here, in this order, so nobody has to trust that they exist:

| # | The thing | Where |
|---|---|---|
| 1 | The signature date | §13 |
| 2 | The depth level, with its reasoning | §4 |
| 3 | The personal-data inventory | §10.4 |
| 4 | The named third-party AI provider, with written permission attached | §10.1 and Annexe A |
| 5 | What happens after go-live | §11.4 |
| 6 | The list of our checks, every row marked *written*, *proven* or *to build* | §5.2 |

A missing one means Solutioning is not finished. It does not mean it will be caught later.

---

## 1. The engagement, in one paragraph

devx labs will build Marigold Living an internal task board for the operations team. Work arrives on it by itself from two signals in the Shopify store — a product dropping below a stock floor Marigold sets, and an order passing the dispatch promise Marigold has published — and anything a person types in themselves. Priya assigns each task to one named person, that person completes it, and every completion is recorded with who did it and when so it can be put back if it was not really done. The board reads from Shopify and never writes to it: it tells a human what to do, and the human does it in Shopify under their own login. Phase 1 is usable by four real people on real orders by 25 September 2026, before the festive window opens, and is finished changing before Marigold's freeze. Phase 2, in December and January, adds due dates that mean the same thing in India and the UK, reminders before something is late rather than after, and a live feed from the store so signals arrive as they happen instead of on a schedule. Marigold owns the repository, the hosting and every third-party account from the first day.

That paragraph is written to be repeated to Anjali Sen and to Ravi Menon without either of them reading anything else.

---

## 2. Scope, by phase, as outcomes

Each row is an outcome — a thing that is true when we are finished — not a task. What proves each one is in §7.

### 2.0 Before the board: two named pieces of work

These are not overhead and they are not free. Both came out of discovery.

| | The outcome | Why it is scope and not a task inside the first ticket |
|---|---|---|
| **S-1** | **The store's actual behaviour is measured and written down**: how often inventory really changes on the ~60 SKUs that move, what the orders data actually contains, and how late a UK fulfilment event arrives relative to the order being paid — measured against roughly 90 real UK orders, not taken on anyone's word | Marigold has no technical person available. The freelancer who set the store up does not answer. Our process expects at least one call with the client's own technical people, and where there is not one, the system's behaviour has to be *discovered*. Discovery has a duration; an assumption does not, until it is wrong in October |
| **S-2** | **The shapes everything else is built on are fixed first**: who may see, complete, assign and reopen a task; what a task is; what a stock floor is; what the dispatch clock starts and stops on | Code can be rewritten in an afternoon. A permission model that four people's work sits on top of cannot. Freezing this for four people and arriving in November with seven is how every later ticket inherits the wrong shape |

### 2.1 Phase 1 — the board, by 25 September 2026

Usable by Priya, Tarun, Rakesh and Anjali (care) on real orders. Farhan joins from September.

| # | Outcome |
|---|---|
| **P1-1** | **One board all users see the same version of.** Everyone sees every task. Unassigned tasks sit at the top so they cannot be quietly ignored. Works on a phone, including Rakesh's, at the signal quality of the Bhiwandi unit — subject to A-8 |
| **P1-2** | **A task appears by itself when a product drops below its floor**, without anyone opening a sheet or a screen |
| **P1-3** | **A task appears by itself when an order passes its dispatch promise.** The clock starts when the order is paid and stops when it is fulfilled. What "its dispatch promise" covers — India-warehouse orders only, or India and UK — is settled by D-1 in §8, not by this document |
| **P1-4** | **A person can add a task themselves**, in their own words, because half of Priya's day is neither stock nor orders |
| **P1-5** | **Every task carries exactly one person's name, and it got there because Priya put it there.** A rule proposes the name — stock to Tarun, packing to Rakesh, customer-facing to Anjali (care), money or vendors to Priya — and nothing is assigned until Priya, or her named backup, confirms it. No person is told to do anything by a computer |
| **P1-6** | **Stock floors exist for every product without Priya typing 900 numbers.** A default per category, a per-product override, and one screen where forty can be changed in a sitting. The ~200 new festive SKUs inherit their category default the day they are created |
| **P1-7** | **Completion is a record, not a claim.** Who marked a task done, and when. Priya, or her backup, can put it back. Nothing is deleted, in this phase or the next |
| **P1-8** | **The person whose name is on a task is told, once, when it lands.** Nobody else is told. There is no automatic message to the group on assignment — that is the decision in §3, row X-4, and the reason is in it |
| **P1-9** | **An independent record of what the store said.** Every inventory reading we take, per product, with a timestamp, appended and never edited, never archived, held apart from the board. This is what makes it possible to ask *did the board miss a crossing* rather than asking the board whether it missed anything |
| **P1-10** | **Priya can answer "what is unfinished right now and who has it" in under a minute without asking anyone** |
| **P1-11** | **Marigold owns everything from day one.** Repository in Marigold's organisation from the first commit; hosting and every third-party account in Marigold's name, on Marigold's card, with Dev as owner and devx added as a member |

**Landing by 3 October 2026** (last merge), inside phase 1's price, deferred from the 25th because eighteen working days will not hold all of it:

| # | Outcome |
|---|---|
| **P1-12** | **One message to the Marigold Ops group each morning at 08:00 IST**: what is outstanding and who has it. Channel subject to D-2 in §8 |
| **P1-13** | **Stock floors can be typed in the Stock Watch sheet and imported**, on an explicit press, with the board reading back what it understood so a fat-fingered number is visible |
| **P1-14** | **A mirror tab in the sheet, written by the machine**, so Priya can see the board from inside the file she thinks in |
| **P1-15** | **Completed tasks leave the screen after seven days.** They leave the *screen*. They stay in the database |
| **P1-16** | **A screen showing, for a chosen week, what was marked done and later put back, by person.** The data behind it is captured from the first day of P1-7, so choosing not to build the screen would not have cost the history |

### 2.2 Phase 2 — December 2026 to January 2027

| # | Outcome |
|---|---|
| **P2-1** | **A due date means the same afternoon to everyone who reads it.** A task due "end of Tuesday" is unambiguous to Rakesh starting at 07:00 IST and to Anjali (care) working a UK evening, and the board shows each person the deadline in their own day |
| **P2-2** | **A reminder arrives before something is late**, not after. Once per task. A reminder that has been sent cannot be unsent, so this path is treated as a dangerous path: it is on the protected list in §5.1, it needs a second reviewer, and send-once behaviour is a criterion with an artefact against it |
| **P2-3** | **Signals arrive live.** The store tells the board when something changed, instead of the board asking on a schedule. This narrows — it does not remove — the blind window described in §6, row N-2 |
| **P2-4** | **The reading ledger records which signals arrived live and which came from a scheduled read**, so the November verdict's error bar and the January one are comparable rather than merely different |

Phase 2 does not fit before 8 October and we are not going to pretend otherwise. Dev's own document says that if we claim it does, he will assume we have not understood the freeze. He is right.

---

## 3. Explicitly out of scope

Two kinds of row: things Marigold said they were not asking for, and things that were discussed and declined. The second kind is the useful kind, so the reason is written next to each.

| # | Not in scope | Why |
|---|---|---|
| **X-1** | **Any write to the Shopify store, in either phase.** No inventory adjustment, no marking fulfilled, no product edit, no order edit | Dev's block, and we agree with it. Read scopes only: products, inventory, orders, fulfilments, locations. The board tells a human; the human acts in Shopify under their own login, where Shopify already records who did it. Any phase-2 write is a separate decision Dev signs separately, with a named accountable person, access scoped to that one operation, and a change record he can read without asking us |
| **X-2** | **A Shopify staff account for anyone at devx labs, and any access to the theme** | Not needed — nothing we build lives in the theme. Named here anyway because it has cost Marigold two days of their own copy before. Nobody at devx edits the live theme, for any reason, including a one-line fix |
| **X-3** | **Two-way editing between the board and the Stock Watch sheet** | Discussed at length and **declined by Priya on the argument**, not by us on cost. Both directions means two systems that each believe they are right about the same cell; one Thursday in November Tarun pastes a row while the board changes it because an order shipped, something wins, and it is wrong half the time with no way to tell which half. That is the day volume triples and the day everyone goes back to paper. What replaced it: one direction per cell — sheet to board for **floors only** on an explicit import, board to sheet as a machine-written **mirror tab**. No cell is written by both |
| **X-4** | **An automatic message to the Marigold Ops group every time a task is assigned** | Asked for in the BRD and declined in the room, because the same document says the shared calendar died from pinging. If every assignment goes to the group, Rakesh gets a message every time Priya assigns something to Tarun, on a bad signal, at the unit — and by Wednesday he mutes the group, which also mutes the one message that was for him. Replaced by: one message to the assignee, and one group digest a day |
| **X-5** | **Deleting anything.** Not tasks, not readings, not completion history | Archive is a view. Priya's laptop struggling is a reason to trim the *sheet mirror*, not a reason to lose the eight weeks Dev wants to count |
| **X-6** | **The Stock Watch sheet's vendor-payment tab, and "Sheet1 (do not delete)"** | Marigold's, not ours. We read a copy to understand the file; we write to one mirror tab and nothing else in it, ever |
| **X-7** | **Automatic assignment without Priya's confirmation** | The rule guesses; she agrees. Declined because she said the reason better than we could: being the one who assigns is how she knows what is going on |
| **X-8** | **"Under 3% of orders past SLA" as a devx acceptance criterion** | Declined as *ours*. It is Marigold's business target and it stays Marigold's, recorded as Dev's. What we are accountable for is that the number exists, is correct, is visible any day he wants it, and covers exactly the orders it claims to cover — see §7, A-3. We will not accept a criterion whose outcome depends on how fast Tarun answers his phone |
| **X-9** | **Success test 1 as written in the BRD** | Declined as an instrument, in the meeting, with Dev's agreement. As written it compares the count of products that crossed their floor against the count of tasks raised — and the only thing that can count crossings is the same component that raises tasks, so a missed crossing is missing from both sides and the two numbers match perfectly. It passes hardest in exactly the case Dev is afraid of. Replaced by the independent reading ledger, P1-9, which gives the comparison two sides |
| **X-10** | **High depth, and the two things it would have bought that we cannot yet operate** | Declined by devx, not by Marigold. See §4.3. We will not price a written commitment as a running check |
| **X-11** | **A load test and a restore drill** | Not in Standard depth's release check. Named here because "it survives Diwali" is a real worry and this document should not leave the impression we tested it. What we do instead: an agreed API read budget against the store before the freeze, §6 row N-5. If Marigold wants either, it is a change request and it is priceable |
| **X-12** | **Returns and refunds, in any form** | Marigold's section 16, raised and withdrawn by Priya in her own document. Nobody reopened it |
| **X-13** | **Anything that emails, messages or is visible to a Marigold customer** | Marigold's section 16. The board is internal. This also matters to the freeze — see §6 row N-6 |
| **X-14** | **Barcode scanning, or anything that changes what Rakesh physically does on the floor** | Marigold's section 16 |
| **X-15** | **Purchasing, forecasting, vendor purchase orders, and anything touching Marigold's accounts or vendor payments** | Marigold's section 16. A task may say "call Kalyan Ceramics about the grey bowls". Nothing more |
| **X-16** | **Replacing Shopify, or moving anything off it** | Marigold's section 16. Shopify stays the system of record, and customer data stays where it is already governed |
| **X-17** | **Any integration with the Leicester 3PL's own systems** | We read what the 3PL puts into Shopify. We do not connect to them. If what they put into Shopify is too late to be useful, that is D-1's consequence, not a new integration |
| **X-18** | **Retiring the Monday export Tarun runs** | Nobody asked and nobody thought to ask. Flagged rather than assumed: it may become unnecessary, and we are not promising that it does |
| **X-19** | **Support, on-call, or anyone answering at 23:00 on 23 November** | Not in this scope unless §11.4 is bought. If it is not bought, **8 October is a handover, not a go-live**, and we will say that out loud on the day rather than let it be discovered |
| **X-20** | **Training the two Diwali temps** | Their accounts are in scope, individually named, same permissions. Someone teaching them is not. Dev's own success test says one of his four should be able to teach it in fifteen minutes; that test is about the product, and it is his to judge |

---

## 4. Depth: **Standard**

Depth is how much apparatus the work carries. It is set by **what a mistake costs** — not by budget, not by SKU count, not by how important the project feels. Four questions set it, and Marigold should be able to argue with each answer.

### 4.1 The four questions, answered for this project

| Question | Answer here |
|---|---|
| **What breaks, and who feels it?** | Marigold's own staff. The board is internal; no Marigold customer can reach it or see it. The worst realistic failure is a task nobody sees — which is what happens today, every day, in a WhatsApp group |
| **Can it be undone?** | In phase 1, yes. The board only reads from Shopify, so a bug cannot change stock, cancel an order or edit a product. A bad screen is redeployed. In phase 2, one thing cannot be undone: a reminder that has been sent |
| **Does it touch money, or sensitive or regulated data?** | No money. No customer personal data ingested from Shopify. It does hold **staff personal data** — four to seven people's names and phone numbers, and a record of what each of them did and when, including the reopen statistics in P1-16 |
| **How long will it live?** | Years. This replaces a paper list and a group chat, so it is not a two-week demo and the documentation and tests should assume a new person reading them in 2028 |

### 4.2 Why not Light

Light is for work where a mistake costs nothing to undo and there is no personal data. Two things rule it out. It holds staff personal data with a monitoring purpose attached, which creates duties even on a day when nothing is broken. And it will live for years, which is what makes a missing test expensive later rather than never.

There is a second reason, and it is the one worth reading. Light is not the same product with fewer checks. Our own observation on an internal pilot, on a sample of fifteen requirements in one session: requirements that named a config file, a hook or a test behind them arrived **8 times out of 8**; requirements written only as prose arrived **0 times out of 7**. The admin panel in that pilot shipped nine write paths and zero buttons — the write side existed at every layer except the one a person clicks — because the check it was given could only see whether a page rendered, and a page with no Create button renders perfectly. That is a count on a small sample and it is **not a prediction about Marigold's project**. What it changed is how we write acceptance criteria, which is §7. Choosing Light here would mean choosing to receive less than was specified, in a shape nobody predicted, on a board whose whole point is a screen people type into.

### 4.3 Why not High

High is where money moves, or where something cannot be undone. Neither is true of phase 1.

If Marigold bought High anyway, three of the things it adds are real and we can operate them: a second environment and its running cost, a second named approver on anything touching the dangerous paths, and a load test plus a restore drill with the restore time written down. **Two of them are not.** Mutation testing — checking that the tests would actually fail if the code were wrong — and a full audit trail of who changed what are *to build* on our side: no tool, no threshold and no settled definition of what counts as core logic. Buying High today would mean paying for a written commitment on those two rather than a running check, and we are not selling that.

So: **Standard**, with one exception carried forward — **phase 2's notification path is treated as a dangerous path when we reach it**, because a message that has been sent cannot be unsent. That means a second reviewer on it, and send-once behaviour named as a criterion with an artefact.

### 4.4 What Standard buys, and what High would have cost

| | **Standard — what Marigold gets** | **High — declined** |
|---|---|---|
| Required checks before any merge | size, gate-change, spec-ancestry, verify, review | the same five |
| Approving reviews | 1, plus code-owner review on protected paths | 2 on protected paths |
| Coverage on the lines a change touched | 80% | 80% plus mutation testing — **to build** |
| Environments | dev and uat | plus production defined in code before it is provisioned |
| Monitoring | errors grouped with the release that introduced them, searchable logs with personal data stripped before they leave the application, alarms on error rate, p95, p99, saturation, and the four that get forgotten on anything scheduled: it did not start, it processed zero rows, it ran twice, the dead-letter queue is not empty | plus a full audit trail of who changed what — **to build** |
| Data outside production | invented data only. See §10.5 | the same, plus any dry run on live records under production's own access controls |
| Release check | the standing list, with the third column | plus load test, threat model, restore drill with the time recorded |
| Launch and after | the checklist; support per §11.4 | rehearsed launch, someone on call, a runbook per alert |
| **Indicative price effect** | included in §11 | **+₹2.5–3.5 lakh on phase 1, and +₹12,000–18,000 a month running** — against a ₹35,000 ceiling. Two of its rows would be commitments, not checks |

Depth is re-checked if the answers change. It goes up with them and it never quietly goes down. The obvious trigger here is phase 2 asking for a write to the store: that is a different answer to question two, and it changes this section.

---

## 5. What we check before anything ships — and the honest status of it

### 5.1 What we do, in plain language

Agents write most of the code on this engagement. That is stated plainly in §10 and it is why this section exists at all: when generation gets cheap and checking does not, the thing worth buying is the checking.

- **One repository, in Marigold's organisation, from the first commit.** Nothing is pushed straight to the main branch. Every piece of work gets its own branch and its own pull request.
- **Intent is written down before the code exists, and it cannot be back-dated.** Each piece of work starts with a short spec that a person approves, and that spec has to be the branch's first commit and an ancestor of every code commit on it. A branch where the code came first cannot be made to look otherwise.
- **A change cannot quietly weaken the things that check it.** If a pull request edits an existing test, a coverage threshold, the pipeline configuration or the acceptance criteria, that edit has to sit in its own commit where a reviewer can see it. It cannot ride inside a change to the product.
- **Small pieces.** A pull request warns above 300 changed lines or 10 files and fails above 400 or 20. Going over is a person's decision, taken by someone other than the author. The reason is not tidiness: on large diffs, reviewers skim, and skimming and reviewing look identical afterwards.
- **Format, lint, types, tests and build run as one command**, locally and again on the server, and that command **fails rather than skips** when something is not wired. A repository that documents six checks and runs four reports green for the two that never ran.
- **80% coverage on the lines this change touched** — not on the whole repository. A whole-repository number is one you inherited; a changed-lines number is one you earned.
- **A fresh agent session reviews every diff** with no memory of having written it, and every finding it raises ends either fixed or dismissed in writing. Never neither.
- **A second human on the paths where being wrong is expensive**: personal data, permissions and authorisation, the notification path in phase 2, database migrations, the pipeline configuration, existing tests, coverage thresholds, and the acceptance criteria themselves. An agent may propose a change to a criterion; only a named person approves one, or criteria become a description of whatever got built.
- **Secrets and known vulnerabilities are scanned on a clock**, over the whole tree, not only on the diff — because an issue introduced by a change that passed is invisible to anything that only reads new changes.
- **One job asks the hosting platform what it actually enforces and fails when that stops matching what this document claims.** This is the check that makes the other checks' claims honest. Our own pilot's context file asserted that its main branch was protected; there was no remote and the pipeline had run zero times.
- **No developer or agent session holds production credentials.** The session cannot reach production because the credential does not exist in it. That is not an instruction to the agent; it is an absence.
- **A weekly demo of working software.** Wednesdays, 09:30 IST, 30 minutes, recorded, avoiding Dev's Tuesday and Thursday afternoons. Software doing something, not a deck and not a percentage complete.

### 5.2 The honest status of every one of them

Read the status words literally.

- **Written** — the file exists and its logic has been exercised away from a live host.
- **Proven** — it has run on a host **and failed something it was supposed to fail**.
- **To build** — it protects nothing today.

**Nothing in this table says *proven*, and that is not modesty.** Our process has not run end to end on a host. What exists on Marigold's project today is nothing at all, because the repository does not exist yet; the middle column is therefore what it becomes at Setup, and the right-hand column is the honest state of the mechanism itself, on our side, on 6 August 2026.

| What it does | On Marigold's project | Status of the mechanism |
|---|---|---|
| Rejects a pull request over the size ceiling | at Setup | **written.** Its logic was run against 30 deliberately broken cases away from a host; it rejected what it was meant to reject, discriminated between the cases, and found a real defect in our own code doing it. It has never blocked a merge on a live host |
| Requires an approved spec as the branch's first commit | at Setup | **written**, same harness, same limitation. No check proves a spec was *read* |
| Forces a gate change into its own commit | at Setup | **written**, same harness, same limitation |
| Format, lint, types, tests, build as one entry point | at Setup, wired to this stack | **written — and deliberately fails while unwired.** Wiring it to this project's stack is Setup work, not a given |
| 80% coverage on changed lines | at Setup | **written.** It skips when no coverage report is produced, which is a hole we will close during Setup rather than describe as closed |
| A fresh session reviews every diff | at Setup | **written — and fails rather than passing when it is not configured**, because a review job that quietly does nothing shows a green tick for work nobody read |
| Every review finding ends fixed or dismissed in writing | at Setup | **written**, enforced by the host's own setting rather than by us |
| Second human on protected paths | at Setup | **written.** Depends on the ownership file's patterns matching this project's real folders — a pattern that matches nothing is owned by nobody while still reading as protected |
| Nothing pushed straight to the main branch | at Setup | **to build, per repository.** It is a setting on Marigold's repository, and it has to be turned on and then tested |
| The host's real configuration matches this document | at Setup | **written — untestable until it has run once against a real repository** |
| Secret scanning over history, daily | at Setup | **written**; the host's own push rejection is **to build** |
| Dependency and code scanning, daily | at Setup | **written**; needs the host's alerts switched on, which is Setup work with an owner |
| Checking that the tests would fail if the code were wrong (mutation testing) | not planned | **to build.** No tool, no threshold. This is one of the two rows that made us decline High |
| A full audit trail of who changed what | not planned at Standard | **to build.** The other one |
| Ticket status derived from what happened rather than written by an agent | at Setup, by hand at first | **to build** as an integration. Until it exists, the tech lead records it manually. An agent will write to any completion signal it is given; our own pilot marked its own work done |

### 5.3 The one place this stops being a written claim

Setup does not end when the files are in place. It ends with three things Marigold can look at:

1. One trivial page — a build identifier and nothing else — **live in dev, put there by the real pipeline**, with the build id matching a tagged commit and a pipeline run.
2. The job that reads the host's configuration back has run on the host and passed, with a link to the run.
3. **One throwaway pull request has been deliberately blocked by a check**, with a link to the run that blocked it.

The third is the one that matters. Until a check has been watched failing, we have tested that it runs, not that it stops anything — the same way a backup nobody has restored is a belief. **When those three exist, we will re-issue the table in §5.2 with the rows that moved and the run links against them.** That is the only route from *written* to *proven* on this project, and it happens before the first feature ticket, not after the freeze.

Setup is also the stage that gets cut when a timeline slips, and it is the worst possible thing to cut: every standard added later leaves everything written before it unchecked, and that debt appears in no diff. If the 25 September date comes under pressure, **features come out of phase 1 and Setup stays**. That is a commitment in this document, not a preference.

---

## 6. What we will **not** verify, and how Marigold will know

Every release hands Marigold a document with three columns: what was checked, how, and the artefact that proves it. A fourth section on the same page says **what this release does not verify**. Nobody volunteers that section, which is exactly why it is in the template — someone reads that file during an incident, and the useful half is the half about what nobody looked at.

Some of these are known today and can be written down before a line of code exists.

| # | What will not be verified | How Marigold will know |
|---|---|---|
| **N-1** | **Nothing we build can see a change made inside the Shopify admin.** If someone edits a product, a price or an inventory count in Shopify itself, our board finds out next time it asks. This is a hole, not a design choice | Named in every release document for the life of the engagement, and named here. Phase 2's live feed narrows it; it does not close it, because a live feed can be missed or delayed |
| **N-2** | **Anything that dips below its floor and recovers between two readings did not happen, as far as the board is concerned.** Priya's brass candle holders on a Saturday are exactly this shape | The reading ledger, P1-9, makes the gap *visible*: the interval between readings is in the data, so the number Dev takes in November arrives with its own error bar instead of pretending it has none. The interval itself is D-3 in §8 |
| **N-3** | **We do not verify that a UK order's dispatch clock is accurate** unless D-1 resolves in time. The 3PL's fulfilment event is what stops the clock, and nobody at Marigold can say when it arrives | If D-1 slips, phase 1's late-order signal covers India-warehouse orders only, the board says so on the screen, and it is a signed scope note rather than an October discovery |
| **N-4** | **We do not verify that a WhatsApp message was delivered to a phone, or read.** Patchy signal at the unit, an old handset and a muted app are outside anything we can check | The board is the record. A message is a convenience. If a task's only existence is a message, we have rebuilt the group chat |
| **N-5** | **We do not verify how the board behaves under Diwali load.** A load test is not in Standard depth and is not being bought — X-11 | Instead: an agreed budget for how often we read the store, fixed in writing before 8 October, so the one way an internal tool can hurt Marigold's customers — hammering the store's API during Black Friday — is bounded by a number both sides agreed |
| **N-6** | **Marigold's freeze does not literally cover this board**, because the freeze is written about things customers can reach and the board is internal. We do not think that was intended | Made explicit instead: no feature deploys after 8 October; a defect fix inside 8 October – 5 December needs Dev's sign-off per fix; and the read budget above |
| **N-7** | **We cannot cheaply verify that a test and the code are not sharing the same misunderstanding.** Both are written by the same kind of session, so a wrong test and a wrong implementation can agree and both look green | Partial answer, stated as partial: on the parts that matter, expected values are computed by hand rather than by the thing that wrote the code. No standard we have read solves this at reasonable cost, and we are not claiming to |
| **N-8** | **We cannot verify that agent-written code contains nothing that reproduces third-party code.** No licence-compatibility check, no copyleft check, no verbatim-reproduction detection | §10.3, and it is the reason we cannot sign Marigold's originality warranty as written |
| **N-9** | **We do not verify Marigold's business outcomes.** Not the under-3% target, not the 90 minutes a day, not the fifteen-minute teach test | X-8. We verify that the numbers those judgements need exist, are correct, and cover what they claim to cover. The judgement is Marigold's |
| **N-10** | **What a person types into a free-text task is not verified or filtered.** See §10.4 | Stated in §10.4 rather than promised away |

---

## 7. How the work is accepted

The rule that carries the most weight in this document: **every acceptance criterion names the artefact that will prove it.** A criterion with prose in that column fails a release rather than passing it. "Verified" is not evidence, and neither is "we tested it manually".

The criteria live in the repository on a protected path with named owners. An agent may propose a change to one. Only a named person approves one. Criteria an agent can edit to match what it built are not criteria.

### 7.1 Phase 1

| # | Criterion | The artefact that proves it |
|---|---|---|
| **A-1** | A product whose stock crosses below its floor produces exactly one open task, with the product, the reading and the time on it | An automated test over a captured store response, plus a screenshot of the board taken after a real crossing on Marigold's store during the pre-window fortnight, with the matching row from the reading ledger beside it |
| **A-2** | The same product staying below its floor across several readings does not produce a second task while the first is open | Automated test with a sequence of readings; the ledger extract showing the readings that were taken |
| **A-3** | The count of orders past dispatch promise is correct, visible any day, and covers exactly the orders it claims to cover | A query, committed in the repository, run against Marigold's real orders, with its output next to the same count computed by hand from a Shopify order export for the same day and the two agreeing. The screen states in words which orders it covers — India only, or India and UK |
| **A-4** | Priya can assign a task to one person, and no task acquires a name any other way | A browser test that drives the actual screen: opens an unassigned task, sees the proposed name, confirms it, and sees it assigned. Plus a test asserting that no task reaches assigned state without a confirming user id |
| **A-5** | The assignee, and only the assignee, is messaged on assignment | A test capturing outbound messages for a five-person fixture and asserting exactly one recipient, plus a screenshot of the message as it arrives on a phone |
| **A-6** | A person can complete a task; the completion records who and when; Priya can put it back; both events survive | A browser test performing complete-then-reopen, plus the two database rows it produced |
| **A-7** | Rakesh can do a full day's work — see the board, complete his own tasks — on his own device | A recorded browser session against the device profile from A-8, plus one screenshot from Rakesh's actual handset taken by a named person during the pre-window fortnight |
| **A-8** | Floors: ~60 authored by hand, every other product covered by its category default, 200 new SKUs inheriting automatically | A query showing every product resolving to a floor and where each came from, run before and after a batch of new SKUs is created |
| **A-9** | Bulk edit changes forty floors in one submission and reports what it changed | A browser test that submits forty changes and asserts forty rows changed, plus the screen's own confirmation output |
| **A-10** | The reading ledger is append-only, never edited and never archived | A test asserting that update and delete against that table fail, plus the migration itself under code-owner review |
| **A-11** | Permissions: everyone sees every task; only the assignee or Priya completes; only Priya or her backup assigns or reopens; temps have the same shape under individually named accounts | One test per role per action, listed exhaustively rather than as "permissions work", plus a browser test where a temp account attempts to complete someone else's task and is refused |
| **A-12** | Marigold owns the repository, the hosting and every third-party account | Screenshots of the ownership pages, and one page live in dev put there by the pipeline with its build id matching a tagged commit |
| **A-13** | Floors typed in the sheet arrive on the board on an explicit import, and the board reads back what it understood | A browser test importing a fixture sheet containing one deliberately malformed value, and the read-back screen showing it |
| **A-14** | The mirror tab is written by the machine, and no cell in it is a source of truth | The written sheet after a run, and a test asserting the import path reads only the floors range |
| **A-15** | The 08:00 digest is sent once a day, lists what is outstanding and who has it, and goes nowhere else | A test asserting one send per day for a fixture, plus a screenshot of a real digest. Channel per D-2 |
| **A-16** | Completed tasks leave the screen after seven days and remain queryable | A browser test with dated fixtures, plus a query returning the hidden rows |
| **A-17** | The reopen view reports, for a chosen week, what was marked done and later put back, by person | The view's output next to the same figures computed by hand from the underlying rows for that week |

### 7.2 Phase 2

| # | Criterion | The artefact that proves it |
|---|---|---|
| **A-18** | A due date set by Priya displays as the correct local moment to a user in India and to a user in the UK, including across a UK clock change | A test table of cases with expected values **computed by hand**, plus two screenshots of the same task under two timezone profiles |
| **A-19** | A reminder is sent once and only once, including when the sender is retried or runs twice | A test that invokes the send path twice and asserts one message; the idempotency record it wrote |
| **A-20** | No reminder is sent for a task already completed | A test with a completion landing between scheduling and sending |
| **A-21** | A live signal from the store produces a task, and a signal that arrives twice does not produce two | A test against a captured payload replayed twice, plus the ledger rows distinguishing live from scheduled |
| **A-22** | A live signal that is missed or delayed is visible rather than silent | An alarm that fires when no signal has arrived for longer than its expected interval, with the alarm's own test run |

**A release is accepted when every criterion in it has a non-empty artefact column and the release document's "what this does not verify" section is written.** An empty artefact cell is not a small omission; it is the specific failure this whole section exists to prevent.

---

## 8. Assumptions, dependencies, and what we need from Marigold

### 8.1 Decisions still open at the time of writing

Each has an owner, a date, what it blocks and what happens if it slips. These are not caveats; they are the shape of the plan.

| # | Open question | Owner | Needed by | If it slips |
|---|---|---|---|---|
| **D-1** | Does the Leicester 3PL push fulfilment events into Shopify, at what delay, per order or in a daily lump? Measured against ~90 real UK orders, not taken on the 3PL's word | Priya Menon (facts and a named contact) with Karan Iyer (measurement, once read access exists) | **Fri 14 Aug 2026** | **Phase 1's late-order signal covers India-warehouse orders only; UK moves to phase 2.** Accepted by both sides in the meeting. Signed as a scope note, not discovered in October |
| **D-2** | Can the WhatsApp business API address a group at all, what does a message cost, and what do its template rules allow? Karan believes it sends only to individual numbers against pre-approved templates and declined to state that as fact from memory | Karan Iyer | **Mon 11 Aug 2026** | The 08:00 digest becomes a set of individual messages or moves to another channel. The messaging line in the running-cost estimate stays marked as an estimate, with the reason |
| **D-3** | How often do we read inventory from the store, and what does the residual blind window mean for the November verdict? | Karan Iyer, with Dev on the cost and rate-limit trade | **Mon 11 Aug 2026, in this document's v1.0** | The November number ships without a stated blind window — which is exactly the kind of unqualified figure Marigold's BRD rejects |
| **D-4** | Is Farhan Qureshi content to be the named backup for board-behaviour decisions, on the same response time? He was not in the meeting | Dev Rawat, in writing | **Fri 15 Aug 2026** | Priya is the sole decision-maker with no backup, and a warehouse day or a day of leave becomes a delivery stall |
| **D-5** | Our own written position on what an agent may **read** and transmit, checked against Marigold's data processing agreement | Karan Iyer | draft **Mon 18 Aug 2026**, and **before the first upload** | Nothing of Marigold's is uploaded. Work that does not need their material proceeds; anything that does, waits. See §10.2 |
| **D-6** | Whether Marigold's originality warranty can be signed in a qualified form, and in what words | Dev Rawat, with his adviser; Karan supplies what we do and do not check | **before signature** | Signature slips, or the clause is carved out. Not a technical decision and not ours to make |
| **D-7** | Which after-go-live option Marigold buys | Anjali Sharma to price (§11.4); Dev Rawat to decide | **before signature** | 8 October is a handover, said out loud on the day |
| **D-8** | Can Rakesh's actual handset run this? Nobody has looked at the phone | Priya Menon (make, model, OS version); Karan to check | **Fri 22 Aug 2026** | The device and browser floor is set from assumption, and if the phone fails it the fix arrives after the screens were built against the wrong baseline |
| **D-9** | What "closed in the tool" counts as, when the tick is on the board and the real work happens in Shopify | Priya Menon with Anjali Sharma, in the design document | **at Kickoff** | Dev's third success test is judged on a definition nobody agreed, which is how a verdict becomes an argument |
| **D-10** | Marigold's obligations on holding staff performance data | Dev Rawat, with his adviser | **before signature** | The reopen report ships with a conservative default retention and is revisited |

### 8.2 What we need from Marigold, and by when

| # | What | Owner | By | What it gates |
|---|---|---|---|---|
| **C-1** | **Read-only Shopify access**: a custom app created by Dev in his own admin, read scopes only (products, inventory, orders, fulfilments, locations), token handed over out of band and held in Marigold's secrets manager | Dev Rawat | **Mon 11 Aug 2026** | Everything in S-1, and therefore the answer to D-1 and any date we can stand behind |
| **C-2** | The 3PL contact and their integration facts | Priya Menon | Fri 14 Aug 2026 | D-1 |
| **C-3** | Farhan's written agreement to be named backup | Dev Rawat | Fri 15 Aug 2026 | The Kickoff working agreement — it cannot name a backup who has not agreed |
| **C-4** | Rakesh's handset make, model and OS version | Priya Menon | Fri 22 Aug 2026 | D-8, the device floor |
| **C-5** | A copy of the Stock Watch sheet, including "Sheet1 (do not delete)" | Priya Menon | with Kickoff | The import and mirror design. We want to see what is in the file before writing anything near it |
| **C-6** | **Priya's afternoon on the ~60 moving SKUs' floors.** Not before Kickoff, but on the critical path and named as such | Priya Menon | **inside the first fortnight of build** | The board cannot raise a single stock task for a product with no floor. If this lands in late September, the 25th has nothing to demonstrate |
| **C-7** | Written reply to Annexe A naming the model provider, its retention terms and its processing region | Dev Rawat | before any upload | Any drafting work on Marigold's material |
| **C-8** | Dev to start Anjali Sen and Ravi Menon on the money question **the day this document lands**, not the day he wants to sign | Dev Rawat | Mon 11 Aug 2026 | The signature date, and therefore the start date, and therefore 25 September |
| **C-9** | Named accounts and phone numbers for all users, including the two Diwali temps before they start | Priya Menon | rolling | P1-8, A-11, and the staff inventory in §10.4 |
| **C-10** | Two hours a week from Priya through build, plus the Wednesday demo | Priya Menon | weekly | Everything. She is the decision-maker on behaviour |

### 8.3 Assumptions

Stated so that a wrong one is a change request rather than an argument.

1. The warehouse is in **Bhiwandi**. The Pune reference in the BRD was the vendor cluster.
2. Users at go-live: **Priya, Tarun, Rakesh, Anjali (care)**; **Farhan** from September; **two named temp accounts** in November. **Seven by mid-November, not four.**
3. Shopify remains the system of record for products, inventory and orders, and remains where customer data lives and is governed.
4. Shopify's own read APIs, rate limits and event behaviour do not change materially during the engagement.
5. The dispatch clock starts when an order is paid and stops when it is marked fulfilled, both as recorded in Shopify.
6. Marigold's published promises are 48 hours to dispatch for India and 3–5 days for the UK, and those figures do not change mid-engagement without a change request.
7. Everyone sees every task. If that changes to per-team visibility, the permission model changes, and the permission model is the one shape everything else sits on.
8. Nothing is deleted in either phase.
9. Hosting is in a region Marigold's adviser is content with; the region is named in the design document before anything is provisioned.
10. Marigold has, or will nominate, an adviser for the two legal questions in D-6 and D-10. We will not give a legal opinion on either.
11. The estimate that running cost fits inside ₹35,000 a month holds only with D-2 and D-3 answered. Until then, §11.3's message line is an estimate and is labelled as one.

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
| **What Marigold accepts** — any change to an acceptance criterion | Priya proposes; **Anjali Sharma** routes it; a devx code owner approves the change in the repository | — |

### 9.2 Agreed response times

| Who | Their commitment |
|---|---|
| **Priya** | Same working day if it reaches her before 18:00 IST |
| **Dev** | Small decisions inside his 09:30 and 21:00 IST windows, about four hours. Anything needing thought, 24–48 hours. **Not Tuesdays or Thursdays 11:00–18:00 IST.** **12 October – 30 November: three to four working days** for anything not on fire |
| **Money over ₹1.5 lakh** | Plus Anjali Sen, London: two working days, three across her Friday |
| **Money over ₹5 lakh** | Plus Ravi Menon: **one week, not compressible** |
| **devx labs** | Anything Marigold asks: same working day. Anything we owe with a date on it: that date, or a message before it saying why not |

**The rule both sides agreed:** any money decision is raised in the week it is first foreseen. One raised in week five that was visible in week two gets a no on principle, even where a yes was available in week two. **The fee in §11 is itself over ₹5 lakh, so it takes the Ravi Menon path** — which is why this document arrives on the 11th rather than the 15th.

### 9.3 What happens to the timeline when an answer is late

| Situation | What we do | What it costs |
|---|---|---|
| An answer we need to keep building is late | We move to work that does not go stale: shared shapes, captured store responses committed as files, test scaffolding, project-specific tooling. We do **not** write specs for far-future work, because those describe a codebase that will not exist | Nothing, for about three days. Beyond that, dependent work slips **day for day**, and the slip is reported at the Wednesday demo with the waiting split into waiting-on-us and waiting-on-them |
| **D-1 unanswered on 14 August** | The UK late-order signal moves to phase 2 and the board says on screen what it covers | No date slip. A scope reduction Dev signs, per the agreement in the meeting |
| **C-1 (store access) late** | S-1 cannot start, so we cannot measure, so we cannot answer D-1, so the late-order signal has no agreed contract | The **most expensive single dependency in this document.** Every working day C-1 is late is a working day off the eighteen available before 25 September |
| **C-6 (Priya's floors) late** | Phase 1 demonstrates on category defaults only | The 25 September set exists but has little to raise a task about, which makes the pre-window fortnight a weaker test than it should be |
| Signature after 20 August | Kickoff and Setup shift with it. **Setup does not shrink** | Features come out of the 25 September set, named at the time, one working day of scope per working day of delay |
| Anything late inside 12 October – 30 November | Expected, and planned for at three to four working days | Deliberately nothing is scheduled to need Dev in that window except a defect-fix sign-off |

---

## 10. AI use on this engagement

### 10.1 What we do, stated plainly

**An agent writes most of the code on this engagement.** A person approves the plan before code exists, and a person judges the result. No line reaches Marigold's repository without passing the checks in §5, which Marigold can inspect in their own repository at any time.

**Marigold's material will be sent to a named third-party model provider.** The provider, its data retention terms and the region the processing happens in are named in **Annexe A**, which is issued with this document. **Nothing of Marigold's — not a document, not a line of code, not a store response — is uploaded until Dev has replied in writing that the annexe is acceptable, checked against Marigold's data processing agreement.** "We will confirm that later" is not available; Dev said so, and it is also our own rule.

*In this fictional document, Annexe A carries a placeholder where the real provider name, retention terms and region go. In a real engagement that placeholder is filled before the document is issued, because an unnamed provider makes this section unsignable.*

### 10.2 What our position does **not** yet cover

Naming this is not a disclaimer. A client document that hides a known gap is worse than one that names it, because the gap gets discovered at the worst possible moment and everything else in the document is re-read as marketing.

**The permission half is written. The read half is not.** We have the part Dev asked for: the provider is named, he signs, and until he signs nothing moves. What we have **not** finished writing down is what an agent may *read* and transmit — there is no per-engagement matrix saying these repositories yes, these logs no, production data never, checked line by line against a client's data processing agreement; no removal of personal data from prompts and session transcripts as a mechanism rather than a habit; and no stated position of our own on how long a provider retains a session or which region it sits in beyond what the provider's terms say. That is a known gap on our side, it is recorded as an open question in our own research, and it needs an answer **before** this engagement rather than during it.

What Marigold is therefore buying, and what closes it: **a written data-handling note for this engagement** — which repositories, which documents, what never enters a session, retention, region — delivered **before the first upload**, signed by Karan Iyer and by Dev. It is a Kickoff deliverable, it is D-5 in §8, and Karan owns it.

### 10.3 The originality warranty

**Marigold's standard clause — "all deliverables are original work, free of third-party intellectual property" — cannot be signed as written, and we are saying so before signature rather than after a dispute.**

We have no licence-compatibility scan, no copyleft check, and nothing that detects a generated block reproducing third-party code verbatim. So we cannot demonstrate originality on agent-written code. **A warranty we cannot stand behind is worse for Marigold than a qualified one**, because at the moment it matters they would be holding a promise nobody can test.

What we will put in front of Marigold's adviser instead: a qualified clause, plus a plain description of what we actually do — the code is reviewed by a fresh session and by a person, it arrives in pieces small enough for a person to read, and third-party dependencies are scanned for known vulnerabilities and kept current. **That is not the same thing as originality and we are not going to call it that.** D-6 is the path; it is Marigold's adviser's call, not ours.

### 10.4 Personal-data inventory

What the board holds, why, and for how long. This is the input to the logging rules and to the invented-data rule in §10.5, which is why it is written now rather than derived from the schema later — a schema records what we built, not what we were allowed to build.

| Data | Purpose | Held where | Retention |
|---|---|---|---|
| **Staff names** (4 rising to 7, including two temps) | Assignment, and showing who has what | Board database | For the life of the account, plus a period for the completion history below |
| **Staff phone numbers** | The message that a task landed on their name | Board database and, in transit, the messaging provider | Deleted when the account is closed. Temp numbers deleted at the end of the festive window |
| **Staff action history** — who assigned, who completed, who reopened, and when | Priya's ability to put a task back, and the reopen view in P1-16 | Board database | **The one row Marigold's adviser must set a number on.** Our conservative default is 24 months, per D-10 |
| **Reopen statistics per named person** | Priya's stated purpose: being able to hold something up in a conversation she has already had twice | Derived from the row above | As above |
| **Order numbers, SKUs, quantities, timestamps, dispatch clocks, assignee** | The work itself | Board database | For the life of the system |
| **Free-text task content** | A person describing a job in their own words | Board database and its backups | For the life of the system |
| **Customer names, email addresses, phone numbers, shipping addresses** | **Not ingested.** A task says "order 41892, dispatch clock at 39 hours". Whoever works it opens Shopify, where the data already is and is already governed | — | — |

Three things about this table are load-bearing.

**We will not write "the board holds no customer data", because that sentence is not true.** The board does not *ingest* customer data from Shopify, and it **can still receive customer data from a human being** — nobody can stop Priya typing *the lady in Pune called twice, her number is* into a free-text box, and a rule in a document does not stop a person typing. What we can do about it, and are doing: **that field never reaches our application logs, never reaches an error report, and never enters a model prompt.** What we cannot do, said plainly: **if it is typed, it is in the database and it is in the backups.** That is a smaller promise than Dev asked for. It is the one that is true.

**The staff data is the unambiguously personal dataset in this project**, and the reopen statistics are performance monitoring of a named employee. Marigold may have that; it is not a side effect nobody declared. It goes in this inventory with a purpose next to it, and **the people it is about are told it exists.** Priya's position, recorded: she would rather Tarun knew, because half the point is being able to hold something up. Marigold's obligations on it are D-10, for Marigold's adviser. Karan is not giving a legal opinion on a call and will not give one in this document.

**Request logs have personal data stripped before they leave the application** — an allowlist of fields, plus a test asserting the logger drops everything not on it. Stripping downstream would mean the data was already in a third party's storage.

### 10.5 Invented data, and no masking script

**Development and test environments carry invented customers only.** Not masked copies of real ones — invented.

Dev anticipated the usual answer and rejected it correctly: a masking script somebody has to remember to run is a script that gets skipped on the busy day, which is the day it matters. Our answer is not a better script. **There is nothing to skip, because the board's schema has no customer data in it to mask.** That is a stronger position than a masking rule, and it is only available because of the decision in X-1 and the inventory above.

---

## 11. Commercials

### 11.1 The fee

| | Range | Includes |
|---|---|---|
| **Phase 1** — S-1, S-2, Kickoff, Setup, the 25 September set, and P1-12 to P1-16 by 3 October | **₹12.5 – 14.5 lakh** | Discovery and measurement of the store, the design document, the perimeter and pipeline, all of §2.1, the acceptance artefacts in §7.1, the engagement data-handling note, weekly demos |
| **Phase 2** — December 2026 to January 2027 | **₹6.0 – 7.5 lakh** | All of §2.2, including the notification path treated as a dangerous path, and the artefacts in §7.2 |
| **Total** | **₹18.5 – 22.0 lakh** | Inside Marigold's ₹18–26 lakh envelope |

**Rework allowance, stated rather than implied: four engineering days per phase are included** for changes arising from our own misreading of an agreed criterion, and for the second attempt at anything the Wednesday demo shows we built to the wrong understanding. Those days are inside the price. They are not a change-request path and Marigold is not asked to approve them; they exist because assuming zero rework is how the first correction gets presented as a failure.

### 11.2 Why it is a range and not a single number

Dev asked for one number and gave us an eight-lakh envelope to put it in. What he is getting is a **three-and-a-half-lakh band, and an explanation** — which is a narrower commitment than the envelope and a more honest one than a point.

The reason is specific, not commercial hedging. **We have no measured baseline.** Our process has not run end to end on a real project, so we have no figure for how long a ticket takes under it, and no figure for what the agent spend on a ticket costs. Quoting to a precision we do not have is exactly how the first honest correction looks like a failure — and Marigold has already paid for eleven weeks of green status reports followed by an admin screen whose buttons did nothing. A number we would revise is worse than a band we will hold.

**The three lines we are least sure of**, which is what Dev asked for:

1. **The UK dispatch clock (D-1).** Whether the 3PL's fulfilment event is usable at all decides whether phase 1 has one late-order signal or two, and whether phase 2 inherits a piece of work nobody has scoped. This is the widest line in the estimate.
2. **The sheet import and mirror (P1-13, P1-14).** We have not opened the file. Four tabs, a fifth nobody understands, a vendor tab we must not touch, and three years of habits inside it. One direction per cell removes the dangerous half of Priya's original request; it does not tell us what is actually in the sheet.
3. **The message channel and its volume (D-2).** Karan will not quote a per-message cost from memory. Until Monday, both the build cost of the digest and the running cost line below are estimates, marked as such, for a stated reason.

### 11.3 Running cost, against the ₹35,000 a month ceiling

| Line | Estimate | Confidence |
|---|---|---|
| Hosting, dev and uat and the board itself | ₹9,000 – 14,000 | Reasonable. Sized to seven users and this read volume |
| Database, including backups | ₹4,000 – 7,000 | Reasonable |
| Error tracking, logs, alarms | ₹3,000 – 5,000 | Reasonable |
| **Messaging** | **₹4,000 – 9,000** | **Estimate, pending D-2.** Per-message pricing and whether the digest is one message or seven are both unresolved, and message volume is one of the two things that could break the ceiling |
| **Total** | **₹20,000 – 35,000** | The top of this band **is** Marigold's ceiling, which is why D-2 and D-3 are answered before signature and not after |

**If the architecture turns out to need more than ₹35,000 a month, Marigold hears it during solutioning, not at go-live.** That is Dev's condition and it is a reasonable one. The lever if it binds is how often we read the store (D-3), which trades directly against the blind window in §6, row N-2 — and that trade is Dev's to make with the numbers in front of him, not ours to make quietly.

### 11.4 After go-live — priced, so it exists as a decision

Nobody discussed this before the meeting. It is priced here because unpriced support does not exist, and if Marigold does not buy it then **8 October is a handover** and we will say that on the day.

| Option | What it is | Price |
|---|---|---|
| **A — Freeze-window cover, 8 Oct – 5 Dec** | A named person reachable in working hours, four-hour response inside the window; a defect fix prepared and taken to Dev for sign-off per fix, per §6 row N-6; alarms routed to a channel devx watches, so a failure is something Marigold is told about rather than finds | **₹1.6 lakh for the window** |
| **B — A plus out-of-hours** | As A, plus one named person and one named backup reachable outside working hours through the window, with a written note per alarm saying what to do about it | **₹2.9 lakh for the window** |
| **C — Ongoing, Dec 2026 – Feb 2027** | Next-working-day response, defect fixes inside the phase-2 rhythm, and the depth question re-asked at the end of it | **₹55,000 a month** |
| **D — Nothing** | 8 October is a handover. Marigold holds the repository, the accounts and the documents. Nobody is watching the alarms | **₹0**, and said out loud on the day |

There is no unbounded option. An open-ended support window either never ends or ends without anyone noticing.

### 11.5 Invoicing and the things Dev will not accept

- **Every hour invoiced maps to a ticket on a board Marigold can see.** No "QA phase" with no artefact behind it — that line item is the reason this bullet exists.
- **A weekly demo of working software, Wednesdays 09:30 IST, recorded.** Not a status deck, not a percentage complete. If a demo is skipped, the invoice for that week is Marigold's to question.
- **Named people, and no silent substitution.** §13.4 names them. If anyone changes, Marigold is told **before** they notice it from the commits.
- **Marigold owns everything from the first commit** — repository, hosting, every third-party account, in Marigold's name, on Marigold's card, with Dev as owner. Not ours with him added.
- **No percentage of defect reduction, velocity, or improvement of any kind appears anywhere in this document, and none will appear in any document we hand over.** If Marigold finds one, it is a mistake, and we would like it sent back.

---

## 12. Changing this mid-phase

Clients change their minds, and a process that treats that as a failure gets routed around. The path below is designed to be used, not to discourage use.

**One rule sits above the rest: a change that alters what Marigold accepts goes through the delivery lead and lands in the acceptance criteria before any code moves.** A criterion changed to match what got built is not a criterion.

| Step | What happens |
|---|---|
| **1. Say it** | To Anjali Sharma, at the Wednesday demo or in writing. No form. Nothing is refused for arriving informally |
| **2. We write it down and price it, within two working days** | What it changes, what comes out to make room if the date is fixed, what it costs, and which acceptance criteria change. One page |
| **3. Marigold decides, at the right level** | Behaviour: Priya, or Farhan. Money over ₹1.5 lakh: Dev plus Anjali Sen, two working days. Over ₹5 lakh: plus Ravi Menon, a week, not compressible. Anything touching customer data or store access: Dev alone |
| **4. It becomes real in the repository** | The criteria change on their protected path, approved by a named person and not by an agent. The design document changes. Both are commits Marigold can read |
| **5. It appears in the release document** | Including in the "what this does not verify" section, if the change moved something out of what we check |

**Three limits on the path:**

- **Money raised late gets a no on principle.** If a change with a money consequence was foreseeable in week two and arrives in week five, it gets a no even where a yes was available in week two. This is Dev's rule and we are adopting it, because the alternative is us absorbing his approval latency silently and then missing a date.
- **After 3 October (last merge) and through 5 December, no change is a feature change.** A defect fix inside that window needs Dev's sign-off per fix. Anything else is January.
- **A change cannot buy back time by removing Setup.** If a date is at risk, features come out. The perimeter stays. Every standard added later leaves everything written before it unchecked, and that debt appears in no diff and on no invoice.

---

## 13. Signatures

A signature on a document nobody can be held to is decoration. Each line below says what that person is answerable for.

### 13.1 For Marigold Living

**Dev Rawat, founder**

Signing for: the scope in §2 and §3 being the thing Marigold wants, including every declined item and its reason; the depth level in §4 and the price of the level above; the fee, the running-cost ceiling and the after-go-live option chosen in §11.4; the dependencies and dates in §8.2, and that a slip in them moves our dates as described in §9.3; **written acceptance of Annexe A's named model provider, its retention terms and its processing region**; and that the staff data in §10.4 is held with the purpose stated and that the people it is about are told.

Signature: ________________  Date: ____________

*Anjali Sen (co-founder) and Ravi Menon (accountant) are on the approval path for the fee per §9.2. Their approval is not a signature on this document.*

### 13.2 For devx labs — delivery

**Anjali Sharma, delivery lead**

Signing for: that this document says what was actually agreed in the meeting of 6 August 2026, including the parts Marigold did not want to hear; the dates, the price band and its stated reason, and the rework allowance; the working agreement in §9; that a change follows §12 and never arrives as a quietly edited criterion; that Marigold is told before a named person changes rather than after; and that if the after-go-live option is D, I say out loud on 8 October that this is a handover.

Signature: ________________  Date: ____________

### 13.3 For devx labs — technical

**Karan Iyer, tech lead**

Signing for: **every technical claim in this document being one I can stand behind, and every gap being named rather than smoothed.** Specifically — the depth level in §4 and the refusal to sell High while two of its rows are *to build*; the status of every row in §5.2, including that no row says *proven* and why; the list in §6 of what we will not verify, and that it goes into every release document; that the criteria in §7 each name an artefact and that a prose artefact fails the release; the honest position in §10.2 that our read-and-transmit policy is half written, and the engagement data-handling note that closes it, delivered before the first upload; the statement in §10.3 that I cannot demonstrate originality of agent-written code and will not sign a warranty saying I can; and that **no percentage improvement, no "proven" and no "guaranteed" appears in this document or in anything we hand Marigold.**

If I cannot stand behind a sentence here, it changes before this document is issued. That is what this signature is for.

Signature: ________________  Date: ____________

### 13.4 The named people

| Who | Role | Signs for |
|---|---|---|
| **Anjali Sharma** | Delivery lead | This document, the commercial frame, the working agreement |
| **Karan Iyer** | Tech lead | Every technical claim, the design document, the perimeter, and the engagement data-handling note. Also code owner on the protected paths |
| **Nikhil Barve** | Senior engineer, phases 1 and 2 | — |
| **Sneha Raut** | Engineer, phase 1 | — |
| **Imran Shaikh** | QA | The acceptance artefacts and the release document, including its third column and its "what this does not verify" section |
| **Deepa Kulkarni** | Engineer from outside this project | Second code owner on the protected paths, so a fortnight's leave cannot stall a merge |

If any of these people changes, Marigold is told before it shows up in the commit history.

---

### Version history

| Version | Date | What changed |
|---|---|---|
| **0.9 DRAFT** | 6 August 2026 | First draft from BRD v1.1 and the frozen discovery notes of the same day. **Not issued. Pending Karan Iyer's review and signature.** Open items at this version: Annexe A's provider placeholder, D-2 and D-3 (both due 11 August, both feeding §11.3), the after-go-live option in §11.4 undecided, and the single figures inside the §11.1 bands not yet fixed |
| 1.0 | intended 11 August 2026 | To be issued to Marigold with Karan's signature, Annexe A attached, D-2 and D-3 closed |

Where this document and the discovery meeting notes of 6 August 2026 disagree, **this document is the authority** — including on anything said in the recording that was later changed.

**FICTIONAL — see the notice at the top of this document.**