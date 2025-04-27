import openai
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def generate_reply(user_message: str) -> str:
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a professional fashion stylist helping customers with outfit recommendations."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=300,
            temperature=0.7
        )
        reply = response.choices[0].message.content.strip()
        return reply
    except Exception as e:
        print(f"OpenAI API error: {e}")
        return "🚨 Sorry, I couldn't generate a response right now."
