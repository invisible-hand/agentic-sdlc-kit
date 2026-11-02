#!/bin/sh
# The same checks CI runs. Same input, same verdict, every time.
status=0
run() { uv run --quiet --extra dev "$@" || status=1; }
run ruff check .
run ruff format --check .
run lint-imports --no-cache
run pytest -q --cov=shop
exit $status
