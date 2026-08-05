# What this does not do, and what we do not know

The holes in everything the other documents describe. Read it before you quote any part of this process to a
client, and read it again before you decide a green pull request means the work is right.

For the other side of the same ledger — what this changes against a developer with an agent and no process,
and what adopting it costs — see [outcomes](18-outcomes.md). That document is the case for doing this; this
one is what the case cannot support.

## Why the holes are written down

Every other document here describes something we built or decided. This one describes what those things
cannot do, and it stays in every version.

The first reason is operational, and it is the third of the five ideas in [why](01-why.md) turned on our own
work. A blind spot that is written down can be covered deliberately by something else — a demo, a second
reader, a decision to accept the risk. A blind spot that is not written down gets treated as covered, and is
then covered by nobody. A check that is documented but absent is worse than one never promised, and the same
is true of a check whose reach is overstated.

The second reason is honesty. This is a hypothesis with instrumentation bolted on, not a validated standard.
Saying otherwise in a document a client may read is how the failure in [why](01-why.md) happens again, with a
signature underneath it.

## What each layer cannot see

None of these is a defect waiting to be fixed. Each is the price of a check that is cheap, fast and
mechanical, and we paid it deliberately.

| Check | What a pass establishes | What it cannot see |
|---|---|---|
| `size.yml` | added + deleted lines and file count are under 400 / 20, excluding lockfiles, snapshots, `**/generated/**` and migration SQL | whether the diff is hard. 280 lines of concurrency logic passes; a 410-line rename fails. It cannot read the `size-override` justification either — it checks that the label exists, not that the pull request explains anything |
| `gates.yml` | no single commit mixes a gate-path change with implementation, and no added line introduces `continue-on-error: true`, `if: false`, `\|\| true`, `.skip(`, `xit(` or `@pytest.mark.skip` | a test left running with its assertions removed. A *newly added* test counts as implementation by design, so a weak assertion introduced in this ticket is invisible. Its gate-path list is literal — `*jest.config*`, `*vitest.config*`, `bunfig.toml`, `pytest.ini`, `.coveragerc`, `codecov.yml`, `.eslintrc*`, a few more. Add a tool whose config filename is not on that list and its thresholds are unprotected, silently |
| `spec.yml` | `docs/specs/<TICKET>.md` exists and is the branch's first commit, alone | whether the spec says anything. An empty spec passes identically to a complete one. It cannot prove a person read it, and a mid-flight revision produces only a `::warning::`, which nothing forces anyone to act on |
| `verify.yml` + `verify.mjs` | six named gates are wired in `package.json` and all six passed — it fails rather than skips when one is missing | whether a test asserts the requirement or the implementation. With the same model writing both, the assertion gets derived from the function. One worked example is 78% line coverage at a 31% mutation score |
| `changed-line-coverage.mjs` | at least 80% of the lines this pull request added or changed were executed by the suite | that executing a line means checking it. Coverage counts visits, not verdicts |
| `review.yml` | a fresh Claude session with `Read,Grep,Glob,Bash(git *),Bash(gh pr *)` read the diff and posted a comment; the job fails outright when `ANTHROPIC_API_KEY` is absent rather than skipping | whether the comment is correct, or whether silence means clean. We do not know this agent's accuracy, and the published numbers for the class are poor |
| `perimeter.yml` | the host's branch-protection API reports the contexts, approval count, code-owner requirement, stale-review dismissal, linear history, conversation resolution and force-push settings written into the job | anything the API does not expose, and anything that happened between runs. It fires on `cron: "0 7 * * 1"` plus pushes to `main` touching workflows, `CODEOWNERS` or `CLAUDE.md`, so a protection turned off Tuesday and restored Sunday leaves no trace. It checks that `CODEOWNERS` has a line for `/.github/workflows/` and one for itself — not that the owners named are still on the team |
| `scan-secrets.mjs` | twelve prefix patterns did not appear in staged content | anything not on that list, including a client's bespoke token format. It is a pre-commit hint, so `--no-verify` walks past it, and host-side push rejection is still *to build* |
| `CODEOWNERS` + required approval | a named owner clicked approve | whether they opened the file |

Read together, the honest summary of a green pull request is narrower than it looks.

