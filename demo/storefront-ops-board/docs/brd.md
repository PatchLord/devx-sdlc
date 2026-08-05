> **FICTIONAL DOCUMENT — CREATED FOR A DEMONSTRATION.** Marigold Living does not exist. Dev Rawat, Priya Menon, Anjali Sen, Farhan Qureshi, Ravi Menon, Tarun, Rakesh, Anjali (support), Kalyan Ceramics and every event, order number and rupee figure in this document are invented for a simulated engagement. Nothing here describes a real company, a real store, a real person or a real engagement. devx labs' process is real; this client is not.

# Business Requirements Document — Storefront Ops Board

| | |
|---|---|
| **Version** | 1.1 |
| **Date** | 6 August 2026 |
| **Written by** | Dev Rawat, founder, and Priya Menon, operations manager — Marigold Living |
| **Sent to** | devx labs, ahead of solutioning |
| **Status** | Our own document. Nobody outside Marigold has reviewed it. |

## How to read this

This is two people writing in one file. Sections are marked **[D]** for Dev and **[P]** for Priya. We have not smoothed each other's sections and in two or three places we have written things that do not agree — where that happens we have left it and said so, rather than picking one, because we would rather you told us which is the expensive one.

We have not written this in your language and we are not going to try. If we have asked for something daft, or two things that cannot both be true, say so in your response and say so plainly. We would rather be told now than in three months. That has happened to us twice.

---

## 1. Who we are, and what we sell **[D]**

Direct-to-consumer home goods on Shopify. Candle holders, bedding, table linen, ceramics. About **900 SKUs** counting every size and colour separately, which is how the store counts them. We are adding roughly **200 more before the festive season**. One warehouse in India, a 3PL in Leicester for UK orders. We sell in India and the UK.

Four people touch an order. That is the whole team this is being built for.

**[P]** From my side the four are: me (operations), Anjali (customer care — she works late, most UK customers write in our evening), Rakesh (warehouse, on the floor, on his phone, never on a laptop), and Tarun (packing, courier follow-ups, and the reorder calls to vendors).

**[D]** From my side the four are Farhan Qureshi running ops, two on customer support, one on the floor.

**Those two paragraphs do not match and we have left them not matching.** Also Priya's draft says the unit is in Bhiwandi and mine says outside Pune. One of us is wrong about our own warehouse. Ask us in the first call; do not guess, and do not assume the roster in section 1 is the list of users.

Two people in this document are called Anjali. One is Anjali in customer care. The other is **Anjali Sen**, my co-founder, in London, who appears only in the money section. Sorry.

## 2. How work reaches this team today **[P]**

I get in around 9, sometimes 9:30 if my daughter's school bus is late.

First I open the Shopify orders page and look at what came in overnight, because the UK orders arrive while we are asleep. Then I open a Google Sheet called **Stock Watch**, which is now four tabs — Candles, Textiles, Ceramics, Misc — plus a fifth called "Sheet1 (do not delete)" that nobody understands and I am afraid to touch. The numbers in it come from Tarun exporting something out of Shopify on Mondays and pasting it in. So by Thursday the sheet is lying to me, I know it is lying to me, and I do not know by how much.

Then WhatsApp. We have a group called **Marigold Ops** and that is where the work actually lives. "Rakesh the Sharma order needs to go today." "Did anyone call Kalyan Ceramics about the grey bowls." "Which courier for Leeds." I also message people separately, because if I put something in the group nobody feels like it is theirs.

Then somewhere between 10 and 11 I make a to-do list. On paper. Then I lose it, or I take it home in my bag, and on Tuesday I rebuild Monday's list from memory.

Around 4pm I go through the orders list and eyeball dates to see what has not gone out. We promise 48 hours to dispatch for India and 3–5 days for the UK, and those promises are printed on our own product pages. Nothing tells me when we have broken one. I find out because I went looking, or because the customer found out first and wrote to Anjali, and Anjali came to me.

**[D]** The one-line version: **work reaches my ops team by somebody noticing.** The WhatsApp group has about 14,000 messages in it. Nothing is assigned. Things get done by whoever is awake.

## 3. What it costs us **[D]**

