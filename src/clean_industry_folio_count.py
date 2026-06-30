import pandas as pd

df = pd.read_csv(
    r"D:\Mutual_Fund_Analytics\data\raw\06_industry_folio_count.csv"
)

# Convert month
df["month"] = pd.to_datetime(df["month"])

# Save cleaned file
df.to_csv(
    r"D:\Mutual_Fund_Analytics\data\processed\06_industry_folio_count_clean.csv",
    index=False
)

print("06_industry_folio_count_clean.csv created successfully")