import pandas as pd

file_path = r"D:\Mutual_Fund_Analytics\data\processed\10_benchmark_indices_clean.csv"

df = pd.read_csv(file_path)

print(df["index_name"].unique())