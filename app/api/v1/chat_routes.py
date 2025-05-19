from fastapi import APIRouter, HTTPException
from app.models.chat_model import ChatRequest, ChatResponse, Message
from app.services.chat_service import DeepSeekChatService
from typing import List

router = APIRouter()
chat_service = DeepSeekChatService()

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(chat_request: ChatRequest):
    try:
        response = await chat_service.chat_completion(
            messages=[message.dict() for message in chat_request.messages],
            model=chat_request.model,
            temperature=chat_request.temperature,
            max_tokens=chat_request.max_tokens
        )
        
        # Extract the assistant's reply
        assistant_reply = response['choices'][0]['message']['content']
        
        return ChatResponse(
            response=assistant_reply,
            model=response['model'],
            usage=response['usage']
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))