import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_reply(user_message: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use gpt-4 if you want premium
            messages=[
                {"role": "system", "content": "You are a professional fashion stylist. Give outfit recommendations based on user questions."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=300,
            temperature=0.7
        )
        reply = response.choices[0].message["content"].strip()
        return reply
    except Exception as e:
        print(f"OpenAI error: {e}")
        return "🚨 AI service is unavailable right now."
