import requests
import os
from dotenv import load_dotenv

load_dotenv()

base_url=os.getenv("BASE_URL")
app_id=os.getenv("APP_ID")
base_params={
    "lat":"48.85714842768622",
    "lon":"2.3510475438011116",
    "appid":app_id
}
response=requests.get(base_url,params=base_params).json()
print(response)