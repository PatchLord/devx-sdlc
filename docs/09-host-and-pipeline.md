# Host configuration, and the pipeline

Everything that actually stops a bad merge lives on the host, not in the repository. This document is the
exact host setup — branch protection, secrets, environments — plus the two workflows that build an artefact
once and move it between environments. Read it when you are standing up a repository, and again when
something merged that should not have.

Every check described in [enforcement](06-enforcement.md) lives in a file inside the repository. That is
convenient, and it is also the whole problem: an agent with write access can edit any of those files, and so
can anybody in a hurry. The gates that matter are the ones the host refuses to merge without, and the host is
the one surface no commit can reach.

In the pilot, the repository's own `CLAUDE.md` asserted that branch protection was on. There was no remote.
CI had run zero times. Nothing in that repository lied — the sentence had been written down and never wired,
and writing it down was mistaken for having it. This document is the wiring.

```
+---------- the host: nothing in a commit reaches this ----------+
| branch protection on main        repository secrets            |
|   required contexts              PERIMETER_TOKEN               |
|   approvals and code owners      ANTHROPIC_API_KEY             |
|   linear history, no force push                                |
+---------------------------------^------------------------------+
                                  | gh api, Administration: read
+--------- the repository: an agent can edit every line ---------+
| perimeter.yml   asserts the box above, weekly                  |
| size gates spec verify review   the five required contexts     |
| deploy.yml promote.yml          build once, promote by id      |
| CODEOWNERS  CLAUDE.md  .claude/  scripts/                      |
+----------------------------------------------------------------+
```

## The settings on `main`, and what each one buys

These are the values, not a range to choose from. They were read back off a real protected repository, not
composed from the API docs.

| Setting | Value | Without it |
|---|---|---|
| `required_status_checks.contexts` | `size, gates, spec, verify, review` | the jobs run, report, and merging ignores them |
| `required_status_checks.strict` | `true` | a check that passed against a stale `main` counts as a pass against current `main` |
| `required_pull_request_reviews.required_approving_review_count` | `1` | anyone merges their own work with no second pair of eyes |
| `required_pull_request_reviews.require_code_owner_reviews` | `true` | `CODEOWNERS` is a text file with no effect |
| `required_pull_request_reviews.dismiss_stale_reviews` | `true` | approve, then push anything, then merge on the old approval |
| `required_linear_history.enabled` | `true` | `gates` and `spec` reason about a commit order nothing was tested in |
| `required_conversation_resolution.enabled` | `true` | a review finding can merge neither fixed nor dismissed |
| `allow_force_pushes.enabled` | `false` | the history every other check reasons about can be rewritten |
| `allow_deletions.enabled` | `false` | `main` can be deleted |
| `enforce_admins.enabled` | `true` | admins are exempt, and the perimeter holds only by consent |

Note what is absent from the required contexts: `scan`. It runs on a clock over the whole tree rather than on
a pull request, so it has no head commit to report against and cannot be a merge gate. That is a real hole —
a pull request can merge green while the repository carries an open critical alert — and the compensation is
that `scan` fails loudly on `main` the next morning. See [enforcement](06-enforcement.md) for the job.

Three settings need the argument spelled out, because they look like taste and are not.

**Linear history is a precondition, not a preference.** `gates.yml` walks `git rev-list --reverse --no-merges
BASE..HEAD` and asks of each commit whether it mixes a gate change with implementation. `spec.yml` asserts
the spec is the branch's *first* commit and alone in it. Both statements are about an order. Merge `main`
into a branch mid-flight and the sequence those two jobs walk is not a sequence anything was ever built or
tested in — the checks still pass or fail, but what they mean stops being what we claim. So this is not a
style rule with a check attached; it is the condition under which two of the five checks say anything true.

The cost is real. You merge by squash or rebase only, and contributors bring a branch up to date by rebasing
rather than merging. Rebasing rewrites the branch, which force-pushes it, which — with `dismiss_stale_reviews`
on — drops the approval you already had. On a busy repository the combination of `strict: true` and linear
history buys correctness at the price of a rebase-and-re-approve cycle. At our team sizes, two or three open
pull requests per repository, that costs minutes a week. At thirty concurrent branches it would not, and the
honest answer there is a merge queue, which we do not run yet.

**Conversation resolution is where the disposition rule becomes enforceable.** The rule from [the build
loop](04-build-loop.md) is that every review-agent finding gets a disposition — fixed, or dismissed in
writing. No workflow can enforce that, because a workflow cannot see whether you read a comment. The host
can: with `required_conversation_resolution` on, an open thread blocks the merge button. It is also what
makes the dismissal rate in [measurement](11-measurement.md) countable at all, because a dismissal becomes a
written act on a thread rather than a silence.

That matters because the review agent's accuracy is not settled. Across 19,450 pull requests (April 2026),
agent-only-reviewed PRs merged at 45.20% against 68.37% for human-only review, and 12 of 13 agents averaged
below a 60% signal ratio. Its findings are input. The gate is that you responded to them, not that you obeyed
them.

**`enforce_admins: true` is the one we will argue about.** On a two-person project it is genuinely defensible
to leave it `false`, because you will otherwise be locked out of your own repository at some point on a
Friday with no second admin to unlock it. Say what that costs: with admins exempt, every rule above becomes a
convention that the two people most able to bypass it have opted out of. `perimeter.yml` downgrades that
finding to a warning rather than a failure — deliberately, so the check does not cry wolf, and dangerously,
because warnings are read as green. If you leave it off, admin merges become a manual entry in the shortcut
count. An uncounted shortcut is invisible exactly when it matters.

### Setting it in the UI

Settings → Branches → Branch protection rules → Add classic branch protection rule. Branch name pattern
`main`. Then, in order:

- Require a pull request before merging → Require approvals: **1** → Dismiss stale pull request approvals
  when new commits are pushed → Require review from Code Owners
- Require status checks to pass before merging → Require branches to be up to date before merging → add
  `size`, `gates`, `spec`, `verify`, `review`
- Require conversation resolution before merging
- Require linear history
- Do not allow bypassing the above settings
- Leave Allow force pushes and Allow deletions unchecked

One gotcha stops you at the second bullet: a check context only appears in that search box after it has
reported on the repository at least once recently. On a fresh repository the five names do not exist, so you
cannot require them. That is why step 0 of the break-it suite below opens a throwaway pull request first.
Until the contexts are required by name they are decoration, and `perimeter.yml` will say so.

### Setting it with `gh api`

This is a full replacement `PUT`: any field you omit is cleared, and `required_status_checks`,
`enforce_admins`, `required_pull_request_reviews` and `restrictions` must all be present even when null. Run
it with your own admin credentials (`gh auth login`). `PERIMETER_TOKEN` is read-only and cannot do this, on
purpose.

```bash
REPO=devx/pulse   # owner/name

gh api -X PUT "repos/$REPO/branches/main/protection" \
  -H "Accept: application/vnd.github+json" \
  --input - <<'JSON'
{
  "required_status_checks": {
    "strict": true,
    "contexts": ["size", "gates", "spec", "verify", "review"]
  },
  "enforce_admins": true,
  "required_pull_request_reviews": {
    "required_approving_review_count": 1,
    "require_code_owner_reviews": true,
    "dismiss_stale_reviews": true
  },
  "restrictions": null,
  "required_linear_history": true,
  "required_conversation_resolution": true,
  "allow_force_pushes": false,
  "allow_deletions": false,
  "block_creations": false,
  "lock_branch": false,
  "allow_fork_syncing": false
}
JSON
```

