import time
import hashlib
import hmac
import requests

# API credentials
api_key = 'YOUR_API_KEY'
api_secret = 'YOUR_API_SECRET'

# API endpoint
host = 'https://api.pro.coins.ph'
endpoint = '/openapi/v1/order'

# Request parameters
order_id = 12345  # Replace with the actual order ID
orig_client_order_id = None  # Replace with the original client order ID if available
timestamp = int(time.time() * 1000)
recv_window = 5000  # Replace with the desired recvWindow value

# Construct the query string
query_string = f"orderId={order_id}&origClientOrderId={orig_client_order_id}&recvWindow={recv_window}&timestamp={timestamp}"

# Generate HMAC signature
signature = hmac.new(api_secret.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()

# Construct headers
headers = {
    'X-COINS-APIKEY': api_key
}

# Construct the full URL
url = f"{host}{endpoint}?{query_string}&signature={signature}"

# Send GET request
response = requests.get(url, headers=headers)

# Print the response
print(response.json())
