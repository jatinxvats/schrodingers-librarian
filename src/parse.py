import re
from collections import Counter
import json
import time
import unicodedata

import pymupdf
import requests

import config

PDF_DIR = config.ROOT / "data" / "raw" / "pdfs"
TEXT_DIR = config.ROOT / "data" / "processed" / "text"
CORPUS = config.ROOT / "data" / "curation" / "corpus.json"


def safe_name(paper_id: str) -> str:
    return paper_id.replace("/", "_")


def download(paper: dict) -> bool:
    path = PDF_DIR / f"{safe_name(paper['id'])}.pdf"
    if path.exists():
        return True
    urls = [paper["pdf_url"], f"https://arxiv.org/pdf/{paper['id']}"]
    for url in urls:
        for attempt in range(3):
            try:
                r = requests.get(url, timeout=60,
                                 headers={"User-Agent": "schrodingers-librarian/0.1"})
                r.raise_for_status()
                path.write_bytes(r.content)
                time.sleep(3)
                return True
            except Exception as e:
                print(f"  {paper['id']} attempt {attempt + 1} failed: {e}")
                time.sleep(5)
    return False

def extract(paper_id: str) -> list[str]:
    """Return page texts. sort=True helps with two-column reading order."""
    doc = pymupdf.open(PDF_DIR / f"{safe_name(paper_id)}.pdf")
    pages = [page.get_text("text") for page in doc]
    doc.close()
    return pages

REF_HEADING = re.compile(
    r"^\s*(?:\d+\.?\s*|[IVX]+\.?\s*)?(?:references|bibliography)\s*$", re.I | re.M
)

def _norm(line: str) -> str:
    return re.sub(r"\d+", "#", line.strip().lower())

ACCENTS = {"¨": "\u0308", "´": "\u0301", "`": "\u0300"}

def fix_text(text: str) -> str:
    text = re.sub(
        r"([¨´`])\s?([A-Za-z])",
        lambda m: unicodedata.normalize("NFC", m.group(2) + ACCENTS[m.group(1)]),
        text,
    )
    return unicodedata.normalize("NFKC", text)

def clean_text(pages: list[str]) -> str:
    """Rules, in order:
    1. Drop running headers/footers: short lines (digits normalized) repeated on
       >=40% of pages, bare page numbers, and arXiv stamps.
    2. Repair hyphenation across line breaks (measure-\\nment -> measurement).
    3. Cut everything after the LAST 'References'/'Bibliography' heading, only if
       it sits in the second half of the text (guards against early mentions).
    4. Replace equation-like short lines (<50% ASCII letters) with one [EQ] marker.
    5. Reflow to single-spaced text.
    """
    # 1. headers/footers
    pages = [fix_text(p) for p in pages]
    page_lines = [p.splitlines() for p in pages]
    counts = Counter()
    for lines in page_lines:
        counts.update({_norm(l) for l in lines if 0 < len(l.strip()) <= 80})
    min_pages = max(3, int(0.4 * len(pages)))

    def is_boilerplate(line: str) -> bool:
        s = line.strip()
        if not s:
            return False
        if re.fullmatch(r"\d{1,3}", s) or s.lower().startswith("arxiv:"):
            return True
        return len(pages) >= 4 and counts[_norm(line)] >= min_pages

    text = "\n".join(l for ls in page_lines for l in ls if not is_boilerplate(l))

    # 2. hyphenation
    text = re.sub(r"(\w)-\n(\w)", r"\1\2", text)

    # 3. references
    matches = list(REF_HEADING.finditer(text))
    if matches and matches[-1].start() > 0.5 * len(text):
        text = text[: matches[-1].start()]

    # 4. equations
    out = []
    for line in text.splitlines():
        s = line.strip()
        if not s:
            continue
        letters = sum(c.isascii() and c.isalpha() for c in s)
        if len(s) < 60 and letters / len(s) < 0.5:
            if not out or out[-1] != "[EQ]":
                out.append("[EQ]")
        else:
            out.append(s)

    # 5. reflow
    return re.sub(r"\s+", " ", " ".join(out)).strip()


def quality(pages: list[str]) -> dict:
    text = "".join(pages)
    n = max(len(text), 1)
    alpha = sum(c.isalpha() or c.isspace() for c in text)
    return {"pages": len(pages), "chars": len(text), "alpha_ratio": round(alpha / n, 3)}


def main():
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    TEXT_DIR.mkdir(parents=True, exist_ok=True)
    corpus = json.loads(CORPUS.read_text(encoding="utf-8"))
    report = {}

    for i, paper in enumerate(corpus, 1):
        print(f"[{i}/{len(corpus)}] {paper['id']}")
        if not download(paper):
            continue
        pages = extract(paper["id"])
        report[paper["id"]] = quality(pages)
        (TEXT_DIR / f"{safe_name(paper['id'])}.txt").write_text(
            clean_text(pages), encoding="utf-8"
        )

    (config.ROOT / "data" / "processed" / "parse_report.json").write_text(
        json.dumps(report, indent=2), encoding="utf-8"
    )
    low = [k for k, v in report.items() if v["alpha_ratio"] < 0.8 or v["chars"] < 5000]
    print(f"\nparsed {len(report)} papers; {len(low)} look suspicious: {low}")


if __name__ == "__main__":
    main()