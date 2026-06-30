import pandas as pd

df = pd.read_csv(
    r"D:\Mutual_Fund_Analytics\data\raw\05_category_inflows.csv"
)

# Convert month
df["month"] = pd.to_datetime(df["month"])

# Save cleaned file
df.to_csv(
    r"D:\Mutual_Fund_Analytics\data\processed\05_category_inflows_clean.csv",
    index=False
)

print("05_category_inflows_clean.csv created successfully")