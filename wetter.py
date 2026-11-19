import requests


print("Temperatur von welcher Stadt wollen Sie wissen?")

current_city = input().capitalize()

r_city = requests.get("https://geocoding-api.open-meteo.com/v1/search?"
                      f"name={current_city}&count=1&language=en&format=json")

city_data = r_city.json()
# print(city_data)
#{'results': [{'id': 2950159, 'name': 'Berlin',
# 'latitude': 52.52437, 'longitude': 13.41053, 
# 'elevation': 74.0, 'feature_code': 'PPLC', 'country_code': 'DE', 
# 'admin1_id': 2950157, 'admin3_id': 6547383, 'admin4_id': 6547539, 'timezone': 'Europe/Berlin', 
# 'population': 3426354, 'postcodes': ['10967', '13347'], 'country_id': 2921044, 'country': 'Germany', 
# 'admin1': 'State of Berlin', 'admin3': 'Berlin, Stadt', 'admin4': 'Berlin'}], 'generationtime_ms': 0.15079975}


print("=" * 100)


current_latitude = city_data["results"][0]["latitude"]
current_longitude = city_data["results"][0]["longitude"]

r_weather = requests.get(f"https://api.open-meteo.com/v1/forecast?"
                 f"latitude={current_latitude}&longitude={current_longitude}&current=temperature_2m")

weather_data = r_weather.json()
# print(weather_data)
# {'latitude': 52.528915, 'longitude': 13.423877, 'generationtime_ms': 0.04017353057861328, 
# 'utc_offset_seconds': 0, 'timezone': 'GMT', 'timezone_abbreviation': 'GMT', 'elevation': 46.0, 
# 'current_units': {'time': 'iso8601', 'interval': 'seconds', 'temperature_2m': '°C'}, 
# 'current': {'time': '2026-11-19T16:00', 'interval': 900, 'temperature_2m': 9.7}}


current_weather = weather_data["current"]["temperature_2m"]
print(f"In {current_city} hat es {current_weather} Grad!")