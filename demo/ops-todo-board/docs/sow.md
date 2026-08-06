> **FICTIONAL DOCUMENT — CREATED FOR A DEMONSTRATION.** Marigold Living does not exist. Dev Rawat, Priya
> Menon, Anjali Sharma and Karan Iyer are invented, as is every date, order number and rupee figure. devx
> labs' process is real; this client and this engagement are not.

# Statement of Work — Ops To-Do Board

**Marigold Living and devx labs · v1.0 · 11 August 2026**

This is the agreement. It is two pages because it should be possible to read all of it before signing it.
The full terms are in [`sow-terms.md`](sow-terms.md) and the detail behind those is in
[`annexes/`](annexes/) — nothing has been shortened away, only moved so that the sentences that decide
whether to sign are not on page forty.

## What we are building

A shared to-do list for Marigold's operations team. A person adds a task, assigns it to somebody, marks it
done, and can put it back if it was not. Some tasks appear on their own when the store crosses a stock floor
or an order passes its dispatch promise. Phase 2 adds due dates that mean the same afternoon to everybody and
one reminder before something is late.

**Phase 1** lands **Friday 25 September 2026**, with three items following by **Friday 2 October**. Phase 2 is
December 2026 to January 2027 and is **not approved by this document**.

That date is conditional and the condition is named: it holds if the decisions in §9 of the terms are
answered inside their stated windows. One of them, the fulfilment-clock question, has a consequence already
agreed — if it is not answered by **Friday 14 August**, the late-order signal covers India-warehouse orders
only in phase 1 and the UK moves to phase 2.

## What it costs

| | | |
|---|---|---|
| **Phase 1 core** | **₹11.6 lakh** | firm |
| The sheet import and mirror tab | up to **₹2.2 lakh** | quoted 28 August, capped |
| After go-live support | **₹0, ₹1.6 or ₹2.9 lakh** | Marigold's choice, §11.4 of the terms |
| A pre-breach warning, priced and not bought | **₹1.1 lakh** | displaces work rather than adding to it |
| Phase 2 | **₹6.0 – 7.5 lakh indicative** | not approved here |

**There is no total row, deliberately.** A single figure would add a firm number, a capped later quote and an
unchosen option, and it would be quoted back as a commitment. In 2026 Marigold is exposed to **₹11.6 lakh at
the floor and ₹16.7 lakh if every option is bought at its ceiling.** Both ends sit inside the ₹18–26 lakh
envelope approved in writing on 5 August.

Payment is five milestones, with **10% retained until the 90-day review on 25 November.** Schedule in §11.6
of the terms.

## Four things to know before signing

**1. What we will not verify.** Thirteen things, each written down rather than discovered later. The ones
worth reading first: we do not verify that Shopify's stock number matches what is on the shelf, and the whole
stock signal fires off that number; phase 1 cannot reduce the count of late orders, because it only fires
after an order is already late; and we do not verify behaviour under Diwali load, because a load test is not
in this depth and is not being bought. The full list is §6 of the terms.

**2. An agent writes most of the code, and three parts of our position on that are not finished.** We cannot
demonstrate that agent-written code is provably original, and Karan Iyer will not sign a warranty saying we
can. Our policy on what an agent may *read and transmit* is half written, and the engagement note that closes
it is a precondition of the first read of Marigold's store rather than a document that follows it. And whether
commits in Marigold's own repository carry a permanent record that a session wrote the code is Dev's decision
to make, not ours — the default is that no such record is written. §10 of the terms, Annexe E for the detail.

**3. What we need from Marigold, and when.** Read-only store access, a written reply naming the model
provider and its terms, a signed controller/processor agreement, two hours a week from Priya, and the stock
floors for the roughly sixty products that actually move. The first three are **preconditions of any work on
Marigold's material at all** — not requests that can slip. Dates in Annexe D.

**4. Every claim we make about our own checks is graded.** Our process has been tested but has never run end
to end on a live repository, so **no check in this document is described as proven.** Each is *written* —
its logic tested against deliberately broken cases — or *to build*. Annexe B has every row and its status.
Anything sold to Marigold as stronger than that is an error we would want reported back.

## How work gets accepted

Every acceptance criterion names the artefact that proves it — a test, a screenshot, a query output. **A
criterion with prose in that column fails a release rather than passing it**; "verified" is not evidence.
Priya accepts each release, and a release document lists what it does *not* verify alongside what it does.
Criteria in Annexe A, mechanics in §7 of the terms.

## Changing it

Scope changes go through Anjali Sharma and are priced before they start. Nothing changes what Marigold has
already accepted. §12 of the terms.

## Risks somebody has accepted by name

Thirteen risks were argued and left rather than fixed, each with an owner so that if one goes wrong it was a
decision rather than an accident — seven carried by Karan Iyer, two by Anjali Sharma, four by Dev Rawat. They
are listed in §15 of the terms, and the four in Dev's name are the ones to read before signing.

## Signatures

| | | |
|---|---|---|
| **Dev Rawat** | founder, Marigold Living | signing for the scope, the price, the four things above, and the four risks in his name |
| **Anjali Sharma** | delivery lead, devx labs | signing for the dates being achievable on the stated conditions, and for the commercial terms |
| **Karan Iyer** | tech lead, devx labs | signing for every technical claim being one he can stand behind, and every gap being named rather than smoothed — **including his refusal to warrant that agent-written code is provably original** |

Full signature block, with what each person is and is not signing for, in §13 of the terms.

---

**Reading path.** This document → [`sow-terms.md`](sow-terms.md) for the wording →
[`annexes/`](annexes/) for the tables. Where this document and the terms differ, **this document governs**;
where the terms and an annexe differ, the terms govern.
