import requests

# API endpoint and parameters
host = "https://api.pro.coins.ph"
endpoint = "/openapi/v1/capital/deposit/history"
params = {
    "coin": "BTC",  # Replace with the desired coin
    "depositOrderId": "",  # Optional: Provide client order id if needed
    "status": 0,  # Optional: Set the desired status code
    "offset": 0,
    "limit": 1000,  # Optional: Set the desired limit (max 1000)
    "startTime": None,  # Optional: Set the start time in milliseconds
    "endTime": None,  # Optional: Set the end time in milliseconds
    "recvWindow": None,  # Optional: Set the recvWindow value
    "timestamp": 0  # Replace with the actual timestamp
}

# Make the API request
response = requests.get(host + endpoint, params=params)

# Print the response
print(response.json())