Read it back with the same query the perimeter uses, so that when the two disagree you know the argument is
about repository files and not about the host:

```bash
gh api "repos/$REPO/branches/main/protection" | jq '{
  contexts:      .required_status_checks.contexts,
  strict:        .required_status_checks.strict,
  approvals:     .required_pull_request_reviews.required_approving_review_count,
  code_owners:   .required_pull_request_reviews.require_code_owner_reviews,
  dismiss_stale: .required_pull_request_reviews.dismiss_stale_reviews,
  linear:        .required_linear_history.enabled,
  conversations: .required_conversation_resolution.enabled,
  force_pushes:  .allow_force_pushes.enabled,
  deletions:     .allow_deletions.enabled,
  admins:        .enforce_admins.enabled
}'
```

Two notes on what is *not* in that body. There is no `require_last_push_approval`, which would stop an author
self-approving their own final push; `dismiss_stale_reviews` covers most of the same gap and the perimeter
does not assert it. And `contexts` is the older field — the newer `checks` array pins each check to an app
id, which `contexts` cannot. So any workflow in this repository that produces a status named `verify`
satisfies the requirement, including one that runs `exit 0`.

The rule we follow: **the `PUT` body and the perimeter's expected values are the same list.** Anything set on
the host but not asserted in the perimeter drifts silently, and a setting nobody checks is a setting nobody
has.

### GitHub has two protection systems, and the perimeter reads whichever answers

Classic branch protection answers `GET /repos/{owner}/{repo}/branches/main/protection`. A repository
configured with a **repository ruleset** instead returns 404 there while being fully protected. A perimeter
job that reads only the classic endpoint therefore reports "main has no branch protection at all" on a
correctly protected repository — a false alarm that reads exactly like the real thing, and the fastest way to
teach a team to ignore the check.

So `perimeter.yml` tries the classic endpoint, falls back to `/repos/{owner}/{repo}/rules/branches/main`, and
normalises both payloads into one shape before asserting anything. It prints which one answered. This was
verified against two real repositories in this org: one on classic protection, one on rulesets and 404ing on
the classic endpoint. Both now pass the same assertions.

The residual weakness is on the ruleset side. Whether anyone can bypass the rules lives in the ruleset's
`bypass_actors`, and the rules endpoint does not return it, so the perimeter emits a warning telling you to
check it by hand rather than asserting something it cannot see. A single bypass actor makes every assertion
advisory for that person. We use classic protection by default because the payload it returns is the payload
the table above documents.

The job itself, its full script and its comments are in [enforcement](06-enforcement.md). What it cannot see
is worth stating in one place, because "the perimeter passed" will otherwise be quoted as meaning more than
it does:

- It checks a context *named* `verify` is required. It cannot see what that job does.
- Ruleset bypass lists, and who holds admin, are invisible to it.
- It cannot see whether the required checks ran on the commit that actually landed. `strict: true` is the
  proxy, and it is a proxy.
- It runs Mondays at 07:00 and on pushes to `main` touching `.github/workflows/**`, `CODEOWNERS` or
  `CLAUDE.md`. A protection change made on Tuesday with no matching push is found up to six days later. If
  that window is too wide, the cron is one line: `0 7 * * *`.

## The two secrets, and the switches

Settings → Secrets and variables → Actions → New repository secret. Repository scope, not environment scope —
an environment secret is invisible to a job that does not name that environment, and the job behaves exactly
as if the secret were absent.

`PERIMETER_TOKEN` — a fine-grained personal access token scoped to this one repository, Repository
permissions → **Administration: Read-only**, nothing else. The workflow `GITHUB_TOKEN` cannot substitute: its
permission set has no administration scope, so it cannot read branch protection at all. **If this secret is
missing, `perimeter.yml` fails.** It does not skip. A perimeter check that skips when unconfigured is
precisely the failure it exists to catch. The weakness of a fine-grained PAT is that it belongs to a person:
when they leave, or when the token expires, the job goes red for a reason unrelated to the code. Red is the
correct failure direction, and the fix once you protect more than one repository is a GitHub App installation
token with `Administration: read`.

`ANTHROPIC_API_KEY` — used by `review.yml`, whose first step checks the key is present and fails with an
explanation before the review action runs. **If this secret is missing, `review` fails, and because `review`
is a required context, nothing merges.** That is a deliberate blast radius: an expired key stops the team. A
review job that skips quietly puts a green check on work nobody read, which is worse. If you decide you do
not want an agent review, the exit is two edits under `CODEOWNERS` — delete the job, and remove `review` from
the perimeter's expected list — so the repository stops claiming a review it does not perform.

Two host switches have no secret and are just as load-bearing. Settings → Advanced Security: turn on
Dependabot alerts and code scanning. `scan.yml` reads the host's alert state rather than running a scanner
itself, because the host has already scanned the whole history with a maintained ruleset and a check living
outside the repository is one an agent cannot quiet. If those switches are off, `scan` fails and says so
rather than reporting a clean tree it never looked at.

Finally, Settings → Environments: create `dev`, `uat` and `production`. On `production`, set required
reviewers and restrict deployment branches to `main`. That reviewer prompt is the human gate on promotion;
`promote.yml` names the environment and nothing else enforces it.

## Build once, promote

Two workflows. `deploy.yml` builds exactly one artefact per commit on `main` and puts it in dev. `promote.yml`
moves that same artefact to uat or production and never builds anything.

The identity of an artefact is the commit that produced it — the first 12 characters of `GITHUB_SHA`. Not a
counter, not a timestamp, not a semver tag applied later. The property we want is that given a running
environment you can get back to the source, in one step, with no lookup table. Every promotion record and
every release file in `docs/releases/` is keyed on that id.

`.github/workflows/deploy.yml`

