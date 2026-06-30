import pandas as pd

df = pd.read_csv(
    r"D:\Mutual_Fund_Analytics\data\raw\09_portfolio_holdings.csv"
)

# Convert portfolio date
df["portfolio_date"] = pd.to_datetime(
    df["portfolio_date"]
)

# Validation checks
print("Invalid Weight:",
      (df["weight_pct"] <= 0).sum())

print("Invalid Market Value:",
      (df["market_value_cr"] <= 0).sum())

print("Invalid Price:",
      (df["current_price_inr"] <= 0).sum())

# Save cleaned file
df.to_csv(
    r"D:\Mutual_Fund_Analytics\data\processed\09_portfolio_holdings_clean.csv",
    index=False
)

print("09_portfolio_holdings_clean.csv created successfully")