```
  ┌─ A GREEN PULL REQUEST ESTABLISHES ─────┐  ┌─ IT DOES NOT ESTABLISH ────────────────┐
  │ the diff is under 400 lines, 20 files  │  │ that anyone read them                  │
  │ no commit mixed a gate change with code│  │ that a new test's assertions are real  │
  │ docs/specs/<TICKET>.md is commit one   │  │ that the spec describes this code      │
  │ format, lint, types, tests, build ran  │  │ that a test fails on a wrong answer    │
  │ changed lines are 80% executed         │  │ that executed means asserted           │
  │ a review agent posted a comment        │  │ that the comment was right             │
  │ someone with write access approved     │  │ that the person understood it          │
  └────────────────────────────────────────┘  └────────────────────────────────────────┘
```

### Two classes sit outside every check in that table

Every check above fires on one change and sees only that change. Two kinds of damage are invisible to that
design by construction.

**What many changes did together.** Across 211 million changed lines between 2020 and 2024, copy-pasted lines
rose from 8.3% to 12.3% of all changes while refactored or moved lines fell from 24.1% to 9.5%. No individual
pull request caused that, and no per-pull-request check could have flagged it.

**What happened while the code sat still.** Across 304,362 verified AI-authored commits, 24.2% of the
statically detectable issues introduced were still present at HEAD, with security issues surviving worst at
41.1%. A vulnerability published today lands on code merged three months ago.

The clocked jobs answer both — the scanners in [enforcement](06-enforcement.md) and the weekly drift read in
[run and support](03-delivery.md). They are a weaker instrument than a required check, and say so: a scanner
cannot judge, and an agent reading metric deltas can be wrong about what a delta means.

### The limit above all of them

**No check in this repository can tell whether the design document is wrong.** Everything here checks
conformance to a specification. A correct implementation of the wrong requirement passes every gate. That is
why the weekly demo agreed at Kickoff in [before build](02-before-build.md) and the feature judgement in step 5
of [the build loop](04-build-loop.md) are not decoration — they are the only two places a wrong requirement
gets caught.

## What we do not know

**Nobody has shown that human review catches AI-introduced defects.** We looked for a controlled study and did
not find one. The closest evidence is about review *accuracy* rather than defect capture: an LLM reviewer with
the problem description available classified correctness 68.5% of the time, and LLM reviewers systematically
flag already-correct code as defective, getting worse when asked for more detailed explanations. Both of our
human gates — the spec approval and the feature judgement — rest on an assumption nobody has tested. That is
why the first number in [measurement](11-measurement.md) counts how often a human changes anything at those
gates. A gate that never changes an outcome is ceremony, and we want that visible in week three rather than
year two.

**We do not know our own review agent's accuracy, and the published numbers for the class are unflattering.**
Across 19,450 pull requests measured in 2026, those reviewed only by a code-review agent merged at 45.20%
against 68.37% for human-only review, and 12 of 13 agents averaged below a 60% signal ratio. An independent
three-and-a-half-week run of four reviewer bots on one real codebase found 93.4% of 617 flagged locations were
raised by exactly one tool, with all four never converging on a single finding. The one counterexample earned
its place by measurement rather than argument: Uber's uReview reports its comments being addressed in the same
changeset 65% of the time against 51% for human comments. We have no equivalent figure for ours, so making
`review` a required check is a bet. The third number in [measurement](11-measurement.md) — the dismissal rate
— is what settles it, and [the runbook](12-runbook.md) keeps the check un-required until that rate justifies
blocking on it.

**The 300-line ceiling is judgement, and the enforced number is 400.** `size.yml` warns above 300 lines or 10
files and fails above 400 or 20. Say that plainly rather than advertising 300: 300 is advice, 400 is the rule,
and a team living at 399 is inside the letter of it. The argument behind both holds — attention is finite, and
past some size a reviewer stops reading and starts approving — but an argument gives a direction, not a value.
What should be measured is not how many lines a reviewer reads. It is **the diff size at which they stop
finding anything**: findings per hundred changed lines, bucketed by diff size, over enough pull requests to
watch the curve flatten. That needs a few hundred reviewed pull requests we do not have, so 300/400 is where
we start, not what we know.

**The composition has not been run end to end.** Every file here has had its logic exercised locally. The
arrangement has not: no ticket has gone Explore, approved spec, Implement, `verify`, `review`, merge, promote
with all six checks live and a person at each human gate. Parts working separately is not evidence that the
sequence works, and a sequence fails at its joins.

**Nothing has been proven on a host.** Zero of these workflows has executed on GitHub. No required check has
ever failed a real pull request. `perimeter.yml` is untestable by construction until it runs against a live
branch-protection API, and it is the one check whose purpose is to tell us the truth about the others. The
host configuration in [host and pipeline](09-host-and-pipeline.md) was read off a real protected repository
rather than invented — a weaker claim than saying our workflows have run under it, and worth keeping distinct.

