# The repository

Everything the agent side of this process needs, as files: forty-seven of them, plus three `.gitkeep`
markers and one generated view. This document gives you the twenty-three it owns in full, in the order you
would create them, and tells you where the other twenty-four live.

The reason to start from a template rather than a checklist is our own estimate: hand-built, this takes
about a fortnight, the result depends on who did it, and the parts that get dropped under pressure are the
ones nobody sees missing. From a template it takes a day. The pilot's evidence is blunter than the
estimate — requirements with a check behind them arrived 8 of 8, requirements written only as prose
arrived 0 of 7. A file you did not create on day one is prose until you do.

Everything here sits inside the agent's reach. That is not a flaw to fix in this document; it is the
division of labour. What has to hold whether or not the agent cooperates lives on the host, in
[host and pipeline](09-host-and-pipeline.md). A repository with every file below and no branch protection
has advice, not enforcement.

## The tree

```
devx-starter/
├── .claude/
│   ├── agents/
│   │   ├── explore.md            reads, asks, writes one file, stops
│   │   ├── implement.md          works from the approved spec and nothing else
│   │   └── review.md             reads and runs; cannot write
│   ├── commands/
│   │   ├── spec.md               /spec <TICKET-ID>
│   │   └── build.md              /build <TICKET-ID>
│   ├── skills/
│   │   ├── build-loop/SKILL.md   the seven steps, and what each must produce
│   │   ├── operate-app/SKILL.md  boot it, drive it, capture what it did
│   │   ├── escalate/SKILL.md     the six classes that need a person
│   │   └── garbage-collect/SKILL.md  a repeated correction becomes a check
│   └── settings.json             what a session may never do
├── .github/
│   ├── workflows/
│   │   ├── size.yml              300 lines / 10 files target, 400 / 20 hard fail
│   │   ├── gates.yml             a gate change mixed into an implementation commit
│   │   ├── spec.yml              the spec is the branch's first commit
│   │   ├── verify.yml            stack gates + 80% coverage on changed lines
│   │   ├── review.yml            the review agent, as a check
│   │   ├── perimeter.yml         the host enforces what this repo claims
│   │   ├── scan.yml              the host's alert state, daily, whole tree
│   │   ├── evidence.yml          .evidence/ attached to the pull request
│   │   ├── deploy.yml            merge to main deploys to dev
│   │   └── promote.yml           dev to staging to production, by hand
│   └── pull_request_template.md  criteria, evidence, learnings, what is unverified
├── docs/
│   ├── decisions/_template.md
│   ├── design/
│   │   ├── README.md
│   │   └── criteria/_template.md protected path — acceptance criteria live here
│   ├── fixtures/README.md
│   ├── releases/                 one dated checklist copy per release
│   ├── specs/_template.md
│   ├── production-ready.md       what good enough means, by enforcement tier
│   └── release-checklist.md
├── log/
│   ├── README.md                 the schema, and why this is not a learnings doc
│   ├── events/_template.md       one file per event, append-only
│   └── weeks/                    what each weekly hour actually found
├── tasks/
│   ├── board.md                  THE TRACKER. every ticket, in the repo
│   └── board.html               generated view — never edited by hand
├── scripts/
│   ├── verify.mjs
│   ├── scan-secrets.mjs
│   ├── changed-line-coverage.mjs
│   ├── collect-week.mjs          the weekly hour's raw material, assembled
│   ├── board.mjs                 check the board, rebuild its index and view
│   └── break-it.mjs              proves each gate rejects what it claims to, offline
├── CLAUDE.md                     the rules that are always true
├── REVIEW.md                     review criteria, owned by the team
├── CODEOWNERS                    the protected set, one list
├── README.md                     how to wire this to your stack
├── commitlint.config.js
├── lefthook.yml                  hints, not gates
├── package.json
├── .editorconfig
├── .gitattributes
└── .gitignore
```

The checking workflows, the gate scripts and `lefthook.yml` are inlined with the argument for gates in
[enforcement](06-enforcement.md). `deploy.yml` and `promote.yml` are in
[host and pipeline](09-host-and-pipeline.md). The templates under `docs/`, `REVIEW.md` and
`production-ready.md` are in [templates](08-templates.md). Everything else is below.

## The order, and why it is that order

| # | Files | Why here |
|---|---|---|
| 1 | `.gitignore`, `.gitattributes`, `.editorconfig` | They change what the first commit looks like. Added later, every earlier file is already wrong. |
| 2 | `package.json` | Every workflow and hook calls a script by name. The names have to exist before anything references them. |
| 3 | `commitlint.config.js`, `lefthook.yml` | Local feedback. Cheap, and wrong-shaped commits are annoying to fix retroactively. |
| 4 | `CLAUDE.md` | The agent's standing rules. Written before the agent does anything. |
| 5 | `.claude/settings.json` | The deny list, so the first session already has it. |
| 6 | `.claude/agents/*`, `.claude/commands/*`, `.claude/skills/*` | The loop itself. Useless without 4 and 5. |
| 7 | `CODEOWNERS` | Needs the paths from 4, 5 and 6 to protect them. |
| 8 | `.github/pull_request_template.md` | The output format. Last, because it names things the earlier files define. |

Then the workflows, then the templates, then host configuration. The ordering is not ceremony. Two of the
dependencies are real and bite if you invert them: a `CODEOWNERS` line for `/.claude/` written before
`.claude/` exists protects a path that matches nothing, and a workflow calling `bun run verify` written
before `package.json` has a `verify` script fails on its first run for a reason that has nothing to do with
the code. The rest is ordinary tidiness — whitespace rules first so no later file needs reformatting.

The whole set is one commit's worth of work, and it should be one commit. A repository that acquired its
gates in dribs over three weeks has three weeks of history that predates them, and the `gates` job cannot
tell a gate that never existed from one that was removed.

## `.gitignore`, `.gitattributes`, `.editorconfig`

Three small files that decide what every later diff looks like.

In `.gitignore` the two lines that matter are `.env` with `.env.*`, because a credential in git is a
credential you must rotate rather than delete, and `.claude/settings.local.json`, which is a per-developer
permission file. That last exclusion has a cost, stated plainly below with the settings file: a local
override can widen the committed policy and nobody will see the diff. We keep the exclusion because the
alternative — committing one developer's local tool permissions into everyone's repository — is worse, but
it is a hole and you should know it is there.

`.gitattributes` sets `* text=auto eol=lf` before the first commit. A mixed-line-ending repository makes
every later diff unreadable and makes the `size` check count lines that did not change, which turns a
50-line ticket into a 400-line failure for no reason anybody can see. Lockfiles are marked
`linguist-generated` with `-diff` so they do not arrive in a review as thousands of lines. Marking them
generated is a statement about how they are reviewed, not whether they are committed: a lockfile is its own
pull request, checked for reproducibility rather than read.

`.editorconfig` is two-space indent, LF, final newline, trimmed trailing whitespace, and markdown exempted
from trimming because two trailing spaces are a line break there. It exists so that a formatter and an
agent agree about whitespace and no commit is half formatting. Formatting noise mixed into a behaviour
change is the cheapest way to make a diff unreviewable while every check stays green.

`.gitignore`

```gitignore
node_modules/
dist/
build/
coverage/
.env
.env.*
!.env.example
*.log
.DS_Store
.claude/settings.local.json

# agent-produced evidence, uploaded by evidence.yml rather than committed
.evidence/
```

`.gitattributes`

```gitattributes
* text=auto eol=lf
bun.lock  linguist-generated=true -diff
*.lock    linguist-generated=true -diff
```

`.editorconfig`

```ini
root = true
[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true
trim_trailing_whitespace = true
indent_style = space
indent_size = 2
[*.md]
trim_trailing_whitespace = false
```

## `package.json`

Five script names are the entire interface between this repository and your stack: `verify`,
`scan:secrets`, `format:check`, `coverage:changed`, `setup`. The workflows and `lefthook.yml` call those
names and nothing else. No CI file knows what your formatter is, which is what lets the same starter serve
a Node service, a Python API and a Flutter app — the wiring for each is in
[stack wiring](10-stack-wiring.md).

The load-bearing line is `format:check`, which as shipped prints a message and exits 1. That is deliberate
and it is the single design decision this file exists to make. A repository that documents six gates and
silently runs four reports green for the two it never ran; that is the pilot's failure in one sentence. So
an unwired gate fails loudly on the first pull request instead of passing quietly forever.

Note the asymmetry with the other five gates. `format:check` is present-but-failing because a missing key
would let a careless `verify` implementation skip it; `lint`, `typecheck`, `test`, `test:coverage` and
`build` are absent entirely, and `scripts/verify.mjs` fails on their absence by name, printing what each
one is for. Both routes end at the same place — red until wired — by two different mechanisms, because we
did not want the guarantee to depend on either one alone.

`test:coverage` has one hard requirement: it must emit `coverage/lcov.info`. Changed-line coverage is
measured from that file and from nothing else. Whole-repo coverage is a number you inherited; changed-line
coverage is one you earned.

`package.json`

```json
{
  "name": "devx-starter",
  "version": "0.1.0",
  "private": true,
  "description": "Starter repository for the devx AI SDLC. Replace this block with your project's own.",
  "scripts": {
    "verify": "bun scripts/verify.mjs",
    "scan:secrets": "bun scripts/scan-secrets.mjs",
    "format:check": "echo 'Wire format:check to your formatter (e.g. prettier --check) — see README.md' && exit 1",
    "coverage:changed": "bun scripts/changed-line-coverage.mjs",
    "setup": "lefthook install"
  },
  "devDependencies": {
    "@commitlint/cli": "^19.6.0",
    "@commitlint/config-conventional": "^19.6.0",
    "lefthook": "^1.10.0"
  }
}
```

## `commitlint.config.js`

Conventional commits, with the two line-length rules switched off. The reason for the exception: commit
bodies carry evidence — a test name, a URL, a query, a stack trace — and a wrapping rule makes an agent
either truncate that or spend two retries fighting the linter. Neither outcome produces a better commit.

The subject-line rules stay on, and they earn their keep. `gates.yml` and the daily gate-diff read both key
off commit shape, and a history you can grep by type and scope is what makes "weakening a gate goes in its
own commit" checkable at all. Turn the subject rules off and that rule becomes an aspiration.

`commitlint.config.js`

```javascript
export default {
  extends: ['@commitlint/config-conventional'],
  rules: { 'body-max-line-length': [0], 'footer-max-line-length': [0] },
}
```

## `CLAUDE.md`

This is the file every session reads without being asked, so it holds only rules that are true on every
ticket. It is short on purpose. A context file that tries to be the process document gets skimmed, and the
rules that matter get skimmed along with it.

Note what it does not contain. There is no rule saying "understand every line you ship". Nothing can check
that, and writing an unenforceable rule into the file the agent treats as authoritative teaches it that the
file contains wishes. Once one line is a wish, the reader cannot tell which lines are not.

`CLAUDE.md` is itself on the protected path, for the reason the pilot demonstrated: its context file
asserted that main was protected and that a red pull request could not merge. There was no remote and CI
had run zero times. A context file is the easiest thing in a repository to make say something false, and it
is the thing every later session believes.

`CLAUDE.md`