As specifically as I can put it.

- Last Diwali we **oversold three SKUs and cancelled 61 orders**. Refunds, goodwill vouchers, about a week of support time. Call it **₹4.5 lakh**, and I do not have a number for the reputational half.
- In November, **218 orders shipped past the 48-hour dispatch promise** on our own product pages. I found that out **in January**, from a spreadsheet, after the fact.
- Reconciling the sheet takes about **90 minutes a day**. That is a third of a person doing data entry, and it is the most useful person I have.

The part that actually worries me is none of those numbers. It is that this does not scale. We are adding 200 SKUs and pushing harder in the UK, and if nothing changes my next operations hire is a person employed to watch a spreadsheet. I refuse to make that hire.

**[P]** The same thing in the form of actual events:

**The brass candle holders.** In February a blogger put the small brass candle holder somewhere and we sold 40-odd over a weekend. The sheet said 30 in stock. We had 11. We took the orders anyway. I spent a week apologising and refunding, and two of those reviews are still up. If someone had told me on Saturday morning that the number had gone below where it should be, it would have been off the site by Saturday afternoon. Nobody told me, because on Saturday nobody was looking at the sheet.

**The Manchester order.** A bedsheet set sat for six days because I asked Tarun about it in the group on a Wednesday, eleven other messages happened, it scrolled up, and each of us thought the other had it. She was very nice about it, which made it worse.

**Diwali week.** Volume triples, we bring in two temp people, and paper lists plus a group chat stop working entirely. Last year I do not know how many orders went out late. I would guess thirty. I could not tell you, and that is the part I hate — not that it went wrong, that I cannot say how wrong.

**Reorders.** Something goes low, I mention it to Tarun, Tarun says he will call the vendor. Two weeks later we are out. Did he call? Did they say four weeks? Did nobody pick up? There is no record of anything. There is a conversation that happened and then stopped existing.

## 4. What we want to stop happening **[P]**

1. Me being the only thing standing between a low stock number and a customer buying something we do not have. It should reach me — better, reach Tarun — without me going to look for it.
2. Finding out about a late order from Anjali finding out from the customer.
3. A job existing in a WhatsApp message and then not existing because the chat moved.
4. Asking "did you do that?" I ask it about twenty times a day and I hate the sound of my own voice doing it.
5. Rebuilding Monday's list from memory.
6. During Diwali, not being able to look at one screen and know what is outstanding without asking anyone anything.

## 5. How we will judge whether this worked **[D]**

Taken at **90 days from a late-August start**, which lands in late November, right after Black Friday. That timing is deliberate. I want the verdict taken when the system is under load, not in a quiet week.

| # | What we want to be true | The signal we would actually look at |
|---|---|---|
| 1 | No stockout that nobody saw coming | For the peak window, the count of products that dropped below their floor and the count of tasks raised are **the same number**, and each one has a person's name against it who acknowledged it |
| 2 | Late orders are a number on a screen, not something I learn in January | That number exists, I can see it any day I want, and it is **under 3% past SLA** through 12 October to 30 November |
| 3 | The board is where work lives | All four of them using it, and the large majority of tasks closed in the tool rather than settled verbally and never recorded. If there is still an 8am roll call in WhatsApp, this failed regardless of what the code does |
| 4 | I can answer "what is unfinished right now, and who has it" | Myself, in under a minute, without asking anyone |
| 5 | It survives us | One of my four can teach it to a new hire in **fifteen minutes**. If it needs you to explain it, I have bought a dependency, not a tool |
| 6 | **[P]** I arrive at 9 and am told what needs doing | The 90 minutes a day of sheet reconciliation is mostly gone, and my paper list stops existing |

## 6. What we think we want **[P]**

Business language, because I do not have any other kind.

**One list of things that need doing, that all four of us see the same version of.** If something is low on stock, it appears by itself — I do not put it there. If an order has gone past what we promised, it appears by itself. And things I think of, I can add, because half my day is neither stock nor orders, it is "chase the courier about the damaged box in Pune."

**Everything on the list has one person's name on it.** One. Not "the team." If it has two names it has nobody's name, I have learned that.

