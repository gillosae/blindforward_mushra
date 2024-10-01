import numpy as np
import pandas as pd

csv_file_path = "results.csv"
df = pd.read_csv(csv_file_path)

# Extract the columns containing the ratings
rating_columns = [
    col for col in df.columns if "Answer.audio_sample" in col and "_rating" in col
]

# Calculate the mean and standard deviation for each audio sample across all workers
means = df[rating_columns].mean()
std_devs = df[rating_columns].std()

# Define a threshold for how many standard deviations a rating must be away to be considered an outlier
std_threshold = 2

# Identify workers whose ratings deviate more than the defined threshold from the mean
outliers = df[
    (df[rating_columns] < (means - std_threshold * std_devs))
    | (df[rating_columns] > (means + std_threshold * std_devs))
]

# Find workers who have multiple outlier ratings
outlier_counts = outliers.notnull().sum(axis=1)
significant_outliers = df[outlier_counts > 7]

print(significant_outliers["WorkerId"])
significant_outliers.to_csv("significant_outliers.csv", index=False)
