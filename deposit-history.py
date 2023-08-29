import time
import hashlib
import hmac
import requests

# Define your API key and secret
api_key = "YOUR_API_KEY"
api_secret = "YOUR_API_SECRET"

# Define the base URL for the API
base_url = "https://api.pro.coins.ph"

# Define the endpoint for fetching deposit history
endpoint = "/openapi/wallet/v1/deposit/history"

# Define the parameters for the request
params = {
    "coin": "BTC",
    "status": 1,
    "startTime": int(time.time()) - (90 * 24 * 60 * 60),  # 90 days ago in seconds
    "endTime": int(time.time()),
    "offset": 0,
    "limit": 1000,
    "timestamp": int(time.time() * 1000),
}

# Create the query string from the parameters
query_string = "&".join(f"{key}={params[key]}" for key in sorted(params))

# Create the full URL for the request
url = f"{base_url}{endpoint}?{query_string}"

# Create the HMAC SHA256 signature
signature = hmac.new(api_secret.encode("utf-8"), query_string.encode("utf-8"), hashlib.sha256).hexdigest()

# Set the request headers
headers = {
    "X-MKT-APIKEY": api_key,
    "X-MKT-SIGNATURE": signature,
}

# Make the GET request
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    deposit_history = response.json()
    print(deposit_history)
else:
    print(f"Request failed with status code: {response.status_code}")
    print(response.text)
