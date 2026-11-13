import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from dotenv import load_dotenv
from groq import Groq, RateLimitError

from src.generate import format_context
from src.retrieve import retrieve

load_dotenv(ROOT / ".env")
JUDGE_MODEL = "qwen/qwen3.8-27b"   # deliberately not the generator's model

PROMPT = """You are grading an answer from a retrieval-augmented system about the foundations of quantum mechanics. The system must answer ONLY from the numbered excerpts it was given.

Check:
1. Every factual claim is supported by the excerpt it cites ([n]).
2. Positions are attributed to the correct author or source.
3. Claims found in no excerpt are flagged as outside knowledge, even if true.
4. The answer covers the MUST INCLUDE items as far as the excerpts allow.
5. The answer does not contradict itself.
If ANSWERABLE is no, the corpus lacks the fact: stating a specific fact or number that no excerpt contains is FAIL (invented-fact); only describing what the excerpts say and noting they give no such fact is PASS.

Grades: PASS = grounded, correctly attributed, covers the must-include items as far as excerpts allow. PARTIAL = mostly right but misses one item or has one weakly supported claim. FAIL = misattribution, unsupported or invented fact, contradiction, or misses the main point.
Tags: misattribution, invented-fact, uncited-claim, outside-knowledge, contradiction, missed-item, none.

Reply with JSON only:
{"grade": "PASS|PARTIAL|FAIL", "tag": "...", "unsupported_claims": ["..."], "note": "one sentence"}"""

_client = None


def client() -> Groq:
    global _client
    if _client is None:
        _client = Groq(api_key=os.environ["GROQ_API_KEY"])
    return _client


def call(user: str) -> dict | None:
    for attempt in range(5):
        try:
            r = client().chat.completions.create(
                model=JUDGE_MODEL, temperature=0, max_tokens=3000,
                messages=[{"role": "system", "content": PROMPT},
                          {"role": "user", "content": user}])
            m = re.search(r"\{.*\}", r.choices[0].message.content or "", re.S)
            if m:
                return json.loads(m.group(0))
        except RateLimitError:
            time.sleep(15 * (attempt + 1))
        except json.JSONDecodeError:
            pass
    return None


def judge(rec: dict) -> dict:
    if rec.get("refused"):  # no model needed
        if rec["answerable"]:
            return {"grade": "FAIL", "tag": "wrong-refusal", "note": "refused an answerable question", "auto": True}
        return {"grade": "PASS", "tag": "none", "note": "correct refusal", "auto": True}
    chunks = retrieve(rec["question"])  # deterministic: same chunks the system saw
    user = (f"QUESTION: {rec['question']}\nANSWERABLE FROM CORPUS: {'yes' if rec['answerable'] else 'no'}\n"
            f"MUST INCLUDE: {rec['must_include']}\n\nEXCERPTS:\n{format_context(chunks)}\n\nANSWER:\n{rec['answer']}")
    out = call(user) or {"grade": "UNJUDGED", "tag": "other", "note": "judge failed to return JSON"}
    out["auto"] = False
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", default="baseline")
    run = ap.parse_args().run
    recs = json.loads((ROOT / "eval" / "results" / f"run_{run}.json").read_text(encoding="utf-8"))["records"]
    results, lines = {}, []
    for r in recs:
        if "answer" not in r:
            continue
        print(f"judging #{r['id']}")
        j = judge(r)
        results[r["id"]] = j
        lines.append(f"#{r['id']} [{r['bucket']}/{r['type']}]{' HOLD-OUT' if r.get('holdout') else ''}: "
                     f"{j['grade']} {j.get('tag', '')} - {j.get('note', '')}")
        time.sleep(1)
    out = ROOT / "eval" / "results"
    (out / f"judge_{run}.json").write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    (out / f"judge_{run}.md").write_text("\n".join(lines), encoding="utf-8")
    counts = {g: sum(1 for j in results.values() if j["grade"] == g) for g in ("PASS", "PARTIAL", "FAIL", "UNJUDGED")}
    print(counts)


if __name__ == "__main__":
    main()