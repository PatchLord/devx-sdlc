FICTIONAL DOCUMENT — CREATED FOR A DEMONSTRATION. Marigold Living does not exist. Dev Rawat, Priya Menon, Anjali Sen, Farhan Qureshi, Ravi Menon, Tarun, Rakesh, Anjali (customer care), Kalyan Ceramics, the Leicester 3PL and every order number, date and rupee figure below are invented for a simulated engagement. Anjali Sharma and Karan Iyer are invented individuals. devx labs' process is real; this client, this meeting and this engagement are not. Third-party model-provider names are withheld deliberately: in a real SOW the provider is named in writing, and in a fictional document naming one would attach a real company to an invented engagement.

# Discovery meeting — Storefront Ops Board

| | |
|---|---|
| **Date** | Thursday 6 August 2026 |
| **Time** | 09:30 – 11:00 IST (90 minutes, hard stop). Video call, recorded |
| **Stage** | 00 Solutioning. Input to the SOW |
| **Present — Marigold Living** | Priya Menon, operations manager · Dev Rawat, founder (joined 09:42) |
| **Present — devx labs** | Anjali Sharma, delivery lead (chair; will write the SOW) · Karan Iyer, tech lead (will sign it) |
| **Absent, referenced** | Anjali Sen (co-founder, London) · Farhan Qureshi (ops lead) · Ravi Menon (accountant) · Tarun, Rakesh, Anjali (customer care) |
| **Inputs** | BRD v1.1, 6 August 2026, read in advance by both sides. No walkthrough — the meeting went straight to the disagreements |
| **Notes by** | Anjali Sharma |
| **State** | **Frozen.** Corrections are appended below, not edited in. Where these notes and the signed SOW differ, **the SOW wins** |

Two people in this record are called Anjali. **A.S.** is Anjali Sharma, devx labs. **Anjali (care)** is Marigold's customer-care person. Anjali Sen is named in full throughout.

---

## 09:30 — Before Dev joined

**A.S.** opened by saying what she wanted out of the 90 minutes: a scope she could write down, the contradictions in section 11 either resolved or given an owner, and the six things the SOW cannot be signed without. She named them so Priya could hold her to it: the depth level, a personal-data inventory, the named model provider with written permission, what happens after go-live, the price shape, and a list of our checks with every row marked *written*, *proven* or *to build*.

**The warehouse.** Settled in forty seconds. The unit is in **Bhiwandi**. Dev was thinking of the vendor cluster outside Pune — Kalyan Ceramics and two others. Priya's section was right; Dev's was a memory of a different drive.

**The roster.** This one was not cosmetic and Karan said so.

> **P.M.:** Today it is four. Me, Tarun, Rakesh, Anjali. Farhan starts in September, so five. And two temps at Diwali who will never have seen it.
>
> **K.I.:** So seven people by the second week of November, not four. That matters more than it sounds. Who can see whose tasks, who can complete something that is not theirs, and who can put a completed thing back — that is a permission model, and a permission model is one of the shapes we fix before anything is built on top of it. If we freeze it for four people and you arrive with seven, every ticket after that inherits the wrong shape.
>
> **P.M.:** Everyone sees everything. That is the whole point of it. I am the one who assigns and I am the one who reopens.
>
> **K.I.:** Then that is the model, and the temps are the interesting case, because "everyone sees everything" including two people who are there for nine days.

Decided: everyone sees every task; only the assignee or Priya may complete one; only Priya (or her named backup) may assign or reopen. Temp accounts are individually named, never shared, and carry the same read-everything / complete-only-mine shape. Detail goes to the design document.

**Then the finding nobody enjoys.** A.S. asked who at Marigold we would put on a technical call. Priya's answer was that there isn't anybody — the store was set up by a freelancer three years ago who no longer answers, Tarun does the Monday export because someone showed him once, and nobody knows what "Sheet1 (do not delete)" is for.

**K.I.:** "Then I have to say this out loud because it changes the plan. Our own process expects at least one call with the client's technical people, and where there isn't one, the behaviour of your systems is something we have to *discover* rather than assume. That is a piece of work with a name and a duration, not a thing that happens quietly inside the first ticket. I need read-only access to the store and I need to go and look at your actual orders and inventory data before I will agree to a date."

Recorded as a scope item, not a complaint.

## 09:42 — Dev joined

Supplier call overran. He flagged his hard stop at 11:00 for the Bhiwandi drive — which is section 14 of his own document biting on the day, and both sides said so.

> **D.R.:** Right. Before anything else. Have you found the thing in there that cannot be true? Not the six I listed. I know about those.

A.S. said yes, one, and that it was his section 5 rather than his section 11, and asked to take it in order so it landed with its reasons attached.

## 09:47 — What raises a task, and the Leicester problem

