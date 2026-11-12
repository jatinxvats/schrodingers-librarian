import json
import sys
from pathlib import Path

D = Path(__file__).resolve().parent
qs = json.loads((D / "questions_skeleton.json").read_text(encoding="utf-8"))
labels = {x["id"]: x for x in json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))}

for q in qs:
    if q["id"] in labels:
        q.update({k: v for k, v in labels[q["id"]].items() if k != "id"})
(D / "questions_skeleton.json").write_text(
    json.dumps(qs, indent=2, ensure_ascii=False), encoding="utf-8"
)
print("merged", len(labels), "labels")