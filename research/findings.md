# Findings ledger

Every claim we have examined, and what happened to it. Append-only: a refuted finding stays here so
nobody re-litigates it, and a source covering old ground becomes a grep instead of a workflow.

**Verdicts.** `accepted` — changed the manual. `refuted` — examined and rejected, reason recorded.
`corroborates` — true, already covered, no change. `unsourced` — direction may hold, digits dropped.

**The rule for accepting anything:** it must change what a developer does on Monday. A finding that
only changes how the manual reads is an edit, not a finding.

---

## Adjudicated

| # | Claim | From | Verdict | Outcome |
|---|---|---|---|---|
| 1 | Speed is the constraint; AI makes delivery faster | general | **refuted** | Checking is the constraint. Idea 1. |
| 2 | METR: developers 19% slower while believing 20% faster | METR, early 2025 | **unsourced as current** | Measures early-2025 tools. Follow-up redesigned; no control group exists any more. Dated in §3, never quoted as current. |
| 3 | Productivity effect is large | meta-analysis, May 2026 | **accepted** | g = 0.33 [0.09, 0.58], smaller in enterprise than lab. Replaced all single-trial claims. |
| 4 | Output rises measurably | Microsoft, Jul 2026 | **accepted** | +24% merged PRs, sustained 4 months. Authors' own caveat used as Idea 4. |
| 5 | Greenfield RCT: 55.8% faster | arXiv 2302, Feb 2023 | **retired** | Three years old. Removed rather than dated, since the meta-analysis supersedes it. |
| 6 | Agent swarms for one ticket | AWS AI-DLC | **refuted** | Parallel agents are safe only when they need not agree. Sequence, not concurrency. |
| 7 | Human review on every pull request | AWS AI-DLC | **refuted** | Arithmetic fails at 60 tickets. Review is per path, not per project. |
| 8 | Hooks as the enforcement layer | general | **refuted** | `--no-verify` walks past them and an agent can edit the hook files. |
| 9 | Whole-repo coverage as a gate | general | **refuted** | 78% suite at 31% mutation passes it. Changed lines only. |
| 10 | Mob elaboration replaces async handover | AWS AI-DLC | **refuted as an edit** | Depends on controls our enforcement lacks; §01 already puts QA in the room. Still open as an org question, see open-questions. |
| 11 | "Understand every line you ship" as a rule | AWS AI-DLC | **refuted** | Unenforceable, so writing it down makes it a wish — ideas 3 and 4. The author's obligation is real; the rule is not writable. |
| 12 | Velocity multiplies defect rate (arithmetic) | AWS AI-DLC | **refuted** | We have the measured form: incidents per PR up 242.7%. Measured beats hypothetical. |
| 13 | Point the agent at a reference implementation | AWS AI-DLC | **corroborates** | Spec template already requires naming existing patterns. |
| 14 | Context is a managed resource | AWS AI-DLC | **corroborates** | Fresh context per role, committed fixtures, already in the loop. |
| 15 | §11 measures only inside the build loop | our own sources file | **accepted** | Our sources said measure "lead time, PR size, review time and defect rate"; we had two of four. Added numbers 5 and 6. |
| 16 | Novelty is a routing axis, distinct from cost | Karpathy, nanochat | **accepted** | Well-trodden / novel here / genuinely novel. Sets leash length, not apparatus. |
| 17 | "Vibe coding" was coined for throwaway work | Karpathy, Feb 2025 | **accepted** | One attributed line; the attribution is the fact. |
| 18 | 95% of AI pilots fail | AWS leader talk | **refuted** | Non-peer-reviewed working paper, 52 interviews, by a project selling the recommended fix. Talk also invents a causal link the study never makes. |
| 19 | Juniors ship 17% more code, understand 17% less | AWS leader talk | **refuted as stated** | Fabricated symmetry. Real finding: 17% lower comprehension (n=52). No "17% more code" exists. |
| 20 | AI generates 10x faster, 3x harder to validate | AWS leader talk | **refuted** | No source found. Invented precision. |
| 21 | Deskilling erodes verification skill | Anthropic + meta-analysis + BairesDev | **accepted** | Three converging sources. §14 gained the risk and three usage rules. The usage pattern, not the tool, decides. |
| 22 | Policy enforcement outside the model loop | Singapore IMDA, Jan 2026 | **accepted as corroboration** | Independent confirmation of the perimeter principle. Exposed one real gap: agent identity. |
| 23 | Four-layer governance | AWS leader talk slide | **partly accepted** | Three of four we have. Embedded security specialist we will not have; said so plainly. Prompted the scan.yml audit. |
| 24 | Security scanning belongs in the enforcement table | **our own audit** | **accepted** | We cited 41.1% survival to HEAD and shipped no gate. Built `scan.yml`, scheduled not per-PR, because the survivors were introduced by changes that passed. |
| 25 | The bottleneck shifts from building to deciding | AWS leader talk | **deferred to a question** | Not a doc change: we have no data on our own decision latency. Opened as C5, and it is measurable from number 2 once the wait is split into waiting-on-us and waiting-on-them. |
| 26 | Code is free; the scarce resources are human time, human and model attention, and context window | Lopopolo, OpenAI, Feb 2026 | **accepted as sharpening** | Our Idea 1 said "checking is the constraint". Naming *three* scarce resources, two of them attention rather than time, explains why context efficiency is a practice and not tidiness. |
| 27 | Skills should let the agent operate the project, not just describe the process | same | **accepted** | The largest gap the transcript exposed. We mandated evidence for anything with an interface and shipped nothing that could boot an app or drive a browser, so it always fell to a person. Built `operate-app`. |
| 28 | Garbage collection: a scheduled slot converting slop into checks | same | **accepted** | We had the principle with no method and no time. Built `garbage-collect` and put an hour in the weekly rhythm. Their version also runs automated refactor PRs — not adopted, see open questions. |
| 29 | A failure message should be a prompt, not a diagnosis | same | **accepted** | Audited all 25 agent-actionable gate failures; four diagnosed without remediating and now carry the fix. 21 of 25 pass. |
| 30 | "Every time you type continue, the harness failed" | same | **accepted as a diagnostic** | Added to the developer section as the sharpest available signal of harness maturity. Not made a seventh number — see open questions. |
| 31 | Make everything the same, for context rather than tidiness | same | **accepted** | One canonical helper, one way per thing, because transferable context makes the model's output predictable. Added as the closing habit of the build loop. |
| 32 | Structural tests: file length caps, layer dependency direction, one canonical implementation | same | **deferred to a question** | A class of check we do not have and probably should. Needs project-specific values, so it is a question rather than an edit. |
| 33 | Enforce invariants, do not micromanage implementations | same | **corroborates** | Already how our gates are shaped — we check the diff, the ancestry, the mixing, never the design. Worth having the phrasing. |
| 34 | Plans should be pushed as a PR and reviewed line by line before kickoff | same | **corroborates strongly** | This is our spec gate, arrived at independently from the opposite direction. He warns that approving an unread plan encodes instructions you do not want followed. |
| 35 | Zero human review before merge; ~10x speedup | same | **refuted for us** | Their context: greenfield, one internal codebase, 3–7 senior engineers at a frontier lab, no client acceptance, no fixed price, ~$1,000/day per person in tokens. We answer to clients and have protected paths. The mechanisms transfer; the review posture does not. Their 10x is their own estimate on greenfield work. |
| 36 | Multiple review agents, one per persona, on every push | same | **deferred to a question** | We have one. Our own sources say four reviewer bots never agreed on a single finding, which argues for lenses rather than votes. Cost and dismissal-rate implications unknown. |
| 37 | Work the way the frontier labs work | user premise, tested | **refuted** | They disagree on the central question. OpenAI Frontier merged with no human review; Anthropic's Code Review will not approve a PR by design and a human retains final authority on every merge. Same year, opposite answers. The real question is whose *situation* resembles ours, and it is Anthropic's — external consumers, contractual exposure. Mechanisms transfer; the review posture does not. |
| 38 | Asking a human is free, so volume does not matter | user premise, partly refuted | **corrected** | Free for the agent, not for the human. Anthropic measured it: only 16% of PRs received substantive feedback because engineers were skimming to keep velocity. Same failure as our size ceiling, different place. Fix is not fewer questions but grading (Blocking / Worth knowing / Pre-existing) and routing by class, so attention is rationed rather than assumed infinite. |
| 39 | Build the autonomous runner | my own proposal, refuted by me | **deferred** | It removes a person typing two commands, about thirty seconds per ticket, and cannot be validated because nothing has run on a host. Ranked fourth behind agent-produced evidence (built), graded and routed escalations (cheap), and the escalation log. A runner driving an unproven loop would industrialise whatever is currently wrong. |
| 40 | A tuned reviewer with written criteria is not a generic bot | Anthropic, Mar 2026 | **accepted** | Under 1% of findings marked incorrect over months of production use, against the generic-bot studies we cite where four bots never agreed on a finding. The difference is written criteria in a `REVIEW.md` the team owns, separate from the context file. Worth adopting. |
| 41 | Big pull requests are where the defects are | Anthropic, Mar 2026 | **corroborates** | On PRs over 1,000 lines, 84% receive findings, averaging 7.5 issues. Independent support for the size ceiling from the defect side rather than the attention side. |
| 42 | Red-on-base: re-run a bug fix's new test at the base commit, require failure, store the proof | ADS-1 | **refuted as an edit** | The principle is right and we hold a weaker version at tier 2. The mechanism needs a machine-readable test report per harness plus an N/A disposition scheme, and `verify.mjs` hard-fails on a missing GATES script so a seventh entry reddens every repo until each wires a reporter. The selector (`fix:`) is author-declared behind a `--no-verify`-able hook, and a new test referencing a symbol absent at base fails by compile error — the one-line bypass. Recorded as experiment E6, not built. |
| 43 | Red-on-stub: revert new implementation hunks, require AC tests to fail | ADS-1 | **refuted** | ADS-1's own correction C1 destroys it: no 'new body' to stub when editing existing functions, and inapplicable to Liquid, config, IaC, SQL and JSON diffs; where reverting breaks the compile, every test "fails" and the gate reports success for tests asserting nothing. Our stack includes a Shopify theme with no instrumentation at all. |
| 44 | Consequence class derived from a path manifest, recomputed at PR time, auto-raised by CI | ADS-1 | **refuted as an edit, kept as a question** | Sharper than our depth grade, which a human sets once in the SOW. But ADS-1 concedes the design "rests on protected-paths.yml being COMPLETE", and a checkout-adjacent module nobody listed ships at the lowest class. It trades a wrong-in-both-directions human guess for a silent gap. See open question D10. |
| 45 | Four-point reviewer attestation, validated complete by CI | ADS-1 | **refuted** | ADS-1 mandates it at line 322 and demolishes it at line 900: four checkboxes are a four-second ritual that cannot be falsified. We already hold the position — a genuine approval and a rubber stamp are byte-identical on the host (11-measurement). Enforcing shape as a substitute for evidence is the thing finding 47 fixes. |
| 46 | A published review-capacity ceiling in evidence-weighted review units | ADS-1 | **refuted** | Conceded broken in the same file: every weighting input is produced by the author's own artefacts, so declaring `in scope: src/**` guarantees empty drift and prices the hardest diff as trivial. Its own counter needs call-graph fan-out analysis — a new product. Our dumber instrument (300/10 target, 400/20 ceiling) is gameable by splitting; theirs by typing one glob. |
| 47 | The production release-checklist gate enforces shape, not evidence | ADS-1's exposure lens, turned on our own file | **accepted** | `promote.yml`'s regex required cells 2 AND 3 both blank, while three of our documents said OR. So `\| Rollback tested \| verified \| \|` passed the production gate — a claim with nothing behind it. Verified by running it, including the break-it case in 09 that prescribed exactly this test and went green. Now a per-row Evidence check over `## Verification`, a missing section counts as failing, three break-it cases, mutation-tested. |
| 57 | Red-on-base is buildable, and the N/A case is mechanical rather than a waiver | E6, measured 6 Aug 2026 | **accepted — build it** | 11 of 12 real bug fixes in a public repository fail at their base commit with a captured expected/actual pair; the twelfth is a commit labelled `fix:` that adds a new file, so it fails on module resolution. The discriminator is not the language but whether the change alters existing behaviour or introduces a new symbol — which means the unsupported case can be decided from the runner's own report instead of by a tech-lead waiver. That removes the tension in ADS-1's own text, which asked for waivers while warning they spend gate credibility. Finding 42 refuted this as an *immediate edit* for build-cost reasons and that refusal was correct; the experiment is what changed. |
| 58 | A design system's tier-1 form is token lints, a11y lints, and protecting the lint config | D15, resolved 6 Aug 2026 | **accepted** | The lintable half is real and cited (`color-no-hex`, `no-arbitrary-value`, Stylelint Polaris), and it matters more for agents than for people: an agent with no token knowledge generates the most specific value it can. The half we were missing was `CODEOWNERS` on lint configuration — `gates.yml` already stopped a rule-disable riding inside a feature commit, and two break-it cases now prove it against the real commit's shape, but on its own commit the disable would have merged unreviewed. |
| 59 | Standing agent context is generative, not preventative | D15 | **accepted** | Twenty design rules in a live project's `CLAUDE.md`, plus a doctrine declared the source of truth, did not stop four a11y rules being switched off inside a 69-file commit. Context makes an agent produce the right thing more often, which is worth having; it prevents nothing. Counting it as enforcement is the error, and it generalises past design systems to every rule we write into a context file. |
| 60 | Red-on-base built, with the N/A decided mechanically and no waiver path | E6 → built 6 Aug 2026 | **accepted** | Four verdicts from the runner's own report: assertion (proof stored), cannot-load (N/A), passes-at-base (fails when the change declares a fix, warns otherwise), unclassifiable (fails, because a gate that cannot tell must not guess). The asymmetry on passes-at-base is the one place it takes an author's word for anything, and it is there because a regression test pinning working behaviour is *supposed* to pass at base. Ships un-required. Verified by a self-tested classifier against real captured output plus three end-to-end runs, one of which correctly rejected a `fix:` whose test only asserted a type. |
| 61 | A second person is structurally required, and GitHub enforces it | host proof, 6 Aug 2026 | **accepted, and now a fact** | `CODEOWNERS` pointing at the author, a protected-path change, and the approval attempt returns `Review Can not approve your own pull request`. Every document that said one person cannot run this was arguing; it is now demonstrated. The corollary is that a solo run must either bring in a second reviewer or record on its own report that the central gate was inoperative. |
| 62 | You cannot repair a broken CODEOWNERS once code-owner review is required | host proof, 6 Aug 2026 | **accepted** | GitHub ignores an owner it cannot resolve, so a file naming a non-existent team silently protects nothing — and requiring the review against it deadlocks the branch, because the file that must approve its own repair is the broken one. Order: land a working file, then require the review. The instinct is the reverse. |

