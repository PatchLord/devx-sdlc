> **FICTIONAL — part of a simulated engagement.** Marigold Living does not exist. See `../../README.md`.

> Annexe to the Statement of Work v1.0, 11 August 2026. The signature document is `../sow.md`;
> where the two differ, **the signature document governs**.

# Annexe D — Obligations and decisions, in full

Everything Marigold must supply, with dates, plus the open decisions and their owners. Referenced from §8 and §9.

## Assumptions, dependencies, and what we need from Marigold

### 8.1 Decisions still open at the time of writing

Each has an owner, a date, what it blocks and what happens if it slips. These are not caveats; they are the shape of the plan.

| # | Open question | Owner | Needed by | If it slips |
|---|---|---|---|---|
| **D-1** | Does the Leicester 3PL push fulfilment events into Shopify, at what delay, per order or in a daily lump? Measured against ~90 real UK orders, not taken on the 3PL's word — by hand, by Karan, with no agent session, per §10.6 | Priya Menon (facts and a named contact) with Karan Iyer (measurement, once read access exists) | **Fri 14 Aug 2026** | **Phase 1's late-order signal covers India-warehouse orders only; UK moves to phase 2.** Accepted by both sides in the meeting. Signed as a scope note, not discovered in October, and the price moves with it per §12's scope-cut table |
| **D-2** | Can the WhatsApp business API address a group at all, what does a message cost, what do its template rules allow — **and is sending order numbers into a group consistent with Marigold's own section 12?** Dev asked that third part and v0.9 dropped it | Karan Iyer | **Tue 11 Aug 2026** | **The fallback is in force when this document is issued, not promised for later:** the 08:00 digest is an individual message to each named person, no group message, each held to that person's 08:00 local time (A-26), carrying task references and order numbers only (A-25) — on the WhatsApp path if C-14 to C-17 land in time and on email if they do not. §11.3's messaging line stays an estimate, with the reason |
| **D-3** | How often do we read inventory from the store, and what does the residual blind window mean for the November figure? | Karan Iyer, with Dev on the cost and rate-limit trade | **Tue 11 Aug 2026** | **The fallback is in force at issue:** every 15 minutes between 08:00 and 22:00 IST, every 60 minutes outside it; the ledger writes on change plus one heartbeat row per cycle, which is what keeps §11.3's database line bounded; the residual blind window is stated on the screen and beside the November figure; and A-20's maximum latency is derived from it. If Dev's cost or rate-limit answer moves the interval, it moves A-20 and §11.3's database line and nothing else in this document |
| **D-4** | Is Farhan Qureshi content to be the named backup for board-behaviour decisions, on the same response time? He was not in the meeting | Dev Rawat, in writing | **Fri 21 Aug 2026** | Priya is the sole decision-maker with no backup, and a warehouse day or a day of leave becomes a delivery stall. A-28's ageing flag is a mitigation for the throughput half and not for this |
| **D-5** | Our own written position on what an agent may **read** and transmit — repositories, documents, logs, extracts, **and how an agent is used during an incident** — checked against Marigold's data processing agreement | Karan Iyer | draft **Fri 7 Aug 2026**, signed by Karan and Dev **before Mon 10 Aug 2026**, which is **before C-1's token is used** | Nothing of Marigold's is uploaded and **S-1 does not start**, because S-1 reads real customer records. In v0.9 this note was dated four days after the first read of ~90 real UK orders; that sequencing was the reason the draft came back unsigned. See §10.2 and §10.6 |
| **D-6** | Whether Marigold's originality warranty can be signed in a qualified form, and in what words | Dev Rawat, with his adviser; Karan supplies what we do and do not check | **before signature** | Signature slips, or the clause is carved out. Not a technical decision and not ours to make. Interacts with D-11 |
| **D-7** | Which after-go-live option Marigold buys | Anjali Sharma to price (§11.4); Dev Rawat to decide | **before signature** | 8 October is a handover, said out loud on the day |
| **D-8** | Can Rakesh's actual handset run this? Nobody has looked at the phone | Priya Menon (make, model, OS version); Karan to check | **Fri 21 Aug 2026** | A-27's profile is set from the closest device we can buy and written down as an assumption rather than a measurement. If the real phone fails it after 2 October, the fix is January |
| **D-9** | What "closed in the tool" counts as, when the tick is on the board and the real work happens in Shopify | Priya Menon with Anjali Sharma | **at Kickoff**, committed under **`docs/design/criteria/`** and not in the design document | Dev's third success test is judged on a definition nobody agreed, which is how a verdict becomes an argument. Moved out of the design document at v1.0: that file is living and agent-drafted, and a definition that decides a verdict belongs on the protected path for exactly the reason §7 gives |
| **D-10** | Marigold's obligations on holding staff performance data | Dev Rawat, with his adviser | **before signature** | The reopen report ships with a conservative default retention and is revisited |
| **D-11** | **Do commits in Marigold's repository carry provenance trailers recording that a session wrote the code?** | Dev Rawat, with his adviser; Karan supplies what a trailer would contain | **before the first commit** | Either answer is effectively permanent. Agents write most of the code and the repository is Marigold's from the first commit, so a trailer is a discoverable record — in an asset Marigold may later show a buyer, an auditor or the next agency — and removing it afterwards means rewriting history. It also interacts with D-6, because those trailers are evidence in exactly the dispute the originality clause creates. Not a tooling decision and not ours to default either way |
| **D-12** | **The dispatch clock's calendar.** Is the UK promise 3 days or 5, elapsed or working? Does the India 48 hours run through Sundays, public holidays and the days the unit is shut? | Priya Menon, with Dev on what was published | **at Kickoff** | **Fallback in force:** the outer figure, working days, against Marigold's holiday calendar (C-11), with the rule stated on the screen beside the number. An order paid at 18:00 on the Friday before a holiday Monday is "breached" at 18:00 on Sunday on an elapsed clock — Priya looks at a number like that once, disbelieves it, and stops looking, which is the shared calendar dying in a third costume |
| **D-13** | Is the board English only? | Priya Menon | at Kickoff | English only, named as a limitation in §3 rather than discovered by Rakesh in September. Not free to change later — it is in every screen and in Priya's free text |
| **D-14** | When a product crosses, recovers and crosses again while the first task is still open, is that one task or two? Priya asked this herself and v0.9 answered it inside a test | Priya Menon | at Kickoff | A-2's behaviour stands — one task while the first is open — and the decision is recorded as hers rather than settled by whoever wrote the test |
| **D-15** | **The controller and processor terms between Marigold and devx.** We hold staff personal data, and free text can carry a customer's | Dev Rawat with his adviser; Anjali Sharma states what we do with it | **before 10 Aug 2026, and therefore ahead of C-12 rather than ahead of signature** | No agreement, no C-1 token in use, no S-1 — see C-12. §10.4 is an inventory, not an agreement, and Dev asked in the meeting what Marigold's obligations actually are |

