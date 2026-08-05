# Wiring it to your stack

Six of the seven pull-request checks run on any repository the day you clone the starter. One of them
has to understand your code. This document is for whoever sets up a repository — it tells you exactly
what to wire, for Node, Python, Go, mobile, a platform you do not control, and a service with no screens.

## What is portable, and what is not

Four checks work on any repository in any language, unchanged, because they read git and the host API
and nothing else. `size.yml` runs `git diff --numstat`. `gates.yml` walks `git rev-list` and reads
`git show --name-status`. `spec.yml` asserts the spec file is an ancestor of every implementation
commit. `perimeter.yml` asks the host what branch protection it is actually enforcing. None of them
compiles anything, so none of them cares what you build.

Two more are stack-independent but need something switched on. `review.yml` reads a diff and calls a
model; it needs `ANTHROPIC_API_KEY` and fails loudly without it rather than passing. `scan.yml` reads
the host's own alert state rather than running a scanner in the job, so it needs Dependabot and code
scanning enabled on the repository, and it says so and fails if they are not.

That leaves `verify`. Everything that has to understand your code lives behind it.

| Check | What it reads | What you wire |
|---|---|---|
| `size` | `git diff --numstat` against the base | nothing |
| `gates` | commit-by-commit `git rev-list`, `git show` | nothing |
| `spec` | commit ancestry of `docs/specs/<ticket>.md` | nothing |
| `perimeter` | the host's branch-protection API | `PERIMETER_TOKEN` (fine-grained, `Administration: read`) |
| `scan` | the host's Dependabot and code-scanning alerts | those two features enabled |
| `review` | the diff, in a fresh session | `ANTHROPIC_API_KEY` |
| `verify` | one entry point: the `verify` script | six gates, plus lcov output |

The four portable checks are portable because they are indirect. They never ask "is this code correct",
only "does the history have the shape we said it does". That is also their limit: they cannot see one
thing about behaviour. All the behavioural evidence in this process arrives through `verify`, which is
why the rest of this document is about wiring it honestly rather than quickly. The checks themselves,
with their full source, live in [enforcement](06-enforcement.md).

## The verify entry point contract

`scripts/verify.mjs` holds a list of six gates and the reason each one exists: `format` (`format:check`),
`lint` (`lint`), `types` (`typecheck`), `tests` (`test`), `coverage` (`test:coverage`), and `build`
(`build`). The full file, including the reason attached to each gate, is in
[enforcement](06-enforcement.md). The contract around it has three parts.

**One name.** CI runs `bun run verify`. The pre-push hook runs `bun run verify`. A developer runs
`bun run verify`. There is exactly one definition of what "verified" means in this repository, and it is
a list you can read in one screen. When CI and the hook disagree about that definition, someone will
trust the wrong one.

**It fails on an unwired gate, it does not skip it.** If `package.json` has no `typecheck` script,
verify exits 1 and prints the missing script names with their reasons. This is the single most important
behaviour in the file. A repository that documents six gates and runs four reports green for the two it
never ran, and everyone downstream reads that green and believes it. Our pilot repository asserted branch
protection in its own context file; there was no remote and CI had run zero times. Nothing lied. Every
check that existed passed. Failing on absence is how you stop that from being a comfortable place to sit.

**Removing a gate is a decision, made visibly.** If a gate genuinely does not apply — and for Go, one
does not — you delete it from `GATES` in its own commit, with the reason in the commit message, reviewed
by a code owner. The cost of this design is real: it puts a hard stop in front of anyone setting up a
repository in a hurry, and the tempting way out is to point a script at `true`. That is why `gates.yml`
also greps added workflow lines for `continue-on-error: true`, `if: false` and a bare `|| true`.

## Close the hole that wiring opens

Wiring your stack means editing `scripts/verify.mjs` and `scripts/changed-line-coverage.mjs`. Those two
files decide which gates run and what coverage threshold applies.

`gates.yml`'s `is_gate_path` already names all three scripts by path, so an edit to either one inside an
implementation commit fails the gate-mixing check. `CODEOWNERS` does not. It protects the workflows,
`lefthook.yml`, `CLAUDE.md`, `.claude/`, and `docs/design/criteria/`, and stops there. So today an agent
can split the change into its own commit — satisfying `gates.yml` — and still merge a `GATES` deletion or
a `--min 80` to `--min 0` without a second pair of eyes.