**On phones.** Mine, and Rakesh's, and Rakesh's phone is not a good phone.

Then the specific things:

- **The stock number is different for different products.** Some things I am fine having two of. Some I want to know about when we are under twenty, because they go in waves. All of these numbers are in my head, and a few are in the margin of the sheet. I do not know how you would get them out of my head, but I would sit down and do it if someone made me.
- **It should just know whose job it is.** Stock is Tarun. Warehouse and packing is Rakesh. Customer-facing is Anjali. Money or a vendor is me. That is basically a rule, so it should be able to work it out and put the right name on.
- **Nothing gets assigned to a person unless I have assigned it.** I do not want people being told to do things by a computer. That is my job, and it is also how I know what is going on.
- **It should tell people.** When something lands on your name you get a message. **On WhatsApp**, because that is the only thing anyone here opens. Send it to the group as well so everyone can see, so there is no "I didn't know."
- **But it must not go off constantly.** We tried a shared calendar two years ago and it pinged so much that within a week everyone including me had it on silent, so it did nothing. I do not know how you square that with the point above. That is for you.
- **We tried Trello.** Anjali did. It lasted nine days. It died because nobody put anything into it and it was a second place to look, and a second place to look is a dead thing.
- **I want to keep the Google Sheet.** I know that sounds like it defeats the purpose. I have had that sheet three years, I do things in it I cannot explain, and my vendor payment dates are in a tab off to the right. What I want is: **if I type something in the sheet it shows up in the list, and if something changes in the list it changes in the sheet. Both directions, so they are never different.** Then I can work however I feel like working that day.
- **When something is done it should go away.** I want to open it and see only what is left. And clear out the old ones after a week or so, otherwise it becomes ten thousand lines nobody cares about, and my laptop already struggles with the sheet as it is.

### 6a. The Tarun thing **[P]**

I am going to be direct, because you will work it out in a week anyway.

Tarun ticks things off before they are done. He is not lying exactly — in his head "I will call them this evening" is the same as done. It is not. Three of the four times we have run out of something this year, it was marked handled.

So: **I want to see who marked something done and when, and I want to be able to put it back.** And I want to be able to look at a week and see how many things he marked done and then came back. I am aware this is really a conversation I should be having with Tarun. I have had it twice. I would still like the numbers, because right now when I raise it he says "I did do it" and I have nothing to hold up.

## 7. Later, not now **[P] [D]**

**[P]** **Dates.** Nothing on my paper list has a date and that is part of the problem. But dates get strange, because Anjali works UK evenings and Rakesh starts at 7am here, and "by end of day Tuesday" means two different afternoons depending on who is reading it. Somehow it should handle that. I do not know what handling it looks like.

**Reminders before something is due**, rather than after it is late. Being told after it is late is what already happens — that is Anjali and the customer.

**And I do not want to keep refreshing something.** If an order comes in it should be on the list, not on the list twenty minutes later. I do not know if that is hard.

**[D]** Those three are phase 2 — due dates across our two timezones, reminders, and whatever makes signals arrive live instead of on a poll. I would rather have them **in December and January** than rushed in before the freeze. If you tell me phase 2 fits before 8 October, I will assume you have not understood the freeze.

I am aware that this sits badly next to success test 2, which is measured through the peak window on a phase 1 that has no reminders in it. I have not resolved that. See section 11.

## 8. Budget **[D]**

**₹18–26 lakh** for the engagement, phase 1 and phase 2 together, across roughly four and a half months. I would rather spend at the top of that range and get something my team actually uses than spend at the bottom and get a demo.

**Hard ceiling on running cost afterwards: ₹35,000 a month** for hosting, tooling and whatever the notifications cost. If the architecture only works at ₹80,000 a month, tell me during solutioning, not at go-live.

The range is a range on purpose. Give me a number inside it, with what is in and what is out, and **tell me which parts of the range you are least sure of.**

## 9. Dates, and what makes them real **[D]**

Our festive push opens **12 October** and runs through Black Friday and Cyber Monday at the end of November. Diwali is in the first half of November this year. That eight-week window is somewhere around **40% of our annual revenue**, and it is the period in which every operational weakness we have turns into a refund.

