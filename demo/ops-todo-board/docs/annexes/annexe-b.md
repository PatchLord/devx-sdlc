> **FICTIONAL — part of a simulated engagement.** Marigold Living does not exist. See `../../README.md`.

> Annexe to the Statement of Work v1.0, 11 August 2026. The signature document is `../sow.md`;
> where the two differ, **the signature document governs**.

# Annexe B — The checks, and the honest status of each

Every check this engagement runs, what it protects, and whether it is *written*, *proven* or *to build* on 11 August 2026. Referenced from §5.

## What we check before anything ships — and the honest status of it

### 5.1 What we do, in plain language

Agents write most of the code on this engagement. That is stated plainly in §10 and it is why this section exists at all: when generation gets cheap and checking does not, the thing worth buying is the checking.

- **One repository, in Marigold's organisation, from the first commit.** Nothing is pushed straight to the main branch. Every piece of work gets its own branch and its own pull request. That the main branch is protected at all is a setting on Marigold's account, not something we can impose — §5.5.
- **Intent is written down before the code exists.** Each piece of work starts with a short spec that a person approves, and that spec has to be the branch's first commit and an ancestor of every code commit on it. **What is enforced is ancestry, not chronology.** v0.9 said intent "cannot be back-dated", and that is not true as written: commit dates are trivially settable and a branch that started with code can be rebased into legality. The honest sentence, and the one that is worth something: **a branch where the code came first cannot merge without being rebuilt, and the rebuild is visible.**
- **A change cannot quietly weaken the things that check it.** If a pull request edits an existing test, a coverage threshold, the pipeline configuration or the acceptance criteria, that edit has to sit in its own commit where a reviewer can see it. It cannot ride inside a change to the product.
- **Small pieces.** A pull request warns above 300 changed lines or 10 files and fails above 400 or 20. Going over is a person's decision, taken by someone other than the author. The reason is not tidiness: on large diffs, reviewers skim, and skimming and reviewing look identical afterwards.
- **Format, lint, types, tests and build run as one command**, locally and again on the server, and that command **fails rather than skips** when something is not wired. A repository that documents six checks and runs four reports green for the two that never ran.
- **80% coverage on the lines this change touched** — not on the whole repository. A whole-repository number is one you inherited; a changed-lines number is one you earned.
- **A fresh agent session reviews every diff** with no memory of having written it, and every finding it raises ends either fixed or dismissed in writing. Never neither.
- **A second human on the paths where being wrong is expensive**: **authentication and the session boundary**, personal data, permissions and authorisation, phase 2's notification path, **phase 2's webhook receiver**, database migrations, the pipeline configuration, existing tests, coverage thresholds, and the acceptance criteria themselves. An agent may propose a change to a criterion; only a named person approves one, or criteria become a description of whatever got built. Two of those entries are new in this version, and both were in scope in v0.9 with no place on this list. And the mechanism that produces the *second* human is itself unproven — see §5.2 and Setup exit 4.
- **Secrets and known vulnerabilities are scanned on a clock**, over the whole tree, not only on the diff — because an issue introduced by a change that passed is invisible to anything that only reads new changes.
- **One job asks the hosting platform what it actually enforces and fails when that stops matching what this document claims.** This is the check that makes the other checks' claims honest. Our own pilot's context file asserted that its main branch was protected; there was no remote and the pipeline had run zero times. **That job reports. It cannot prevent** — §5.5.
- **No developer or agent session holds production credentials.** The session cannot reach production because the credential does not exist in it. That is not an instruction to the agent; it is an absence — and because it was an absolute in v0.9 with no status row anywhere, it now has one in §5.2 that says exactly how far the absence goes and what it does not cover.
- **A weekly demo of working software.** Wednesdays, 09:30 IST, 30 minutes, recorded, avoiding Dev's Tuesday and Thursday afternoons. Software doing something, not a deck and not a percentage complete.

**§5.1 names the surfaces. §7 is where each becomes a criterion with an artefact against it, and three of them are new in this version.** A protected path with nothing in §7 asserting anything about it is a line in a text file — the same failure §5.2's ownership row describes from the other direction. So, written out here so that a reader can check it rather than trust it, §7 must carry:

1. **The login boundary** (§7.1) — every route on the board refusing a request with no valid session, enumerated from the router rather than sampled; the sign-in boundary driven in a browser; session expiry; and a closed account's session ending. v0.9's permissions criterion began at "everyone sees every task", which assumed the answer to the question nobody asked.
2. **The scheduled reader's four failure modes, as four criteria** (§7.1) — it did not start, it processed zero rows, it ran twice, the failed-signal queue is not empty — each with the alarm's own test run as its artefact. Both of the board's auto-signals hang off that reader, and if it dies on 2 October the board looks calm.
3. **The phase-2 receiver's authenticity** (§7.2) — an unsigned or mis-signed payload rejected and counted, and a valid payload replayed outside its freshness window rejected.