```yaml
name: deploy

# Build once, promote the same artefact. This is the workflow that makes stage 03's exit criterion
# reachable: "one trivial page live in dev, put there by the real pipeline."
#
# The artefact is built exactly once, here, on a push to main, and tagged with the commit that
# produced it. Every later environment gets that same artefact by digest. Nothing is rebuilt per
# environment, because a rebuild makes the thing you tested and the thing you shipped two different
# things.
#
# The build and deploy STEPS are stack-specific and marked below. Everything around them - the
# identity of the artefact, the promotion record, the timestamps measurement number 6 needs - is not.

on:
  push:
    branches: [main]

permissions:
  contents: read
  packages: write
  id-token: write

concurrency:
  group: deploy-dev
  cancel-in-progress: false   # never cancel a deploy mid-flight

jobs:
  build:
    name: build once
    runs-on: arm64
    timeout-minutes: 25
    outputs:
      build_id: ${{ steps.id.outputs.build_id }}
    steps:
      - uses: actions/checkout@v4

      - name: Identify this build
        id: id
        run: |
          set -euo pipefail
          # The build id IS the commit. Not a counter, not a timestamp: given a running
          # environment you must be able to get back to the source that produced it.
          BUILD_ID="${GITHUB_SHA::12}"
          echo "build_id=$BUILD_ID" >> "$GITHUB_OUTPUT"
          echo "$BUILD_ID" > BUILD_ID
          echo "Build id: $BUILD_ID"

      - uses: oven-sh/setup-bun@v2
        with: { bun-version: latest }

      - run: bun install --frozen-lockfile

      # ── STACK-SPECIFIC: replace with your build. It must not read any environment's
      #    configuration. Anything inlined at build time makes promotion a lie. ──
      - name: Build
        run: bun run build

      - name: Package
        run: tar -czf artefact.tgz BUILD_ID $(bun run --silent build:artefact-paths 2>/dev/null || echo dist)

      - uses: actions/upload-artifact@v4
        with:
          name: build-${{ steps.id.outputs.build_id }}
          path: artefact.tgz
          retention-days: 30

  dev:
    name: deploy to dev
    needs: build
    runs-on: arm64
    timeout-minutes: 20
    environment:
      name: dev
    steps:
      - uses: actions/checkout@v4
      - uses: actions/download-artifact@v4
        with: { name: build-${{ needs.build.outputs.build_id }} }

      - name: Verify the artefact is the one we built
        run: |
          set -euo pipefail
          tar -xzf artefact.tgz
          [ "$(cat BUILD_ID)" = "${{ needs.build.outputs.build_id }}" ] \
            || { echo "::error::Artefact build id does not match the build that produced it."
                 echo "Do not deploy this. It means the artefact was rebuilt or swapped between the build"
                 echo "job and here, so what you would ship is not what was tested. Re-run the workflow"
                 echo "from the commit you intend to deploy."
                 exit 1; }

      # ── STACK-SPECIFIC: replace with your deploy. ──
      - name: Deploy
        run: echo "Deploying build ${{ needs.build.outputs.build_id }} to dev"

      - name: Record the promotion
        run: |
          set -euo pipefail
          # The "accepted work waiting to go live" number is computed from these lines. They cannot be reconstructed later,
          # which is why they are written at the moment of promotion rather than derived afterwards.
          printf '%s\t%s\t%s\t%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
            "${{ needs.build.outputs.build_id }}" "dev" "$GITHUB_RUN_ID" \
            | tee -a "$GITHUB_STEP_SUMMARY"
```

The line that carries the most weight is the comment on the build step: the build must not read any
environment's configuration. If an API base URL or a feature flag is inlined at build time, the artefact you
promote to production is not the artefact you tested in uat, and every claim in this section collapses.
Configuration is read at start-up from the environment, or promotion is a lie.

`.github/workflows/promote.yml`

```yaml
name: promote

# Moves an already-built artefact to uat or production. It never builds. If you find yourself
# wanting a build step here, the artefact you are promoting is not the artefact that was tested.
#
# Deliberately manual: promotion to production is a decision, and stage 06 says every decision that
# can be made before the launch window is made before it.

on:
  workflow_dispatch:
    inputs:
      build_id:
        description: "The 12-character build id to promote (from the deploy run you are promoting)"
        required: true
      to:
        description: "Target environment"
        required: true
        type: choice
        options: [uat, production]

permissions:
  contents: read
  actions: read

jobs:
  promote:
    name: promote ${{ inputs.build_id }} to ${{ inputs.to }}
    runs-on: arm64
    timeout-minutes: 20
    environment:
      name: ${{ inputs.to }}    # required reviewers on this environment are the gate
    steps:
      - uses: actions/checkout@v4

      - name: Fetch the exact artefact that was tested
        uses: actions/download-artifact@v4
        with:
          name: build-${{ inputs.build_id }}
          github-token: ${{ secrets.GITHUB_TOKEN }}
          run-id: ${{ github.event.inputs.run_id || github.run_id }}
        continue-on-error: true

      - name: The artefact must exist and match
        run: |
          set -euo pipefail
          if [ ! -f artefact.tgz ]; then
            echo "::error::No artefact found for build ${{ inputs.build_id }}."
            echo "You cannot promote a build that was never produced by the pipeline. If the artefact"
            echo "has aged out of retention, the honest move is to rebuild from that commit, redeploy"
            echo "to dev, and re-test - not to promote something new under an old build id."
            exit 1
          fi
          tar -xzf artefact.tgz
          [ "$(cat BUILD_ID)" = "${{ inputs.build_id }}" ] \
            || { echo "::error::Artefact contents do not match the requested build id."; exit 1; }

      - name: Production requires a signed release checklist
        if: inputs.to == 'production'
        env:
          BUILD_ID: ${{ inputs.build_id }}
        run: |
          set -euo pipefail
          F="docs/releases/$BUILD_ID.md"
          [ -f "$F" ] || { echo "::error::$F is missing. Stage 05 says a production release carries a dated checklist with evidence links."; exit 1; }

          # A row with BOTH cells blank — a checklist filed with the awkward rows left empty.
          # Applies to every table in the file, including the two- and three-column ones.
          if grep -qiE '^\|[^|]*\|[[:space:]]*\|[[:space:]]*\|' "$F"; then
            echo "::error::$F has rows with both the verification and evidence columns empty."
            echo "Fill in how each line was verified and link the evidence, or waive the line in writing"
            echo "with a named person against it. An honest waiver is worth more than a false tick, and"
            echo "an empty cell is neither."
            exit 1
          fi

          # Then every Verification row's EVIDENCE cell specifically. The check above only fires when the
          # verification cell is blank too, so `| Rollback tested | verified | |` passed it: the word
          # "verified" with nothing behind it, which is precisely what the third column exists to prevent
          # and what the template, docs/03-delivery.md and docs/18-outcomes.md all name in prose. It
          # caught the lazy filer and waved the dishonest one through, which is inverted. Found by
          # turning an outside standard's exposure-grading lens back on this file, and confirmed by
          # running it: the break-it case in docs/09 that prescribes "one row's evidence column left
          # blank, confirm it still refuses" went green.
          # Table shape is fixed by docs/08-templates.md: | Item | How it was verified | Evidence |
          BAD=$(awk -F'|' '
            /^## Verification/ { inv = 1; next }
            /^## /             { inv = 0 }
            inv && /^\|/ {
              if ($0 ~ /^\|[[:space:]]*-+/)              next   # the --- separator
              if ($2 ~ /^[[:space:]]*Item[[:space:]]*$/) next   # the header row
              rows++
              ev = $4; gsub(/[[:space:]]/, "", ev)
              if (ev == "") print "  " $0
            }
            END { if (rows == 0) print "  (no Verification rows found — has the section been renamed or removed?)" }
          ' "$F")

          if [ -n "$BAD" ]; then
            echo "::error::$F has Verification rows with an empty Evidence column."
            printf '%s\n' "$BAD"
            echo ""
            echo "A word in the middle column is a claim; the third column is what makes it checkable."
            echo "Name the artefact — a test name, a screenshot path, a query output, a run URL. If a line"
            echo "genuinely could not be verified, waive it in writing with a named person against it."
            echo "A waiver is a decision. An empty cell is nobody having made one."
            exit 1
          fi

      # ── STACK-SPECIFIC: replace with your deploy. Same artefact, different target. ──
      - name: Deploy
        run: echo "Promoting ${{ inputs.build_id }} to ${{ inputs.to }}"

      - name: Record the promotion
        run: |
          printf '%s\t%s\t%s\t%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
            "${{ inputs.build_id }}" "${{ inputs.to }}" "$GITHUB_RUN_ID" \
            | tee -a "$GITHUB_STEP_SUMMARY"
```

