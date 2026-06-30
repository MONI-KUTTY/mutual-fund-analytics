import pandas as pd

# Load Raw Dataset
file_path = r"D:\Mutual_Fund_Analytics\data\raw\08_investor_transactions.csv"

df = pd.read_csv(file_path)

print("Original Shape:", df.shape)

# Convert transaction_date to datetime
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)

# Validation Checks
print("\nMissing Values:")
print(df.isnull().sum())

print("\nTransaction Types:")
print(df["transaction_type"].unique())

print("\nKYC Status Values:")
print(df["kyc_status"].unique())

print("\nInvalid Amount Records:")
print((df["amount_inr"] <= 0).sum())

# Save Cleaned Dataset
output_file = (
    r"D:\Mutual_Fund_Analytics\data\processed"
    r"\investor_transactions_clean.csv"
)

df.to_csv(output_file, index=False)

print("\nCleaned file saved successfully:")
print(output_file)