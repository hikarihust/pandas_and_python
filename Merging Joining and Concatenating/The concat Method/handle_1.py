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

print(len(pd.concat([week1, week2])))
print("----------------------------------------")
print(pd.concat([week1, week2], ignore_index=False))
print("----------------------------------------")
print(pd.concat([week1, week2], ignore_index=True))
print("========================================")
