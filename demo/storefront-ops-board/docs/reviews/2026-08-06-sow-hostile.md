**HOSTILE REVIEW — BRD v1.1 and SOW v0.9 DRAFT (fictional engagement, Marigold Living / devx labs)**

Reviewed against `02-before-build.md`, `05-depth.md`, `17-artefacts.md`, `18-outcomes.md`, `19-first-run.md`, `research/open-questions.md`. Ranked by what the finding costs. The SOW is genuinely better than most — the disclosure discipline in §5.2, §6 and §10.2 is real. That makes the remaining holes more dangerous, not less, because the document has earned the reader's trust before it reaches them.

---

### 1. There is no production environment, and the SOW says so twice without noticing

§4.4: `| Environments | dev and uat | plus production defined in code before it is provisioned |`. §1: "Phase 1 is **usable by four real people on real orders** by 25 September 2026." A-12's artefact: "one page live in **dev** put there by the pipeline."

Standard depth as the SOW itself scopes it buys dev and uat. Nothing in §2, §7, §8 or §11 names a production environment, its region, who deploys to it, or a criterion proving the board is live where seven people will use it through 40% of annual revenue. §5.3's exit proof is a page in **dev**. The meeting agreed "last deploy on the 8th" — deploy to *what*.

Dev's §13 forbids, verbatim: *"We'll sort out production later. Whatever production needs gets decided before the freeze, not during it."* The SOW reproduces the freeze in N-6 and never names the thing being frozen. This also strands §5.1's correct rule — "No developer or agent session holds production credentials" — with no stated deploy identity, which means Option A's "defect fix prepared and taken to Dev" on 23 November has no described mechanism to reach users. **Highest cost: it is a whole environment, its running cost, and its IaC, absent from a fixed band whose top is the ceiling.**

### 2. Authentication is absent from scope, criteria and price

A-11 is exhaustive on *authorisation*. Nothing anywhere says how seven people — including two temps and a warehouse hand on a cheap phone on the public internet — log in. No auth outcome in §2, no criterion in §7, no line in §11, no D-row, no session policy, no account deactivation when a temp leaves (§10.4 promises "temp numbers deleted at the end of the festive window" with no deliverable behind it). `19-first-run.md` names auth as one of four protected-set surfaces the vehicle must touch; §5.1 lists "permissions and authorisation" as protected. A subsystem on the protected set is missing from a document whose entire pitch is that nothing unspecified gets built.

### 3. The 90-day review — the client's whole judgment framework — was dropped

BRD §5 is six tests taken "at 90 days from a late-August start… in late November." Meeting decision 7: "The 90-day review reports against it." The SOW contains **no 90-day review**: no date, no attendees, no agenda, no artefact, no consequence, no link to phase 2 scope or final payment. It survives only as N-9's disclaimer ("We do not verify Marigold's business outcomes").

So the meeting where this engagement is judged exists in no signed document. In late November, Dev holds six tests; devx holds seventeen satisfied criteria; nobody scheduled the conversation, and the freeze plus his own 3–4 day latency window is running. This is how a phase ends with an angry client while every criterion passed.

### 4. Real customer data reaches devx before devx's own data-handling note exists

C-1 hands over read-only store access **11 August**. S-1 measures "roughly **90 real UK orders**" immediately. D-5 — the engagement data-handling note, the thing that closes R1 — is drafted **18 August**. §10.5's invented-data rule covers "development and test environments"; S-1 is neither.

Shopify orders carry names, emails, phone numbers and shipping addresses. Dev's block 1 is "not in its database, not in its logs, and **not in any prompt, session transcript or file sent to a model provider.**" A-1's artefact is "an automated test over a **captured store response**", and the process's own fixture rule ("needed once, fetch it; needed again, commit it and read the file") pushes those captures into the repository permanently, where the review job in §5.1 transmits every diff containing them.

Nothing governs the S-1 dataset: where extracts live, whether they are redacted before capture, whether an agent session touches them, whether fixtures are synthesised from real payload *shapes* rather than real payloads. The SOW claims compliance with block 1 in §10.5 while its own §2.0 schedules the breach a week earlier. **Fix: a dated rule that S-1 extracts are field-limited at the query, held outside any agent-readable path, and that every committed fixture is a hand-synthesised shape — before C-1, not before Kickoff.**

