# Agentic SDLC Live

Presenter kit for a 90-minute live demo in Claude Code. One ticket, one small shop app, no pre-made
PRs or demo branches. Every run happens on stage and is scored by a judge the agents can't see.

## Run it

```sh
./workshop/reset.sh                              # clean sandbox in ~/shop-live
cd ~/shop-live && claude                         # first time only: accept the trust prompt
```

The first `claude` in `~/shop-live` matters. Until the folder is trusted, Claude Code ignores
`.claude/settings.json` permission rules and refuses `--bg`.

## What's here

| Path | What it is |
|---|---|
| `shop/`, `tests/`, `ticket.md` | The app and Dana's vague ticket |
| `AGENTS.md` | The only rules the agents start with |
| `.claude/skills/` | `/spec`, `/panel`, `/harvest`. All three run only when typed |
| `.claude/agents/` | Three reviewers and a skeptic, each with its own model and effort |
| `.claude/hooks/` | A Stop hook that sends the agent back while checks are red |
| `workshop/` | Spec, Dana's answers, judge and scripts. `git archive` leaves this out of the sandbox |

```sh
python3 workshop/score.py <lane> [<lane> ...]               # score lanes against Dana's rules
./workshop/rehearse.sh <label> <runs> <model> <effort> <blind|spec>   # run the race for real
```

The run of show, storyboard and evidence live in the Artifact, not in this repo.

The `shop/` app, tooling and first skill are adapted from Si Jie Lim's
[tt-masterclass-agentic-sdlc-lite](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite),
MIT licensed. See `LICENSE`.
