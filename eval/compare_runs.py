import json
import sys
from pathlib import Path

R = Path(__file__).resolve().parent / "results"
a_name, b_name = (sys.argv[1], sys.argv[2]) if len(sys.argv) > 2 else ("baseline", "baseline2")
a = {r["id"]: r for r in json.loads((R / f"run_{a_name}.json").read_text(encoding="utf-8"))["records"]}
b = {r["id"]: r for r in json.loads((R / f"run_{b_name}.json").read_text(encoding="utf-8"))["records"]}

flips, cite_diff, src_diff = [], [], []
for i in sorted(a):
    x, y = a[i], b.get(i)
    if not y or "answer" not in x or "answer" not in y:
        continue
    if x["refused"] != y["refused"]:
        flips.append(i)
    if set(x["citations"]["cited"]) != set(y["citations"]["cited"]):
        cite_diff.append(i)
    if [s["paper_id"] for s in x["sources"]] != [s["paper_id"] for s in y["sources"]]:
        src_diff.append(i)

print(f"refusal flipped between runs: {flips}")
print(f"different sources cited:      {len(cite_diff)} of {len(a)} questions")
print(f"different retrieved papers:   {len(src_diff)} of {len(a)} (should be 0: retrieval is deterministic)")