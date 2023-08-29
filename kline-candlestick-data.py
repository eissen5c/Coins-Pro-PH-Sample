import requests

# API base URL
base_url = "https://api.pro.coins.ph/"

# Endpoint for Kline/candlestick data
endpoint = "/openapi/quote/v1/klines"

# Parameters
params = {
    "symbol": "BTCUSDT",     # Replace with the desired symbol
    "interval": "1h",        # Replace with the desired interval
    "limit": 500             # Optional: Set the desired limit
    # You can add "startTime" and "endTime" if needed
}

# Make the GET request
response = requests.get(base_url + endpoint, params=params)

# Check if the request was successful
if response.status_code == 200:
    klines_data = response.json()
    print(klines_data)
else:
    print(f"Request failed with status code: {response.status_code}")