| Date | What | Why it is that date |
|---|---|---|
| Late August | Start | So phase 1 has real use before the window |
| **25 September** | Phase 1 usable — board, tasks arriving from stock floors and SLA breaches, assign, complete. Used by four real people on real orders | Two weeks of real use before the window opens |
| **8 October** | **Feature freeze.** Nothing new ships after this. If it is not in by then it is January | Four days before the window |
| **8 Oct – 5 Dec** | **No deploys to anything my customers can reach.** Not a small one. Not a hotfix that is definitely safe. If something is broken badly enough to justify touching the store in that window, it comes to me and I decide | This is the revenue |
| **Late November** | The 90-day verdict in section 5 | Taken under load, on purpose |
| **Dec – Jan** | Phase 2 | After the window, not squeezed into it |

## 10. Systems already in use, and the graveyard **[P] [D]**

| System | What it does today | Note |
|---|---|---|
| **Shopify** | The store. Orders, inventory, product pages that carry the 48-hour dispatch promise | The system of record. Customer data already lives here and is already governed here |
| **Google Sheet "Stock Watch"** | Stock floors, by hand, from a Monday export. Four tabs plus "Sheet1 (do not delete)". Vendor payment dates in a tab to the right | Priya wants to keep it and wants it kept in step, both directions |
| **WhatsApp group "Marigold Ops"** | Where the work actually is. ~14,000 messages | Also the only app anyone reliably opens |
| **Phones** | Rakesh has no laptop. His phone is old and cheap and the signal at the unit is patchy | Whatever this is, it works there or it does not work |
| **3PL in Leicester** | UK fulfilment | Nobody here can tell you how much of what the Leicester 3PL does is visible to us. Assume nothing |
| **Paper** | Priya's daily list | We would like this to stop |
| **Trello** | Dead. Nine days | Died because it was a second place to look |
| **Shared calendar** | Dead. On silent inside a week | Died because it pinged constantly |

## 11. Things in this document that fight each other **[D]**

We know about at least these. We have deliberately not fixed them, because we do not know which side to give up and you might.

1. **"It should work out whose job it is and put the right name on"** against **"nothing gets assigned to a person unless I have assigned it."** Both are in section 6, both are Priya's, and both are things she means.
2. **"Message the group on WhatsApp every time something lands on someone's name"** against **"it must not go off constantly, that is how the calendar died."**
3. **"When something is done it should go away, clear out the old ones after a week"** against **Priya wanting to see across a week who marked what done and reopened it**, and against **my success test 1, which compares two counts over an eight-week window.** If the old ones are cleared out, I am not sure what either of us is counting.
4. **Phase 2 arrives in December and January**, but **success test 2 is measured through the peak window**, and the things that would most obviously reduce late orders — a due date, a reminder before something is late — are the phase 2 items. I do not know if test 2 is fair against phase 1 alone. Tell me what it is fair to measure.
5. **My rule that no customer data goes into this system** (section 12) against **Priya's free-text tasks**, which will say things like "chase the courier about the damaged box in Pune, the lady called twice." Nobody has told her not to type that, and I am not sure a rule stops it.
6. **The board must not be a second place to look** — that is what killed Trello — against **the board being a new place to look.** The sheet sync in section 6 is Priya's answer to this. I do not know whether it is a good answer.

## 12. The two things I will personally block **[D]**

I am open to being argued out of my dates if you can show me why, and my budget if you can show me what the extra buys. Not these two.

**1. My customers' data does not go into this system, or into any AI tool.**

The board holds order numbers, SKUs, quantities, timestamps, dispatch clocks and who is assigned. It does not hold customer names, email addresses, phone numbers or shipping addresses — not in its database, not in its logs, and not in any prompt, session transcript or file sent to a model provider. A task says "order 41892, dispatch clock at 39 hours." It does not say who she is or where she lives. If the person working the task needs the address, they open Shopify, where the data already is and is already governed.

Dev and test environments get **invented customers only**. I am aware the usual answer is "we run a masking script." A script somebody has to remember to run is a script that gets skipped on the busy day, which is the day it matters. Show me that the masking cannot be bypassed, or show me invented data.

