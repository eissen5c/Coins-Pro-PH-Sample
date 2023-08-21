import requests

url = "https://api.pro.coins.ph/openapi/v1/ping"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error:", response.status_code)
