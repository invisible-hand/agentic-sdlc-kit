#!/bin/sh
# Run the race for real and score it. Use it before each dry run, and after any model update.
#   ./workshop/rehearse.sh <label> <runs> <model> <effort> <blind|spec>
set -eu
label=$1 runs=$2 model=$3 effort=$4 mode=$5
kit=$(git -C "$(dirname "$0")" rev-parse --show-toplevel)
live=${LIVE:-$HOME/shop-live}
raw="$kit/workshop/results/raw"; mkdir -p "$raw"

prompt="Implement the ticket in ticket.md. Commit when you are done."
if [ "$mode" = spec ]; then
  prompt="Implement the ticket in ticket.md. This is the agreed spec, follow it exactly:

$(cat "$kit/workshop/spec.md")

Commit when you are done."
fi

cd "$live"
i=1
while [ "$i" -le "$runs" ]; do
  claude -p "$prompt" -w "$label-$i" --model "$model" --effort "$effort" \
    --permission-mode acceptEdits --setting-sources project --strict-mcp-config \
    --output-format json > "$raw/$label-$i.json" 2> "$raw/$label-$i.err" &
  i=$((i + 1))
done
wait

lanes=""
i=1
while [ "$i" -le "$runs" ]; do lanes="$lanes $live/.claude/worktrees/$label-$i"; i=$((i + 1)); done
python3 "$kit/workshop/score.py" $lanes
python3 - "$raw" "$label" "$runs" <<'P'
import json, sys
raw, label, runs = sys.argv[1], sys.argv[2], int(sys.argv[3])
for i in range(1, runs + 1):
    try:
        d = json.load(open(f"{raw}/{label}-{i}.json"))
        print(f"{label}-{i}: {d['duration_ms']/1000:.0f}s  ${d.get('total_cost_usd', 0):.2f}  turns={d.get('num_turns')}")
    except Exception as e:
        print(f"{label}-{i}: no result ({e})")
P
