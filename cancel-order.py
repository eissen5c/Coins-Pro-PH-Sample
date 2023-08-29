import time
import hmac
import hashlib
import requests

# API endpoint and key information
base_url = "https://api.pro.coins.ph"
api_key = "your_api_key"
api_secret = "your_api_secret"

# Function to create a signed request
def create_signed_request(endpoint, params):
    params['timestamp'] = int(time.time() * 1000)
    query_string = '&'.join([f"{k}={v}" for k, v in params.items()])
    signature = hmac.new(api_secret.encode(), query_string.encode(), hashlib.sha256).hexdigest()
    headers = {
        'CB-ACCESS-KEY': api_key,
        'CB-ACCESS-SIGN': signature,
        'CB-ACCESS-TIMESTAMP': str(params['timestamp']),
    }
    response = requests.delete(f"{base_url}{endpoint}?{query_string}", headers=headers)
    return response

# Cancel order function
def cancel_order(order_id=None, orig_client_order_id=None):
    endpoint = "/openapi/v1/order"
    params = {}
    if order_id:
        params['orderId'] = order_id
    elif orig_client_order_id:
        params['origClientOrderId'] = orig_client_order_id
    else:
        raise ValueError("Either orderId or origClientOrderId must be provided.")
    
    response = create_signed_request(endpoint, params)
    return response.json()

# Example usage
try:
    result = cancel_order(order_id=12345)
    print("Order canceled successfully:", result)
except Exception as e:
    print("Error:", e)