### 5. Three phase-1 outcomes have no acceptance criterion, and one of them is the pilot's exact failure

Cross-check §2.1 against §7.1. Missing entirely:

- **P1-4** — "A person can add a task themselves, in their own words." No criterion. This is a screen a person types into, with no browser test naming it. `02-before-build.md`: *"the criterion for a screen names a browser test that clicks the button, or the button does not get built."* The pilot shipped nine write paths and zero buttons for precisely this reason, and §4.2 tells Marigold that story as a selling point three sections earlier. Priya said half her day is neither stock nor orders.
- **P1-3** — the *task* for a late order. A-3 proves a **count** is correct. No criterion proves a task appears.
- **P1-10** — "in under a minute without asking anyone." Dev's test 4, no criterion.
- **S-1 and S-2**, the two work items devx added to scope, have no criteria at all.

### 6. The dispatch clock has no calendar, and "3–5 days" is a range

Assumption 5: "starts when an order is paid and stops when it is marked fulfilled." Assumption 6: "48 hours… for India and **3–5 days** for the UK."

Which is the UK SLA — 3 or 5? Working days or elapsed? Does the India 48 hours run through Sundays, public holidays, and the Diwali days the warehouse is shut? An order paid 18:00 Friday before a holiday Monday is "breached" at 18:00 Sunday on an elapsed clock. Priya will look at that number once, disbelieve it, and stop looking — which is N-4's own failure mode and the shared calendar dying in a third costume. This undefined number is the basis of A-3, of Dev's test 2, and of the only signal the SOW claims for late orders. It is a one-line fix now and an unwinnable argument in November.

### 7. BRD §15 question 1 was dropped, and Assumption 3 contradicts it

Priya: *"How you would get the correct stock number. The site's number and the shelf's number disagree, and Rakesh will tell you the shelf is right."*

Not in the meeting notes. Not in the SOW. Not an assumption, not an exclusion, not a D-row. Instead, Assumption 3: "Shopify remains the system of record for products, inventory and orders" — the SOW resolves her stated open question in devx's favour, silently, in an assumptions list. The entire stock-floor signal fires off a number she has told you in writing is wrong. Reconciliation is legitimately out of scope; the *risk* is not, and it belongs in §6 next to N-1 and N-2 where a founder will read it.

### 8. §10.4 makes a promise §10.2 says devx cannot keep, and Karan signs both

§10.4: the free-text field "never reaches our application logs, never reaches an error report, and **never enters a model prompt.**"
§10.2: "**no removal of personal data from prompts and session transcripts as a mechanism rather than a habit.**"

The logging half has a mechanism (allowlist plus a test). The prompt half has none, has no criterion in §7, and is the exact gap §10.2 discloses two pages earlier. §13.3 has Karan signing for "every technical claim in this document being one I can stand behind." This is the sentence the tech lead is supposed to catch. Either name the mechanism — the task table excluded from every agent-readable path, enforced by a test — or downgrade the sentence to what §10.2 admits.

### 9. Free-text task content leaves the system via WhatsApp, and the inventory says it does not

§10.4 places "Free-text task content" in "Board database and its backups." P1-12 sends the group "what is outstanding and who has it" — task titles, in Priya's words. P1-8 messages the assignee. So free text, which the SOW concedes may contain *"the lady in Pune called twice, her number is"*, is transmitted to Meta daily. The one load-bearing table in the document is wrong about its own data flow.

BRD §15 q8 asked two things: can the API do it, what does it cost, **and** "whether sending order numbers into a WhatsApp group is consistent with section 12." D-2 answers the first two and drops the third.

### 10. Depth: `05-depth.md`'s own table says personal data means High, and §4.3 never addresses it

The table: `When it applies | nothing to undo, no money, no personal data | real users, recoverable mistakes | **money, personal data, or cannot be undone**`.

