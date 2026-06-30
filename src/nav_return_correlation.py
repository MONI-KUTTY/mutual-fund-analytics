import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------
# Load Cleaned Dataset
# ---------------------------------

file_path = r"D:\Mutual_Fund_Analytics\data\processed\02_nav_history_clean.csv"

df = pd.read_csv(file_path)

# ---------------------------------
# Convert Date Column
# ---------------------------------

df["date"] = pd.to_datetime(df["date"])

# ---------------------------------
# Select First 10 Mutual Funds
# ---------------------------------

selected_funds = df["amfi_code"].unique()[:10]

df = df[df["amfi_code"].isin(selected_funds)]

# ---------------------------------
# Pivot NAV Data
# ---------------------------------

pivot_df = df.pivot(
    index="date",
    columns="amfi_code",
    values="nav"
)

# ---------------------------------
# Calculate Daily Returns
# ---------------------------------

daily_returns = pivot_df.pct_change().dropna()

# ---------------------------------
# Correlation Matrix
# ---------------------------------

correlation_matrix = daily_returns.corr()

# ---------------------------------
# Plot Heatmap
# ---------------------------------

plt.figure(figsize=(10,8))

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5
)

plt.title(
    "Correlation Matrix of Daily NAV Returns (10 Selected Funds)",
    fontsize=16,
    fontweight="bold"
)

plt.tight_layout()

plt.show()