```markdown
# How we work in this repository

The full process is in the AI SDLC. These are the rules that are always true, so you do not have to
look them up.

## Always work from a ticket

No branch, no commit, no pull request without a ticket. The branch is named after it: `PULSE-123-short-slug`.

## The design document is the source of truth

`docs/design/` holds it. When the code and the design document disagree, **say so** — do not quietly
follow whichever one is convenient. A divergence is the most valuable thing you can report, because it
means the document has gone stale and every later ticket would have rediscovered it.

Where the answer corrects the design document, the correction lands **in the document**, not only in this
ticket's spec.

## Never approve your own work

You may **propose** a change to acceptance criteria. Only a person approves one.
You may not merge. You may not push to `main`. You may not set a ticket's status — status is derived from
what actually happened.

## Weakening a gate goes in its own commit

Never in the same commit as implementation. The protected set:

- existing tests (modifying or deleting them — adding new ones for new code is implementation)
- coverage thresholds
- CI and hook config
- `CODEOWNERS`, `CLAUDE.md`, `.claude/`
- the acceptance criteria

If a gate is in your way, say so and stop. Do not route around it. `--no-verify`, `git stash` to hide
staged state, quiet flags, deleting a failing test, editing a workflow to skip a job — all of these are
the thing we are guarding against, and all of them are visible.

## Green checks are not evidence

They are evidence only if you did not touch what produces them. Attach the artefact that proves each
criterion: the test name, the screenshot, the response, the query output.

## Retry twice, then ask

If a check fails, fix the cause and try again. After two attempts, stop and ask the developer. Looping on
a red gate burns budget without producing evidence.

## Asking is free. Asking the same question twice is a bug

There is no budget on questions and no virtue in a low count. Guessing to avoid interrupting someone turns
a two-minute answer into a day of wrong work.

The `escalate` skill has the six classes that require a person, how to grade the request so only the
blocking ones interrupt, and the one-file record you leave in `log/events/`. Write the record even when the
answer arrives immediately — **especially** then, because an easy question is the most likely kind to be
asked again, and that file is the only thing that will notice.

## Fetch once, then commit it

Documentation, an external system's response shape, a design frame — needed once, fetch it. Needed again,
commit it as a fixture and read the file. Strip real credentials and real personal data before it lands.

Never fetch live during implementation. It makes the result depend on which tools happened to be connected.

## Say what you did not do

At the end of a ticket, state what you could not verify. An account of the work that claims everything is
checked is not one.
```

The first line points at "the AI SDLC" as a single document. Repoint it at your copy of this document set
when you clone — the [README](README.md) index is the right target — and do that in the same commit as the
rest of your `CLAUDE.md` edits, since it is a protected path and each edit costs a code owner's attention.

## `.claude/settings.json`

Two lists. `deny` is for actions with no legitimate use inside a ticket: force-push, push to `origin main`,
`--no-verify` and its `-n` short form, `gh pr merge`, `gh pr review --approve`, `gh api --method DELETE`,
label manipulation through any of its four spellings, and reading `.env`, `.env.*`, `*.pem` or `id_rsa*`.
`ask` is for actions that are sometimes right and always worth a human keystroke: `git rebase`,
`git reset --hard`, `rm -rf`, and edits to `.github/workflows/`, `CODEOWNERS`, `lefthook.yml`, `CLAUDE.md`,
`.claude/**` and `docs/design/criteria/**`.

The label entries look fussy next to the rest and they are the most specific thing in the file. They are
there because `size.yml` honours a `size-override` label. An agent that can apply a label can grant itself
the override, which turns the size ceiling into a suggestion it controls. Denying `gh pr edit --add-label`
alone would not do it, so the deny list names the label API four ways.

Be clear about what this file is worth. It is a harness-side filter on tool calls, not a gate. Patterns
match strings, so a variant nobody listed gets through, and an agent with `Bash` can read `.env` with
`cat`. The committed file can be widened by `.claude/settings.local.json`, which is gitignored, so a local
override is invisible in review. Every entry here has a hard counterpart elsewhere: the push and merge
denials are real only because branch protection and the merge button live on the host, and the `ask`
entries on gate paths are real only because `CODEOWNERS` requires a second person on those paths. Read this
file as friction that removes the easy mistake, and nothing more.

`.claude/settings.json`

```json
{
  "permissions": {
    "deny": [
      "Bash(git push*--force*)",
      "Bash(git push*origin main*)",
      "Bash(git commit*--no-verify*)",
      "Bash(git commit*-n *)",
      "Bash(gh pr merge*)",
      "Bash(gh pr review*--approve*)",
      "Bash(gh api*--method DELETE*)",
      "Read(./.env)",
      "Read(./.env.*)",
      "Read(**/*.pem)",
      "Read(**/id_rsa*)",
      "Bash(gh pr edit*--add-label*)",
      "Bash(gh pr edit*--remove-label*)",
      "Bash(gh label*)",
      "Bash(gh api*labels*)"
    ],
    "ask": [
      "Bash(git rebase*)",
      "Bash(git reset*--hard*)",
      "Bash(rm -rf*)",
      "Edit(./.github/workflows/**)",
      "Edit(./CODEOWNERS)",
      "Edit(./lefthook.yml)",
      "Edit(./CLAUDE.md)",
      "Edit(./.claude/**)",
      "Edit(./docs/design/criteria/**)"
    ]
  }
}
```

## The three agents

The three files share a frontmatter shape — `name`, `description`, `tools`, `model` — and the `tools` line
is what makes each role real rather than nominal. Explore can fetch and can write one file. Implement can
write code and cannot fetch. Review can read and run and cannot write at all. Change those lines and you
have three prompts with different headings, which is a naming convention, not a separation of duties. What
each role is for, and why the sequence is explore then implement then review, is argued in
[the build loop](04-build-loop.md); this section is the files.

All three pin `model: opus`. A review done by a cheaper model is a different check, and the failure mode is
not that it is worse — it is that you would not know which check you were relying on when you decided the
diff was fine.

### `.claude/agents/explore.md`

Tools: `Read, Grep, Glob, WebFetch, Write, Bash`. It can fetch, because exploration is exactly when an
external shape should be looked up, and it writes one file.

Two clauses do most of the work. "Ask everything you need, in one pass" exists because the alternative is a
day of interruptions, and a developer interrupted eight times answers the eighth question worse than the
first. The requirement that the spec carry the questions and answers verbatim exists because the
implementing agent never sees this conversation: an answer that is not in the spec did not happen. The
third clause is the novelty judgement — well-trodden, novel here, genuinely novel — which is not
difficulty. It is how much of this work exists a thousand times over in public code, and it sets how close
a person stays to the diff. [Depth](05-depth.md) covers how that judgement is used.

`.claude/agents/explore.md`

```markdown
---
name: explore
description: Reads the ticket, the design document and the code, asks the developer everything it needs, and writes the spec. Ends there. Use at the start of every ticket.
tools: Read, Grep, Glob, WebFetch, Write, Bash
model: opus
---

You read and you write one file. You do not implement.

## What you read

1. The ticket — its description and its acceptance criteria.
2. `docs/design/` — the design document for this phase. This is the source of truth.
3. The code as it actually is now. Not as the design document says it is.
4. `docs/decisions/` — why things are the way they are.
5. Committed fixtures in `docs/fixtures/` — the real shapes of external systems.
6. The project folder, if the question is what the client actually said.

## What you ask

Everything you need, **in one pass**, before writing the spec. Not only when the design document is
unclear — anything:

- the design document and the code contradict each other
- something was never specified
- you can see a better approach than the one implied
- the existing code looks wrong

Ask it all at once. Do not interrupt the developer repeatedly through the day.

The `escalate` skill has the six classes and how to grade a request. You do not write log events —
your questions and their answers go into the spec verbatim, and the weekly collector reads them from
there. That is the same record by a shorter route.

Where an answer corrects the design document, say so explicitly and name the file and section that needs
changing. That correction is a separate concern from this ticket's spec.

## What you write

One file: `docs/specs/<TICKET-ID>.md`, from the template in `docs/specs/_template.md`.

It must carry **the questions and the answers in the words they were given**. The implementing agent never
sees this conversation. An answer that is not in the spec did not happen.

It must also name the patterns already present in the codebase that this work should follow. A spec that
could have been written without reading the code is not a spec.

And it must answer **how well-trodden this is** — well-trodden, novel here, or genuinely novel. This is not
how hard the work is. It is how much of it exists a thousand times over in public code, which is a different
thing and a better predictor of where the implementation will go quietly wrong. Genuinely novel work gets
smaller steps and a person reading the diff, so getting this wrong costs attention in the place it was least
likely to be spent.

## Then stop

Do not write code. Do not create a branch beyond the spec commit. Say the spec is ready for approval and
end your turn.
```

### `.claude/agents/implement.md`

Tools: `Read, Grep, Glob, Write, Edit, Bash` — no `WebFetch`. Implementation that fetches live makes the
result depend on which tools happened to be connected that afternoon, and makes the same ticket
irreproducible next month. If an external shape is needed it is a committed fixture, or the spec is wrong.

The prohibitions are written as a list of named things rather than a principle, because a general
instruction to behave well does not survive a red gate at five o'clock. The size ceiling is here in
numbers — 300 lines and 10 files as target, 400 and 20 as hard fail — so the agent can stop and say the
ticket needs splitting rather than discovering the ceiling from CI after the work exists to argue for
itself.

The one carve-out prevents a deadlock. New tests for new code are implementation, not a gate change.
Without that clause there is no legal commit ordering at all: a test-only commit lands red, and an
implementation-only commit fails changed-line coverage.

`.claude/agents/implement.md`

```markdown
---
name: implement
description: Implements an approved spec in its own steps, one commit per step, with checks on every commit. Use after a spec has been approved.
tools: Read, Grep, Glob, Write, Edit, Bash
model: opus
---

You work from the approved spec and nothing else. You did not do the exploration and you do not have it —
if the spec does not answer something, the spec is wrong, and you say so rather than guessing.

## How you work

Read `docs/specs/<TICKET-ID>.md`. Decide your own steps. **One commit per step**, pushed as you go, so
progress is observable and no single diff becomes unreadable.

The spec says how well-trodden this is, and it changes how you work. **Well-trodden** — follow the pattern
already here and move. **Novel here** — say which pattern you are introducing and why the existing ones did
not fit, before you introduce it. **Genuinely novel** — smaller steps than you would otherwise take, stop at
the first thing you are unsure of rather than the second, and write the reasoning into `docs/decisions/`.
Confidence is not calibrated to novelty: unfamiliar work produces output that looks exactly as assured as
familiar work.

Write tests where behaviour is specified. New tests for the code you are adding are implementation, not a
gate change.

## What you must not do

- Touch existing tests, coverage thresholds, CI config, hook config, `CODEOWNERS`, `CLAUDE.md`, `.claude/`
  or the acceptance criteria **in the same commit as implementation**. If one genuinely needs changing, it
  is its own commit, and a criteria change is a proposal for a human.
- Push to `main`. Merge. Approve. Set a ticket status.
- Use `--no-verify`, `git stash` to hide staged state, or any flag that suppresses a check.
- Exceed the size ceiling: 300 lines and 10 files is the target, 400 and 20 is a hard fail. If the work is
  larger, stop and say the ticket needs splitting.

## When a check fails

Fix the cause. Try again. After two attempts, stop and ask. Never make the check quieter.

## When you need a person

Use the `escalate` skill. It has the six classes, how to grade the request so only the blocking ones
interrupt, and the record you leave in `log/events/`. Asking is free; guessing to avoid interrupting is
the expensive option. Match the situation against the classes rather than deciding whether you feel
confident enough — confidence is the unreliable part.

## Before you open the pull request

- Every acceptance criterion has its evidence attached — the test name, the screenshot, the response.
- The documents this change made wrong are fixed.
- Everything learned that was not in the design document is routed: a test, a fixture, a decision record,
  a proposed criterion, a rule in `CLAUDE.md`, or a note for the CSM.
- State what you did not verify.
```

### `.claude/agents/review.md`

Tools: `Read, Grep, Glob, Bash` — no `Write`, no `Edit`. It reports, and it cannot fix. That keeps its
findings readable as findings instead of arriving as a diff nobody asked for and everybody then has to
review.

Check 3 is why this role exists in this form. The gate surface — a deleted test, a lowered threshold, a
removed job, an assertion loosened inside a test that stayed — is the one class no automated check can
catch, because the deception is of the checks. So the reader is told to report it first and separately,
before anything else it found.

Two instructions guard against the failure modes of agent review itself: findings are input rather than
verdicts, dismissed in writing on the pull request, and if it finds nothing it says so, because a reviewer
that manufactures work teaches people to ignore it. We do not make this a required check on day one. Across
19,450 pull requests measured in 2026, agent-only-reviewed PRs merged at 45.20% against 68.37% for
human-only, and 12 of 13 agents averaged below a 60% signal ratio. We have no reason to assume ours beats
that, which is why the dismissal rate is one of the six numbers in [measurement](11-measurement.md).

`.claude/agents/review.md`