Two signals in phase 1: a product crossing below its floor, and an order past its dispatch promise. Plus anything a person types in, which Priya was firm about — "half my day is neither of those."

Karan went at the second signal.

> **K.I.:** Your 48-hour promise for India I can compute, because the clock starts when the order is paid and stops when the warehouse marks it fulfilled, and both of those are events in Shopify. The 3–5 days for the UK I cannot promise you yet, and your own document is why. You wrote *assume nothing* about Leicester. So: does the 3PL push a fulfilment event back into Shopify, how late, and does it come one order at a time or in a lump at close of day?
>
> **P.M.:** I don't know. I see tracking numbers appear. Sometimes not for two days.
>
> **K.I.:** "Sometimes not for two days" is the answer that worries me, because if the event is late, my clock is late, and a UK order will look on time for two days and then jump straight to breached. Your team will stop believing the number in week one, and a number nobody believes is worse than no number — that is the shared calendar dying again in a different costume.
>
> **D.R.:** So what do you need.
>
> **K.I.:** Somebody at the 3PL to tell me how their integration works, and read access so I can go and look at ninety UK orders and measure the lag myself. I am not taking their word for it either.

**This is the question that blocks something.** The shape of the fulfilment clock is a shared surface, and shared surfaces get fixed before anything is built on them. Owner, date and the consequence of slipping are in the open-questions table. Both sides accepted the consequence in the room: **if it is not answered by Friday 14 August, phase 1's late-order signal covers India-warehouse orders only, UK moves to phase 2, and Dev signs that as a scope note rather than discovering it in October.**

## 09:58 — The floors, and the 200 new SKUs

Priya's section 15 question — how do 900-odd numbers get out of her head — turned out to be the biggest schedule item in the document, and it is not our work.

> **K.I.:** The board cannot raise a single stock task until a floor exists for that product. So "phase 1 usable on 25 September" has a dependency that is entirely your calendar, Priya, and if it takes you a fortnight then the date is fiction no matter what we do.
>
> **P.M.:** I told you I don't know if it is a day or a fortnight.
>
> **A.S.:** How many of the 900 actually move?
>
> **P.M.:** Sixty. Maybe sixty-five. The rest sit there.
>
> **K.I.:** Then do sixty by hand and let the rest come from a rule. A default per category, so Candles gets one number, Textiles gets another, and anything you have not touched inherits it. The 200 new SKUs inherit it too, automatically, which is the part you were going to be stuck with in October otherwise. Then a screen where you can change forty of them in one sitting rather than one at a time.
>
> **P.M.:** That I can do in an afternoon.

Decided. Category defaults, per-product override, bulk edit. Priya's afternoon is on the Kickoff critical path and is named as such.

## 10:05 — "It should know whose job it is" against "nothing gets assigned unless I assign it"

Section 11, contradiction 1. Resolved, and Priya did most of the resolving.

> **P.M.:** Both of those are true, I know how that sounds. Stock is Tarun, packing is Rakesh, customer-facing is Anjali, money and vendors are me. But I am not having a computer tell Rakesh to do something. That is my job, and it is also how I know what is happening.
>
> **A.S.:** So the rule fills the name in and you press the button.
>
> **P.M.:** Yes. That is exactly it. It guesses and I agree.

Decided: the rule proposes an assignee; nothing is assigned until Priya (or her named backup) confirms; unconfirmed tasks sit in an unassigned pile at the top of the board so they cannot be quietly ignored.

Karan then said the consequence out loud, which is what opened the next twenty minutes.

> **K.I.:** Fine. But note what that does to your success test 1, Dev, because it now depends on Priya pressing a button. If she is on a call for three hours, tasks exist with nobody's name on them, and your test reads that as a failure of the software.

## 10:11 — The contradiction, and it was not one of the six

> **K.I.:** And that is the smaller half. Dev, test 1 says: for the peak window, the count of products that dropped below their floor and the count of tasks raised are the same number. Where do you think the first of those two numbers comes from?
>
> **D.R.:** From the products that dropped below their floor.
>
> **K.I.:** From *us noticing that they did.* The only thing that can count crossings is the same component that raises the tasks. So if it misses a crossing, it does not raise a task and it does not count the crossing either, and the two numbers match perfectly. Your test passes hardest in exactly the case you are afraid of. It cannot fail for the reason you wrote it.
>
> *(pause)*
>
> **D.R.:** Say that again.
>
> **K.I.:** You have written a test that compares a system against its own opinion of itself. It reads as a strong test and it is a tautology. And in phase 1 it is worse than that, because your section 7 puts webhooks in phase 2 — so phase 1 asks Shopify on a schedule. Anything that dips below its floor and gets restocked between two asks never happened, as far as the board is concerned, and never happened as far as your count is concerned. That is your brass candle holders, on a Saturday, when the dip and the recovery are hours apart.
>
> **D.R.:** So what do I measure instead.
>
> **K.I.:** Something that is not the board. An append-only ledger: every inventory reading we take, per product, with a timestamp — separate from the board, never edited, never archived. Then a crossing is a thing you can find in the readings whether or not a task got raised, and the comparison has two independent sides. That I can build and that you can audit yourself.
>
> **D.R.:** And the crossings between two readings?
>
> **K.I.:** Those I cannot recover in phase 1. How often we read is a decision, and it trades against your ₹35,000 ceiling and against the store's rate limits. What I can tell you is that the ledger makes the gap *visible* — you will be able to see how far apart the readings were, which means the number you get in November comes with its own error bar instead of pretending it hasn't got one.