**D-2 and D-3 are Karan's own, they are due the day v1.0 issues, and they have no float on the path to signature.** So neither is written here as a promise that it will be closed. Each carries a fallback that is **in force at issue**: if Monday's answer never arrives, this document still describes a working system at a stated cost, and nothing in §8.4 moves. An answer that does arrive improves a number and changes A-15, A-20 or §11.3 — never a date and never a scope row.

### 8.2 What we need from Marigold, and by when

| # | What | Owner | By | What it gates |
|---|---|---|---|---|
| **C-1** | **Read-only Shopify access**: a custom app created by Dev in his own admin, read scopes only (products, inventory, orders, fulfilments, locations), token handed over out of band and held in Marigold's secrets manager | Dev Rawat | **Tue 11 Aug 2026** | Everything in S-1, and therefore the answer to D-1 and any date we can stand behind. **Not used before C-12 and D-5 exist** |
| **C-2** | The 3PL contact and their integration facts | Priya Menon | Fri 14 Aug 2026 | D-1 |
| **C-3** | Farhan's written agreement to be named backup | Dev Rawat | Fri 21 Aug 2026 | The Kickoff working agreement — it cannot name a backup who has not agreed |
| **C-4** | Rakesh's handset make, model and OS version | Priya Menon | Fri 21 Aug 2026 | D-8, and A-27's profile |
| **C-5** | A copy of the Stock Watch sheet, including "Sheet1 (do not delete)" | Priya Menon | with Kickoff | The import and mirror design, and the price for P1-13 and P1-14, which §11.1 does not quote until we have opened the file |
| **C-6** | **Priya's afternoon on the ~60 moving SKUs' floors.** Not before Kickoff, but on the critical path and named as such | Priya Menon | **inside the first fortnight of build** | The board cannot raise a single stock task for a product with no floor. If this lands in late September, the 25th has nothing to demonstrate |
| **C-7** | Written reply to Annexe A naming the model provider, its retention terms and its processing region | Dev Rawat | **before any upload, and therefore before S-1** | Any work on Marigold's material at all. Dated ahead of discovery at v1.0, not ahead of the build |
| **C-8** | Dev to start Anjali Sen and Ravi Menon on the money question **the day this document lands**, not the day he wants to sign | Dev Rawat | Tue 11 Aug 2026 | The signature date, and therefore the start date, and therefore 25 September |
| **C-9** | Named accounts and phone numbers for all users, including the two Diwali temps before they start, **and a named person who deactivates a temp account when they leave** | Priya Menon | rolling | P1-8, A-11, A-19's deactivation case, and the staff inventory in §10.4 |
| **C-10** | Two hours a week from Priya through build, plus the Wednesday demo | Priya Menon | weekly | Everything. She is the decision-maker on behaviour, and from v1.0 she is also the person who accepts a release under §7.3 |
| **C-11** | **Marigold's holiday calendar for both markets**, including the days the Bhiwandi unit is shut | Priya Menon | at Kickoff | D-12, A-3, and every dispatch-clock number anyone will argue about in November |
| **C-12** | **The controller/processor agreement signed** — D-15 | Dev Rawat | **before C-1's token is used** | S-1, and every later thing that depends on it. The token exists and is not used until this does |
| **C-13** | **A named person at Marigold adjusts one product's stock in the Shopify admin on 18 September**, at a time we know | Priya Menon | 18 Sep 2026 | A-1's screenshot. X-1 makes us read-only, so we cannot cause the crossing our own criterion needs; without this row A-1 depends on ~60 SKUs happening to oblige inside a chosen fortnight |
| **C-14** | A WhatsApp Business Account in Marigold's name, on Marigold's card | Dev Rawat | **Thu 20 Aug 2026** | P1-8, P1-12, A-15 |
| **C-15** | **Meta business verification completed** | Dev Rawat | **Fri 4 Sep 2026** | As above. This is Marigold-side, routinely takes weeks and can be refused — which is why D-2's email fallback exists and is not a punishment. v0.9 asked what the API costs and never asked about the path to sending the first message |
| **C-16** | A dedicated number for the board's messages, not a person's handset | Priya Menon | Fri 4 Sep 2026 | As above |
| **C-17** | Message templates submitted and pre-approved | Karan drafts; Dev Rawat submits | **Fri 11 Sep 2026** | The 25 September message set. A template rejected in the first week of build is a rewrite; one rejected in the last week is the email fallback |
| **C-18** | **A repository plan on Marigold's account that supports branch protection and rulesets** | Dev Rawat | **before Setup** | Every gate in §5. A gate that cannot be turned on is not a gate, and some plans do not carry it |
| **C-19** | **A fine-grained token with `Administration: read`**, for the job that reads the host's real configuration back | Dev Rawat | before Setup | The one check that makes every other check's claim honest. Some organisations block this token class by policy, and we would rather learn that in the first ten minutes than in Setup |
| **C-20** | **Runners available to the repository**, with enough minutes for a day's merges | Dev Rawat | before Setup | The whole pipeline. A queued run is a green tick that has not happened yet |
| **C-21** | **One named administrator on the repository and the hosting — Dev Rawat, and nobody else** | Dev Rawat | before Setup | See the note below this table |
| **C-22** | **The Shopify API version pinned in writing, with its sunset date** | Karan Iyer proposes; Dev Rawat agrees | before Setup | Assumption 4. A version sunset falling inside 8 October – 5 December is a change nobody would have permission to make |
| **C-23** | **A model-provider API key on Marigold's account for our own review job** | Dev Rawat | before Setup | The review check in §5.1. It means Marigold's card pays for our reviewer, which is a real line and belongs in §11.3 rather than on a statement Dev reads in October |

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

