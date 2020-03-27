import pandas as pd

week1 = pd.read_csv("../Restaurant - Week 1 Sales.csv")
week2 = pd.read_csv("../Restaurant - Week 2 Sales.csv")
customers = pd.read_csv("../Restaurant - Customers.csv")
foods = pd.read_csv("../Restaurant - Foods.csv")

print(week2.head(3))
print("----------------------------------------")
print(customers.head(3))
print("========================================")

week2 = week2.merge(customers, how = "left", left_on = "Customer ID", right_on = "ID", sort = True).drop("ID", axis = "columns")
print(week2.head())
