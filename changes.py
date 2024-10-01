import pandas as pd


def compare_csvs(file1, file2):
    # Load the two CSV files into DataFrames
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    # Ensure that both CSVs have the same columns
    if df1.columns.tolist() != df2.columns.tolist():
        raise ValueError(
            "The two CSV files have different columns and cannot be directly compared."
        )

    # Compare the DataFrames row-wise and find differences
    comparison = df1.compare(df2, align_axis=0)

    # If there are differences, print them with row and column information
    if not comparison.empty:
        print("Differences between the two CSV files:")
        for row in comparison.index.get_level_values(0).unique():
            for column in comparison.columns.get_level_values(0).unique():
                diff = comparison.loc[row, column]
                if not diff.isnull().all():
                    print(f"Row {row}, Column '{column}':")
                    print(f"    Value in {file1}: {diff['self']}")
                    print(f"    Value in {file2}: {diff['other']}\n")
    else:
        print("The two CSV files are identical.")


if __name__ == "__main__":
    compare_csvs("mushra_merged.csv", "mushra_merged2.csv")