Fix that first, in one commit, before you wire anything. Add one line to `CODEOWNERS`, whose full
contents are in [the repository files](07-repository.md):

```
/scripts/                  @devx/tech-leads
```

This is the shape of the work in this document. Wiring is not just adding commands; it is making sure
the thing you added cannot be quietly unadded.

## Node and TypeScript with bun

The stack the starter was written against, so the wiring is six lines in `package.json`:

```json
"format:check":  "prettier --check .",
"lint":          "eslint .",
"typecheck":     "tsc --noEmit",
"test":          "bun test",
"test:coverage": "bun test --coverage --coverage-reporter=lcov",
"build":         "tsc -p tsconfig.build.json"
```

`bun test --coverage --coverage-reporter=lcov` writes `coverage/lcov.info`, which is the path
`changed-line-coverage.mjs` defaults to. With vitest:
`vitest run --coverage --coverage.reporter=lcov --coverage.reportsDirectory=coverage`. With jest:
`jest --coverage --coverageReporters=lcov`. All three land in the same place.

The one thing that reliably breaks is a monorepo. The coverage script matches lcov `SF:` paths against
`git diff` paths, stripping only `process.cwd()` and a leading `./`:

```
  git diff says   apps/api/src/orders.ts   line 42
  lcov SF: says   src/orders.ts
                  ^ no match — the file is reported as "not present in coverage output",
                    every changed line counts as uncovered, and the gate fails at 0%
```

Two ways out. Either run coverage from the repository root so `SF:` paths are already repo-relative, or
prefix them after the fact:

```json
"test:coverage": "cd apps/api && bun test --coverage --coverage-reporter=lcov && sed -i.bak 's|^SF:|SF:apps/api/|' coverage/lcov.info && mkdir -p ../../coverage && mv coverage/lcov.info ../../coverage/lcov.info"
```

Check it before you trust it: `grep '^SF:' coverage/lcov.info | head -3` must print paths that
`git ls-files` would also print.

**Browser obligation.** For anything with screens, the acceptance criterion names a Playwright test and a
screenshot, and the screenshot is compared to the design frame by a person — the comparison is human, the
capture is not. Add `"test:e2e": "playwright test --reporter=line"` and run it as its own CI job against
the pull request's preview deployment. Two details. E2e specs do not count toward changed-line coverage,
because the `SKIPS` regex in `changed-line-coverage.mjs` excludes `e2e/`, `__tests__/`, `*.test.*` and
`*.spec.*` — a test file covering itself is not evidence. And the screenshot goes in the pull request's
Evidence column, not in a comment, because that table is what the reviewer reads.

Our pilot is the whole argument for this. The admin panel shipped 9 write hooks and 0 buttons, 0 forms,
0 submit handlers. The write side existed at every layer except the one a human touches, and the agent's
own build report explained why: it had chosen a render check that could only see reads. The agent builds
to the shape of the check. A weak gate does not give you the same product less verified; it gives you a
different, smaller product.

## Python

`verify.mjs` reads `package.json` and shells out with `bun run`. Keeping a `package.json` in a Python
repository looks odd and is the cheapest option: it is the gate manifest, not a dependency list.

```json
"format:check":  "uv run ruff format --check .",
"lint":          "uv run ruff check .",
"typecheck":     "uv run mypy src",
"test":          "uv run pytest -q",
"test:coverage": "uv run pytest -q --cov=src --cov-report=lcov:coverage/lcov.info",
"build":         "uv build"
```

The cost is that CI and every developer machine now needs bun installed for a Python project. The
alternative is porting the fifty-odd lines of `verify.mjs` to Python and having `verify.yml` call
`uv run python scripts/verify.py`. Both are defensible. Pick one and write down which, because a
repository where half the team runs a different entry point has no entry point.

coverage.py writes absolute paths into lcov unless you tell it otherwise, which defeats the path match
above. Set this in `pyproject.toml`:

```toml
[tool.coverage.run]
relative_files = true
source = ["src"]
```

