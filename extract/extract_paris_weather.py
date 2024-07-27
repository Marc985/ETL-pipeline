import requests
import os
from dotenv import load_dotenv
import pandas as pd
from extract_utils import extract

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
path="../dags/city/paris_weather.csv"
extract(path,paris_df)
