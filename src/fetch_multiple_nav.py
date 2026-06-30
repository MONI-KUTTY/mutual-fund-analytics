import requests
import pandas as pd
import os

schemes = {
    "sbi_bluechip": 119551,
    "icici_bluechip": 120503,
    "nippon_large_cap": 118632,
    "axis_bluechip": 119092,
    "kotak_bluechip": 120841
}

output_folder = r"D:\Mutual_Fund_Analytics\data\raw"

for fund_name, scheme_code in schemes.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    print(f"Fetching {fund_name}...")

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        file_path = os.path.join(
            output_folder,
            f"{fund_name}_nav.csv"
        )

        nav_df.to_csv(file_path, index=False)

        print(f"Saved: {file_path}")

    else:
        print(f"Failed for {fund_name}")