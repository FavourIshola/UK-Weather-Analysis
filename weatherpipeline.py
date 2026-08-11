import requests
import pandas as pd

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
print("Wind Speed:", current["wind_speed_10m"], "km/h")

#pandas table
weather = {
    "time": current["time"],
    "temperature": current["temperature_2m"],
    "rain": current["rain"],
    "wind_speed": current["wind_speed_10m"]
}
#taking my weather data and turning it into a DataFrame(table)
df = pd.DataFrame([weather])
print(df)

#save pandas table as a CSV file
df.to_csv("weather_data.csv", index=False)