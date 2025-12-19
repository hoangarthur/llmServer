from fastapi import FastAPI, Header, HTTPException
import requests
import os
from pydantic import BaseModel

app = FastAPI()

OLLAMA_URL = os.getenv("OLLAMA_URL")
API_KEY = os.getenv("API_KEY")

class ChatRequest(BaseModel):
    prompt: str

@app.post("/chat")
def chat(request: ChatRequest, x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    
    payload = {
        "model": "llama3.2:latest",
        "prompt": request.prompt,
        "stream": False
    }

    r = requests.post(f"{OLLAMA_URL}/api/generate", json=payload)
    return r.json()
