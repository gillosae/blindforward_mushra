import os
import re

import pandas as pd
import yaml

query_csv = "mushra.csv"
query_df = pd.read_csv(query_csv)
query_df["index"] = query_df.index
print(query_df)

results_csv = "results.csv"
result_df = pd.read_csv(results_csv)

bad_file = "badguys.yaml"
with open("badguys.yaml", "r") as file:
    bad_worker_ids = file.read().split()

# Drop bad worker results
result_df = result_df[~result_df["WorkerId"].isin(bad_worker_ids)]

# Drop other stuffs
pattern = re.compile(r"^\d+_\d+_rating$")
rating_columns = [col for col in result_df.columns if pattern.match(col)]
result_df = result_df[rating_columns]

result_df = result_df.transpose()
result_df.index = result_df.index.astype(str).str.strip()
result_df.index = result_df.index.str.replace("_rating", "")


result_df["idx"] = result_df.index.map(lambda x: int(x.split("_")[0]))
result_df["querynum"] = result_df.index.map(lambda x: int(x.split("_")[1]))
result_df = result_df.sort_values(by=["idx", "querynum"])
print(result_df)
