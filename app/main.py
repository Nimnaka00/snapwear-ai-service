from fastapi import FastAPI
from app.api.v1 import chat_routes

app = FastAPI()

app.include_router(chat_routes.router, prefix="/api/v1", tags=["Chat"])
