## View 1961 Census Data
## Diarmuid McDonnell
## 2020-05-27

# Import modules

import pandas as pd # module for handling data


# Import data

census_1961_data = pd.read_csv("census_1961.csv", encoding = "ISO-8859-1", index_col=False, dtype="object")


# View data

print(census_1961_data.sample(10))
print("Finished executing script")