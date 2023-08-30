import requests
import time
import hashlib
import hmac

# API base URL
BASE_URL = "https://api.pro.coins.ph"

# API endpoint for withdrawal
ENDPOINT = "/openapi/v1/capital/withdraw/apply"

# API key and secret (replace with your actual API credentials)
API_KEY = "your_api_key"
API_SECRET = "your_api_secret"

# User data
USER_DATA = {
    "coin": "BTC",                  # Replace with the desired coin
    "amount": "0.01",              # Replace with the withdrawal amount
    "withdrawOrderId": "123456",   # Optional: client order id
    "recvWindow": 5000,            # Optional: recvWindow value
    "timestamp": int(time.time() * 1000)
}

# Create a sorted, query string of parameters
query_string = '&'.join([f"{key}={USER_DATA[key]}" for key in sorted(USER_DATA.keys())])

# Generate the signature
signature = hmac.new(API_SECRET.encode(), query_string.encode(), hashlib.sha256).hexdigest()

# Add the signature to the user data
USER_DATA["signature"] = signature

# Send the POST request
response = requests.post(BASE_URL + ENDPOINT, data=USER_DATA, headers={"X-MBX-APIKEY": API_KEY})

# Print the response
print(response.json())
