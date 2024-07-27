import requests
import os
from dotenv import load_dotenv
import pandas as pd
from .utils import extract


def extract_new_york_weather_data():

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
    extract(path,new_yourk_df)


