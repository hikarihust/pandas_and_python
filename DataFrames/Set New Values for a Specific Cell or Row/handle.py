import pandas as pd

bond = pd.read_csv("../jamesbond.csv", index_col = "Film")
bond.sort_index(inplace = True)
print(bond.head(3))

bond.info()

print("==============================")
print(bond.loc["Dr. No"])

print("==============================")
bond.loc["Dr. No", "Actor"] = "Sir Sean Connery"
print(bond.loc["Dr. No"])

print("==============================")
bond.loc["Dr. No", ["Box Office", "Budget", "Bond Actor Salary"]] = [448800000, 7000000, 600000]
print(bond.loc["Dr. No"])

print("==============================")
print(bond.loc["Dr. No", "Budget"])

print("==============================")
bond2 = bond.loc["Dr. No"]
print(bond2["Budget"])