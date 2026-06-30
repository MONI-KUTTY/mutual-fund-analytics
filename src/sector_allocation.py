import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------
# Load Cleaned Dataset
# ---------------------------------

file_path = r"D:\Mutual_Fund_Analytics\data\processed\09_portfolio_holdings_clean.csv"

df = pd.read_csv(file_path)

# ---------------------------------
# Aggregate Sector Weights
# ---------------------------------

sector_weights = (
    df.groupby("sector")["weight_pct"]
    .sum()
    .sort_values(ascending=False)
)

# ---------------------------------
# Create Donut Chart
# ---------------------------------

plt.figure(figsize=(10,10))

plt.pie(
    sector_weights,
    labels=sector_weights.index,
    autopct="%1.1f%%",
    startangle=90,
    pctdistance=0.85
)

# Create Donut Hole
centre_circle = plt.Circle(
    (0,0),
    0.70,
    fc="white"
)

fig = plt.gcf()

fig.gca().add_artist(centre_circle)

# ---------------------------------
# Chart Title
# ---------------------------------

plt.title(
    "Sector Allocation Across All Equity Funds",
    fontsize=16,
    fontweight="bold"
)

plt.tight_layout()

plt.show()