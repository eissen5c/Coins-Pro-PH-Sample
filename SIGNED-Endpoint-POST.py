# Import necessary modules
import requests  # For making HTTP requests
import hashlib   # For generating hash functions
import hmac      # For creating HMAC signatures
import time      # For working with time

# Define API key and secret key (replace with your actual keys)
api_key = 'tAQfOrPIZAhym0qHISRt8EFvxPemdBm5j5WMlkm3Ke9aFp0EGWC2CGM8GHV4kCYW'
secret_key = 'lH3ELTNiFxCQTmi9pPcWWikhsjO04Yoqw3euoHUuOLC3GYBW64ZqzQsiOEHXQS76'

# Define base URL for the API endpoint (replace $HOST with actual hostname)
base_url = 'https://$HOST/openapi/v1/order'

# Define order data parameters
data = {
    'symbol': 'ETHBTC',       # Trading symbol (e.g., ETHBTC)
    'side': 'BUY',            # Order side (BUY or SELL)
    'type': 'LIMIT',          # Order type (LIMIT or MARKET)
    'timeInForce': 'GTC',     # Time in force (GTC, GTT, IOC, FOK)
    'quantity': '1',          # Order quantity
    'price': '0.1',           # Order price
    'recvWindow': '5000',     # Recv window in milliseconds (adjust as needed)
}

# Calculate current timestamp in milliseconds
timestamp = int(time.time() * 1000)
data['timestamp'] = str(timestamp)

# Construct query string by joining key-value pairs
query_string = '&'.join([f'{key}={value}' for key, value in data.items()])

# Generate HMAC SHA256 signature using secret key
signature = hmac.new(secret_key.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()
data['signature'] = signature  # Add signature to data

# Define headers for the request
headers = {
    'X-COINS-APIKEY': api_key  # Include API key in headers
}

# Send HTTP POST request to the API endpoint
response = requests.post(base_url, headers=headers, data=data)

# Print the response from the server
print(response.text)