**Resolution: partial.** The instrument changed in the room, from "count what the board did" to "an independent append-only reading ledger". What did not resolve is the polling interval and what the residual blind window means for the 90-day verdict. That is an open question with an owner and a date. Dev's reaction, for the record: *"That is the first time anyone has told me one of my own tests is rubbish. Keep doing that."*

## 10:19 — Notifications, and how the calendar died

> **P.M.:** When something lands on your name you get a message. On WhatsApp, because that is the only thing anyone opens. And in the group, so nobody can say they didn't know.
>
> **K.I.:** And two paragraphs later you tell me the calendar died because it pinged constantly. Those are the same request twice with opposite settings. Can I put it the way I think it actually plays out — if every assignment goes to the group, then Rakesh gets a message every time you assign something to Tarun. On his phone, at the unit, on a bad signal. By Wednesday he mutes the group. And once it is muted, the one message that was actually for him is also muted, and now the board is a second place to look and you have Trello again.
>
> **P.M.:** *(pause)* Yes. That is what would happen.
>
> **K.I.:** So: the person whose name is on it gets a message. Nobody else does. And you get one summary a day, in the group, at a time you choose — what is outstanding and who has it. That is the "no I didn't know" problem solved once a day instead of forty times.
>
> **P.M.:** Eight in the morning. That is when the roll call happens now.
>
> **D.R.:** If there is still a roll call at eight, test 3 has failed.
>
> **P.M.:** It is not a roll call if I am not asking anyone anything. It is me reading it.

Decided: per-assignee message on assignment. One daily digest to the group at 08:00 IST. No other automatic group traffic in phase 1.

**Then the thing Karan would not answer.**

> **K.I.:** I need to stop before I say something about WhatsApp I would have to correct. Two things I am not confident of. I believe the business API sends to individual numbers against pre-approved templates and does **not** address a group at all — which would mean the 08:00 digest cannot go where you want it to go, and we would be talking about a group of individual messages or a different channel for that one thing. And I will not give you a cost per message from memory, because you have a ₹35,000 ceiling and message volume is one of the two things that could break it.
>
> **D.R.:** When.
>
> **K.I.:** Monday. With the pricing page attached, not my recollection of it.

Deferred to Karan, 11 August. See the table.

## 10:27 — The Google Sheet

The line Dev suspected was the most expensive in his document. It was, and it did not survive intact.

> **A.S.:** Priya, take me through why the sheet stays.
>
> **P.M.:** Three years of it. My vendor payment dates are in a tab on the right. I do things in it I could not explain to you. And if the list is somewhere else then the sheet is somewhere else, and I am back to two places.
>
> **K.I.:** Understood, and I am not going to try to take it off you. What I want to talk you out of is the *both directions* part, and I will do it with a Thursday in November. Both directions means two systems that each believe they are right. One morning Tarun pastes over a row while the board is changing the same row because an order shipped. Now they disagree. Something has to win, and whichever one wins is wrong half the time — and you will not find out which half, you will find out that the number on the screen is not the number in the sheet, on the day volume triples. At that point you stop trusting both of them, and you go back to paper. That is not a hypothetical, that is the failure mode of every two-way sync anyone has ever built.
>
> **P.M.:** But the sheet is how I —
>
> **K.I.:** *(cutting in)* Sorry. One more thing and then I will stop. Your sheet is already lying to you by Thursday, on your own account, because it is a Monday export. So the thing you are defending is not an accurate sheet. It is a *familiar* one.
>
> **A.S.:** Priya, you were saying, before I let Karan in.
>
> **P.M.:** I was saying the sheet is where the floors are going to get typed. I am not typing sixty numbers into a new screen at nine at night. I am typing them into the sheet, because that is where I think.
>
> **K.I.:** That I can give you, and it is not the same request. Sheet to board, one direction, for floors only, when you press an import button — you type, you press, it lands, and the board tells you what it read so you can see if you fat-fingered one. And board to sheet, one direction, a mirror tab that is rewritten and that nobody types into. Two directions across the file, never both directions into the same cell. Your vendor tab is not touched by us, ever, and I will name it in the SOW as yours.