### Round 8 — ADS-1 (6 August 2026)

An outside standard, ~21,800 words, arrived as a rival: eight principles, nine gates, and its own hostile
review printed inside it. Five independent lenses produced **34 candidates**; adversarial refutation left
**one**, and it was not a transplant — it came from turning ADS-1's exposure-grading lens back on our own
`promote.yml` and finding the last tier-1 gate before production did not enforce the predicate its own error
message claimed.

That ratio is the finding about the round. ADS-1 is better written than our documents on cost, latency and
self-attack, and it is a **source to mine rather than a rival**: it has no enforcement-tier concept, so a
four-checkbox ritual sits in the same numbered gate list as its strongest mechanism — and its own reviewer
supplies the consequence, that "the cheap ceremonial gates ship immediately because they are trivial, the
load-bearing ones ship broken or never". Two of its most distinctive mechanisms are conceded broken in the
same file.

Where it is ahead of us and we could not act yet: it hard-caps serial pre-code human approvals at 1/2/3 and
declares that exceeding the cap is **a defect in the standard, not a discipline failure in the engineer** —
our latency argument with an actual number. It pre-commits each gate's author to deleting their own gate if
escape-point data never implicates it, the only shrinking mechanism either document has. And its per-gate
"how this will be gamed" section attacks six of its own gates in the voice of a compliant employee, which is
a form worth stealing.

