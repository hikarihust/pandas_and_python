import pandas as pd 

chicago = pd.read_csv("../chicago.csv").dropna(how="all")
chicago["Department"] = chicago["Department"].astype("category")
chicago.info()
print(chicago.tail(3))

print("================================")
print(chicago["Name"].str.split(",").str.get(0).value_counts().head())

print("================================")
print(chicago["Name"].str.split(",").str.get(1).str.strip().str.split(" ").str.get(0).value_counts().head(3))