import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------
# Load Cleaned NAV Dataset
# ---------------------------------

file_path = r"D:\Mutual_Fund_Analytics\data\processed\02_nav_history_clean.csv"

df = pd.read_csv(file_path)

# ---------------------------------
# Convert Date Column
# ---------------------------------

df["date"] = pd.to_datetime(df["date"])

# ---------------------------------
# Sort Data
# ---------------------------------

df = df.sort_values(
    by=["amfi_code", "date"]
)

# ---------------------------------
# Calculate Maximum Drawdown
# ---------------------------------

results = []

for fund in df["amfi_code"].unique():

    fund_data = df[
        df["amfi_code"] == fund
    ].copy()

    # Running Maximum NAV

    fund_data["running_max"] = (
        fund_data["nav"].cummax()
    )

    # Drawdown

    fund_data["drawdown"] = (
        fund_data["nav"]
        /
        fund_data["running_max"]
    ) - 1

    # Maximum Drawdown

    max_dd = fund_data["drawdown"].min()

    # Worst Drawdown Date

    worst_date = fund_data.loc[
        fund_data["drawdown"].idxmin(),
        "date"
    ]

    results.append({

        "amfi_code": fund,

        "maximum_drawdown": max_dd,

        "worst_drawdown_date": worst_date

    })

# ---------------------------------
# Create DataFrame
# ---------------------------------

drawdown_df = pd.DataFrame(results)

drawdown_df = drawdown_df.sort_values(
    by="maximum_drawdown"
)

# ---------------------------------
# Display Results
# ---------------------------------

print("\nMaximum Drawdown Table\n")

print(drawdown_df)

# ---------------------------------
# Save CSV
# ---------------------------------

output_file = r"D:\Mutual_Fund_Analytics\data\processed\maximum_drawdown.csv"

drawdown_df.to_csv(
    output_file,
    index=False
)

print("\nMaximum Drawdown file saved successfully!")

print(output_file)

# ---------------------------------
# Plot Maximum Drawdown
# ---------------------------------

plt.figure(figsize=(12,8))

plt.barh(
    drawdown_df["amfi_code"].astype(str),
    drawdown_df["maximum_drawdown"] * 100
)

plt.title(
    "Maximum Drawdown of Mutual Funds",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Maximum Drawdown (%)")

plt.ylabel("AMFI Code")

plt.tight_layout()

plt.show()