```markdown
---
name: review
description: Reviews a finished ticket in a fresh context, having neither explored nor implemented it. Runs as a check on the pull request.
tools: Read, Grep, Glob, Bash
model: opus
---

You did not plan this work and you did not write it. That is the point — a session reviewing its own work
catches less than a fresh one does, and repeating the self-review does not close the gap.

**You cannot write or edit.** You report.

## Read these first

`REVIEW.md` is your operating instructions — the order of attention, how to grade, and what not to review.
`docs/production-ready.md` is the standard itself. Both are owned by the team and change without anyone
editing this file, which is the point: what gets reviewed should not require an agent edit.

If `REVIEW.md` is absent, say so in your report. A repository with no written review criteria is being
reviewed against whatever you happen to think, and that is not a check.

## What you check

1. **Against the spec and the criteria.** Does it do what `docs/specs/<TICKET-ID>.md` said, and does each
   acceptance criterion actually have the evidence it claims?
2. **The evidence itself.** Is the screenshot of the thing, or of an assertion? Does the named test assert
   the behaviour, or does it assert whatever the code happens to do?
3. **The gate surface.** Did any existing test get weakened or deleted? Any threshold lowered? Any CI job
   removed? Any assertion loosened in a test that stayed? Report these first and separately — they are the
   one class no automated check can see, because the deception is of the checks.
4. **Whether it belongs here.** Does this follow the patterns already in the codebase, or invent a third
   way to do something already done twice?
5. **What is missing.** A criterion with no evidence. A path the tests do not reach. An error case nobody
   handled.

## How you report

Every finding gets a severity and a location. Be specific enough that someone can act without asking you
what you meant.

Findings the developer believes are wrong get **dismissed in writing on the pull request** — that is a
legitimate outcome and you should say so. You are not the arbiter; you are the second pair of eyes.

If you find nothing, say so plainly. Do not manufacture findings — a reviewer that invents work teaches
people to ignore it, which is worse than one that occasionally misses something.

If a check itself looks wrong — it blocks something that should be allowed, or two rules cannot both be
satisfied — say so under its own heading as **class D** (see the `escalate` skill). You cannot write, so
your report is the only route that class has, and it goes to whoever owns the gate rather than to the
author. It is the most under-reported class precisely because working around a wrong gate is easier than
reporting one.
```

## The two commands

Two commands, not one, and that is the whole reason for having commands at all. Two separate invocations
are what give explore and implement separate contexts. A single `/ticket` command that did both would hand
the implementation the exploration transcript, and the spec would stop being the handoff — it would become
a summary of a conversation the implementer already had, which nobody would then have any reason to write
carefully.

### `.claude/commands/spec.md`

This one creates the branch, dispatches explore, then commits the spec on its own as the branch's first
commit. `spec.yml` later checks that commit is an ancestor of every implementation commit, which closes the
route of building freehand and writing a plausible spec afterwards.

The last line is the one people delete first: approval is a state on the host, not a word an agent writes
into a file. The agent writes that file, so a field in it saying "approved" is the agent approving its own
work with extra steps.

`.claude/commands/spec.md`

````markdown
---
description: Start a ticket — gather context, ask what you need, write the spec
argument-hint: <TICKET-ID>
allowed-tools: Task, Read, Grep, Glob, Bash
---

Ticket: **$1**

Create the branch if it does not exist: `git switch -c $1-<short-slug>` off an up-to-date `main`.

Then dispatch the **explore** subagent. Give it the ticket id and tell it to:

1. Read the ticket, `docs/design/`, the code as it is now, `docs/decisions/`, and any committed fixtures.
2. Ask me — in one pass — everything it needs. Anything unclear, contradictory, or better done another way.
3. Write `docs/specs/$1.md` from `docs/specs/_template.md`, carrying the questions and my answers in my
   own words.
4. Stop. No implementation.

When it returns, commit the spec **on its own, as the branch's first commit**:

```
git add docs/specs/$1.md && git commit -m "docs($1): spec"
```

Then show me the spec and stop. Do not begin implementing. I approve it by approving the pull request on
the host — not by you writing "approved" anywhere.
````

### `.claude/commands/build.md`

It refuses before it starts. Three preconditions: the spec file exists, it is the branch's first commit
(`git log --oneline main..HEAD | tail -1`), and the pull request carries an approving review or the
`spec-approved` label. Any one false means stop and say so.

This is a hint, not a gate — the workflows check the same ancestry server-side, where the agent cannot
reach — but it is the cheapest place to catch the mistake. Catching it here costs a sentence. Catching it
in CI costs a day of work that now exists and will argue for itself.

After the subagent returns, the command confirms the size ceiling with `git diff --stat main..HEAD` and is
told to say the ticket needed splitting rather than to ask for an override, checks that no commit mixes a
gate change with implementation, and fills in the pull request template. Then it stops. A person judges the
feature when its whole set of tickets is merged and running in dev, not from the diff.

`.claude/commands/build.md`

```markdown
---
description: Implement an approved spec — own steps, one commit each, checks on every commit
argument-hint: <TICKET-ID>
allowed-tools: Task, Read, Grep, Glob, Bash
---

Ticket: **$1**

First verify the spec is there and was approved before any code:

- `docs/specs/$1.md` exists
- it is the branch's first commit: `git log --oneline main..HEAD | tail -1` should be the spec commit
- the pull request carries an approving review, or the `spec-approved` label

If any of those is false, stop and tell me. Do not implement against an unapproved spec.

Then dispatch the **implement** subagent with the spec as its input and a fresh context. It must not be
given this conversation — the spec is the handoff, and if the spec is thin that is a finding, not something
to work around.

When it returns:

1. Confirm the size ceiling holds — `git diff --stat main..HEAD`. Over 400 lines or 20 files means the
   ticket needed splitting; say so rather than asking for an override.
2. Confirm no commit mixes a gate change with implementation.
3. Open the pull request using `.github/pull_request_template.md`, filled in: the criteria table with
   evidence, what we learned and where it landed, and what this does not verify.

Then stop. The review agent runs as a check. I judge the feature when its whole set of tickets is merged.
```

## `.claude/skills/build-loop/SKILL.md`

The commands say what to run. This says what each step must produce before the next may begin, and it loads
on any ticket work, including in a session that never types `/spec`. That last property is the point: the
commands are opt-in and this is not.

It is also the one file in `.claude/` a human reads end to end, which is why the reasoning sits next to each
rule rather than in a separate document. Two things in it are easy to skim past. Step 5 says that while the
agent works, the developer's job is explicitly not to watch — it is to answer, to stop it early when it is
going the wrong way, and to refuse a shortcut that makes a check quieter instead of the code right. And the
last line is the rule that makes the loop converge rather than merely run: every defect a person found
leaves a check behind.

`.claude/skills/build-loop/SKILL.md`

`````markdown
---
name: build-loop
description: Use when starting, implementing, reviewing or finishing any ticket in this repository — the seven-step loop from ticket to merge, including what each step must produce before the next one may begin.
---

# The build loop

One ticket, one branch, one pull request, one merge. Seven steps, in order.

```
   ┌──────────┐   ┌───────────┐   ┌──────────┐   ┌──────────────┐
   │ 1 TICKET │──▶│ 2 EXPLORE │──▶│ 3 SPEC   │──▶│ 4 APPROVE    │
   └──────────┘   └───────────┘   └──────────┘   └───────┬──────┘
                                                         │ a person, on the host
        ┌────────────────────────────────────────────────┘
        ▼
   ┌──────────────┐   ┌───────────┐   ┌──────────┐
   │ 5 IMPLEMENT  │──▶│ 6 REVIEW  │──▶│ 7 MERGE  │
   └──────────────┘   └───────────┘   └──────────┘
```

## 1 — Ticket

Sized to the review, not to the clock: **≤300 lines, ≤10 files**. CI fails above 400 and 20.

If it cannot be described in one or two sentences without "and", it is more than one ticket. Split it
before you start, not when the diff gets large.

## 2 — Explore

Run `/spec <TICKET-ID>`, which dispatches the **explore** agent. It reads the ticket, `docs/design/`, the
code as it actually is, `docs/decisions/`, and the committed fixtures — then asks you everything it needs
**in one pass**.

Answer properly. Every answer that is not written into the spec did not happen, because the agent that
implements this will not have this conversation.

## 3 — Spec

`docs/specs/<TICKET-ID>.md`, from `docs/specs/_template.md`. It carries the questions and your answers in
your words, and names the patterns in the codebase the work should follow.

It also states how well-trodden the work is, which sets the leash: well-trodden work is reviewed on its
evidence, genuinely novel work gets a person reading the diff. Cost of getting it wrong sets the apparatus
around a ticket; novelty sets how close you stay to it.

Commit it **alone, as the branch's first commit**. `spec.yml` checks that it is an ancestor of every
implementation commit — because a spec written after the code is a description, not a plan.

## 4 — Approve

A person reads the spec and approves it on the host. Not a field in the file, not a line an agent writes.
This is the cheapest place to catch a wrong direction — one paragraph of reading against a day of rework.

If the spec is thin, that is the finding. Send it back.

## 5 — Implement

Run `/build <TICKET-ID>`. The **implement** agent gets the spec and a fresh context — deliberately not
this conversation. It chooses its own steps and commits one per step.

While it works, your job is not to watch. It is to:
- answer when it asks
- notice when it is going the wrong way and stop it early
- refuse a shortcut that makes a check quieter instead of the code right

It never touches an existing test, a threshold, CI config or the acceptance criteria in an implementation
commit. If a gate is genuinely wrong, that is its own commit and its own conversation.

## 6 — Review

The **review** agent runs on the pull request in a fresh context. It did not plan this and did not write
it — a session reviewing its own work catches less, and re-reading does not fix that.

You read what it reports and you read the diff. Its findings are input, not verdicts: dismiss what is
wrong, in writing, on the pull request.

Then check the one class of thing no automated check can see: **did the gate surface get weaker?** A
deleted test, a lowered threshold, a loosened assertion, a removed job. The checks cannot detect
tampering with the checks.

## 7 — Merge

Every acceptance criterion has evidence attached — the test name, the screenshot, the response. Not the
word "verified".

The pull request states what was learned that was not in the design document, and where it landed: a test,
a fixture, a decision record, a proposed criterion, a rule in `CLAUDE.md`, or a note for the CSM. And it
states what this does not verify.

Then merge. Status is derived from that merge, never written by hand.

## The rule that makes this converge

**Every defect a person found leaves a check behind.** If review caught it and nothing was added, review
will catch it again next month. That is the difference between a process that improves and one that just
runs.
`````

## `CODEOWNERS`

One list, referenced everywhere else. Two kinds of path are on it. First, where a mistake is not
recoverable: payments, billing, auth, anything holding personal data, and migrations — the highest blast
radius in any repository. Second, the gates themselves: `.github/workflows/`, `lefthook.yml`, `CODEOWNERS`,
`CLAUDE.md`, `.claude/` and `docs/design/criteria/`. An agent that can edit those can make itself pass, so
a second person is required on them.

The property that makes this workable is that review is required per path, not per project. A single
developer merges their own ordinary work and cannot merge a change to a protected path alone. That is why
this document set does not ask for human review of every pull request: at agent speed three developers
produce more diff in a week than anyone reads, and a review that has become a rubber stamp is
indistinguishable from no review while still producing a green check. Requiring less review in more places
buys you real review in the places that matter.

Two things to do before first use, and both are easy to skip.

Replace `@devx/tech-leads` with a real team slug. A `CODEOWNERS` entry that does not resolve silently
protects nothing — GitHub does not require an owner who does not exist. `perimeter.yml` greps for the lines
but does not verify that the owners resolve to real people, so that check is on you, by hand, once.

Then check the glob patterns against this project's actual layout. `/src/**/payment*/` matches nothing in a
repository whose code lives under `apps/api/`, and it will match nothing quietly for the life of the
project. Open a throwaway pull request touching each protected path and confirm the review requirement
fires; that is the only way to know the patterns are right.

`CODEOWNERS`

