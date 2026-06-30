import pandas as pd

df = pd.read_csv(
    r"D:\Mutual_Fund_Analytics\data\raw\07_scheme_performance.csv"
)

print("Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

# Check return columns
return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

print("\nReturn Column Types:")
print(df[return_cols].dtypes)

# Expense Ratio Check
invalid_expense = (
    (df["expense_ratio_pct"] < 0.1)
    |
    (df["expense_ratio_pct"] > 2.5)
).sum()

print("\nExpense Ratio Outside Range:")
print(invalid_expense)

# Return Anomaly Check
anomalies = df[
    (df["return_1yr_pct"] > 100)
    | (df["return_1yr_pct"] < -100)
    | (df["return_3yr_pct"] > 100)
    | (df["return_3yr_pct"] < -100)
    | (df["return_5yr_pct"] > 100)
    | (df["return_5yr_pct"] < -100)
]

print("\nReturn Anomalies:")
print(len(anomalies))