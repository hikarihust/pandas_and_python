import pandas as pd

week1 = pd.read_csv("../Restaurant - Week 1 Sales.csv")
week2 = pd.read_csv("../Restaurant - Week 2 Sales.csv")
customers = pd.read_csv("../Restaurant - Customers.csv")
foods = pd.read_csv("../Restaurant - Foods.csv")
satisfaction = pd.read_csv("../Restaurant - Week 1 Satisfaction.csv")


print(week1.head(3))
print("----------------------------------------")
print(satisfaction.head(3))

print("========================================")
print(week1.merge(satisfaction, how = "left", left_index = True, right_index = True).head())
print("----------------------------------------")
print(week1.join(satisfaction, how="left").head())
