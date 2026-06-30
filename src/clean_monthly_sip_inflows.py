import pandas as pd

df = pd.read_csv(
    r"D:\Mutual_Fund_Analytics\data\raw\04_monthly_sip_inflows.csv"
)

# Convert month
df["month"] = pd.to_datetime(df["month"])

# Fill missing YoY growth values
df["yoy_growth_pct"] = (
    df["yoy_growth_pct"]
    .fillna(0)
)

# Save cleaned file
df.to_csv(
    r"D:\Mutual_Fund_Analytics\data\processed\04_monthly_sip_inflows_clean.csv",
    index=False
)

print("04_monthly_sip_inflows_clean.csv created successfully")