**Why promote has no build step.** A build step here would produce a second artefact from the same source and
call it the same release. It would not be the same release. Compilers are not bit-for-bit deterministic
across runner images, lockfile resolution can drift, and a base image tag moves. Every one of those turns
"we tested this in uat" into "we tested something very like this". If you catch yourself adding a build to
this file, what you actually want is a redeploy to dev from the current commit, followed by a fresh test pass.

**Why production refuses an unsigned release.** The checklist step is the only place in the pipeline where a
human's written statement is a merge-equivalent gate. It requires `docs/releases/<build_id>.md` to exist —
copied from the template in [templates](08-templates.md) — and it makes two passes. First, any table row with
*both* the verification and evidence columns blank is refused, anywhere in the file. Then, inside the
`## Verification` section specifically, **every row's evidence cell must be non-empty**, and a missing
`## Verification` section counts as a failure rather than as nothing to check.

The check is crude on purpose: it matches empty cells, not content, so it cannot tell a real evidence link
from the word "yes". The second pass is where that crudeness boundary now sits — a claim in the middle column
with an empty third column is refused, and what the third column *says* is still not parsed. A written waiver
makes a perfectly good evidence cell, because a waiver is a decision and an empty cell is nobody having made
one.

**This gate was wrong for its whole life until 6 August 2026, and the fix is worth reading as a warning.** The
original was one regex requiring four pipes with cells two and three both whitespace-only — an AND, where
every sentence describing it said OR. So `| Rollback tested | verified | |` passed the production gate: the
word "verified" with nothing behind it, which is exactly the failure the third column exists to prevent and
which [delivery](03-delivery.md), [outcomes](18-outcomes.md) and [the first run](19-first-run.md) all name in
prose. It caught the careless filer and waved the dishonest one through, which is inverted. Worse, break-it
case 6 below prescribes *"add the file with one row's evidence column left blank, and confirm it still
refuses"* — followed literally on an otherwise-complete file, that went green, so the one prescribed proof of
the last gate before production exposure could never have reproduced. Two tier-3 sentences knew about the
failure; the tier-1 gate that claimed to catch it did not.

**Two known weaknesses, stated plainly.** First, the download step names no deploy run: `run-id` falls back
to `github.run_id`, which is the promote run itself, so on GitHub's default artifact scoping it finds nothing
and the next step is what speaks. That is why the download is `continue-on-error`. To promote across runs, add
a `run_id` input to the dispatch and pass the deploy run's id. Most teams need that edit on day one; make it
before the first uat promotion, not during it. Second, retention is 30 days. A build older than that cannot
be promoted, and the correct response is the one the error message gives: rebuild from that commit, redeploy
to dev, re-test. Do not ship something new under an old id.

The tab-separated promotion records exist because the elapsed time from client acceptance to production in
[measurement](11-measurement.md) is computed from them, and they cannot be reconstructed once the runs age
out. They are written at the moment of promotion for that reason alone.

## Proving the logic first, offline

The suite below is the authority, because only the host can show that a red check blocks a merge. But it
needs a remote, a runner and five pull requests, so in practice it runs once at setup and never again —
which leaves the *logic* inside each gate untested for the rest of a project's life. Every defect found in
these checks so far has been logic, not configuration.

`scripts/break-it.mjs` does the offline half in seconds. Each case builds a throwaway git repository, runs
the gate's real script against it, and asserts the verdict — including the legal version of the same
change, which is the half that proves a check discriminates rather than merely refuses.

Run it before the host suite. It is free, it is repeatable, and it catches the class of defect that would
otherwise cost you five pull requests to discover.

```bash
node scripts/break-it.mjs          # every case
node scripts/break-it.mjs size     # one gate
node scripts/break-it.mjs -v       # with each script's output
```

Three cases in it are regressions for defects that shipped and were found later: substring path matching
that classified `src/attestation.ts` as a test, a suppression rule that failed the very commit introducing
it, and a `size-override` an author could grant themselves. A fourth was found by writing the harness —
the pathspec exclusions used `**/bun.lockb` without `glob` magic, so a lockfile at the repository root was
never excluded and every dependency change counted thousands of lines against the ceiling.

It reads each `run:` block out of the workflow YAML rather than keeping a copy, and refuses to run if a
workflow grows a `${{ }}` expression or an `env:` entry it cannot supply. A harness testing a drifted copy
is worse than no harness, because it reports green about code that is not shipping.

**What it cannot prove, and must not be allowed to stand in for:** that a red check blocks a merge, that
code-owner review is enforced, that force-pushes are refused, that stale approvals are dismissed, or that
these files are valid Actions YAML. Those are host facts. Run the suite below as well.

