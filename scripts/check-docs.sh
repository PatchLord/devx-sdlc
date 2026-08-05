#!/usr/bin/env bash
# Verifies the docs/ set after any edit. Replaces check-manual.sh.
set -uo pipefail
cd "$(dirname "$0")/.."
STARTER=${STARTER:-../devx-starter}
FAIL=0
say() { printf "  %-40s %s\n" "$1" "$2"; }

EXPECTED="README 01-why 02-before-build 03-delivery 04-build-loop 05-depth 06-enforcement \
07-repository 08-templates 09-host-and-pipeline 10-stack-wiring 11-measurement 12-runbook \
13-troubleshooting 14-limits 15-reference 16-agent-run-delivery 17-artefacts 18-outcomes 19-first-run"

# 1. every document present
MISSING=""
for d in $EXPECTED; do [ -f "docs/$d.md" ] || MISSING="$MISSING $d"; done
[ -z "$MISSING" ] && say "all 20 documents present" "ok" || { say "all 20 documents present" "MISSING:$MISSING"; FAIL=1; }

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

# 4. every starter file inlined exactly once across the set
if [ -d "$STARTER" ]; then
  N=0; PROBLEM=""
  while IFS= read -r src; do
    rel=${src#"$STARTER"/}
    # tasks/board.html is generated from tasks/board.md by scripts/board.mjs. Inlining a generated
    # file would mean maintaining a copy of a derivative, which is the drift this whole design avoids.
    case "$rel" in .git/*|*.gitkeep|tasks/board.html) continue ;; esac
    N=$((N+1))
    probe=$(awk 'length($0)>28' "$src" | sed -n '2p')
    [ -z "$probe" ] && probe=$(awk 'length($0)>16' "$src" | sed -n '1p')
    [ -z "$probe" ] && continue
    hits=$(grep -Fl "$probe" docs/*.md 2>/dev/null | wc -l | tr -d ' ')
    [ "$hits" -eq 1 ] || PROBLEM="$PROBLEM $rel($hits)"
  done < <(find "$STARTER" -type f -not -path '*/.git/*')
  [ -z "$PROBLEM" ] && say "each starter file inlined once" "ok ($N files)" \
                    || { say "each starter file inlined once" "NOT ONCE:$PROBLEM"; FAIL=1; }
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