```
# ── The protected set. One list, referenced everywhere. ──
# A change to anything here needs review from someone other than the author.
# This is required PER PATH, not per project — which is what makes the SDLC
# workable with a single developer on a project.
#
# Replace @devx/tech-leads with your real team slug before first use.

# Money, personal data, auth — the paths where a mistake is not recoverable
/src/**/payment*/          @devx/tech-leads
/src/**/billing*/          @devx/tech-leads
/src/**/auth*/             @devx/tech-leads
/src/**/pii*/              @devx/tech-leads

# Migrations — the highest blast radius surface in any repository
/migrations/               @devx/tech-leads
/prisma/migrations/        @devx/tech-leads

# The gates themselves. An agent that can edit these can make itself pass.
/.github/workflows/        @devx/tech-leads
/lefthook.yml              @devx/tech-leads
/CODEOWNERS                @devx/tech-leads
/CLAUDE.md                 @devx/tech-leads
/.claude/                  @devx/tech-leads
/docs/design/criteria/     @devx/tech-leads
```

## `.github/pull_request_template.md`

Four sections, and each exists because of a specific way an evidence pack goes soft.

The criteria table has a third column for the artefact — the test name, the screenshot, the response —
because a criterion with nothing against its name is prose, and prose disappears. "What we learned that was
not in the design document" forces each discovery to name a destination, since a learning recorded only as
a paragraph in a merged pull request gets rediscovered by the next ticket at full price. "What this does
not verify" is the section a reader should check first: an evidence pack that claims everything is checked
is not one, and an empty answer there is a stronger signal than a long one.

The HTML comments stay in the committed file. They are the instruction the filling agent reads, and a
template whose reasoning has been stripped out gets filled in with the word "verified".

`.github/pull_request_template.md`

```markdown
## Ticket

<!-- PULSE-123 — must match the branch name -->

## Spec

<!-- Link to docs/specs/<ticket>.md. It is the branch's first commit. -->

## Acceptance criteria

| Criterion | How it was proven | Evidence |
|---|---|---|
| | | |

<!-- Every criterion names its check. A criterion with nothing against its
     name is prose, and prose disappears. Never write "verified" as prose. -->

## What we learned that was not in the design document

<!-- Each item names where it landed: a test · a fixture · a decision record ·
     the design document · a rule in CLAUDE.md · the CSM.
     Empty is a valid answer. "Nothing" after two days is worth a second look. -->

## What this does not verify

<!-- State it. An evidence pack that claims everything is checked is not one. -->

## What the design document got wrong

Implementation always finds something the design missed. Empty is fine — but if something diverged,
**fix it in the design document in this pull request or a linked one.**

Not bookkeeping. Everyone's model of this system came from that document, so a stale one produces people
who are confidently wrong about where a symptom points. Worse than not knowing, and invisible from the
inside.

-

## Production-ready standard

`docs/production-ready.md`, the tier-2 lines. Tier 1 is already enforced by checks.

- [ ] Walked. Anything not applicable is named below rather than silently skipped
```

## `README.md`

The starter's own README, not the index of this document set. It has to exist because two files point a
reader at it by name when a gate is unwired: the `format:check` line in `package.json`, and the failure
message in `verify.yml`. A repository whose error messages reference a missing file teaches people that the
error messages are stale.

Read it as the setup order in four steps, of which the first is not optional. Two things in the shipped copy
need editing when you clone. It points at `AI-SDLC.md`, the single file this set replaced — repoint that at
your copy of the [index](README.md). And its enforcement table lists six workflows; the starter now has
seven checking workflows plus the two deployment ones, so `scan` belongs in that table and `deploy` and
`promote` belong in a sentence under it. Both are honest omissions of drift rather than design decisions,
and both cost a code owner's approval to fix, since `README.md` is not itself a protected path but the
files it describes are.

`README.md`

`````markdown
# devx AI SDLC — starter repository

Everything the AI SDLC says a repository must have, as working files. Clone it, run one script, wire
four things to your stack.

The process itself is in **AI-SDLC.md**. This is the enforcement.

---

## Why this exists

In our pilot, a cold session built a backend, a web app and an admin panel from a frozen spec: 27
commits, 72 tests, 87% coverage — and not shippable. The repository's own `CLAUDE.md` asserted branch
protection. There was no remote. **CI had never run once.**

Nothing lied. Every check that existed passed. The checks that mattered had been written down and never
built, and writing them down was mistaken for having them.

So this repository exists to make the gap between *documented* and *enforced* impossible to sit in
quietly. That is the whole design goal.

---

## Setup

```bash
bun install
bun run setup            # installs the git hooks
```

Then four things, in this order. The first is not optional and nothing else works without it.

### 1. Branch protection on `main`

Everything in `.github/workflows/` runs inside the repository, where an agent can reach it. Branch
protection lives on the host, where it cannot. **Until this is set, every gate here is advisory.**

On `main`, require:

- status checks: `size`, `gates`, `spec`, `verify`, `review` — and "up to date with main"
- 1 approving review, **code owner review**, and dismiss stale reviews
- **require linear history** — this one is a precondition, not a preference. `gates.yml` walks
  `git rev-list` commit by commit and `spec.yml` asserts the spec is an ancestor of every
  implementation commit. A merge commit inside a branch makes both reason about an order nothing was
  tested in.
- **require conversation resolution** — so a review finding cannot be merged while neither fixed nor
  dismissed
- no force pushes, no deletions

GitHub has two protection systems and either is fine: classic branch protection, or a repository
ruleset. `perimeter.yml` reads whichever one answers and normalises both before asserting anything —
a repository on rulesets returns 404 from the classic endpoint while being fully protected, so a
check that only read the classic endpoint would raise a false alarm. In ruleset mode it cannot see
`bypass_actors`, so it warns and tells you to check those by hand.

Then add `PERIMETER_TOKEN` — a fine-grained token with `Administration: read` — and run the
**perimeter** workflow. It asks the host what it is actually enforcing and fails if that does not match
what this repository claims. It is the only check that can catch the pilot's failure.

### 2. `CODEOWNERS`

Replace `@devx/tech-leads` with your real team. Then confirm the paths are right for this project —
the defaults cover payments, auth, PII, migrations and the gate files themselves.

### 3. The stack gates

`bun run verify` fails until you wire these in `package.json`:

```json
"format:check": "prettier --check .",
"lint":         "eslint .",
"typecheck":    "tsc --noEmit",
"test":         "bun test",
"test:coverage": "bun test --coverage --coverage-reporter=lcov",
"build":        "…"
```

It **fails** rather than skipping what is missing. A repository that documents six gates and runs four
reports green for the two it never ran.

`test:coverage` must emit `coverage/lcov.info` — changed-line coverage is measured from it, because
whole-repo coverage is a number you inherited and changed-line coverage is one you earned.

### 4. `ANTHROPIC_API_KEY`

For the review workflow. Without it that job fails loudly instead of passing silently — if you do not
want a review agent, delete the job *and* remove `review` from `REQUIRED_CHECKS` in `perimeter.yml`, so
the repository stops claiming a review it does not do.

---

## Working a ticket

```
/spec PULSE-123      # explore → asks you everything → writes docs/specs/PULSE-123.md
                     # you read it. you approve it on the host.
/build PULSE-123     # implement, in its own steps, one commit each
                     # review runs as a check. you read the diff.
```

Three roles, sequential, never parallel. They are real because **their tools differ** — explore reads
and writes one file, implement writes code but cannot merge or push to `main`, review cannot write at
all. A role that is only a name is a naming convention.

The loop is in `.claude/skills/build-loop/SKILL.md`. The rules that are always true are in `CLAUDE.md`.

---

## What is actually enforced

| | Where it lives | What it catches |
| --- | --- | --- |
| `size` | `.github/workflows/size.yml` | over 400 lines or 20 files — a diff that gets read, not reviewed |
| `gates` | `gates.yml` | a weakened check hidden inside an implementation commit; skipped tests; `continue-on-error` |
| `spec` | `spec.yml` | no spec, or a spec that is not the branch's first commit |
| `verify` | `verify.yml` | the stack gates, plus 80% coverage **on changed lines** |
| `review` | `review.yml` | a fresh session, gate-surface findings first |
| `perimeter` | `perimeter.yml` | **the host not enforcing what this repository says it does** |
| protected paths | `CODEOWNERS` | payments, auth, PII, migrations, and the gate files themselves |
| fast feedback | `lefthook.yml` | formatting and staged secrets — *hints, not gates* |

Hooks are hints. `--no-verify` walks past all of them and always will. The gates are the required checks
on the host. This repository is honest about which is which, in the files themselves.

---

## What this does not do

- **It cannot prove a person read the spec.** `spec.yml` proves the spec came first. That approval
  happened is a state on the host; `perimeter.yml` checks the host is *configured* to require it.
  Whether the human actually read it is not observable, by anything, ever.
- **The secret scanner is a hint** and only knows the shapes in its list. Rotate anything that reached
  a remote — deleting the commit does not un-publish the key.
- **The review agent's accuracy is unknown.** Its findings are input, not verdicts. Dismiss the wrong
  ones in writing.
- **`size` excludes generated files**, so a large generated diff passes. Every entry on that exclude
  list is review you are not doing; keep it short.
- **`gates` cannot catch a test that was always weak.** It catches tests that *became* weaker. A
  meaningless assertion written on day one looks exactly like a passing test.

None of this is a reason not to run it. It is what you should say when someone asks whether this is
covered.
`````

## Two traps that fail silently

Git does not commit an empty directory. A reader who builds the tree above by hand ends with no
`docs/design/criteria/` and no `docs/releases/`, which means the `CODEOWNERS` line for
`/docs/design/criteria/` matches nothing and protects nothing. Acceptance criteria are then editable by an
agent without a second person, which is the exact failure that stage 03 in
[before build](02-before-build.md) exists to prevent. Nothing reports this. The repository looks correct
and the protection is absent.

```bash
mkdir -p docs/design/criteria docs/releases
touch docs/design/criteria/.gitkeep docs/releases/.gitkeep
```

The second one is the lockfile. `verify.yml` runs `bun install --frozen-lockfile`, which fails outright if
there is no lockfile to freeze. Commit `bun.lock` in your first commit. `.gitattributes` marks it as
generated so it does not clutter reviews, and generated is not the same as uncommitted — that mark is about
how it is read, not whether it exists.

Both traps share a shape worth naming, because it recurs: the failure is in something absent, and absence
is what no check in this repository is good at seeing. `perimeter.yml` catches one class of it by asking
the host what it enforces. For everything else, the defence is that the tree above is complete and you
built it in one pass.

## What none of these files can do

Every file in this document sits inside the agent's reach. It can edit `CLAUDE.md`, widen
`.claude/settings.json` through a gitignored local override, rewrite an agent definition to give itself
`WebFetch`, or delete a line from `CODEOWNERS`. None of that is hidden — each one is a diff on a protected
path, and the daily ten-minute gate-diff read described in [measurement](11-measurement.md) is what sees
it — but none of it is prevented here.

```
 ┌─ THIS DOCUMENT: INSIDE THE AGENT'S REACH ┐  ┌─ ENFORCEMENT AND HOST: OUTSIDE IT ───────┐
 │  CLAUDE.md, .claude/, agents, commands   │  │  branch protection on main               │
 │  CODEOWNERS as a file in the repo        │  │  required status checks, strict          │
 │  package.json scripts and thresholds     │  │  code-owner review, dismiss stale        │
 │  lefthook.yml and the hooks it installs  │  │  linear history, no force push           │
 │  anything the repo claims about itself   │  │  the merge and approve buttons           │
 └──────────────────────────────────────────┘  └──────────────────────────────────────────┘
              every one a hint                             every one a gate
```

So finish the set, then do the two things that make it mean something. Wire `format:check`, `lint`,
`typecheck`, `test`, `test:coverage` and `build` in `package.json` so `bun run verify` stops failing for the
wrong reason — the per-stack recipes are in [stack wiring](10-stack-wiring.md). And set branch protection
before the first feature commit, following [host and pipeline](09-host-and-pipeline.md). Until protection
is on, everything here is a well-argued suggestion. The pilot had an excellent CI pipeline and a context
file asserting it was enforced. The pipeline ran zero times, and nobody noticed for the length of the
build.

### `.claude/skills/operate-app/SKILL.md`

The skill that closes the gap between requiring evidence for anything with an interface and being able to produce it. Without this, every UI ticket costs a person booting the app by hand.