```javascript
#!/usr/bin/env node
// Proves the gates reject what they claim to reject, offline, in seconds.
//
// docs/09-host-and-pipeline.md has a break-it suite that runs against a real repository. It is the
// authority, because only the host can prove a red check actually blocks a merge. But it needs a remote,
// a runner and five pull requests, so it gets run once at setup and never again — which means the LOGIC
// inside each gate goes untested for the rest of the project's life.
//
// This does the offline half. Each case builds a throwaway git repository, runs the gate's real script
// against it, and asserts the verdict. Every defect found in these checks so far has been logic:
// substring path matching that classified src/attestation.ts as a test, a suppression check that failed
// its own commit, an override anyone could grant themselves. All three are regression cases below.
//
//   node scripts/break-it.mjs            # run everything
//   node scripts/break-it.mjs spec       # one workflow
//   node scripts/break-it.mjs -v         # show each script's output
//
// What this CANNOT prove, and do not let it stand in for: that a red check blocks a merge, that
// code-owner review is enforced, that force-pushes are rejected, that stale reviews are dismissed, or
// that these workflows are even valid Actions YAML. Those live on the host. Run the real suite too.

import { execFileSync } from "node:child_process";
import { mkdtempSync, writeFileSync, readFileSync, mkdirSync, rmSync, appendFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, dirname } from "node:path";

const ROOT = new URL("..", import.meta.url).pathname;
const only = process.argv.slice(2).filter((a) => !a.startsWith("-"))[0];
const VERBOSE = process.argv.includes("-v");

// ── extracting the script the workflow actually runs ────────────────────────────────────────────────
// Read the `run:` block out of the YAML rather than keeping a copy here. A copy drifts, and a harness
// testing a drifted copy is worse than no harness — it reports green about code that is not shipping.
function extractRun(workflow, stepName) {
  const lines = readFileSync(join(ROOT, ".github/workflows", workflow), "utf8").split("\n");
  const at = lines.findIndex((l) => l.trim() === `- name: ${stepName}`);
  if (at === -1) throw new Error(`${workflow}: no step named "${stepName}"`);
  const start = lines.findIndex((l, i) => i > at && /^\s*run: \|\s*$/.test(l));
  if (start === -1) throw new Error(`${workflow}/${stepName}: no "run: |" block`);

  // The step's own `env:` block, because that is how a workflow is supposed to receive anything
  // attacker-controlled — a branch name interpolated into the script body is a command-injection hole.
  // Modelling env here means the harness tests the same composition CI does, and a newly added variable
  // fails loudly rather than arriving undefined.
  const envAt = lines.findIndex((l, i) => i > at && i < start && /^\s*env:\s*$/.test(l));
  const stepEnv = {};
  if (envAt !== -1) {
    const envIndent = lines[envAt].match(/^\s*/)[0].length;
    for (let i = envAt + 1; i < start; i++) {
      const m = lines[i].match(/^(\s*)([A-Za-z_][A-Za-z0-9_]*):\s*(.+)$/);
      if (!m || m[1].length <= envIndent) break;
      stepEnv[m[2]] = m[3].trim();
    }
  }
  const indent = lines[start].match(/^\s*/)[0].length + 2;
  const body = [];
  for (let i = start + 1; i < lines.length; i++) {
    if (lines[i].trim() === "") { body.push(""); continue; }
    if (lines[i].match(/^\s*/)[0].length < indent) break;
    body.push(lines[i].slice(indent));
  }
  let script = body.join("\n");

  // The only substitution allowed: GitHub expressions we can supply from the environment. Anything else
  // remaining means the workflow grew an expression this harness does not model, and pretending
  // otherwise would test a fiction — so it fails loudly instead.
  const subs = {
    "github.event.pull_request.base.sha": "$BASE_SHA",
    "github.event.pull_request.head.sha": "$HEAD_SHA",
    "github.event.pull_request.head.ref": "$HEAD_REF",
  };
  for (const [expr, val] of Object.entries(subs)) {
    script = script.split(`\${{ ${expr} }}`).join(val);
  }
  const leftover = script.match(/\$\{\{[^}]*\}\}/);
  if (leftover) {
    throw new Error(
      `${workflow}/${stepName}: unmodelled expression ${leftover[0]}.\n` +
      `Add it to the subs map in break-it.mjs, or this harness is testing something the workflow does not do.`);
  }
  return { script, stepEnv };
}

// Which env values the harness can supply itself. Anything else in a step's env block has to be given by
// the case, and if neither can supply it the run is aborted rather than executed with it undefined.
const RESOLVE = {
  "${{ github.event.pull_request.base.sha }}": (r) => r.BASE_SHA,
  "${{ github.event.pull_request.head.sha }}": (r) => r.HEAD_SHA,
  "${{ github.event.pull_request.head.ref }}": (r) => r.HEAD_REF,
};

// ── a throwaway repository ──────────────────────────────────────────────────────────────────────────
const git = (cwd, ...a) => execFileSync("git", a, { cwd, encoding: "utf8", stdio: ["ignore", "pipe", "pipe"] });

function build({ branch = "PULSE-142-thing", baseFiles = {}, commits = [] }) {
  const dir = mkdtempSync(join(tmpdir(), "breakit-"));
  git(dir, "init", "-q", "-b", "main");
  git(dir, "config", "user.email", "t@example.com");
  git(dir, "config", "user.name", "Test");
  write(dir, { "README.md": "base\n", ...baseFiles });
  git(dir, "add", "-A");
  git(dir, "commit", "-qm", "base");
  const BASE_SHA = git(dir, "rev-parse", "HEAD").trim();

  git(dir, "checkout", "-q", "-b", branch);
  for (const c of commits) {
    if (c.delete) for (const f of c.delete) git(dir, "rm", "-q", f);
    if (c.files) write(dir, c.files);
    git(dir, "add", "-A");
    git(dir, "commit", "-qm", c.message);
  }
  return { dir, BASE_SHA, HEAD_SHA: git(dir, "rev-parse", "HEAD").trim(), HEAD_REF: branch };
}

function write(dir, files) {
  for (const [p, content] of Object.entries(files)) {
    mkdirSync(dirname(join(dir, p)), { recursive: true });
    writeFileSync(join(dir, p), content);
  }
}

// ── running one case ────────────────────────────────────────────────────────────────────────────────
const results = [];

function check(name, { script, stepEnv = {}, repo, env = {}, expect, contains, stubGh = null }) {
  // Resolve the step's declared env, then let the case override. Whatever neither can supply is fatal:
  // a script running with an undefined input tests nothing and passes suspiciously often.
  const resolved = {};
  const unresolved = [];
  for (const [k, expr] of Object.entries(stepEnv)) {
    if (RESOLVE[expr]) resolved[k] = RESOLVE[expr](repo);
    else if (!(k in env)) unresolved.push(`${k}: ${expr}`);
  }
  if (unresolved.length) {
    throw new Error(`${name}: cannot supply step env — ${unresolved.join(", ")}.\n` +
      `Either add it to RESOLVE, or set it in the case's env so the value is deliberate.`);
  }
  const bin = join(repo.dir, ".stub");
  if (stubGh) {
    mkdirSync(bin, { recursive: true });
    writeFileSync(join(bin, "gh"), `#!/bin/sh\n${stubGh}\n`, { mode: 0o755 });
  }
  const scriptPath = join(repo.dir, ".break-it.sh");
  writeFileSync(scriptPath, script);
  const out = join(repo.dir, ".gh-output");
  writeFileSync(out, "");

  let stdout = "", code = 0;
  try {
    stdout = execFileSync("bash", [scriptPath], {
      cwd: repo.dir, encoding: "utf8", stdio: ["ignore", "pipe", "pipe"],
      env: {
        ...process.env,
        PATH: stubGh ? `${bin}:${process.env.PATH}` : process.env.PATH,
        BASE_SHA: repo.BASE_SHA, HEAD_SHA: repo.HEAD_SHA, HEAD_REF: repo.HEAD_REF,
        GITHUB_OUTPUT: out, GITHUB_ENV: join(repo.dir, ".gh-env"), ...resolved, ...env,
      },
    });
  } catch (e) {
    code = e.status ?? 1;
    stdout = (e.stdout || "") + (e.stderr || "");
  }

  const verdict = code === 0 ? "pass" : "fail";
  const ok = verdict === expect && (!contains || stdout.includes(contains));
  results.push({ name, expect, verdict, ok,
    why: ok ? "" : verdict !== expect ? `expected the gate to ${expect}, it ${verdict}ed`
                                      : `missing expected message: "${contains}"` });
  if (VERBOSE || !ok) console.log(`\n─── ${name} (${verdict}, wanted ${expect})\n${stdout.trim()}\n`);
  const written = readFileSync(out, "utf8");
  rmSync(repo.dir, { recursive: true, force: true });
  return written;
}

// ═══ spec.yml ═══════════════════════════════════════════════════════════════════════════════════════
if (!only || only === "spec") {
  const first = extractRun("spec.yml", "The spec exists, and it came first");
  const revised = extractRun("spec.yml", "A spec revised mid-flight is visible");
  const SPEC = "docs/specs/PULSE-142.md";
  const spec = { [SPEC]: "# PULSE-142\n\nA spec.\n" };
  const impl = { "src/thing.ts": "export const thing = 1;\n" };

  check("spec: a branch with no ticket id is rejected before anything else", {
    ...first, expect: "fail", contains: "does not start with a ticket id",
    repo: build({ branch: "fix-thing", commits: [{ files: spec, message: "docs: spec" }] }),
  });

  check("spec: no spec file for the ticket", {
    ...first, expect: "fail", contains: "Run /spec PULSE-142 before implementing",
    repo: build({ commits: [{ files: impl, message: "feat: no spec anywhere" }] }),
  });

  check("spec: the spec is the second commit", {
    ...first, expect: "fail", contains: "first commit must be the spec alone",
    repo: build({ commits: [{ files: impl, message: "feat: code first" }, { files: spec, message: "docs: spec after" }] }),
  });

  check("spec: the first commit is the spec plus something else", {
    ...first, expect: "fail", contains: "first commit must be the spec alone",
    repo: build({ commits: [{ files: { ...spec, ...impl }, message: "docs+feat together" }] }),
  });

  check("spec: spec first, then implementation — the legal ordering", {
    ...first, expect: "pass", contains: "The spec is the first commit",
    repo: build({ commits: [{ files: spec, message: "docs: spec" }, { files: impl, message: "feat: thing" }] }),
  });

  check("spec: a spec revised after implementation began warns, and does not block", {
    ...revised, expect: "pass", contains: "spec changed after implementation began",
    repo: build({ commits: [
      { files: spec, message: "docs: spec" },
      { files: impl, message: "feat: thing" },
      { files: { [SPEC]: "# PULSE-142\n\nRevised.\n" }, message: "docs: revise the spec" }] }),
  });
}