**The instrumentation arrives last.** Five of the six numbers depend on the Pulse integration, which is a *to
build* row. Until it exists a tech lead records them by hand, and hand-recorded numbers decay in exactly the
weeks that matter. Three fields must be in that spec before it is built, because they cannot be reconstructed
afterwards: who found each defect, promotion and release timestamps, and stage entry and exit dates.

**And we do not know that the general effect applies to us.** A 2026 meta-analysis of 23 studies puts the
productivity effect at g = 0.33, 95% confidence interval 0.09 to 0.58, with gains largest in controlled
experiments and smaller in open-source and enterprise settings. The lower bound is close to nothing, and
agency work on a client's existing codebase sits at the end of the range where the effect shrinks.

## The trial nobody can run any more

There is a reason we cannot settle any of this by pointing at a study, and it will not improve.

The most-cited figure in this field is an early-2025 randomised trial in which 16 experienced maintainers
working on their own large repositories were 19% slower with AI while believing afterwards they had been 20%
faster. It measured early-2025 tools. It is routinely quoted as though it describes the present, and it does
not.

The follow-up was redesigned rather than published. The dominant reason was selection: developers increasingly
declined to take part if they might be assigned to work without AI, and some withheld exactly the tasks they
most wanted AI for. Time-on-task also became unreliable for developers running several agents at once.
**The clean randomised productivity trial is becoming unrunnable, because there is no longer a population
willing to be the control group.** That cuts both ways. Nobody will hand us a trustworthy number showing this
works, either.

So the six numbers in [measurement](11-measurement.md) are not a nice-to-have. They are the only evidence we
will ever have about our own delivery. And the finding that trial did establish cleanly is the one to keep: a
practitioner's sense of whether this is working is not evidence. Twenty percent faster was the perception, 19%
slower the measurement, in the same people on the same work.

## The risk this process may be creating

Everything above assumes a person can verify what an agent produced. Three independent 2026 findings suggest
that working this way erodes exactly that ability.

The meta-analysis above found **no significant effect on learning** — g = 0.14, 95% confidence interval -0.18
to 0.47 — alongside its moderate productivity effect. On current evidence, AI use does not reliably build
skill.

An Anthropic study put developers through comprehension tests after working with and without AI. The
AI-assisted group scored **17% lower**, and their largest deficit was in **identifying when code is incorrect
and understanding why it fails** — precisely the skill every gate in [enforcement](06-enforcement.md) assumes
a human has. The sample was 52 people on one Python library with comprehension tested immediately, so treat
the magnitude as indicative rather than settled. The authors say they do not know whether the effect persists.

A 2026 survey of 1,569 developers across 77 countries found **16% of senior engineers** say juniors fully
understand the AI-generated code they submit, while **85% of juniors** say AI improves their understanding.
Neither figure is reliable on its own. The gap between them is the finding: people do not know what they have
stopped knowing.

Put together: the mode of working this document prescribes may degrade the verification skill the document
depends on, and the people it happens to will report the opposite.

**One thing in that research is actionable, because it was a usage pattern rather than a fixed effect.** In
the same Anthropic study, developers who used the agent for *conceptual questions* scored above 65% on
comprehension. Those who *delegated code generation* scored below 40%. Same tool, opposite outcome. So the
rules we adopt, for anyone still building the judgement this process assumes:

- Ask the agent to explain the area before you ask it to change the area.
- Write the first version of anything unfamiliar yourself, then have the agent review it. The reverse order
  feels faster and teaches nothing.
- Read the diff before accepting it, not after the check goes green. A green check tells you the code passed.
  It does not tell you that you could have written it.

This is not a gate and cannot be made into one. **No check can detect whether the person who approved a spec
understood it.** What we can do is watch the fifth number in [measurement](11-measurement.md) — defects
reaching a person, split by who found them — because a developer whose tickets increasingly generate defects
that *other people* find is the observable shadow of a comprehension problem. That is a weak instrument for a
serious risk, and naming it as weak is the honest position.

## The two residual risks

**The tech lead's queue.** One person holds the design document, the feature judgement, the daily gate diffs,
the protected-path review and Release Check, across every project at once. The rule in [depth](05-depth.md)
that a second person is named for every protected path protects against absence, not against load — a second
name does not put a second head on the queue. The failure is quiet: feature judgement degrades into a skim of
the pull request, which is exactly the line-by-line diff read that [the build loop](04-build-loop.md) decided
not to rely on. The fifth number sees part of it, because a skim shows up as defects drifting from the feature
review towards QA and the client. What no number sees is a skim that produces no defect anyone ever finds. The
cycle-time number will not help either, because a lead who is skimming looks fast rather than slow.

