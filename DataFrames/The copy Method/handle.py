import pandas as pd

bond = pd.read_csv("../jamesbond.csv", index_col = "Film")
bond.sort_index(inplace = True)
print(bond.head(3))

print("=============================")
directors = bond["Director"]
print(directors.head(3))
directors["A View to a Kill"] = "Mister John Glen"
print(directors.head(3))
print(bond.head(3))


print("=============================")
bond = pd.read_csv("../jamesbond.csv", index_col = "Film")
bond.sort_index(inplace = True)
print(bond.head(3))
directors = bond["Director"].copy()
print("=============================")
print(directors.head(3))

print("=============================")
directors["A View to a Kill"] = "Mister John Glen"
print(directors.head(3))
print(bond.head(3))
