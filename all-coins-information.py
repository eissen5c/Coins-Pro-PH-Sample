import hashlib
import hmac
import time
import requests

# API endpoint and parameters
endpoint = "/openapi/wallet/v1/config/getall"
api_key = "YOUR_API_KEY"
api_secret = "YOUR_API_SECRET"
recv_window = 5000
timestamp = int(time.time() * 1000)  # Current timestamp in milliseconds

# Create a string for the query parameters
query_string = f"recvWindow={recv_window}&timestamp={timestamp}"

# Create the HMAC SHA256 signature
signature = hmac.new(api_secret.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()

# Construct the full URL
url = f"https://api.example.com{endpoint}?{query_string}&signature={signature}"

# Set up headers
headers = {
    "X-MBX-APIKEY": api_key
}

# Perform the GET request
response = requests.get(url, headers=headers)

# Print the response
print(response.text)
