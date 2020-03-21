import pandas as pd

bond = pd.read_csv("../jamesbond.csv", index_col = "Film")
bond.sort_index(inplace = True)
print(bond.head(3))

bond.info()

print("==============================")
mask = bond["Actor"] == "Sean Connery"
print(bond[mask])

print("==============================")
print(bond.where(mask))

print(bond.where(bond["Box Office"] > 800))

print("==============================")
mask2 = bond["Box Office"] > 800
print(bond.where(mask & mask2))