// ═══ gates.yml — the mixing check ═══════════════════════════════════════════════════════════════════
if (!only || only === "gates") {
  const mixing = extractRun("gates.yml", "No commit mixes a gate change with implementation");
  const wf = { ".github/workflows/size.yml": "name: size\n# a workflow\n" };
  const src = { "src/two.ts": "export const two = 2;\n" };

  check("gates: a workflow edit and source in one commit", {
    ...mixing, expect: "fail", contains: "mixes a gate change with implementation",
    repo: build({ baseFiles: wf, commits: [{ files: { ...wf, ".github/workflows/size.yml": "name: size\n# edited\n", ...src }, message: "chore: touch a gate and source" }] }),
  });

  check("gates: the same change split into two commits — must discriminate, not just refuse", {
    ...mixing, expect: "pass", contains: "gate-only change",
    repo: build({ baseFiles: wf, commits: [
      { files: { ".github/workflows/size.yml": "name: size\n# edited\n" }, message: "chore: the gate change alone" },
      { files: src, message: "feat: the source alone" }] }),
  });

  check("gates: CLAUDE.md and source in one commit", {
    ...mixing, expect: "fail", contains: "mixes a gate change with implementation",
    repo: build({ baseFiles: { "CLAUDE.md": "rules\n" }, commits: [{ files: { "CLAUDE.md": "rules\nmore\n", ...src }, message: "chore: rules and code" }] }),
  });

  check("gates: a NEW test added with the code it covers is implementation, and passes", {
    ...mixing, expect: "pass",
    repo: build({ commits: [{ files: { ...src, "src/two.test.ts": "test('two', () => {});\n" }, message: "feat: code and its new test" }] }),
  });

  check("gates: an EXISTING test modified alongside code is a gate change, and fails", {
    ...mixing, expect: "fail", contains: "mixes a gate change with implementation",
    repo: build({ baseFiles: { "src/two.test.ts": "test('two', () => { expect(2).toBe(2); });\n" },
      commits: [{ files: { ...src, "src/two.test.ts": "test('two', () => {});\n" }, message: "feat: code, and loosen its test" }] }),
  });

  check("gates: an existing test deleted alongside code fails", {
    ...mixing, expect: "fail", contains: "mixes a gate change with implementation",
    repo: build({ baseFiles: { "src/two.test.ts": "test('two', () => {});\n" },
      commits: [{ files: src, delete: ["src/two.test.ts"], message: "feat: code, and delete its test" }] }),
  });

  // Regression. With substring matching (*test*|*spec*) attestation.ts reads as a test; modified, it
  // would be classed as a gate change, both paths would land in the gate bucket, and the commit would
  // PASS while smuggling source into a gate-only commit.
  check("gates: REGRESSION — src/attestation.ts is source, not a test", {
    ...mixing, expect: "fail", contains: "mixes a gate change with implementation",
    repo: build({ baseFiles: { "src/attestation.ts": "export const a = 1;\n", ...wf },
      commits: [{ files: { "src/attestation.ts": "export const a = 2;\n", ".github/workflows/size.yml": "name: size\n# edited\n" }, message: "chore: gate plus attestation" }] }),
  });

  check("gates: REGRESSION — src/specification.ts is source, not a spec file", {
    ...mixing, expect: "fail", contains: "mixes a gate change with implementation",
    repo: build({ baseFiles: { "src/specification.ts": "export const s = 1;\n", "CODEOWNERS": "* @team\n" },
      commits: [{ files: { "src/specification.ts": "export const s = 2;\n", "CODEOWNERS": "* @team\n# edited\n" }, message: "chore: owners plus specification" }] }),
  });

  // Reproduces a real commit from a live project: feat(us2), 69 files, and four accessibility rules
  // turned off in biome.json in the same commit. One of them was noLabelWithoutControl, and the defect
  // it exists to catch was fixed nineteen days later. This is the shape gates.yml has to reject.
  check("gates: REGRESSION — a lint rule turned off inside a feature commit", {
    ...mixing, expect: "fail", contains: "mixes a gate change with implementation",
    repo: build({
      baseFiles: { "biome.json": '{ "linter": { "rules": { "a11y": { "noLabelWithoutControl": "error" } } } }\n' },
      commits: [{ files: {
        "biome.json": '{ "linter": { "rules": { "a11y": { "noLabelWithoutControl": "off" } } } }\n',
        "src/masters/list.tsx": "export const List = () => null;\n",
        "src/masters/form.tsx": "export const Form = () => null;\n",
      }, message: "feat(us2): six masters — REST API + React UI, wired end-to-end" }] }),
  });

  check("gates: the same lint change on its own commit passes, and is visible", {
    ...mixing, expect: "pass", contains: "gate-only change",
    repo: build({
      baseFiles: { "biome.json": '{ "linter": { "rules": { "a11y": { "noLabelWithoutControl": "error" } } } }\n' },
      commits: [
        { files: { "biome.json": '{ "linter": { "rules": { "a11y": { "noLabelWithoutControl": "off" } } } }\n' },
          message: "chore(lint): turn off noLabelWithoutControl — see DEFERRED entry" },
        { files: { "src/masters/list.tsx": "export const List = () => null;\n" }, message: "feat: the masters list" },
      ] }),
  });

  check("gates: source alone, no gate touched, passes", {
    ...mixing, expect: "pass", contains: "No commit mixes a gate change",
    repo: build({ commits: [{ files: src, message: "feat: just code" }] }),
  });
}

// ═══ gates.yml — the suppression check ══════════════════════════════════════════════════════════════
if (!only || only === "suppress") {
  const sup = extractRun("gates.yml", "No check was suppressed");
  const wfBase = { ".github/workflows/verify.yml": "name: verify\njobs:\n  verify:\n    steps:\n      - run: bun test\n" };

  check("suppress: a workflow gaining continue-on-error", {
    ...sup, expect: "fail", contains: "turns a gate into a decoration",
    repo: build({ baseFiles: wfBase, commits: [{ files: { ".github/workflows/verify.yml": wfBase[".github/workflows/verify.yml"] + "        continue-on-error: true\n" }, message: "ci: tolerate failure" }] }),
  });

  check("suppress: a workflow gaining 'if: false'", {
    ...sup, expect: "fail", contains: "turns a gate into a decoration",
    repo: build({ baseFiles: wfBase, commits: [{ files: { ".github/workflows/verify.yml": wfBase[".github/workflows/verify.yml"] + "    if: false\n" }, message: "ci: switch it off" }] }),
  });

  check("suppress: a step ending in '|| true'", {
    ...sup, expect: "fail", contains: "unable to fail",
    repo: build({ baseFiles: wfBase, commits: [{ files: { ".github/workflows/verify.yml": wfBase[".github/workflows/verify.yml"] + "      - run: bun run lint || true\n" }, message: "ci: quiet the linter" }] }),
  });

  // Regression. The naive version of the || true rule failed the very commit that introduced it,
  // because this workflow uses the command-substitution idiom three times.
  check("suppress: REGRESSION — '|| true' inside a command substitution is the normal idiom, and passes", {
    ...sup, expect: "pass",
    repo: build({ baseFiles: wfBase, commits: [{ files: { ".github/workflows/verify.yml": wfBase[".github/workflows/verify.yml"] + "      - run: X=$(grep -c foo bar || true)\n" }, message: "ci: count without tripping set -e" }] }),
  });

  check("suppress: a test newly marked .skip(", {
    ...sup, expect: "fail", contains: "Tests were skipped rather than fixed",
    repo: build({ baseFiles: { "src/a.test.ts": "test('a', () => {});\n" },
      commits: [{ files: { "src/a.test.ts": "test.skip('a', () => {});\n" }, message: "test: skip the awkward one" }] }),
  });

  check("suppress: an ordinary change touching no workflow and skipping nothing", {
    ...sup, expect: "pass",
    repo: build({ commits: [{ files: { "src/b.ts": "export const b = 2;\n" }, message: "feat: b" }] }),
  });
}

