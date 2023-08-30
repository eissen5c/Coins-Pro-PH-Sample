import requests
import hashlib
import hmac
import time

# API endpoint and parameters
BASE_URL = "https://api.pro.coins.ph"
ENDPOINT = "/openapi/v1/historyOrders"
API_KEY = "your_api_key"
API_SECRET = "your_api_secret"
SYMBOL = "BTCUSDT"  # Change this to the desired symbol
LIMIT = 500
RECV_WINDOW = 5000
TIMESTAMP = int(time.time() * 1000)

# Generate HMAC SHA256 signature
query_string = f"symbol={SYMBOL}&limit={LIMIT}&recvWindow={RECV_WINDOW}&timestamp={TIMESTAMP}"
signature = hmac.new(API_SECRET.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()

# Construct request URL
url = f"{BASE_URL}{ENDPOINT}?{query_string}&signature={signature}"

# Construct request headers
headers = {
    "X-MBX-APIKEY": API_KEY
}

# Make the GET request
response = requests.get(url, headers=headers)

# Handle the response
if response.status_code == 200:
    data = response.json()
    print("History Orders:")
    for order in data:
        print(order)
else:
    print(f"Error: {response.status_code} - {response.text}")
