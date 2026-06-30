import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------
# Load Cleaned Dataset
# ---------------------------------

file_path = r"D:\Mutual_Fund_Analytics\data\processed\05_category_inflows_clean.csv"

df = pd.read_csv(file_path)

# ---------------------------------
# Convert Month Column to DateTime
# ---------------------------------

df["month"] = pd.to_datetime(df["month"])

# ---------------------------------
# Convert Month to Year-Month Format
# ---------------------------------

df["month"] = df["month"].dt.strftime("%Y-%m")

# ---------------------------------
# Create Pivot Table
# ---------------------------------

heatmap_data = df.pivot(
    index="category",
    columns="month",
    values="net_inflow_crore"
)

# ---------------------------------
# Plot Heatmap
# ---------------------------------

plt.figure(figsize=(18,6))

sns.heatmap(
    heatmap_data,
    cmap="YlGnBu",
    annot=True,
    fmt=".0f",
    linewidths=0.5
)

# ---------------------------------
# Chart Title and Labels
# ---------------------------------

plt.title(
    "Monthly Category-wise Net Inflow Heatmap",
    fontsize=18,
    fontweight="bold"
)

plt.xlabel("Month", fontsize=14)

plt.ylabel("Fund Category", fontsize=14)

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()