import pandas as pd

week1 = pd.read_csv("../Restaurant - Week 1 Sales.csv")
week2 = pd.read_csv("../Restaurant - Week 2 Sales.csv")
customers = pd.read_csv("../Restaurant - Customers.csv", index_col = "ID")
foods = pd.read_csv("../Restaurant - Foods.csv", index_col = "Food ID")

customers_ = pd.read_csv("../Restaurant - Customers.csv")

print(customers.head(3))
print("----------------------------------------")
print(foods.head(3))
print("----------------------------------------")
print(week1.head())

print("========================================")
sales = week1.merge(customers, how = "left", left_on = "Customer ID", right_index = True)
print(sales)
print("----------------------------------------")
print(week1.merge(customers_, how = "left", left_on = "Customer ID", right_on = "ID"))

print("========================================")
sales = sales.merge(foods, how = "left", left_on = "Food ID", right_index = True)
print(sales.head(3))

print("========================================")
print(week1.head(3))
print("----------------------------------------")
print(week2.head(3))
print("----------------------------------------")
print(week1.merge(week2, how = "left", left_index = True, right_index = True, suffixes = [" - Week 1", " - Week 2"]))