If any of those is absent from §7 when this document is signed, then this section is describing a perimeter the criteria do not have, and that is worth catching before signature rather than in a release document in October.

### 5.2 The honest status of every one of them

Read the status words literally.

- **Written** — the file exists and its logic has been exercised away from a live host.
- **Proven** — it has run on a host **and failed something it was supposed to fail**.
- **To build** — it protects nothing today.

**Nothing in this table says *proven*, and that is not modesty.** Our process has not run end to end on a host. The middle column has been changed since v0.9, which said "at Setup" on nine rows — a commitment wearing a status's clothes, in a table whose entire purpose is status. It now says what is true on **11 August 2026**, which for almost every row is *nothing*, because Marigold's repository does not exist yet. What each becomes is Setup's job; when Setup runs is in §8's schedule; and the four things that prove Setup actually finished are in §5.3. The right-hand column is the honest state of the mechanism itself, on our side, today.

| What it does | On Marigold's project, 11 August 2026 | Status of the mechanism |
|---|---|---|
| Rejects a pull request over the size ceiling | nothing — no repository yet | **written.** Its logic was run against 30 deliberately broken cases away from a host; it rejected what it was meant to reject, discriminated between the cases, and found a real defect in our own code doing it. It has never blocked a merge on a live host |
| Requires an approved spec as the branch's first commit | nothing — no repository yet | **written**, same harness, same limitation. No check proves a spec was *read*, and what it enforces is ancestry rather than chronology — §5.1 |
| Forces a gate change into its own commit | nothing — no repository yet | **written**, same harness, same limitation |
| Format, lint, types, tests, build as one entry point | nothing — and it is not wired to this stack, which is Setup work with an owner | **written — and deliberately fails while unwired.** Wiring it to this project's stack is Setup work, not a given |
| 80% coverage on changed lines | nothing — no repository yet | **written.** It skips when no coverage report is produced, which is a hole we will close during Setup rather than describe as closed |
| A fresh session reviews every diff | nothing — and it needs a model key on Marigold's account, per §8.2 | **written — and fails rather than passing when it is not configured**, because a review job that quietly does nothing shows a green tick for work nobody read |
| Every review finding ends fixed or dismissed in writing | nothing — it is a setting on Marigold's repository | **written**, enforced by the host's own setting rather than by us |
| Second human on protected paths | nothing — the ownership file does not exist and its patterns have never been matched against this project's folders | **written**, with two dependencies said out loud. A pattern that matches nothing is owned by nobody while still reading as protected. And **the mechanism that produces the *second* human — two owner entries, because the host has no per-path approval count — is believed to work and has never been tried.** Setup exit 4 is the first time it will be. Until then every second-owner claim in this document, at Standard and in §4.4's High column, is a claim about an untried mechanism |
| Nothing pushed straight to the main branch | nothing — the setting does not exist because the repository does not | **to build, per repository.** It is a setting on Marigold's account, and it has to be turned on and then tested. It also depends on their repository plan supporting it — §8.2 |
| The host's real configuration matches this document | nothing | **written — untestable until it has run once against a real repository.** It reports a mismatch; it cannot prevent one — §5.5 |
| Secret scanning over history, daily | nothing | **written**; the host's own push rejection is **to build** |
| Dependency and code scanning, daily | nothing | **written**; needs the host's alerts switched on, which is Setup work with an owner |
| No developer or agent session holds production credentials | nothing to hold — there is no production and no credential until §5.4's provisioning on 18 September. From then, the deploy identity belongs to the pipeline and is issued to no person and no session | **an arrangement, not a mechanism, and to build as a check.** Nothing scans a session for a credential it should not have. What exists is that the credential is never issued into one. Somebody with administrator rights on Marigold's account could put one in a session tomorrow and nothing of ours would go red. The absence is real, it is the single most load-bearing rule in this section, and it is not self-enforcing — which is why §11.4's fix path during the freeze window is written as a pull request through the same gates rather than a person with a terminal at 23:00 |
| Checking that the tests would fail if the code were wrong (mutation testing) | not planned | **to build.** No tool, no threshold. One of the rows that made us decline High |
| A full audit trail of who changed what | not planned at Standard | **to build.** The second one |
| Ticket status derived from what happened rather than written by an agent | recorded by hand by the tech lead from the first ticket | **to build** as an integration, **and an exception** — that word deliberately — to something our own process lists as never bending at any depth, at any novelty grade, in any project shape. **Karan Iyer carries that exception**, it is recorded in this document's accepted-risk section with his name on it, and the consequence is stated rather than left implicit: §11.5 promises every invoiced hour maps to a ticket on a board Marigold can see, and until the integration exists that board is maintained by a person. An agent will write to any completion signal it is given; our own pilot marked its own work done |

