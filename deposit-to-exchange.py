import requests
import time
import hashlib
import hmac

# API information
base_url = "https://api.pro.coins.ph"
endpoint = "/openapi/v1/capital/deposit/apply"
api_key = "your_api_key_here"
api_secret = "your_api_secret_here"

# Parameters for the deposit request
coin = "BTC"
amount = "0.1"
depositOrderId = "123456"  # Optional
recvWindow = 5000
timestamp = int(time.time() * 1000)  # Current timestamp in milliseconds

# Create the request payload
payload = {
    "coin": coin,
    "amount": amount,
    "depositOrderId": depositOrderId,
    "recvWindow": recvWindow,
    "timestamp": timestamp
}

# Create the query string
query_string = '&'.join([f'{key}={payload[key]}' for key in payload])
signature_payload = f'{endpoint}?{query_string}'

# Generate the HMAC signature
signature = hmac.new(api_secret.encode('utf-8'), signature_payload.encode('utf-8'), hashlib.sha256).hexdigest()

# Add the signature to the payload
payload['signature'] = signature

# Make the POST request
url = f'{base_url}{endpoint}?{query_string}&signature={signature}'
headers = {'X-MBX-APIKEY': api_key}
response = requests.post(url, headers=headers)

# Print the response
print(response.json())
