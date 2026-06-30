import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------
# Load Datasets
# ---------------------------------

cagr = pd.read_csv(
    r"D:\Mutual_Fund_Analytics\data\processed\cagr_comparison.csv"
)

sharpe = pd.read_csv(
    r"D:\Mutual_Fund_Analytics\data\processed\sharpe_ratio.csv"
)

alpha = pd.read_csv(
    r"D:\Mutual_Fund_Analytics\data\processed\alpha_beta.csv"
)

drawdown = pd.read_csv(
    r"D:\Mutual_Fund_Analytics\data\processed\maximum_drawdown.csv"
)

fund = pd.read_csv(
    r"D:\Mutual_Fund_Analytics\data\processed\01_fund_master_clean.csv"
)

# ---------------------------------
# Select Required Columns
# ---------------------------------

scorecard = cagr[
    ["amfi_code", "cagr_3yr"]
]

scorecard = scorecard.merge(
    sharpe[
        ["amfi_code", "sharpe_ratio"]
    ],
    on="amfi_code"
)

scorecard = scorecard.merge(
    alpha[
        ["amfi_code", "alpha"]
    ],
    on="amfi_code"
)

scorecard = scorecard.merge(
    drawdown[
        ["amfi_code", "maximum_drawdown"]
    ],
    on="amfi_code"
)

scorecard = scorecard.merge(
    fund[
        ["amfi_code", "expense_ratio_pct"]
    ],
    on="amfi_code"
)

# ---------------------------------
# Ranking
# ---------------------------------

scorecard["rank_cagr"] = (
    scorecard["cagr_3yr"]
    .rank(
        ascending=False,
        method="min"
    )
)

scorecard["rank_sharpe"] = (
    scorecard["sharpe_ratio"]
    .rank(
        ascending=False,
        method="min"
    )
)

scorecard["rank_alpha"] = (
    scorecard["alpha"]
    .rank(
        ascending=False,
        method="min"
    )
)

scorecard["rank_expense"] = (
    scorecard["expense_ratio_pct"]
    .rank(
        ascending=True,
        method="min"
    )
)

scorecard["rank_drawdown"] = (
    scorecard["maximum_drawdown"]
    .rank(
        ascending=False,
        method="min"
    )
)

# ---------------------------------
# Composite Score
# ---------------------------------

scorecard["fund_score"] = (

      (41 - scorecard["rank_cagr"]) * 0.30

    + (41 - scorecard["rank_sharpe"]) * 0.25

    + (41 - scorecard["rank_alpha"]) * 0.20

    + (41 - scorecard["rank_expense"]) * 0.15

    + (41 - scorecard["rank_drawdown"]) * 0.10

)

# ---------------------------------
# Convert Score to 100 Scale
# ---------------------------------

scorecard["fund_score"] = (

    scorecard["fund_score"]

    / scorecard["fund_score"].max()

) * 100

# ---------------------------------
# Final Ranking
# ---------------------------------

scorecard = scorecard.sort_values(

    by="fund_score",

    ascending=False

)

scorecard["overall_rank"] = range(

    1,

    len(scorecard) + 1

)

# ---------------------------------
# Display Results
# ---------------------------------

print("\nFund Scorecard\n")

print(scorecard)

# ---------------------------------
# Save CSV
# ---------------------------------

output_file = r"D:\Mutual_Fund_Analytics\data\processed\fund_scorecard.csv"

scorecard.to_csv(
    output_file,
    index=False
)

print("\nFund Scorecard saved successfully!")

print(output_file)

# ---------------------------------
# Plot Top 10 Funds
# ---------------------------------

top10 = scorecard.head(10)

plt.figure(figsize=(12,6))

plt.bar(

    top10["amfi_code"].astype(str),

    top10["fund_score"]

)

plt.title(

    "Top 10 Mutual Funds by Composite Score",

    fontsize=16,

    fontweight="bold"

)

plt.xlabel("AMFI Code")

plt.ylabel("Fund Score")

plt.tight_layout()

plt.show()