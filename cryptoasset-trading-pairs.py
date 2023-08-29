import requests

def get_trading_pairs():
    # API endpoint URL
    base_url = "https://api.pro.coins.ph"
    endpoint = "/openapi/v1/pairs"
    url = base_url + endpoint

    try:
        response = requests.get(url)
        if response.status_code == 200:
            trading_pairs_data = response.json()
            return trading_pairs_data
        else:
            print(f"Request failed with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    trading_pairs = get_trading_pairs()
    if trading_pairs:
        print("Cryptoasset Trading Pairs:")
        for pair in trading_pairs:
            print(f"Base: {pair['base']} - Quote: {pair['quote']}")