Where we are ahead, and it should mine us: **it has no perimeter check.** It pins gate-bearing config with
CODEOWNERS and sets branch protection once during rollout, but nothing reads the host back and fails when it
drifts — so all nine of its gates live where an agent can reach them. We also mandate one monorepo, which
dissolves its cross-repo classification hole, and we already put named third-party AI processing with written
client permission in the SOW, which is its own missing-category #1.
| 48 | `verify.mjs` runs `tests` before `build` | arvind-sbd | **accepted** | Where a workspace package is consumed as compiled `dist` — the topology `02-before-build` mandates — the tests import the previous build and pass for the wrong reason. Nothing in `verify.mjs` short-circuits, so the order was free to fix. That repo has had it right in CI for 250 commits and *still* needed a prose rule for the inner loop, so `10-stack-wiring` now prescribes a topological `dependsOn` too. No published incident attributes a defect to this; the doc says so. |
| 49 | "No session holds production credentials" closes a class it cannot reach | arvind-sbd | **accepted** | A dev-only or destructive script running *inside* a deployed container holds that credential by design, supplied by our own infrastructure. Their guard file records the incident: a dev seed's delete-then-recreate emptied `access_grants`, with a comment and one Terraform ternary as the only control. |
| 50 | Destructive scripts must refuse their own target | arvind-sbd | **accepted** | New `production-ready.md` section, four tier-1 rows: refuse a protected `APP_ENV`, refuse an undeclared host, refuse an absent connection string rather than guessing, read the URL the command will *actually* use, and test the guard by spawning the real entry point so a **deleted** guard fails. Public 2026 incidents match the shape exactly. |
| 51 | Auth-substitute paths need an allow-list **and** a held secret | arvind-sbd | **accepted** | Their deny-list version shipped under a docstring claiming it "can never be switched on in prod even by mistake", survived two further commits, and was fixed 16 days later. And the allow-list alone is not enough: their own IaC deploys the allow-listed name to a container app, where a bare header minted a principal. A published advisory adds the sharper case — `NODE_ENV` inlined to `"development"` by a bundler, so the guarded block ran in production. |
| 52 | `gates.yml` protects checks by enumerating three script names | arvind-sbd | **refuted** | `14-limits.md` already names this hole in the same terms and prices it deliberately. The proposed fixes self-defeat: `scripts/*.mjs` fails the commit adding a non-check script, and an added-`"off"` grep fails the commit introducing any lint config. What was real was maintenance: the list omitted Biome and Ruff, which our live projects use, and `board.mjs`, which now gates. Added. |
| 53 | The pilot's "0 of 7" measures distance from the work, not prose | arvind-sbd | **refuted** | The load-bearing claim is false. Their per-feature DAG board was out of sync for **fifteen days**, peak eight task IDs, reconciled by a batch re-bake — while rendering "56 done" on screen against a `tasks.md` at 64. So the proposed remedy, "make it visible in a rendered artefact", is the thing that failed. |
| 54 | `perimeter.yml`'s warning that `bypass_actors` is unreadable | arvind-sbd | **refuted** | The API claim is right; the consequence is refuted by the repo offered as evidence. Its ruleset covers `~DEFAULT_BRANCH` and `refs/heads/dev` in one object, so `perimeter.yml` with `main` hardcoded reads the same object and fails roughly ten assertions — it catches that repo's real hole loudly. |
| 55 | "Records are never updated" contradicts our own spec check | arvind-sbd | **refuted as proposed, accepted as a copy-edit** | Their `spec.md` has twelve post-initial commits deleting ~173 lines including whole requirement blocks, so the repo falsifies the stricter rule rather than supporting it. But our own table did contradict itself, so 17 now says "never *quietly* updated" and explains why `spec.yml` warns rather than fails. |
| 56 | Our own inline check passed while nine copies were stale | found while applying the above | **accepted** | `check-docs.sh` probed one line per starter file, so a drifted body was invisible if that line had not changed. Replaced with whole-body containment in `scripts/check-inlines.py`, which immediately found **nine** stale copies — `CLAUDE.md`, `explore.md`, `settings.json`, `build-loop`, the PR template, `spec.yml`, `verify.yml`, `lefthook.yml` and `break-it.mjs`. All resynced by scoring every fenced block against the file body and asserting one unambiguous winner. |

