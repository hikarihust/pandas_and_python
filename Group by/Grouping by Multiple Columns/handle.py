import pandas as pd

fortune = pd.read_csv("../fortune1000.csv", index_col = "Rank")
sectors = fortune.groupby(["Sector", "Industry"])
print(fortune.head(3))
print("----------------------------------------")
print(len(fortune))
print("----------------------------------------")
print(fortune.tail(3))
print("========================================")

print(sectors.size())
print("----------------------------------------")
print(sectors.sum())
print("----------------------------------------")
print(sectors["Revenue"].sum())
print("----------------------------------------")
print(sectors["Employees"].mean())
