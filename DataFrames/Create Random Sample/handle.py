import pandas as pd

bond = pd.read_csv("../jamesbond.csv", index_col = "Film")
bond.sort_index(inplace = True)
print(bond.head(3))

bond.info()

print("==============================")
print(bond.sample())

print("==============================")
print(bond.sample(n = 3, axis = "columns"))