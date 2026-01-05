from dotenv import load_dotenv
load_dotenv()  

from fastapi import FastAPI, Depends
from auth import verify_api_key
from rag import generate_answer

app = FastAPI()

@app.post("/chat")
def chat(question: str, _: str = Depends(verify_api_key)):
    answer = generate_answer(question)
    return {"answer": answer}
