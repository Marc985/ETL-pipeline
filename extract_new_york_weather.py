import requests
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

base_url=os.getenv("BASE_URL")
app_id=os.getenv("APP_ID")
base_params={
    "lat":"40.71210132463293",
    "lon":"-74.01241338211616",
    "appid":app_id
}

response=requests.get(base_url,params=base_params).json()
weather=response["weather"]

new_yourk_df=pd.DataFrame(weather)
path="city/new_york_weather.csv"

if os.path.exists(path):
   existing_weather_df=pd.read_csv(path)
   new_yourk_df=pd.concat([existing_weather_df,new_yourk_df])
   new_yourk_df.to_csv(path,index=False)
else:
    new_yourk_df.to_csv(path,index=False)
print(new_yourk_df)

