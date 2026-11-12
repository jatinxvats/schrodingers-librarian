import json
import math
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.retrieve import retrieve

QUESTIONS = ROOT / "eval" / "questions_skeleton.json"
CHUNKS = ROOT / "data" / "processed" / "chunks.jsonl"

STOP = set("""a an the of to in on and or is are was were be been it its this that these those
what which who how why does do did can could would should for with as by at from about into than
then there their they them we you not no yes if so such actually really""".split())


def stem(w: str) -> str:
    for suf in ("ing", "ed", "es", "s"):
        if w.endswith(suf) and len(w) - len(suf) >= 4:
            return w[: -len(suf)]
    return w


def toks(s: str) -> list[str]:
    return [stem(w) for w in re.findall(r"[a-z]+", s.lower())
            if w not in STOP and len(w) > 2]


def load_index():
    chunks = [json.loads(l) for l in CHUNKS.open(encoding="utf-8")]
    tfs = [Counter(toks(c["text"])) for c in chunks]
    df = Counter(t for tf in tfs for t in tf)
    return chunks, tfs, df


def lexical(query, chunks, tfs, df, k=5):
    q = set(toks(query))
    n = len(chunks)
    scored = sorted(
        ((sum((1 + math.log(tf[t])) * math.log(n / df[t]) for t in q if t in tf), i)
         for i, tf in enumerate(tfs)),
        reverse=True,
    )
    out, seen = [], set()
    for s, i in scored:
        if s <= 0:
            break
        pid = chunks[i]["paper_id"]
        if pid in seen:
            continue
        seen.add(pid)
        out.append((s, chunks[i]))
        if len(out) >= k:
            break
    return out


def snip(text: str, n: int = 190) -> str:
    return " ".join(text.split())[:n]


def main(ids: list[int]):
    qs = {q["id"]: q for q in json.loads(QUESTIONS.read_text(encoding="utf-8"))}
    chunks, tfs, df = load_index()
    lines = []
    for qid in ids:
        q = qs[qid]
        lines.append(f"\n=== #{qid} [{q['bucket']}/{q['type']}] {q['question']}")
        lines.append("-- SEMANTIC (cutoff off):")
        for c in retrieve(q["question"], k=5, max_distance=None, max_per_paper=1):
            lines.append(f"  {c.distance:.3f} [{c.paper_id}] {c.title[:55]} | {snip(c.text)}")
        lines.append("-- KEYWORD:")
        for s, c in lexical(q["question"], chunks, tfs, df):
            lines.append(f"  {s:.1f} [{c['paper_id']}] {c['title'][:55]} | {snip(c['text'])}")
    report = "\n".join(lines)
    out = ROOT / "eval" / "results" / f"label_report_{'_'.join(map(str, ids))}.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    # usage: python eval/label_report.py 3 5 7 9 10
    main([int(a) for a in sys.argv[1:]])