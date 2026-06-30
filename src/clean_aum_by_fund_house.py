import pandas as pd

df = pd.read_csv(
    r"D:\Mutual_Fund_Analytics\data\raw\03_aum_by_fund_house.csv"
)

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Validate positive values
print("Invalid AUM:",
      (df["aum_crore"] <= 0).sum())

print("Invalid Schemes:",
      (df["num_schemes"] <= 0).sum())

# Save cleaned file
df.to_csv(
    r"D:\Mutual_Fund_Analytics\data\processed\03_aum_by_fund_house_clean.csv",
    index=False
)

print("03_aum_by_fund_house_clean.csv created successfully")