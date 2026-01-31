from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

app = FastAPI()

class Prompt(BaseModel):
    question: str

@app.post("/generate")
async def generate_llm(prompt: Prompt):
    response = client.responses.create(
        input=prompt.question,
        model="openai/gpt-oss-20b"
    )
    return {"answer": response.output_text}
