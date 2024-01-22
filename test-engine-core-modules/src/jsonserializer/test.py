import json
from pandas import DataFrame
import pandas as pd

data_path = "user_defined_files/teststring.json"
csv_file_path = "user_defined_files/test_drifted.csv"
json_file_path = "user_defined_files/test_drifted.json"

with open(data_path, "r") as data:
    file = json.load(data)
print(type(file))
df = DataFrame.from_dict(file)
print(df)

output_dict = dict()
if isinstance(df, DataFrame):
    for key in df.keys():
        output_dict[key] = df.dtypes[key].name
print(output_dict)

df = pd.read_csv(csv_file_path)
df.to_json(json_file_path, orient='records', indent=2)

with open(json_file_path, "r") as data:
    file = json.load(data)
print(type(file))
new_df = DataFrame.from_dict(file)
print(new_df)
