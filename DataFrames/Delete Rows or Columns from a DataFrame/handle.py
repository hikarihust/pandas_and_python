import pandas as pd

bond = pd.read_csv("../jamesbond.csv", index_col = "Film")
bond.sort_index(inplace = True)
print(bond.head(3))

bond.info()

print("==============================")
bond.drop("Casino Royale", inplace = True)
print(bond.head())

print("==============================")
bond.drop(labels = ["Box Office", "Bond Actor Salary", "Actor"], axis = "columns", inplace = True)
print(bond.head())

print("==============================")
bond = pd.read_csv("../jamesbond.csv", index_col = "Film")
bond.sort_index(inplace = True)
print(bond.head(3))
actor = bond.pop("Actor")
print(actor)
print(bond.head(3))

print("==============================")
bond = pd.read_csv("../jamesbond.csv", index_col = "Film")
bond.sort_index(inplace = True)
print(bond.head(3))
del bond["Director"]

del bond["Year"]
print(bond.head(3))