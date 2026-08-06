> **FICTIONAL — part of a simulated engagement.** Marigold Living does not exist. See `../../README.md`.

> Annexe to the Statement of Work v1.0, 11 August 2026. The signature document is `../sow.md`;
> where the two differ, **the signature document governs**.

# Annexe F — Depth, and why not High

The full reasoning, the compensating controls, and the two triggers that reopen the decision. Referenced from §4.

## Depth: **Standard**

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

| | **Standard — what Marigold gets** | **High — declined** |
|---|---|---|
| Required checks before any merge | size, gate-change, spec-ancestry, verify, review | the same five |
| Approving reviews | 1, plus code-owner review on protected paths. The second owner in §13.4 comes from a second owner entry, and that mechanism is unproven until Setup exit 4 in §5.3 | 2 on protected paths — **to build**, for the reason in §4.3, and in the same evidential state as the two rows below |
| Coverage on the lines a change touched | 80% | 80% plus mutation testing — **to build** |
| Environments | dev, uat, **and a named production environment** — what it is, when it exists and who provisions it is §5.4 | the same, plus production **defined in code before it is provisioned**. That is the row this project does not buy, and §5.4 says what it costs us not to |
| Monitoring | errors grouped with the release that introduced them, searchable logs with personal data stripped before they leave the application, alarms on error rate, p95, p99, saturation, and the four that get forgotten on anything scheduled: it did not start, it processed zero rows, it ran twice, the dead-letter queue is not empty — **and on this project those four are acceptance criteria in §7.1, not monitoring wishes**, because the board's two auto-signals both hang off a scheduled reader | plus a full audit trail of who changed what — **to build** |
| Data outside production | invented data only in dev and uat. See §10.5. The one activity that handles real customer data is S-1, and it is governed in §2.0 and §10 rather than by this row | the same, plus any dry run on live records under production's own access controls |
| Release check | the standing list, with the third column | plus load test, threat model, restore drill with the time recorded |
| Launch and after | the checklist; support per §11.4 | rehearsed launch, someone on call, a runbook per alert |
| **Indicative price effect** | included in §11 | **+₹2.5–3.5 lakh on phase 1, and +₹12,000–18,000 a month running** — against a ₹35,000 ceiling. Three of its rows would be commitments, not checks |

Depth is re-checked if the answers change. It goes up with them and it never quietly goes down. Two triggers are named in §4.3. One event is scheduled rather than triggered: **the four questions are asked again, in writing, at the start of phase 2**, because a public endpoint that creates work for seven people is a different answer to the first question, and because any phase-2 write to the store would be a different answer to the second.

---