| When | What | Depends on |
|---|---|---|
| 7 Aug 2026 | **D-5 drafted** — the engagement data-handling note, covering uploads *and* incidents | Karan Iyer |
| before 10 Aug | **D-5 signed by Karan and Dev. C-12, the processor agreement, in place.** Both are preconditions of the C-1 token being used | Dev Rawat, Karan Iyer |
| 11 Aug | **v1.0 issued**, with Annexe A and Annexe B. C-1, C-8, C-18 to C-23 requested. D-2 and D-3 issue with their fallbacks in force | Anjali Sharma |
| 11 – 14 Aug | **S-1 begins.** The store measured by hand, by Karan, no agent session, field-limited at the query, per §10.6 | C-1, C-7, C-12, D-5 |
| 14 Aug | **D-1 answered**, or the UK late-order signal moves to phase 2 as a signed scope note with a price change | Priya Menon, Karan Iyer |
| 20 Aug | **Signature.** D-6, D-7, D-10, D-11 and D-15 answered before it. C-14 requested | Dev Rawat |
| 21 Aug | D-4 (Farhan) and D-8 (the handset) answered | Dev Rawat, Priya Menon |
| 24 Aug | **Kickoff.** D-9, D-12, D-13 and D-14 settled. C-5 and C-11 in hand. S-2 and the design brief begin | Signature |
| 24 Aug – 1 Sep | **Setup**, ending with the four exit proofs in §5.3 — including one throwaway pull request deliberately blocked, and one code-owner review demanded and satisfied on a protected path. **A-33** (S-2's shapes) and **A-38** (the design brief accepted by Priya) both land here, before any implementation ticket exists | C-18 to C-23 |
| **2 – 25 Sep** | **Build: eighteen working days.** C-6, Priya's floors, inside the first fortnight | Everything above |
| 4 Sep | C-15 and C-16 — Meta verification and the dedicated number | Dev Rawat, Priya Menon |
| 11 Sep | C-17 — templates pre-approved, or the digest moves to email on D-2's fallback | Dev Rawat |
| 15 Sep | **A-7's real-handset evidence taken**, three weeks before last merge rather than after it | Priya Menon |
| 18 Sep | **C-13** — one product's stock adjusted in the admin, so A-1 has a real crossing. **Production provisioned and named** per §5.4 | Priya Menon, Karan Iyer |
| **25 Sep** | **Phase 1 core usable by four real people on real orders**, in production, with **A-37** taken on the day. Conditional on C-1 by 11 August and signature by 20 August. A-35's read budget agreed by now | |
| 25 Sep – 8 Oct | **The pre-window fortnight.** A-31 taken a second time on real data. §7.3 acceptance runs on the 25 September release | Priya Menon, Dev Rawat |
| **2 Oct** | **Last merge.** P1-12 to P1-16 land by here. Five days between "we stopped changing it" and "we are not allowed to change it" | |
| 8 Oct | **Freeze begins.** No feature deploys. A defect fix needs Dev's sign-off per fix, by the path in §11.4. **If Marigold has bought none of §11.4's options, this is a handover and Anjali Sharma says so out loud on the day** | D-7 |
| 12 Oct – 30 Nov | The festive window. Dev at three to four working days; devx's own cover named in §9.2 | |
| **25 Nov, 14:00 IST** | **The 90-day review** — §14. Dev's six tests, our criteria and their artefacts, N-12's honest sentence about test 2, and the review agent's dismissal rate | Both sides |
| 5 Dec | Freeze ends | |
| Dec 2026 – Jan 2027 | **Phase 2** — beginning by asking §4's four questions again rather than carrying Standard forward, per §7.2 | Karan Iyer |

Two dates in this table are ours to miss and nobody else's: 7 and 10 August. If they slip, S-1 does not start, and every date below them moves day for day. That is stated here rather than in §9.3 because it is the only row in the schedule where the dependency is devx's.

---