**The starter existing but never being run.** This is now more likely than the starter never getting written,
because it is written. The shape of the failure: the files sit in the repository, no project turns the
required checks on, and their existence gets read as coverage. Someone quotes a *written* row from [the
runbook](12-runbook.md) in a statement of work as though it were protecting something. That is the failure in
[why](01-why.md) reproduced at company scale, one step further along, with a client's signature underneath it.
The mitigation is the three-value status column — *written*, *proven*, *to build* — and it is weak, because it
works only for as long as people read a column.

A third is worth naming though it is not yet a risk: gates turned on and counting skipped. [The
runbook](12-runbook.md) answers it with a rule — if the first step gets cut for time, cut it from the gates
and not from the counting. A gate we have not built is a known absence. A number we never started counting is
an answer that cannot be recovered.

## What we deliberately rejected

Recorded so nobody re-adds them without engaging the reason. Where the rejection has a known weakness, it is
in the same row. Two of these were rejected on this process's own logic rather than on evidence, and are
marked as such.

| Rejected | Why | What we do instead |
|---|---|---|
| Parallel agent swarms implementing one ticket | Actions carry implicit decisions, and agents that cannot see each other's traces make conflicting ones. Parallel agents are safe when they need not agree — the opposite of implementing one ticket | Explore, Implement, Review in sequence, fresh context each. Weakness: that evidence covers parallel *building*; parallel *reviewing* may well help and we have not tested it |
| Human review of every pull request | The arithmetic fails. Our pilot produced 2,789 lines in thirty minutes; three developers at that rate produce more diff per week than anyone can read | Review required per **path**, not per project — the protected set agreed at Setup in [before build](02-before-build.md). It is what makes this work with one developer: they merge their own ordinary work and cannot merge a protected path alone |
| Hooks as the enforcement layer | `--no-verify` walks past them: six consecutive commits on record skipped gitleaks, lint-staged, Jest and Playwright, taking a suite from 104 passing to 63 failing. And `permissions.deny` on `.claude/hooks/**` is not enforced, so an agent can edit its own enforcement hook. Both issues were closed "not planned" | Hooks stay as hints, because a local failure in two seconds is cheaper than a CI round trip. The gate is the required check on the host, outside anything local can reach |
| Whole-repo coverage as a gate | A 78% suite at a 31% mutation score passes it, and most of the number is inherited from code this ticket never touched | `changed-line-coverage.mjs` at 80% of the changed lines. Weakness: same oracle problem, smaller. The real answer is mutation on core logic, which [depth](05-depth.md) puts at High depth only and which we have not calibrated |
| Letting the agent write ticket status | Our pilot's agent maintained its own board and marked its own work done. An agent writes to any completion signal it is handed | Status computed from events: branch pushed, checks green, review approved, merged, promoted. Weakness: that derivation is the *to build* Pulse integration, so today a person types it |
| Reading `perimeter.yml`'s expectations from a config file | Rejected on this process's own logic, not on evidence. A file the agent can edit is not an expectation, it is a suggestion. The check that checks the checks cannot take its standard from inside the blast radius | `REQUIRED_CHECKS="size gates spec verify review"` literal in the workflow, on a path `CODEOWNERS` protects. Cost: changing it takes a code-owner-reviewed commit, which is the point |
| A rule saying "understand every line you ship" | Rejected on this process's own logic. No artefact distinguishes someone who understood from someone who clicked. Unenforceable, so writing it down makes it a wish — and by the second idea in [why](01-why.md) a wish is worse than an absence, because everyone downstream reasons from it | The size ceiling, so a diff *can* be understood, and judging the feature running in dev rather than reading the diff |
| "Velocity multiplies defect rate" arithmetic | A constructed multiplication — three times the output at the same defect rate gives three times the defects. It cannot be wrong, so it cannot be checked, so it is not evidence | The measured form: across 22,000 developers against each organisation's own low-adoption baseline, time in review up 441.5%, incidents per pull request up 242.7%, bugs per developer up 54% |
| Several reviewers voting on findings | 80+ independent agents once agreed unanimously on a vulnerability that did not exist. Consensus is not a reliability signal, and cost is linear in reviewers | One review agent, dismissal rate counted. [The runbook](12-runbook.md) lists voting among the things not to build first: apparatus that takes a month to build cannot be cheaply abandoned |
| An LLM judge score as a release gate | Judges show high inter-judge agreement while being systematically biased, and a single scalar hides its components | Deterministic checks plus the named evidence per criterion. A judge, if we ever add one, is validated against human labels first |
