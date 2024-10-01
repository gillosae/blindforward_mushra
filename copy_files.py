import os
import shutil

import pandas as pd

# Load the CSV file (replace with the correct path to your CSV)
csv_file = "mushra_final.csv"
df = pd.read_csv(csv_file)

# Columns that contain file paths
file_columns = [
    "ref_dry",
    "ref_wet",
    "tar_dry",
    "tar_wet",
    "pred1",
    "pred2",
    "random_param",
]


# Function to copy files to the new destination
def copy_files(row):
    for col in file_columns:
        old_path = row[col]
        if os.path.exists(old_path):
            # Replace the beginning of the path with './samples/'
            new_path = old_path.replace("/ssd4/doyo/", "./samples/")
            new_dir = os.path.dirname(new_path)

            # Create the directory if it doesn't exist
            os.makedirs(new_dir, exist_ok=True)

            # Copy the file
            shutil.copy2(old_path, new_path)
            print(f"Copied {old_path} to {new_path}")
        else:
            print(f"File not found: {old_path}")


# Apply the function to each row in the dataframe
df.apply(copy_files, axis=1)
