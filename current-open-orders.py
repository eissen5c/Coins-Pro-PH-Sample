import requests
import time
import hashlib
import hmac

# API endpoint
base_url = "https://api.pro.coins.ph"
endpoint = "/openapi/v1/openOrders"

# API keys
api_key = "YOUR_API_KEY"
api_secret = "YOUR_API_SECRET"

# Parameters
symbol = "BTCUSDT"  # Change this to the desired symbol
timestamp = int(time.time() * 1000)
recv_window = 5000  # Set the desired recvWindow value

# Prepare the query parameters
params = {
    "symbol": symbol,
    "recvWindow": recv_window,
    "timestamp": timestamp
}

# Create a query string
query_string = '&'.join([f"{key}={params[key]}" for key in params])

# Generate the signature
signature = hmac.new(api_secret.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()

# Construct the full URL
url = f"{base_url}{endpoint}?{query_string}&signature={signature}"

# Add the API Key to headers
headers = {
    "X-MBX-APIKEY": api_key
}

# Make the GET request
response = requests.get(url, headers=headers)

# Print the response
print(response.json())
