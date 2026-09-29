# UK Weather Data Analysis

## Overview

This project is a Python-based weather data analysis project using the **Open-Meteo API**.

It collects 7 days of hourly weather data for four UK cities:

* London
* Manchester
* Edinburgh
* Birmingham

The project analyses temperature, rainfall and wind speed and uses graphs to compare the weather between cities.

## Technologies Used

* Python
* Requests
* Pandas
* Matplotlib
* Open-Meteo API

## What the Project Does

* Collects weather data from the Open-Meteo API.
* Retrieves hourly temperature, rainfall and wind-speed data.
* Stores the data in a Pandas DataFrame.
* Saves the collected data as a CSV file.
* Calculates average, minimum and maximum temperatures.
* Calculates total rainfall and average wind speed.
* Counts the number of rainy hours for each city.
* Identifies the warmest, coldest and rainiest cities.
* Creates graphs to compare weather conditions.

## Visualisations

The project creates:

* A bar chart comparing average temperatures between cities.
* A line graph showing temperature changes over the 7-day forecast.

## Files

```text
UK-Weather-Analysis/
│
├── weather_analysis.py
├── weather_data.csv
└── README.md
```

## How to Run

Install the required libraries:

```bash
pip install requests pandas matplotlib
```

Then run the Python file:

```bash
python weather_analysis.py
```

The program will collect the weather data, analyse it and display the graphs.

## What I Learnt

Through this project, I practised:

* Working with APIs
* Using Python loops and conditional statements
* Working with Pandas DataFrames
* Grouping and analysing data
* Exporting data to CSV
* Creating graphs using Matplotlib
* Basic API error handling

## Data Source

Weather data is provided by the **Open-Meteo API**.

https://open-meteo.com/
