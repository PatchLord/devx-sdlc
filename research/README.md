# How research works here

The manual is the deliverable. This folder is the workbench. Keeping them separate is what makes it
cheap to absorb a new source without performing surgery on 72,000 words.

## The four files

| File | What it is |
|---|---|
| `ai-sdlc-sources.md` | Intake and verification. One entry per source: what it is, its limits, the takeaway, and what it means for us. |
| `findings.md` | Every claim adjudicated, with its verdict. Append-only. **Check here first** — most new sources repeat ground already covered. |
| `open-questions.md` | The frontier. What we know we do not know. |
| `experiments.md` | The evidence nobody will hand us. Hypothesis, falsifier, consequence. |

## A research round

**Batch, do not stream.** Editing the manual once per source is how you spend a day on a finding that
gets refuted. Collect five to ten sources, then run one round.

1. **Intake.** Drop the raw source in `transcripts/` or add it to the sources file. Do not summarise
   yet — summarising early loses the thing you did not know you needed.

   `transcripts/` is deliberately **not committed** — it holds verbatim conference talks and articles that
   belong to the people who wrote them, and this repository is public. Every source is cited in
   `ai-sdlc-sources.md` with a link; the raw text stays on the machine that fetched it.
2. **Grep `findings.md`.** If the claim is already adjudicated, stop. Record it as a repeat and move on.
3. **Debate the batch.** One workflow: independent lenses find candidate changes, then every candidate
   is adversarially verified with instructions to default to refuted. Expect most to die. The last batch
   was 24 examined, 3 accepted, and the 21 refutations were mostly "the doc already says this".
4. **Verify every figure against the primary source.** Not the talk, not the blog quoting the talk. Two
   of the last three headline numbers we checked did not survive: one was a non-peer-reviewed working
   paper by a vendor selling the fix, one was a fabricated symmetry built from a single real number.
5. **Apply survivors in one pass.** Then run `scripts/check-manual.sh`.
6. **Append to `findings.md`** — including the refutations. That file is worth more than the accepted
   changes, because it is what stops the next round redoing this one.

## The rules that do the work

**A finding must change what a developer does on Monday.** Otherwise it is an edit, not a finding.

**A figure not in `ai-sdlc-sources.md` loses its digits and keeps its direction.**

**Prefer 2026 evidence.** Model capability moved far enough that a 2025 productivity measurement does
not describe the tools anyone is using. Date anything older, in the same breath, whether or not it
flatters the argument.

**Audit our own artifacts as a source.** Three of the last five accepted changes came from checking our
own work rather than from reading — a `perimeter.yml` bug found by querying real repositories, a
self-grantable size override, and a security gate our own cited figure demanded and we had not built.
Reading has a high refutation rate now. Our own files do not.

## When research is finished

Not a feeling. Four criteria:

1. **Dry.** Two consecutive rounds produce zero accepted changes.
2. **Built.** Every *to build* row is built, or reclassified as never-will-be with the reason.
3. **Proven.** The process has run end to end on one real project, and the six numbers have data.
4. **Closed.** `open-questions.md` is empty or every entry is explicitly deferred.

Criterion 3 is the one that matters, and it is the one no amount of reading can satisfy. Until it is
met the manual is a hypothesis with instrumentation attached, which is what part 14 already says.
