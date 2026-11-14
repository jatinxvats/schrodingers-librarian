# Schrödinger's Librarian

**A retrieval-augmented Q&A system over arXiv papers on the foundations of quantum mechanics, and an honest account of what breaks.**


Live demo: [https://schrodingers-librarian.streamlit.app/]

Evaluation commit: `[1631c00]`

(The free demo sleeps when idle. The first visit after a pause takes about a minute to wake.)


## Why this project

I built this project to test how a RAG pipeline can be leveraged to answer questions related to quantum mechanics. My primary motivation was to learn and break several aspects of the RAG system and incubate a comprehensive understanding of the underlying architecture. 

The system answers a question using only passages retrieved from 113 papers, cites the passages it used, and refuses when nothing relevant is found. The papers are unreviewed preprints, so the system reports what papers claim, and does not certify what is true.


## What's in it

- **Corpus:** 113 arXiv papers (quant-ph, 2018-2025), curated from 609 candidates found by one query per subtopic (measurement, interpretations, decoherence, Bell/EPR, contextuality, uncertainty) plus a review/tutorial query. Selection quotas and a hand-screened list of reviews are in `data/curation/`.

- **Pipeline:** PDF text extraction (PyMuPDF) → cleaning → 10,184 chunks (median 180 tokens, ~40 tokens of overlap) → `all-MiniLM-L6-v2` embeddings → ChromaDB (cosine).

- **Retrieval:** top 5 chunks, at most 2 per paper, with a distance cutoff of 0.45 below which the system refuses. The cutoff was calibrated on about 11 queries before the evaluation and not tuned afterwards.

- **Generation:** `openai/gpt-oss-120b` on Groq, temperature 0.1, a system prompt that requires numbered citations, attribution of each position to its source, and an explicit statement when the excerpts don't answer the question.

- **Interface:** Streamlit, with the retrieved passage behind every citation so you can check it. FastAPI wrapper in `api/`.


## Evaluation

**Test set:** 50 questions I wrote and labelled: 12 definitions, 10 comparisons, 10 contested, 6 multi-topic, 12 unanswerable (6 out-of-domain, 6 near-domain where the topic is in the corpus but the fact isn't). 20 are marked hold-out and were not used for tuning. For each answerable question I recorded which papers contain a passage that directly answers it, and what a good answer must contain.

| | All (n=50) | Dev | Hold-out |
|---|---|---|---|
| Retrieval precision (paper level) | 0.78 | 0.77 | 0.79 |
| Recall (relevant papers in top 5) | 0.67 | 0.65 | 0.70 |
| Hit rate (≥1 relevant paper) | 0.97 | 1.00 | 0.94 |
| False refusals (answerable, refused) | 4 / 39 | 0 | 4 / 16 |
| Correct refusals (unanswerable) | 8 / 11 | 6 / 7 | 2 / 4 |
| Invalid citation numbers | 0 | 0 | 0 |


**Run-to-run variation (two identical runs):** retrieval was identical both times. In the generated answers, 13 of 50 questions cited a different set of sources, one question (#32) flipped between refusing and answering, and the false-refusal count moved from 4 to 3. Single results for one question should not be over-read.


**Answer grading.** Answers were graded by an LLM judge (`qwen/qwen3.8-27b`, a different model from the generator) against my per-question rubric, with the 12 refusal cases graded mechanically. Of the 38 answers the judge read: 11 PASS, 21 PARTIAL, 6 FAIL. Twenty of the 21 PARTIALs were "missed item" against a demanding rubric, so they mostly measure coverage and say little about errors. I checked the judge's three "invented fact" verdicts against the source text: two (#48, #49) were not invented, because the figures were in the excerpts, but the answers stretched them (below).


**Caveats on the numbers**
- Labels are mine and paper-level (a relevant paper may still return an irrelevant chunk). I wrote relevance lists after seeing retrieval output, so precision is probably somewhat optimistic.
- Some rubric items were drafted from outside knowledge and only partly checked against the corpus, which is part of why PARTIAL is so common.
- The hold-out set is not random. It contains several of the hardest cases.
- Fifty questions is small, and differences of a few points are noise.


## What breaks

| Layer | Failure | Example |
|---|---|---|
| Parsing | Display equations and table values become `[EQ]` | A table of dust-grain decoherence times in a review was unreadable, so "How long does a dust grain stay coherent?" (answerable) was refused (#46) |
| Parsing | Reference lists leak into chunks for some papers | One paper's bibliography reached retrieval; 546 chunks were filtered out, not all caught |
| Retrieval | Rare proper names embed poorly | "What is the Frauchiger-Renner paradox?" was refused at distance 0.53 although a paper about it is in the corpus (#10); rephrased as #37 it passed at 0.35 |
| Retrieval | Papers mention concepts without explaining them | "What does Bell's theorem rule out?" returned niche papers; the chunk that states it was not in the top 5 (#2) |
| Retrieval | A definition question is answered from historical commentary | "What is a Hilbert space?" retrieved von Neumann commentary |
| Retrieval | Unreviewed or fringe papers rank highly | A paper with unusual retrocausal claims about collapse was the top hit for "How could collapse be verified?" (#24); kept in the corpus on purpose |
| Generation | Stretching a source | A paper's remark about prediction accuracy (electron g-factor) became "the Born rule has been verified to one part in 10¹²" (#49); a secondhand "as large as a 40 kg mirror" became "the largest object in superposition to date" (#48) |
| Generation | Filling a gap when the excerpts discuss the topic but lack the fact | The Copenhagen side of a QBism comparison was filled in from general knowledge (#19, flagged by the judge, not independently verified) |
| Generation | Attribution drift on contested questions | The same retrieved passages led to a view being attributed differently across runs |
| Generation | Over-refusal | Partially answerable questions get the refusal sentence (#35, and #32 in one run) |

**Label corrections from checking the corpus:** #46 started as "unanswerable" and became answerable once the table was found; #48 and #49 were relabelled "partial".


## Limitations

- arXiv holds research papers, not textbooks, so basic definitions are thin.
- Retrieval is semantic only (no keyword fallback), which is why rare names fail.
- Contested questions get several attributed views, with no verdict, by design.
- The demo is capped at 10 questions per session and 300 per day to protect the API key.


## Run it yourself

```
pip install -r requirements.txt        # the deployed app
python -m src.ingest                   # fetch arXiv metadata
python -m src.curate                   # select the corpus
python -m src.parse                    # download PDFs, extract text
python -m src.chunk
python -m src.index                    # embed and store in Chroma
streamlit run app/streamlit_app.py     # needs GROQ_API_KEY in .env
python eval/run_eval.py --name myrun   # re-run the evaluation
```

Corpus text is excerpted from arXiv papers for research and demonstration. Each citation links to the paper.