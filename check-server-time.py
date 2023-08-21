# Import the 'requests' library, which allows sending HTTP requests and receiving responses.
import requests

# Define the URL of the API endpoint to send the GET request to.
url = "https://api.pro.coins.ph/openapi/v1/time"

# Send a GET request to the specified URL and store the response in the 'response' variable.
response = requests.get(url)

# Check if the status code of the response is equal to 200 (HTTP OK).
if response.status_code == 200:
    # If the response status code is 200, parse the response content as JSON and store it in the 'data' variable.
    data = response.json()
    # Print the parsed JSON data to the console.
    print(data)
else:
    # If the response status code is not 200, print an error message along with the actual status code received from the server.
    print("Error:", response.status_code)
