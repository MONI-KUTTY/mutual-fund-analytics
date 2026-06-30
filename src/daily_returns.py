import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------
# Load Cleaned NAV Dataset
# ---------------------------------

file_path = r"D:\Mutual_Fund_Analytics\data\processed\02_nav_history_clean.csv"

df = pd.read_csv(file_path)

# ---------------------------------
# Convert Date Column to DateTime
# ---------------------------------

df["date"] = pd.to_datetime(df["date"])

# ---------------------------------
# Sort Data by AMFI Code and Date
# ---------------------------------

df = df.sort_values(
    by=["amfi_code", "date"]
)

# ---------------------------------
# Compute Daily Returns
# ---------------------------------

df["daily_return"] = (
    df.groupby("amfi_code")["nav"]
      .pct_change()
)

# ---------------------------------
# Remove First Record of Each Fund
# ---------------------------------

df = df.dropna(subset=["daily_return"])

# ---------------------------------
# Display First 10 Records
# ---------------------------------

print("First 10 Daily Returns:\n")

print(
    df[
        ["amfi_code", "date", "nav", "daily_return"]
    ].head(10)
)

# ---------------------------------
# Summary Statistics
# ---------------------------------

print("\nSummary Statistics:\n")

print(df["daily_return"].describe())

# ---------------------------------
# Plot Daily Return Distribution
# ---------------------------------

plt.figure(figsize=(10,6))

sns.histplot(
    df["daily_return"],
    bins=50,
    kde=True
)

plt.title(
    "Distribution of Daily Returns",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Daily Return")

plt.ylabel("Frequency")

plt.tight_layout()

# ---------------------------------
# Save Daily Returns Dataset
# ---------------------------------

output_file = r"D:\Mutual_Fund_Analytics\data\processed\daily_returns.csv"

df.to_csv(
    output_file,
    index=False
)

print("\nDaily Returns file saved successfully!")

print(output_file)

# ---------------------------------
# Display Histogram
# ---------------------------------

plt.show()