§4.1 answers the sensitive-data question: "It **does** hold staff personal data… including the reopen statistics." §4.2 then uses exactly that fact to rule out Light. §4.3 rules out High on money and reversibility only, and never returns to the fact it just relied on. §4.1's reversibility argument is also about *deploys* — "a bad screen is redeployed" — and never asks the disclosure question, which is the irreversible one for a personal-data store on the public internet.

Karan's reasoning may well be right, but the SOW must argue *against the table's wording* rather than around it, because Marigold's adviser reads D-10 with that table in front of them. The stakes are not academic: three of the things this project visibly lacks — production defined in code, a restore drill with a recorded time, a load test before Diwali — are the High column.

### 11. Test 2 cannot move, and the SOW never says why

P1-3 raises a task **when an order passes** its promise. Phase 1 contains no due dates and no reminders (P2-1, P2-2, December). So nothing in phase 1 tells anyone an order is *about* to be late. Dev asked the question directly — BRD §11 contradiction 4: *"I do not know if test 2 is fair against phase 1 alone. Tell me what it is fair to measure."* The SOW's answer is X-8 and N-9: the 3% is your target, not our criterion.

That is a disclaimer, not an answer, and it is the one contradiction he explicitly asked to be told about. The honest sentence — *phase 1 makes the number exist and trustworthy; it cannot be expected to reduce it, because it only fires after the breach; the mechanism that reduces it is phase 2* — is absent, and a pre-breach warning signal is a phase-1-sized thing nobody proposed. A competent adversary ships exactly P1-3 and the November number is unchanged.

### 12. WhatsApp's prerequisites have no dependency row, and they are Marigold-side and slow

D-2 asks whether the business API can address a group and what a message costs. It does not ask about the path to sending the first message at all: a WhatsApp Business Account, Meta business verification, a dedicated number, and **template pre-approval** — which Karan already suspects is required. Per P1-11 all of that must be in Marigold's name on Marigold's card. Business verification alone routinely runs weeks and can be rejected. There is no C-row, no owner, no date, and P1-8 — a 25 September commitment — depends on it.

### 13. The entire §5 perimeter sits on settings in a repository devx does not own, with no dependency row

§5.2: "Nothing pushed straight to the main branch | at Setup | **to build, per repository.** It is a setting on Marigold's repository." P1-11 puts the repo in Marigold's org on Marigold's card.

`19-first-run.md` lists five host-side ways this stalls, all of which now sit inside a third party's account and policy: runner availability, branch protection depending on the plan, a `CODEOWNERS` slug that resolves, required contexts that cannot be named before they run once, and `PERIMETER_TOKEN` needing a fine-grained token that some orgs block. Its own words: *"Discovering this after writing the SOW is worse than discovering it in the first ten minutes."* Zero of the five appear in §8.2. §11.3 has no line for the git host, CI minutes, or seats for six devx people. And §5.3's promise — "features come out of phase 1 and Setup stays" — converts each of these into days off the eighteen.

### 14. Marigold never accepts anything

§7: "**A release is accepted when** every criterion in it has a non-empty artefact column and the release document's 'what this does not verify' section is written."

Acceptance is a property of devx's own paperwork, signed by devx's QA. There is no client sign-off, no acceptance window, no rejection path, no deemed-acceptance clause, and no named Marigold signature on any release. For a founder whose last vendor delivered "a table that rendered beautifully and buttons that did nothing" with a QA line item and no artefact, this is the structural hole that most exactly reproduces his experience — dressed in better paperwork. Compounding it: §11.5 rests invoicing on "a ticket on a board Marigold can see", while §5.2's own last row marks ticket-status derivation **to build** and hand-maintained. A hand-maintained status board has the same evidentiary weight as the status reports he stopped believing.

### 15. The commercial half is missing, not just uncertain

Absent entirely: payment schedule, milestones, deposit, invoicing cadence, termination for convenience or cause, liability cap, IP assignment of the deliverable, confidentiality, governing law and jurisdiction (devx in India, Marigold selling into the UK), and a controller/processor agreement between Marigold and devx — §10.4 is an inventory, not an agreement, and devx processes staff personal data and, via free text, customer data. Dev asked "tell me what our obligations are on that."

