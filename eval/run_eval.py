import argparse
import json
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from groq import RateLimitError

import src.generate as gen
from src.retrieve import FETCH, K, MAX_DISTANCE, MAX_PER_PAPER, retrieve

QUESTIONS = ROOT / "eval" / "questions.json"
OUT = ROOT / "eval" / "results"
REFUSAL_START = "the retrieved papers do not contain enough information"


def is_refusal(text: str) -> bool:
    t = text.strip().lower()
    return t == gen.NO_ANSWER.strip().lower() or t.startswith(REFUSAL_START)


def uncited_sentences(text: str) -> int:
    sents = re.split(r"(?<=[.!?])\s+", text)
    return sum(1 for s in sents if len(s.split()) >= 8 and not re.search(r"\[\d+\]", s))


def ask(question: str) -> dict:
    for attempt in range(5):
        try:
            return gen.answer(question)
        except RateLimitError:
            time.sleep(15 * (attempt + 1))
    raise RuntimeError("rate limited after 5 attempts")


def run_one(q: dict) -> dict:
    rec = {k: q.get(k) for k in
           ("id", "bucket", "type", "question", "answerable", "holdout",
            "relevant_papers", "must_include", "notes")}
    try:
        best = retrieve(q["question"], k=1, max_distance=None)[0].distance
        res = ask(q["question"])
    except Exception as e:
        rec["error"] = f"{type(e).__name__}: {e}"
        return rec

    sources = [{"n": s["n"], "paper_id": s["paper_id"], "title": s["title"],
                "distance": s["distance"]} for s in res["sources"]]
    retrieved = [s["paper_id"] for s in sources]
    rel = set(q.get("relevant_papers") or [])
    rec.update(
        answer=res["answer"],
        refused=is_refusal(res["answer"]),
        sources=sources,
        best_distance=round(best, 3),
        citations=res["citations"],
        uncited_sentences=uncited_sentences(res["answer"]),
    )
    if q["answerable"] and rel:
        rec["precision"] = (sum(p in rel for p in retrieved) / len(retrieved)
                            if retrieved else None)
        rec["recall"] = len(rel & set(retrieved)) / min(len(rel), K)
        rec["hit"] = bool(rel & set(retrieved))
    return rec


def mean(xs):
    xs = [x for x in xs if x is not None]
    return round(sum(xs) / len(xs), 3) if xs else None


def summarize(records: list[dict]) -> dict:
    def block(rs):
        ans = [r for r in rs if r.get("answerable") and "hit" in r]
        una = [r for r in rs if r.get("answerable") is False and "answer" in r]
        return {
            "n": len(rs),
            "answerable_n": len(ans),
            "precision": mean([r["precision"] for r in ans]),
            "recall": mean([r["recall"] for r in ans]),
            "hit_rate": mean([float(r["hit"]) for r in ans]),
            "false_refusals": sum(1 for r in ans if r["refused"]),
            "unanswerable_n": len(una),
            "correct_refusals": sum(1 for r in una if r["refused"]),
            "unanswerable_answered": [r["id"] for r in una if not r["refused"]],
            "invalid_citations": sum(len(r["citations"]["invalid"]) for r in rs if "citations" in r),
            "uncited_sentences_per_answer": mean([r.get("uncited_sentences") for r in rs if "answer" in r]),
            "errors": [r["id"] for r in rs if "error" in r],
        }
    return {
        "all": block(records),
        "dev": block([r for r in records if not r.get("holdout")]),
        "holdout": block([r for r in records if r.get("holdout")]),
    }


def write_grading_sheet(records: list[dict], path: Path):
    lines = ["# Grading sheet\n",
             "Grade: PASS / PARTIAL / FAIL. Tag: misattribution, invented-fact, "
             "uncited-claim, wrong-refusal, missed-retrieval, outside-knowledge, "
             "contradiction, other.\n"]
    for r in records:
        lines += [f"\n---\n## #{r['id']} [{r['bucket']}/{r['type']}]"
                  f"{' (HOLD-OUT)' if r.get('holdout') else ''}",
                  f"**Q:** {r['question']}",
                  f"**Answerable:** {r['answerable']}  |  **Best distance:** {r.get('best_distance')}  "
                  f"|  **Refused:** {r.get('refused')}",
                  f"**Must include:** {r['must_include']}",
                  f"**Label notes:** {r['notes']}",
                  f"\n**Answer:**\n\n{r.get('answer', r.get('error'))}\n",
                  "**Sources:**"]
        rel = set(r.get("relevant_papers") or [])
        for s in r.get("sources", []):
            mark = "relevant" if s["paper_id"] in rel else "-"
            lines.append(f"- [{s['n']}] {s['paper_id']} {s['title'][:70]} ({s['distance']}) {mark}")
        lines += ["", "**Grade:** ____   **Tag:** ____   **Note:** ____"]
    path.write_text("\n".join(lines), encoding="utf-8")


def git_hash() -> str:
    try:
        return subprocess.check_output(["git", "rev-parse", "--short", "HEAD"],
                                       cwd=ROOT, text=True).strip()
    except Exception:
        return "unknown"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", default="baseline")
    ap.add_argument("--fresh", action="store_true", help="ignore any saved progress")
    args = ap.parse_args()

    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / f"run_{args.name}.json"
    questions = json.loads(QUESTIONS.read_text(encoding="utf-8"))

    run = {"name": args.name, "git": git_hash(), "records": [],
           "config": {"model": gen.MODEL, "temperature": gen.TEMPERATURE, "k": K,
                      "fetch": FETCH, "max_per_paper": MAX_PER_PAPER,
                      "max_distance": MAX_DISTANCE}}
    if path.exists() and not args.fresh:
        run = json.loads(path.read_text(encoding="utf-8"))
    done = {r["id"] for r in run["records"] if "error" not in r}
    run["records"] = [r for r in run["records"] if r["id"] in done]

    for q in questions:
        if q["id"] in done:
            continue
        print(f"#{q['id']} {q['question'][:70]}")
        run["records"].append(run_one(q))
        path.write_text(json.dumps(run, indent=2, ensure_ascii=False), encoding="utf-8")
        time.sleep(1.5)

    run["records"].sort(key=lambda r: r["id"])
    run["summary"] = summarize(run["records"])
    path.write_text(json.dumps(run, indent=2, ensure_ascii=False), encoding="utf-8")
    write_grading_sheet(run["records"], OUT / f"grading_{args.name}.md")
    print(json.dumps(run["summary"], indent=2))


if __name__ == "__main__":
    main()