import os
import httpx
from dotenv import load_dotenv
load_dotenv()

class DeepSeekChatService:
    def __init__(self):
        self.api_key = os.getenv("DEEPSEEK_API_KEY")
        self.api_url = os.getenv("DEEPSEEK_API_URL")
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        self.backend_url = os.getenv("SNAPWEAR_BACKEND_URL")

    async def search_products(self, keywords):
        async with httpx.AsyncClient() as client:
            results = []
            for keyword in keywords:
                response = await client.get(f"{self.backend_url}/api/products/search", params={"keyword": keyword})
                if response.status_code == 200:
                    results.extend(response.json())
            # Deduplicate by product ID
            return {prod["_id"]: prod for prod in results}.values()

    async def chat_completion(self, messages, model="deepseek/deepseek-r1:free", temperature=0.7, max_tokens=250):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                self.api_url,
                headers=self.headers,
                json={
                    "model": model,
                    "messages": messages,
                    "temperature": temperature,
                    "max_tokens": max_tokens
                },
                timeout=30.0
            )
            if response.status_code != 200:
                raise Exception(f"API request failed with status {response.status_code}: {response.text}")
            return response.json()

    async def generate_response_with_products(self, chat_request):
        # Get AI's understanding of the request
        ai_response = await self.chat_completion(
            messages=[m.dict() for m in chat_request.messages],
            model=chat_request.model,
            temperature=chat_request.temperature,
            max_tokens=chat_request.max_tokens
        )
        raw_reply = ai_response["choices"][0]["message"]["content"]

        # Simple keyword extraction (can be improved with NLP)
        user_input = next((m.content for m in chat_request.messages if m.role == "user"), "")
        keywords = [word.strip(",.") for word in user_input.lower().split() if len(word) > 3]

        products = await self.search_products(keywords)

        # Build product link responses
        product_links = ""
        for p in list(products)[:5]:  # limit to 5
            link = f"<a href='http://localhost:3000/products/{p['_id']}' target='_blank'>{p['name']}</a>"
            product_links += f"• {link}<br>"

        full_response = raw_reply
        if product_links:
            full_response += "\n\nHere are some items you might like:<br>" + product_links

        return {
            "response": full_response,
            "model": ai_response["model"],
            "usage": ai_response["usage"]
        }
