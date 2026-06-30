import pandas as pd
from sqlalchemy import create_engine

# Create SQLite connection
engine = create_engine(
    r"sqlite:///D:/Mutual_Fund_Analytics/bluestock_mf.db"
)

# Load CSVs
fund_master = pd.read_csv(
    r"D:\Mutual_Fund_Analytics\data\processed\01_fund_master_clean.csv"
)

nav_history = pd.read_csv(
    r"D:\Mutual_Fund_Analytics\data\processed\02_nav_history_clean.csv"
)

transactions = pd.read_csv(
    r"D:\Mutual_Fund_Analytics\data\processed\08_investor_transactions_clean.csv"
)

performance = pd.read_csv(
    r"D:\Mutual_Fund_Analytics\data\processed\07_scheme_performance_clean.csv"
)

aum = pd.read_csv(
    r"D:\Mutual_Fund_Analytics\data\processed\03_aum_by_fund_house_clean.csv"
)

# Load into SQLite tables
fund_master.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

nav_history.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

transactions.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

aum.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)

print("Data loaded successfully into SQLite!")