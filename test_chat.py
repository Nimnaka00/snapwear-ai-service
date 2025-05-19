import requests

url = "http://localhost:8000/api/v1/chat"
payload = {
    "messages": [
        {"role": "system", "content": "You are a fashion assistant for Snapwear."},
        {"role": "user", "content": "What should I wear to a wedding?"}
    ],
    "model": "deepseek-ai/deepseek-r1",
    "temperature": 0.7,
    "max_tokens": 500
}

response = requests.post(url, json=payload)

if response.status_code == 200:
    print("✅ Test passed! Status code:", response.status_code)
    print("Response:", response.json())
else:
    print("❌ Test failed. Status code:", response.status_code)
    print("Details:", response.text)