// ═══ size.yml ═══════════════════════════════════════════════════════════════════════════════════════
if (!only || only === "size") {
  const measure = extractRun("size.yml", "Measure the diff");
  const enforce = extractRun("size.yml", "Enforce the ceiling");
  const pad = (n, name = "src/pad.ts") => ({ [name]: Array.from({ length: n }, (_, i) => `export const pad${i} = ${i};`).join("\n") + "\n" });

  // measure writes files= and lines= to GITHUB_OUTPUT; enforce reads them from env. Run both, threading
  // the values across exactly as Actions does, so the two steps are tested as they actually compose.
  const sized = (n, opts = {}) => {
    const repo = build({ commits: [{ files: pad(n), message: `feat: ${n} lines` }], ...opts.build });
    const dir = repo.dir;
    const out = check(`size: measuring ${n} lines`, { ...measure, repo: { ...repo, dir }, expect: "pass" });
    results.pop(); // the measure step is plumbing, not a case
    const kv = Object.fromEntries(out.trim().split("\n").filter(Boolean).map((l) => l.split("=")));
    return kv;
  };

  const runEnforce = (name, { lines, files, expect, contains, env = {}, stubGh }) =>
    check(name, { ...enforce, repo: build({ commits: [{ files: { "src/x.ts": "x\n" }, message: "x" }] }),
      env: { LINES: String(lines), FILES: String(files), OVERRIDE: "false", AUTHOR: "dev",
             PR: "1", REPO: "acme/demo", GH_TOKEN: "x", ...env },
      expect, contains, stubGh });

  const big = sized(500);
  results.push({ name: "size: 500 added lines are measured as 500", expect: "pass",
    verdict: big.lines === "500" ? "pass" : "fail", ok: big.lines === "500",
    why: big.lines === "500" ? "" : `measured ${big.lines} lines, expected 500` });

  const lock = (() => {
    const repo = build({ commits: [{ files: { "bun.lockb": "x\n".repeat(5000), "src/x.ts": "export const x = 1;\n" }, message: "chore: lockfile" }] });
    const out = check("size: lockfile measurement", { ...measure, repo, expect: "pass" });
    results.pop();
    return Object.fromEntries(out.trim().split("\n").filter(Boolean).map((l) => l.split("=")));
  })();
  results.push({ name: "size: a 5,000-line lockfile is excluded from the count", expect: "pass",
    verdict: lock.lines === "1" ? "pass" : "fail", ok: lock.lines === "1",
    why: lock.lines === "1" ? "" : `measured ${lock.lines} lines, expected 1 — the exclusion list is not working` });

  runEnforce("size: over the ceiling with no override", { lines: 500, files: 1, expect: "fail", contains: "exceeds the ceiling of 400 lines" });
  runEnforce("size: over the target but under the ceiling passes with a warning", { lines: 350, files: 1, expect: "pass", contains: "over the 300/10 target" });
  runEnforce("size: comfortably small passes quietly", { lines: 40, files: 2, expect: "pass", contains: "Within the ceiling" });
  runEnforce("size: over on file count alone fails", { lines: 100, files: 25, expect: "fail", contains: "exceeds the ceiling" });

  runEnforce("size: override applied by a tech lead is allowed, and recorded", {
    lines: 500, files: 1, env: { OVERRIDE: "true", AUTHOR: "dev" }, expect: "pass", contains: "overridden by lead",
    stubGh: `echo '"lead"' | tr -d '"'`,
  });

  // The defect this was written for: an override you grant yourself is a bypass.
  runEnforce("size: REGRESSION — an override the author applied to their own pull request is a bypass", {
    lines: 500, files: 1, env: { OVERRIDE: "true", AUTHOR: "dev" }, expect: "fail", contains: "That is a bypass, not an override",
    stubGh: `echo dev`,
  });

  runEnforce("size: override label with no labelling event fails rather than passing", {
    lines: 500, files: 1, env: { OVERRIDE: "true", AUTHOR: "dev" }, expect: "fail", contains: "cannot tell who applied it",
    stubGh: `echo ""`,
  });
}

// ═══ promote.yml — the release checklist ════════════════════════════════════════════════════════════
// The only place in the pipeline where a human's written statement is a merge-equivalent gate, which
// makes it the one most worth testing. Its original check fired only when BOTH the verification and
// evidence cells were blank, so it caught the lazy filer and passed the dishonest one.
if (!only || only === "promote") {
  const checklist = extractRun("promote.yml", "Production requires a signed release checklist");
  const HEAD = `# Release 0123456789ab\n\n## What is in it\n\n| Ticket | What it does | Evidence |\n| --- | --- | --- |\n| PULSE-1 | returns form | PR #12 |\n\n## Verification\n\n| Item | How it was verified | Evidence |\n| --- | --- | --- |\n`;
  const TAIL = `\n## What this release does not verify\n\nSafari.\n`;
  const release = (rows) => ({ "docs/releases/0123456789ab.md": HEAD + rows + TAIL });
  const promote = (name, rows, expect, contains) => check(name, {
    ...checklist, env: { BUILD_ID: "0123456789ab" }, expect, contains,
    repo: build({ commits: [{ files: release(rows), message: "docs: release" }] }),
  });

  check("promote: no release file at all is refused", {
    ...checklist, env: { BUILD_ID: "0123456789ab" }, expect: "fail", contains: "is missing",
    repo: build({ commits: [{ files: { "src/x.ts": "x\n" }, message: "feat: x" }] }),
  });

  promote("promote: a row with both cells blank is refused",
    "| Rollback tested, not assumed | | |\n", "fail", "both the verification and evidence columns empty");

  // The defect. This shape passed the production gate: a claim with nothing behind it.
  promote("promote: REGRESSION — 'verified' with an empty Evidence cell is refused",
    "| Rollback tested, not assumed | verified | restore log |\n| Migrations run forward on a copy of prod data | verified | |\n",
    "fail", "empty Evidence column");

  promote("promote: 'n/a' with an empty Evidence cell is refused too",
    "| Rollback tested, not assumed | n/a | |\n", "fail", "empty Evidence column");

  promote("promote: every Verification row carrying evidence goes through",
    "| Rollback tested, not assumed | restored to staging | restore-2026-08-06.log |\n| Migrations run forward on a copy of prod data | ran on a dump | run #4412 |\n",
    "pass");

  // A waiver is a legitimate outcome and must not be blocked — it is a decision, unlike an empty cell.
  promote("promote: a written waiver in the Evidence cell is accepted",
    "| Rollback tested, not assumed | waived | waived — Jaimin, restore drill deferred to Monday |\n",
    "pass");

  // Deleting the section would otherwise be the cheapest evasion of the rule above.
  check("promote: removing the Verification section entirely is refused", {
    ...checklist, env: { BUILD_ID: "0123456789ab" }, expect: "fail", contains: "no Verification rows",
    repo: build({ commits: [{ files: { "docs/releases/0123456789ab.md": "# Release\n\n## What is in it\n\n| A | B | C |\n| --- | --- | --- |\n| x | y | z |\n" }, message: "docs: release" }] }),
  });
}