Decided. **Sheet → board:** stock floors only, on an explicit import, with a read-back. **Board → sheet:** a mirror tab, machine-written, read-only. **No cell written by both.** Priya gave up general two-way editing and insisted on the floors path and on the vendor tab being named as untouchable; both recorded as her call, not ours.

## 10:36 — "It should go away" against counting a week of it

Section 11, contradiction 3. Resolved cleanly and quickly.

**K.I.:** "Going away is a view, not a delete. Done tasks drop off your screen after seven days. Nothing is removed from the database, and the reading ledger is append-only and never archived at all. What you asked for is a screen with only live work on it, and what Dev asked for is eight weeks of history — those only fight if 'clear out' means 'destroy', and it does not have to."

Decided. Archive is a filter. Deletion is not in scope in either phase. Priya's laptop struggling with the sheet is a reason the *sheet mirror* gets trimmed, not a reason to lose data.

## 10:39 — Customer data, the free-text box, and the thing Dev's rule does not cover

> **K.I.:** Your rule 1 I agree with and I want to make it stronger in one place and weaker in another. Stronger: there is no masking script in this project, because there is no customer data in the board's schema to mask. Dev and test get invented customers only. You were right that a script somebody has to remember is a script that gets skipped, and the way to win that argument is to have nothing to skip.
>
> **D.R.:** And weaker.
>
> **K.I.:** I will not write "the board holds no customer data" in a document I sign, because Priya's free-text box exists and I cannot stop her typing *the lady in Pune called twice, her number is* into it. Nobody can. A rule in a document does not stop a person typing. So the truthful sentence is: **the board does not ingest customer data from Shopify, and it can still receive customer data from a human being.** What I can do about the second half is make the field never reach our logs, never reach an error report, and never reach a model prompt — and tell you plainly that if it is typed, it is in the database and it is in the backups.
>
> **D.R.:** That is a smaller promise than I wanted.
>
> **K.I.:** It is the one that is true. And there is a second thing your rule does not cover, which I would rather raise now than have you find in the SOW. Your rule is about *customers*. The one dataset in here that is unambiguously personal is your **staff** — four to seven people's names, phone numbers, and a record of what each of them did and when. And section 6a asks for a report on how many things Tarun marked done and then reopened. That is performance monitoring of a named employee. I am not saying you cannot have it. I am saying it goes in the personal-data inventory with a purpose written next to it, the people it is about are told it exists, and it is not a side effect nobody declared.
>
> **P.M.:** I would rather Tarun knew it existed, honestly. Half the point is being able to hold something up.
>
> **D.R.:** Put it in. And tell me what our obligations are on that, because we have people writing to us from the UK and I don't know if that touches it.

Karan's answer: the staff are in India and the data is employment data, and he is not going to give a legal opinion on a call. What goes in the SOW is the inventory — what is held, why, for how long — and Marigold's own adviser reads it. Recorded.

## 10:45 — "You are going to run AI on our code"

> **D.R.:** Named provider, in writing, before you upload anything. That is a condition, not a preference.
>
> **A.S.:** Yes, and it is a condition on our side too — our process puts named third-party AI processing with your written permission in the SOW, and we do not upload a document before we have it. The provider, the retention terms and where the processing happens are in the annexe that goes to you on Monday. Nothing of yours goes anywhere until you have written back.
>
> **D.R.:** Checked against our DPA, not assumed.
>
> **K.I.:** Here is where I have to be straight with you, because you will find this out anyway and I would rather you found it out from me. What we have written down is the *permission* half — the provider is named, you sign, and until you sign nothing moves. What we have **not** finished writing down is the harder half: exactly what an agent is allowed to *read* and transmit. We have no per-engagement matrix that says these repositories yes, these logs no, production data never, checked line by line against a client's DPA. We have no redaction of personal data out of prompts and session transcripts as a mechanism rather than a habit. We have no stated position on how long a provider retains a session or which region it sits in beyond what their terms say. That is a known gap on our side, it has a number in our own open-questions list, and it needs an answer before this engagement rather than during it.
>
> **D.R.:** So you are telling me you don't have a policy.
>
> **K.I.:** I am telling you we have half of one, and the half we have is the half you asked for. What I will not do is describe the other half as finished. If it matters to you as much as I think it does, then the thing to buy is a written data-handling note **for this engagement** — which repositories, which documents, what never goes near a session, retention, region — delivered before the first upload and signed by both of us. That is a Kickoff deliverable and I will own it.
>
> **D.R.:** Do that. Second thing. Our standard contract says deliverables are original work, free of third-party IP. Can you sign that?
>
> **K.I.:** Not as written, no. And I want to be careful here because this is the one where a confident answer would be worse than a slow one. We have no licence-compatibility scan, no copyleft check, and nothing that detects a generated block reproducing third-party code verbatim. So I cannot *prove* originality on agent-written code, and a warranty I cannot stand behind is worse for you than a qualified one, because the moment it matters you will be holding a promise nobody can test. What I would put in front of your lawyer is a qualified clause plus what we actually do — the code is reviewed, it is small in pieces a person can read, and the dependencies are scanned. That is not the same thing as originality and I am not going to call it that.
>
> **D.R.:** *(long pause)* All right. That is two honest answers in five minutes, which is two more than I got in fourteen weeks last time. Put both in the document in those words.

