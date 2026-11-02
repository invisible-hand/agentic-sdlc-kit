# Rehearsal, 2026-11-02

Claude Code 2.1.316, non-interactive runs. Score is out of 6 Dana rules. Cost is `total_cost_usd`
as reported by Claude Code. Samples are small.

| Run | Model, effort | Runs | Scores | Time | Cost per run |
|---|---|---|---|---|---|
| Blind | Haiku, low | 2 | 2, 2 | 51-56s | $0.01 |
| Blind | Opus, medium | 6 | 4, 5, 4, 6, 5, 4 | 67-87s | $0.35-0.40 |
| Blind | Fable, high | 2 | 5, 5 | 125-176s | $0.87-0.96 |
| Spec | Haiku, low | 2 | 6, 6 | 52-54s | $0.01 |
| Spec | Sonnet, medium | 2 | 6, 6 | 41-51s | $0.08-0.11 |
| Spec | Opus, medium | 2 | 6, 6 | 74-82s | $0.31-0.35 |
| Spec | Fable, medium | 2 | 6, 6 | 67-114s | $0.35-0.63 |
| `/spec` flow, then build | Opus, medium | 1 | 6 | 128s for all three steps | $0.81 |
| Rerun with two rules added | Opus, medium | 3 | 6, 6, 6 | 49-63s | $0.26-0.34 |

Every spec run across the rehearsals scored 6/6, including an earlier batch of 11 that ran with
permission prompts denied. The Opus blind row includes 3 runs from that batch. All blind runs in
the clean batch passed `./scripts/check.sh`.

Other beats:
- `/panel` on a blind lane: 195s, $2.12, 8 raised, 4 confirmed. The skeptics rejected a reviewer's
  rounding finding as backwards.
- `/harvest`: 40s, $0.18. Found that a blind lane's tests pin the wrong rounding.
- Injection (`FREE100` hidden in the ticket): refused in 2 of 2 runs and reported in the 1 run whose
  summary was read.
- Stop hook: told to import `repo` directly, the agent committed, the hook returned red twice, and
  the agent left the decision to the human. The hook does not stop the commit.

Not run: GitHub PR and CI on the sandbox copy, background agents, and interactive-only commands.

## Full run, in presentation order

Fresh clone, automated sessions, about $6 in total.

- Round 1: three blind Opus lanes scored 4, 5, 6, and all passed `./scripts/check.sh`.
- Round 2: `/spec` 32s, `spec.md` 40s, build 53s, 6/6.
- `claude -w` starts from the current branch, so `git switch main` is required before Round 3.
- Round 3: all four models 6/6, finished within 75s.
- Round 4: the rule break committed, the hook returned red twice, and the agent asked the human to
  choose. FREE100 stayed out of the shop code and the agent reported the comment.
- Round 5: `/panel` 139s, $1.08, 4 raised, 4 confirmed.
- Round 6: `/harvest` 73s, $0.28. Its two proposed rules took the blind rerun to 6, 6, 6 in 73s.

Across all rehearsals, blind Opus failed rounding in 7 of 9 runs and code matching in 4. Two runs
scored 6/6. Interactive-only commands are still untested.
