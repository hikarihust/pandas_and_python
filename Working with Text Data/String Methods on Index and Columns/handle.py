import pandas as pd 

chicago = pd.read_csv("../chicago.csv", index_col = "Name").dropna(how="all")
chicago["Department"] = chicago["Department"].astype("category")
chicago.info()
print(chicago.tail(3))

print("================================")
chicago.index = chicago.index.str.strip().str.title()
print(chicago.head(3))

print("================================")
chicago.columns = chicago.columns.str.strip().str.upper()
print(chicago.head(3))