Recorded, with the wording carried to the SOW verbatim.

## 10:52 — "How do I know it works"

> **P.M.:** Can I ask the stupid version of Dev's question. How do I know, in October, that it is doing what you said and not just looking like it.
>
> **A.S.:** Two things, and then Karan will tell you what neither of them covers. First, every acceptance criterion names the thing that proves it — a test, a screenshot of a person actually completing a task, the output of a query, a link to a run. A criterion with prose in that column fails the release rather than passing it. Second, every release hands you a list of what it does **not** verify. That is the more useful of the two documents and nobody volunteers it, which is why we do.
>
> **K.I.:** And the limits, because Dev's section 13 asks for exactly this. Our checks exist as files, and the SOW lists every one of them marked **written**, **proven** or **to build**. Today most of them say *written*: the file exists, the logic has been tested off a host. We have run our gate logic against thirty deliberately broken cases and it rejected what it was supposed to reject and found a real defect in our own code doing it — that part I will show you. What we have **not** yet done is watch a red check stop a merge on a live host on a real project. So the honest sentence is *this is how we work*, and the sentence I will not write is *this is proven to reduce defects*. There is no percentage in that document. If you find one, it is a mistake and I want you to send it back.
>
> **D.R.:** What is the one you are least comfortable about.
>
> **K.I.:** Two. The tests are written by the same thing that writes the code, so a test and a bug can share the same misunderstanding and both look green — nothing we have catches that cheaply, and no standard I have read catches it either. Our partial answer is to compute expected values by hand on the parts that matter. And the platform one: **nothing we build can see a change somebody makes inside the Shopify admin.** If someone edits a product there, our board finds out next time it asks. That is a hole, not a feature, and it goes in the SOW as a hole.
>
> **D.R.:** Good.

## 10:56 — Price, date, and four minutes left

> **D.R.:** Number. Inside eighteen to twenty-six.
>
> **A.S.:** Not today, and I will tell you why rather than stalling you. Two things move it and neither is settled: the depth level, which we have just decided, and the Leicester answer, which could remove or add a whole signal. A number I give you now is a number I would revise, and you have told me what you think of documents that get revised. Monday the 11th you get the SOW with one number in it, what is in, what is out, and the three lines I am least sure of.
>
> **D.R.:** Monday is fine. Understand that anything over five lakh needs Anjali Sen and Ravi Menon, and Ravi is a week, so Monday-plus-a-week is realistically the 20th before I can sign.
>
> **A.S.:** Which is why it is Monday and not the 15th. Your own document said bring money the week we first see it.
>
> **D.R.:** And the depth thing. Explain the scale and show me the difference.
>
> **K.I.:** Three levels, set by what a mistake costs, not by size. This is **Standard**, and here is the reasoning so you can argue with it. Nobody's money moves. Nothing customer-facing changes. A mistake is recoverable — it is your staff who feel it, and the worst realistic case is a task nobody sees, which is Tuesday today anyway. Against that: it holds staff personal data, and it will live for years. That is Standard. High is where money moves or something cannot be undone.
>
> **D.R.:** And if I paid for High.
>
> **K.I.:** You would get a second environment and its running cost, a second named owner approving anything that touches the dangerous paths, and a load test and a restore drill with the restore time written down. Those are real. But two of High's rows — mutation testing and a full audit trail — are *to build* on our side, meaning if you bought High today you would be buying a written commitment for those two rather than a running check. I am not going to sell you that. Standard, and phase 2's notification path gets treated as a dangerous path when we get there, because a message that has been sent cannot be unsent.
>
> **A.S.:** Dates. Is 25 September real. Arithmetic, not opinion: signature realistically the 20th, then handover, kickoff and setup — and setup is not cuttable, it ends with one page live in dev put there by the real pipeline and one deliberately-broken pull request that a gate actually blocks. Call it the 1st of September before a feature ticket starts. That leaves **eighteen working days** to the 25th.
>
> **D.R.:** Which is not phase 1 as I wrote it.
>
> **A.S.:** No. Eighteen days is a smaller phase 1. The 25th is real for: the board, both signals, assign, complete, reopen, the per-person message, the floors with category defaults and bulk edit, and the reading ledger. Deferred to your freeze date: the daily group digest, the sheet import and mirror, the seven-day archive filter, and Priya's reopen report — the *data* for that report is captured from day one, the screen is not.
>
> **D.R.:** So everything lands on the 8th, which is the freeze, which means no slack at all.
>
> **K.I.:** Which is why I want to move one of your own dates. Last merge on **Friday 3 October**, last deploy on the 8th. Five days between "we stopped changing it" and "we stopped being allowed to change it".
>
> **D.R.:** Agreed. Take it.
>
> **K.I.:** One more, and it is your section 15 question 11. Your freeze says no deploys to anything your customers can reach. The board is internal — your customers cannot reach it. So strictly your freeze does not cover it, and I do not think you meant to leave that open. What I propose: no *feature* deploys after the 8th; a defect fix during the window needs your sign-off per fix; and we agree a read budget against your store in advance, because the one way this internal thing can hurt your customers is by hammering the API during Black Friday.
>
> **D.R.:** I had not thought past that sentence. You are right. And that runs straight into the thing we never discussed — who fixes it at 11pm on the 23rd of November.
>
> **A.S.:** Which is the after-go-live question, and it is priced separately or it does not exist. What I will bring Monday is a shape: a window with an end date, a response time inside the freeze and a different one outside it, and how you are told when something has broken rather than finding out. If you decide not to buy it, then the 8th of October is a handover and we will say that out loud at the time rather than discovering it when the first thing breaks.
>
> **D.R.:** Price it. I am not deciding today.

