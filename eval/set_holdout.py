import json
from pathlib import Path

P = Path(__file__).resolve().parent / "questions_skeleton.json"
HOLDOUT = {3, 5, 7, 9, 10, 14, 15, 17, 20, 26, 28, 30, 32, 35, 37, 40, 43, 46, 48, 50}

qs = json.loads(P.read_text(encoding="utf-8"))
for q in qs:
    q["holdout"] = q["id"] in HOLDOUT
P.write_text(json.dumps(qs, indent=2, ensure_ascii=False), encoding="utf-8")
print(sum(q["holdout"] for q in qs), "held out")