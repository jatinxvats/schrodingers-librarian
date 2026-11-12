import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from src.retrieve import retrieve, MAX_DISTANCE

qs = {q["id"]: q for q in json.loads((ROOT / "eval" / "questions_skeleton.json").read_text(encoding="utf-8"))}
for qid in range(39, 45):
    d = retrieve(qs[qid]["question"], k=1, max_distance=None)[0].distance
    verdict = "REFUSED" if d > MAX_DISTANCE else "PASSES CUTOFF"
    print(f"#{qid} best {d:.3f} -> {verdict}  {qs[qid]['question']}")