And I need **the AI provider named in writing before you upload the first document**, checked against our data processing agreement rather than assumed. We sell in the UK. This is not theoretical for me, and "we'll confirm that later" is a no.

**2. Nothing gets write access to my store in phase 1.**

Read only: products and inventory read, orders read, and whatever is needed to listen for the signals. The board tells a human what to do. The human does it in Shopify, under their own login, where Shopify already records who did it.

If phase 2 wants to write anything — adjust inventory, mark fulfilled, anything at all — that is a separate decision I sign separately, with a named person accountable, access scoped to that one operation, and a record of who changed what that I can read without asking you.

Nobody at devx labs gets a Shopify staff account with app or theme permissions. **Nobody edits the live theme, ever, for any reason, including "it's a one-line fix."** That has happened to me and it cost two days of my own copy changes.

## 13. What I will not accept in the paperwork **[D]**

- **Claims you have not actually run.** If a check exists as a file but has never run on a real host and failed something it was supposed to fail, your document says so, in those words. No "proven." No "guaranteed." **No percentage improvement in defects, velocity or anything else.** I have been given numbers by an agency before and they were invented. If I find one claim in a document that turns out to be aspirational, I will read the whole document as marketing and price you accordingly.
- **A phase I cannot see running.** A weekly demo of working software, on a schedule, or I stop paying. Not a status deck. Not a percentage complete. Software, doing something, in front of me.
- **"We'll sort out production later."** Whatever production needs gets decided before the freeze, not during it.
- **Anything I cannot walk away with.** The repository is mine from the first commit, in my organisation. Hosting and every third-party account in Marigold's name, on Marigold's card, with me as owner. Not yours with me added.
- **Silent substitution of people.** Name who is doing the work. If they change, tell me before I notice from the commits.
- **Invoiced time I cannot map to a ticket.** Every hour ties to something on a board I can see.

### Why I am like this **[D]**

I paid a firm to rebuild our re-order and subscription flow over fourteen weeks. For eleven weeks the status reports were green and the weekly call was "on track." What arrived was an admin screen with a table that rendered beautifully and buttons that did nothing — the save side had been built at every layer except the one a person clicks. They edited our live theme directly with no version control, so twice my own product copy was silently reverted by their next deploy. The invoice contained a "QA phase" for which nobody could produce a single artefact, and when I asked what tests existed the answer was "we tested it manually." The hosting account was in their name and it took a month and a lawyer's letter to move it. That is why I am hostile to status reports, why I do not accept the word "done" without something I can look at, and why ownership and scoped access came before anything else in this document.

## 14. How fast we can answer you **[D]**

Honestly, and I am not flattering myself.

- I read messages properly twice a day, around **9:30am and around 9pm IST**. A small decision landing in one of those windows comes back within about four hours. Outside them, next morning.
- Anything that needs me to look at a screen and think: **24 to 48 hours.**
- **Tuesdays and Thursdays I am at the warehouse or on supplier calls, effectively gone 11am to 6pm IST.** Do not plan a decision point on those afternoons.
- **From 12 October to the end of November, assume three to four working days** for anything not on fire. I will be the bottleneck. Plan around it now rather than discovering it then.

**My named backup is Farhan Qureshi**, ops lead. He can decide anything about how the board behaves — states, who gets what, what a stock floor means, wording, workflow. He cannot decide money, anything touching customer data, or anything touching store access. Those three are mine.

**[P]** I should say that I am the one who will use this every day and I am not sure whether the person you should be asking about how it behaves is Farhan or me. We have not sorted that out between ourselves.

### Money specifically **[D]**

| Threshold | Who else | Realistic time |
|---|---|---|
| Over **₹1.5 lakh** | **Anjali Sen**, co-founder, equal shareholder, in London, four and a half hours behind me, batches her decisions | **Two working days.** Three if it crosses her Friday |
| Over **₹5 lakh** | Also **Ravi Menon**, our accountant, because it competes with the festive stock buy for the same cash | **A week**, and I cannot compress it |

So: **if you can see a money decision coming, bring it to me in the week you first see it, not the week you need it.** A change request landing on my desk in week five that was obvious in week two gets a no on principle, even if I would have said yes in week two.

