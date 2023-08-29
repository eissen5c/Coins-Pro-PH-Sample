import time
import requests
import hashlib
import hmac

# API endpoint
base_url = "https://api.pro.coins.ph"
endpoint = "/openapi/v1/openOrders"

# API credentials
api_key = "YOUR_API_KEY"
api_secret = b"YOUR_API_SECRET"

# Symbol to cancel orders for
symbol = "BTC-PHP"

# Other parameters
recvWindow = 5000  # Set as needed
timestamp = int(time.time() * 1000)  # Current timestamp in milliseconds

# Create the query string
query_string = f"symbol={symbol}&recvWindow={recvWindow}&timestamp={timestamp}"

# Create the HMAC SHA256 signature
signature = hmac.new(api_secret, query_string.encode('utf-8'), hashlib.sha256).hexdigest()

# Construct the request URL
url = f"{base_url}{endpoint}?{query_string}&signature={signature}"

# Construct headers
headers = {
    "X-MKT-APIKEY": api_key
}

# Send the DELETE request to cancel orders
response = requests.delete(url, headers=headers)

# Process the response
if response.status_code == 200:
    print("All open orders on the symbol have been canceled successfully.")
else:
    print(f"Failed to cancel orders. Status code: {response.status_code}")
    print("Response:", response.text)
