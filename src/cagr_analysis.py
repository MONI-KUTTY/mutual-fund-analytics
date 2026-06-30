import pandas as pd
import numpy as np
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
# CAGR Function
# ---------------------------------

def calculate_cagr(start_nav, end_nav, years):

    if start_nav <= 0 or end_nav <= 0:
        return np.nan

    return ((end_nav / start_nav) ** (1 / years)) - 1

# ---------------------------------
# Calculate CAGR for Each Fund
# ---------------------------------

results = []

for fund in df["amfi_code"].unique():

    fund_data = df[df["amfi_code"] == fund]

    fund_data = fund_data.sort_values("date")

    if len(fund_data) < 2:
        continue

    latest_nav = fund_data.iloc[-1]["nav"]

    cagr_1 = np.nan
    cagr_3 = np.nan
    cagr_5 = np.nan

    if len(fund_data) >= 252:
        start_nav = fund_data.iloc[-252]["nav"]
        cagr_1 = calculate_cagr(start_nav, latest_nav, 1)

    if len(fund_data) >= 756:
        start_nav = fund_data.iloc[-756]["nav"]
        cagr_3 = calculate_cagr(start_nav, latest_nav, 3)

    if len(fund_data) >= 1260:
        start_nav = fund_data.iloc[-1260]["nav"]
        cagr_5 = calculate_cagr(start_nav, latest_nav, 5)

    results.append({

        "amfi_code": fund,

        "cagr_1yr": cagr_1,

        "cagr_3yr": cagr_3,

        "cagr_5yr": cagr_5

    })

# ---------------------------------
# Create Comparison Table
# ---------------------------------

cagr_df = pd.DataFrame(results)

# Convert to Percentage

cagr_df["cagr_1yr"] = cagr_df["cagr_1yr"] * 100
cagr_df["cagr_3yr"] = cagr_df["cagr_3yr"] * 100
cagr_df["cagr_5yr"] = cagr_df["cagr_5yr"] * 100

# ---------------------------------
# Display Results
# ---------------------------------

print("\nCAGR Comparison Table\n")

print(cagr_df)

# ---------------------------------
# Save CSV
# ---------------------------------

output_file = r"D:\Mutual_Fund_Analytics\data\processed\cagr_comparison.csv"

cagr_df.to_csv(
    output_file,
    index=False
)

print("\nCAGR Comparison Table saved successfully!")

print(output_file)
plt.figure(figsize=(12,6))

cagr_df.set_index("amfi_code")[[
    "cagr_1yr",
    "cagr_3yr",
    "cagr_5yr"
]].plot(
    kind="bar",
    figsize=(14,6)
)

plt.title(
    "CAGR Comparison of All Mutual Funds",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("AMFI Code")

plt.ylabel("CAGR (%)")

plt.xticks(rotation=90)

plt.tight_layout()

plt.show()