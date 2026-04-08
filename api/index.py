from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=print(os.environ.get("GROQ_API_KEY")),
    base_url="https://api.groq.com/openai/v1",
)

app = FastAPI()

class Prompt(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "FastAPI Groq chatbot is live 🚀"}


@app.post("/generate")
async def generate_llm(prompt: Prompt):
    response = client.chat.completions.create(
    model="llama3-70b-8192",
    messages=[
        {"role": "user", "content": prompt.question}
    ]
)

    return {
        "answer": response.choices[0].message.content
}
