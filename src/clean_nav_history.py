import pandas as pd

# Load Raw Dataset
file_path = r"D:\Mutual_Fund_Analytics\data\raw\02_nav_history.csv"

df = pd.read_csv(file_path)

print("Original Shape:", df.shape)

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Sort by AMFI code and date
df = df.sort_values(
    by=["amfi_code", "date"]
)

# Validation Checks
print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nInvalid NAV Records:")
print((df["nav"] <= 0).sum())

# Save Cleaned Dataset
output_file = (
    r"D:\Mutual_Fund_Analytics\data\processed"
    r"\nav_history_clean.csv"
)

df.to_csv(output_file, index=False)

print("\nCleaned file saved successfully:")
print(output_file)