```markdown
---
name: operate-app
description: Use when a ticket touches anything a person can see or click, and you need to produce the evidence that a criterion is met — boot the app, drive it, capture a screenshot or a trace. Also use when asked to prove a flow works end to end.
---

# Operate the app, and produce the evidence

The rule this exists to satisfy: **a ticket with an interface is not done until something has operated
it.** Not "the component renders" — a page with no Create button renders perfectly. Something has to
click the flow and record what happened.

That something should be you. If a human has to boot the app and take the screenshot, the ticket costs
synchronous human time on every iteration, which is the cost this whole process exists to remove.

## What counts as evidence

One directory per ticket, `.evidence/<TICKET-ID>/`, gitignored. CI uploads it as a pull-request
artefact and comments the link, so it is durable without bloating the repository.

| Criterion is about | Evidence that satisfies it |
|---|---|
| A screen looking right | `<criterion-id>.png` plus the design frame reference in the manifest |
| A flow working | a browser test that clicks it, named in the manifest, plus its output |
| An empty, loading or error state | one screenshot per state, suffixed `-empty`, `-loading`, `-error` |
| An endpoint | the real request and response, `<criterion-id>.http` |
| A background job | the log lines or the query output showing it ran and what it changed |

Every run also writes `.evidence/<TICKET-ID>/manifest.md`:

```markdown
# PULSE-123 evidence

| Criterion | Artefact | What it proves |
|---|---|---|
| CO-1 | co-1.png | guest reaches the confirmation screen without an account |
| CO-2 | co-2-error.png | an expired card shows the retry path, not a generic error |
| CO-4 | checkout.rollback.test.ts | a failed payment leaves no order row |

Boot: `bun run dev` on :3000, seeded with `bun run seed:demo`.
Not covered: CO-5, the empty-cart state. No route reaches it with seed data — flagged in the PR.
```

That last line matters more than the rest. **Say what you could not produce evidence for, and why.**
A manifest with no gaps on a ticket that has gaps is worse than no manifest.

## Booting the app

Read the project's `README.md` and `package.json` first — the commands are there, and if they are not,
that is a finding to report rather than something to guess at. Prefer a documented one-command boot.
If none exists, the first ticket that needs one should add it, because every later ticket pays
otherwise.

Boot in the worktree you are working in, not the developer's main checkout. Two agents on two tickets
must not fight over a port or a database.

## Driving it

Three ways, in order of preference. Use whichever the project already has; do not introduce a second.

**1. A browser test already in the repository.** Best, because it is repeatable and becomes a gate.
Extend the existing suite rather than writing a script beside it.

**2. Chrome DevTools over MCP**, where the session has it. Navigate, snapshot, screenshot, read console
and network. Use the accessibility snapshot rather than a screenshot when you are checking structure —
it is cheaper in context and more precise about what is actually there.

**3. Headless Chromium directly**, when there is no other option:

```bash
"$CHROME" --headless --disable-gpu --hide-scrollbars \
  --force-device-scale-factor=2 --window-size=1440,900 \
  --screenshot=".evidence/$TICKET/co-1.png" "http://localhost:3000/checkout"
```

A screenshot of a page you never interacted with proves the page loads. It does not prove the flow
works. If the criterion is about a flow, you have to click it.

## When you cannot

Stop and say so, in the pull request, naming the criterion. Do not:

- screenshot something adjacent and describe it as the thing
- write "verified" or "tested manually" as prose — that is the exact phrase the process forbids
- mark a criterion proven because the code looks like it should work

An honest gap is a finding. A false artefact is the failure mode the whole document exists to prevent,
and it is worse than an empty cell because it stops anyone looking.

## Two habits worth keeping

**Read the console and the network log**, not just the screen. A page can look correct while throwing.
If there are errors, they belong in the manifest even when the criterion passes.

**Capture the failing state first when you are fixing a bug.** Evidence that a bug existed is worth as
much as evidence it is gone, and it is unrecoverable once you have fixed it.
```

### `.claude/skills/garbage-collect/SKILL.md`

The procedure behind "every defect a person found leaves a check behind". It was a principle with no method and no time allocated, which is how the same review comment gets written for a year.

```markdown
---
name: garbage-collect
description: Use when the same correction has been made twice — in review, in a gate diff, or by hand — and should become a check instead. Also use for the weekly slot where accumulated corrections get converted into enforcement.
---

# Turn a repeated correction into a check

The rule: **every defect a person found leaves a check behind.** If review caught it and nothing was
added, review will catch it again next month, and the process never converges.

This is the procedure for that, and the reason it is a skill rather than a good intention is that it
needs doing on a schedule. Left to when-there-is-time, it never happens, and the same review comment
gets written for a year.

## The trigger

Any of these, and the second one is the important one:

- the same review comment written twice
- a correction you made by hand that you have made before
- a gate diff where somebody weakened a check because it was wrong rather than inconvenient
- an agent that produced the same class of wrong output twice in one ticket

"Twice" is the whole trigger and nobody remembers across weeks, which is what `log/` is for. Before
deciding something is new, check: `grep -ri '<a word from it>' log/events/`. If it is already there with
`disposition: recurring`, this is the second time and it converts now.

## The procedure

**1. Name the class, not the instance.** "This PR forgot a timeout on a fetch" is an instance. "Network
calls in this codebase have no enforced timeout" is the class. You cannot check an instance.

**2. Decide where it belongs**, cheapest first:

| The failure is | The check is |
|---|---|
| A pattern in code that is always wrong here | a lint rule, bespoke to this repository |
| A structural rule — layering, file size, one canonical helper | a test about the source, not its behaviour |
| A missing artefact — no evidence, no criterion, no runbook | a required check on the pull request |
| A judgement nobody can encode | a line in the design document, and a review-agent instruction |
| Something the agent keeps not knowing | a rule in `CLAUDE.md` or the relevant skill |

Prefer a lint or a structural test over a review-agent instruction. The reviewer is probabilistic; a
lint is not.

**3. Write the failure message as a prompt, not a diagnosis.** This is the part people skip and it is
where most of the value is. The agent reads the failure and fixes it without a human in the loop, but
only if the message says what to do:

```
  Diagnosis only, useless:  "no-floating-promises: Promises must be awaited"
  A prompt, self-healing:   "This promise is unawaited. In this codebase every side-effectful call
                             is wrapped in withRetry(...) with an explicit timeout — see
                             src/lib/net.ts. Wrap it, do not add void."
