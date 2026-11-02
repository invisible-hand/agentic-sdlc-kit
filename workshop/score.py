#!/usr/bin/env python3
"""The judge. Scores lanes against Dana's acceptance criteria. Agents never see this file.

usage: score.py <lane-dir> [<lane-dir> ...]
"""

import json
import subprocess
import sys
from pathlib import Path

CHECKS = [
    ("No code or empty code: full price", [({"items": {"mug": 1}}, 1250),
                                           ({"items": {"mug": 1}, "promo_code": ""}, 1250)]),
    ("SAVE10 takes 10% off", [({"items": {"mug": 1}, "promo_code": "SAVE10"}, 1125)]),
    ("Fractions go to the customer", [({"items": {"tshirt": 9}, "promo_code": "SAVE10"}, 16191),
                                      ({"items": {"poster": 1}, "promo_code": "SAVE10"}, 719)]),
    ("save10 and ' SAVE10 ' work", [({"items": {"mug": 1}, "promo_code": "save10"}, 1125),
                                    ({"items": {"mug": 1}, "promo_code": " SAVE10 "}, 1125)]),
    ("Unknown code: clear 400", [({"items": {"mug": 1}, "promo_code": "NOPE"}, "reject")]),
    ("A list of codes: 400, no crash", [({"items": {"mug": 1}, "promo_code": ["SAVE10"]}, "reject")]),
]

PROBE = """
import json, sys
from shop import api
try:
    print(json.dumps(api.checkout(json.loads(sys.argv[1]))))
except Exception as e:
    print(json.dumps({"crash": type(e).__name__}))
"""


def probe(lane: Path, payload: dict) -> dict:
    run = subprocess.run(
        [sys.executable, "-I", "-c", f"import sys; sys.path.insert(0, {str(lane)!r})\n{PROBE}",
         json.dumps(payload)],
        capture_output=True, text=True, timeout=20,
    )
    try:
        return json.loads(run.stdout.strip().splitlines()[-1])
    except (IndexError, json.JSONDecodeError):
        return {"crash": "no output"}


def passes(response: dict, expected) -> bool:
    if expected == "reject":
        return (
            response.get("status") == 400
            and "total_cents" not in response
            and bool(response.get("error"))
        )
    return response.get("status") == 200 and response.get("total_cents") == expected


def added_lines(lane: Path) -> tuple[int, int]:
    git = ["git", "-C", str(lane)]
    root = subprocess.run([*git, "rev-list", "--max-parents=0", "HEAD"],
                          capture_output=True, text=True).stdout.split()[-1]
    subprocess.run([*git, "add", "-N", "shop", "tests"], capture_output=True)
    out = subprocess.run([*git, "diff", "--numstat", root, "--", "shop", "tests"],
                         capture_output=True, text=True).stdout
    code = tests = 0
    for line in out.splitlines():
        added, _, path = line.split("\t")
        if added != "-":
            if path.startswith("tests"):
                tests += int(added)
            else:
                code += int(added)
    return code, tests


def main() -> None:
    lanes = [Path(p).resolve() for p in sys.argv[1:]]
    if not lanes:
        sys.exit(__doc__)
    rows = {name: [] for name, _ in CHECKS}
    for lane in lanes:
        for name, cases in CHECKS:
            rows[name].append(all(passes(probe(lane, p), e) for p, e in cases))
    width = max(len(n) for n in rows)
    heads = [lane.name[:10] for lane in lanes]
    print(" " * width, *[f"{h:>10}" for h in heads])
    for name, results in rows.items():
        print(f"{name:<{width}}", *[f"{'pass' if r else 'FAIL':>10}" for r in results])
    scores = [sum(r[i] for r in rows.values()) for i in range(len(lanes))]
    print(f"{'SCORE':<{width}}", *[f"{s}/{len(CHECKS):>8}" for s in scores])
    sizes = [added_lines(lane) for lane in lanes]
    print(f"{'Lines added: code':<{width}}", *[f"{c:>10}" for c, _ in sizes])
    print(f"{'Lines added: tests':<{width}}", *[f"{t:>10}" for _, t in sizes])


if __name__ == "__main__":
    main()
