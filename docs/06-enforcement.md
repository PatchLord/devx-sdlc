# Enforcement: every check, with its code

This document holds every automated check in the process — what each one enforces, its complete file,
how to run it on your machine, what it catches and what it cannot see. Read it when you are setting a
repository up, when a check has failed and you want to know whether it is right, or when you are about
to change one. Branch protection, secrets and the deploy pipeline live on the host and are covered in
[host and pipeline](09-host-and-pipeline.md).

## Reach: hooks are hints, required checks are gates

The pilot settled how we build checks. One frozen spec, one cold session, no process: 44 commits, 64
tests, 87% line coverage. Requirements backed by a config file, a hook or a test: 8 of 8 present.
Requirements written only as prose: 0 of 7. The admin panel had nine write hooks and zero buttons, zero
forms, zero submit handlers, because the gate that session chose for that app was a render check, and a
render check can only see reads. [Why this exists](01-why.md) tells that story in full.

The agent builds to the shape of the check. A weak gate does not give you the same product, less
verified. It gives you a different, smaller product. So a check is not paperwork attached to the work;
it is a specification of the work's shape, and the first question about one is not "is it strict?" but
"can the thing it constrains edit it?"

Everything in a repository is a file, and a file is inside reach. Branch protection is not a file. It is
state on the host, reachable only through an API that needs a token the working tree does not contain.

```
host (github.com) — no file in the repository can change any of this
 ┌────────────────────────────────────────────────────────────────┐
 │ branch protection on main     required checks:                 │
 │ required approvals >= 1         size gates spec verify review  │
 │ require_code_owner_reviews    strict: up to date with main     │
 │ dismiss_stale_reviews         required_linear_history          │
 │ no force push, no deletion    required_conversation_resolution │
 └────────────────────────────────────────────────────────────────┘
       ▲                                            │
       │ perimeter.yml asks the host                │ merge is refused
       │ "what are you actually enforcing?"         │ until every
       │ (PERIMETER_TOKEN lives on the host)        ▼ check has passed
 ┌────────────────────────────────────────────────────────────────┐
 │ repository — the agent's working tree                          │
 │                                                                │
 │ .github/workflows/*.yml   scripts/*.mjs   package.json         │
 │ tests   thresholds   lefthook.yml   CLAUDE.md   .claude/       │
 │ CODEOWNERS   docs/design/criteria/   any test file             │
 │                                                                │
 │ every one of these is a file an agent can edit                 │
 └────────────────────────────────────────────────────────────────┘
       │
       │ lefthook runs here, on your machine. `git commit --no-verify` skips it.
       ▼
hooks are hints. required checks are gates.
```

Two consequences we act on. A check that lives in the repository cannot protect itself: it is protected
by `CODEOWNERS` plus a required review, and `CODEOWNERS` holds only because the host enforces
`require_code_owner_reviews`. The chain ends on the host every time. And hooks hold nothing —
`lefthook.yml` says so in its first line. We keep them because a failure found in two seconds costs less
than the same failure found in four minutes of CI, not because they stop anything.

Every workflow below declares `runs-on: arm64`, a self-hosted runner label from the environment these
were written against. On GitHub-hosted runners change it to `ubuntu-latest` and delete the "Ensure gh
and jq are available" steps in `review.yml`, `perimeter.yml` and `scan.yml`; they exist only because a
minimal self-hosted runner ships neither tool.

## size — the ticket is sized to the review

**What it enforces.** Target 300 changed lines and 10 files, hard fail above 400 and 20, measured across
the whole pull request with generated files excluded.

Not tidiness. Faros AI's two-year telemetry study of 22,000 developers, published 2026, measures median
time-in-review up 441.5% and incidents per pull request up 242.7% at peak AI adoption against each
organisation's own low-adoption baseline. Monzo reports the same shape from the inside: average pull
request size up about 20%, and larger AI-assisted pull requests taking longer to review. Small pull
requests are the countermeasure, and they hold only if something refuses the large one.

`.github/workflows/size.yml`

```yaml
name: size

# A ticket is sized to the review, not to the clock.
# Target 300 lines / 10 files. Hard fail above 400 / 20.
# Above the ceiling the right answer is almost always to split the ticket.

on:
  pull_request:
    types: [opened, synchronize, reopened, labeled, unlabeled]

permissions:
  contents: read
  pull-requests: read

jobs:
  size:
    runs-on: arm64
    timeout-minutes: 10
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      # Self-hosted runners are minimal and do not ship GitHub-hosted's toolset.
      # Installed without root, so this works whether or not sudo is available.
      - name: Ensure gh and jq are available
        run: |
          set -euo pipefail
          mkdir -p "$HOME/.local/bin"
          echo "$HOME/.local/bin" >> "$GITHUB_PATH"
          export PATH="$HOME/.local/bin:$PATH"

          ARCH=$(uname -m)
          case "$ARCH" in
            aarch64|arm64) JQ=arm64; GH=arm64 ;;
            x86_64|amd64)  JQ=amd64; GH=amd64 ;;
            *) echo "::error::Unsupported architecture $ARCH"; exit 1 ;;
          esac

          if ! command -v jq >/dev/null; then
            echo "jq not present, installing jq-linux-$JQ"
            curl -fsSL "https://github.com/jqlang/jq/releases/download/jq-1.7.1/jq-linux-$JQ"               -o "$HOME/.local/bin/jq"
            chmod +x "$HOME/.local/bin/jq"
          fi

          if ! command -v gh >/dev/null; then
            echo "gh not present, installing gh_2.63.2_linux_$GH"
            curl -fsSL "https://github.com/cli/cli/releases/download/v2.63.2/gh_2.63.2_linux_$GH.tar.gz"               | tar -xz -C /tmp
            mv "/tmp/gh_2.63.2_linux_$GH/bin/gh" "$HOME/.local/bin/gh"
          fi

          jq --version && gh --version | head -1

      - name: Measure the diff
        id: measure
        run: |
          set -euo pipefail
          BASE="${{ github.event.pull_request.base.sha }}"
          HEAD="${{ github.event.pull_request.head.sha }}"

          # Generated and vendored files are not what a reviewer reads.
          # Keep this list short and justified — every entry here is review you are not doing.
          #
          # The `glob` magic is load-bearing, not decoration. Without it git uses wildmatch without
          # WM_PATHNAME, so `**` is just "any characters" and `**/bun.lockb` requires a slash before the
          # filename — meaning a lockfile at the repository root was NOT excluded. Since lockfiles live
          # at the root, every dependency change counted thousands of lines and failed this check for a
          # reason the comment above says is excluded. Found by scripts/break-it.mjs, which asserts the
          # exclusions on real paths; the same slip hid root-level *.snap, generated/ and migrations/.
          EXCLUDE=(
            ':(exclude,glob)**/*.lock'
            ':(exclude,glob)**/bun.lockb'
            ':(exclude,glob)**/package-lock.json'
            ':(exclude,glob)**/pnpm-lock.yaml'
            ':(exclude,glob)**/yarn.lock'
            ':(exclude,glob)**/*.snap'
            ':(exclude,glob)**/generated/**'
            ':(exclude,glob)**/*.generated.*'
            ':(exclude,glob)**/migrations/**/*.sql'
          )

          STAT=$(git diff --numstat "$BASE...$HEAD" -- . "${EXCLUDE[@]}")
          FILES=$(printf '%s\n' "$STAT" | grep -c . || true)
          LINES=$(printf '%s\n' "$STAT" | awk '{a+=$1; d+=$2} END {print (a+d)+0}')

          echo "files=$FILES" >> "$GITHUB_OUTPUT"
          echo "lines=$LINES" >> "$GITHUB_OUTPUT"
          echo "This pull request changes $LINES lines across $FILES files (excluding generated files)."

      - name: Enforce the ceiling
        env:
          FILES: ${{ steps.measure.outputs.files }}
          LINES: ${{ steps.measure.outputs.lines }}
          OVERRIDE: ${{ contains(github.event.pull_request.labels.*.name, 'size-override') }}
          AUTHOR: ${{ github.event.pull_request.user.login }}
          PR: ${{ github.event.pull_request.number }}
          REPO: ${{ github.repository }}
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          set -euo pipefail
          OVER=0
          [ "$LINES" -gt 400 ] && OVER=1
          [ "$FILES" -gt 20 ] && OVER=1

          if [ "$OVER" -eq 0 ]; then
            if [ "$LINES" -gt 300 ] || [ "$FILES" -gt 10 ]; then
              echo "::warning::$LINES lines / $FILES files is over the 300/10 target. Under the ceiling, so this passes — but the next one should be smaller."
            fi
            echo "Within the ceiling."
            exit 0
          fi

          if [ "$OVERRIDE" = "true" ]; then
            # A deny rule in .claude/settings.json is a hint: an agent can be told not to label its
            # own pull request, and nothing local stops it. So check who actually applied the label.
            # An override the author granted themselves is not an override, it is a bypass.
            LABELER=$(gh api "repos/$REPO/issues/$PR/events" --paginate \
              --jq '[.[] | select(.event == "labeled" and .label.name == "size-override") | .actor.login] | last // ""' \
              2>/dev/null || echo "")

            if [ -z "$LABELER" ]; then
              echo "::error::The size-override label is present but no labelling event was found, so we cannot tell who applied it."
              exit 1
            fi

            if [ "$LABELER" = "$AUTHOR" ]; then
              echo "::error::$AUTHOR applied the size-override label to their own pull request. That is a bypass, not an override."
              echo "Splitting the ticket is the usual answer. If it genuinely cannot be split, a tech lead applies the label."
              exit 1
            fi

            echo "::warning::Over the ceiling ($LINES lines / $FILES files), overridden by $LABELER."
            echo "The label is a record, not an excuse. The pull request must say why splitting was not possible."
            exit 0
          fi

          echo "::error::$LINES lines / $FILES files exceeds the ceiling of 400 lines / 20 files."
          echo ""
          echo "Split the ticket. A diff this size is read, not reviewed — and the class of defect this"
          echo "process exists to catch is the one that survives a skim."
          echo ""
          echo "If it genuinely cannot be split, a tech lead adds the 'size-override' label and the"
          echo "pull request explains why. That is deliberately a person's decision, not an agent's."
          exit 1
```

The override is deliberately two controls, not one. The deny list in
[.claude/settings.json](07-repository.md) refuses `gh pr edit --add-label`, `gh label` and
`gh api ...labels...` — but that file is enforced by the agent harness, so it stops the happy path and
nothing else. The workflow therefore reads the labelling event from the API and refuses an override the
author granted themselves. Belt and braces, because only the second one is out of reach.

**How to test it locally.** Reproduce the measurement:

```bash
BASE=$(git merge-base origin/main HEAD)
git diff --numstat "$BASE...HEAD" -- . \
  ':(exclude,glob)**/*.lock' ':(exclude,glob)**/bun.lockb' ':(exclude,glob)**/package-lock.json' \
  ':(exclude,glob)**/pnpm-lock.yaml' ':(exclude,glob)**/yarn.lock' ':(exclude,glob)**/*.snap' \
  ':(exclude,glob)**/generated/**' ':(exclude,glob)**/*.generated.*' ':(exclude,glob)**/migrations/**/*.sql' \
  | awk '{a+=$1; d+=$2} END {print NR" files, "(a+d)" lines"}'
```

**What it catches.** The Friday-afternoon 400-line pull request. The ticket that was described with an
"and". The refactor mixed into a feature.

**What it cannot catch.** It counts lines, so 400 lines of moved code reads the same as 400 lines of new
control flow, and 40 lines of subtle concurrency reads as small. It cannot see one ticket split into
three 399-line pull requests. The exclusion list is a hole by construction — anything under a directory
named `generated/` is invisible, and naming a directory is one tool call. Keep that list short, because
every entry is review you have decided not to do.

## gates — a change that weakens a check arrives in its own commit

**What it enforces.** Two things. No commit contains both a gate change and implementation. And no
commit adds the markers a bypass leaves behind: `continue-on-error: true`, `if: false`, a trailing
`|| true` in a workflow step, or a skipped test.

Weakening a check must stay allowed, or the process becomes something people route around. What is not
allowed is weakening it inside a commit whose subject says `feat(billing): add proration`. This check
does not prevent the weakening. It makes it legible — one commit, one diff, one line in `git log` —
where a code owner's review lands on it.

`.github/workflows/gates.yml`

