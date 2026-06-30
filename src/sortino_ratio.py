import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------
# Load Daily Returns Dataset
# ---------------------------------

file_path = r"D:\Mutual_Fund_Analytics\data\processed\daily_returns.csv"

df = pd.read_csv(file_path)

# ---------------------------------
# Risk-Free Rate
# ---------------------------------

risk_free_rate = 0.065

daily_rf = risk_free_rate / 252

# ---------------------------------
# Calculate Sortino Ratio
# ---------------------------------

results = []

for fund in df["amfi_code"].unique():

    fund_data = df[df["amfi_code"] == fund]

    mean_return = fund_data["daily_return"].mean()

    downside_returns = fund_data[
        fund_data["daily_return"] < 0
    ]["daily_return"]

    downside_std = downside_returns.std()

    if downside_std == 0 or np.isnan(downside_std):
        sortino = np.nan
    else:
        sortino = (
            (mean_return - daily_rf)
            / downside_std
        ) * np.sqrt(252)

    results.append({

        "amfi_code": fund,

        "average_daily_return": mean_return,

        "downside_std_dev": downside_std,

        "sortino_ratio": sortino

    })

# ---------------------------------
# Create DataFrame
# ---------------------------------

sortino_df = pd.DataFrame(results)

# ---------------------------------
# Rank Funds
# ---------------------------------

sortino_df = sortino_df.sort_values(
    by="sortino_ratio",
    ascending=False
)

sortino_df["rank"] = range(
    1,
    len(sortino_df) + 1
)

# ---------------------------------
# Display Results
# ---------------------------------

print("\nSortino Ratio Ranking\n")

print(sortino_df)

# ---------------------------------
# Save CSV
# ---------------------------------

output_file = r"D:\Mutual_Fund_Analytics\data\processed\sortino_ratio.csv"

sortino_df.to_csv(
    output_file,
    index=False
)

print("\nSortino Ratio file saved successfully!")

print(output_file)

# ---------------------------------
# Plot Ranking
# ---------------------------------

plt.figure(figsize=(12,8))

plt.barh(
    sortino_df["amfi_code"].astype(str),
    sortino_df["sortino_ratio"]
)

plt.title(
    "Sortino Ratio Ranking of Mutual Funds",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Sortino Ratio")

plt.ylabel("AMFI Code")

plt.tight_layout()

plt.show()