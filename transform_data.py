import requests

API_KEY = "cb61e61deca4c9538e556334e2f6d51f"
CITY = "London"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)

if response.status_code == 200:
    data = response.json()

    # Extracted useful info
    transformed = {
        "city": data["name"],
        "country": data["sys"]["country"],
        "temperature": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "condition": data["weather"][0]["description"],
        "wind_speed": data["wind"]["speed"]
    }

    print("Transformed Weather Data:")
    for key, value in transformed.items():
        print(f"{key.capitalize()}: {value}")
else:
    print("Failed to retrieve data. Status code:", response.status_code)