```yaml
name: gates

# A change that weakens a check must arrive in its own commit, where it is visible.
# Mixed into an implementation commit it is invisible — which is exactly why it happens.
#
# Adding a new test for new code is implementation. Modifying or deleting an existing
# test is a gate change. That asymmetry is what makes a legal commit ordering exist.

on:
  pull_request:
    types: [opened, synchronize, reopened]

permissions:
  contents: read

jobs:
  gates:
    runs-on: arm64
    timeout-minutes: 10
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: No commit mixes a gate change with implementation
        run: |
          set -euo pipefail
          BASE="${{ github.event.pull_request.base.sha }}"
          HEAD="${{ github.event.pull_request.head.sha }}"

          is_gate_path() {
            case "$1" in
              .github/workflows/*|lefthook.yml|.lefthook/*|CODEOWNERS|CLAUDE.md|.claude/*) return 0 ;;
              docs/design/criteria/*)                                                     return 0 ;;
              *jest.config*|*vitest.config*|*bunfig.toml|*pytest.ini|*.coveragerc)         return 0 ;;
              scripts/verify.mjs|scripts/scan-secrets.mjs|scripts/changed-line-coverage.mjs) return 0 ;;
              scripts/board.mjs|scripts/break-it.mjs|scripts/red-on-base.mjs)                return 0 ;;
              *codecov.yml|*sonar-project.properties|*.eslintrc*|eslint.config.*)          return 0 ;;
              biome.json|biome.jsonc|.biome.json|ruff.toml|.ruff.toml)                    return 0 ;;
              *) return 1 ;;
            esac
          }

          # Anchored on filename and directory, NOT substring. The obvious version
          # (*test*|*spec*) classifies src/attestation.ts and src/specification.ts as tests, which
          # would let a source file be edited in a gate-only commit and skip the mixing check.
          is_test_path() {
            case "$1" in
              *.test.*|*.spec.*|*_test.*|*-test.*|*_spec.*|*-spec.*)              return 0 ;;
              */__tests__/*|*/__mocks__/*|*/tests/*|*/test/*|*/e2e/*|*/spec/*)    return 0 ;;
              tests/*|test/*|e2e/*|spec/*)                                        return 0 ;;
              *) return 1 ;;
            esac
          }

          FAILED=0
          for SHA in $(git rev-list --reverse --no-merges "$BASE..$HEAD"); do
            GATE_CHANGES=""
            IMPL_CHANGES=""

            while IFS=$'\t' read -r STATUS PATH_A _; do
              [ -z "${STATUS:-}" ] && continue

              if is_gate_path "$PATH_A"; then
                GATE_CHANGES="$GATE_CHANGES  $STATUS $PATH_A"$'\n'
              elif is_test_path "$PATH_A" && [ "$STATUS" != "A" ]; then
                # An existing test, modified or deleted — a gate change.
                GATE_CHANGES="$GATE_CHANGES  $STATUS $PATH_A"$'\n'
              else
                # Source code, or a newly added test for it.
                IMPL_CHANGES="$IMPL_CHANGES  $STATUS $PATH_A"$'\n'
              fi
            done < <(git show --name-status --format= --no-renames "$SHA")

            if [ -n "$GATE_CHANGES" ] && [ -n "$IMPL_CHANGES" ]; then
              FAILED=1
              echo "::error::Commit $(git log -1 --format='%h %s' "$SHA") mixes a gate change with implementation."
              echo "  gate:"; printf '%s' "$GATE_CHANGES" | sed 's/^/  /'
              echo "  implementation:"; printf '%s' "$IMPL_CHANGES" | sed 's/^/  /'
              echo ""
            elif [ -n "$GATE_CHANGES" ]; then
              echo "Commit $(git log -1 --format='%h' "$SHA") is a gate-only change — visible, as intended:"
              printf '%s' "$GATE_CHANGES"
            fi
          done

          if [ "$FAILED" -eq 1 ]; then
            echo "Split those commits. Weakening a check is allowed; hiding it inside a feature is not."
            exit 1
          fi
          echo "No commit mixes a gate change with implementation."

      - name: No check was suppressed
        run: |
          set -euo pipefail
          BASE="${{ github.event.pull_request.base.sha }}"
          HEAD="${{ github.event.pull_request.head.sha }}"
          FAILED=0

          # Hooks are hints — --no-verify walks straight past them and leaves a trace only here.
          # There is no reliable marker in a commit object, so we check what a bypass tends to leave:
          # skipped jobs, quieted tests, and deleted assertions.

          ADDED=$(git diff "$BASE...$HEAD" -- '.github/workflows/**' | grep '^+' || true)

          if printf '%s' "$ADDED" | grep -qE 'continue-on-error:[[:space:]]*true|if:[[:space:]]*false'; then
            echo "::error::A workflow gained continue-on-error or 'if: false'. That turns a gate into a decoration."
            printf '%s\n' "$ADDED" | grep -nE 'continue-on-error:[[:space:]]*true|if:[[:space:]]*false'
            FAILED=1
          fi

          # `|| true` is only dangerous when it swallows a whole command. Inside a command
          # substitution it is the normal idiom for stopping grep's exit 1 from tripping set -e,
          # and this very workflow uses it three times - a naive check fails its own commit.
          SWALLOWED=$(printf '%s\n' "$ADDED" | grep -E '\|\|[[:space:]]*true[[:space:]]*$' | grep -v '[$][(]' || true)
          if [ -n "$SWALLOWED" ]; then
            echo "::error::A workflow step ends in '|| true', which makes its command unable to fail."
            echo "If the command is allowed to fail, say so with continue-on-error and a comment giving"
            echo "the reason. If it is not, delete the '|| true'. If you only wanted grep's exit 1 to"
            echo "stop tripping set -e, move it inside a command substitution: X=\$(cmd || true)."
            printf '%s\n' "$SWALLOWED"
            FAILED=1
          fi

          # WORD BOUNDARIES, and they are not decoration. `xit(` is Jasmine's excluded test — and it is also
          # the last four characters of `process.exit(`, so without \b this fired on every Node CLI script in
          # the repository and called them skipped tests. It did exactly that on a real pull request, which is
          # the only reason it was found: break-it had no case with a process.exit in the diff.
          # Two files are excluded, for the same reason the `|| true` check above scopes itself: a check that
          # scans for a pattern fails the commit that IMPLEMENTS or TESTS that pattern. This file has to
          # contain `xit(` to look for it, and break-it.mjs has to contain it to prove the search works —
          # the word-boundary fix above was refused by its own check, on its own pull request.
          #
          # Narrow on purpose: both are gate paths under CODEOWNERS, so a skipped test smuggled into either
          # still needs an owner. Excluding the test directories would be the version that defeats the check.
          SKIPS=$(git diff "$BASE...$HEAD" -- . ':(exclude).github/workflows/gates.yml' ':(exclude)scripts/break-it.mjs' \
            | grep -E '^\+.*(\.skip\(|\.todo\(|\bxit\(|\bxdescribe\(|@pytest\.mark\.skip|\bt\.Skip\()' || true)
          if [ -n "$SKIPS" ]; then
            echo "::error::Tests were skipped rather than fixed:"
            printf '%s\n' "$SKIPS"
            echo "A skipped test reports green and proves nothing. Fix it or delete it in a gate-only commit and say why."
            FAILED=1
          fi

          exit "$FAILED"
```

### Why `STATUS != "A"` is the whole design

That one condition is what makes a legal commit ordering exist. Remove it and the rule is unsatisfiable
in the good case.

`git show --name-status --no-renames` prints a status letter per path: `A` added, `M` modified, `D`
deleted. The `--no-renames` is deliberate — a rename otherwise shows as a single `R` line that hides
which side actually changed, so we force it to appear as `D` on the old path plus `A` on the new one.
The classification then falls out:

| Path | Status | Classified as |
|---|---|---|
| `.github/workflows/verify.yml`, `lefthook.yml` | any | gate |
| `CODEOWNERS`, `CLAUDE.md`, `.claude/*` | any | gate |
| `docs/design/criteria/*`, `vitest.config.ts`, `.coveragerc` | any | gate |
| `scripts/verify.mjs`, `scripts/changed-line-coverage.mjs` | any | gate |
| `src/billing/proration.test.ts` | `A` | implementation |
| `src/billing/proration.test.ts` | `M` or `D` | **gate** |
| `src/billing/proration.ts` | any | implementation |

Adding a new test for new code is implementation. Modifying or deleting a test that already existed is a
gate change.

Consider what happens without the asymmetry. Every test file is a gate. An agent writes
`proration.ts` and `proration.test.ts` in one commit — the normal, correct shape of the work — and the
check fails it. The only legal shapes left are an implementation commit with no test in it, followed by
a test-only commit; or a test-only commit first, which fails `verify` in isolation because the code it
tests does not exist yet. You have made correct behaviour illegal. A rule that fires on correct
behaviour gets disabled inside a week, and then it protects nothing at all. The asymmetry is the price
of the rule being satisfiable, and satisfiable is a precondition for being obeyed.

The cost is exact and worth naming: a brand-new test carries status `A`, so a new test that asserts
nothing passes through as implementation and is structurally invisible here. That is the hole. It is
covered below under what this cannot catch, and it is not covered anywhere else.

### Why `is_test_path` is anchored, not a substring

The obvious implementation is `case "$1" in *test*|*spec*)`. It is wrong in the dangerous direction.

Substring matching classifies `src/attestation.ts`, `src/latest/index.ts` and `src/specification.ts` as
tests. That is not merely noisy — it is a bypass. A source file misclassified as a test can be modified
inside a commit that also touches a workflow, and the mixing check will see two gate changes rather than
a gate change plus implementation, and pass. The false positive on the test side becomes a false
negative on the enforcement side.

So the patterns are anchored on the filename separator or on a full directory segment: `*.test.*`,
`*_test.*`, `*-spec.*` and their siblings for filenames, `*/tests/*`, `*/e2e/*`, `*/__mocks__/*` for
directories, plus the same directory names at the repository root. Run those patterns over real paths
and `src/attestation.ts`, `src/latest/index.ts`, `src/spectrum.ts` and `docs/specs/PULSE-123.md` all
come back as implementation, which is what they are.

Two residual weaknesses, in the same breath, because anchoring trades one error for another.

It misses test conventions that use a prefix rather than a suffix. `src/test_billing.py` — pytest's
default `test_*.py` naming, sitting next to the module it tests — is classified as implementation.
`BillingTests.cs` is too. In a Python or .NET repository that does not put tests under a `tests/`
directory, the modify-a-test rule silently does not apply. If your repository is shaped that way, add
the pattern in a gate-only commit; the alternative is a rule you believe in that is not running.

And it over-matches on directory names. `src/test/fixtures/seed.json` and `src/e2e/helpers.ts` are a
fixture and a helper, not tests, but both classify as gate changes — so editing one alongside source
fails the commit. That is a false positive you pay in an extra commit, which is the direction we want
the error to point.

The suppression step has its own limits. It reads only `.github/workflows/**` for the first two
patterns, so a `|| true` added to `scripts/verify.mjs`, a Makefile or a `package.json` script is
invisible. The trailing-`|| true` regex is anchored at end of line and excludes lines containing `$(`,
which is what stops it firing on this repository's own `FILES=$(... | grep -c . || true)` idiom — that
line ends in `)`, so it never matched, and the `$(` guard is a second layer. The exclusion is also the
gap: `cmd || true && echo ok`, `cmd || echo skipped`, and a bare `set +e` all walk past. And the `.skip(`
grep reads the whole diff, so prose in a markdown file that mentions `.skip(` fails the check. That is
the price of grepping for a pattern instead of understanding intent, and it is paid in false positives
rather than missed tampering. We prefer that direction.

**How to test it locally.** Print what the check sees, commit by commit:

```bash
for SHA in $(git rev-list --reverse --no-merges origin/main..HEAD); do
  echo "== $(git log -1 --format='%h %s' "$SHA")"
  git show --name-status --format= --no-renames "$SHA" | sed 's/^/   /'
done
```

Then make it fail: in a scratch branch, edit an existing test and a source file in one commit and push.

**What it catches.** The deleted assertion inside a feature commit. The threshold lowered from 80 to 60
while "fixing the build". The `.skip(` added to quiet a flake. The job given `continue-on-error: true`.

**What it cannot catch.** A brand-new test that asserts nothing. That is oracle contamination — when the
same model writes the code and the test, the assertion gets derived from the function rather than the
requirement, and one worked example reports 78% line coverage at a 31% mutation score. Coverage cannot
see it either; only mutation testing or a person reading assertions can, and mutation testing is not in
the starter. It also cannot catch a *legal* gate-only commit that nobody reviews: `CODEOWNERS` protects
workflows and `.claude/` but not `src/**/*.test.ts`, so deleting a test in its own commit passes `gates`
and needs no second pair of eyes unless a human reads the commit list. And the first step reasons over
`git rev-list BASE..HEAD`, which means what we claim only when history is linear. That is why
`required_linear_history` is a precondition, not a preference.

## spec — the spec exists, and it came first

**What it enforces.** The branch name starts with a ticket id. `docs/specs/<TICKET>.md` exists at HEAD.
The branch's first commit is that spec file and nothing else. A later commit touching the spec warns.

The spec is the handoff, and the session that implements does not have the conversation that produced
it. A spec committed after the code is a description of what was built, and the approval that gated it
was approval of nothing. The spec's contents and template are in [templates](08-templates.md); how it
gets written is in [before the build](02-before-build.md).

`.github/workflows/spec.yml`

```yaml
name: spec

# The spec is the handoff. The agent that implements does not have the conversation that
# produced it — so anything not written down did not happen.
#
# This job proves the spec came FIRST. It cannot prove a person approved it: approval is a
# state on the host (a review on this pull request), not a field in a file an agent can write.
# See perimeter.yml for the half that checks the host is actually configured to require it.

on:
  pull_request:
    types: [opened, synchronize, reopened]

permissions:
  contents: read

jobs:
  spec:
    runs-on: arm64
    timeout-minutes: 10
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      # BRANCH comes through `env`, never interpolated into the script body. A branch name is
      # attacker-controlled and git permits ; $ ` ( ) | & " in one, so `X="${{ ...head.ref }}"` is a
      # command-injection hole — and on a persistent self-hosted runner that is remote code execution
      # rather than a spoiled build. The shas are hex and could not carry a payload, but they go through
      # env too so that no future edit has to reason about which of the three was safe.
      - name: The spec exists, and it came first
        id: spec
        env:
          BASE: ${{ github.event.pull_request.base.sha }}
          HEAD: ${{ github.event.pull_request.head.sha }}
          BRANCH: ${{ github.event.pull_request.head.ref }}
        run: |
          set -euo pipefail

          # ── the front half ────────────────────────────────────────────────────────────────────────
          # A `design/` or `process/` branch is work that exists BEFORE tickets do: the TDD, the frozen
          # contracts, a change to the process itself. Every other rule in this file assumes a ticket, and
          # the front half legitimately has none — `create-tickets` comes after `freeze-contracts`, so
          # demanding a ticket here is circular.
          #
          # This is a NAMED PATH, not an exemption, and the difference is the constraint that replaces the
          # one it drops. A front-half branch may touch only front-half paths. It cannot carry application
          # code — which is the thing an exemption would have let through, and the reason "skip spec when
          # there is no ticket id" was rejected: that phrasing makes every unnamed branch a free pass.
          #
          # It also announces itself, so a front-half branch is visible in the log rather than silently
          # different. A prefix that passes quietly is a prefix that becomes the way everything ships.
          case "$BRANCH" in
            design/*|process/*)
              echo "Front-half branch: $BRANCH"
              echo "This is work that precedes tickets — a TDD, frozen contracts, or the process itself."
              echo "The ticket rules below do not apply. In their place: it may touch ONLY front-half paths."
              echo ""
              STRAY=$(git diff --name-only "$BASE...$HEAD" \
                | grep -vE '^(docs/|\.claude/|\.github/|scripts/|tasks/|log/|CLAUDE\.md|CODEOWNERS|REVIEW\.md|README\.md|lefthook\.yml|package\.json|commitlint\.config\.js|\.gitignore|\.editorconfig|\.gitattributes)' \
                || true)
              if [ -n "$STRAY" ]; then
                echo "::error::A front-half branch is carrying files that are not front-half work:"
                printf '  %s\n' $STRAY
                echo ""
                echo "Application code needs a ticket, a spec, and criteria that resolve — which is what this"
                echo "prefix sets aside. Move those files to a ticketed branch. The prefix buys a different"
                echo "constraint, not a lighter one."
                exit 1
              fi
              echo "Only front-half paths touched. Nothing here needs a ticket."
              # An OUTPUT, not `exit 0`. Exiting zero ends this STEP and leaves the rest of the job to run —
              # so the front-half branch passed here and then failed the two ticket steps below, which is
              # exactly the shape of a check that looks satisfied and is not. The steps are gated on this.
              echo "front_half=true" >> "$GITHUB_OUTPUT"
              exit 0
              ;;
          esac

          TICKET=$(printf '%s' "$BRANCH" | grep -oE '^[A-Z][A-Z0-9]+-[0-9]+' || true)
          if [ -z "$TICKET" ]; then
            echo "::error::Branch '$BRANCH' does not start with a ticket id (e.g. PULSE-123-short-slug)."
            echo "If this is work that precedes tickets — a TDD, contracts, or the process itself — name it"
            echo "design/... or process/... instead. That path may touch only front-half files."
            echo "Rename it and push again:"
            echo "  git branch -m PULSE-123-\$(echo '$BRANCH' | tr -cd '[:alnum:]-' | cut -c1-30)"
            echo "  git push origin :$BRANCH && git push -u origin HEAD"
            echo "The ticket id is how spec.yml finds docs/specs/<TICKET>.md, so it is not cosmetic."
            exit 1
          fi
          echo "Ticket: $TICKET"

          SPEC="docs/specs/$TICKET.md"
          if ! git cat-file -e "$HEAD:$SPEC" 2>/dev/null; then
            echo "::error::$SPEC is missing. Run /spec $TICKET before implementing."
            exit 1
          fi

          FIRST=$(git rev-list --reverse --no-merges "$BASE..$HEAD" | head -1)
          if [ -z "$FIRST" ]; then
            echo "::error::No commits on this branch."
            exit 1
          fi

          FIRST_FILES=$(git show --name-only --format= --no-renames "$FIRST")
          if [ "$(printf '%s\n' "$FIRST_FILES" | grep -c .)" -ne 1 ] || [ "$FIRST_FILES" != "$SPEC" ]; then
            echo "::error::The branch's first commit must be the spec alone. It was:"
            git log -1 --format='  %h %s' "$FIRST"
            printf '%s\n' "$FIRST_FILES" | sed 's/^/    /'
            echo ""
            echo "A spec committed after the code is a description of what was built, not a plan for it,"
            echo "and the approval that gated it was approval of nothing."
            exit 1
          fi
          echo "The spec is the first commit: $(git log -1 --format='%h %s' "$FIRST")"

      - name: The ticket exists on the board
        if: steps.spec.outputs.front_half != 'true'
        env:
          BRANCH: ${{ github.event.pull_request.head.ref }}
        run: |
          set -euo pipefail
          TICKET=$(printf '%s' "$BRANCH" | grep -oE '^[A-Z][A-Z0-9]+-[0-9]+')
          BOARD=tasks/board.md

          # The board is the tracker. A ticket that exists only in a branch name is not a ticket — nobody
          # can see what it is for, what was already found, or what a previous session left alone.
          # Deliberately bash rather than scripts/board.mjs: this runs on every pull request, and a check
          # that needs a toolchain installed is a check that skips on the runner where it is missing.
          if [ ! -f "$BOARD" ]; then
            echo "::error::$BOARD is missing, so there is nowhere for a ticket to exist."
            exit 1
          fi
          if ! grep -qE "^# $TICKET( |$|\b)" "$BOARD"; then
            echo "::error::$TICKET has no entry in $BOARD."
            echo "Add one before opening this pull request. The board is the tracker, so an entry is what"
            echo "makes the ticket real: what it is for, what is already in place, and what was already"
            echo "found and verified. See the shape at the top of that file."
            exit 1
          fi
          echo "$TICKET is on the board: $(grep -E "^# $TICKET" "$BOARD" | head -1)"

          # A DONE entry with no Resolution throws away the more useful half of the record.
          awk -v tk="$TICKET" '
            $0 ~ "^# "tk"( |$)" { inside = 1; next }
            /^# [A-Z][A-Z0-9]+-[0-9]+/ { inside = 0 }
            inside && /^\*\*State\*\*/ && /DONE/ { done = 1 }
            inside && /^## +Resolution/ { res = 1 }
            END {
              if (done && !res) {
                print "::error::"tk" is marked DONE with no \"## Resolution\" section."
                print "Say what changed, what you deliberately left alone, and what is still open."
                print "A ticket closed with only a list of what shipped loses the half that helps the next person."
                exit 1
              }
            }' "$BOARD"

      - name: A spec revised mid-flight is visible
        if: steps.spec.outputs.front_half != 'true'
        env:
          BASE: ${{ github.event.pull_request.base.sha }}
          HEAD: ${{ github.event.pull_request.head.sha }}
          BRANCH: ${{ github.event.pull_request.head.ref }}
        run: |
          set -euo pipefail
          TICKET=$(printf '%s' "$BRANCH" | grep -oE '^[A-Z][A-Z0-9]+-[0-9]+')
          SPEC="docs/specs/$TICKET.md"

          # Revising a spec is legitimate — the exploration was wrong, or the work taught you something.
          # It is not legitimate to revise it quietly, because the approval was of the earlier text.
          LATER=$(git rev-list --reverse --no-merges "$BASE..$HEAD" | tail -n +2)
          TOUCHED=""
          for SHA in $LATER; do
            if git show --name-only --format= --no-renames "$SHA" | grep -qx "$SPEC"; then
              TOUCHED="$TOUCHED  $(git log -1 --format='%h %s' "$SHA")"$'\n'
            fi
          done

          if [ -n "$TOUCHED" ]; then
            echo "::warning::The spec changed after implementation began:"
            printf '%s' "$TOUCHED"
            echo "That is allowed. Say in the pull request what changed and why, and get the spec"
            echo "re-approved — the existing approval was of the earlier text."
          else
            echo "The spec was not revised after implementation began."
          fi
```

**How to test it locally.**

```bash
git rev-list --reverse --no-merges origin/main..HEAD | head -1 \
  | xargs -I{} git show --name-only --format= {}
# must print exactly one line: docs/specs/<TICKET>.md
```

**What it catches.** Work that started before anyone wrote down what it was. A branch named `fix-thing`.
The spec backfilled from the diff in commit nine.

**What it cannot catch.** Whether a person read the spec, approved it, or approved *this version* of it.
Approval is a state on the host — a review on the pull request — not a field in a file, and any field in
a file is a field an agent can write. `perimeter.yml` checks the host is configured to require the
review; nothing checks that the review was thoughtful. It cannot judge contents either: a one-line spec
passes. The revision step warns rather than fails because revision is legitimate, and the cost is exact
— a warning nobody reads is not a control. The real control for that case is `dismiss_stale_reviews` on
the host.

## verify — the stack gates, in one entry point

**What it enforces.** One command, `bun run verify`, runs format, lint, types, build, tests and coverage —
build. CI runs it and the pre-push hook runs it, so "verified" means the same thing in both places. If
the entry point is missing, or any of the six is unwired, it fails rather than skipping.

That failure mode is the design. A repository that documents six gates and runs four reports green for
the two it never ran, and everyone downstream believes it. The pilot's own context file claimed branch
protection; there was no remote and CI had run zero times. Wiring the entry point to a language that is
not Node is [stack wiring](10-stack-wiring.md).

`.github/workflows/verify.yml`

```yaml
name: verify

# The stack-specific gates: format, lint, types, tests, coverage, build.
# This starter does not know your stack, so it calls one conventional entry point.
# Wire `verify` in package.json (or the Makefile target) to whatever your project actually runs.
#
# It fails when that entry point is missing. That is deliberate: a repository that claims
# these gates and has not wired them is worse off than one that never claimed them, because
# everyone downstream reads green and believes it.

on:
  pull_request:
    types: [opened, synchronize, reopened]
  push:
    branches: [dev]

permissions:
  contents: read

jobs:
  verify:
    runs-on: arm64
    timeout-minutes: 25
    steps:
      - uses: actions/checkout@v4

      - uses: oven-sh/setup-bun@v2
        with:
          bun-version: latest

      - name: Install
        run: bun install --frozen-lockfile

      - name: The verify entry point exists
        run: |
          set -euo pipefail
          if ! node -e "process.exit(require('./package.json').scripts?.verify ? 0 : 1)" 2>/dev/null; then
            echo "::error::package.json has no 'verify' script."
            echo ""
            echo "Wire it to your stack, for example:"
            echo '  "verify": "bun run format:check && bun run lint && bun run typecheck && bun run test:coverage && bun run build"'
            echo ""
            echo "Failing rather than skipping is the point. See README.md."
            exit 1
          fi

      # The board is the tracker and board.html is generated from it. Regenerating in memory and
      # comparing makes staleness a fact rather than a matter of anyone's diligence — which is the only
      # reason it is safe to keep a second representation of the same state at all.
      - name: The board is well-formed and its view is current
        run: node scripts/board.mjs --check

      - name: Verify
        run: bun run verify

      - name: Coverage on changed lines
        if: github.event_name == 'pull_request'
        run: |
          set -euo pipefail
          # Measured on the whole pull request against main, not per commit — a test-only commit
          # and an implementation-only commit each fail in isolation, so per-commit has no legal ordering.
          if [ ! -f coverage/lcov.info ]; then
            echo "::warning::No coverage/lcov.info produced, so changed-line coverage was not measured."
            echo "Have your test step emit lcov to enable this check. Until then, this gate does not exist."
            exit 0
          fi
          git fetch --no-tags --depth=1 origin "${{ github.event.pull_request.base.ref }}"
          bun scripts/changed-line-coverage.mjs \
            --lcov coverage/lcov.info \
            --base "origin/${{ github.event.pull_request.base.ref }}" \
            --min 80
```

`scripts/verify.mjs`

```javascript
#!/usr/bin/env bun
// The stack-specific gates, in one entry point, so CI and the pre-push hook agree on what
// "verified" means.
//
// It fails on any gate that is not wired. Not skips. A repository that documents six gates and
// runs four reports green for the two it never ran, and everyone downstream believes it.
// If you genuinely do not want one, delete it from GATES here — in its own commit, with a reason,
// reviewed by a code owner. That is a decision, and this makes it look like one.

import { execSync } from "node:child_process";
import { readFileSync } from "node:fs";

const GATES = [
  { name: "format", script: "format:check", why: "Formatting differences make a diff unreadable, which is the same as unreviewed." },
  { name: "lint", script: "lint", why: "Catches the class of mistake nobody should spend review attention on." },
  { name: "types", script: "typecheck", why: "The cheapest check there is, and the one AI-written code most often fails at the seams." },
  // build BEFORE tests, deliberately. In a monorepo where a workspace package is consumed as compiled
  // dist, the tests import the previous build unless something rebuilt it first — and then they pass for
  // the wrong reason. Nothing here short-circuits, so the order costs nothing and buys that.
  { name: "build", script: "build", why: "In a monorepo where a workspace package is consumed as compiled dist, it must be rebuilt before the tests import it — otherwise the tests pass against the previous build. And code that does not build has not been verified, whatever the tests said." },
  { name: "tests", script: "test", why: "The evidence every acceptance criterion points at." },
  { name: "coverage", script: "test:coverage", why: "Must emit coverage/lcov.info — changed-line coverage is measured from it." },
];

const scripts = JSON.parse(readFileSync("package.json", "utf8")).scripts ?? {};
const missing = GATES.filter((g) => !scripts[g.script]);

if (missing.length) {
  console.error("Not every gate is wired. Add these to package.json:\n");
  for (const g of missing) console.error(`  "${g.script}": "..."   — ${g.why}`);
  console.error(
    "\nThis fails rather than passing what it did not run. Wire them to your stack, or remove\n" +
      "the ones that do not apply from GATES in scripts/verify.mjs and say why in the commit.",
  );
  process.exit(1);
}

let failed = 0;
for (const g of GATES) {
  process.stdout.write(`\n── ${g.name} ──────────────────────────────────────\n`);
  try {
    execSync(`bun run ${g.script}`, { stdio: "inherit" });
  } catch {
    console.error(`\n${g.name} failed.`);
    failed++;
  }
}

if (failed) {
  console.error(
    `\n${failed} gate(s) failed.\n\n` +
      "Fix the cause. Making the check quieter — deleting the test, lowering the threshold,\n" +
      "adding a skip — is a gate change: its own commit, reviewed by a code owner, with a reason.",
  );
  process.exit(1);
}
console.log("\nAll gates pass.");
```

Coverage is measured on changed lines, not the whole repository. Whole-repo coverage is a number you
inherit — a 78% suite at a 31% mutation score passes it, and 200 untested new lines barely move it in a
large repository. Changed-line coverage is a number this pull request earned. The threshold is 80%,
passed as `--min 80` from `verify.yml`.

`scripts/changed-line-coverage.mjs`

```javascript
#!/usr/bin/env bun
// Coverage on the lines this pull request changed, not on the repository as a whole.
//
// Whole-repo coverage is a number you inherit; changed-line coverage is a number you earned.
// Measured across the whole pull request against the base branch — per commit there is no legal
// ordering, because a test-only commit and an implementation-only commit each fail in isolation.

import { execFileSync } from "node:child_process";
import { readFileSync } from "node:fs";

const arg = (name, fallback) => {
  const i = process.argv.indexOf(`--${name}`);
  return i === -1 ? fallback : process.argv[i + 1];
};

const lcovPath = arg("lcov", "coverage/lcov.info");
const base = arg("base", "origin/main");
const min = Number(arg("min", "80"));

// Only code we would expect a test to reach. Tests, config and generated files are excluded —
// counting them inflates the number without adding a single assertion.
const COUNTS = /\.(ts|tsx|js|jsx|mjs|cjs|py|go|rb|java|kt|cs|php)$/;
const SKIPS = /(^|\/)(node_modules|dist|build|coverage|generated)\/|\.(test|spec|stories|d)\.|(^|\/)(__tests__|__mocks__|e2e)\//;

const git = (...a) => execFileSync("git", a, { encoding: "utf8" });

// Which lines did we add or change?
const changed = new Map(); // file -> Set<lineNo>
let file = null;
for (const line of git("diff", "--unified=0", `${base}...HEAD`).split("\n")) {
  const head = line.match(/^\+\+\+ b\/(.+)$/);
  if (head) {
    file = head[1];
    continue;
  }
  const hunk = line.match(/^@@ -\S+ \+(\d+)(?:,(\d+))? @@/);
  if (hunk && file && COUNTS.test(file) && !SKIPS.test(file)) {
    const start = Number(hunk[1]);
    const count = hunk[2] === undefined ? 1 : Number(hunk[2]);
    if (!changed.has(file)) changed.set(file, new Set());
    for (let n = start; n < start + count; n++) changed.get(file).add(n);
  }
}

if (changed.size === 0) {
  console.log("No changed lines in files we measure. Nothing to check.");
  process.exit(0);
}

// Which of those did a test execute?
const hits = new Map(); // file -> Map<lineNo, count>
let current = null;
for (const line of readFileSync(lcovPath, "utf8").split("\n")) {
  if (line.startsWith("SF:")) {
    current = line.slice(3).replace(`${process.cwd()}/`, "").replace(/^\.\//, "");
    if (!hits.has(current)) hits.set(current, new Map());
  } else if (line.startsWith("DA:") && current) {
    const [n, c] = line.slice(3).split(",").map(Number);
    hits.get(current).set(n, Math.max(hits.get(current).get(n) ?? 0, c));
  }
}

let total = 0;
let covered = 0;
const gaps = [];

for (const [f, lines] of changed) {
  const fileHits = hits.get(f);
  if (!fileHits) {
    // Instrumented at all? If the file is absent from lcov, no test loaded it.
    total += lines.size;
    gaps.push(`  ${f} — not present in coverage output; no test loads this file (${lines.size} changed lines)`);
    continue;
  }
  const uncovered = [];
  for (const n of [...lines].sort((a, b) => a - b)) {
    if (!fileHits.has(n)) continue; // not an executable line — a comment, a blank, a type
    total++;
    if (fileHits.get(n) > 0) covered++;
    else uncovered.push(n);
  }
  if (uncovered.length) gaps.push(`  ${f}:${uncovered.join(",")}`);
}

if (total === 0) {
  console.log("No executable changed lines. Nothing to check.");
  process.exit(0);
}

const pct = (covered / total) * 100;
console.log(`Changed-line coverage: ${covered}/${total} = ${pct.toFixed(1)}% (minimum ${min}%)`);

if (gaps.length) {
  console.log("\nChanged lines no test reached:");
  for (const g of gaps) console.log(g);
}

if (pct < min) {
  console.log(
    `\n::error::Changed-line coverage ${pct.toFixed(1)}% is under ${min}%.\n` +
      "Add tests for the lines above. Lowering this threshold is a gate change: its own commit, " +
      "reviewed by a tech lead, with a reason.",
  );
  process.exit(1);
}
```

**How to test it locally.**

```bash
bun run verify                       # fails until all six scripts exist in package.json
bun scripts/changed-line-coverage.mjs --lcov coverage/lcov.info --base origin/main --min 80
```

**What it catches.** Unformatted, unlinted, untyped, unbuilt code. New lines no test reaches. A
repository claiming gates it never wired — `verify.mjs` names the missing script and says why it exists.

**What it cannot catch.** Whether a test asserts anything. A test that imports a function, calls it and
asserts nothing scores 100% changed-line coverage. The honest missing gate is mutation testing, and it
is not in the starter. Two smaller limits. When a changed file is absent from `lcov.info` the script
counts every changed line against you, comments and blanks included, because it has no instrumentation
data to tell them apart — the verdict is right, the percentage is pessimistic. And `verify.yml` warns
and exits 0 when `coverage/lcov.info` does not exist. That is the one place we chose warn-and-pass, and
the cost is exact: a repository whose test step emits no lcov shows `verify` green with changed-line
coverage never measured.

## criteria — every criterion names evidence that exists

**What it enforces.** That every row of a criteria table — in the pull request body, and in the spec the
branch was built from — carries an evidence cell that resolves to something a person or a script can go
and look at. Three forms resolve: a path to a file that exists in the repository, a test title a test
file actually contains, or a URL. Prose fails. An empty cell fails. And so do the words that stand in
for proof — verified, done, tested, confirmed, yes, n/a, ✓ — **including when they are wrapped in
backticks or quotes**, which is the form that defeated the first version of the resolver entirely.

"Green checks are not evidence" is the oldest rule in this standard, and until now it had no mechanical
form. The criteria table was read by people, so a cell saying `verified` passed. A claim in place of an
artefact is worse than a blank cell: the blank cell is visibly missing, and the claim reads as
diligence.

Finding 47 in [`research/findings.md`](../research/findings.md) is the case that made this a check
rather than a preference. `promote.yml` once required two cells to be blank with an AND, where three of
this standard's own documents said OR. So `| Rollback tested | verified | |` was accepted — the empty
row was refused and the confident one merged through a production gate. The row that looked filled in
was the one nothing had checked.

Two design consequences follow directly from that finding, and both are the same shape.

*It resolves every row and never stops at the first failure.* Finding 47's bug was a condition that
stopped looking once part of a row was filled in, and reported on the whole. A resolver that returned on
the first bad cell would also make a five-row table take five pushes to fix.

*It refuses to pick one table when several qualify.* Selection by first match was the same defect in a
second place: a `## Scope` table headed `| Item | Check |` matches the criterion and evidence column
patterns by luck, so it shadowed the real table under a literal `## Acceptance criteria` heading, and
the gate exited 0 with two failing criteria unread. Precedence is now by strength of signal — tables
inside an acceptance-criteria section first, then tables whose header names both columns — and **every**
table in the winning tier is resolved and its rows concatenated. The cost is that an unrelated table
inside a criteria section can now refuse the document. That is the direction this fails on purpose: a
false refusal is a question for a person, a false pass is a production gate agreeing with itself.

The claim words are refused before any text search, and the order is load-bearing. Words like "verified"
and "done" appear inside real test files. The first version tested the claim list against a cell that
still carried its wrappers, so `` `verified` `` — the way anybody writing markdown types a word they
mean literally — never matched, execution fell through to the test-file search, and a fixture containing
`it("email is verified after signup", ...)` made the cell resolve. The gate then reported evidence for a
row that named none. Backticks, quotes, curly quotes, bold, italic and brackets are stripped as matched
pairs around the whole cell, repeatedly, and every one of them has a regression case in the resolver's
self-test.

`.github/workflows/criteria.yml`

```yaml
name: criteria

# Does every acceptance criterion name evidence that exists?
#
# "Green checks are not evidence" is the oldest rule here and until now it had no mechanical form. The criteria
# table was read by people, so a cell saying `verified` passed — and a claim in place of an artefact is worse
# than a blank cell, because a blank cell is visibly missing and a claim looks like an answer.
#
# This resolves every row of the table. A cell passes when it names something checkable: a path that exists, a
# test title a test file actually contains, or a URL. It fails on prose, on an empty cell, and on the words
# that stand in for proof — verified, done, tested, confirmed, yes, n/a, ✓ — including when they are wrapped in
# backticks or quotes, which defeated the first version of this check completely.
#
# It resolves EVERY row and never stops at the first failure. That is not a nicety: `promote.yml` once required
# two cells to be blank with an AND where three documents said OR, so `| Rollback tested | verified | |` passed
# a production gate. A check that reads part of its input and reports on all of it is the defect class this
# repository has hit most often. Same reason the resolver refuses to PICK one table when several qualify.
#
# ADVISORY at first, and honest about why: it is new, and its false-positive rate on real specs is unknown. A
# check promoted to required before anyone knows how often it is wrong is how a team learns to add
# `size-override`-shaped escapes. Promote it once it has run on real work — same rule as `review`.
#
# WHAT THIS CANNOT DO. It cannot tell whether the test a criterion names actually PROVES that criterion; it
# checks that the artefact exists, not that it is honest. A test called "checkout works" that asserts `true`
# satisfies this check completely, and `red-on-base` plus mutation testing are what push back on that. It also
# cannot see evidence that lives only in somebody's head or in a Slack thread, which is the point.

on:
  pull_request:
    types: [opened, synchronize, reopened, edited]

permissions:
  contents: read

jobs:
  criteria:
    runs-on: arm64
    timeout-minutes: 10
    steps:
      - uses: actions/checkout@v4

      - uses: oven-sh/setup-bun@v2
        with:
          bun-version: latest

      # The resolver's own tests, here rather than only on a laptop. If it cannot tell a claim from an
      # artefact, a green run on this workflow means nothing at all.
      - name: The resolver still works
        run: node scripts/lib/criteria.mjs --self-test

      # The body goes through the environment, never through shell interpolation. `spec.yml` shipped
      # `${{ github.event.pull_request.head.ref }}` inline once, which is a command injection with a branch
      # name for a payload — a pull request body is a far larger and more attacker-controlled string.
      - name: Every criterion on the pull request names evidence that exists
        env:
          PR_BODY: ${{ github.event.pull_request.body }}
          BRANCH: ${{ github.event.pull_request.head.ref }}
        run: |
          set -euo pipefail
          printf '%s' "${PR_BODY:-}" > .criteria-pr-body.md

          FAILED=0

          echo "── the pull request body ────────────────────────────────────────"
          node scripts/lib/criteria.mjs .criteria-pr-body.md || FAILED=1

          # The spec's table is a different artefact from the pull request's, and it is the one that was agreed
          # BEFORE the work. A branch whose spec criteria never resolved should not have reached a pull request
          # at all — scripts/next.mjs refuses to enter implementation in that state — so a failure here is
          # evidence that something bypassed the loop, which is worth knowing on its own.
          TICKET=$(printf '%s' "$BRANCH" | grep -oE '^[A-Z][A-Z0-9]+-[0-9]+' || true)
          if [ -n "$TICKET" ] && [ -f "docs/specs/$TICKET.md" ]; then
            echo
            echo "── docs/specs/$TICKET.md ────────────────────────────────────────"
            node scripts/lib/criteria.mjs "docs/specs/$TICKET.md" || FAILED=1
          fi

          rm -f .criteria-pr-body.md
          if [ "$FAILED" -ne 0 ]; then
            echo
            echo "::error::A criterion names no evidence that can be checked."
            echo "Name the test, the file, the screenshot or the run. If a criterion genuinely cannot be"
            echo "proven, that is a question for a person BEFORE it is code — say so under 'What this does"
            echo "not verify' and take the row out of the criteria table, rather than filling the cell with"
            echo "a word that looks like proof."
            exit 1
          fi
```

The resolver itself is `scripts/lib/criteria.mjs`, a library rather than a gate: it decides and reports
and refuses nothing on its own. It becomes tier 1 when a required check calls it, and tier 1
harness-only when a hook does — the same file is what lets a session refuse to enter implementation
while the spec's criteria do not resolve, which is the third bound in [orientation](20-orientation.md).
Its `--self-test` runs against fixtures on disk rather than strings, because half of what it does is ask
the filesystem a question, and it runs in this workflow rather than only on somebody's laptop. If the
resolver cannot tell a claim from an artefact, a green run here means nothing at all.

**It is advisory at first, and classified that way in `perimeter.yml`.** The honest reason is that its
false-positive rate on real specs is unknown. Nobody has yet run it across a body of specs written
before it existed, and a check promoted to required before anyone knows how often it is wrong is exactly
how a team learns to add `size-override`-shaped escapes — after which the escape is the process and the
check is decoration. It is promoted the same way `review` is: once it has produced findings on real
work, and its refusal rate is a number somebody can quote.

**The failure output names its own teacher.** It prints `docs/design/criteria/_template.md` for five
worked examples and the `acceptance-criteria` skill for the rules in full. That belongs in the error
rather than only in the skill, because a failing check is the one moment the reader is guaranteed to be
looking. A rule that lives only where a session may or may not load it is prose — [tier
3](08-templates.md), which loses to context pressure. The same sentence attached to a red X gets read.

**How to test it locally.**

```bash
node scripts/lib/criteria.mjs --self-test            # the resolver, against fixtures on disk
node scripts/lib/criteria.mjs docs/specs/PULSE-123.md

gh pr view --json body --jq .body > .criteria-pr-body.md
node scripts/lib/criteria.mjs .criteria-pr-body.md ; rm -f .criteria-pr-body.md
```

Then make it fail on purpose. Put `| Rollback tested | verified | |` in a table under an
`## Acceptance criteria` heading and watch the row come back as a claim rather than evidence. Wrap the
word in backticks and watch it come back the same way — that is the regression that matters. Add a
`## Scope` table above it headed `| Item | Check |` and confirm the criteria table is still read.

**What it catches.** The cell that says `verified`, `done` or `n/a` where an artefact belongs, quoted or
not. The empty evidence cell. The criterion whose evidence is a sentence about how it was checked. A
named path that does not exist. A criteria table that is a bulleted list, which names no artefact and
cannot be resolved at all. And a spec whose criteria never resolved, which is evidence the loop was
bypassed on the way to this pull request.

**What it cannot catch.** It checks that the artefact exists, not that it is honest. A test named
"checkout works" that asserts `true` satisfies it completely, and so does
`| Totals are correct | README.md |`, because the file is there. That judgement is a person's, which is
why the review agent's prompt is pointed at exactly this column, and `red-on-base` is what asks whether
the named test would have failed before the change. Mutation testing is the honest missing gate here as
well, and it is not in the starter. Three smaller limits, all stated because they are easy to miss: it
does not run the test it finds or fetch the URL it accepts, so a 404 passes; it searches test files by
literal text, so a title assembled at runtime reads as prose, which is a false refusal rather than a
false pass; and it skips fenced code blocks, so a table inside one is invisible — safe only because a
missing table is a refusal and not a pass.

## review — a fresh session reads the diff

**What it enforces.** That a session which did not plan the work and did not write it reads the pull
request, in its own job, with read-only tools, and posts one comment. And that the job fails rather than
skips when `ANTHROPIC_API_KEY` is absent.

Its findings are input, not a verdict. Across 19,450 pull requests measured in 2026, pull requests
reviewed only by code-review agents merged at 45.20% against 68.37% for human-only review, and 12 of 13
agents averaged below a 60% signal ratio. It is a required check because it should be hard to skip, not
because it is authoritative; `required_conversation_resolution` on the host is what turns "input" into
"every finding gets a written disposition". The agent's own instructions live in
[.claude/agents/review.md](07-repository.md), and its place in the loop is [the build
loop](04-build-loop.md).

`.github/workflows/review.yml`

```yaml
name: review

# A fresh session reviews the ticket. It did not plan the work and did not write it — that is the
# whole reason it is worth running, and it is why this is a separate job rather than something the
# implementing session does to itself.
#
# Its findings are input, not a verdict. Dismiss the wrong ones in writing on the pull request.
# It is a check because it should be hard to skip, not because it is authoritative.

on:
  pull_request:
    types: [opened, synchronize, reopened]

permissions:
  contents: read
  pull-requests: write

jobs:
  review:
    runs-on: arm64
    timeout-minutes: 20
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      # Self-hosted runners are minimal and do not ship GitHub-hosted's toolset.
      # Installed without root, so this works whether or not sudo is available.
      - name: Ensure gh and jq are available
        run: |
          set -euo pipefail
          mkdir -p "$HOME/.local/bin"
          echo "$HOME/.local/bin" >> "$GITHUB_PATH"
          export PATH="$HOME/.local/bin:$PATH"

          ARCH=$(uname -m)
          case "$ARCH" in
            aarch64|arm64) JQ=arm64; GH=arm64 ;;
            x86_64|amd64)  JQ=amd64; GH=amd64 ;;
            *) echo "::error::Unsupported architecture $ARCH"; exit 1 ;;
          esac

          if ! command -v jq >/dev/null; then
            echo "jq not present, installing jq-linux-$JQ"
            curl -fsSL "https://github.com/jqlang/jq/releases/download/jq-1.7.1/jq-linux-$JQ"               -o "$HOME/.local/bin/jq"
            chmod +x "$HOME/.local/bin/jq"
          fi

          if ! command -v gh >/dev/null; then
            echo "gh not present, installing gh_2.63.2_linux_$GH"
            curl -fsSL "https://github.com/cli/cli/releases/download/v2.63.2/gh_2.63.2_linux_$GH.tar.gz"               | tar -xz -C /tmp
            mv "/tmp/gh_2.63.2_linux_$GH/bin/gh" "$HOME/.local/bin/gh"
          fi

          jq --version && gh --version | head -1

      - name: The reviewer is configured
        env:
          KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          set -euo pipefail
          if [ -z "${KEY:-}" ]; then
            echo "::error::ANTHROPIC_API_KEY is not set, so no review ran."
            echo "This job fails rather than skips. A review job that quietly does nothing is the"
            echo "worst of the options — the pull request shows a green check for work nobody read."
            echo "Either add the secret, or delete this job and remove 'review' from the required"
            echo "checks in perimeter.yml so the repository stops claiming a review it does not do."
            exit 1
          fi

      - uses: anthropics/claude-code-action@v1
        with:
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
          prompt: |
            Review this pull request as the `review` agent defined in .claude/agents/review.md.
            Follow that file exactly.

            Read REVIEW.md for the order of attention, the grading scale and what not to review, and
            docs/production-ready.md for the standard itself. Both are owned by the team and change
            without editing any agent. If REVIEW.md is absent, say so in your report — a repository
            with no written criteria is being reviewed against whatever you happen to think.

            Also read .claude/skills/build-loop/SKILL.md for what the wrap step owes, and
            docs/specs/ for the spec this branch was built from.

            Grade every finding **Important**, **Nit** or **Pre-existing**. Ungraded findings mean a
            human reads all of them and therefore reads none properly. Pre-existing never blocks: a
            pull request that touched a file is not responsible for everything in it.

            You cannot write or edit anything. Post one review comment.

            Order your findings so the gate surface comes first: any existing test modified or
            deleted, threshold lowered, assertion loosened, or CI job removed or made
            non-blocking. Those are the class of change no automated check in this repository
            can catch, because the deception is of the checks themselves.

            Then: the criteria table — does each row's evidence actually prove the criterion, or
            does it restate it. Then correctness, then what is missing.

            If you find nothing, say so plainly in one line. Do not manufacture findings.
          claude_args: --allowed-tools "Read,Grep,Glob,Bash(git *),Bash(gh pr *)"
```

The ordering rule in that prompt is the point of the job. Gate-surface findings come first because the
gate surface is the one thing the gates cannot inspect — a check cannot notice that it was the check
which got weakened.

**How to test it locally.** You cannot run the action locally, so test the halves separately. For the
failure path, clear the secret in a scratch repository and confirm the job goes red rather than
green-with-nothing. For the review itself, from a checkout of the branch:

```bash
claude -p "Review this pull request as the review agent defined in .claude/agents/review.md. \
Order gate-surface findings first." --allowedTools "Read,Grep,Glob,Bash(git *),Bash(gh pr *)"
```

**What it catches.** The criteria row whose evidence restates the criterion instead of proving it. The
missing error path. The assertion that cannot fail.

**What it cannot catch.** It cannot run the application, so the pilot's failure — nine write hooks, zero
buttons — is visible to it only if the criteria table names a button and it notices the absence. It must
not outvote a person: a 60% signal ratio means two in five findings are noise, which is why dismissal in
writing is part of the loop, and why *how often findings are dismissed* is one of the six numbers in
[measurement](11-measurement.md). Nothing automated measures that number; you count it from the pull
requests.

## perimeter — the one check that checks the checks

**What it enforces.** That the host is configured the way this repository documents. It asks the GitHub
API what protection on `main` actually says and compares it to expectations written literally in this
file.

Hardcoded, and we will not reverse that. We considered reading them from a config file and rejected it:
a config file an agent can edit is not an expectation, it is a suggestion. `CODEOWNERS` protects this
file, so changing what we claim to enforce requires a code owner's review of that exact diff.

It needs `PERIMETER_TOKEN`, a fine-grained token with `Administration: read`; the default `GITHUB_TOKEN`
cannot read branch protection. Missing secret fails the job, because a perimeter check that skips when
unconfigured is the failure it exists to catch.

`.github/workflows/perimeter.yml`

```yaml
name: perimeter

# The one check that checks the checks.
#
# NOTE, and it is a real limitation: this reads protection for `dev` only. The process promotes
# dev -> uat -> prod and all three need protecting — uat and prod more than dev, since a promotion
# straight into prod is the change with the least review and the most consequence. Checking one
# branch and reporting on "the perimeter" overstates what has been verified. The fuller version
# loops all three and is recorded as owed; `scripts/setup-check.mjs` does check all three, so the
# gap is covered at setup time and not continuously.
#
# Everything else in this directory runs inside the repository, where an agent can reach it.
# Branch protection lives on the host, where it cannot. So this job asks the host what it is
# actually enforcing and compares that to what we say we enforce.
#
# The expected values are written HERE, in a file CODEOWNERS protects — not read from a config
# file, because a config file an agent can edit is not an expectation, it is a suggestion.
#
# Requires PERIMETER_TOKEN: a fine-grained token with Administration: read on this repository.
# GITHUB_TOKEN cannot read branch protection. If that secret is missing this job FAILS —
# a perimeter check that skips when unconfigured is the exact failure it exists to catch.

on:
  schedule:
    - cron: "0 7 * * 1" # Monday morning, so a weekend change is found before the week's work lands on it
  push:
    branches: [dev]
    paths:
      - ".github/workflows/**"
      - "CODEOWNERS"
      - "CLAUDE.md"
  workflow_dispatch:

permissions:
  contents: read

jobs:
  perimeter:
    runs-on: arm64
    timeout-minutes: 10
    steps:
      - uses: actions/checkout@v4

      # Self-hosted runners are minimal and do not ship GitHub-hosted's toolset.
      # Installed without root, so this works whether or not sudo is available.
      - name: Ensure gh and jq are available
        run: |
          set -euo pipefail
          mkdir -p "$HOME/.local/bin"
          echo "$HOME/.local/bin" >> "$GITHUB_PATH"
          export PATH="$HOME/.local/bin:$PATH"

          ARCH=$(uname -m)
          case "$ARCH" in
            aarch64|arm64) JQ=arm64; GH=arm64 ;;
            x86_64|amd64)  JQ=amd64; GH=amd64 ;;
            *) echo "::error::Unsupported architecture $ARCH"; exit 1 ;;
          esac

          if ! command -v jq >/dev/null; then
            echo "jq not present, installing jq-linux-$JQ"
            curl -fsSL "https://github.com/jqlang/jq/releases/download/jq-1.7.1/jq-linux-$JQ"               -o "$HOME/.local/bin/jq"
            chmod +x "$HOME/.local/bin/jq"
          fi

          if ! command -v gh >/dev/null; then
            echo "gh not present, installing gh_2.63.2_linux_$GH"
            curl -fsSL "https://github.com/cli/cli/releases/download/v2.63.2/gh_2.63.2_linux_$GH.tar.gz"               | tar -xz -C /tmp
            mv "/tmp/gh_2.63.2_linux_$GH/bin/gh" "$HOME/.local/bin/gh"
          fi

          jq --version && gh --version | head -1

      - name: The host enforces what we say it enforces
        env:
          GH_TOKEN: ${{ secrets.PERIMETER_TOKEN }}
          REPO: ${{ github.repository }}
        run: |
          set -euo pipefail

          if [ -z "${GH_TOKEN:-}" ]; then
            echo "::error::PERIMETER_TOKEN is not set, so nothing verified that branch protection exists."
            echo "Create a fine-grained token with Administration: read and add it as a repository secret."
            echo "Until then this repository's gates are unproven — including the ones that look green."
            exit 1
          fi

          # ── what we claim ────────────────────────────────────────────────────────────────────
          # Every workflow in this repository must appear in exactly one of these three lists. That is
          # what makes the wall-of-red problem impossible: a gate this project cannot yet wire gets
          # DELETED and struck from the list, in one visible commit, rather than left failing forever.
          #
          # Three states, and the third is the one people get wrong:
          #   REQUIRED  — blocks the merge. Wired, and the host enforces it.
          #   ADVISORY  — runs and reports; merging ignores it. Earning its slot, or informational.
          #   NOT-A-GATE— never a pull-request check at all: scheduled, dispatched, or a deploy.
          #
          # A gate left installed but unwired fails on every pull request, and six permanent reds
          # teach everyone to stop reading the list — after which a real failure is indistinguishable
          # from the noise. That is the failure this whole repository exists to prevent, arriving
          # through the back door. So: if you cannot wire it, delete it and record it as *to build*.
          REQUIRED_CHECKS="size gates spec verify"
          ADVISORY_CHECKS="review red-on-base evidence criteria"
          NOT_A_GATE="perimeter scan deploy promote"
          REQUIRED_APPROVALS=1
          # ─────────────────────────────────────────────────────────────────────────────────────

          FAILED=0
          fail() { echo "::error::$1"; FAILED=1; }

          # GitHub has two protection systems and a repository can use either. Classic branch
          # protection answers /branches/dev/protection; a repository configured with a ruleset
          # returns 404 there while being fully protected. Verified against real repositories in
          # this org: one uses classic, one uses rulesets and 404s on the classic endpoint. Reading
          # only the classic endpoint therefore produces a false alarm rather than a false pass.
          # We read whichever answers and normalise both into one shape before asserting anything.
          MODE=""
          if P=$(gh api "repos/$REPO/branches/dev/protection" 2>/dev/null); then
            MODE="classic branch protection"
            NORM=$(jq -n --argjson p "$P" '{
              contexts:      ($p.required_status_checks.contexts // []),
              strict:        ($p.required_status_checks.strict // false),
              approvals:     ($p.required_pull_request_reviews.required_approving_review_count // 0),
              reviews:       ($p.required_pull_request_reviews != null),
              code_owners:   ($p.required_pull_request_reviews.require_code_owner_reviews // false),
              dismiss_stale: ($p.required_pull_request_reviews.dismiss_stale_reviews // false),
              linear:        ($p.required_linear_history.enabled // false),
              conversation:  ($p.required_conversation_resolution.enabled // false),
              no_force:      ($p.allow_force_pushes.enabled == false),
              no_delete:     ($p.allow_deletions.enabled == false),
              admins:        ($p.enforce_admins.enabled // false)
            }')
          elif R=$(gh api "repos/$REPO/rules/branches/dev" 2>/dev/null) && [ "$(jq 'length' <<<"$R")" -gt 0 ]; then
            MODE="repository ruleset"
            NORM=$(jq -n --argjson r "$R" '
              def has_rule($t): any($r[]; .type == $t);
              def params($t): (first($r[] | select(.type==$t) | .parameters) // {});
              {
                contexts:      [ (params("required_status_checks").required_status_checks // [])[].context ],
                strict:        (params("required_status_checks").strict_required_status_checks_policy // false),
                approvals:     (params("pull_request").required_approving_review_count // 0),
                reviews:       has_rule("pull_request"),
                code_owners:   (params("pull_request").require_code_owner_review // false),
                dismiss_stale: (params("pull_request").dismiss_stale_reviews_on_push // false),
                linear:        has_rule("required_linear_history"),
                conversation:  has_rule("required_conversation_resolution"),
                no_force:      has_rule("non_fast_forward"),
                no_delete:     has_rule("deletion"),
                admins:        null
              }')
          else
            echo "::error::dev is protected by neither branch protection nor a ruleset. Every gate in this repository is advisory."
            echo "Set one up, then re-run this job. Nothing below could be checked."
            exit 1
          fi
          echo "Protection is enforced by: $MODE"
          echo "$NORM" | jq .

          q() { jq -r "$1" <<<"$NORM"; }

          echo "── required status checks ──"
          for C in $REQUIRED_CHECKS; do
            jq -e --arg c "$C" '.contexts | index($c)' <<<"$NORM" >/dev/null \
              || fail "'$C' is not a required status check. It runs, it reports, and merging ignores it."
          done

          [ "$(q '.strict')" = "true" ] \
            || fail "Branches may merge without being up to date with main. A check that passed against stale main proves less than it looks like."

          echo "── review ──"
          [ "$(q '.reviews')" = "true" ] \
            || fail "Pull request review is not required. Approval is the one gate no workflow can replace."

          N=$(q '.approvals')
          [ "$N" -ge "$REQUIRED_APPROVALS" ] \
            || fail "Required approvals is $N, expected at least $REQUIRED_APPROVALS."

          [ "$(q '.code_owners')" = "true" ] \
            || fail "Code owner review is not required, so CODEOWNERS is a text file with no effect. The protected paths are not protected."

          [ "$(q '.dismiss_stale')" = "true" ] \
            || fail "Stale reviews are not dismissed. Someone can approve, then push anything, and merge on the old approval."

          echo "── history ──"
          # Linear history is a PRECONDITION here, not a preference. gates.yml walks
          # `git rev-list BASE..HEAD` commit by commit, and spec.yml asserts the spec is the branch's
          # first commit and an ancestor of every implementation commit. A merge commit inside a
          # branch makes both of them reason about an order nothing was ever tested in.
          [ "$(q '.linear')" = "true" ] \
            || fail "Linear history is not required, so the commit order gates.yml and spec.yml reason about is not the order anything was tested in."

          # Enforces the rule that every review finding gets a disposition, fixed or dismissed.
          [ "$(q '.conversation')" = "true" ] \
            || fail "Unresolved review conversations can be merged, so a finding can end up neither fixed nor dismissed."

          [ "$(q '.no_force')" = "true" ] \
            || fail "Force pushes to main are allowed, so the history that every other check reasons about can be rewritten."

          [ "$(q '.no_delete')" = "true" ] \
            || fail "main can be deleted."

          ADMINS=$(q '.admins')
          if [ "$ADMINS" = "null" ]; then
            echo "::warning::Ruleset mode. Whether anyone can bypass these rules is held in the ruleset's bypass_actors, which this endpoint does not return. Check it by hand on the ruleset, because a bypass actor makes every assertion above advisory for that person."
          elif [ "$ADMINS" != "true" ]; then
            echo "::warning::Administrators are exempt from these rules. Defensible on a small team; know that it means the perimeter holds only as long as everyone chooses to respect it."
          fi

          # ── every workflow is classified, and every claim has a file ──
          # Catches both directions of drift: a workflow added and never classified, and a name we
          # still claim to enforce whose file somebody deleted.
          echo "── the workflow inventory ──"
          ALL_LISTED="$REQUIRED_CHECKS $ADVISORY_CHECKS $NOT_A_GATE"
          for F in .github/workflows/*.yml; do
            [ -e "$F" ] || continue
            NAME=$(basename "$F" .yml)
            case " $ALL_LISTED " in
              *" $NAME "*) ;;
              *) fail "Workflow '$NAME' is not classified as REQUIRED, ADVISORY or NOT-A-GATE in this file. An unclassified workflow is one nobody has decided the status of, and it will sit red or green without meaning either." ;;
            esac
          done
          for NAME in $ALL_LISTED; do
            [ -f ".github/workflows/$NAME.yml" ] \
              || fail "This file claims '$NAME' but .github/workflows/$NAME.yml does not exist. Either restore it or strike the name — a claim with no file behind it is the pilot's failure exactly."
          done
          echo "Every workflow is classified, and every classified name has a file."

          echo "── the files that define the perimeter ──"
          for F in CODEOWNERS CLAUDE.md .github/workflows/size.yml .github/workflows/gates.yml .github/workflows/spec.yml; do
            [ -f "$F" ] || fail "$F is missing from the repository."
          done
          grep -q '^/\.github/workflows/' CODEOWNERS \
            || fail "CODEOWNERS does not protect .github/workflows/, so an agent can rewrite the gates and own the review of that change."
          grep -q '^/CODEOWNERS' CODEOWNERS \
            || fail "CODEOWNERS does not protect itself."

          if [ "$FAILED" -eq 1 ]; then
            echo ""
            echo "The perimeter does not match what this repository documents."
            echo "A check that is documented but absent is worse than one that was never promised —"
            echo "everyone downstream believes it ran."
            exit 1
          fi
          echo ""
          echo "The perimeter matches. Required: $REQUIRED_CHECKS, $REQUIRED_APPROVALS approval(s), code owners, no force push."

      # The in-session half of the perimeter. `.claude/settings.json` registers hooks by script path, and a
      # path that resolves to nothing is a hole in the enforcement surface that looks exactly like a hook:
      # registered, listed, never running. This belongs here rather than in a pull-request check because it is
      # the same question every other step on this job asks — does the thing we claim to enforce exist?
      #
      # Only NEVER INSTALLED fails. On a fresh checkout there are no heartbeats, so every hook reads NEVER
      # FIRED, and failing on that would make this job permanently red — the wall of red this file's own three
      # states exist to prevent.
      - name: Every registered hook points at a script that exists
        run: node scripts/hook-health.mjs --check
```

The two greps at the end are checking that `CODEOWNERS` assigns `/.github/workflows/` and `/CODEOWNERS`
itself to the tech leads group — the exact lines are in [the repository files](07-repository.md). An
agent that can edit `.github/workflows/` can make itself pass. An agent that can edit `CODEOWNERS` can
grant itself that. Those two lines are the base of the chain, and everything else in this document rests
on them.

Two assertions carry more weight than they look. `required_linear_history` is the precondition for
`gates.yml` and `spec.yml`: one walks `git rev-list BASE..HEAD` commit by commit and the other asserts
the spec is the first commit, and a merge commit inside a branch makes both reason about an order
nothing was ever tested in. `required_conversation_resolution` is the only mechanical enforcement of
"every review finding gets a disposition" — without it, a finding can end up neither fixed nor dismissed
and the pull request still merges. Both are host state, so this job is the only thing that will ever
tell you they are gone.

**How to test it locally.** With a token that has `Administration: read`:

```bash
GH_TOKEN=$PERIMETER_TOKEN gh api repos/OWNER/REPO/branches/main/protection | jq '{
  contexts: .required_status_checks.contexts,
  strict: .required_status_checks.strict,
  approvals: .required_pull_request_reviews.required_approving_review_count,
  code_owners: .required_pull_request_reviews.require_code_owner_reviews,
  dismiss_stale: .required_pull_request_reviews.dismiss_stale_reviews,
  linear: .required_linear_history.enabled,
  conversations: .required_conversation_resolution.enabled,
  force_push: .allow_force_pushes.enabled,
  admins: .enforce_admins.enabled }'
```

If that returns 404, the repository uses a ruleset; read `repos/OWNER/REPO/rules/branches/main` instead.
Then break it on purpose: remove `size` from the required checks on the host, run the job with
`workflow_dispatch`, confirm it fails, put it back.

**What it cannot catch.** It is not a pull request check, because protection is not a property of a
branch under review. It runs Monday 07:00 UTC, on pushes to `main` touching workflows, `CODEOWNERS` or
`CLAUDE.md`, and on demand — so a perimeter broken by any other route is found up to a week later. In
ruleset mode it cannot read `bypass_actors`, so it normalises `admins` to null and warns; a bypass actor
makes every assertion above advisory for that person, and you have to check the ruleset by hand. In
classic mode it treats `enforce_admins.enabled == false` as a warning rather than a failure, defensible
on a small team at this cost: the perimeter then holds only while every administrator chooses to respect
it, and the person most likely to be in a hurry at 6pm is the one with admin rights.

## scan — known vulnerabilities, on a clock

**What it enforces.** That no critical dependency or code-scanning alert is open, and no high alert has
been open more than seven days. Daily at 06:00 UTC, on every push to `main`, and on demand.

The reason it runs on a clock rather than per pull request is a measurement. Across 304,362 verified
AI-authored commits, 15–29% introduced at least one new static-analysis issue, 24.2% of introduced
issues were still present at HEAD, and security issues persisted worst at 41.1%. Read that carefully:
the issues that survive were introduced by changes that *passed*. A scan bound to a pull request sees
the moment an issue is introduced and never sees it again — it has no way to notice that the thing it
waved through in March is still there in August. Per-pull-request scanning answers "did this diff add
something new"; the number above says the problem is "what is still open across the whole tree". Those
are different questions and need different triggers.

It reads the host's alert state rather than running a scanner inside the job, for the same reason
`perimeter.yml` reads the host rather than a file: the host has already scanned the full history with a
maintained ruleset, and a check that lives outside the repository is one an agent cannot quiet. The cost
is a dependency — Dependabot and code scanning have to be switched on. If Dependabot is unavailable the
job fails rather than reporting a clean tree it never looked at.

`.github/workflows/scan.yml`

```yaml
name: scan

# Scanning on a clock, over the whole tree, not once per ticket.
#
# The reason is a number this process already cites: of the static-analysis issues introduced by
# AI-authored commits, 24.2% are still present at HEAD, and security issues persist worst at 41.1%.
# A scan that only reads the diff of one pull request sees the moment an issue is introduced and
# never sees it again. Most of the surviving ones were introduced by a change that passed.
#
# So this job reads the whole repository's current alert state on a schedule. It deliberately reads
# the HOST's alerts rather than running a scanner in the job: the host has already scanned the whole
# history with a maintained ruleset, and a check that lives outside the repository is one an agent
# cannot quiet. That does mean Dependabot and code scanning have to be switched on - if they are not,
# this job says so and fails, rather than reporting a clean tree it never looked at.

on:
  schedule:
    - cron: "0 6 * * *"      # daily, before the working day
  push:
    branches: [dev]
  workflow_dispatch:

permissions:
  contents: read
  security-events: read

jobs:
  scan:
    runs-on: arm64
    timeout-minutes: 15
    steps:
      - uses: actions/checkout@v4

      - name: Ensure gh and jq are available
        run: |
          set -euo pipefail
          mkdir -p "$HOME/.local/bin"; echo "$HOME/.local/bin" >> "$GITHUB_PATH"
          export PATH="$HOME/.local/bin:$PATH"
          case "$(uname -m)" in aarch64|arm64) A=arm64 ;; x86_64|amd64) A=amd64 ;; *) echo "::error::unsupported arch"; exit 1 ;; esac
          command -v jq >/dev/null || { curl -fsSL "https://github.com/jqlang/jq/releases/download/jq-1.7.1/jq-linux-$A" -o "$HOME/.local/bin/jq"; chmod +x "$HOME/.local/bin/jq"; }
          command -v gh >/dev/null || { curl -fsSL "https://github.com/cli/cli/releases/download/v2.63.2/gh_2.63.2_linux_$A.tar.gz" | tar -xz -C /tmp; mv "/tmp/gh_2.63.2_linux_$A/bin/gh" "$HOME/.local/bin/gh"; }

      - name: What is open right now, and for how long
        env:
          GH_TOKEN: ${{ secrets.PERIMETER_TOKEN || secrets.GITHUB_TOKEN }}
          REPO: ${{ github.repository }}
        run: |
          set -euo pipefail
          FAILED=0
          NOW=$(date -u +%s)
          # An open critical is a today problem. A high gets a week before it becomes one.
          HIGH_AGE_DAYS=7

          check_age() {   # $1 = json array of {severity, created_at, title, url}
            local KIND="$1" DATA="$2"
            local N; N=$(jq 'length' <<<"$DATA")
            echo "  $KIND: $N open"
            [ "$N" -eq 0 ] && return 0
            while IFS=$'\t' read -r SEV CREATED TITLE URL; do
              [ -z "${SEV:-}" ] && continue
              local AGE=$(( (NOW - $(date -u -d "$CREATED" +%s 2>/dev/null || echo "$NOW")) / 86400 ))
              case "$SEV" in
                critical)
                  echo "::error::critical $KIND, open $AGE day(s): $TITLE  $URL"; FAILED=1 ;;
                high)
                  if [ "$AGE" -gt "$HIGH_AGE_DAYS" ]; then
                    echo "::error::high $KIND, open $AGE day(s), past the $HIGH_AGE_DAYS-day limit: $TITLE  $URL"; FAILED=1
                  else
                    echo "::warning::high $KIND, open $AGE day(s): $TITLE"
                  fi ;;
                *) echo "    $SEV ($AGE d): $TITLE" ;;
              esac
            done < <(jq -r '.[] | [.severity, .created_at, .title, .url] | @tsv' <<<"$DATA")
          }

          echo "── dependency alerts ──"
          if D=$(gh api "repos/$REPO/dependabot/alerts?state=open&per_page=100" 2>/dev/null); then
            check_age "dependency alert" \
              "$(jq '[.[] | {severity: .security_advisory.severity, created_at, title: (.security_advisory.summary // "?"), url: .html_url}]' <<<"$D")"
          else
            echo "::error::Dependabot alerts are unavailable. Either the feature is off, or the token cannot read them."
            echo "A scan that cannot see is not a scan. Turn it on in Settings > Code security, or remove this job and the row it claims in the enforcement table."
            FAILED=1
          fi

          echo "── code scanning alerts ──"
          if C=$(gh api "repos/$REPO/code-scanning/alerts?state=open&per_page=100" 2>/dev/null); then
            check_age "code scanning alert" \
              "$(jq '[.[] | {severity: (.rule.security_severity_level // .rule.severity // "note"), created_at, title: (.rule.description // .rule.id), url: .html_url}]' <<<"$C")"
          else
            echo "::warning::Code scanning is not enabled, so nothing is looking at the source itself — only at dependencies."
            echo "This is the class where 41.1% of AI-introduced issues survive to HEAD. Enable CodeQL or another scanner."
          fi

          if [ "$FAILED" -eq 1 ]; then
            echo ""
            echo "A red scan is a ticket, not a merge block: it runs on a clock rather than on a pull request,"
            echo "because the issues that survive were introduced by changes that passed."
            exit 1
          fi
          echo "Nothing open past its limit."
```

A red scan is a ticket, not a merge block. There is no pull request for it to stop, which is the design:
blocking today's unrelated ticket on last quarter's transitive dependency is how a security control
becomes the thing everyone learns to override.

**How to test it locally.** With a token that can read the alert endpoints:

```bash
gh api "repos/OWNER/REPO/dependabot/alerts?state=open&per_page=100" \
  --jq '.[] | [.security_advisory.severity, .created_at, .security_advisory.summary] | @tsv'
gh api "repos/OWNER/REPO/code-scanning/alerts?state=open&per_page=100" \
  --jq '.[] | [(.rule.security_severity_level // .rule.severity), .created_at, .rule.id] | @tsv'
```

**What it catches.** A critical dependency advisory nobody triaged. A high left open past a week. Code
scanning silently switched off — the dependency half fails loudly, and the code-scanning half warns and
names what is unwatched.

**What it cannot catch.** Anything the host's scanners do not flag: business-logic authorisation holes,
a missing tenancy check, a secret already committed. Severity is the advisory's opinion, not yours — a
critical in a dev-only dependency and a critical in the request path score the same. `date -u -d` is GNU
`date`, so this step needs a Linux runner; on macOS it silently falls back to an age of zero, which
under-reports rather than over-reports. And the code-scanning half warning rather than failing means a
repository with dependency alerts on and CodeQL off shows this job green while nothing reads the source
— the exact class where 41.1% survive to HEAD.

## The hints: lefthook and the secret scan

Not gates. The files say so in their first line. They exist to make the fast failure fast.

`lefthook.yml`

```yaml
# Hooks are hints. The gates are the required checks on the host.
# These exist to give fast feedback, not to protect anything.
pre-commit:
  parallel: true
  commands:
    format:  { glob: "*.{js,ts,tsx,json,css,md}", run: "bun run format:check {staged_files}" }
    secrets: { run: "bun run scan:secrets" }
commit-msg:
  commands:
    conventional: { run: "bunx commitlint --edit {1}" }
pre-push:
  commands:
    verify: { run: "bun run verify" }
    # Catches the board problems CI does not: duplicate ids, a blocker with no entry, a DONE entry
    # with no Resolution on a ticket other than this branch's. A hint, so --no-verify walks past it —
    # the one property that must hold is gated in spec.yml instead.
    board:  { run: "node scripts/board.mjs --check" }
    # The gates' own tests, before they get a chance to be wrong on somebody else's branch. A hint here and a
    # required check in verify.yml: this one is fast enough to want locally and too important to leave optional.
    selftest: { run: "node scripts/self-test.mjs" }
    # A hook that silently stopped firing is worse than no hook. Only NEVER INSTALLED fails (exit 1) — a
    # registered script that is not in the tree. NEVER FIRED is the normal state of a fresh clone and must not
    # fail, or this recreates the wall of red that finding 63 is about.
    hooks:    { run: "node scripts/hook-health.mjs --check" }
```

The pre-push hook runs the same `bun run verify` that `verify.yml` runs. That is the point of having one
entry point: the four-minute CI failure and the twenty-second local failure are the same failure. The
commit-msg hook calls commitlint against [commitlint.config.js](07-repository.md).

`scripts/scan-secrets.mjs`

```javascript
#!/usr/bin/env bun
// Staged content only, and only patterns with a real prefix — a scanner that cries wolf gets
// bypassed, and a bypassed scanner is worse than none because it still reads as protection.
//
// This is a hint, not a gate. It runs pre-commit, where --no-verify walks straight past it.
// Rotate anything that reached a remote; a deleted commit is not a rotated key.

import { execSync } from "node:child_process";

const PATTERNS = [
  [/\bsk-ant-[A-Za-z0-9_-]{20,}/, "Anthropic API key"],
  [/\bsk-(proj-)?[A-Za-z0-9]{32,}/, "OpenAI API key"],
  [/\bghp_[A-Za-z0-9]{36}\b/, "GitHub personal access token"],
  [/\bgithub_pat_[A-Za-z0-9_]{50,}/, "GitHub fine-grained token"],
  [/\bAKIA[0-9A-Z]{16}\b/, "AWS access key id"],
  [/\bsk_(live|test)_[A-Za-z0-9]{20,}/, "Stripe secret key"],
  [/\bxox[baprs]-[A-Za-z0-9-]{10,}/, "Slack token"],
  [/-----BEGIN (RSA |EC |OPENSSH |PGP )?PRIVATE KEY-----/, "private key"],
  [/\bpostgres(ql)?:\/\/[^\s:@/]+:[^\s@/]+@/, "database URL with a password in it"],
  [/\bmongodb(\+srv)?:\/\/[^\s:@/]+:[^\s@/]+@/, "database URL with a password in it"],
  [/\beyJ[A-Za-z0-9_-]{10,}\.eyJ[A-Za-z0-9_-]{10,}\./, "JWT"],
];

const SKIP = /(^|\/)(node_modules|dist|build|coverage)\/|\.(lock|lockb|png|jpe?g|gif|pdf|woff2?)$|(^|\/)bun\.lockb$/;

const staged = execSync("git diff --cached --name-only --diff-filter=ACM", { encoding: "utf8" })
  .split("\n")
  .filter((f) => f && !SKIP.test(f));

let found = 0;
for (const file of staged) {
  let diff;
  try {
    diff = execSync(`git diff --cached -U0 -- ${JSON.stringify(file)}`, { encoding: "utf8" });
  } catch {
    continue;
  }
  for (const line of diff.split("\n")) {
    if (!line.startsWith("+") || line.startsWith("+++")) continue;
    if (/\b(example|placeholder|dummy|fake|redacted|xxx+|your[-_]?key)\b/i.test(line)) continue;
    for (const [re, what] of PATTERNS) {
      if (re.test(line)) {
        console.error(`${file}: ${what}`);
        console.error(`  ${line.slice(1).trim().slice(0, 120)}`);
        found++;
        break;
      }
    }
  }
}

if (found) {
  console.error(
    `\n${found} likely secret(s) staged.\n\n` +
      "Unstage them and read them from the environment. If one already reached a remote, rotate it —\n" +
      "removing the commit does not un-publish the key.\n\n" +
      "A committed fixture must have real credentials and real personal data stripped before it lands.",
  );
  process.exit(1);
}
```

The third hint is the deny and ask lists in [.claude/settings.json](07-repository.md), which stop the
agent force-pushing, merging, self-approving, self-labelling or reading `.env` — and which prompt before
it edits a workflow, `CODEOWNERS`, `CLAUDE.md` or a design criterion.

**How to test them locally.**

```bash
lefthook install                                  # or: bun run setup
printf 'const k = "AKIAZZZZZZZZZZZZZZZZ"\n' > leak.ts
git add leak.ts && bun run scan:secrets ; git reset && rm leak.ts
```

**What they catch.** A staged AWS, Anthropic, OpenAI, GitHub, Stripe or Slack credential, a private key,
or a database URL with a password in it, before it reaches a remote. A commit message that is not
conventional. Formatting drift, in two seconds instead of four minutes.

**What they cannot catch.** Anything, once someone types `--no-verify`. That is not a flaw in lefthook;
it is what a hook is. `scan-secrets.mjs` reads staged content only, matches only patterns with a real
prefix — a bare 32-character password is invisible to it — and skips lines containing `example`,
`placeholder`, `dummy`, `fake`, `redacted` or `your-key`. That skip is deliberate: a scanner that cries
wolf gets bypassed, and a bypassed scanner is worse than none because it still reads as protection. The
only real control is host-side push protection, which rejects at the remote and is covered in [host and
pipeline](09-host-and-pipeline.md). Rotate anything that reached a remote; deleting the commit does not
un-publish the key.

`.claude/settings.json` is enforced by the agent harness, not the host. `Bash(git commit*--no-verify*)`
does not match `git -c core.hooksPath=/dev/null commit`, and none of it applies to a person in a
terminal or to a different tool. Treat it as a guardrail on the happy path, and let the required checks
be the reason none of that matters.

## What this set does not give us

A published four-layer model for agentic governance asks for pipeline guardrails, policy-as-code,
embedded security specialists, and senior sign-off on AI-assisted production changes. Three of those are
here: the required checks are the guardrails, `CODEOWNERS` plus branch protection are the policy, and
code-owner review on the protected paths is the sign-off.

The embedded security specialist we do not have, and probably will not. A person per pod is not a
staffing shape a services company of our size can hold. What we do instead is put auth, payments and
personal data on protected paths so a second person sees every change to them, and run `scan.yml` daily.
That is weaker. Not equivalent — weaker — and the honest way to describe it to a client is weaker. A
daily alert-state check finds a known vulnerability with a CVE number; it does not find the
authorisation bug a specialist would have found reading the diff.

## The enforcement summary

Read the status column literally. **Written** means the file exists as printed above and its logic has
run locally. **Proven** means it has run on a host and failed something it was supposed to fail. **To
build** means it protects nothing today, and quoting the row as a guarantee is the original problem
happening again.

| Rule | Enforced by | Where | Status |
|---|---|---|---|
| ≤400 lines / 20 files per pull request | required check on the diff | `size.yml` | written |
| Over-ceiling is a person's decision | `size-override` label, labeller ≠ author | `size.yml` | written |
| Gate changes in their own commit | required check over commit statuses | `gates.yml` | written |
| No suppression markers added | required check grepping the diff | `gates.yml` | written — workflows only |
| Branch carries a ticket id | required check | `spec.yml` | written |
| Spec exists and is the first commit | required check | `spec.yml` | written |
| The spec was *approved* | review requirement on the host | host config, asserted by `perimeter.yml` | written — no check proves it was read |
| A spec revision is visible | warning on the pull request | `spec.yml` | written — a warning, not a gate |
| Format, lint, types, build, tests | one entry point: hook and required check | `verify.mjs` + `verify.yml` | written — fails when unwired |
| 80% coverage on changed lines | threshold that fails the build | `changed-line-coverage.mjs` | written — skipped when no lcov |
| Assertions actually assert | mutation testing | nothing | **to build** |
| Every criterion names evidence that resolves | advisory check over every row of the table | `criteria.yml` + `scripts/lib/criteria.mjs` | written — advisory until its false-positive rate is known |
| A claim word cannot stand in for an artefact | the resolver's refusal list, wrappers stripped first | `scripts/lib/criteria.mjs` | written — the quoted form is a regression case |
| The named artefact actually proves the criterion | judgement, plus `red-on-base` for a named test | `review.yml`, `red-on-base.yml` | **to build** — nothing mechanical reads the artefact |
| A fresh session reviews the diff | required check | `review.yml` | written — fails when unconfigured |
| Every finding gets a disposition | `required_conversation_resolution` | host config, asserted by `perimeter.yml` | written |
| The gate surface is inspected | the review agent's first ordering rule | `review.yml` | written — the only check aimed at the checks |
| Protected paths need a second reviewer | CODEOWNERS + `require_code_owner_reviews` | `CODEOWNERS`, host config | written |
| History is linear | `required_linear_history` | host config, asserted by `perimeter.yml` | written — precondition for `gates.yml` and `spec.yml` |
| Nothing is pushed straight to main | branch protection | host config | to build, per repository |
| The host matches this document | scheduled job against the host API | `perimeter.yml` | written — untestable until it runs |
| No secret reaches the remote | host push protection; the scan is a hint | host config + `scan-secrets.mjs` | scan written; **host rejection to build** |
| Conventional commit messages | commit-msg hook | `commitlint.config.js` | hook written; required check to build |
| The agent cannot merge, approve, force-push, self-label | harness permissions | `.claude/settings.json` | written — harness only, not the host |
| Known vulnerabilities are not left open | daily job over the host's alert state | `scan.yml` | written — needs Dependabot and code scanning enabled |
| Status is derived, never self-reported | git and CI events | tracker integration | to build |

## Nothing here is proven

Every check above is *written*. Not one is *proven*, because at the time of writing none has executed on
a host and failed something it should have failed. That is the pilot's failure exactly: its context file
claimed branch protection, there was no remote, and CI had run zero times. No check at all looks
identical from the outside to a check that passes.

So the last step of setting this up is not reading these files. It is this, once, per repository:

1. Push a branch whose first commit is not the spec. Watch `spec` fail.
2. Push a commit that edits an existing test and a source file together. Watch `gates` fail.
3. Push a 500-line diff. Watch `size` fail. Have someone else add the label. Watch it pass with a
   warning. Then add the label yourself on a second pull request and watch it fail anyway.
4. Delete a required script from `package.json`. Watch `verify` fail rather than skip.
5. Remove `size` from the host's required checks. Run `perimeter` by hand. Watch it fail. Put it back.
6. Unset `ANTHROPIC_API_KEY`. Watch `review` fail rather than report green for work nobody read.
7. Turn Dependabot off. Run `scan` by hand. Watch it fail rather than report a clean tree.
8. Put `| Rollback tested | verified | |` in a pull request body, then the same word in backticks. Watch
   `criteria` refuse both rows and name the template that shows the right shape. It reports rather than
   blocks, so what you are observing is that the resolver is right — which is the precondition for ever
   making it required.

Until a failure has been observed, a check is a claim. After it — and only for the specific thing you
made fail — the status column may say *proven*. Put the run link next to the row. The dated plan for
doing this on a real repository is in [the runbook](12-runbook.md); what to do when one of these fires
and you think it is wrong is in [troubleshooting](13-troubleshooting.md).

### `evidence.yml` — making the artefacts durable

Every acceptance criterion is supposed to carry the artefact that proves it, and for anything with an
interface that artefact is a screenshot or a browser trace. Those had nowhere to live: committing
screenshots bloats the repository, and nothing else in the process could see them.

So `.evidence/<TICKET-ID>/` is gitignored, produced by the `operate-app` skill, and uploaded here as a
pull-request artefact with one comment edited in place.

```yaml
name: evidence

# Makes the evidence the agent produced durable and linked from the pull request.
#
# Our own rule is that a ticket with an interface is not done until something operated it, and that
# every acceptance criterion carries the artefact that proves it. Before this job the artefacts had
# nowhere to live: committing screenshots bloats the repository, and nothing else in the process could
# see them. So .evidence/ is gitignored, produced by the operate-app skill, and uploaded here.
#
# This job deliberately does NOT fail when evidence is missing. It cannot tell whether a ticket needed
# any - a migration or a worker legitimately has none - and a check that guesses would either block
# honest work or teach people to produce a screenshot of nothing. It reports what is there and says
# plainly when there is nothing, and the human reading the criteria table decides.

on:
  pull_request:
    types: [opened, synchronize, reopened]

permissions:
  contents: read
  pull-requests: write

jobs:
  evidence:
    runs-on: arm64
    timeout-minutes: 10
    steps:
      - uses: actions/checkout@v4

      # Self-hosted runners are minimal and do not ship GitHub-hosted's toolset.
      # Installed without root, so this works whether or not sudo is available.
      - name: Ensure gh and jq are available
        run: |
          set -euo pipefail
          mkdir -p "$HOME/.local/bin"
          echo "$HOME/.local/bin" >> "$GITHUB_PATH"
          export PATH="$HOME/.local/bin:$PATH"

          ARCH=$(uname -m)
          case "$ARCH" in
            aarch64|arm64) JQ=arm64; GH=arm64 ;;
            x86_64|amd64)  JQ=amd64; GH=amd64 ;;
            *) echo "::error::Unsupported architecture $ARCH"; exit 1 ;;
          esac

          if ! command -v jq >/dev/null; then
            echo "jq not present, installing jq-linux-$JQ"
            curl -fsSL "https://github.com/jqlang/jq/releases/download/jq-1.7.1/jq-linux-$JQ"               -o "$HOME/.local/bin/jq"
            chmod +x "$HOME/.local/bin/jq"
          fi

          if ! command -v gh >/dev/null; then
            echo "gh not present, installing gh_2.63.2_linux_$GH"
            curl -fsSL "https://github.com/cli/cli/releases/download/v2.63.2/gh_2.63.2_linux_$GH.tar.gz"               | tar -xz -C /tmp
            mv "/tmp/gh_2.63.2_linux_$GH/bin/gh" "$HOME/.local/bin/gh"
          fi

          jq --version && gh --version | head -1

      - name: Collect what the agent produced
        id: collect
        run: |
          set -euo pipefail
          BRANCH="${{ github.event.pull_request.head.ref }}"
          TICKET=$(printf '%s' "$BRANCH" | grep -oE '^[A-Z][A-Z0-9]+-[0-9]+' || true)
          echo "ticket=$TICKET" >> "$GITHUB_OUTPUT"

          DIR=".evidence/$TICKET"
          if [ -z "$TICKET" ] || [ ! -d "$DIR" ]; then
            echo "found=none" >> "$GITHUB_OUTPUT"
            echo "No evidence directory at $DIR."
            exit 0
          fi

          COUNT=$(find "$DIR" -type f -not -name manifest.md | wc -l | tr -d ' ')
          echo "found=$COUNT" >> "$GITHUB_OUTPUT"
          echo "$COUNT artefact(s) in $DIR:"
          find "$DIR" -type f | sed 's/^/  /'

          # The manifest is the part a person reads. Its "not covered" line is the honest bit.
          if [ -f "$DIR/manifest.md" ]; then
            echo "manifest=yes" >> "$GITHUB_OUTPUT"
          else
            echo "manifest=no" >> "$GITHUB_OUTPUT"
            echo "::warning::Artefacts present but no manifest.md, so nothing says which criterion each one proves."
          fi

      - name: Upload
        if: steps.collect.outputs.found != 'none'
        uses: actions/upload-artifact@v4
        with:
          name: evidence-${{ steps.collect.outputs.ticket }}
          path: .evidence/${{ steps.collect.outputs.ticket }}
          retention-days: 90
          if-no-files-found: ignore

      - name: Say what is there, on the pull request
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          PR: ${{ github.event.pull_request.number }}
          REPO: ${{ github.repository }}
          FOUND: ${{ steps.collect.outputs.found }}
          MANIFEST: ${{ steps.collect.outputs.manifest }}
          TICKET: ${{ steps.collect.outputs.ticket }}
        run: |
          set -euo pipefail
          RUN="https://github.com/$REPO/actions/runs/${{ github.run_id }}"

          if [ "$FOUND" = "none" ]; then
            BODY=$(printf '**No evidence artefacts on this branch.**\n\nThat is correct for work with nothing to look at — a migration, a worker, a refactor. It is not correct for anything with an interface: our rule is that a ticket with an interface is not done until something operated it, and "it renders" is a different check.\n\nIf this ticket has a visible criterion, run the `operate-app` skill and push. If it does not, say so under **What this does not verify** and this comment can be ignored — NOT in the criteria table, which the `criteria` check reads: a cell holding an explanation instead of an artefact is exactly what that check refuses, and this comment used to send people straight into it.')
          else
            BODY=$(printf '**%s evidence artefact(s)** for `%s` — [download from the run](%s).\n\nManifest present: **%s**. The manifest is the part worth reading: it says which criterion each artefact proves, and which criteria it could not cover. A manifest with no gaps on a ticket that has gaps is worse than none.' \
              "$FOUND" "$TICKET" "$RUN" "$MANIFEST")
          fi

          # One comment per pull request, edited in place, so the thread does not fill with duplicates.
          ID=$(gh api "repos/$REPO/issues/$PR/comments" --jq \
            '[.[] | select(.body | startswith("**No evidence") or startswith("**") and contains("evidence artefact")) | .id] | last // ""' 2>/dev/null || echo "")
          if [ -n "$ID" ]; then
            gh api -X PATCH "repos/$REPO/issues/comments/$ID" -f body="$BODY" >/dev/null
          else
            gh api -X POST "repos/$REPO/issues/$PR/comments" -f body="$BODY" >/dev/null
          fi
          echo "Reported."
```

**It does not fail when evidence is absent, on purpose.** It cannot tell whether a ticket needed any —
a migration, a worker or a refactor legitimately has none — and a check that guessed would either block
honest work or teach people to produce a screenshot of nothing. It reports what is there, says plainly
when there is nothing, and the person reading the criteria table decides. That is one of the few places
we prefer a warning to a gate, and the reason is that the alternative gate would be dishonest.

## `red-on-base.yml` and `scripts/red-on-base.mjs` — does the test catch its own bug?

Every other check here asks whether the tests pass. This one asks whether they would have **failed before the
change**. A test that passes against the unfixed code is not evidence of anything, and on a green dashboard it
is indistinguishable from a real one.

It runs the pull request's new and changed tests against the base commit and classifies how each fails:

| At the base commit | Verdict | What happens |
|---|---|---|
| Fails on an **assertion**, with a captured expected/actual | **ASSERTION** | proof stored, check satisfied |
| Cannot **load** — the symbol did not exist yet | **NOT-A-BEHAVIOUR-FIX** | N/A, and the check passes |
| **Passes** | PASSED-AT-BASE | fails the check when the change declares a fix; a warning otherwise |
| Fails in a way the script cannot read | UNCLASSIFIED | **fails**, because a gate that cannot tell must not guess |

**Two design choices are worth the argument.**

*There is no "is this a bug fix?" question.* The standard that proposed this mechanism gated it on a
conventional-commit prefix and routed everything else through a tech-lead waiver — while elsewhere warning
that routine waivers on a non-negotiable check spend the one budget of gate credibility. E6 in
[`research/experiments.md`](../research/experiments.md) shows the question is unnecessary: run the test at
base and the *outcome* classifies the change. Eleven of twelve real fixes failed on an assertion; the twelfth
was a commit labelled `fix:` that added a new file, so its test could not resolve its import — which is
precisely how you detect that something is not a behaviour fix, mechanically, with nobody signing anything.

*Passing at base is only a defect when the change claims to fix something.* A regression test pinning
behaviour that already works is supposed to pass at base. Telling those apart needs intent, so the check reads
the commit subjects for a declared fix and warns rather than fails when there is none. That asymmetry is
deliberate and it is the one place this check takes an author's word for anything.

**What it cannot do**, stated because the gap is easy to miss: it says nothing about whether the assertion is
the *right* assertion. A test and the code can share a misunderstanding and this will store the proof
happily — open question D11. It catches a missing proof, not a wrong one.

The classifier is the whole check, so it is tested against **real captured runner output** — including the two
outputs from E6 — and that self-test runs in CI rather than only on somebody's laptop. It is deliberately not
in `REQUIRED_CHECKS`: it reports, and merging ignores it, until it has produced findings on real work and its
N/A rate is known. Same rule as `review`.

### `.github/workflows/red-on-base.yml`

```yaml
name: red-on-base

# Does the new test actually catch the bug it was written for?
#
# Every other check here asks whether the tests pass. This one asks whether they would have FAILED before
# the change — because a test that passes against the unfixed code is not evidence of anything, and it is
# indistinguishable from a real test on a green dashboard.
#
# It runs the pull request's new and changed tests against the base commit and classifies how each one
# fails. An assertion failure is proof and gets stored. A failure to even load means the change introduced
# a new symbol rather than fixing existing behaviour, which is N/A rather than a violation — decided from
# the runner's own report, with no waiver and no person. A test that PASSES at base fails the check when the
# change declares a fix.
#
# NOT required at first. Turn it on once it has produced findings on real work and its N/A rate is known —
# same rule as `review`. Until then it reports and merging ignores it, which is the honest state.
#
# Evidence for the mechanism, including why there is no "is this a bug fix?" question, is E6 in the SDLC's
# research/experiments.md: 11 of 12 real fixes in a public repository failed at base on an assertion, and
# the twelfth was a commit labelled `fix:` that added a file.

on:
  pull_request:
    types: [opened, synchronize, reopened]

permissions:
  contents: read

jobs:
  red-on-base:
    runs-on: arm64
    timeout-minutes: 20
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0 # the base commit has to be reachable, and a worktree is created at it

      - uses: oven-sh/setup-bun@v2
        with:
          bun-version: latest

      - name: Install
        run: bun install --frozen-lockfile

      # The classifier is the whole gate: if it cannot tell an assertion failure from a suite that never
      # loaded, a green run means nothing. It is checked against real captured runner output before it is
      # trusted, and that check runs here rather than only on somebody's laptop.
      - name: The classifier still works
        run: node scripts/red-on-base.mjs --self-test

      - name: Run the new tests against the base commit
        env:
          BASE_SHA: ${{ github.event.pull_request.base.sha }}
          HEAD_SHA: ${{ github.event.pull_request.head.sha }}
        run: node scripts/red-on-base.mjs

      - name: Keep the proof
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: red-on-base-proof
          path: .evidence/red-on-base/
          if-no-files-found: ignore
          retention-days: 30
```

### `scripts/red-on-base.mjs`

```javascript
#!/usr/bin/env node
// Red-on-base: does the new test actually catch the bug it was written for?
//
// A green suite proves the tests that exist pass. It does not prove a test asserts anything. This runs the
// pull request's new and changed tests against the BASE commit — the code before the fix — and asks how they
// fail there. A bug fix's test must fail at base, and it must fail on an ASSERTION rather than because a
// symbol did not exist yet. A test that fails at base with "cannot find module" has proven nothing.
//
//   node scripts/red-on-base.mjs              # the gate; BASE_SHA and HEAD_SHA from the environment
//   node scripts/red-on-base.mjs --self-test  # prove the classifier against real captured runner output
//
// WHY THERE IS NO "IS THIS A BUG FIX?" QUESTION. ADS-1, which proposed this mechanism, gated it on a
// conventional-commit prefix and routed everything else through a tech-lead waiver — while elsewhere warning
// that routine waivers on a non-negotiable check spend the one budget of gate credibility. Measuring 12 real
// fixes (research/experiments.md, E6) showed the question is unnecessary: run the test at base and the
// OUTCOME classifies the change. Eleven failed on an assertion. The twelfth was a commit labelled `fix:`
// that added a new file, so its test could not resolve its import — which is exactly how you detect that
// something is not a behaviour fix, mechanically, with no human and no waiver.
//
// WHAT IT CANNOT DO. It says nothing about whether the assertion is the RIGHT assertion. A test and the code
// can share a misunderstanding and this gate will happily store the proof — see open question D11. It
// catches a MISSING proof, not a wrong one.

import { execFileSync } from "node:child_process";
import { existsSync, mkdirSync, writeFileSync, readFileSync, rmSync, cpSync } from "node:fs";
import { join, dirname } from "node:path";

const args = process.argv.slice(2);
const sh = (cmd, a, opts = {}) =>
  execFileSync(cmd, a, { encoding: "utf8", stdio: ["ignore", "pipe", "pipe"], ...opts });

// ── the classifier ──────────────────────────────────────────────────────────────────────────────────
// Patterns per runner, kept together and visible so a new stack extends one list. The order matters: a
// load failure must be recognised BEFORE an assertion pattern, because a suite that failed to load often
// prints text that looks like an assertion elsewhere in the output.
const LOAD_FAILURE = [
  /Test suite failed to run/, // jest
  /Cannot find module|Failed to load url|ERR_MODULE_NOT_FOUND/, // jest, vitest, node
  /SyntaxError:|ReferenceError:.*is not defined/, //
  /ImportError|ModuleNotFoundError|E   NameError/, // pytest
  /collected 0 items|errors during collection/, // pytest
  /is not a function|is not a constructor/, // js: the symbol exists as undefined
];
const ASSERTION = [
  /expect\(.*\)\.|Expected value to equal|Expected:.*\n.*Received:/s, // jest, vitest
  /AssertionError|assert\.|toBe|toEqual|toMatch|toThrow/,
  /^E\s+assert |^E\s+AssertionError/m, // pytest
  /FAIL .*\n.*●/s,
];

export function classify(output, exitCode) {
  if (exitCode === 0) return { verdict: "PASSED-AT-BASE", why: "the test passes against the unfixed code" };
  for (const re of LOAD_FAILURE) {
    const m = output.match(re);
    if (m) return { verdict: "NOT-A-BEHAVIOUR-FIX", why: `the suite could not load at base: ${m[0].slice(0, 60).trim()}` };
  }
  for (const re of ASSERTION) {
    if (re.test(output)) {
      const pair = output.match(/Expected[^\n]*\n[^\n]*\n?[^\n]*Received[^\n]*\n[^\n]*/) ||
                   output.match(/Expected[^\n]{0,80}|Received[^\n]{0,80}/);
      return { verdict: "ASSERTION", why: (pair?.[0] || "assertion failure").replace(/\s+/g, " ").slice(0, 120) };
    }
  }
  // Never pass on ambiguity. An unclassifiable failure is a gap in this script, and a gate that guesses is
  // worse than one that admits it cannot tell.
  return { verdict: "UNCLASSIFIED", why: "the run failed and this script could not tell how" };
}

// ── self-test: real captured output, not invented text ──────────────────────────────────────────────
if (args.includes("--self-test")) {
  const cases = [
    ["assertion, from dayjs fefdcd4b6 at base", 1,
     `FAIL test/plugin/utc-utcOffset.test.js\n  ✕ cloning dates modified with utcOffset (5ms)\n\n  ● cloning dates modified with utcOffset\n\n    expect(received).toEqual(expected)\n\n    Expected value to equal:\n      "2023-10-28T17:00:00Z"\n    Received:\n      "2023-10-28T21:00:00Z"\n`,
     "ASSERTION"],
    ["load failure, from dayjs 6a42e0d73 at base", 1,
     `FAIL test/plugin/negativeYear.test.js\n  ● Test suite failed to run\n\n    Cannot find module '../../src/plugin/negativeYear' from 'negativeYear.test.js'\n`,
     "NOT-A-BEHAVIOUR-FIX"],
    ["a test that does not catch its own bug", 0, `Tests: 13 passed, 13 total`, "PASSED-AT-BASE"],
    ["pytest collection error", 1, `ImportError while importing test module 'tests/test_x.py'\nE   ModuleNotFoundError: No module named 'app.new'`, "NOT-A-BEHAVIOUR-FIX"],
    ["pytest assertion", 1, `    def test_total():\n>       assert total == 300\nE       assert 250 == 300`, "ASSERTION"],
    ["something this script cannot read", 1, `Segmentation fault (core dumped)`, "UNCLASSIFIED"],
  ];
  let bad = 0;
  for (const [name, code, out, want] of cases) {
    const got = classify(out, code).verdict;
    const ok = got === want;
    if (!ok) bad++;
    console.log(`  ${ok ? "ok  " : "FAIL"}  ${name.padEnd(44)} ${got}${ok ? "" : ` (wanted ${want})`}`);
  }
  console.log(`\n  ${cases.length - bad}/${cases.length} classified correctly`);
  if (bad) console.log("\n  The classifier is the whole gate. Fix it before trusting a green run.");
  process.exit(bad ? 1 : 0);
}

// ── the gate ────────────────────────────────────────────────────────────────────────────────────────
const BASE = process.env.BASE_SHA;
const HEAD = process.env.HEAD_SHA || "HEAD";
if (!BASE) {
  console.error("::error::BASE_SHA is not set, so there is no base commit to run against.");
  process.exit(1);
}

// The command that runs specific test files. Stack-specific, like the six gates in verify.mjs, and it fails
// loudly when absent rather than skipping — a gate that skips when unwired reports green for work nobody ran.
const pkg = existsSync("package.json") ? JSON.parse(readFileSync("package.json", "utf8")) : {};
const RUNNER = process.env.RED_ON_BASE_CMD || (pkg.scripts?.["test:file"] ? "bun run test:file" : null);
if (!RUNNER) {
  console.error('::error::No way to run a single test file. Add a "test:file" script to package.json:');
  console.error('  "test:file": "vitest run"      (or "jest", or "pytest -q")');
  console.error("It receives one or more test paths as arguments. Or set RED_ON_BASE_CMD.");
  console.error("This fails rather than skipping, because a gate that skips when unwired is the failure");
  console.error("it exists to catch.");
  process.exit(1);
}

const TEST_RE = /(\.test\.|\.spec\.|_test\.|(^|\/)(tests?|e2e|spec)\/)/;
// Only real test SOURCE files. Two exclusions, both learned by running this: `.evidence/` holds this
// gate's own stored proof, and those filenames contain ".test.js" — so without this the gate reads its
// own output back as a test and reports a verdict on it. And a fixture or snapshot named like a test is
// not a test.
const SOURCE_EXT = /\.(js|jsx|mjs|cjs|ts|tsx|mts|cts|py|rb|go|java|kt|cs|php)$/;
const NOT_A_TEST = /^\.evidence\/|^\.red-on-base-worktree\/|(^|\/)__snapshots__\/|\.snap$/;
const changed = sh("git", ["diff", "--name-status", "--diff-filter=AM", `${BASE}...${HEAD}`])
  .split("\n").filter(Boolean)
  .map((l) => l.split("\t"))
  .filter(([, p]) => p && TEST_RE.test(p) && SOURCE_EXT.test(p) && !NOT_A_TEST.test(p))
  .map(([status, p]) => ({ status, path: p }));

if (!changed.length) {
  console.log("No test files added or changed in this pull request. Nothing for this gate to prove.");
  process.exit(0);
}

console.log(`Running ${changed.length} changed test file(s) against ${BASE.slice(0, 9)} — the code before this change.\n`);

// A worktree, so the checkout cannot disturb the working copy CI is using. node_modules is not copied by
// git, so it is linked from the main tree: dependency changes inside the same pull request are a known
// limitation, reported rather than hidden.
const WT = ".red-on-base-worktree";
rmSync(WT, { recursive: true, force: true });
sh("git", ["worktree", "add", "--detach", "-f", WT, BASE]);
if (existsSync("node_modules")) {
  try { sh("ln", ["-s", join(process.cwd(), "node_modules"), join(WT, "node_modules")]); } catch { /* windows, or already there */ }
}

const results = [];
try {
  for (const { status, path } of changed) {
    // the test as this pull request writes it, against the code as it was before
    const content = sh("git", ["show", `${HEAD}:${path}`]);
    mkdirSync(join(WT, dirname(path)), { recursive: true });
    writeFileSync(join(WT, path), content);

    let out = "", code = 0;
    try {
      out = execFileSync("sh", ["-c", `${RUNNER} ${JSON.stringify(path)}`],
        { cwd: WT, encoding: "utf8", stdio: ["ignore", "pipe", "pipe"] });
    } catch (e) { code = e.status ?? 1; out = (e.stdout || "") + (e.stderr || ""); }

    const { verdict, why } = classify(out, code);
    results.push({ path, status, verdict, why, out });
    const icon = { ASSERTION: "✓", "NOT-A-BEHAVIOUR-FIX": "–", "PASSED-AT-BASE": "✗", UNCLASSIFIED: "?" }[verdict];
    console.log(`  ${icon} ${verdict.padEnd(20)} ${path}\n      ${why}`);
  }
} finally {
  sh("git", ["worktree", "remove", "--force", WT]);
}

// ── the proof, stored ───────────────────────────────────────────────────────────────────────────────
const dir = ".evidence/red-on-base";
mkdirSync(dir, { recursive: true });
for (const r of results) {
  writeFileSync(join(dir, r.path.replace(/[/\\]/g, "_") + ".txt"),
    `${r.path}\nbase: ${BASE}\nverdict: ${r.verdict}\n${r.why}\n\n${"-".repeat(70)}\n${r.out}`);
}
writeFileSync(join(dir, "summary.md"),
  `# Red-on-base against \`${BASE.slice(0, 9)}\`\n\n| | Test | Verdict | |\n|---|---|---|---|\n` +
  results.map((r) => `| ${r.status} | \`${r.path}\` | **${r.verdict}** | ${r.why} |`).join("\n") + "\n");

// ── the verdict ─────────────────────────────────────────────────────────────────────────────────────
const unclassified = results.filter((r) => r.verdict === "UNCLASSIFIED");
const passed = results.filter((r) => r.verdict === "PASSED-AT-BASE");
const proven = results.filter((r) => r.verdict === "ASSERTION");
const na = results.filter((r) => r.verdict === "NOT-A-BEHAVIOUR-FIX");

console.log(`\n${proven.length} proven by assertion · ${na.length} not a behaviour fix · ${passed.length} passed at base · ${unclassified.length} unclassified`);
console.log(`Proof stored in ${dir}/`);

if (unclassified.length) {
  console.error(`\n::error::${unclassified.length} test run(s) failed at base in a way this script cannot classify.`);
  unclassified.forEach((r) => console.error(`  ${r.path}`));
  console.error("Read the stored output. Then either extend LOAD_FAILURE/ASSERTION in this script — in its");
  console.error("own commit, because it is a gate — or say in the pull request why this case is different.");
  console.error("It fails rather than passing, because a gate that cannot tell must not guess.");
  process.exit(1);
}

// Passing at base is only a DEFECT when the change claims to fix something. A regression test that pins
// behaviour which already works is supposed to pass at base, and telling the two apart needs intent.
const declaresFix = /(^|\n)fix(\(|:)/i.test(sh("git", ["log", "--format=%s%n%b", `${BASE}..${HEAD}`]));
if (passed.length && declaresFix) {
  console.error(`\n::error::This change declares a fix, and ${passed.length} of its tests pass against the unfixed code.`);
  passed.forEach((r) => console.error(`  ${r.path}`));
  console.error("So those tests do not catch the thing being fixed. Either the test needs to assert the");
  console.error("behaviour that was actually wrong, or the fix is not the fix. This is the case the gate");
  console.error("exists for, and it is worth the interruption.");
  process.exit(1);
}
if (passed.length) {
  console.log(`\n::warning::${passed.length} test(s) pass against the base commit. Legitimate for a regression`);
  console.log("test pinning behaviour that already worked; not legitimate if it was meant to catch a defect.");
  console.log("Nothing in this change declared a fix, so this is a warning rather than a failure.");
}
console.log("\nRed-on-base satisfied.");
```
