import json
import config

CURATION_DIR = config.ROOT / "data" / "curation"
QUOTA_PER_BUCKET = 14   # per topic bucket; multi-tag papers count toward all their buckets
REVIEW_QUOTA = 20


def load_ids(name: str) -> set[str]:
    f = CURATION_DIR / name
    return set(json.loads(f.read_text(encoding="utf-8"))) if f.exists() else set()


def curate(papers: list[dict]) -> list[dict]:
    topics = list(config.SUBTOPICS)
    keep = load_ids("review_keep.json")   # hand-approved reviews with no topic tag
    drop = load_ids("review_drop.json")   # hand-rejected papers of any kind
    papers = [p for p in papers if p["id"] not in drop]

    selected: dict[str, dict] = {}

    def n_selected(tag: str) -> int:
        return sum(tag in p["tags"] for p in selected.values())

    # 1. fill each topic bucket (order of appearance = rough relevance proxy)
    for tag in topics:
        for p in papers:
            if n_selected(tag) >= QUOTA_PER_BUCKET:
                break
            if tag in p["tags"]:
                selected.setdefault(p["id"], p)

    # 2. reviews: must overlap a topic bucket OR be in the hand-approved keep list
    for p in papers:
        if n_selected("review") >= REVIEW_QUOTA:
            break
        if "review" in p["tags"] and (
            any(t in topics for t in p["tags"]) or p["id"] in keep
        ):
            selected.setdefault(p["id"], p)

    return list(selected.values())


def write_screen_file(papers: list[dict]):
    """Reviews with no topic tag: the ones you hand-screen."""
    topics = set(config.SUBTOPICS)
    lines = [
        f"{p['id']}\t{p['title']}"
        for p in papers
        if "review" in p["tags"] and not topics & set(p["tags"])
    ]
    CURATION_DIR.mkdir(parents=True, exist_ok=True)
    (CURATION_DIR / "review_screen.txt").write_text("\n".join(lines), encoding="utf-8")


def main():
    papers = json.loads((config.METADATA_DIR / "papers.json").read_text(encoding="utf-8"))
    write_screen_file(papers)
    corpus = curate(papers)

    out = CURATION_DIR / "corpus.json"
    out.write_text(json.dumps(corpus, indent=2), encoding="utf-8")

    print(f"{len(corpus)} papers selected")
    for tag in list(config.SUBTOPICS) + ["review"]:
        print(f"  {tag}: {sum(tag in p['tags'] for p in corpus)}")


if __name__ == "__main__":
    main()