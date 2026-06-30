import pandas as pd

fund_master = pd.read_csv(
    r"D:\Mutual_Fund_Analytics\data\raw\01_fund_master.csv"
)

nav_history = pd.read_csv(
    r"D:\Mutual_Fund_Analytics\data\raw\02_nav_history.csv"
)

# -----------------------------
# Explore Fund Master
# -----------------------------

print("\nFund Houses:")
print(fund_master["fund_house"].unique())

print("\nCategories:")
print(fund_master["category"].unique())

print("\nSub Categories:")
print(fund_master["sub_category"].unique())

print("\nRisk Categories:")
print(fund_master["risk_category"].unique())

# -----------------------------
# AMFI Code Validation
# -----------------------------

fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = fund_codes - nav_codes

print("\nValidation Results")
print("-" * 50)

print("Total Fund Master AMFI Codes:", len(fund_codes))
print("Total NAV History AMFI Codes:", len(nav_codes))
print("Missing Codes:", len(missing_codes))

if len(missing_codes) > 0:
    print("\nSample Missing Codes:")
    print(list(missing_codes)[:10])
else:
    print("\nAll AMFI codes are present in nav_history.")