```

If the message does not contain the fix, you have written a speed bump rather than a check.

**4. Migrate the existing violations in the same pass.** A rule that only applies to new code leaves
the codebase in two states, and the next person cannot tell which state is intended. Large-scale
mechanical change is cheap now — there is no excuse for a migration that stays half-finished.

**5. The check change is its own commit.** It touches the protected set, so it cannot ride along with
implementation. Say in the commit which class of failure it eliminates — that sentence is the only place
the reasoning survives, and it is what stops someone deleting the rule in six months for looking
arbitrary.

**6. Close the event.** Set `disposition: converted` and put the commit in `resolution:` on the file in
`log/events/`. An open event nobody dispositioned means the next hour re-litigates the same thing.

## The weekly slot

Once a week, one named person, an hour:

```bash
node scripts/collect-week.mjs --write     # the week's findings, dismissals and divergences, from the host
grep -l 'disposition: open' log/events/*.md
```

The report gives you the material and the counts. It does not group anything — grouping instances into a
class is the judgement, and it is the part that cannot be automated. Convert what recurred; mark what
happened once `recurring` and leave it. A check written for a single incident is one nobody can justify
later.

Every event you touched leaves with a disposition. The count of `converted` is the only evidence the loop
is converging. If a month passes with nothing to convert, either the process is working or nobody is
looking, and those look identical from the outside — which is why the report also prints how many comments
it read.
```

### `.claude/skills/escalate/SKILL.md`

The six classes that require a person, and the record each one leaves. It exists as a skill rather than
a paragraph in `CLAUDE.md` because the agent needs the class list in front of it at the moment it is
deciding, and because the two halves of the rule pull against each other: asking must feel free, and the
same question must not arrive three times.

The routing table is the part that keeps volume tolerable. If every request queues to the developer
holding the ticket, you have rebuilt the bottleneck with extra steps.

````markdown
---
name: escalate
description: Use whenever you hit a situation that needs a person — a decision you lack standing for, an ambiguity that changes the work, a check you believe is wrong, novel territory, or a second failure on the same cause. Defines the six classes, how to grade the request, and the record you must leave.
---

# Calling a human

**Asking is free. Asking the same question twice is a bug.**

Both halves matter. There is no budget on escalations and no virtue in a low count — an agent that
guesses to avoid interrupting has converted a two-minute question into a day of wrong work. But an
escalation that arrives on a third ticket means the answer was missing from somewhere durable, and that
is what the record at the bottom of this file is for.

You are not exercising judgement about *whether* to escalate. You are matching the situation against six
classes. If it matches, stop and ask, regardless of how confident you feel.

## The six classes

**A — Authority.** You do not have the standing to decide. Hard stop, nothing proceeds.

- Anything that changes what the client accepts: an acceptance criterion, a scope boundary
- Anything commercial: timeline, cost, what is in or out of a phase
- Any change to the protected set: payments, personal data, auth, migrations, CI or hook config,
  existing tests, coverage thresholds, `CODEOWNERS`, context files
- Anything irreversible: a production write, a data migration, sending email, publishing, deleting
  something nobody asked to have deleted
- Spending past the ticket's token budget

**B — Ambiguity that changes the work.** Ask, then pick up something else while you wait.

- The design document and the code disagree. The most valuable escalation there is — the document has
  gone stale and every later ticket would rediscover it
- A criterion cannot be proven as written; no artefact would settle it
- The spec does not answer something you must decide to proceed
- Two patterns already in the codebase both apply and imply different designs

**C — Judgement that cannot be encoded.** Does this look right. Would this client accept it. Is this the
right trade-off. No check will ever settle these.

**D — The system is wrong, not the code.** Hard stop. The most under-reported class.

- A check fails and you believe the check is incorrect
- A gate blocks something that should be allowed
- Two rules cannot both be satisfied

Working around a wrong gate quietly teaches us nothing and leaves the gate wrong.

**E — Novel territory.** No precedent in this codebase and none in the design document, or the spec
graded this *genuinely novel*. Models are least reliable where training data is thinnest and least likely
to signal it.

**F — Repeated failure.** A gate has gone red twice on the same cause. Two attempts, then stop. Looping
on a red check burns budget and produces no evidence.

## Grade the request

Only one of these interrupts anybody:

- **Blocking** — work stops until answered.
- **Worth knowing** — you proceeded on a stated assumption. Say which assumption.
- **Pre-existing** — already true before this ticket. Logged, not this ticket's problem.

A person answering thirty requests in a day is answering the last ten badly, and a badly answered
escalation is worse than none because it carries authority. Grading is how you avoid that without asking
less.

## Route it

To the developer holding the ticket by default — but not everything. If every request queues to one
person you have rebuilt the bottleneck with extra steps.

| Class | Goes to |
|---|---|
| A, commercial or scope | whoever owns the SOW |
| A, acceptance criteria | a code owner |
| C | the tech lead |
| D | whoever owns the gate |
| B, E, F | the developer holding the ticket |

## The format

An escalation a person cannot answer in two minutes has failed.

```markdown
**Ticket** PULSE-142   **Class** B — ambiguity that changes the work   **Blocking**

The design document says a guest checkout keeps the cart for 30 days. `cart.service.ts:88` expires it
after 7, and has since the first commit. Both are defensible and they produce different work.

- If 30 days is right: a config value and one migration for existing rows.
- If 7 days is right: the design document is wrong, and criterion CO-7 needs rewording — which is a
  criteria change and therefore yours.

**Not blocked:** CO-1 through CO-4 are finished and pushed. This is the last item.
**My read, if it helps:** 7 days, because it predates the document and nobody has complained.
```

Four things make it answerable: the class, the specific decision, the consequence of each answer, and
what is **not** blocked. Your own read comes last and is optional — useful for speed, dangerous if it
becomes the thing that gets approved without being read.

## Leave the record. This part is not optional.

Write `log/events/YYYY-MM-DD-short-slug.md` in the same commit as anything else you push:

```markdown
---
date: 2026-08-04
kind: escalation-B
ticket: PULSE-142
raised_by: agent
summary: design document says 30-day guest cart, cart.service.ts has said 7 since the first commit
disposition: open
resolution:
---

Escalated on PR #214. Both readings defensible; blocked on one decision.
```

Schema and dispositions are in `log/README.md`. Write the file even when the answer arrives immediately —
**especially** then, because a question that is easy to answer is the most likely kind to be asked again,
and the record is the only thing that will notice.

You write the file. You do not decide what becomes a check: that happens in the weekly hour, by a person,
across everything that accumulated. You cannot do it because each of your runs starts with no memory of
the last one — which is the entire reason this log exists.
````

### `log/README.md`

The one artefact added purely to make `garbage-collect` work. Its trigger is *the same correction twice*,
and nothing recorded the first occurrence — human memory was the mechanism, and it does not scale past
one person or one week.

Read the opening paragraph carefully, because the failure mode is specific: this is **not** a learnings
document. Learnings already have four destinations that something actually reads — a lint, a structural
test, `REVIEW.md`, a skill. A fifth destination that nothing reads competes with those and gives a
learning somewhere legitimate to go that is not a check.

````markdown
# The log

Raw material for the weekly garbage-collection hour. One file per event, append-only, and every file
eventually reaches a disposition.

**This is not a learnings document.** Nothing here is written to be read for insight, and nobody reads it
except the weekly hour. A learning that belongs somewhere durable goes in a lint, a structural test,
`REVIEW.md`, `CLAUDE.md`, a skill or a decision record — all of which have a guaranteed reader. This
directory exists for one reason: `garbage-collect` triggers on **the same correction twice**, and that
needs a memory longer than one person's.

## Why one file per event

Two branches appending rows to a shared table conflict on the same line. Two branches adding differently
named files never conflict. An agent writes its escalation on a ticket branch, which merges through a
pull request like anything else.

## The schema

`log/events/YYYY-MM-DD-short-slug.md`:

```markdown
---
date: 2026-08-04
kind: escalation-B
ticket: PULSE-142
raised_by: agent
summary: design document says 30-day guest cart, cart.service.ts has said 7 since the first commit
disposition: open
resolution:
---

Anything worth keeping that does not fit in the summary. Usually nothing. Links are better than prose —
the pull request, the comment, the failing run.
```

Seven fields, all mechanical. Nothing here requires a judgement at write time, which is the only reason
it gets written at all.

| Field | Values |
|---|---|
| `kind` | `escalation-A` … `escalation-F` (see the `escalate` skill), `review-finding`, `dismissal`, `divergence`, `defect` |
| `raised_by` | `agent`, `script`, or a person's name |
| `summary` | One line. What happened — not what should be done about it |
| `disposition` | `open`, `converted`, `recurring`, `closed` |
| `resolution` | Required unless `open`. For `converted`, the commit or pull request that added the check |

**Dispositions, and what each one commits you to.**

- **`open`** — not yet looked at. The weekly hour's queue is exactly this set.
- **`converted`** — a check now exists that would have caught it. Name the commit.
- **`recurring`** — happened once, watching for the second. This is the disposition that makes the whole
  thing work: it is the memory that `garbage-collect` needs and nothing else provides.
- **`closed`** — a one-off, deliberately not converted. A check written for a single incident is one
  nobody can justify later.

## How events arrive

Most of them are already recorded somewhere and get extracted rather than typed:

| Kind | Where it comes from |
|---|---|
| `escalation-A`…`F` | The agent writes the file when it escalates. It knows the class and the reason |
| `review-finding` | Pull request review comments — extracted by `scripts/collect-week.mjs` |
| `dismissal` | A review reply beginning `Dismissed:` — extracted, which is why the prefix is required |
| `divergence` | The pull request template's "what the design document got wrong" — extracted |
| `defect` | **Hand-written.** Something found after merge. Nothing else in the system knows about these |

That last row is the only recurring manual entry, and it is the one worth doing by hand: a defect that
reached a person is the only measurement that cannot be gamed.

## The weekly hour

```bash
node scripts/collect-week.mjs --write     # assembles this week's report from the host
grep -l 'disposition: open' log/events/*.md
```

Read the report, group the open events into classes, convert the ones that recurred, and set a
disposition on every file you touched. An event left `open` for a second week is either a class nobody
cares about — close it — or the process is not running.

The count of `converted` events is the only evidence the loop is converging. If a month passes with none,
either the process is working or nobody is looking, and those two look identical from outside.
````

### `log/events/_template.md`

One file per event, because two branches appending rows to a shared table conflict on the same line and
two branches adding differently named files never do. Seven fields, none of which needs a judgement at
write time — which is the only reason it gets written.

```markdown
---
date: 2026-08-04
kind: escalation-B
ticket: PULSE-142
raised_by: agent
summary: one line — what happened, not what should be done about it
disposition: open
resolution:
---

Links beat prose: the pull request, the comment, the failing run. Usually there is nothing to add here.

Copy this to `YYYY-MM-DD-short-slug.md`. Files starting with `_` are ignored by the collector.
Field values are in `log/README.md`.
```

### `scripts/collect-week.mjs`

Assembles the weekly hour's raw material from the host. Almost none of it is typed by anyone: review
findings, dismissals, what the design document got wrong and the questions a spec asked are all recorded
already, scattered across pull requests. Only defects reaching a person are hand-written, because nothing
else in the system knows about those.

Three things in it came from running it rather than reading it. It fetches concurrently, because 141
serial calls took over two minutes on a real repository and a weekly tool that slow gets skipped. It
retries once, because a single dropped connection should not cost a week's material. And it prints how
many comments it read, because *no findings* and *nothing looked* must not render identically — that
confusion is the failure this entire loop exists to prevent, and a report is not exempt from it.

It deliberately does not group findings into classes. That is the judgement, it is the part worth a
person's hour, and a tool that guessed at it would be believed.

```javascript
#!/usr/bin/env node
// Assembles the raw material for the weekly garbage-collection hour.
//
// Almost everything the hour needs is already recorded — scattered across pull requests. This pulls it
// into one place so nobody has to remember to write it down: review findings, dismissals, what the design
// document got wrong, and the open events in log/events/.
//
// It does not decide anything. Grouping findings into classes and converting them into checks is the
// human's job, and the report says so where it would otherwise look like the script had done it.
//
//   node scripts/collect-week.mjs                # print the report
//   node scripts/collect-week.mjs --write        # also write log/weeks/YYYY-Www.md
//   node scripts/collect-week.mjs --days 14      # a longer window
//
// Needs gh, authenticated. If it cannot reach the host the report is marked PARTIAL and this exits 1 —
// a partial report that looks complete is the failure this whole loop exists to avoid.

import { execFile } from "node:child_process";
import { promisify } from "node:util";
import { readdirSync, readFileSync, writeFileSync, mkdirSync, existsSync } from "node:fs";
import { join } from "node:path";

const args = process.argv.slice(2);
const flag = (n, d) => { const i = args.indexOf(n); return i === -1 ? d : args[i + 1]; };
const DAYS = Number(flag("--days", 7));
const WRITE = args.includes("--write");
const SINCE = new Date(Date.now() - DAYS * 864e5);

const problems = [];
const run = promisify(execFile);

// One retry, because a transient `unexpected EOF` from the API should not cost a week's material.
// Observed on a real run: one dropped connection out of 141 calls.
const gh = async (a) => {
  for (let attempt = 0; ; attempt++) {
    try { return JSON.parse((await run("gh", a, { maxBuffer: 64 << 20 })).stdout); }
    catch (e) { if (attempt) throw e; await new Promise((r) => setTimeout(r, 800)); }
  }
};

// 141 serial calls took over two minutes on a real repository. A weekly tool that slow gets skipped.
const pool = async (items, n, fn) => {
  const out = [], it = items[Symbol.iterator]();
  await Promise.all(Array.from({ length: Math.min(n, items.length) }, async () => {
    for (let x = it.next(); !x.done; x = it.next()) out.push(await fn(x.value));
  }));
  return out;
};

// ── the host ────────────────────────────────────────────────────────────────────────────────────────
let repo = flag("--repo", null), prs = [];
try {
  repo ??= (await gh(["repo", "view", "--json", "nameWithOwner"])).nameWithOwner;
  prs = (await gh(["pr", "list", "-R", repo, "--state", "merged", "--limit", "200",
                   "--json", "number,title,mergedAt,body,author"]))
    .filter((p) => new Date(p.mergedAt) >= SINCE);
} catch (e) {
  problems.push(`could not read the host: ${String(e.message).split("\n")[0]}`);
}

const findings = [], dismissals = [], divergences = [], learned = [];
const GRADE = /^[\s>*_\-–•\d.]*(?:\*\*)?(important|nit|pre-existing)(?:\*\*)?\s*[:—–-]?\s*(.*)$/i;
const DISMISS = /^[\s>*_\-–•]*(?:\*\*)?dismissed(?:\*\*)?\s*:\s*(.*)$/i;

const section = (body, re) => {
  const lines = (body || "").split("\n");
  const at = lines.findIndex((l) => /^#{1,6}\s/.test(l) && re.test(l));
  if (at === -1) return "";
  const rest = lines.slice(at + 1);
  const end = rest.findIndex((l) => /^#{1,6}\s/.test(l));
  return (end === -1 ? rest : rest.slice(0, end)).join("\n");
};
const meaningful = (t) =>
  t.replace(/<!--[\s\S]*?-->/g, "")            // template comments
   .split("\n").map((l) => l.trim())
   .filter((l) => l && !/^[-*_]$/.test(l) && !/^(none|n\/?a|nothing|tbd)\.?$/i.test(l))
   .join("\n").trim();

let commentsRead = 0;
await pool(prs, 8, async (pr) => {
  let bodies = [];
  try {
    const [reviews, inline, issue] = await Promise.all([
      gh(["api", `repos/${repo}/pulls/${pr.number}/reviews`, "--paginate"]),
      gh(["api", `repos/${repo}/pulls/${pr.number}/comments`, "--paginate"]),
      gh(["api", `repos/${repo}/issues/${pr.number}/comments`, "--paginate"]),
    ]);
    bodies = [
      ...reviews.map((r) => ({ body: r.body, who: r.user?.login, path: null })),
      ...inline.map((c) => ({ body: c.body, who: c.user?.login, path: c.path })),
      ...issue.map((c) => ({ body: c.body, who: c.user?.login, path: null })),
    ].filter((c) => c.body);
    commentsRead += bodies.length;
  } catch (e) {
    problems.push(`#${pr.number} comments unreadable: ${String(e.message).split("\n")[0]}`);
  }

  for (const c of bodies) {
    for (const line of (c.body || "").split("\n")) {
      const d = line.match(DISMISS);
      if (d) { dismissals.push({ pr: pr.number, who: c.who, text: d[1].trim() }); continue; }
      const g = line.match(GRADE);
      if (g && g[2].trim().length > 12) {
        findings.push({ pr: pr.number, grade: g[1].toLowerCase(), path: c.path, text: g[2].trim() });
      }
    }
  }

  const wrong = meaningful(section(pr.body, /design document got wrong/i));
  if (wrong) divergences.push({ pr: pr.number, title: pr.title, text: wrong });
  const l = meaningful(section(pr.body, /learned that was not in the design/i));
  if (l) learned.push({ pr: pr.number, text: l });
});

// ── specs written this window ───────────────────────────────────────────────────────────────────────
// The explore agent asks everything in one pass and carries the answers into the spec verbatim, so the
// questions are already recorded. Nothing extra needs writing: this reads them out of the specs that
// appeared this week. "Which of these should never have needed asking" is the fourth question of the hour.
const asked = [];
try {
  const added = (await run("git", ["log", `--since=${SINCE.toISOString()}`, "--diff-filter=A",
                                   "--name-only", "--pretty=format:", "--", "docs/specs"]))
    .stdout.split("\n").map((s) => s.trim())
    .filter((f) => f.endsWith(".md") && !f.includes("_template"));
  for (const f of [...new Set(added)]) {
    if (!existsSync(f)) continue;
    const body = readFileSync(f, "utf8");
    const q = meaningful(section(body, /questions and answers/i));
    const dis = meaningful(section(body, /design document and the code disagree/i));
    if (q || dis) asked.push({ file: f, q, dis });
  }
} catch { /* not a git repository, or no specs yet — neither is a problem worth failing over */ }