// ── report ──────────────────────────────────────────────────────────────────────────────────────────
const w = Math.max(...results.map((r) => r.name.length));
console.log("");
for (const r of results) console.log(`  ${r.ok ? "ok  " : "FAIL"}  ${r.name.padEnd(w)}  ${r.why}`);
const bad = results.filter((r) => !r.ok);
console.log(`\n  ${results.length - bad.length}/${results.length} cases behaved as documented`);
if (bad.length) {
  console.log(`\n  ${bad.length} gate(s) do not do what the documents say they do. That is the point of running this.`);
  process.exit(1);
}
console.log(`
  Proven: the logic inside these gates rejects what it claims to, and — as importantly — passes the
  legal version of the same change. Not proven, and only the host can: that a red check blocks a
  merge, that code-owner review is enforced, that force-pushes are refused, that stale approvals are
  dismissed, or that these files are valid Actions YAML. Run the suite in
  docs/09-host-and-pipeline.md against a real repository before calling setup done.`);
```

## The break-it suite, in order

A gate that has never rejected anything is indistinguishable from one that cannot. Run these five once, on
the real repository, before you call setup done. They are ordered because each depends on the previous: the
contexts must exist before they can be required, and protection must exist before the perimeter can assert
anything about it.

**0. Make the contexts exist.** Open one throwaway pull request with a one-line change so `size`, `gates`,
`spec`, `verify` and `review` each report once. Now they are selectable in the UI and nameable in the `PUT`.
Close it, then apply the protection above.

**1. A pull request over the ceiling must fail `size`.**

```bash
git switch -c PULSE-901-break-size main
printf '# PULSE-901\n\nBreak-it fixture. Not real work.\n' > docs/specs/PULSE-901.md
git add docs/specs/PULSE-901.md && git commit -m "docs: spec for PULSE-901"
for i in $(seq 1 500); do echo "export const pad$i = $i;" >> src/pad.ts; done
git add src/pad.ts && git commit -m "feat: 500 lines of padding"
git push -u origin PULSE-901-break-size && gh pr create --fill && gh pr checks --watch
```

Expected: `size` red, with `500 lines / 1 files exceeds the ceiling of 400 lines / 20 files`. Other checks
will also be red on a fixture branch — read the `size` job specifically. Then add the `size-override` label
and re-run: `size` must go **yellow-passing** with the warning, because the override is a person's recorded
decision, not an agent's. Remove the label, close the pull request, delete the branch.

**2. A commit mixing a gate change with source must fail `gates`.**

```bash
git switch -c PULSE-902-break-gates main
printf '# PULSE-902\n\nBreak-it fixture.\n' > docs/specs/PULSE-902.md
git add docs/specs/PULSE-902.md && git commit -m "docs: spec for PULSE-902"
echo "# break-it fixture" >> .github/workflows/size.yml
echo "export const two = 2;" >> src/two.ts
git add .github/workflows/size.yml src/two.ts
git commit -m "chore: touch a gate and source in one commit"
git push -u origin PULSE-902-break-gates && gh pr create --fill && gh pr checks --watch
```

Expected: `gates` red with `mixes a gate change with implementation`, listing both paths. Then split the
commit in two — the workflow edit alone, then the source alone — force-push, and `gates` must go green while
printing the gate-only commit as visible. That second half is the part people skip, and it is the half that
proves the check discriminates rather than just refuses.

**3. Two spec failures.** Both must fail `spec`, for different reasons.

```bash
# 3a: no spec at all
git switch -c PULSE-903-no-spec main
echo "export const three = 3;" >> src/three.ts
git add src/three.ts && git commit -m "feat: no spec anywhere"
git push -u origin PULSE-903-no-spec && gh pr create --fill

# 3b: the spec is the second commit
git switch -c PULSE-904-late-spec main
echo "export const four = 4;" >> src/four.ts
git add src/four.ts && git commit -m "feat: code first"
printf '# PULSE-904\n\nWritten after the fact.\n' > docs/specs/PULSE-904.md
git add docs/specs/PULSE-904.md && git commit -m "docs: spec for PULSE-904"
git push -u origin PULSE-904-late-spec && gh pr create --fill
```

Expected on 3a: `docs/specs/PULSE-903.md is missing. Run /spec PULSE-903 before implementing.` Expected on 3b:
`The branch's first commit must be the spec alone`, with the offending commit printed. While you are here,
push a branch named `fix-thing` with no ticket id: `spec` must reject the branch name before it looks for a
file at all.

**4. Turning off code-owner review must fail `perimeter`.**

```bash
gh api -X PATCH "repos/$REPO/branches/main/protection/required_pull_request_reviews" \
  -F require_code_owner_reviews=false
gh workflow run perimeter.yml && sleep 5 && gh run watch
```

Expected: red, with `Code owner review is not required, so CODEOWNERS is a text file with no effect.` Restore
it and re-run, and confirm green:

```bash
gh api -X PATCH "repos/$REPO/branches/main/protection/required_pull_request_reviews" \
  -F require_code_owner_reviews=true
gh workflow run perimeter.yml && sleep 5 && gh run watch
```

A check that fails at everything is as useless as one that passes everything, so both runs are the test.

**5. Removing `PERIMETER_TOKEN` must fail, not skip.** Rename the secret to `PERIMETER_TOKEN_OLD`, run the
workflow, confirm it goes red with `PERIMETER_TOKEN is not set`, then rename it back and confirm green. This
is the most important of the five, because it is the pilot's failure mode exactly: the check that looks
configured, does nothing, and reports nothing.

**6. Promotion, both halves.** Push a trivial change to `main` and watch `deploy` produce a build id and put
it in dev. Then dispatch `promote` to production with that id and *no* `docs/releases/<id>.md`, and confirm it
refuses. Add the file with one row's evidence column left blank — leaving the middle column FILLED, because that
is the shape the gate used to miss — and confirm it still refuses. Fill the row, and confirm it goes through
the environment's reviewer prompt. Three runs, one green. `scripts/break-it.mjs promote` covers the same
three cases offline in a second, and should be run first.

## Recording it

Each of those runs has a URL. Collect them — the red runs and the green restores — in the setup ticket's
decision record under `docs/decisions/`. That list is the artefact. Write the run URLs, not the word
"verified".

The status column in [the runbook](12-runbook.md) moves a row from *written* to *proven* only when there is a
red run to point at. Until then, the honest statement about a repository is that its gates are written and
untested on a host. That is a much better sentence to be able to say than the one the pilot's context file
said.
