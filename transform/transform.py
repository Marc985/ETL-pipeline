import pandas as pd
import os
def transform_weather_data(weather_data,city_name):
    weather_df=pd.DataFrame(weather_data)
    path=f"city/{city_name}_weather.csv"
    if os.path.exists(path):
        existing_weather_df=pd.read_csv(path)
        new_yourk_df=pd.concat([existing_weather_df,weather_df])
        new_yourk_df.to_csv(path,index=False)
    else:
        weather_df.to_csv(path,index=False)
    print(new_yourk_df)