import requests
import hashlib
import hmac
import time

# API information
BASE_URL = "https://api.pro.coins.ph/"
API_KEY = "YOUR_API_KEY"
SECRET_KEY = b'YOUR_SECRET_KEY'

# Endpoint and parameters
endpoint = "/openapi/v1/asset/tradeFee"
params = {
    'symbol': 'BTC-PHP',  # Example symbol
    'recvWindow': 5000,
    'timestamp': int(time.time() * 1000)
}

# Create the query string
query_string = '&'.join([f"{key}={value}" for key, value in params.items()])

# Create the HMAC SHA256 signature
signature = hmac.new(SECRET_KEY, query_string.encode('utf-8'), hashlib.sha256).hexdigest()

# Add the signature to the parameters
params['signature'] = signature

# Make the GET request
response = requests.get(BASE_URL + endpoint, params=params, headers={'X-MBX-APIKEY': API_KEY})

# Print the response
print(response.json())
