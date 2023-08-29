import requests

# API endpoint
base_url = "https://api.pro.coins.ph/"
endpoint = "/openapi/quote/v1/ticker/bookTicker"

# Function to get ticker book data
def get_ticker_book_data(symbol=None, symbols=None):
    # Construct the URL with parameters
    url = f"{base_url}{endpoint}"
    
    # Prepare parameters based on provided inputs
    params = {}
    if symbol:
        params["symbol"] = symbol
    if symbols:
        params["symbols"] = symbols
    
    # Make the GET request
    response = requests.get(url, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Test the function with examples
symbol_data = get_ticker_book_data(symbol="BTCUSDT")
print("Ticker book data for symbol BTCUSDT:")
print(symbol_data)

symbols_data = get_ticker_book_data(symbols=["BTCUSDT", "BNBUSDT"])
print("\nTicker book data for symbols BTCUSDT and BNBUSDT:")
print(symbols_data)
