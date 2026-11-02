# Agentic SDLC kit

Presenter kit. Never give this to the agents, and keep it from the audience until after the session.

The zero-state repo is `agentic-sdlc-live`. This kit holds what must stay out of it: Dana's answers,
the spec, the judge, the scripts and the rehearsal results.

```sh
./workshop/reset.sh                     # fresh clone in ~/shop-live
cd ~/shop-live && claude                # first time only: accept the trust prompt
python3 <kit>/workshop/score.py .claude/worktrees/blind-*
<kit>/workshop/inject.sh                # Round 4, run from the clone
./workshop/rehearse.sh <label> <runs> <model> <effort> <blind|spec>
```

`reset.sh` removes `origin` from the clone, so nothing can be pushed to the zero-state repo by mistake. For the PR step, create a repo of your own and add it as `origin`.
