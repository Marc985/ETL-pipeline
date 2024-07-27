import pandas as pd
import os
new_york_df=pd.read_csv("../dags/city/new_york_weather.csv")
paris_df=pd.read_csv("../dags/city/paris_weather.csv")
tokyo_df=pd.read_csv("../dags/city/tokyo_weather.csv")

new_york_df["city"]="New York"
paris_df["city"]="Paris"
tokyo_df["city"]="Tokyo"
weather_data=pd.concat([new_york_df,paris_df,tokyo_df],ignore_index=True)
weather_data.to_csv("../dags/transformed_data/weather_data.csv",index=False)

print(weather_data)