Also missing: any mechanism converting scope reduction into price reduction. §11.2 calls D-1 "the widest line in the estimate"; if the UK signal moves to phase 2 on 14 August, nothing says the phase-1 number moves. And §11.1's "Total | ₹18.5 – 22.0 lakh | Inside Marigold's ₹18–26 lakh envelope" excludes §11.4 — real exposure with Option B is ~₹24.9 lakh, which the word "Total" hides. Separately, a *band* is unapprovable by Ravi Menon, who approves a number against the festive stock buy; v1.0 must carry the point or spend his week twice.

### 16. A-3's hand-check is the test-1 tautology one level down

"a query, committed in the repository, run against Marigold's real orders, with its output next to **the same count computed by hand from a Shopify order export for the same day** and the two agreeing."

Both sides read the same Shopify fulfilment timestamps. If the 3PL's event is late — the entire content of D-1 — the machine and the hand-count are late identically and agree perfectly. This verifies the SQL, not the clock, which is exactly the defect Karan correctly demolished in BRD test 1 at 10:11. The check that would work is against something outside Shopify: courier pickup scans or the 3PL's own timestamps for a sample.

Related, one level up: X-9 claims the reading ledger "gives the comparison two sides." It is independent of the *board*, not of the *reader*. If the reader does not run, there is no reading and no task, and the two counts agree again. §4.4's "job did not start / processed zero rows" alarms partly cover it — say that, and stop calling the sides independent.

### 17. Rakesh, who decides whether test 3 passes, is under-specified everywhere

- No offline or degraded-network outcome or criterion. BRD §10 states the requirement absolutely: *"His phone is old and cheap and the signal at the unit is patchy | Whatever this is, it works there or it does not work."* A-7 is "a recorded browser session against the device profile" plus one screenshot — passable on office wifi.
- A-7's only real-handset evidence is taken "during the pre-window fortnight," i.e. 25 September – 8 October: the criterion proving the hardest platform requirement can only be satisfied after last merge on 3 October, when failing it cannot be fixed.
- P1-1 says "subject to **A-8**" — A-8 is the stock-floors criterion. The device dependency is A-7/D-8. A wrong cross-reference in a scope row.
- No language or localisation decision anywhere, for a warehouse hand in Bhiwandi reading Priya's free text.

### 18. Anjali (care) gets her notifications in the middle of the UK night for three months

The BRD says she works UK evenings; that is why she hears from customers first. P1-12 sends the digest at **08:00 IST** — 02:30 in the UK. P1-8 fires when Priya assigns, i.e. IST working hours, i.e. UK small hours. Timezones are P2-1, December. There are no quiet hours in phase 1. The one person whose muting the app costs Marigold customers is the one the notification design was not written for, and X-4's own argument — "by Wednesday he mutes the group" — applies to her twice as hard.

---

### Smaller, cheap now, expensive later

