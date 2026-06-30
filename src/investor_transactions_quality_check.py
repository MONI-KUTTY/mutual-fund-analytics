import pandas as pd

df = pd.read_csv(
    r"D:\Mutual_Fund_Analytics\data\raw\08_investor_transactions.csv"
)

print("Columns:")
print(df.columns)

print("\nShape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nData Types:")
print(df.dtypes)

print("\nTransaction Types:")
print(df["transaction_type"].unique())

print("\nKYC Status Values:")
print(df["kyc_status"].unique())

print("\nSample Data:")
print(df.head())

print(
    "Invalid Amount Records:",
    (df["amount_inr"] <= 0).sum()
)