### 5.3 The one place this stops being a written claim

Setup does not end when the files are in place. It ends with **four** things Marigold can look at:

1. One trivial page — a build identifier and nothing else — **live in dev, put there by the real pipeline**, with the build id matching a tagged commit and a pipeline run.
2. The job that reads the host's configuration back has run on the host and passed, with a link to the run.
3. **One throwaway pull request has been deliberately blocked by a check**, with a link to the run that blocked it.
4. **One pull request on a protected path has had a code-owner review demanded of it and satisfied**, by the second owner rather than the author, with a link to the run. New in this version, and it exists for two reasons. An ownership pattern that matches nothing is owned by nobody while still reading as protected, and a group named in that file which does not resolve blocks every merge with an error message that explains nothing. Until this has happened once, every protected-path sentence in §5.1, §7 and §12 is decoration. It is also the only thing that will tell us whether the two-owner mechanism §4.3 and §13.4 both rely on works at all.

The third and fourth are the ones that matter. Until a check has been watched failing, we have tested that it runs, not that it stops anything — the same way a backup nobody has restored is a belief. **When those four exist, we will re-issue the table in §5.2 with the rows that moved and the run links against them.** That is the only route from *written* to *proven* on this project, and it happens before the first feature ticket, not after the freeze.

Setup is also the stage that gets cut when a timeline slips, and it is the worst possible thing to cut: every standard added later leaves everything written before it unchecked, and that debt appears in no diff. If the 25 September date comes under pressure, **features come out of phase 1 and Setup stays** — in the order ranked in §2.3, so that nobody has to negotiate it in the third week of September. That is a commitment in this document, not a preference.

### 5.4 Production, named

Standard depth buys dev and uat. Four real people work real orders from 25 September, and that does not happen in dev. v0.9 said "Environments: dev and uat", proved one page live *in dev*, and promised four people on real orders — three sentences that do not fit together, and Dev's own document forbids "we'll sort out production later" in those words. So:

- **There is a production environment**, provisioned by **Friday 18 September 2026** — a week before the 25th, not on it — in a region named in the design document before anything is provisioned, and inside the running-cost band in §11.3.
- **Karan Iyer provisions it and owns it.** At Standard it is **not** defined in code before it is provisioned. That is High's row and we are not claiming it, and the cost of not buying it is exact rather than rhetorical: an environment set up by hand can be reproduced only by the person who set it up, from notes, and that person is one person. It is a hole we are describing, not one we are hiding.
- **What runs there is the artefact that was promoted, not a rebuild.** §7.1 carries the criterion and its artefact: the build identifier live in production matches a tagged commit, a pipeline run, and the same artefact that passed in uat.
- **Nothing is patched on it by hand.** The deploy identity belongs to the pipeline; no person and no session holds it. That is what §5.1's credentials rule means in practice, and §5.2's row for it says how far that goes.
- **A defect fix inside 8 October – 5 December reaches production only with Dev's sign-off per fix**, per §6 row N-6, through the same gates as any other change.

### 5.5 The perimeter reports. It cannot prevent

Every gate in §5.1 is a setting or a token on a repository Marigold owns, in Marigold's organisation, on Marigold's card, with Dev as owner. That is what P1-11 buys and we are not proposing to change it. What has to be said out loud is the consequence, because v0.9 said "it is a setting on Marigold's repository" and stopped there:

**Dev — or anyone at Marigold given administrator rights — can switch off a required check, change branch protection, or rotate the token our configuration job reads with. Our answer is that the job *reports* it, the next time it runs. It cannot prevent it.** There is no version of this in which a supplier's document enforces something inside a client's account, and a document that implies otherwise is describing a perimeter it does not have.

Three things instead of that implication:

- **One named administrator on the repository: Dev Rawat**, and nobody else, per §8.2. A gate is not removed by somebody who did not know it was a gate.
- **A gate removed mid-phase stops merges the same working day**, and it is said at the Wednesday demo rather than worked around. Merging past a missing gate is our own pilot's failure with a client's name on it.
- **The one exception in this engagement is named as an exception** — the hand-maintained ticket status in §5.2's last row, with Karan Iyer's name on it — so that a non-conforming corner of this project is a recorded decision rather than a silent hole. If a second one appears, it gets a row and a name in the same way.

And the honest limit of this whole section, which is the same shape twice: **nothing we run can see a change made inside the Shopify admin** (§6, N-1), and **nothing we run can stop a change made inside Marigold's repository settings.** Both are holes. Both are in this document as holes rather than as things we quietly hope nobody tests.

---
