import pandas as pd

bond = pd.read_csv("../jamesbond.csv", index_col = "Film")
bond.sort_index(inplace = True)
print(bond.head(3))

print(bond.loc["Moonraker"])
print(bond.loc["Moonraker", "Actor":"Budget"])
print(bond.loc["Moonraker", ["Actor", "Budget", "Year"]])

print("==================")
print(bond.iloc[14])
print(bond.iloc[14, 2])
print(bond.iloc[14, 2 : 5])

print("==================")
print(bond.loc[["Moonraker", "Octopussy"]])