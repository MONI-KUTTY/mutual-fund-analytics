import pandas as pd
import plotly.express as px

# ---------------------------------
# Load Cleaned Dataset
# ---------------------------------

file_path = r"D:\Mutual_Fund_Analytics\data\processed\06_industry_folio_count_clean.csv"

df = pd.read_csv(file_path)

# ---------------------------------
# Convert Month to DateTime
# ---------------------------------

df["month"] = pd.to_datetime(df["month"])

# ---------------------------------
# Filter Data (2022–2025)
# ---------------------------------

df = df[
    (df["month"] >= "2022-01-01") &
    (df["month"] <= "2025-12-31")
]

# ---------------------------------
# Create Line Chart
# ---------------------------------

fig = px.line(
    df,
    x="month",
    y="total_folios_crore",
    markers=True,
    title="Growth of Mutual Fund Folios (2022–2025)",
    labels={
        "month":"Month",
        "total_folios_crore":"Total Folios (Crore)"
    },
    template="plotly_white",
    height=650
)

# ---------------------------------
# Mark January 2022
# ---------------------------------

fig.add_scatter(
    x=[df.iloc[0]["month"]],
    y=[df.iloc[0]["total_folios_crore"]],
    mode="markers+text",
    marker=dict(size=12, color="green"),
    text=["13.26 Cr\nJan 2022"],
    textposition="bottom right",
    showlegend=False
)

# ---------------------------------
# Mark December 2025
# ---------------------------------

fig.add_scatter(
    x=[df.iloc[-1]["month"]],
    y=[df.iloc[-1]["total_folios_crore"]],
    mode="markers+text",
    marker=dict(size=12, color="red"),
    text=["26.12 Cr\nDec 2025"],
    textposition="top left",
    showlegend=False
)

# ---------------------------------
# Improve Layout
# ---------------------------------

fig.update_layout(
    title_x=0.5,
    xaxis_title="Month",
    yaxis_title="Total Folios (Crore)",
    hovermode="x unified"
)

# ---------------------------------
# Display Chart
# ---------------------------------

fig.show()