import requests

current_city = "Wiesbaden"
wiesbaden_latitude = 50.08
wiesbaden_longitude = 8.24

r = requests.get(f"https://api.open-meteo.com/v1/forecast?"
                 f"latitude={wiesbaden_latitude}&longitude={wiesbaden_longitude}&current=temperature_2m")

data = r.json()

temperature_wiesbaden = data["current"]["temperature_2m"]
print(f"In {current_city} hat es {temperature_wiesbaden} Grad!")