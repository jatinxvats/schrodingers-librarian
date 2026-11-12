import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.retrieve import retrieve

QUESTIONS = ROOT / "eval" / "questions_skeleton.json"
CORPUS = ROOT / "data" / "curation" / "corpus.json"


def show(qid: int, keywords: list[str]):
    qs = json.loads(QUESTIONS.read_text(encoding="utf-8"))
    q = next(x for x in qs if x["id"] == qid)
    print(f"\n#{qid} [{q['bucket']} / {q['type']}] {q['question']}\n")

    print("RETRIEVED (cutoff off):")
    for c in retrieve(q["question"], k=8, max_distance=None, max_per_paper=1):
        print(f"  {c.distance:.3f}  [{c.paper_id}] {c.title[:70]}")
        print(f"          {c.text[:160]}...")

    if keywords:
        print(f"\nCORPUS SEARCH for {keywords}:")
        for p in json.loads(CORPUS.read_text(encoding="utf-8")):
            blob = f"{p['title']} {p['abstract']}".lower()
            hits = [k for k in keywords if k.lower() in blob]
            if hits:
                print(f"  [{p['id']}] {p['title'][:70]}  <- {hits}")


if __name__ == "__main__":
    # usage: python eval/label_helper.py 2 "bell" "hidden variable"
    show(int(sys.argv[1]), sys.argv[2:])