import pandas as pd
import yaml

# Load the YAML file
with open("afx_module_configs.yaml", "r") as file:
    yaml_data = yaml.safe_load(file)

# Prepare the data for the CSV
csv_data = []
for afx, details in yaml_data.items():
    afx_class = details["class"]
    parameters_str = []

    # Extract parameters and their default sampling range
    parameters = details.get("parameters", {})
    for param, param_details in parameters.items():
        sampling_range_default = param_details.get("sampling_range", {}).get(
            "default", ""
        )
        if sampling_range_default:
            parameters_str.append(f"{param} {sampling_range_default}")

    # Join parameters into a single string
    parameters_content = ", ".join(parameters_str)

    # Create a row for this AFX
    row = {
        "class": afx_class,
        "AFX": afx,
        "plot acronyms": "",
        "parameters": parameters_content,
    }
    csv_data.append(row)

# Create a DataFrame
df = pd.DataFrame(csv_data)

# Save to CSV
df.to_csv("afx_module_params_with_sampling_range.csv", index=False)

print("CSV file created: afx_module_params_with_sampling_range.csv")
