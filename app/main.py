from fastapi import FastAPI
from dotenv import load_dotenv
from api.v1 import chat_routes

load_dotenv()

app = FastAPI()

app.include_router(chat_routes.router, prefix="/api/v1", tags=["Chat"])
