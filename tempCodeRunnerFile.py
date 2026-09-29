#warmest and coldest city
warmest_city = average_temperature.idxmax()
coldest_city = average_temperature.idxmin()
print("\nWarmest city:")
print(warmest_city)

print("\nColdest city:")
print(coldest_city)

#city with the most rainfall
rainiest_city = city_sum["rain"] ["sum"].idxmax()
print("\nCity with the most rainfall:")
print(rainiest_city)

#line graph to compare temperatures over the 7 days
for city in cities:
    city_data = df[df["city"] == city]
    plt.plot(city_data ["time"], city_data ["temperature"], label=city)

plt.title ("7-Day Temperature Forecast")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.xticks(rotation = 45)
plt.tight_layout()
plt.show()