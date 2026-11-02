# shop

Tiny checkout service. Python 3.12, stdlib only.

## Layout

- `shop/api.py`: entry point. Validates the request and calls `service`. Never imports `repo`.
- `shop/service.py`: business rules.
- `shop/repo.py`: storage (in-memory dicts). Prices are integer cents.

## Commands

`./scripts/check.sh` runs lint, format, layering, tests and coverage. CI runs the same checks.

## Rules

- Every behaviour change ships with a test.
- Never edit a test just to make it pass.