### Round 9 — a live spec-kit project (6 August 2026)

`devx-commerce/arvind-sbd`, dev branch, 250 commits of real client work. Unlike ADS-1 this was **evidence
rather than argument**, so the burden was inverted: our standard is written and unproven, theirs has shipped
features, and where they differed the burden sat on our document. Six lenses produced **45 candidates**;
four survived.

The verdict that matters: **the rules that survived 250 commits are the ones written as code with the
causing incident in the file. The rules that drifted are the ones written as documents to be maintained.**
Their fail-closed database guards hold and fail a build today. Their per-feature DAG board drifted for
fifteen days while displaying a stale count, and their plan documents became — in their own words —
"executable recipes… stale code, a regression generator". That is our tier table confirmed by an outside
project, and simultaneously an indictment of our artefact list, because we had no tier-1 form for the one
hazard they kept paying for: **a process that already holds the credential.**

Where they are behind us, and it is worth knowing before anyone treats spec-kit as sufficient: no
`CODEOWNERS` file at all, a ruleset bypass actor set to `always`, **zero required status checks** so CI is
advisory at the host tier, and ten-plus Playwright specs that no workflow invokes because the web workspace
has no `test` script. That last one is the first time one of our rules has caught a gap in somebody else's
repository rather than the reverse.

And the round found a defect in our own tooling, which is where the last four rounds have also found things.

## Where accepted findings have actually come from

Worth watching, because it should change where effort goes.

| Source of finding | Accepted |
|---|---|
| Auditing our own artifacts | `perimeter.yml` ruleset bug, self-grantable size override, missing security scan, `is_test_path` false positives, gates.yml self-blocking |
| Our own sources file contradicting the manual | numbers 5 and 6 |
| External reading | novelty axis, deskilling, governance corroboration |

Three of the last five accepted changes came from checking our own work rather than from reading.
