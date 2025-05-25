from fastapi import APIRouter, HTTPException
from app.models.chat_model import ChatRequest, ChatResponse, Message
from app.services.chat_service import DeepSeekChatService
from typing import List

router = APIRouter()
chat_service = DeepSeekChatService()

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(chat_request: ChatRequest):
    try:
        # New method that combines AI response with product links
        response = await chat_service.generate_response_with_products(chat_request)

        return ChatResponse(
            response=response["response"],
            model=response["model"],
            usage=response["usage"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
