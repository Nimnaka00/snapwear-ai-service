# 🧠 SnapWear AI Service

This is a FastAPI-based backend service for SnapWear's **AI Stylist Chatbot**. It uses OpenAI's GPT model to give smart outfit advice and fashion recommendations.

---

## 📁 Project Structure

```
snapwear-ai-service/
│
├── app/
│   ├── api/v1/
│   │   └── chat_routes.py         # API routes
│   ├── models/
│   │   └── chat_model.py          # Request/response models
│   ├── services/
│   │   └── chat_service.py        # OpenAI logic
│   └── main.py                    # FastAPI app entry point
│
├── .env                           # Environment variables
├── .gitignore
├── requirements.txt              # Python dependencies
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
source venv/bin/activate         # macOS/Linux
venv\Scripts\activate            # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment

Create a `.env` file with your OpenAI API key:

```
OPENAI_API_KEY=your_openai_key_here
```

---

## 🚀 Run the Server

```bash
uvicorn main:app --reload --app-dir app
```

Visit:
- Swagger Docs: [http://localhost:8000/docs](http://localhost:8000/docs)
- Chat Endpoint: `POST /api/v1/chat`

---

## 🧪 Sample Chat API

### Request
`POST http://localhost:8000/api/v1/chat`

**Headers:**
```http
Content-Type: application/json
```

**Body:**
```json
{
  "message": "Can you suggest a party outfit?"
}
```

### Response
```json
{
  "reply": "Sure! Try a sleek black dress with silver heels and a clutch. Add a bold red lip!"
}
```

---

## 🧠 Built With

- [FastAPI](https://fastapi.tiangolo.com/)
- [OpenAI GPT-3.5](https://platform.openai.com/docs)

---

## 💡 Tip

You can test the API using Swagger at `/docs` or Postman. Make sure your `.env` is properly configured.

---

## 📬 Contact

For help or issues, please contact the SnapWear dev team.
