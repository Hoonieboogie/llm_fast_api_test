from fastapi import FastAPI
from pydantic import BaseModel
from law_rag import get_rag_answer as get_law_answer
from rag_llm_recent import get_rag_answer as get_manual_answer

app = FastAPI(title="Runpod LLM RAG Server")

class Query(BaseModel):
    text: str
    mode: str = "manual"  # 기본값: 매뉴얼 모드

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/rag")
def rag_chat(req: Query):
    if req.mode == "manual":
        answer = get_manual_answer(req.text, persist_dir="/app/vector_store_q_only")
    else:
        answer = get_law_answer(req.text)
    return {"mode": req.mode, "answer": answer}