## 11:00 — Stop

Dev left on the hour. Not covered, by agreement: the two Diwali temps beyond the account decision, the returns question Priya raised and withdrew in her own document, and the ₹35,000 running-cost breakdown, which waits on the WhatsApp answer. Priya stayed on for six minutes to give Karan Tarun's export steps and the name of the tab nobody understands.

---

## Decisions made

1. The unit is in **Bhiwandi**. The Pune reference was the vendor cluster.
2. Users at go-live are **Priya, Tarun, Rakesh, Anjali (care)**, plus **Farhan** from September and **two named temp accounts** in November. Seven by mid-November, not four.
3. **Permissions:** everyone sees every task; assignee or Priya may complete; only Priya or her named backup may assign or reopen. Temps get individual accounts, same shape.
4. **Assignment:** the rule proposes a name, Priya confirms. Nothing is assigned without her confirmation. Unconfirmed tasks surface at the top of the board.
5. **Stock floors:** category defaults, per-product override, bulk-edit screen. The ~60 moving SKUs are authored by hand by Priya. The 200 new SKUs inherit their category default automatically.
6. **Success test 1's instrument changes.** An append-only inventory-reading ledger, separate from the board and never archived, is the counting basis — not the board's own record of what it raised.
7. **Success test 2 splits.** devx labs is accountable for the late-order number existing, being correct, being visible daily, and covering exactly the orders it claims to cover. The **under-3% target is Marigold's business target**, recorded as Dev's, not as a devx acceptance criterion. The 90-day review reports against it.
8. **Notifications:** per-assignee message on assignment; one group digest at 08:00 IST; no other automatic group traffic in phase 1. Channel for the digest depends on OQ-2.
9. **Google Sheet:** one direction per cell. Sheet → board for **stock floors only**, on an explicit import, with a read-back. Board → sheet as a machine-written mirror tab. General two-way editing is dropped — Priya's decision, on the two-sources-of-truth argument. The vendor-payment tab is named in the SOW as Marigold's and is never touched.
10. **Archive is a view, not a delete.** Done tasks leave the screen after seven days. Nothing is deleted in either phase. The ledger is never archived.
11. **Customer data:** the board does not ingest customer data from Shopify. Dev and test use invented customers only, with no masking step to skip. The free-text field is excluded from logs, error reports and model prompts. The SOW will **not** claim the board holds no customer data, because a human can type it in.
12. **Staff data goes in the personal-data inventory**, including the reopen statistics, with a purpose and a retention period, and the people it is about are told it exists.
13. **Depth: Standard.** Reasoning recorded. High was explained and declined by devx, not by Marigold, because two of its rows are *to build* on our side.
14. **Shopify access: read only.** A custom app created by Dev in his own admin, read scopes only (products, inventory, orders, fulfilments, locations), token held in Marigold's secrets manager. No devx staff account. No theme access of any kind, which is easy because we are not building in the theme.
15. **Freeze amended.** Last merge **Friday 3 October**; last deploy **8 October**. During 8 Oct – 5 Dec: no feature deploys; a defect fix needs Dev's sign-off per fix; an agreed API read budget against the store.
16. **Phase 1 for 25 September** is the reduced set named at 10:56. The remainder lands by 3 October. Phase 2 is December–January, unchanged.
17. **Nothing of Marigold's is uploaded to any model provider** until Dev has replied in writing to the annexe naming the provider, its retention terms and its processing region.
18. **A written data-handling note for this engagement** — repositories, documents, what never enters a session, retention, region — is a Kickoff deliverable owned by Karan, delivered before the first upload.
19. The SOW will contain **no percentage, no "proven" and no "guaranteed"**, and every check is marked *written*, *proven* or *to build*.
20. **The originality warranty is not signed as written.** Karan cannot prove originality of agent-written code and said so. A qualified clause plus a description of what we actually do goes to Marigold's adviser.
21. **Weekly demo: Wednesdays 09:30 IST, 30 minutes**, working software only. Avoids Dev's Tuesday and Thursday afternoons.
22. **Discovery of the existing setup is a named piece of work**, because Marigold has no technical person to hand and the store's behaviour has to be measured rather than assumed.