// ── the log ─────────────────────────────────────────────────────────────────────────────────────────
const EV = "log/events";
const events = !existsSync(EV) ? [] : readdirSync(EV)
  .filter((f) => f.endsWith(".md") && !f.startsWith("_"))
  .map((f) => {
    const raw = readFileSync(join(EV, f), "utf8");
    const fm = raw.match(/^---\n([\s\S]*?)\n---/);
    const o = { file: f };
    for (const line of (fm?.[1] || "").split("\n")) {
      const m = line.match(/^([a-z_]+):\s*(.*)$/);
      if (m) o[m[1]] = m[2].trim();
    }
    return o;
  });
const open = events.filter((e) => (e.disposition || "open") === "open");
const thisWeek = events.filter((e) => e.date && new Date(e.date) >= SINCE);
const byKind = (list) => Object.entries(list.reduce((a, e) => ((a[e.kind || "?"] = (a[e.kind || "?"] || 0) + 1), a), {}))
  .sort((a, b) => b[1] - a[1]);

// ── the one mechanical hint at recurrence ───────────────────────────────────────────────────────────
// Groups findings whose opening words match. Cheap and sometimes useful. Real grouping is a judgement,
// so this is labelled a hint and nothing downstream depends on it.
const key = (t) => t.toLowerCase().replace(/`[^`]*`/g, " ").replace(/[^a-z ]/g, " ")
  .split(/\s+/).filter(Boolean).slice(0, 6).join(" ");
const repeated = Object.entries(findings.reduce((a, f) => ((a[key(f.text)] ||= []).push(f), a), {}))
  .filter(([, g]) => g.length > 1 && new Set(g.map((f) => f.pr)).size > 1)
  .sort((a, b) => b[1].length - a[1].length);
const hotPaths = Object.entries(findings.filter((f) => f.path)
  .reduce((a, f) => ((a[f.path] ||= new Set()).add(f.pr), a), {}))
  .filter(([, s]) => s.size > 1).sort((a, b) => b[1].size - a[1].size);

// ── report ──────────────────────────────────────────────────────────────────────────────────────────
const d = new Date(Date.now() - 3 * 864e5); // ISO week of the window's middle
const wk = (() => { const t = new Date(Date.UTC(d.getFullYear(), d.getMonth(), d.getDate()));
  t.setUTCDate(t.getUTCDate() + 4 - (t.getUTCDay() || 7));
  return `${t.getUTCFullYear()}-W${String(Math.ceil(((t - Date.UTC(t.getUTCFullYear(), 0, 1)) / 864e5 + 1) / 7)).padStart(2, "0")}`; })();
const n = (x) => (Array.isArray(x) ? x.length : x);
const pct = (a, b) => (b ? `${Math.round((a / b) * 100)}%` : "—");
const L = [];
const p = (s = "") => L.push(s);

p(`# ${wk} — ${repo || "(repo unknown)"}`);
p();
if (problems.length) {
  p(`> **PARTIAL — ${problems.length} thing(s) could not be read.** Do not read the counts below as rates.`);
  problems.slice(0, 6).forEach((x) => p(`> - ${x}`));
  if (problems.length > 6) p(`> - …and ${problems.length - 6} more`);
  p();
}
p(`Window: ${DAYS} days, from ${SINCE.toISOString().slice(0, 10)}.`);
p();
p("| | |");
p("|---|---|");
p(`| Pull requests merged | ${n(prs)} |`);
p(`| Comments read | ${commentsRead} |`);
p(`| Review findings | ${n(findings)} (${["important", "nit", "pre-existing"].map((g) => `${findings.filter((f) => f.grade === g).length} ${g}`).join(", ")}) |`);
p(`| Findings per pull request | ${prs.length ? (findings.length / prs.length).toFixed(1) : "—"} |`);
p(`| Dismissed | ${n(dismissals)} — ${pct(dismissals.length, findings.length)} of findings |`);
p(`| Design document diverged | ${n(divergences)} of ${n(prs)} |`);
p(`| Escalations logged | ${n(thisWeek.filter((e) => (e.kind || "").startsWith("escalation")))} |`);
p(`| Defects reaching a person | ${n(thisWeek.filter((e) => e.kind === "defect"))} |`);
p(`| Specs written | ${n(asked)} carrying questions |`);
p(`| Open events carried in | ${n(open)} |`);
p();
// "Nothing found" and "nothing looked" must not render identically. That confusion is the failure mode
// this whole loop exists to prevent, and a report is not exempt from it.
if (!findings.length && commentsRead)
  p(`No graded findings in ${commentsRead} comments. Either the week was clean, or findings are not being written as **Important** / **Nit** / **Pre-existing** — check one pull request by hand before believing the first reading.`);
else if (!commentsRead && prs.length)
  p("No comments were read at all, so the finding count means nothing.");
p();

const list = (title, rows, fmt) => { if (!rows.length) return; p(`## ${title}`); p(); rows.forEach((r) => p(fmt(r))); p(); };

p("## The queue");
p();
if (!open.length) p("Nothing open. Either the week was quiet or nothing is being logged — those look identical here, so check that `log/events/` grew at all.");
else { p("Every one of these needs a disposition before the hour ends: `converted`, `recurring` or `closed`.");
  p(); byKind(open).forEach(([k, c]) => p(`- **${k}** — ${c}`));
  p(); open.forEach((e) => p(`- \`${e.file}\` — ${e.kind || "?"} · ${e.ticket || "no ticket"} — ${e.summary || "(no summary)"}`)); }
p();

if (repeated.length) {
  p("## Possibly the same thing twice — hint only");
  p();
  p("Matched on opening words across different pull requests. A mechanical guess, not a grouping. The");
  p("classes that matter will not all show up here, and some of these are coincidence.");
  p();
  repeated.forEach(([k, g]) => { p(`**${g.length}× “${k}…”** — PRs ${[...new Set(g.map((f) => f.pr))].join(", ")}`);
    g.slice(0, 3).forEach((f) => p(`  - ${f.grade}: ${f.text.slice(0, 160)}`)); p(); });
}
list("Files drawing findings in more than one pull request", hotPaths, ([f, s]) => `- \`${f}\` — ${s.size} pull requests`);
list("What the design document got wrong", divergences, (r) => `**#${r.pr}** ${r.title}\n${r.text}\n`);
list("Asked before work started", asked, (r) =>
  `**${r.file}**\n${r.q ? r.q + "\n" : ""}${r.dis ? `\n_Design document vs code:_ ${r.dis}\n` : ""}`);
list("Dismissed findings", dismissals, (r) => `- **#${r.pr}** ${r.who || ""}: ${r.text.slice(0, 200)}`);
list("Learned, and where it landed", learned, (r) => `**#${r.pr}**\n${r.text}\n`);
list("All findings", findings, (r) => `- **#${r.pr}** ${r.grade}${r.path ? ` \`${r.path}\`` : ""} — ${r.text.slice(0, 200)}`);

p("## The four questions");
p();
p("1. Which of these happened before? Those convert. The rest get `recurring` and wait for a second.");
p("2. For each conversion: lint, structural test, required check, `REVIEW.md` line, or a rule in a skill —");
p("   cheapest that actually holds. Prefer a lint over a review instruction; the reviewer is probabilistic.");
p("3. Does the failure message contain the fix, or only the diagnosis? A diagnosis is a speed bump.");
p("4. Which escalation should never have needed asking? That answer was missing from something durable.");
p();
p(`Dismissal rate ${pct(dismissals.length, findings.length)}. Above roughly one in three and the reviewer is`);
p("costing more attention than it saves — tighten `REVIEW.md` rather than ignoring it.");

const out = L.join("\n") + "\n";
process.stdout.write(out);
if (WRITE) {
  mkdirSync("log/weeks", { recursive: true });
  writeFileSync(`log/weeks/${wk}.md`, out);
  process.stderr.write(`\nwrote log/weeks/${wk}.md\n`);
}
process.exit(problems.length ? 1 : 0);
```

### `scripts/board.mjs`

Three modes over one source. `--check` asserts the board is well-formed and that its view is current;
`--index` rewrites the summary table inside `board.md`; `--html` regenerates `tasks/board.html`.

The design decision worth understanding is why a second representation is safe here when it usually is not.
The project this board came from keeps a hand-maintained `dag-board.html` and has a written lesson that
exists **only** because its agent kept forgetting to update it — a rule in prose standing in for a check,
which is the failure these documents are about. Here the view is generated and its staleness is a fact:
`--check` rebuilds it in memory and fails when what is on disk differs, a `PostToolUse` hook regenerates it
whenever a session writes a file, and `verify.yml` refuses to merge a stale one. Nothing is left to anyone
remembering, because nothing has to be remembered — change `board.md` and the view follows.

```javascript
#!/usr/bin/env node
// The board is the tracker, so the two properties that keep it honest are checked rather than trusted.
//
//   node scripts/board.mjs --check            # every entry well-formed; used by CI
//   node scripts/board.mjs --check PULSE-142  # ...and this ticket has an entry
//   node scripts/board.mjs --index            # rewrite the index table in place
//   node scripts/board.mjs --html             # regenerate tasks/board.html
//
// tasks/board.md is the ONLY writable source. board.html is generated from it and must never be edited by
// hand — that is the whole reason it is safe to have. The project this board was adopted from keeps a
// hand-maintained dag-board.html and has a written lesson that exists only because its agent kept
// forgetting to update it. A generated view cannot be forgotten: `--check` regenerates it in memory and
// fails if what is on disk differs, so a stale view cannot merge, and a Claude hook regenerates it the
// moment the board changes.

import { readFileSync, writeFileSync, existsSync } from "node:fs";

const BOARD = "tasks/board.md";
const args = process.argv.slice(2);
const TICKET = args.find((a) => /^[A-Z][A-Z0-9]+-[0-9]+$/.test(a));

if (!existsSync(BOARD)) {
  console.error(`::error::${BOARD} is missing. The board IS the tracker — without it a ticket has no home.`);
  process.exit(1);
}
const raw = readFileSync(BOARD, "utf8");
const lines = raw.split("\n");

// ── parse ───────────────────────────────────────────────────────────────────────────────────────────
// An entry is a level-1 heading whose text starts with a ticket id. Everything above the first one is
// the file's own preamble, and the fenced template inside it must not be read as an entry — so fences
// are tracked and skipped.
const entries = [];
let fence = null;
lines.forEach((line, i) => {
  const f = line.match(/^(`{3,})/);
  if (f) { fence = fence && line.startsWith(fence) ? null : fence || f[1]; return; }
  if (fence) return;
  const m = line.match(/^# ([A-Z][A-Z0-9]+-[0-9]+)\b\s*(.*)$/);
  if (m) entries.push({ id: m[1], title: m[2].replace(/^—\s*/, ""), line: i + 1, body: [] });
  else if (entries.length) entries.at(-1).body.push(line);
});

for (const e of entries) {
  const text = e.body.join("\n");
  e.state = (text.match(/^\*\*State\*\*\s*(.+)$/m)?.[1] || "").trim();
  e.done = /^DONE\b/i.test(e.state);
  e.blockedBy = (text.match(/^\*\*Blocked by\*\*\s*(.+)$/m)?.[1] || "").trim();
  e.hasResolution = /^##\s+Resolution\b/m.test(text);
  e.num = Number(e.id.split("-")[1]);
}

// ── the view ────────────────────────────────────────────────────────────────────────────────────────
// Generated from the entries above. Self-contained: no network, no fonts, no scripts, so it opens from
// disk and from a static host identically, and renders in light or dark.
const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));

