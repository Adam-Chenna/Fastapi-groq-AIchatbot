from fastapi import FastAPI
from pydantic import BaseModel
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key = os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

app = FastAPI()

class Prompt(BaseModel):
    Question : str

@app.post("/generates")
async def generates_llms(prompt : Prompt):
    response = client.responses.create(
        input = prompt.Question,
        model="openai/gpt-oss-20b"
    )
    return {"answer": response.output_text}


