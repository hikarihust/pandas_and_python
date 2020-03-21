import pandas as pd 

chicago = pd.read_csv("../chicago.csv").dropna(how="all")
chicago["Department"] = chicago["Department"].astype("category")
chicago.info()
print(chicago.tail(3))

print("================================")
print(chicago["Name"])

print("================================")
chicago["Name"] = chicago["Name"].str.lstrip().str.rstrip()
print(chicago["Name"])

print("================================")
chicago["Position Title"] = chicago["Position Title"].str.strip()
print(chicago["Position Title"])