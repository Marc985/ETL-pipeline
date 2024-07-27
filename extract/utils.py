import os
import pandas as pd
def extract(path,weather_data):
        weather_data.to_csv(path,index=False)
