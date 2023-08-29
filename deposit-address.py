import requests
import hashlib
import hmac
import time

# API endpoint
host = "https://api.pro.coins.ph"
endpoint = "/openapi/wallet/v1/deposit/address"

# API credentials
api_key = "your_api_key"
api_secret = "your_api_secret"

# Parameters
coin = "BTC"
network = "BTC"
timestamp = int(time.time() * 1000)  # Current timestamp in milliseconds

# Optional parameters
recvWindow = 5000  # You can adjust this value based on your needs

# Creating the query string
query_string = f"coin={coin}&network={network}&timestamp={timestamp}"
if recvWindow:
    query_string += f"&recvWindow={recvWindow}"

# Creating the signature
signature = hmac.new(api_secret.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()

# Constructing the final URL
url = f"{host}{endpoint}?{query_string}&signature={signature}"

# Making the API request
response = requests.get(url, headers={"X-Auth-API-Key": api_key})

# Handling the response
if response.status_code == 200:
    deposit_data = response.json()
    print("Deposit Address Data:")
    print(deposit_data)
else:
    print(f"Error: {response.status_code} - {response.text}")
