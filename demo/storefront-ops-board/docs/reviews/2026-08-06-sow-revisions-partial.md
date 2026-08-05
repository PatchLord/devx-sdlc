# SOW revisions — PARTIAL

The final assembly agent's output was truncated: it begins mid-sentence and its opening markers were
lost, so the revised BRD and the first ten sections of the revised SOW do not exist. What survived is
below — commercial terms, signatures, the 90-day review and the accepted risks — and it is kept because
those sections were absent from the v0.9 draft entirely.

**This is not a signed SOW.** The signed document does not exist yet; see the tech lead's review.

---

kind appears anywhere in this document, and none will appear in any document we hand over.** If Marigold finds one, it is a mistake, and we would like it sent back.

### 11.6 Payment schedule

Absent from the draft entirely, along with the rest of §12's terms.

| # | Milestone | Amount | Trigger |
|---|---|---|---|
| 1 | Signature | **20% of ₹11.6 lakh** = ₹2.32 lakh | 6 August, invoiced 7 August, 14 days |
| 2 | Setup exits, all four items in §5.3 with run links | 15% = ₹1.74 lakh | 21 August |
| 3 | Monthly against tickets closed, September | 25% = ₹2.90 lakh | 30 September |
| 4 | **Phase 1 acceptance** — the 2 October release document signed by Priya and Dev (§7.3) | 30% = ₹3.48 lakh | 2 October |
| 5 | **Retention, released at the 90-day review** | **10% = ₹1.16 lakh** | 25 November, on the signed record of §14 |
| — | Option A | ₹1.6 lakh | Invoiced 8 October, 14 days |
| — | P1-13 / P1-14, if bought | per the 28 August quote | On acceptance of the 2 October release |

Invoices are monthly, in arrears, 14 days. **The 10% retention is the only money that depends on the November meeting**, and it is there so that the meeting exists for both of us rather than only for Marigold.

---

## 12. Commercial and legal terms

The draft contained a change-control path and nothing else. These are the terms Dev asked for when he said "tell me what our obligations are on that", and the ones his adviser will look for first.

| | |
|---|---|
| **Intellectual property** | All deliverables, the repository and its history assign to Marigold **on payment of the milestone that covers them**. devx retains its own pre-existing tooling — the starter repository, the perimeter and pipeline templates, the skills and the check scripts — licensed to Marigold perpetually, royalty-free, for this system, and Marigold may modify them. **Originality is qualified per §10.3 and D-6, not warranted flat** |
| **Confidentiality** | Both ways, three years from signature, standard carve-outs for what is public or independently known. Marigold's store data, order data and staff data are confidential without qualification |
| **Data protection** | **Marigold is controller; devx is processor.** The agreement is D-15, signed as Annexe E before store access is used on 10 August. §10.4 is an inventory and is not a substitute for it. The named model provider is a sub-processor and is disclosed as one in Annexe A |
| **Liability** | Each party's aggregate liability is capped at **the fees actually paid under this SOW**, excluding fraud, wilful misconduct, breach of confidentiality, and breach of the data-protection terms. No indirect or consequential loss either way. **Marigold's festive revenue is not underwritten by this document and nobody should read it as if it were** |
| **Termination for convenience** | Either side, **15 working days' written notice.** Marigold pays for work completed to the last merged ticket plus any work in progress at the notice date. **A five-working-day wind-down is included at no charge**: documents current, credentials handed over, the release document for whatever last shipped, and a written statement of what is unfinished. Marigold already owns the repository and the accounts, so there is nothing to release and no lawyer's letter needed. That is deliberate |
| **Termination for cause** | Either side, on a material breach not cured within 10 working days of written notice |
| **Suspension** | If an invoice is more than 30 days overdue we may stop merging and tell Dev in writing. We do not remove access, revoke credentials or take anything down. Ever |
| **Governing law** | India. Courts of Mumbai. Marigold sells into the UK, which is a data-protection question rather than a jurisdiction one, and it is D-15's |
| **Non-solicitation** | None. Neither side asked for one |
| **Publicity** | We do not name Marigold, show the board, or describe this engagement anywhere without Dev's written agreement per instance |

