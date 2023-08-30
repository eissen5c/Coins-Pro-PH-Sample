import requests

# API endpoint and parameters
host = "https://api.pro.coins.ph/"
endpoint = "/openapi/v1/capital/withdraw/history"
params = {
    "coin": "BTC",  # Replace with the desired coin or leave empty for all coins
    "withdrawOrderId": "",  # Replace with the desired order ID or leave empty
    "status": 0,  # Replace with the desired status code
    "offset": 0,
    "limit": 1000,
    "startTime": None,  # Replace with the desired start time or leave as None
    "endTime": None,  # Replace with the desired end time or leave as None
    "recvWindow": 5000,  # Replace with the desired recvWindow value
    "timestamp": int(time.time() * 1000)  # Replace with your timestamp implementation
}

# Replace with your API key and secret
api_key = "YOUR_API_KEY"
api_secret = "YOUR_API_SECRET"

# Create a query string from the parameters
query_string = "&".join(f"{key}={value}" for key, value in params.items() if value is not None)

# Create a signature using your API secret and query string
signature = hmac.new(api_secret.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()

# Add the signature to the parameters
params['signature'] = signature

# Make the GET request
response = requests.get(host + endpoint, params=params, headers={"X-MBX-APIKEY": api_key})

# Print the response
print(response.json())