- **No backup or restore commitment.** X-11 declines a restore *drill* as a High item, which lets the absence of backups hide. X-5 makes the board the sole record of the eight weeks Dev's verdict needs; §10.4 mentions "backups" only in passing. No RPO, no RTO, no restore path.
- **N-5's read budget has no owner, date or alarm.** It is the only control on the one way an internal tool can hurt customers during Black Friday, and it appears in four places without a D-number. §4.4's alarm list has no rate-limit or budget breach row.
- **No Shopify API version pinned.** Assumption 4 plus a hard no-deploy window 8 Oct – 5 Dec means a version sunset inside the window is unfixable by agreement.
- **No devx availability statement.** §9.2 promises "Anything Marigold asks: same working day" and Option A four-hour response through 8 Oct – 5 Dec — the Indian festive season, when devx's own team is on leave. No holiday calendar, no named cover.
- **§11.3 omits CI minutes, repo seats, the secrets manager, Sheets API, and the review job's model spend on Marigold's card** — the last being C1 in devx's own research — in a band whose top "**is** Marigold's ceiling."
- **The rework allowance appears in no meeting note.** "Four engineering days per phase are included" reads as generosity and functions as a cap on devx's remediation of its own misreadings, classified by devx (§12 step 2 routes pricing through Anjali Sharma). Frozen notes say the SOW wins, so Marigold acquires a term never discussed.
- **A-2 silently resolves Priya's open question 3** ("is that one thing on my list or two? … Or maybe I do, if nobody has done it") with no D-row and no decision record.
- **D-9 parks the definition behind Dev's test 3 in the design document** — a living, agent-drafted, devx-owned artefact per `17-artefacts.md`. Definitions that decide a verdict belong in `docs/design/criteria/` on the protected path, for exactly the reason §7 gives.
- **No designer, no design phase, no design acceptance, no design tokens.** `02-before-build.md` requires a design brief naming empty, loading, error, validation and every breakpoint, and client acceptance of the design before implementation tickets. The predecessor product died of being unpleasant to use.
- **No start-date baseline.** "By 25 September" has no stated signature or Kickoff date in §8.3; §9.3 only describes what happens "after 20 August."
- **Test 5 has no deliverable.** "One of my four can teach it to a new hire in fifteen minutes" — N-9 declines to verify it, X-20 declines to train, and there is no user documentation of any kind in §2 or §11.
- **Test 6 is arguably pre-failed.** N-9 declines to verify the 90 minutes; X-18 keeps Tarun's Monday export; P1-14 keeps the sheet alive as a mirror. The one success test belonging to the person who uses this daily has no criterion, an explicit non-verification, and two scope decisions pointing away from it.
- **§5.2's middle column says "at Setup" on nine rows.** The process requires three words — *written*, *proven*, *to build* — per project. "At Setup" is a commitment wearing a status's clothes, and a founder reads the right-hand column's "written" as "you have this." The preamble disclaims it; the table does not.
- **Priya is the single confirm-and-reopen point** with no age alarm on the unassigned pile and D-4 unresolved. During Diwali her button is the board's throughput limit, and Karan said so in the room; the SOW records neither the risk nor the cheap mitigation.
- **BRD test 3's roll-call clause is unaddressed.** "If there is still an 8am roll call in WhatsApp, this failed regardless of what the code does" — and P1-12 builds an 08:00 WhatsApp group message. Priya's distinction ("It is not a roll call if I am not asking anyone anything") is in the frozen notes and in no signed document.
- **N-4 over-disclaims.** The business API returns delivery status; disclaiming all knowledge of delivery discards a cheap send-failure alarm, and §4.4's alarm list has no notification-failure row.
- **Unstated: whether BRD v1.1 has already passed through a model.** Dev's condition attaches to "the first document," which devx received on 6 August and drafted from the same day. He will ask this in the first five minutes and the SOW has no sentence for it.

---

### What a competent adversary delivers while satisfying every word

A board polled nightly, served from **dev** (§4.4 buys no production), reachable by a shared link (no auth criterion exists), English-only, with no free-text task form (P1-4 has no criterion) and no late-order task (only A-3's count). Every artefact in §7.1 is satisfied with committed fixtures, one screenshot per row, and a single agreeing hand-count on a day of devx's choosing. Rakesh's criterion is met on office wifi. The digest fires at 02:30 UK. Option D is selected, so 8 October is a handover, and phase 2 returns in December to build the things that would have moved test 2. In late November the count of raised stock tasks equals the count of crossings in a ledger written by the same reader, the late-order number is 9% against an undefined calendar, and no meeting exists at which anyone is obliged to discuss it.

Every criterion passes. Marigold hates it. Nothing in the document has been breached.

### The four things to fix before this leaves the building

1. Name production — environment, region, deploy identity, cost, and a criterion that the board is live where the team uses it. Then add authentication as an outcome with a criterion.
2. Add criteria for P1-3, P1-4, P1-10, S-1, S-2, and a maximum acceptable latency between a floor crossing and a task existing. Without that number, "appears by itself" is satisfied by a nightly poll and Priya's February recurs.
3. Put the 90-day review in the document — date, attendees, what each side brings, and the honest sentence about what phase 1 can and cannot move on test 2.
4. Govern the S-1 dataset before C-1, and either give §10.4's "never enters a model prompt" a mechanism and a test, or delete the clause. It is currently a claim Karan's own §10.2 says he cannot stand behind, above his signature.