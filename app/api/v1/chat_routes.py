from fastapi import APIRouter
from models.chat_model import ChatRequest, ChatResponse
from services.chat_service import generate_reply

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat_with_ai(payload: ChatRequest):
    reply = generate_reply(payload.message)
    return {"reply": reply}
