import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------
# Load Cleaned Dataset
# ---------------------------------

file_path = r"D:\Mutual_Fund_Analytics\data\processed\08_investor_transactions_clean.csv"

df = pd.read_csv(file_path)

sns.set_style("whitegrid")

# ======================================================
# 1. Horizontal Bar Chart - SIP Amount by State
# ======================================================

sip_df = df[df["transaction_type"] == "SIP"]

state_sip = (
    sip_df.groupby("state")["amount_inr"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(12,8))

sns.barplot(
    x=state_sip.values,
    y=state_sip.index
)

plt.title(
    "Total SIP Investment Amount by State",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Total SIP Amount (₹)")

plt.ylabel("State")

plt.tight_layout()

plt.show()

# ======================================================
# 2. T30 vs B30 City Tier Pie Chart
# ======================================================

plt.figure(figsize=(8,8))

city_tier = df["city_tier"].value_counts()

plt.pie(
    city_tier,
    labels=city_tier.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title(
    "Investor Distribution by City Tier (T30 vs B30)",
    fontsize=16,
    fontweight="bold"
)

plt.tight_layout()

plt.show()