Note that `pytest.ini` and `.coveragerc` are already in `gates.yml`'s protected set and `pyproject.toml`
is not. If your coverage config lives there, add `pyproject.toml` to `is_gate_path` in the same commit
you add `/scripts/` to `CODEOWNERS`. Otherwise `omit = ["src/payments/*"]` is a coverage-threshold change
that reads as ordinary configuration.

**Browser obligation.** Most Python services have no browser surface; see the last section. Where there
is one — Django templates, an admin, a Streamlit tool — use `pytest-playwright`:
`uv run pytest tests/e2e --screenshot=on --output=artifacts/e2e`, and attach the screenshot the same way.

## Go

Go is the case where a gate genuinely does not apply, and it is worth doing properly rather than pointing
`typecheck` at `go vet`.

```json
"format:check":  "test -z \"$(gofmt -l . | tee /dev/stderr)\"",
"lint":          "golangci-lint run ./...",
"test":          "go test ./... -covermode=atomic -coverprofile=coverage.out",
"test:coverage": "bun run test && mkdir -p coverage && gcov2lcov -infile=coverage.out -outfile=coverage/lcov.info",
"build":         "go build ./..."
```

There is no `typecheck`. The Go compiler is the type checker and `build` runs it, so a separate
`typecheck` script would either duplicate `go build` or be a lie. Delete the `types` entry from `GATES`
in `scripts/verify.mjs`, in its own commit, message:
`chore(gates): drop types gate — go build is the type check`. That is exactly the exit `verify.mjs`
documents, and using it is not a failure of the design.

`gcov2lcov` derives `SF:` paths from the coverage profile, which carries the full module path. Check and
strip:

```bash
grep '^SF:' coverage/lcov.info | head -3
sed -i.bak "s|^SF:$(go list -m)/|SF:|" coverage/lcov.info
```

`.go` is already in the coverage script's `COUNTS` regex, so nothing else changes.

**Browser obligation.** Usually none — a Go service is an API. If it serves HTML, keep Playwright in its
own directory with its own `package.json` and run it as a separate CI job. Do not put a Node toolchain in
the `verify` path of a Go binary, or your build gate starts failing for reasons that have nothing to do
with the build.

## Mobile

Two things change structurally, both from the platform rather than from us. There is no per-pull-request
preview URL, and store review sets the release cadence. That pushes Release Check into fewer, larger
releases, and it makes the rehearsed rollback a staged rollout percentage rather than a redeploy — see
[delivery](03-delivery.md).

Flutter is the easiest to wire because `flutter test --coverage` emits `coverage/lcov.info` natively:

```json
"format:check":  "dart format --output=none --set-exit-if-changed .",
"lint":          "dart analyze --fatal-infos",
"typecheck":     "dart analyze --fatal-infos",
"test":          "flutter test",
"test:coverage": "flutter test --coverage",
"build":         "flutter build apk --debug && flutter build ios --no-codesign"
```

Native iOS needs a conversion step:

```bash
xcodebuild test -scheme App -destination 'platform=iOS Simulator,name=iPhone 16' \
  -enableCodeCoverage YES -derivedDataPath build
xcrun llvm-cov export -format=lcov \
  -instr-profile "$(find build -name '*.profdata' | head -1)" \
  build/Build/Products/Debug-iphonesimulator/App.app/App > coverage/lcov.info
```

Android with JaCoCo has no lcov reporter at all. You either write the XML-to-lcov conversion yourself or
you do not have this gate. Say which, out loud, in `README.md`.

One edit is required whatever you choose. `.swift`, `.dart`, `.kts` and `.m` are **not** in the `COUNTS`
regex in `changed-line-coverage.mjs`, which today reads
`/\.(ts|tsx|js|jsx|mjs|cjs|py|go|rb|java|kt|cs|php)$/`. An unedited starter measures changed-line
coverage on a Swift or Dart repository as "no changed lines in files we measure" and exits 0. It passes,
permanently, having measured nothing. Add your extensions. And note `.kt` is there while `.kts` is not,
which is right — Gradle build scripts are not code a test should reach.

**Browser obligation.** It becomes a simulator obligation. The criterion names an automated UI test and
the screenshot it produced: XCUITest, Espresso, or Maestro
(`maestro test flows/checkout.yaml --format junit`, which writes screenshots per step). A human compares
that image to the design frame. Do not accept a screenshot taken by hand — it proves the screen existed
once on someone's laptop, not that it survives the next change.

