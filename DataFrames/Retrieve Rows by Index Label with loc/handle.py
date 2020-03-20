import pandas as pd

bond = pd.read_csv("../jamesbond.csv", index_col = "Film")
bond.sort_index(inplace = True)
print(bond.head(3))

print(bond.loc["Goldfinger"])
print(bond.loc["GoldenEye"])
# print(bond.loc["Sacred Bond"])
print(bond.loc["Casino Royale"])


print(bond.loc["Diamonds Are Forever" : "Moonraker"])
print(bond.loc[: "On Her Majesty's Secret Service"])

print(bond.loc[["Octopussy", "Moonraker"]])

print(bond.loc[["Moonraker", "Octopussy"]])

print("Gold Bond" in bond.index)

# df = bond.loc[["Moonraker", "Octopussy"]]
# print(df["Year"])
#df.to_csv("./test.csv")
# df = df.reset_index(drop=True)
# print(df)
# df.to_csv("./test2.csv", index_label=False, index= False)