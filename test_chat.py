import requests

url = "http://localhost:8000/api/v1/chat"
payload = {
    "message": "What should I wear to a wedding?"
}

response = requests.post(url, json=payload)

if response.status_code == 200:
    print("✅ Test passed! Status code:", response.status_code)
    print("Response:", response.json())
else:
    print("❌ Test failed. Status code:", response.status_code)
    print("Details:", response.text)
