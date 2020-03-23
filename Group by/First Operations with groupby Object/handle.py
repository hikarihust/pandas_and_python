import pandas as pd

fortune = pd.read_csv("../fortune1000.csv", index_col = "Rank")
sectors = fortune.groupby("Sector")
print(fortune.head(3))
print(len(fortune))
print("----------------------------------------")
print(fortune.tail(3))
print("========================================")

print(len(fortune))
print("----------------------------------------")
print(len(sectors))
print("----------------------------------------")
print(fortune["Sector"].nunique())
print("----------------------------------------")

print("========================================")
print(sectors.size())
print("----------------------------------------")
print(fortune["Sector"].value_counts())

print("========================================")
print(sectors.first())

print("========================================")
print(sectors.last())

print("========================================")
print(sectors.groups)

print("========================================")
print(fortune.loc[24])
