#!/bin/sh
# One command, clean slate. Builds the sandbox from this repo, without workshop/.
#   ./workshop/reset.sh            local sandbox only
#   ./workshop/reset.sh --github   also reset the GitHub copy, for the PR and CI step
set -eu
kit=$(git -C "$(dirname "$0")" rev-parse --show-toplevel)
live=${LIVE:-$HOME/shop-live}
remote=${LIVE_REMOTE:-invisible-hand/shop-live}

if [ -e "$live" ]; then
  [ -f "$live/.sandbox" ] || { echo "refusing: $live is not a sandbox" >&2; exit 1; }
  rm -rf "$live"
fi
mkdir -p "$live"
git -C "$kit" archive HEAD | tar -x -C "$live"
touch "$live/.sandbox"
printf '.sandbox\n' >> "$live/.gitignore"
git -C "$live" init -q -b main
git -C "$live" add -A
git -C "$live" -c user.name=Workshop -c user.email=workshop@example.com commit -qm "Shop before the ticket"
(cd "$live" && uv sync --quiet --extra dev && ./scripts/check.sh > /dev/null) \
  || { echo "sandbox checks are red" >&2; exit 1; }

if [ "${1:-}" = "--github" ]; then
  gh repo view "$remote" > /dev/null 2>&1 || gh repo create "$remote" --private > /dev/null
  gh pr list -R "$remote" --state open --json number --jq '.[].number' \
    | xargs -I{} gh pr close {} -R "$remote" --delete-branch > /dev/null
  git -C "$live" remote add origin "https://github.com/$remote.git"
  git -C "$live" push -q --force origin main
fi
echo "ready: $live"
