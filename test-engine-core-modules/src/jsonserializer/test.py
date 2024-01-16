import json
from pandas import DataFrame

data_path = "user_defined_files/teststring.json"

with open(data_path, "r") as data:
    file = json.load(data)
df = DataFrame.from_dict(file)
print(df)

output_dict = dict()
if isinstance(df, DataFrame):
    for key in df.keys():
        output_dict[key] = df.dtypes[key].name
print(output_dict)