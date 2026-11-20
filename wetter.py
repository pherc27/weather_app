import requests

#KONSTANTEN
GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"

def get_coordinates(city):

    r_city = requests.get(f"{GEOCODING_URL}?"
                      f"name={city}&count=1&language=en&format=json")

    city_data = r_city.json()
    latitude = city_data["results"][0]["latitude"]
    longitude = city_data["results"][0]["longitude"]
    return latitude, longitude

def get_weather(latitude, longitude):

    r_weather = requests.get(f"{WEATHER_URL}?"
                             f"latitude={latitude}&longitude={longitude}&current=temperature_2m")

    weather_data = r_weather.json()

    weather = weather_data["current"]["temperature_2m"]
    return weather

def main():
    loop = True

    while loop:
        print("=" * 60)
        print("Von welcher Stadt wollen Sie die Temperatur wissen? // Zum Verlassen 'Q' eingeben")
        print("-" * 60)
        city = input().capitalize()
        if city != "Q":
            latitude, longitude = get_coordinates(city)
        
            weather = get_weather(latitude, longitude)
            print(weather)
        else:
            loop = False

if __name__ == "__main__":
    main()
