import pandas as pd

# Load all datasets

df1 = pd.read_csv(
    r"D:\Mutual_Fund_Analytics\data\raw\01_fund_master.csv"
)

df2 = pd.read_csv(
    r"D:\Mutual_Fund_Analytics\data\raw\03_aum_by_fund_house.csv"
)

df3 = pd.read_csv(
    r"D:\Mutual_Fund_Analytics\data\raw\04_monthly_sip_inflows.csv"
)

df4 = pd.read_csv(
    r"D:\Mutual_Fund_Analytics\data\raw\05_category_inflows.csv"
)

df5 = pd.read_csv(
    r"D:\Mutual_Fund_Analytics\data\raw\06_industry_folio_count.csv"
)

df6 = pd.read_csv(
    r"D:\Mutual_Fund_Analytics\data\raw\09_portfolio_holdings.csv"
)

df7 = pd.read_csv(
    r"D:\Mutual_Fund_Analytics\data\raw\10_benchmark_indices.csv"
)

# Print dataset information

datasets = {
    "01_fund_master": df1,
    "03_aum_by_fund_house": df2,
    "04_monthly_sip_inflows": df3,
    "05_category_inflows": df4,
    "06_industry_folio_count": df5,
    "09_portfolio_holdings": df6,
    "10_benchmark_indices": df7
}

for name, df in datasets.items():

    print("\n" + "=" * 80)
    print(name)
    print("=" * 80)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nShape:")
    print(df.shape)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())