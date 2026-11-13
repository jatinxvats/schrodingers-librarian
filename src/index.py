import json

import chromadb
import numpy as np
from sentence_transformers import SentenceTransformer

import config

CHUNKS = config.ROOT / "data" / "processed" / "chunks.jsonl"
EMBEDDINGS = config.ROOT / "data" / "processed" / "embeddings.npy"
CHROMA_DIR = config.ROOT / "data" / "chroma"
COLLECTION = "qm_foundations"
MODEL = "all-MiniLM-L6-v2"
BATCH = 256


def get_collection(reset: bool = False):
    client = chromadb.PersistentClient(path=str(CHROMA_DIR))
    if reset:
        try:
            client.delete_collection(COLLECTION)
        except Exception:
            pass
    return client.get_or_create_collection(
        COLLECTION, metadata={"hnsw:space": "cosine"}
    )


def load_chunks() -> list[dict]:
    return [json.loads(l) for l in CHUNKS.open(encoding="utf-8")]


def fill(col, chunks, embeddings):
    for i in range(0, len(chunks), BATCH):
        batch = chunks[i : i + BATCH]
        col.upsert(
            ids=[c["chunk_id"] for c in batch],
            documents=[c["text"] for c in batch],
            embeddings=embeddings[i : i + BATCH].tolist(),
            metadatas=[
                {
                    "paper_id": c["paper_id"],
                    "title": c["title"],
                    "authors": ", ".join(c["authors"]),
                    "date": c["date"],
                    "pdf_url": c["pdf_url"],
                    "chunk_index": c["chunk_index"],
                }
                for c in batch
            ],
        )


def build():
    """Full rebuild: embed every chunk, save the embeddings, refill Chroma."""
    chunks = load_chunks()
    model = SentenceTransformer(MODEL)
    emb = model.encode(
        [c["text"] for c in chunks], normalize_embeddings=True,
        batch_size=BATCH, show_progress_bar=True,
    ).astype("float32")
    np.save(EMBEDDINGS, emb)
    col = get_collection(reset=True)
    fill(col, chunks, emb)
    print("collection size:", col.count())


def ensure_index():
    """Deploy-time: fill Chroma from the saved embeddings if it is empty or stale."""
    chunks = load_chunks()
    col = get_collection()
    if col.count() != len(chunks):
        col = get_collection(reset=True)
        fill(col, chunks, np.load(EMBEDDINGS))
    return col


if __name__ == "__main__":
    build()