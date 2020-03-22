import pandas as pd

sales = pd.read_csv("../quarters.csv")
print(sales)

print("=========================================")
print(pd.melt(sales, id_vars = "Salesman", var_name = "Quarter", value_name = "Revenue"))