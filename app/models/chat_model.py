from pydantic import BaseModel
from typing import List, Optional

class Message(BaseModel):
    role: str  # "user", "assistant", or "system"
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]
    model: Optional[str] = "deepseek-r1"
    temperature: Optional[float] = 0.7
    max_tokens: Optional[int] = 1000

class ChatResponse(BaseModel):
    response: str
    model: str
    usage: dict