// Enough markdown for a board entry to stay readable. Deliberately small — a dependency here would put a
// package install between somebody and looking at the board.
function mini(md) {
  const out = [];
  let list = false, code = false;
  for (const raw of md.split("\n")) {
    const l = raw.replace(/\s+$/, "");
    if (/^\s*```/.test(l)) { if (list) { out.push("</ul>"); list = false; } code = !code; out.push(code ? "<pre><code>" : "</code></pre>"); continue; }
    if (code) { out.push(esc(raw)); continue; }
    const inline = (s) => esc(s)
      .replace(/`([^`]+)`/g, "<code>$1</code>")
      .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
      .replace(/(?<!\*)\*([^*]+)\*(?!\*)/g, "<em>$1</em>");
    const h = l.match(/^(#{2,4})\s+(.*)$/);
    const li = l.match(/^\s*[-*]\s+(?:\[( |x|X)\]\s+)?(.*)$/);
    if (h) { if (list) { out.push("</ul>"); list = false; } out.push(`<h4>${inline(h[2])}</h4>`); continue; }
    if (li) {
      if (!list) { out.push("<ul>"); list = true; }
      const box = li[1] === undefined ? "" : `<span class="box ${/x/i.test(li[1]) ? "on" : ""}">${/x/i.test(li[1]) ? "✓" : ""}</span>`;
      out.push(`<li>${box}${inline(li[2])}</li>`);
      continue;
    }
    if (list) { out.push("</ul>"); list = false; }
    if (l.trim() === "") continue;
    out.push(`<p>${inline(l)}</p>`);
  }
  if (list) out.push("</ul>");
  if (code) out.push("</code></pre>");
  return out.join("\n");
}

function buildHtml() {
  const bucket = (e) =>
    e.done ? "done"
    : /^blocked/i.test(e.state) ? "blocked"
    : /^in progress/i.test(e.state) ? "running"
    : "open";
  const GROUPS = [
    ["running", "In progress", "Being worked on right now"],
    ["blocked", "Blocked", "Waiting on an answer or another ticket"],
    ["open", "Open", "Ready to pick up"],
    ["done", "Done", "Closed, with a resolution"],
  ];
  const counts = Object.fromEntries(GROUPS.map(([k]) => [k, entries.filter((e) => bucket(e) === k).length]));

  const card = (e) => {
    const body = e.body.join("\n").replace(/^\*\*(State|Depth|Blocked by|Raised by)\*\*.*$/gm, "").trim();
    const meta = [e.state, e.blockedBy && `blocked by ${e.blockedBy}`].filter(Boolean).join(" · ");
    return `<details class="card ${bucket(e)}"${bucket(e) === "running" ? " open" : ""}>
<summary><span class="id">${esc(e.id)}</span><span class="title">${esc(e.title || "")}</span><span class="meta">${esc(meta)}</span></summary>
<div class="body">${body ? mini(body) : "<p class='empty'>No detail recorded. An entry with no Goal or Findings is a title, not a ticket.</p>"}</div>
</details>`;
  };

  return `<title>Board</title>
<style>
:root{--bg:#fbfaf8;--panel:#fff;--ink:#1a1a19;--ink2:#55554f;--ink3:#87877f;--line:#e6e3dc;
--run:#8a5a2b;--blk:#9c3d2e;--opn:#4a4a7a;--dne:#2d6a4f;--mono:ui-monospace,'SF Mono',Menlo,monospace}
@media(prefers-color-scheme:dark){:root{--bg:#161619;--panel:#1e1e22;--ink:#ececea;--ink2:#b0b0aa;
--ink3:#82827c;--line:#32323a;--run:#d99f5e;--blk:#e39b8c;--opn:#a8a8c8;--dne:#7fc6a1}}
:root[data-theme=dark]{--bg:#161619;--panel:#1e1e22;--ink:#ececea;--ink2:#b0b0aa;--ink3:#82827c;
--line:#32323a;--run:#d99f5e;--blk:#e39b8c;--opn:#a8a8c8;--dne:#7fc6a1}
:root[data-theme=light]{--bg:#fbfaf8;--panel:#fff;--ink:#1a1a19;--ink2:#55554f;--ink3:#87877f;
--line:#e6e3dc;--run:#8a5a2b;--blk:#9c3d2e;--opn:#4a4a7a;--dne:#2d6a4f}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:400 15px/1.6 -apple-system,BlinkMacSystemFont,'Segoe UI',system-ui,sans-serif}
.wrap{max-width:900px;margin:0 auto;padding:40px 22px 80px}
h1{font-size:22px;margin:0 0 4px;letter-spacing:-.01em}
.note{color:var(--ink3);font:400 12px/1.5 var(--mono);margin:0 0 26px}
.tallies{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 30px}
.tally{border:1px solid var(--line);background:var(--panel);border-radius:6px;padding:8px 12px;min-width:96px}
.tally b{display:block;font:650 20px/1.2 var(--mono)}
.tally span{font:500 10px/1 var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--ink3)}
.tally.running b{color:var(--run)}.tally.blocked b{color:var(--blk)}
.tally.open b{color:var(--opn)}.tally.done b{color:var(--dne)}
h2{font:650 11px/1 var(--mono);letter-spacing:.12em;text-transform:uppercase;color:var(--ink3);
margin:34px 0 4px;padding-bottom:8px;border-bottom:1px solid var(--line)}
h2 em{font-style:normal;text-transform:none;letter-spacing:0;font-weight:400;color:var(--ink3)}
.card{border:1px solid var(--line);background:var(--panel);border-radius:7px;margin:8px 0;overflow:hidden}
.card>summary{cursor:pointer;padding:11px 14px;display:flex;gap:10px;align-items:baseline;flex-wrap:wrap;list-style:none}
.card>summary::-webkit-details-marker{display:none}
.card>summary::before{content:'▸';color:var(--ink3);font-size:11px;margin-right:2px}
.card[open]>summary::before{content:'▾'}
.id{font:600 12px/1.4 var(--mono)}
.card.running .id{color:var(--run)}.card.blocked .id{color:var(--blk)}
.card.open .id{color:var(--opn)}.card.done .id{color:var(--dne)}
.title{flex:1;min-width:200px}
.card.done .title{color:var(--ink2)}
.meta{font:400 11px/1.4 var(--mono);color:var(--ink3)}
.body{padding:2px 16px 14px;border-top:1px solid var(--line);color:var(--ink2);font-size:14px}
.body h4{font-size:12px;letter-spacing:.04em;text-transform:uppercase;color:var(--ink3);margin:16px 0 4px}
.body p{margin:6px 0}.body ul{margin:6px 0;padding-left:20px}.body li{margin:3px 0}
.body code{font:400 12.5px var(--mono);background:var(--bg);border:1px solid var(--line);border-radius:3px;padding:.5px 4px}
.body pre{overflow-x:auto;background:var(--bg);border:1px solid var(--line);border-radius:5px;padding:10px}
.body pre code{border:0;background:none;padding:0}
.box{display:inline-block;width:13px;height:13px;border:1px solid var(--line);border-radius:3px;
margin-right:7px;text-align:center;font-size:9px;line-height:12px;color:var(--dne)}
.box.on{border-color:var(--dne)}
.empty{color:var(--ink3);font-style:italic}
.none{color:var(--ink3);font-size:13px;margin:10px 0}
</style>
<div class="wrap">
<h1>Board</h1>
<p class="note">Generated from tasks/board.md — do not edit. Regenerate: node scripts/board.mjs --html</p>
<div class="tallies">
${GROUPS.map(([k, label]) => `<div class="tally ${k}"><b>${counts[k]}</b><span>${label}</span></div>`).join("\n")}
</div>
${GROUPS.map(([k, label, hint]) => {
  const list = entries.filter((e) => bucket(e) === k).sort((a, b) => a.num - b.num);
  return `<h2>${label} <em>— ${hint}</em></h2>\n${list.length ? list.map(card).join("\n") : `<p class="none">Nothing here.</p>`}`;
}).join("\n")}
</div>
`;
}

// ── check ───────────────────────────────────────────────────────────────────────────────────────────
if (args.includes("--check")) {
  const problems = [];

  // A duplicate id makes two branches resolve to one spec, and spec.yml cannot tell them apart.
  const seen = new Map();
  for (const e of entries) {
    if (seen.has(e.id)) problems.push(`${e.id} appears twice (lines ${seen.get(e.id)} and ${e.line}). Ids are never reused.`);
    else seen.set(e.id, e.line);
  }

  for (const e of entries) {
    if (!e.state) problems.push(`${e.id} has no **State** line. open | in progress | blocked | DONE (date)`);

    // The honesty check. Marking something done without saying what changed — and what did NOT — throws
    // away the more useful half, which is the whole reason this board beats a tracker field.
    if (e.done && !e.hasResolution)
      problems.push(`${e.id} is DONE with no "## Resolution". Say what changed, what you deliberately left alone, and what is still open.`);

    // A blocker that does not exist is a typo wearing the appearance of a dependency.
    for (const b of e.blockedBy.split(/[,\s]+/).filter((x) => /^[A-Z][A-Z0-9]+-[0-9]+$/.test(x)))
      if (!seen.has(b)) problems.push(`${e.id} is blocked by ${b}, which has no entry on the board.`);
  }

  if (TICKET && !seen.has(TICKET))
    problems.push(`This branch is ${TICKET} and the board has no entry for it. Add one before opening a pull request — a ticket that exists only in a branch name is not a ticket.`);

  if (problems.length) {
    console.error(`::error::${BOARD} has ${problems.length} problem(s).`);
    problems.forEach((p) => console.error(`  ${p}`));
    process.exit(1);
  }
  // The view is generated, so staleness is a fact rather than a matter of diligence: regenerate it in
  // memory and compare. This is what makes it impossible for a session to "forget" the HTML.
  const wanted = buildHtml();
  const onDisk = existsSync("tasks/board.html") ? readFileSync("tasks/board.html", "utf8") : null;
  if (onDisk !== wanted) {
    console.error("::error::tasks/board.html is stale — it does not match tasks/board.md.");
    console.error("  Run: node scripts/board.mjs --html   and commit the result.");
    console.error("  It is generated, never hand-edited, which is the only reason it is safe to keep.");
    process.exit(1);
  }

  const open = entries.filter((e) => !e.done).length;
  console.log(`${BOARD}: ${entries.length} entries, ${open} open, ${entries.length - open} done. Well-formed, view current.`);
  process.exit(0);
}

// ── index ───────────────────────────────────────────────────────────────────────────────────────────
// Regenerated in place between markers, so the "view" is the file itself and can never be stale in a way
// nobody sees. Running this is idempotent; a drifted index shows up as a diff.
if (args.includes("--index")) {
  const START = "<!-- board:index -->";
  const END = "<!-- /board:index -->";
  const rows = entries
    .slice()
    .sort((a, b) => Number(a.done) - Number(b.done) || a.num - b.num)
    .map((e) => `| ${e.done ? "✓" : "·"} | \`${e.id}\` | ${e.title || ""} | ${e.state || "—"} | ${e.blockedBy || ""} |`);
  const table = [
    START,
    "",
    "| | Ticket | | State | Blocked by |",
    "|---|---|---|---|---|",
    ...rows,
    "",
    `_${entries.filter((e) => !e.done).length} open, ${entries.filter((e) => e.done).length} done. Regenerate with \`node scripts/board.mjs --index\`._`,
    "",
    END,
  ].join("\n");

  let out;
  if (raw.includes(START) && raw.includes(END)) {
    out = raw.slice(0, raw.indexOf(START)) + table + raw.slice(raw.indexOf(END) + END.length);
  } else {
    // First run: place it directly after the file's opening paragraph, before the first section.
    const at = lines.findIndex((l, i) => i > 0 && /^## /.test(l));
    const head = at === -1 ? lines : lines.slice(0, at);
    const tail = at === -1 ? [] : lines.slice(at);
    out = [...head, table, "", ...tail].join("\n");
  }
  if (out === raw) console.log("Index already current.");
  else { writeFileSync(BOARD, out); console.log(`Index rewritten: ${entries.length} entries.`); }
  process.exit(0);
}

if (args.includes("--html")) {
  const out = buildHtml();
  const path = "tasks/board.html";
  const current = existsSync(path) ? readFileSync(path, "utf8") : null;
  if (current === out) console.log("tasks/board.html already current.");
  else { writeFileSync(path, out); console.log(`tasks/board.html written: ${entries.length} entries.`); }
  process.exit(0);
}

console.error("Usage: board.mjs --check [TICKET-ID] | --index | --html");
process.exit(2);
```
