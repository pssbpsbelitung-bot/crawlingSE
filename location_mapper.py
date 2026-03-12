import pandas as pd
from geopy.geocoders import Nominatim
import time

geolocator = Nominatim(user_agent="belitung_map")

df = pd.read_csv("data/discovered_accounts.csv")

lat_list = []
lon_list = []

for text in df["caption"]:

    try:

        location = geolocator.geocode(text)

        if location:

            lat_list.append(location.latitude)
            lon_list.append(location.longitude)

        else:

            lat_list.append(None)
            lon_list.append(None)

    except:

        lat_list.append(None)
        lon_list.append(None)

    time.sleep(1)

df["lat"] = lat_list
df["lon"] = lon_list

df.to_csv("data/map_ready_data.csv",index=False)

print("Map data selesai dibuat")