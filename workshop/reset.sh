#!/bin/sh
# One command, clean slate: a fresh clone of the zero-state repo.
set -eu
repo=${SHOP_REPO:-https://github.com/invisible-hand/agentic-sdlc-live.git}
live=${LIVE:-$HOME/shop-live}
if [ -e "$live" ]; then
  [ -f "$live/.git/sandbox" ] || { echo "refusing: $live is not a sandbox" >&2; exit 1; }
  rm -rf "$live"
fi
git clone -q "$repo" "$live"
git -C "$live" remote remove origin   # a push must never reach the zero-state repo
touch "$live/.git/sandbox"
(cd "$live" && uv sync --quiet --extra dev && ./scripts/check.sh > /dev/null) \
  || { echo "sandbox checks are red" >&2; exit 1; }
echo "ready: $live"
