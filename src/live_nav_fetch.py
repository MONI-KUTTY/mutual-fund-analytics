import requests
import pandas as pd
import os

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    nav_df = pd.DataFrame(data["data"])

    output_file = r"D:\Mutual_Fund_Analytics\data\raw\hdfc_top100_nav.csv"

    nav_df.to_csv(output_file, index=False)

    print("CSV saved successfully")
    print(nav_df.head())

else:
    print("API request failed:", response.status_code)