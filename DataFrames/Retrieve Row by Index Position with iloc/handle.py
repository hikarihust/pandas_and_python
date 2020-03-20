import pandas as pd

bond = pd.read_csv("../jamesbond.csv")
print(bond.head(3))

print(bond.loc[15])
print(bond.iloc[15])

print(bond.iloc[[15, 20]])
print(bond.iloc[:4])
print(bond.iloc[4:8])
print(bond.iloc[20:])

bond2 = pd.read_csv("../jamesbond.csv", index_col = "Film")
bond2.sort_index(inplace = True)
print(bond2.head(3))
print(bond2.iloc[[0, 5, 10, 15, 20]])