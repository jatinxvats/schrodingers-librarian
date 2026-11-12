import re
import sys
from pathlib import Path

TEXT = Path(__file__).resolve().parent.parent / "data" / "processed" / "text"


def main(paper_id: str, pattern: str, width: int = 220, limit: int = 8):
    if paper_id == "all":  # count matches per paper
        counts = {}
        for f in TEXT.glob("*.txt"):
            n = len(re.findall(pattern, f.read_text(encoding="utf-8"), re.I))
            if n:
                counts[f.stem] = n
        for pid, n in sorted(counts.items(), key=lambda x: -x[1]):
            print(f"{pid}: {n}")
        return
    text = (TEXT / f"{paper_id.replace('/', '_')}.txt").read_text(encoding="utf-8")
    hits = list(re.finditer(pattern, text, re.I))
    print(f"{paper_id}: {len(hits)} matches for /{pattern}/\n")
    for m in hits[:limit]:
        s, e = max(0, m.start() - width), min(len(text), m.end() + width)
        print("...", text[s:e], "...\n")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])