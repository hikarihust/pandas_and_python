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
print(week1.merge(week2, how = "inner", on = ["Customer ID", "Food ID"]))
print("----------------------------------------")
print(week1[week1["Customer ID"] == 578])
print("----------------------------------------")
print(week2[week2["Customer ID"] == 578])
