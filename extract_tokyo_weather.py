import requests
import os
from dotenv import load_dotenv

load_dotenv()

base_url=os.getenv("BASE_URL")
app_id=os.getenv("APP_ID")
base_params={
    "lat":"35.6828",
    "lon":"139.7595",
    "appid":app_id
}
response=requests.get(base_url,params=base_params).json()
print(response)