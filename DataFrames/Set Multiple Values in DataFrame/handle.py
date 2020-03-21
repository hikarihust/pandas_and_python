import pandas as pd

bond = pd.read_csv("../jamesbond.csv", index_col = "Film")
bond.sort_index(inplace = True)
print(bond.head(3))

bond.info()

print("==============================")
print(bond["Actor"])
mask = bond["Actor"] == "Sean Connery"
print(bond[mask])

print("==============================")
bond.loc[mask, "Actor"] = "Sir Sean Connery"
print(bond)

print("==============================")
print(bond[bond["Actor"] == "Roger Moore"])

print(bond.loc[bond["Actor"] == "Roger Moore"])