import requests
import pandas as pd

#API
url = "https://api.open-meteo.com/v1/forecast"

#using more than one city
cities = {
    "London": (51.51147, -0.13078308),
    "Manchester": (53.4809, -2.2374),
    "Edinburgh": (55.9521, -3.1965),
    "Birmingham":(52.4814, -1.8998)
}

#empty list to store all the weather data
weather_data = []

#for loop
for city, coordinates in cities.items():
    latitude, longitude = coordinates

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m,rain,wind_speed_10m"
    }


    response = requests.get(url, params=params)

    #Python
    data = response.json()
    

    #hourly
    hourly = data["hourly"]

    
    times = hourly["time"]
    temperatures = hourly["temperature_2m"]
    rain = hourly["rain"]
    wind_speeds = hourly["wind_speed_10m"]

    #second for loop
    for i in range(len(times)):
        weather_data.append({
            "city": city, 
            "time": times[i],
            "temperature": temperatures[i],
            "rain": rain[i],
            "wind_speed": wind_speeds[i]
        })

df = pd.DataFrame(weather_data)

print(df)

#save pandas table as a CSV file
df.to_csv("weather_data.csv", index=False)