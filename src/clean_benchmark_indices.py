import pandas as pd

df = pd.read_csv(
    r"D:\Mutual_Fund_Analytics\data\raw\10_benchmark_indices.csv"
)

# Convert date
df["date"] = pd.to_datetime(df["date"])

# Validate close value
print("Invalid Close Values:",
      (df["close_value"] <= 0).sum())

# Save cleaned file
df.to_csv(
    r"D:\Mutual_Fund_Analytics\data\processed\10_benchmark_indices_clean.csv",
    index=False
)

print("10_benchmark_indices_clean.csv created successfully")