import json
import re

from sentence_transformers import SentenceTransformer

import config

TEXT_DIR = config.ROOT / "data" / "processed" / "text"
CORPUS = config.ROOT / "data" / "curation" / "corpus.json"
OUT = config.ROOT / "data" / "processed" / "chunks.jsonl"

tokenizer = SentenceTransformer("all-MiniLM-L6-v2").tokenizer


MAX_TOKENS = 200       # leaves headroom under MiniLM's 256 limit
OVERLAP_TOKENS = 40    # about 20% overlap, so boundary-cut derivations survive somewhere
MIN_TOKENS = 30        # drop tiny fragments
MAX_EQ_SHARE = 0.3     # drop chunks that are mostly [EQ] markers

# protect abbreviations whose period is not a sentence end
ABBREV = re.compile(
    r"\b(?:et al|Fig|Figs|Eq|Eqs|Ref|Refs|Sec|vs|cf|Phys|Rev|Lett|e\.g|i\.e)\.", re.I
)
CITE = re.compile(r"Phys\.\s*Rev|arXiv:|\bet al\.,|\[\d{1,3}\]\s+[A-Z]\.")

def split_sentences(text: str) -> list[str]:
    text = ABBREV.sub(lambda m: m.group(0)[:-1] + "\u2024", text)
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z\[\(])", text)
    return [p.replace("\u2024", ".").strip() for p in parts if p.strip()]


def split_long(s: str) -> list[str]:
    """Hard-split a 'sentence' that alone exceeds the budget (glossaries, run-ons)."""
    out, cur = [], []
    for w in s.split():
        cur.append(w)
        if n_tokens(" ".join(cur)) >= MAX_TOKENS:
            out.append(" ".join(cur))
            cur = []
    if cur:
        out.append(" ".join(cur))
    return out


def keep(chunk: str) -> bool:
    if len(CITE.findall(chunk)) >= 3:
        return False
    words = chunk.split()
    if n_tokens(chunk) < MIN_TOKENS:
        return False
    return words.count("[EQ]") / len(words) <= MAX_EQ_SHARE


def chunk_text(text: str) -> list[str]:
    sents = []
    for s in split_sentences(text):
        sents.extend(split_long(s) if n_tokens(s) > MAX_TOKENS else [s])
    sizes = [n_tokens(s) for s in sents]

    chunks, i = [], 0
    while i < len(sents):
        j, total = i, 0
        while j < len(sents) and total + sizes[j] <= MAX_TOKENS:
            total += sizes[j]
            j += 1
        if j == i:          # safety: always make progress
            j = i + 1
        chunks.append(" ".join(sents[i:j]))
        if j >= len(sents):
            break
        # step back over whole sentences to build the overlap
        k, back = j, 0
        while k > i + 1 and back + sizes[k - 1] <= OVERLAP_TOKENS:
            k -= 1
            back += sizes[k]
        i = k
    return [c for c in chunks if keep(c)]


def n_tokens(s: str) -> int:
    return len(tokenizer.encode(s, add_special_tokens=False))


def main():
    corpus = json.loads(CORPUS.read_text(encoding="utf-8"))
    n_chunks, too_long, sizes = 0, 0, []
    with OUT.open("w", encoding="utf-8") as f:
        for paper in corpus:
            path = TEXT_DIR / f"{paper['id'].replace('/', '_')}.txt"
            if not path.exists():
                continue
            for i, chunk in enumerate(chunk_text(path.read_text(encoding="utf-8"))):
                t = n_tokens(chunk)
                sizes.append(t)
                too_long += t > 256
                f.write(json.dumps({
                    "chunk_id": f"{paper['id']}::{i}",
                    "text": chunk,
                    "paper_id": paper["id"],
                    "title": paper["title"],
                    "authors": paper["authors"][:3],
                    "date": paper["date"],
                    "pdf_url": paper["pdf_url"],
                    "chunk_index": i,
                }) + "\n")
                n_chunks += 1
    sizes.sort()
    print(f"{n_chunks} chunks; median {sizes[len(sizes)//2]} tokens; "
          f"{too_long} ({too_long / n_chunks:.1%}) exceed 256 tokens")


if __name__ == "__main__":
    main()