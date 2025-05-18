import requests

API_KEY = "cb61e61deca4c9538e556334e2f6d51f" 
CITY = "Dubai"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    print("Weather Data:", data)
else:
    print("Failed to retrieve data. Error Code:", response.status_code)
    print("Error Message:", response.text)
