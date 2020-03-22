import pandas as pd

sales = pd.read_csv("../salesmen.csv", parse_dates = ["Date"])
sales["Salesman"] = sales["Salesman"].astype("category")
print(sales.head(3))
sales.info()
print(sales["Salesman"].value_counts())

print("============================")
print(sales.pivot(index = "Date", columns = "Salesman", values = "Revenue"))