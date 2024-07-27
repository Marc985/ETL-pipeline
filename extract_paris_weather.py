import requests
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

base_url=os.getenv("BASE_URL")
app_id=os.getenv("APP_ID")
base_params={
    "lat":"48.85714842768622",
    "lon":"2.3510475438011116",
    "appid":app_id
}
response=requests.get(base_url,params=base_params).json()
weather=response["weather"]
paris_df=pd.DataFrame(weather)
path="city/paris_weather.csv"

if os.path.exists(path):
   existing_weather_df=pd.read_csv(path)
   new_yourk_df=pd.concat([existing_weather_df,paris_df])
   new_yourk_df.to_csv(path,index=False)
else:
    paris_df.to_csv(path,index=False)
print(new_yourk_df)