import requests

# API base URL
base_url = "https://api.pro.coins.ph/"

# Endpoint for fetching order book depth
endpoint = "/openapi/quote/v1/depth"

# Parameters
params = {
    "symbol": "BTCUSD",  # Replace with the desired symbol
    "limit": 100  # You can change this value as needed
}

# Sending GET request
response = requests.get(base_url + endpoint, params=params)

# Handling response
if response.status_code == 200:
    order_book_data = response.json()
    # Process the order book data as needed
    print(order_book_data)
else:
    print("Error:", response.status_code)
    print(response.text)
