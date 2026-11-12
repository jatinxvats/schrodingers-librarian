from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from src.generate import answer
from src.retrieve import _load


@asynccontextmanager
async def lifespan(app: FastAPI):
    _load()  # load the embedding model and Chroma once at startup, not per request
    yield


app = FastAPI(title="schrodingers-librarian", lifespan=lifespan)


class AskRequest(BaseModel):
    question: str = Field(min_length=3, max_length=500)


class AskResponse(BaseModel):
    answer: str
    sources: list[dict]


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/ask", response_model=AskResponse)
def ask(req: AskRequest):
    try:
        result = answer(req.question.strip())
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"generation failed: {type(e).__name__}")
    return AskResponse(answer=result["answer"], sources=result["sources"])