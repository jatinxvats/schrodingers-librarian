import json
import re
from collections import Counter

import arxiv
import config


def date_clause() -> str:
    return f"submittedDate:[{config.DATE_START} TO {config.DATE_END}]"


def or_group(prefix: str, terms: list[str]) -> str:
    return "(" + " OR ".join(f'{prefix}:"{t}"' for t in terms) + ")"


def subtopic_query(terms: list[str]) -> str:
    return f"cat:{config.CATEGORY} AND {or_group('abs', terms)} AND {date_clause()}"


def review_query() -> str:
    cats = "(" + " OR ".join(f"cat:{c}" for c in config.REVIEW_CATEGORIES) + ")"
    return (
        f"{cats} AND {or_group('ti', config.REVIEW_TITLE_TERMS)} "
        f"AND {or_group('abs', config.REVIEW_TOPIC_TERMS)} AND {date_clause()}"
    )


def strip_version(entry_id: str) -> str:
    return re.sub(r"v\d+$", "", entry_id.rsplit("/abs/", 1)[-1])


def run_query(client, query: str, max_results: int):
    search = arxiv.Search(
        query=query, max_results=max_results, sort_by=arxiv.SortCriterion.Relevance
    )
    for r in client.results(search):
        yield {
            "id": strip_version(r.entry_id),
            "title": " ".join(r.title.split()),
            "authors": [a.name for a in r.authors],
            "date": r.published.date().isoformat(),
            "abstract": " ".join(r.summary.split()),
            "pdf_url": r.pdf_url,
            "categories": r.categories,
        }


def fetch_all() -> list[dict]:
    client = arxiv.Client(page_size=100, delay_seconds=3, num_retries=3)
    papers: dict[str, dict] = {}

    def add(query: str, max_results: int, tag: str):
        for p in run_query(client, query, max_results):
            entry = papers.setdefault(p["id"], {**p, "tags": []})
            if tag not in entry["tags"]:
                entry["tags"].append(tag)

    for name, terms in config.SUBTOPICS.items():
        print(f"fetching: {name}")
        add(subtopic_query(terms), config.PER_SUBTOPIC, name)

    print("fetching: review")
    add(review_query(), config.REVIEW_MAX, "review")

    return list(papers.values())


def main():
    papers = fetch_all()
    config.METADATA_DIR.mkdir(parents=True, exist_ok=True)
    out = config.METADATA_DIR / "papers.json"
    out.write_text(json.dumps(papers, indent=2), encoding="utf-8")

    counts = Counter(t for p in papers for t in p["tags"])
    print(f"\n{len(papers)} unique papers")
    for tag, n in counts.most_common():
        print(f"  {tag}: {n}")
    print("\nSample review titles:")
    for p in [p for p in papers if "review" in p["tags"]][:15]:
        print(f"- [{p['id']}] {p['title']}")


if __name__ == "__main__":
    main()