import requests

url = "http://localhost:8000/api/v1/chat"
payload = {
    "messages": [
        {
            "role": "system",
            "content": "You are a helpful AI fashion assistant for Snapwear. Be concise and clear in your recommendations."
        },
        {
            "role": "user",
            "content": "What outfit do you recommend for a summer beach party?"
        }
    ],
    "model": "deepseek/deepseek-r1:free",
    "temperature": 0.7,
    "max_tokens": 400
}

response = requests.post(url, json=payload)

if response.status_code == 200:
    print("✅ Test passed! Status code:", response.status_code)
    print("Response:\n", response.json()["response"])
else:
    print("❌ Test failed. Status code:", response.status_code)
    print("Details:", response.text)
