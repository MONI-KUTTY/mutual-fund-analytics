import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------
# Load Datasets
# ---------------------------------

scorecard = pd.read_csv(
    r"D:\Mutual_Fund_Analytics\data\processed\fund_scorecard.csv"
)

fund_nav = pd.read_csv(
    r"D:\Mutual_Fund_Analytics\data\processed\02_nav_history_clean.csv"
)

daily_returns = pd.read_csv(
    r"D:\Mutual_Fund_Analytics\data\processed\daily_returns.csv"
)

benchmark = pd.read_csv(
    r"D:\Mutual_Fund_Analytics\data\processed\10_benchmark_indices_clean.csv"
)

# ---------------------------------
# Convert Dates
# ---------------------------------

fund_nav["date"] = pd.to_datetime(fund_nav["date"])

daily_returns["date"] = pd.to_datetime(daily_returns["date"])

benchmark["date"] = pd.to_datetime(benchmark["date"])

# ---------------------------------
# Select Top 5 Funds
# ---------------------------------

top5 = scorecard.head(5)["amfi_code"].tolist()

# ---------------------------------
# Plot NAV Comparison
# ---------------------------------

plt.figure(figsize=(14,7))

for fund in top5:

    temp = fund_nav[
        fund_nav["amfi_code"] == fund
    ]

    plt.plot(
        temp["date"],
        temp["nav"],
        label=str(fund)
    )

# Plot Nifty 50

nifty50 = benchmark[
    benchmark["index_name"] == "NIFTY50"
]

plt.plot(
    nifty50["date"],
    nifty50["close_value"],
    linestyle="--",
    linewidth=2,
    label="NIFTY50"
)

# Plot Nifty 100

nifty100 = benchmark[
    benchmark["index_name"] == "NIFTY100"
]

plt.plot(
    nifty100["date"],
    nifty100["close_value"],
    linestyle=":",
    linewidth=2,
    label="NIFTY100"
)

plt.title(
    "Top 5 Funds vs Nifty 50 & Nifty 100",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Date")

plt.ylabel("NAV / Index Value")

plt.legend()

plt.tight_layout()

plt.show()

# ---------------------------------
# Benchmark Daily Returns
# ---------------------------------

tracking = []

for benchmark_name in ["NIFTY50", "NIFTY100"]:

    bench = benchmark[
        benchmark["index_name"] == benchmark_name
    ].copy()

    bench = bench.sort_values("date")

    bench["benchmark_return"] = (
        bench["close_value"].pct_change()
    )

    bench = bench.dropna()

    for fund in top5:

        fund_data = daily_returns[
            daily_returns["amfi_code"] == fund
        ]

        merged = pd.merge(
            fund_data,
            bench[
                ["date", "benchmark_return"]
            ],
            on="date",
            how="inner"
        )

        tracking_error = (
            np.std(
                merged["daily_return"]
                -
                merged["benchmark_return"]
            )
            * np.sqrt(252)
        )

        tracking.append({

            "amfi_code": fund,

            "benchmark": benchmark_name,

            "tracking_error": tracking_error

        })

# ---------------------------------
# Create Tracking Error Table
# ---------------------------------

tracking_df = pd.DataFrame(tracking)

print("\nTracking Error Table\n")

print(tracking_df)

# ---------------------------------
# Save CSV
# ---------------------------------

output_file = r"D:\Mutual_Fund_Analytics\data\processed\tracking_error.csv"

tracking_df.to_csv(
    output_file,
    index=False
)

print("\nTracking Error file saved successfully!")

print(output_file)