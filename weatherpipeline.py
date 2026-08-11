import requests

#API
url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude" : 51.51147,
    "longitude" : -0.13078308,
    "current" : "temperature_2m,rain,wind_speed_10m"
}

response = requests.get(url, params=params)

#Python
data = response.json()

#current
current = data["current"]

#temperature, rain, wind
print("Time:", current["time"])
print("Temperature:", current["temperature_2m"], "°C")
print("Rain:", current["rain"], "mm")
print("Wind:", current["wind_speed_10m"], "km/h")


