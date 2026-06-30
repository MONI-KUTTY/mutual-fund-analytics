import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------
# Load Cleaned Dataset
# ---------------------------------

file_path = r"D:\Mutual_Fund_Analytics\data\processed\03_aum_by_fund_house_clean.csv"

df = pd.read_csv(file_path)

# ---------------------------------
# Convert Date Column to DateTime
# ---------------------------------

df["date"] = pd.to_datetime(df["date"])

# ---------------------------------
# Extract Year
# ---------------------------------

df["year"] = df["date"].dt.year

# ---------------------------------
# Filter Years (2022–2025)
# ---------------------------------

df = df[
    (df["year"] >= 2022) &
    (df["year"] <= 2025)
]

# ---------------------------------
# Create Plot
# ---------------------------------

plt.figure(figsize=(16,8))

sns.barplot(
    data=df,
    x="year",
    y="aum_crore",
    hue="fund_house"
)

# ---------------------------------
# Titles and Labels
# ---------------------------------

plt.title(
    "AUM Growth by Fund House (2022–2025)",
    fontsize=18,
    fontweight="bold"
)

plt.xlabel("Year", fontsize=14)

plt.ylabel("AUM (₹ Crore)", fontsize=14)

plt.xticks(fontsize=12)

plt.yticks(fontsize=12)

plt.legend(
    title="Fund House",
    bbox_to_anchor=(1.02,1),
    loc="upper left"
)

# ---------------------------------
# Highlight SBI Dominance
# ---------------------------------

plt.text(
    2.8,
    df["aum_crore"].max()*0.95,
    "SBI MF ~ ₹12.5 Lakh Crore",
    fontsize=12,
    color="red",
    fontweight="bold"
)

plt.tight_layout()

plt.show()