from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import spacy
import requests

app = FastAPI()

# Allow all origins (for development only)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or use ["http://localhost:3000"] etc.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

nlp = spacy.load("en_core_web_sm")

class PromptRequest(BaseModel):
    prompt: str

@app.post("/process")
async def process_prompt(data: PromptRequest):
    prompt = data.prompt

    # Named Entity Recognition
    doc = nlp(prompt)
    entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
    print("Named Entities:", entities)

    try:
        # Call local LLM (Ollama)
        response = requests.post("http://localhost:11434/api/generate", json={
            "model": "llama3",
            "prompt": f"Detect named entitites: {prompt}",
            "stream": False
        })
        response.raise_for_status()
        llm_response = response.json()["response"]
    except Exception as e:
        print("LLM Response:", llm_response)
        llm_response="Error generating response from LLM"

    return {
        "entities": entities,
        "llm_response": llm_response
    }