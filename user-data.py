import requests
import hashlib
import hmac
import time

# Define the API endpoint URL
url = "https://api.pro.coins.ph/openapi/wallet/v1/config/getall?recvWindow=DATA_HERE&timestamp=DATA_HERE"

# Replace these with your actual API key and secret
api_key = "YOUR_API_KEY"
api_secret = "YOUR_API_SECRET"

# Generate a timestamp for the request
timestamp = str(int(time.time() * 1000))

# Create the HMAC SHA256 signature
signature_payload = f"{timestamp}.{api_key}"
signature = hmac.new(api_secret.encode('utf-8'), signature_payload.encode('utf-8'), hashlib.sha256).hexdigest()

# Set up the headers for the request
headers = {
    "X-Timestamp": timestamp,
    "X-API-KEY": api_key,
    "X-SIGNATURE": signature
}

# Send the GET request with headers
response = requests.get(url, headers=headers)

# Check the response status code
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error:", response.status_code)
