import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# ---------------------------------
# Load Daily Returns
# ---------------------------------

fund_df = pd.read_csv(
    r"D:\Mutual_Fund_Analytics\data\processed\daily_returns.csv"
)

benchmark_df = pd.read_csv(
    r"D:\Mutual_Fund_Analytics\data\processed\10_benchmark_indices_clean.csv"
)

# ---------------------------------
# Convert Date Columns
# ---------------------------------

fund_df["date"] = pd.to_datetime(fund_df["date"])

benchmark_df["date"] = pd.to_datetime(
    benchmark_df["date"]
)

# ---------------------------------
# Filter Nifty 100
# ---------------------------------

benchmark_df = benchmark_df[
    benchmark_df["index_name"] == "NIFTY100"
]

# ---------------------------------
# Compute Benchmark Daily Returns
# ---------------------------------

benchmark_df = benchmark_df.sort_values("date")

benchmark_df["benchmark_return"] = (
    benchmark_df["close_value"]
    .pct_change()
)

benchmark_df = benchmark_df.dropna()

# ---------------------------------
# Alpha Beta Calculation
# ---------------------------------

results = []

for fund in fund_df["amfi_code"].unique():

    temp = fund_df[
        fund_df["amfi_code"] == fund
    ]

    merged = pd.merge(
        temp,
        benchmark_df[
            ["date", "benchmark_return"]
        ],
        on="date",
        how="inner"
    )

    if len(merged) < 30:
        continue

    slope, intercept, r_value, p_value, std_err = linregress(

        merged["benchmark_return"],

        merged["daily_return"]

    )

    alpha = intercept * 252

    beta = slope

    results.append({

        "amfi_code": fund,

        "alpha": alpha,

        "beta": beta,

        "r_squared": r_value ** 2

    })

# ---------------------------------
# Create DataFrame
# ---------------------------------

alpha_beta_df = pd.DataFrame(results)

alpha_beta_df = alpha_beta_df.sort_values(
    by="alpha",
    ascending=False
)

# ---------------------------------
# Display Results
# ---------------------------------

print("\nAlpha Beta Table\n")

print(alpha_beta_df)

# ---------------------------------
# Save CSV
# ---------------------------------

output_file = r"D:\Mutual_Fund_Analytics\data\processed\alpha_beta.csv"

alpha_beta_df.to_csv(
    output_file,
    index=False
)

print("\nAlpha Beta file saved successfully!")

print(output_file)

# ---------------------------------
# Plot Alpha
# ---------------------------------

plt.figure(figsize=(12,8))

plt.barh(
    alpha_beta_df["amfi_code"].astype(str),

    alpha_beta_df["alpha"]
)

plt.title(
    "Alpha of Mutual Funds",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Alpha")

plt.ylabel("AMFI Code")

plt.tight_layout()

plt.show()