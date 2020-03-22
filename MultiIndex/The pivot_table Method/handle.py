import pandas as pd

foods =pd.read_csv("../foods.csv")
print(foods.head(3))
foods.info()

print("============================")
print(foods.pivot_table(values = "Spend", index = ["Gender", "Item"], columns = "City", aggfunc = "min").head(3))

print("============================")
print(pd.pivot_table(data = foods, values = "Spend", index = ["Gender", "Item"], columns = "City", aggfunc = "min").head(3))

print("============================")
print(pd.pivot_table(foods, values = "Spend", index = ["Gender", "Item"], columns = "City", aggfunc = "min").head(3))
