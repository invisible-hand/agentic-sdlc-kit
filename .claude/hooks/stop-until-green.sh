#!/bin/sh
# Stop hook: the agent cannot finish while the checks are red.
# Exit 2 sends the failure back to Claude and it keeps working. Gives up after 3 tries.
cat > /dev/null
[ -z "$(git status --porcelain)" ] && [ -z "$(git log -1 --since='30 minutes ago' --format=%h)" ] && exit 0

tries_file=".check-tries"
output=$(./scripts/check.sh 2>&1)
if [ $? -eq 0 ]; then
  rm -f "$tries_file"
  exit 0
fi

tries=$(( $(cat "$tries_file" 2>/dev/null || echo 0) + 1 ))
echo "$tries" > "$tries_file"
[ "$tries" -ge 3 ] && exit 0

echo "Checks are red. You are not done. Fix this, do not weaken the checks:" >&2
echo "$output" | tail -40 >&2
exit 2
