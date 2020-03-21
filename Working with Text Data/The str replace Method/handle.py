import pandas as pd 

chicago = pd.read_csv("../chicago.csv").dropna(how="all")
chicago["Department"] = chicago["Department"].astype("category")
chicago.info()
print(chicago.tail(3))

print("===================")
chicago["Department"] = chicago["Department"].str.replace("MGMNT", "MANAGEMENT")
print(chicago)

print("===================")
chicago["Employee Annual Salary"] = chicago["Employee Annual Salary"].str.replace("$", '').astype(float)
print(chicago)
print(chicago["Employee Annual Salary"].sum())
