import requests

# API base URL
base_url = "https://api.pro.coins.ph/"

# Endpoint path
endpoint_path = "/openapi/quote/v1/ticker/price"

# Construct the full URL
url = base_url + endpoint_path

# Parameters
params = {
    "symbol": "BTCUSDT"  # Example symbol
}

# Make the GET request
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    
    # Extract and print the latest price
    if "symbol" in params:
        symbol = params["symbol"]
        price = data.get(symbol)
        print(f"Latest price for {symbol}: {price}")
    else:
        for symbol, price in data.items():
            print(f"Latest price for {symbol}: {price}")
else:
    print(f"Request failed with status code: {response.status_code}")
