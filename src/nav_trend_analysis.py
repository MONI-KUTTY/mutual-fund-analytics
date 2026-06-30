import pandas as pd
import plotly.express as px

file_path = r"D:\Mutual_Fund_Analytics\data\processed\02_nav_history_clean.csv"
df = pd.read_csv(file_path)

df["date"] = pd.to_datetime(df["date"])

df = df[
    (df["date"] >= "2022-01-01") &
    (df["date"] <= "2026-12-31")
]

df["amfi_code"] = df["amfi_code"].astype(str)

fig = px.line(
    df,
    x="date",
    y="nav",
    color="amfi_code",
    title="Daily NAV Trend - All 40 Schemes (2022–2026)",
    labels={
        "date": "Date",
        "nav": "NAV (₹)",
        "amfi_code": "AMFI Code"
    },
    template="plotly_white",
    height=700
)

fig.add_vrect(
    x0="2023-01-01",
    x1="2023-12-31",
    fillcolor="green",
    opacity=0.10,
    layer="below",
    line_width=0,
    annotation_text="2023 Bull Run",
    annotation_position="top left"
)

fig.add_vrect(
    x0="2024-01-01",
    x1="2024-12-31",
    fillcolor="red",
    opacity=0.10,
    layer="below",
    line_width=0,
    annotation_text="2024 Market Corrections",
    annotation_position="top left"
)

fig.update_layout(

    title_x=0.5,
    xaxis_title="Date",
    yaxis_title="NAV (₹)",
    legend_title="AMFI Code",
    hovermode="x unified"
)

fig.show()