### 12.1 Changing this mid-phase

Clients change their minds, and a process that treats that as a failure gets routed around. The path below is designed to be used.

**One rule sits above the rest: a change that alters what Marigold accepts goes through the delivery lead and lands in the acceptance criteria before any code moves.** A criterion changed to match what got built is not a criterion.

| Step | What happens |
|---|---|
| **1. Say it** | To Anjali Sharma, at the Wednesday demo or in writing. No form. Nothing is refused for arriving informally |
| **2. We write it down and price it, within two working days** | What it changes, what comes out to make room if the date is fixed (§2.3's order), what it costs, and which acceptance criteria change. One page. **Whether it is a change or our own rework is classified here, and Priya may dispute the classification per §11.1** |
| **3. Marigold decides, at the right level** | Behaviour: Priya, or Farhan. Money over ₹1.5 lakh: Dev plus Anjali Sen, two working days. Over ₹5 lakh: plus Ravi Menon, a week, not compressible. Customer data, store access or repository settings: Dev alone |
| **4. It becomes real in the repository** | The criteria change on their protected path, approved by a named person and not by an agent. The design document changes. Both are commits Marigold can read |
| **5. It appears in the release document** | Including in the "what this does not verify" section, if the change moved something out of what we check |

**Three limits on the path:**

- **Money raised late gets a no on principle.** Foreseeable in week two, arriving in week five, gets a no even where a yes was available in week two. Dev's rule, adopted, because the alternative is us absorbing his approval latency silently and then missing a date.
- **After 2 October and through 5 December, no change is a feature change.** A defect fix inside that window follows §11.4's path with Dev's sign-off per fix. Anything else is January.
- **A change cannot buy back time by removing Setup.** If a date is at risk, features come out in §2.3's order. The perimeter stays.

---

## 13. Signatures

A signature on a document nobody can be held to is decoration. Each line says what that person is answerable for. **Signatures are rendered as typed names because this is a fictional document.**

### 13.1 For Marigold Living

**Dev Rawat, founder**

Signing for: the scope in §2 and §3 being the thing Marigold wants, including every declined item, every named non-verification in §6, and the drop order in §2.3; the depth level in §4 **including the recorded deviation in §4.3 and the two triggers that reopen it**; the fee in §11.1 — ₹13.2 lakh approved today, the ₹2.2 lakh capped decision due 28 August, phase 2 not approved — and the running-cost position in §11.3 **including that the top of that band is above his own ceiling and what the levers are**; Option A in §11.4 and the fix path described in it; the dependencies and dates in §8.2, and that a slip in them moves our dates as described in §9.3; the terms in §12; **written acceptance of Annexe A's named model provider, its retention terms and its processing region, given 6 August as Annexe B**; that the staff data in §10.4 is held with the purpose stated and that the people it is about are told; that D-6, D-10, D-11 and D-15 are his to answer with his adviser; and the risks recorded against his name in §15.

**Signed: Dev Rawat — 6 August 2026**

*Anjali Sen (co-founder) and Ravi Menon (accountant) approved the ₹18–26 lakh envelope in writing on 5 August 2026, Annexe C. That approval is what makes this signature possible on the 6th; it is not a signature on this document.*

**Priya Menon, operations manager**

Signing for: being the decision-maker on how the board behaves, at the response time in §9.2; **accepting each release on behalf of the people who use it** (§7.3), inside the three-working-day window, with one extension available to her; the decisions that are hers — D-9, D-12 with Dev, D-13, D-14 — and that C-5, C-6, C-9, C-11 and C-13 are her dependencies with her dates on them; that the design brief is accepted by her before implementation tickets are written; and that she withdrew the two-way sheet sync herself, on the argument, so its absence is not something devx took from her.

**Signed: Priya Menon — 6 August 2026**

### 13.2 For devx labs — delivery

**Anjali Sharma, delivery lead**

Signing for: that this document says what was actually agreed in the meeting of 6 August 2026, including the parts Marigold did not want to hear; the dated schedule in §8.4, the firm price and what is deliberately not priced, and the rework allowance **including the disclosure that Marigold never discussed it**; the working agreement in §9, including devx's own festive-season cover being named rather than assumed; that a change follows §12.1 and never arrives as a quietly edited criterion; that Marigold is told before a named person changes rather than after; that the 90-day review in §14 happens on 25 November whether or not it is comfortable; and that every change the tech lead required before signing is in this document rather than in a covering note.

**Signed: Anjali Sharma — 6 August 2026**

### 13.3 For devx labs — technical

**Karan Iyer, tech lead**

Signing for: **every technical claim in this document being one I can stand behind, and every gap being named rather than smoothed.** Specifically — the depth level in §4, **the recorded deviation in §4.3 from our own table's personal-data limb, which is mine and is named as mine**, and the refusal to sell High while two of its rows are *to build* and a third has never been tried; the status of every row in §5.2, including that **no row says *proven***, that the middle column now states what is true today rather than a promise, and that the last row is an **exception** to something our process says never bends, carried by me; production being named, provisioned from code, and proved by a promoted artefact rather than by a page in dev; the four Setup exits in §5.3, including a code-owner review actually demanded and satisfied; the list in §6 of what we will not verify, and that it goes into every release document; that the criteria in §7 each name an artefact, that a prose artefact fails the release, and that the four scheduled-job alarms are criteria and not monitoring wishes; the honest position in §10.2, and the three different strengths in §10.4 — **logs and error reports are mechanisms with tests, and keeping the task table out of a model prompt is an instruction to four named people, which I will not describe as a mechanism**; §10.6's handling of real customer data during S-1, and that D-5 and C-12 precede it; the statement in §10.3 that I cannot demonstrate originality of agent-written code and will not sign a warranty saying I can; the running-cost position in §11.3 including that the ceiling binds; the fix path in §11.4 and that no agent ever runs remediation against production; and that **no percentage improvement, no "proven" and no "guaranteed" appears in this document or in anything we hand Marigold.**

**The conditions I attached to signing are in the document, not here:** Deepa's funded hours (§11.1), the four Setup exits (§5.3), the four alarm criteria (A-21 to A-24), authentication as an outcome with criteria (P1-0, A-18, A-19), the phase-2 receiver on the protected list with authenticity criteria (A-45 to A-47), the depth deviation recorded with my name on it (§4.3), and the risks in §15 that I am carrying rather than fixing. If I could not stand behind a sentence, it changed before this document was issued. That is what this signature is for.

**Signed: Karan Iyer — 6 August 2026**

**Imran Shaikh, QA**

Signing for: the acceptance artefacts and the release document, including its third column and its "what this release does not verify" section; that an empty artefact cell fails a release rather than passing it; and that a release is not handed to Priya for acceptance until it is ready under §7.3, item 1.

**Signed: Imran Shaikh — 6 August 2026**

### 13.4 The named people

| Who | Role | Signs for / allocated |
|---|---|---|
| **Anjali Sharma** | Delivery lead | This document, the commercial frame, the working agreement, the 90-day review |
| **Karan Iyer** | Tech lead | Every technical claim, the design document, the perimeter, Setup, production, the data-handling note, the D-1/D-3/D-8/D-12 measurements. First code owner on all protected paths |
| **Nikhil Barve** | Senior engineer, phases 1 and 2 | Named first responder under Option A, 8 Oct – 5 Dec |
| **Sneha Raut** | Engineer, phase 1 | Named cover under Option A |
| **Imran Shaikh** | QA | The acceptance artefacts and the release document |
| **Deepa Kulkarni** | Engineer from outside this project | **Second code owner on the protected paths, funded at six hours a week through phase 1 inside the fee** (§11.1), so a fortnight's leave cannot stall a protected merge and Karan is not the single point of failure |

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

10. **Shopify's stock number may not match the shelf**, and the whole low-stock signal fires off it (N-11, X-19). Reconciliation is out of scope by his choice.
11. **Phase 1 cannot move the late-order percentage** (N-12), and P1-18 — the one thing that could, before December — is not bought.
12. **Priya is the single confirm-and-reopen point** until D-4 closes, and during Diwali her button is the board's throughput limit. A-28's ageing flag is a mitigation, not a fix.
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