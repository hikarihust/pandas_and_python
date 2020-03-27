import pandas as pd

week1 = pd.read_csv("../Restaurant - Week 1 Sales.csv")
week2 = pd.read_csv("../Restaurant - Week 2 Sales.csv")
customers = pd.read_csv("../Restaurant - Customers.csv")
foods = pd.read_csv("../Restaurant - Foods.csv")

print(len(week1))
print("----------------------------------------")
print(week1)
print("========================================")

print(len(week2))
print("----------------------------------------")
print(week2)
print("========================================")

print(week1.head(2))
print("----------------------------------------")
print(week2.head(2))
print("----------------------------------------")
print(len(week1.merge(week2, how = "outer", on = "Customer ID", suffixes = [" - Week 1", " - Week 2"])))
print("----------------------------------------")
merged = week1.merge(week2, how = "outer", on = "Customer ID", suffixes = [" - Week 1", " - Week 2"],
            indicator = True)
print(merged)
print("----------------------------------------")
print(merged["_merge"].value_counts())
print("----------------------------------------")
mask = merged["_merge"].isin(["left_only", "right_only"])
print(merged[mask])


