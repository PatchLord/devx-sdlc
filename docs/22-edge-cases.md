# The cases this process does not yet handle

Everything here is a situation a real project reaches and this standard has no mechanism for. Each row says
what happens today, and the route — the cheapest thing that would work — so that meeting one of these is a
decision rather than a surprise.

Two of them are resolved and stay listed, because the reasoning is the useful part and because a resolved case
with no record invites the same argument again.

## Why this document exists at all

A process is abandoned at its first unhandled case, and it is abandoned quietly. The person hits something the
rules do not cover, does the sensible thing outside the process, and does not come back — because coming back
means explaining the gap. After that the process is what people say they do.

So the failure to design against is not "we met a case we had not planned for". It is **meeting one and having
nowhere to put it.** A named route, even a bad one, keeps the work inside the system where the next person can
see it.

## Resolved

### New work arrives mid-project and no ticket covers it

**What happened:** nothing routed back to the TDD. `draft-tdd` fired only when `docs/design/tdd.md` did not
exist, so once it existed the design was effectively frozen and new work went straight to a spec. That is how a
codebase grows features its own design document never mentions, and the next person reads that document and is
confidently wrong.

**Resolved.** A board entry carries **`Design`**, naming the part of the design it comes from. `next.mjs`
checks the path resolves and, where a heading is given, that the heading exists. When it does not, the step is
`extend-tdd`: extend the living TDD, link the entry to the new section, then spec. The cycle repeats for the
life of the project rather than running once at the start.

**The limit, stated:** it checks the section *exists*, never that it *describes this ticket*. A link to the
wrong heading passes completely. It catches the common case, which is no design at all.

### A ticket should not be finished

**What happened:** `DONE` was the only terminal state. An entry that should be abandoned either sat open for
ever or was marked DONE having shipped nothing — and the second is worse, because it makes the board lie about
what exists.

**Resolved.** `DROPPED (YYYY-MM-DD)` is a second terminal state, needs a **Resolution** saying why, and stops
blocking whatever was waiting on it. Dropping is a decision; deleting the entry is how the decision disappears.

## Open, with a route

### A production incident, mid-ticket

**Today:** nothing. The loop wants a spec as the branch's first commit, a board entry, and criteria that
resolve. During an incident all three are wrong: the fix has to ship. So the honest prediction is that the first
incident is handled entirely outside this process, and **that is the most likely moment for the process to be
abandoned** — see above.

**Route:** a `hotfix/` branch prefix that `spec.yml` recognises and lets through **with the debt recorded, not
waived** — the workflow writes a `log/events/` entry naming the branch, and that entry cannot be closed until
the spec and the board entry exist. The gate moves from "before" to "within a stated window", which is a
different claim and an honest one. What must not happen is a label that skips the check with nothing left
behind, because that label becomes the normal path within a month.

### A frozen contract has to change, and other tickets are already built on it

**Today:** `docs/design/criteria/` is a protected path, so the change gets a code owner. Nothing tells the
other in-flight branches that the shape under them moved. They will merge green against the old contract and
break something nobody was looking at.

**Route:** derivable, and cheap. `next.mjs` already knows the base and the branch; a contract file whose last
commit is newer than the branch's fork point is a fact. Emit `contract-moved-under-you` and make it a person's
step. The alternative — a lint that greps for the changed symbol — is more work and less certain.

### A blocker never resolves

**Today:** `blocked-by-ticket` fires for ever with no sense of duration. A ticket blocked in March looks exactly
like a ticket blocked this morning.

**Route:** the board entry's state has no timestamp for *when* it became blocked, and adding one would be
typed rather than derived, which the board refuses on principle. The derivable version is the age of the last
commit that touched the entry. Report it in the directive — "blocked for 34 days" — and let a person decide.
Escalating automatically after N days would produce a class of escalation nobody asked for.

### A criterion becomes unprovable *after* implementation starts

**Today:** `resolve-criteria` is consulted before `implement` and never again. A criterion that looked provable
and turns out not to be is discovered at the pull request, by the `criteria` check, after the work.

**Route:** the check already runs on every push. What is missing is the *reframing* — at that point it is a
class B escalation and a spec revision, not a cell to fill in. The `respond-to-review` skill should say so
where it covers a red `criteria`, because the instinct under time pressure is to write something that resolves
rather than to admit the criterion was wrong.

### The loop gives up mid-ticket

**Today:** `stop-guard` releases at forty continuations or four hours, and then **nothing records that it
did.** The session ends looking like any other. A person reading the board sees a ticket in progress and no
sign that the loop ran out.

**Route:** the counter is already persisted per ticket. On release, append a `log/events/` entry — that
directory is already the place where things a person must look at go, and the weekly hour already reads it.

### Nobody is available to answer

**Today:** every `human=true` step stalls indefinitely. Correct, and better than the alternative — but there
is no record that the project is waiting, so a week can pass invisibly.

**Route:** an escalation already has a class and a disposition. What it lacks is a *second* named person for
when the first does not answer, which is an organisational decision rather than a mechanism, and it belongs in
the SOW's obligations table where response times already live.

### The TDD and the code diverge

**Today:** `CLAUDE.md` says report a divergence, and the pull request template has a field for it. Both are
prose, and finding 59 says prose does not prevent.

**Route:** there is no good mechanical answer, and it is worth saying so rather than inventing one. The nearest
honest thing is a *frequency* check rather than a correctness check: the divergence field being empty on every
pull request for a fortnight is itself the signal, since implementation almost always finds something. That is
a measurement for the weekly hour, not a gate.

### Work that legitimately has no acceptance criterion

**Today:** a dependency bump or a spike has no criterion of the usual shape, and `criteria` refuses prose. The
predictable response is an exemption, and an exemption is the first thing that gets abused.

**Route: none needed, and this is worth knowing before somebody builds one.** The gate is already satisfiable
honestly. A dependency bump's real evidence is that the existing suite still passes, and the artefact for that
is the run — a URL resolves. A spike's output is a finding, and a path to the written finding resolves.
Verified against the resolver:

| Evidence cell | Verdict |
|---|---|
| `verify passes` | refused |
| `the existing suite still passes` | refused |
| `https://github.com/…/actions/runs/123` | resolves |
| `.github/workflows/verify.yml` | resolves |

So the fix is teaching the form in the `acceptance-criteria` skill, not adding a way past the check.

## What this list is not

It is not a backlog. Building all of it would add mechanism faster than any of it has been shown to be needed,
and most of these cases have never actually occurred here — the process has not run on a real project yet. The
honest state is: **each has a route, none has been built, and the first one to be met should be the first one
built.**
