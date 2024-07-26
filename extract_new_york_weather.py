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
columns = ["id", "main", "description", "icon"]
print(response["weather"])
new_yourk_df=pd.DataFrame(response["weather"],columns)
new_yourk_df.to_csv("city/new_york_weather.csv",index=False)

new_york_weather=pd.read_csv("city/new_york_weather.csv")
print(new_york_weather)
