> **FICTIONAL — part of a simulated engagement.** Marigold Living does not exist. See `../../README.md`.

> Annexe to the Statement of Work v1.0, 11 August 2026. The signature document is `../sow.md`;
> where the two differ, **the signature document governs**.

# Annexe E — AI use, in full

The data inventory, the preconditions of the first store read, the provenance options, and what our position does not yet cover. Referenced from §10.

## AI use on this engagement

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

| Data | Purpose | Held where | Retention |
|---|---|---|---|
| **Staff names** (4 rising to 7, including two temps) | Assignment, and showing who has what | Board database | For the life of the account, plus a period for the completion history below |
| **Staff phone numbers** | The message that a task landed on their name | Board database and, in transit, the messaging provider | **Removed from the live database when the account is closed.** Backups are not edited, so the number persists in them until they age out on their own schedule — **35 days**. Temp numbers are removed at the end of the festive window on the same terms |
| **Staff action history** — who assigned, who completed, who reopened, and when | Priya's ability to put a task back, and the reopen view in P1-16 | Board database | **The one row Marigold's adviser must set a number on.** Our conservative default is 24 months, per D-10 |
| **Reopen statistics per named person** | Priya's stated purpose: being able to hold something up in a conversation she has already had twice | Derived from the row above | As above |
| **Order numbers, SKUs, quantities, timestamps, dispatch clocks, assignee** | The work itself | Board database, and in transit to the messaging provider in the assignee message and the 08:00 digest | For the life of the system |
| **Free-text task content** | A person describing a job in their own words | Board database and its backups. **It does not leave the board in a message** — the assignee message and the digest carry a task reference, the order number and a name, never the free text | For the life of the system |
| **Customer names, email addresses, phone numbers, shipping addresses** | **Not ingested by the board.** A task says "order 41892, dispatch clock at 39 hours". Whoever works it opens Shopify, where the data already is and is already governed. **Handled once, outside the board, by S-1's discovery read — see §10.6** | Not in the board's database. S-1's extract sits on Marigold's own storage, outside every agent-readable path | S-1's extract is deleted when D-1 is answered and written up, and no later than **31 August 2026**, with the deletion recorded |

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
