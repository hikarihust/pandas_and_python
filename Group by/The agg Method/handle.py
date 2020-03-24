import pandas as pd

fortune = pd.read_csv("../fortune1000.csv", index_col = "Rank")
sectors = fortune.groupby("Sector")
print(fortune.head(3))
print("----------------------------------------")
print(len(fortune))
print("----------------------------------------")
print(fortune.tail(3))
print("========================================")
print(sectors["Employees"].mean())
print("----------------------------------------")
print(sectors.agg({"Revenue" : ["sum", "mean"],
             "Profits" : "sum",
              "Employees" : "mean"}))
print("----------------------------------------")
print(sectors.agg(["size", "sum", "mean"]))
