import os
import pandas as pd
def extract(path,weather_data):
        if os.path.exists(path):
            existing_weather_df=pd.read_csv(path)
            new_yourk_df=pd.concat([existing_weather_df,weather_data])
            new_yourk_df.to_csv(path,index=False)
        else:
            weather_data.to_csv(path,index=False)
