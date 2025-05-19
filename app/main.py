from fastapi import FastAPI
from app.api.v1.chat_routes import router as chat_router
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Snapwear AI Service",
    description="Chatbot powered by DeepSeek R1",
    version="1.0.0"
)

app.include_router(chat_router, prefix="/api/v1")

# This block is crucial for uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)