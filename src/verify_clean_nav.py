import pandas as pd

df = pd.read_csv(
    r"D:\Mutual_Fund_Analytics\data\processed\nav_history_clean.csv"
)

print("Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nNAV <= 0:")
print((df["nav"] <= 0).sum())