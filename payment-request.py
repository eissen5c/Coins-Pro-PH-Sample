import hashlib
import hmac
import time
import requests
from urllib.parse import urlencode

# Define your API credentials
api_key = "YOUR_API_KEY"
api_secret = "YOUR_API_SECRET"

# Define the base URL and endpoint
base_url = "https://api.pro.coins.ph"
endpoint = "/openapi/v3/payment-request/payment-requests"

# Define the payload parameters
payload = {
    "payer_contact_info": "user@example.com",
    "receiving_account": 1234567890,
    "amount": 100.00,
    "message": "Payment for services",
    "supported_payment_collectors": ["coins_peso_wallet"],
    "expires_at": "2023-09-01T12:00:00.000000Z",  # Set your desired expiration date
    "timestamp": int(time.time() * 1000)
}

# Create the query string
query_string = urlencode(payload)

# Create the signature
signature = hmac.new(api_secret.encode(), query_string.encode(), hashlib.sha256).hexdigest()

# Include the signature and API key in the payload
payload["signature"] = signature
payload["apiKey"] = api_key

# Send the POST request
response = requests.post(f"{base_url}{endpoint}", data=payload)

# Print the response
print(response.status_code)
print(response.json())
