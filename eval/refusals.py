import json
R = "eval/results/run_%s.json"
runs = {n: {x["id"]: x for x in json.load(open(R % n, encoding="utf-8"))["records"]}
        for n in ("baseline", "baseline2")}
for i in sorted(runs["baseline"]):
    a, b = runs["baseline"][i], runs["baseline2"][i]
    if a["answerable"] and (a.get("refused") or b.get("refused")):
        print(f"#{i} refused in: {[n for n in runs if runs[n][i].get('refused')]}, "
              f"best {a['best_distance']}, chunks {len(a['sources'])}")