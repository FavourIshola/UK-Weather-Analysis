import requests
import pandas as pd
import matplotlib.pyplot as plt

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
        "hourly": "temperature_2m,rain,wind_speed_10m",
        "forecast_days": 7
    }


    response = requests.get(url, params=params)

    #if statement FOR ERROR HANDLING
    if response.status_code == 200: #200 means everything worked
        data = response.json()
    else:
        print("Could not get weather for", city)
        continue

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

#groupby separate my data by city. mean is for average 
#making a graph using Pandas to show the avarages
average_temperature = df.groupby("city")["temperature"].mean()
average_temperature.plot(kind= "bar")
plt.title("Average Temperature by UK City")
plt.xlabel("City")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

#calculating the summary
city_sum = df.groupby("city").agg({
    "temperature": ["mean", "min", "max"],
    "rain": "sum", 
    "wind_speed": "mean"
})
city_sum = city_sum.round(2) #rounding it up

print("\n Weather summary by city:")
print(city_sum)

#calculating number of rainy hours
rainy_hours = df[df["rain"] > 0].groupby("city").size()
print("\nNumber of rainy hours:")
print(rainy_hours)