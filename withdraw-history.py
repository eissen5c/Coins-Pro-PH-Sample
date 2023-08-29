import time
import hashlib
import hmac
import requests

# API base URL
BASE_URL = "https://api.pro.coins.ph"

# API endpoint
ENDPOINT = "/openapi/wallet/v1/withdraw/history"

# Your API Key and Secret
API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_API_SECRET"

# Current timestamp
timestamp = int(time.time() * 1000)

# Request parameters
params = {
    "coin": "BTC",
    "withdrawOrderId": "123456",
    "status": 0,
    "startTime": timestamp - (90 * 24 * 60 * 60 * 1000),  # 90 days ago
    "endTime": timestamp,
    "offset": 0,
    "limit": 100,
    "recvWindow": 5000,
    "timestamp": timestamp,
}

# Create a query string
query_string = "&".join([f"{key}={params[key]}" for key in params])

# Create a signature using HMAC SHA256
signature = hmac.new(
    bytes(API_SECRET.encode("utf-8")),
    msg=bytes(query_string.encode("utf-8")),
    digestmod=hashlib.sha256,
).hexdigest()

# Add the signature to the query string
query_string += f"&signature={signature}"

# Construct the full URL
url = BASE_URL + ENDPOINT + "?" + query_string

# Make the GET request
response = requests.get(url, headers={"X-BH-APIKEY": API_KEY})

# Print the response
print(response.json())
