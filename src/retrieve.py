from dataclasses import dataclass

from sentence_transformers import SentenceTransformer

from src.index import MODEL, get_collection

K = 5                  # chunks handed to the generator
FETCH = 30             # candidates pulled before filtering and capping
MAX_PER_PAPER = 2      # keeps one paper from filling every slot
MAX_DISTANCE = 0.45    # SET THIS after calibration (cosine distance; lower = closer)

_model = None
_col = None


@dataclass
class Chunk:
    text: str
    paper_id: str
    title: str
    authors: str
    date: str
    pdf_url: str
    chunk_index: int
    distance: float


def _load():
    global _model, _col
    if _model is None:
        _model = SentenceTransformer(MODEL)
        _col = get_collection()
    return _model, _col


def retrieve(
    query: str,
    k: int = K,
    max_distance: float | None = MAX_DISTANCE,
    max_per_paper: int = MAX_PER_PAPER,
) -> list[Chunk]:
    """Ranked chunks with citation metadata. An empty list means nothing relevant."""
    model, col = _load()
    emb = model.encode([query], normalize_embeddings=True).tolist()
    res = col.query(
        query_embeddings=emb,
        n_results=FETCH,
        include=["documents", "metadatas", "distances"],
    )

    out, per_paper = [], {}
    for doc, meta, dist in zip(
        res["documents"][0], res["metadatas"][0], res["distances"][0]
    ):
        if max_distance is not None and dist > max_distance:
            break  # results are sorted, so everything after this is worse
        pid = meta["paper_id"]
        if per_paper.get(pid, 0) >= max_per_paper:
            continue
        per_paper[pid] = per_paper.get(pid, 0) + 1
        out.append(Chunk(
            text=doc, paper_id=pid, title=meta["title"], authors=meta["authors"],
            date=meta["date"], pdf_url=meta["pdf_url"],
            chunk_index=meta["chunk_index"], distance=dist,
        ))
        if len(out) >= k:
            break
    return out