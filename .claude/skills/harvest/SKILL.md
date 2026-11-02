---
name: harvest
description: Turn what the review found into something permanent, so the next run starts better.
disable-model-invocation: true
---

Take the confirmed findings and the human's decisions from this session, then route each one:

| What it is | Where it goes |
|---|---|
| CI or the hook already catches it | Nowhere, that layer worked |
| A machine can check it | A test in `tests/` |
| A human decided it | A one-line rule in `AGENTS.md` |
| The spec should have asked | A sharper question in the `spec` skill |

Propose at most three changes, smallest first, and show the diff. Apply them only after the
human says yes. List what you left out and why.
