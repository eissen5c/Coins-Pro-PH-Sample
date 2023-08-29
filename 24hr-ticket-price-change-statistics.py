import requests

# API endpoint and base URL
BASE_URL = "https://api.pro.coins.ph"
TICKER_ENDPOINT = "/openapi/quote/v1/ticker/24hr"

# Define the parameters
params = {
    "symbol": "BTCUSDT",  # Example symbol, you can change this
    # "symbols": ["BTCUSDT", "ETHUSDT"],  # Use either 'symbol' or 'symbols', not both
}

# Make the API request
response = requests.get(BASE_URL + TICKER_ENDPOINT, params=params)

# Check if the request was successful
if response.status_code == 200:
    ticker_data = response.json()
    
    # Print the ticker data
    print("Ticker Data:")
    print(ticker_data)
    
else:
    print(f"Error: {response.status_code} - {response.text}")
