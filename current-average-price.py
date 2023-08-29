import requests

# API base URL
base_url = "https://api.pro.coins.ph/"

# Endpoint for current average price
endpoint = "/openapi/quote/v1/avgPrice"

# Symbol to retrieve average price for
symbol = "BTCUSDT"  # Replace with the desired symbol

# Construct the complete URL
url = base_url + endpoint

# Query parameters
params = {
    "symbol": symbol
}

try:
    # Sending GET request to the API
    response = requests.get(url, params=params)

    # Checking if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        average_price = data["avgPrice"]
        print(f"Current average price for {symbol}: {average_price}")
    else:
        print(f"Error: {response.status_code} - {response.text}")
except requests.RequestException as e:
    print(f"An error occurred: {e}")
