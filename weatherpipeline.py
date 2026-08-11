import requests
import pandas as pd

#API
url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude" : 51.51147,
    "longitude" : -0.13078308,
    "hourly" : "temperature_2m,rain,wind_speed_10m"
}

response = requests.get(url, params=params)

#Python
data = response.json()

#hourly
hourly = data["hourly"]

#temperature, rain, wind
times = hourly["time"]
temperatures = hourly["temperature_2m"]
rain = hourly["rain"]
wind_speed = hourly["wind_speed_10m"]

#pandas table
df = pd.DataFrame({
    "time": times,
    "temperature": temperatures,
    "rain": rain,
    "wind_speed": wind_speed
})

print(df)

#save pandas table as a CSV file
df.to_csv("weather_data.csv", index=False)