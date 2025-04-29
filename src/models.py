from pydantic import BaseModel
from typing import List


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: List[Message]
    temperature: float = 0.5
    model: str = "gemma3:4b-it-q4_K_M"


class ChatResponse(BaseModel):
    content: str