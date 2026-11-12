import json

import chromadb
from sentence_transformers import SentenceTransformer

import config

CHUNKS = config.ROOT / "data" / "processed" / "chunks.jsonl"
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

def main():
    chunks = [json.loads(l) for l in CHUNKS.open(encoding="utf-8")]
    model = SentenceTransformer(MODEL)
    col = get_collection(reset=True)

    for i in range(0, len(chunks), BATCH):
        batch = chunks[i : i + BATCH]
        embeddings = model.encode(
            [c["text"] for c in batch], normalize_embeddings=True, show_progress_bar=False
        ).tolist()
        col.upsert(
            ids=[c["chunk_id"] for c in batch],
            documents=[c["text"] for c in batch],
            embeddings=embeddings,
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
        print(f"{min(i + BATCH, len(chunks))}/{len(chunks)}")
    print("collection size:", col.count())


if __name__ == "__main__":
    main()