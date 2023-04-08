import requests
import random
import json

url = (["https://www.google.com/", "https://www.facebook.com/",
        "https://twitter.com/", "https://www.amazon.com/", "https://www.apple.com/"])

for item in url:
    res = requests.get(random.choice(url))
    print(f"url:{item}, status_code:{res.status_code}, html_length:{len(res.text)}")


WEATHER_API = "https://api.open-meteo.com/v1/forecast?"
CITY_API = "https://geocoding-api.open-meteo.com/v1/search"
name = input("Enter a name of a city here: ")
try:
    geo_response = requests.get(f"{CITY_API}?name={name.title()}&language=en&count=10&format=json")
    geo_data = geo_response.json()
    geo_results = geo_data.get("results")
    city_geo_data = geo_results[0]
except TypeError:
    print("No such city")
else:
    r = requests.get(f"{WEATHER_API}latitude={city_geo_data['latitude']}&longitude={city_geo_data['longitude']}"
                     f"&current_weather=true")
    weather_data = r.json().get("current_weather")
    print(weather_data)