## Open questions

| # | Question | Owner | Date | What it blocks | If it slips |
|---|---|---|---|---|---|
| **OQ-1** | Does the Leicester 3PL push fulfilment events into Shopify, at what latency, per order or in a daily batch? Measured against ~90 real UK orders, not taken on the 3PL's word | **Priya Menon** (get the 3PL's integration facts and a named contact) with **Karan Iyer** (measure it in the store once read access exists) | **Fri 14 Aug 2026** | The fulfilment-clock contract, which is a shared surface frozen before anything builds on it. Therefore the whole late-order signal, and the criteria behind Dev's test 2 | **Phase 1's late-order signal covers India-warehouse orders only. UK moves to phase 2.** Dev signs it as a scope note. Accepted in the room by both sides |
| **OQ-2** | Can the WhatsApp business API address a group at all, what does a message cost, and what do its template rules allow? Karan believes it sends only to individual numbers against approved templates and declined to state it as fact | **Karan Iyer** | **Mon 11 Aug 2026** | The 08:00 group digest, and the messaging line in the ₹35,000/month running-cost ceiling | Digest becomes a per-person message or a different channel. Cost line in the SOW is marked as an estimate with the reason |
| **OQ-3** | How often do we read inventory from Shopify, and what does the residual blind window between two readings mean for the 90-day verdict? | **Karan Iyer**, with Dev on the cost and rate-limit trade | **In the SOW, Mon 11 Aug 2026** | The reading ledger's design, the API read budget for the freeze window, and the error bar attached to test 1's number | Test 1's number ships without a stated blind window, which is exactly the kind of unqualified figure Dev's section 13 rejects |
| **OQ-4** | Is Farhan Qureshi content to be the named backup decision-maker for board behaviour, and does he accept the same response time? He was not in this meeting | **Dev Rawat** (tell him; get it in writing) | **Fri 15 Aug 2026** | The Kickoff working agreement, which cannot name a backup who has not agreed to it | Priya is sole decision-maker with no backup, and her leave or a warehouse day becomes a delivery stall |
| **OQ-5** | Our position on what an agent may **read** and transmit — per-engagement repository and document allowlist, redaction from prompts and session transcripts, retention and residency — checked against Marigold's DPA rather than assumed | **Karan Iyer** | **Before the first upload; draft by Mon 18 Aug 2026** | The first document upload, and therefore the start of any drafting work on Marigold material | Nothing of Marigold's is uploaded. Work that does not need their material can start; anything that does, waits |
| **OQ-6** | Whether Marigold's standard originality warranty can be signed in a qualified form, and in what words | **Dev Rawat** (his adviser), with Karan supplying what we do and do not check | **Before signature** | Signature | Signature slips, or the clause is carved out. Not a technical decision and not ours to make |
| **OQ-7** | What after-go-live support is bought: window, end date, response time inside and outside the freeze, and how Marigold is told something has broken | **Anjali Sharma** to price; **Dev Rawat** to decide | **Priced Mon 11 Aug; decided before signature** | Whether 8 October is a go-live or a handover | It is a handover, said out loud on the day rather than discovered when something breaks in the peak window |
| **OQ-8** | Can Rakesh's actual phone run this? Nobody has looked at the phone | **Priya Menon** (send make, model and OS version; Karan to check) | **Fri 22 Aug 2026** | The front-end floor for browser and device support, and whether "on phones" means what we assume | Support floor is set from assumption. If the phone fails it, the fix lands after the floors are already built against the wrong baseline |
| **OQ-9** | What "closed in the tool" counts as, when the tick is on the board and the real work happens in Shopify (Priya's own question 6) | **Priya Menon** and **Anjali Sharma**, in the design document | **At Kickoff** | The definition behind Dev's test 3, and therefore what the 90-day verdict measures | Test 3 is judged on a definition nobody agreed, which is how a verdict becomes an argument |
| **OQ-10** | Marigold's obligations on holding staff performance data, given the inventory in decision 12 | **Dev Rawat** (his adviser) | **Before signature** | Nothing technical. The reopen report's retention period | Report ships with a conservative default retention; revisited later |

## What each side does before Kickoff

**devx labs**

- SOW to Marigold **Monday 11 August**: one number inside ₹18–26 lakh, what is in, what is out, the three lines we are least sure of, the depth level and its reasoning, the personal-data inventory including staff, the post-go-live options priced, and the check list with every row marked *written*, *proven* or *to build*. — A.S.
- Annexe naming the model provider, retention terms and processing region, sent with the SOW. **Nothing is uploaded before Dev replies in writing.** — A.S.
- OQ-2 answered with the pricing page attached, Monday 11 August. — K.I.
- Read-only measurement of the store as soon as access exists: UK fulfilment lag against ~90 orders, inventory-change frequency for the 60 moving SKUs, and what the orders data actually contains. — K.I.
- Draft engagement data-handling note (OQ-5), 18 August. — K.I.
- Named people in the SOW, and a written commitment to tell Marigold before anyone changes rather than after they notice from the commits. — A.S.
- The 3PL question put to Priya's contact in writing so there is a record of what was asked. — K.I.

**Marigold Living**

- Read-only Shopify access: a custom app created by Dev in his own admin, read scopes only, token handed over out of band. **Owner Dev, by Monday 11 August** — this gates Karan's measurement work and therefore the answer to OQ-1.
- The 3PL contact and their integration facts (OQ-1). Priya, by 14 August.
- Farhan's written agreement to be named backup (OQ-4). Dev, by 15 August.
- Rakesh's phone details (OQ-8). Priya, by 22 August.
- Priya's afternoon on the 60 moving SKUs' floors — **not before Kickoff**, but named on the critical path, and it has to happen inside the first fortnight of build or the 25 September set has nothing to raise a task about.
- A copy of the Stock Watch sheet, including "Sheet1 (do not delete)", so we can see what is actually in it before we write anything near it. Priya, with Kickoff.
- Dev to start Anjali Sen and Ravi Menon on the money question the day the SOW lands, not the day he wants to sign it.

## Working agreement, as agreed in the room

| | |
|---|---|
| **Decision-maker, board behaviour** | **Priya Menon.** States, who gets what, what a floor means, wording, workflow. Settles Marigold's own open question 14 |
| **Backup** | **Farhan Qureshi**, same authority for behaviour only. Subject to OQ-4 — he has not yet been asked |
| **Reserved to Dev Rawat** | Money. Anything touching customer data. Anything touching store access. Not delegable, and not to Priya or Farhan |
| **Priya's response time** | Same working day if it reaches her before 18:00 IST. She is on the tool all day |
| **Dev's response time** | Small decisions inside his 09:30 and 21:00 IST windows, ~4 hours. Anything needing thought, 24–48 hours. **Not Tuesday or Thursday 11:00–18:00 IST.** **12 October – 30 November: 3–4 working days** for anything not on fire — planned for now, not discovered then |
| **Money latency** | Over ₹1.5 lakh: + Anjali Sen, two working days, three across her Friday. Over ₹5 lakh: + Ravi Menon, one week, not compressible. **Any money decision is raised in the week it is first foreseen.** One raised in week five that was visible in week two gets a no on principle |
| **Weekly demo** | **Wednesdays 09:30 IST, 30 minutes.** Working software. Not a deck, not a percentage. Recorded for whoever missed it |
| **Escalation, in the freeze window** | Per decision 15: a defect fix needs Dev's sign-off per fix. Response time depends on OQ-7 |
| **Client latency is a delivery constraint, not a courtesy note** | Both sides accepted that with building compressed, Dev's answer time may set the timeline rather than devx's capacity — particularly across 12 Oct – 30 Nov. Question wait time is tracked split into waiting-on-us and waiting-on-them, and reported at the demo |

## Not covered, carried forward

Returns and refunds — Priya raised and withdrew it in her own document; it stays out of scope per section 16 and nobody reopened it. The two Diwali temps beyond the account decision. The ₹35,000/month breakdown, which waits on OQ-2 and OQ-3. Whether the Monday export Tarun runs can be retired entirely, which nobody thought to ask and which Karan flagged after Dev left.

## Status of this record

Frozen 6 August 2026. Corrections are appended below with a date and an author, never edited into the text above. Where this record and the signed SOW disagree, the SOW is the authority — including on anything said in the recording that was later changed.

*No corrections at time of issue.*

**FICTIONAL — see the notice at the top of this document.**