I am aware that once you are building fast, my answer time may become the thing that sets the timeline rather than your capacity. That is exactly why I have written this down instead of telling you I am "very responsive."

## 15. What we have not decided yet

The honest section. Neither of us has an answer to any of these and we are not going to invent one before your call.

**About the stock numbers [P]**
1. How you would get the correct stock number. The site's number and the shelf's number disagree, and Rakesh will tell you the shelf is right.
2. How the floor for each of 900-odd products gets out of my head. I will sit and do it if someone makes me, but I do not know whether that is a day or a fortnight, and I do not know what happens to the 200 new SKUs.

**About the list itself [P]**
3. What happens when the same problem appears twice. If a product is low on Monday and still low on Tuesday, is that one thing on my list or two? I do not want to see it twice. Or maybe I do, if nobody has done it.
4. Whether the completed things being cleared out after a week can coexist with wanting to look back over a week. See section 11, point 3.
5. Whether the returns mess belongs in this. Probably not. I will stop.
6. Whether "closed in the tool" counts if someone ticks it on the board and does the actual thing in Shopify. That is most of the work, so it matters what counts.

**About the sheet, WhatsApp and the phones [P] [D]**
7. Whether keeping the Google Sheet in step in both directions is actually a sensible thing to ask for. Priya wants it. Dev suspects it is the most expensive line in this document. Neither of us knows.
8. Whether WhatsApp is a channel you can even use for this, what it costs per message, and whether sending order numbers into a WhatsApp group is consistent with section 12. Nobody here has checked.
9. Whether Rakesh's phone can run whatever this is. Someone should look at the actual phone.

**About the shape of the engagement [D]**
10. Whether phase 1 by 25 September is real or whether I have picked a date I liked. Tell me which.
11. What happens between 8 October and 5 December if phase 1 has a bug my team cannot work around. I have written "it comes to me and I decide" and I have not thought past that sentence.
12. **What happens after go-live.** Who fixes things, for how long, how we are told when something has broken, and what that costs. We have not discussed it at all and I would rather see it priced than assumed.
13. How much care this needs. It touches orders and my store's data but not payments and, if section 12 holds, not customer data. I do not know where that lands on whatever scale you use, and I would like the scale explained and the price difference shown.
14. Who our decision-maker for board behaviour actually is — Priya or Farhan. Section 14.
15. What we do about the two temp people during Diwali who will never have seen this tool.
16. How much of everything above is unreasonable. **[P]** Tell me. I would rather be told now than find out in three months, which is what happened with the last two things we tried.

## 16. What we are not asking for

So the number you give us is a number for something. Returns and refunds processing. Anything touching our accounts or vendor payments beyond a task that says "call the vendor." Replacing Shopify or moving off it. Anything that emails or messages our customers. Barcode scanning or anything that changes what Rakesh physically does on the floor. Purchasing, forecasting or vendor purchase orders as a system. A customer-facing change of any kind.

## 17. What we would like back from you **[D]**

1. One number inside ₹18–26 lakh, with what is in and what is out, and which parts of it you are least sure of.
2. The date question answered: is phase 1 by 25 September real, and what would you cut to make it real.
3. Which of the contradictions in section 11 cannot both be true, and what you recommend giving up on each.
4. The named AI provider, in writing, before the first document is uploaded, and how it sits against our data processing agreement.
5. Named people. Who is actually doing this.
6. What happens after go-live, and what it costs.
7. **A written list of the checks you run on our project, and which of them exist on our project today and which do not.** In your words, not ours. If one has never actually run and caught anything, the list says that. Section 13 is the whole of my position on this.

---

### Version history

| Version | Date | What changed |
|---|---|---|
| 0.1 | 2 August 2026 | Priya's notes, handwritten, typed up 4 August |
| 1.0 | 5 August 2026 | Dev's brief, written separately, before reading Priya's |
| 1.1 | 6 August 2026 | The two merged into one file. Disagreements between them left in and collected in sections 11 and 15 rather than resolved. Sent to devx labs. |

**FICTIONAL — see the notice at the top of this document.**