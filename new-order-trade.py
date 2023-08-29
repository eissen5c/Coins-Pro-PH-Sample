import time
import hashlib
import hmac
import requests

# Replace with your actual API key and secret
API_KEY = "your_api_key"
API_SECRET = "your_api_secret"

BASE_URL = "https://api.pro.coins.ph"

def generate_signature(query_params):
    query_string = '&'.join([f'{k}={v}' for k, v in query_params.items()])
    return hmac.new(API_SECRET.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()

def create_order(symbol, side, type, timeInForce=None, quantity=None, quoteOrderQty=None,
                 price=None, newClientOrderId=None, stopPrice=None, newOrderRespType=None,
                 stpFlag=None, recvWindow=None):
    endpoint = "/openapi/v1/order"

    query_params = {
        "symbol": symbol,
        "side": side,
        "type": type,
        "timeInForce": timeInForce,
        "quantity": quantity,
        "quoteOrderQty": quoteOrderQty,
        "price": price,
        "newClientOrderId": newClientOrderId,
        "stopPrice": stopPrice,
        "newOrderRespType": newOrderRespType,
        "stpFlag": stpFlag,
        "recvWindow": recvWindow,
        "timestamp": int(time.time() * 1000)  # Current timestamp in milliseconds
    }

    signature = generate_signature(query_params)
    query_params["signature"] = signature

    response = requests.post(BASE_URL + endpoint, params=query_params, headers={"X-MBX-APIKEY": API_KEY})

    return response.json()

if __name__ == "__main__":
    symbol = "BTCUSDT"
    side = "BUY"
    type = "LIMIT"
    quantity = 0.01
    price = 45000
    newOrderRespType = "FULL"
    timestamp = int(time.time() * 1000)

    order_response = create_order(symbol, side, type, quantity=quantity, price=price, newOrderRespType=newOrderRespType, timestamp=timestamp)

    print("Order Response:")
    print(order_response)
