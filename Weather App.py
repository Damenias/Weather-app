import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"].title(),
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
        return weather
    else:
        print("❌ Error:", data.get("message", "Unable to fetch weather."))
        return None

# --- Main Program ---
if __name__ == "__main__":
    API_KEY = "3da22ba3adcae300c20d8f4ef631d5ba"  # actual key
    city_name = input("Enter a city name: ")     
    weather = get_weather(city_name, API_KEY)

    if weather:
        print(f"\n🌤 Weather in {weather['city']}:")
        print(f"🌡 Temperature: {weather['temperature']}°C")
        print(f"☁ Condition: {weather['description']}")
        print(f"💧 Humidity: {weather['humidity']}%")
        print(f"💨 Wind Speed: {weather['wind_speed']} m/s")

