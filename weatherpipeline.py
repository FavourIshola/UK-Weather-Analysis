import requests

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude" : 51.51147,
    "longitude" : -0.13078308,
    "current" : "temperature_2m,rain,wind_speed_10m"
}

response = requests.get(url, params=params)
print(response.json())