import pandas as pd

week1 = pd.read_csv("../Restaurant - Week 1 Sales.csv")
week2 = pd.read_csv("../Restaurant - Week 2 Sales.csv")
customers = pd.read_csv("../Restaurant - Customers.csv")
foods = pd.read_csv("../Restaurant - Foods.csv")

print(week1.head(3))
print("----------------------------------------")
print(foods.head(3))
print("========================================")

week1 = week1.merge(foods, how = "left", on = "Food ID", sort = True)
print(week1.head())
print("----------------------------------------")
print(len(week1))
