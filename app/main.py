from fastapi import FastAPI, Form
from .rag_engine import generate_answer
from .embeddings import embed_text

app = FastAPI()

@app.post("/ask")
def ask_question(context: str = Form(...), question: str = Form(...)):
    answer = generate_answer(context, question)
    return {"answer": answer}
