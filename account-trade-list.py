import requests
import hashlib
import hmac
import time

# API key and secret
api_key = 'your_api_key'
api_secret = 'your_api_secret'

# API endpoint
base_url = 'https://api.pro.coins.ph'
endpoint = '/openapi/v1/myTrades'

# Parameters
symbol = 'BTC-PHP'
timestamp = int(time.time() * 1000)
query_params = {
    'symbol': symbol,
    'timestamp': timestamp
}

# Create signature
query_string = '&'.join([f'{key}={value}' for key, value in query_params.items()])
signature = hmac.new(api_secret.encode(), query_string.encode(), hashlib.sha256).hexdigest()

# Add signature to query parameters
query_params['signature'] = signature

# Send GET request
response = requests.get(base_url + endpoint, params=query_params, headers={'X-MBX-APIKEY': api_key})
data = response.json()

# Print the response data
print(data)
