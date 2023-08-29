import requests

# API endpoint and parameters
host = "https://api.pro.coins.ph/"
endpoint = "/openapi/quote/v1/trades"
params = {
    "symbol": "BTCUSDT",
    "limit": 500
}

# Checking and adjusting the limit parameter
limit = params["limit"]
if limit <= 0 or limit > 1000:
    params["limit"] = 1000

# Making the GET request
response = requests.get(host + endpoint, params=params)

# Handling the response
if response.status_code == 200:
    trades = response.json()
    # Process the list of trades as needed
    for trade in trades:
        print(trade)  # Replace this with your desired processing logic
else:
    print("Error:", response.status_code)
    print("Response:", response.text)
