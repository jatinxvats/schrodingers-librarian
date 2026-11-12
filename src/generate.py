import os
import re

from dotenv import load_dotenv
from groq import Groq

import config
from src.retrieve import retrieve

load_dotenv(config.ROOT / ".env")

MODEL = "openai/gpt-oss-120b"
TEMPERATURE = 0.1
MAX_TOKENS = 2000

SYSTEM_PROMPT = """You are a research assistant answering questions about the foundations of quantum mechanics, using only excerpts from arXiv papers.

RULES
1. Use ONLY the numbered context excerpts below the question. Do not use outside knowledge, even if you know the answer. If a fact is not in the excerpts, you do not know it.
2. Cite every factual claim with the excerpt number in square brackets, like [1] or [2][3]. Cite with plain square brackets only; never use any other citation format. Never cite a number that is not in the context. Never cite an excerpt for something it does not say.
3. If the excerpts only partly answer the question, state what they support and say plainly what they do not cover. If they do not answer it at all, reply exactly: "The retrieved papers do not contain enough information to answer this." and stop.
4. Many questions here are contested (interpretations, collapse, the role of the observer). Do not pick a winner or blend positions into one voice. Present each position separately, attribute it to the source that holds it, and note where authors disagree.
5. The excerpts are arXiv preprints, not textbooks, and are not peer reviewed. Describe what a paper claims or argues, not what is settled fact, unless the excerpt itself presents it as established.
6. Excerpts are extracted from PDFs. "[EQ]" marks a removed equation and text may be garbled. Do not guess at missing equations or fill in their content.
7. Be concise: a short direct answer first, then supporting detail. No preamble, and no list of sources at the end (the app shows them)."""

NO_ANSWER = (
    "I couldn't find relevant material in my collection of quantum foundations "
    "papers for that question. It may be outside the corpus (about 110 arXiv "
    "papers on measurement, interpretations, Bell/EPR, decoherence, contextuality "
    "and uncertainty), so try rephrasing or asking about one of those topics."
)

_client = None


def _groq() -> Groq:
    global _client
    if _client is None:
        _client = Groq(api_key=os.environ["GROQ_API_KEY"])
    return _client


def format_context(chunks) -> str:
    return "\n\n".join(
        f"[{i}] {c.title} ({c.authors}, {c.date})\n{c.text}"
        for i, c in enumerate(chunks, 1)
    )


def normalize_citations(text: str) -> str:
    """Turn gpt-oss style markers like 【1†L4-L7】 into plain [1]."""
    return re.sub(r"【(\d+)[^】]*】", r"[\1]", text)


def check_citations(text: str, n_sources: int) -> dict:
    nums = {
        int(n)
        for g in re.findall(r"\[(\d+(?:\s*,\s*\d+)*)\]", text)
        for n in re.split(r"\s*,\s*", g)
    }
    return {
        "cited": sorted(nums),
        "invalid": sorted(n for n in nums if not 1 <= n <= n_sources),
    }


def answer(query: str) -> dict:
    chunks = retrieve(query)
    if not chunks:
        return {"answer": NO_ANSWER, "sources": [], "citations": {"cited": [], "invalid": []}}

    resp = _groq().chat.completions.create(
        model=MODEL,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
        reasoning_effort="low",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user",
             "content": f"Context:\n{format_context(chunks)}\n\nQuestion: {query}"},
        ],
    )
    sources = [
        {"n": i, "paper_id": c.paper_id, "title": c.title, "authors": c.authors,
         "date": c.date, "pdf_url": c.pdf_url, "distance": round(c.distance, 3),
         "text": c.text}
        for i, c in enumerate(chunks, 1)
    ]
    text = normalize_citations(resp.choices[0].message.content or "")
    return {
        "answer": text,
        "sources": sources,
        "citations": check_citations(text, len(sources)),
    }