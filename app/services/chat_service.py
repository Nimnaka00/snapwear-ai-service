import requests
import os

HUGGINGFACE_API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"
HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")

headers = {
    "Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"
}

def generate_reply(user_message: str) -> str:
    payload = {
        "inputs": user_message,
        "parameters": {"max_new_tokens": 100},
    }

    response = requests.post(HUGGINGFACE_API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        prediction = response.json()
        if isinstance(prediction, list) and "generated_text" in prediction[0]:
            return prediction[0]["generated_text"]
        else:
            return "👗 Sorry, I couldn't think of an answer right now!"
    else:
        return "🚨 Error contacting AI service. Please try again later."
