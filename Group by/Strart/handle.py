import pandas as pd

fortune = pd.read_csv("../fortune1000.csv", index_col = "Rank")
sectors = fortune.groupby("Sector")
print(fortune.head(3))
print("========================================")

print(type(fortune))

print(type(sectors))

print(sectors)
