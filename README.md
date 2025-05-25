# 🧠 SnapWear AI Service

This is a **FastAPI-based backend** powering SnapWear's **AI Stylist Chatbot**. It uses the **DeepSeek R1 model** via [OpenRouter](https://openrouter.ai) to generate outfit advice and dynamically recommend products from SnapWear's fashion catalog.

---

## 📁 Project Structure

```
snapwear-ai-service/
│
├── app/
│   ├── api/v1/
│   │   └── chat_routes.py         # Chat endpoint with product recommendation logic
│   ├── models/
│   │   └── chat_model.py          # Pydantic models for chat request/response
│   ├── services/
│   │   └── chat_service.py        # DeepSeek/OpenRouter integration
│   └── main.py                    # FastAPI app entry point
│
├── .env                           # Environment variables
├── requirements.txt               # Python dependencies
├── test_chat.py                   # Local test script using requests
├── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/snapwear-ai-service.git
cd snapwear-ai-service
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate        # Windows
# OR
source venv/bin/activate     # macOS/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Variables

Create a `.env` file in the root:

```env
DEEPSEEK_API_KEY=your_openrouter_api_key
DEEPSEEK_API_URL=https://openrouter.ai/api/v1/chat/completions
SNAPWEAR_BACKEND_URL=http://localhost:5000
```

> Make sure your Snapwear backend is running on port `5000`.

---

## 🚀 Running the Server

```bash
uvicorn main:app --reload
```

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- Chat endpoint: `POST /api/v1/chat`

---

## 🧰 Test the AI Endpoint

### Using `test_chat.py`

```bash
python test_chat.py
```

### Using Postman

**POST** `http://localhost:8000/api/v1/chat`

**Body:**

```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful AI fashion assistant for Snapwear."
    },
    {
      "role": "user",
      "content": "What outfit should I wear to a summer party?"
    }
  ],
  "model": "deepseek/deepseek-r1:free",
  "temperature": 0.7,
  "max_tokens": 400
}
```

---

## 💡 Features

- 🌟 **Real-time product recommendations** based on user queries
- 🧠 Powered by DeepSeek via OpenRouter
- 🧵 AI responses + Snapwear product links
- 🧲 Swagger + test script for local validation

---

## 🧠 Built With

- [FastAPI](https://fastapi.tiangolo.com/)
- [DeepSeek R1 via OpenRouter](https://openrouter.ai)
- [MongoDB](https://www.mongodb.com/) (Snapwear product catalog)
- [httpx](https://www.python-httpx.org/) for async API calls

---

## 📬 Contact

For help, questions, or collaboration:
**SnapWear Dev Team** — `dev@snapwear.com`
