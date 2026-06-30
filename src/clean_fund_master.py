import pandas as pd

df = pd.read_csv(
    r"D:\Mutual_Fund_Analytics\data\raw\01_fund_master.csv"
)

# Convert launch_date to datetime
df["launch_date"] = pd.to_datetime(df["launch_date"])

# Save cleaned file
df.to_csv(
    r"D:\Mutual_Fund_Analytics\data\processed\01_fund_master_clean.csv",
    index=False
)

print("01_fund_master_clean.csv created successfully")