import requests
import random
import json

GOOGLE = "https://www.google.com/"
FACEBOOK = "https://www.facebook.com/"
TWITTER = "https://twitter.com/"
AMAZON = "https://www.amazon.com/"
APPLE = "https://www.apple.com/"
ALL = [GOOGLE, FACEBOOK, TWITTER, AMAZON, APPLE]
while True:
    for item in ALL:
        res = requests.get(random.choice(ALL))
        print(f"url:{item}, status_code:{res.status_code}, html_length:{len(res.text)}")

import requests

while True:
    WEATHER_API = "https://api.open-meteo.com/v1/forecast?"
    CITY_API = "https://geocoding-api.open-meteo.com/v1/search"
    name = input("Enter a name of a city here: ")
    r_2 = requests.get(f"{CITY_API}?name={name.title()}&language=en&count=10&format=json")
    data = r_2.json()
    results = data.get("results")
    dict = results[0]
    r = requests.get(f"{WEATHER_API}latitude={dict['latitude']}&longitude={dict['longitude']}&hourly=temperature_2m")
    data_2 = r.json()
    print(data_2)

