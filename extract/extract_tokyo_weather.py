import requests
import os
from dotenv import load_dotenv
import pandas as pd
from pathlib import Path
from .utils import extract

def extract_tokyo_weather_data():
    load_dotenv()

    base_url=os.getenv("BASE_URL")
    app_id=os.getenv("APP_ID")
    base_params={
        "lat":"35.6828",
        "lon":"139.7595",
        "appid":app_id
    }
    response=requests.get(base_url,params=base_params).json()
    weather=response["weather"]
    tokyo_df=pd.DataFrame(weather)
    path=Path("city/tokyo_weather.csv")

    extract(path,tokyo_df)
