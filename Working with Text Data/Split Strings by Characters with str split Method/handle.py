import pandas as pd 

chicago = pd.read_csv("../chicago.csv").dropna(how="all")
chicago["Department"] = chicago["Department"].astype("category")
chicago.info()
print(chicago.tail(3))

print("================================")
print(chicago["Name"])

print("================================")
print(chicago["Name"].str.split(","))

print("================================")
print(chicago["Name"].str.split(",").str.get(0).str.title().value_counts())

print("================================")
print(chicago["Position Title"].str.split(" ").str.get(0).value_counts())
