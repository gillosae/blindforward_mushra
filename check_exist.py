import os

import pandas as pd

csv_file_path = "mushra_merged.csv"
df = pd.read_csv(csv_file_path)

# List of columns to check for file paths
columns_to_check = [
    "ref_dry",
    "ref_wet",
    "tar_dry",
    "tar_wet",
    "pred1",
    "pred2",
    "random_param",
]


# Function to check if the file exists for each path in the columns
def check_paths(df, columns):
    missing_paths = []
    for index, row in df.iterrows():
        for col in columns:
            file_path = row[col]
            if not os.path.exists(file_path):
                missing_paths.append((index, col, file_path))

    if missing_paths:
        print("The following paths are missing:")
        for idx, col, path in missing_paths:
            print(f"Row {idx}, Column {col}: {path}")
    else:
        print("All paths exist.")


# Run the check
check_paths(df, columns_to_check)
