#!/usr/bin/env bash
# Verifies the docs/ set after any edit. Replaces check-manual.sh.
set -uo pipefail
cd "$(dirname "$0")/.."
STARTER=${STARTER:-../devx-starter}
FAIL=0
say() { printf "  %-40s %s\n" "$1" "$2"; }

EXPECTED="README 01-why 02-before-build 03-delivery 04-build-loop 05-depth 06-enforcement \
07-repository 08-templates 09-host-and-pipeline 10-stack-wiring 11-measurement 12-runbook \
13-troubleshooting 14-limits 15-reference 16-agent-run-delivery 17-artefacts 18-outcomes 19-first-run \
20-orientation 21-capability 22-edge-cases"

# 1. every document present
MISSING=""
for d in $EXPECTED; do [ -f "docs/$d.md" ] || MISSING="$MISSING $d"; done
# Counted from EXPECTED rather than written as a literal. "all 20 documents present" stayed in this message
# while the set grew to 22, which is a check reporting a number it had stopped measuring.
NDOCS=$(printf '%s\n' $EXPECTED | wc -l | tr -d ' ')
[ -z "$MISSING" ] && say "all $NDOCS documents present" "ok" || { say "all $NDOCS documents present" "MISSING:$MISSING"; FAIL=1; }

# 2. no cross-link points at a file that does not exist
DEAD=""
for f in docs/*.md; do
  for l in $(grep -oE '\]\(([0-9]{2}-[a-z-]+|README)\.md\)' "$f" | tr -d '](){}' | sed 's/\.md//' | sort -u); do
    [ -f "docs/$l.md" ] || DEAD="$DEAD $(basename "$f")->$l"
  done
done
[ -z "$DEAD" ] && say "no dead cross-links" "ok" || { say "no dead cross-links" "DEAD:$DEAD"; FAIL=1; }

# 3. no leftover references to the old numbered parts
STALE=$(grep -lE '\b(part|section) (1[0-5]|[1-9])\b' docs/*.md 2>/dev/null | tr '\n' ' ')
[ -z "$STALE" ] && say "no 'part N' references" "ok" || say "no 'part N' references" "check: $STALE"

# 4. every starter file inlined exactly once, and inlined CURRENT
#
# This used to probe a single line, which passed while an inlined copy was stale: the probe line had not
# changed, so a drifted body was invisible. Since the docs inline each file verbatim, the honest check is
# whether the doc contains the file's ENTIRE body. Found by editing three starter files and watching the
# old version of this check stay green.
if [ -d "$STARTER" ]; then
  RESULT=$(STARTER="$STARTER" python3 scripts/check-inlines.py)
  N=${RESULT%%|*}; REST=${RESULT#*|}
  STALE=${REST%%|*}; REST=${REST#*|}
  NOTONCE=${REST%%|*}; UNMENTIONED=${REST#*|}
  if [ -n "$STALE" ] || [ -n "$NOTONCE" ] || [ -n "$UNMENTIONED" ]; then
    say "starter accounted for in docs" "STALE:$STALE NOT-ONCE:$NOTONCE UNMENTIONED:$UNMENTIONED"; FAIL=1
  else
    say "starter accounted for in docs" "ok ($N files)"
  fi
fi

# 4b. the demo agreement's counts match what they count
#
# The two-page agreement summarises a 23,000-word terms document, and every number in it is a hand-copied
# figure with no link back to the rows it counts. Three of them had drifted before this check existed — the
# risk count twice over, and the exclusion count by one — and the reader who found it was a simulated client
# reading his own signature block. A summary is the right shape; an unchecked summary is a liability.
if [ -d "demo/ops-todo-board" ]; then
  if python3 scripts/check-sow-counts.py > /tmp/.sow-counts 2>&1; then
    say "demo agreement counts" "ok"
  else
    say "demo agreement counts" "MISMATCH"; sed 's/^/    /' /tmp/.sow-counts; FAIL=1
  fi
fi

# 5. figures trace to the sources file
UNTRACED=""
for p in $(cat docs/*.md | grep -oE '[0-9]+(\.[0-9]+)?%' | sort -u); do
  grep -qF "$p" research/ai-sdlc-sources.md || UNTRACED="$UNTRACED $p"
done
[ -z "$UNTRACED" ] && say "percentages traceable" "ok" || { say "percentages traceable" "UNTRACED:$UNTRACED"; FAIL=1; }

# 6. voice, and fences
BANNED=""
for w in robust scalable seamless leverage game-changing holistic synergy streamlined transformative "In conclusion" "Furthermore," "Moreover,"; do
  grep -qiE "\b${w}" docs/*.md && BANNED="$BANNED '$w'"
done
[ -z "$BANNED" ] && say "no banned terms" "ok" || { say "no banned terms" "FOUND:$BANNED"; FAIL=1; }
ODD=""
for f in docs/*.md; do n=$(grep -c '^```' "$f"); [ $((n % 2)) -eq 0 ] || ODD="$ODD $(basename "$f")"; done
[ -z "$ODD" ] && say "fences balanced" "ok" || { say "fences balanced" "ODD:$ODD"; FAIL=1; }

echo
if [ "$FAIL" -eq 0 ]; then
  echo "  docs OK"
  printf "  %-26s %6s words\n" "$(basename "$f")" "" >/dev/null
  for f in docs/*.md; do printf "    %-26s %6s words\n" "$(basename "$f")" "$(wc -w < "$f" | tr -d ' ')"; done
  echo "    ------------------------------------"
  printf "    %-26s %6s words\n" "TOTAL" "$(cat docs/*.md | wc -w | tr -d ' ')"
else
  echo "  DOCS HAVE PROBLEMS — do not commit"
fi
exit $FAIL
