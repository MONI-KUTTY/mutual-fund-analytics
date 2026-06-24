import pandas as pd
import os

# Path to raw data folder
raw_folder = r"D:\Mutual_Fund_Analytics\data\raw"

# Get all CSV files
csv_files = [f for f in os.listdir(raw_folder) if f.endswith(".csv")]

print(f"Total CSV files found: {len(csv_files)}")

for file in csv_files:
    file_path = os.path.join(raw_folder, file)

    print("\n" + "="*80)
    print(f"FILE: {file}")
    print("="*80)

    try:
        df = pd.read_csv(file_path)

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

    except Exception as e:
        print(f"Error reading {file}: {e}")