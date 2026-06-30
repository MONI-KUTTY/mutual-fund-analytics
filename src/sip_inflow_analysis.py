import pandas as pd
import plotly.express as px

# ---------------------------------
# Load Cleaned Dataset
# ---------------------------------

file_path = r"D:\Mutual_Fund_Analytics\data\processed\04_monthly_sip_inflows_clean.csv"

df = pd.read_csv(file_path)

# ---------------------------------
# Convert Month Column to DateTime
# ---------------------------------

df["month"] = pd.to_datetime(df["month"])

# ---------------------------------
# Filter Data (Jan 2022 – Dec 2025)
# ---------------------------------

df = df[
    (df["month"] >= "2022-01-01") &
    (df["month"] <= "2025-12-31")
]

# ---------------------------------
# Create Interactive Line Chart
# ---------------------------------

fig = px.line(
    df,
    x="month",
    y="sip_inflow_crore",
    markers=True,
    title="Monthly SIP Inflow Trend (Jan 2022 - Dec 2025)",
    labels={
        "month": "Month",
        "sip_inflow_crore": "SIP Inflow (₹ Crore)"
    },
    template="plotly_white",
    height=650
)

# ---------------------------------
# Highlight Highest SIP Inflow
# ---------------------------------

max_row = df.loc[df["sip_inflow_crore"].idxmax()]

fig.add_scatter(
    x=[max_row["month"]],
    y=[max_row["sip_inflow_crore"]],
    mode="markers+text",
    marker=dict(size=12, color="red"),
    text=["₹31,002 Cr\nDec 2025"],
    textposition="top center",
    showlegend=False
)

# ---------------------------------
# Improve Layout
# ---------------------------------

fig.update_layout(
    title_x=0.5,
    xaxis_title="Month",
    yaxis_title="SIP Inflow (₹ Crore)",
    hovermode="x unified"
)

# ---------------------------------
# Display Chart
# ---------------------------------

fig.show()