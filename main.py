import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from openai import OpenAI


# Load variables from .env
load_dotenv()

api_key = os.getenv("NVIDIA_API_KEY")

if not api_key:
    raise ValueError("NVIDIA_API_KEY was not found in .env")


# NVIDIA provides an OpenAI-compatible API
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=api_key
)

app = FastAPI()


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return FileResponse("static/index.html")


@app.post("/chat")
def chat(request: ChatRequest):

    completion = client.chat.completions.create(
        model="deepseek-ai/deepseek-v4-flash-0731",
        messages=[
            {
                "role": "user",
                "content": request.message
            }
        ],
        temperature=1,
        top_p=0.95,
        max_tokens=2048,
        extra_body={
            "chat_template_kwargs": {
                "thinking": True,
                "reasoning_effort": "high"
            }
        },
        stream=False
    )

    answer = completion.choices[0].message.content

    return {
        "answer": answer
    }
