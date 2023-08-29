import time
import hashlib
import hmac
import requests

# API base URL
BASE_URL = "https://api.pro.coins.ph/"

# User data
USER_DATA = {
    "coin": "BTC",
    "network": "BTC",
    "address": "your_btc_address",
    "addressTag": "optional_address_tag",
    "amount": 0.5,
    "withdrawOrderId": "your_withdraw_order_id",
    "recvWindow": 5000,
    "timestamp": int(time.time() * 1000)
}

# API secret key
API_SECRET = "your_api_secret_key"

# Generate the query string
query_string = "&".join([f"{key}={USER_DATA[key]}" for key in sorted(USER_DATA.keys())])

# Generate the signature using HMAC SHA256
signature = hmac.new(API_SECRET.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()

# Add the signature to the user data
USER_DATA["signature"] = signature

# Construct the full URL
url = BASE_URL + "openapi/wallet/v1/withdraw/apply"

# Make the POST request
response = requests.post(url, data=USER_DATA)

# Print the response
print(response.json())
