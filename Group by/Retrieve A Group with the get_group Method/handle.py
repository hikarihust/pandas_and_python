import pandas as pd

fortune = pd.read_csv("../fortune1000.csv", index_col = "Rank")
sectors = fortune.groupby("Sector")
print(fortune.head(3))
print(len(fortune))
print("----------------------------------------")
print(fortune.tail(3))
print("========================================")

print(sectors.get_group("Retailing"))
print("----------------------------------------")
print(fortune[fortune["Sector"] == "Retailing"])
