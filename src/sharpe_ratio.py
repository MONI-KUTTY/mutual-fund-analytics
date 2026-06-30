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
# Calculate Sharpe Ratio
# ---------------------------------

results = []

for fund in df["amfi_code"].unique():

    fund_data = df[df["amfi_code"] == fund]

    mean_return = fund_data["daily_return"].mean()

    std_return = fund_data["daily_return"].std()

    if std_return == 0:
        sharpe = np.nan
    else:
        sharpe = (
            (mean_return - daily_rf)
            / std_return
        ) * np.sqrt(252)

    results.append({

        "amfi_code": fund,

        "average_daily_return": mean_return,

        "risk_std_dev": std_return,

        "sharpe_ratio": sharpe

    })

# ---------------------------------
# Create DataFrame
# ---------------------------------

sharpe_df = pd.DataFrame(results)

# ---------------------------------
# Rank Funds
# ---------------------------------

sharpe_df = sharpe_df.sort_values(
    by="sharpe_ratio",
    ascending=False
)

sharpe_df["rank"] = range(
    1,
    len(sharpe_df) + 1
)

# ---------------------------------
# Display Results
# ---------------------------------

print("\nSharpe Ratio Ranking\n")

print(sharpe_df)

# ---------------------------------
# Save CSV
# ---------------------------------

output_file = r"D:\Mutual_Fund_Analytics\data\processed\sharpe_ratio.csv"

sharpe_df.to_csv(
    output_file,
    index=False
)

print("\nSharpe Ratio file saved successfully!")

print(output_file)
plt.figure(figsize=(12,8))

plt.barh(
    sharpe_df["amfi_code"].astype(str),
    sharpe_df["sharpe_ratio"]
)

plt.title(
    "Sharpe Ratio Ranking of Mutual Funds",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Sharpe Ratio")

plt.ylabel("AMFI Code")

plt.tight_layout()

plt.show()