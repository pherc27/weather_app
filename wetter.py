import requests
import time

#KONSTANTEN
GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"

def get_coordinates(city):

    r_city = requests.get(f"{GEOCODING_URL}?"
                      f"name={city}&count=1&language=en&format=json")

    city_data = r_city.json()

    if "results" not in city_data: return None

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

    
    print("=" * 80)
    print("Von welcher Stadt wollen Sie die Temperatur wissen? // Zum Verlassen 'Q' eingeben")
    print("=" * 80)
    while True:
        city = input("Stadt eingeben (Q zum Beenden): ").capitalize()

        if city == "Q": break

        print("Lade Wetterdaten")
        time.sleep(1.5)
        
        coordinates = get_coordinates(city)
        if coordinates is None: 
            print("Diese Stadt gibt es nicht, versuche erneut")
            continue

        latitude, longitude = coordinates
    
        weather = get_weather(latitude, longitude)
        print(f"In {city} hat es {weather} Grad!")
        print("-" * 80)
        time.sleep(1)
            

if __name__ == "__main__":
    main()