## A platform we do not control

A Shopify theme or a forked Medusa admin puts part of the product where our checks cannot reach. That
makes the fixture rule matter more, not less: capture the platform's actual shapes once into
`docs/fixtures/` and build against files, so a broken build is a broken build and not a bad afternoon on
someone else's API. The fixtures directory and its README are in [templates](08-templates.md).

For a Shopify theme:

```json
"format:check":  "prettier --check --plugin=@shopify/prettier-plugin-liquid .",
"lint":          "shopify theme check --fail-level warning",
"typecheck":     "tsc --noEmit",
"test":          "vitest run",
"test:coverage": "vitest run --coverage --coverage.reporter=lcov --coverage.reportsDirectory=coverage",
"build":         "vite build && shopify theme check --fail-level warning"
```

`.liquid` is not in `COUNTS` and cannot be — there is no coverage instrumentation for Liquid. The
consequence is exact and you should state it in the pull request's "What this does not verify" section:
**changed-line coverage does not see template changes on this stack.** The way to shrink that blind spot
is to move logic out of `.liquid` into `assets/*.ts` modules that vitest can reach, and leave the
templates as markup. That is a design constraint imposed by a gate, which is the mechanism working in the
direction we want for once.

For a forked Medusa admin, the fork is the interesting part. Whole-repo coverage on a fork measures
upstream's tests, which you did not write and cannot fix; changed-line coverage measures your divergence,
which is the only code you own. Set `--base` on the coverage script to your fork point, keep the
divergence as a named patch set, and add a gate that fails when the fork drifts without an updated patch
list. `medusa build` is the build gate; integration tests run against `medusa develop` with committed
fixtures for the external calls.

**Browser obligation.** There is a preview surface, so use it. `shopify theme push --unpublished` returns
a preview URL; run Playwright against it in a separate job. For a hosted admin you cannot preview per
pull request, name a staging URL and a fixed test account in the spec, and accept that the evidence is
one step further from the merge commit than we would like.

## When there is no interface

For a pipeline, a worker, or an integration, the screenshot rule does not apply and nothing replaces it
by default. You have to name the substitute in the acceptance criteria, or the criterion is prose, and
prose disappears.

The substitute is a real call or a real query, with its output committed. Concretely: the criterion says
"`POST /v1/orders` with `docs/fixtures/order-create.json` returns 201 and the row in `orders` has
`status='pending'`", and the evidence is the test name plus the captured response under `docs/fixtures/`.
Judging the feature means running it against real data in dev and reading the output, not opening a
screen.

Two things get harder without a screen, and both need saying. First, an unbuilt path stays invisible for
longer. In the pilot, the missing admin buttons were noticed because a person looked at a screen; with no
screen there is no equivalent moment, so the end-to-end call through the real transport — not a unit test
of the handler function — is the only thing standing where the screenshot stood. Second, coverage carries
more weight than it can bear. Changed-line coverage proves a test executed the line; it does not prove
the assertion means anything. When the same model writes the code and the test, the assertion tends to be
derived from the function rather than from the requirement: one worked example reports 78% line coverage
at a 31% mutation score — vendor-authored and illustrative, but the mechanism is not in dispute. On a
no-interface ticket, add property-based or contract tests at the integration boundary, and have the
review agent read the assertions rather than the coverage number.

## The one line that decides whether the coverage gate exists

`verify.yml` does not fail when lcov is missing. It warns, prints "this gate does not exist", and exits
0. That is the one place in the starter where a gate skips rather than fails, and it exists so the first
pull request in a fresh repository is not blocked by a coverage file nobody has wired yet.

The cost is that a warning in a log is invisible after week one. So: the moment you finish wiring
`test:coverage`, change that `exit 0` to `exit 1` in its own commit. If your stack cannot emit lcov —
Android with JaCoCo, a Liquid theme, a repository that is mostly configuration — then delete the coverage
row from the "What is actually enforced" table in `README.md` and remove the `coverage` entry from
`GATES`, so the repository stops claiming a measurement it does not take.

Either of those is fine. Leaving the warning in place is the one option that is not, because it is the
pilot's failure in miniature: a check written down, never built, and the writing-down mistaken for having
it.
