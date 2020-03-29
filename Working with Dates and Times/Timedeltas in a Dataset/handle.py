import pandas as pd

shipping = pd.read_csv("../ecommerce.csv", index_col = "ID", parse_dates = ["order_date", "delivery_date"])
print(shipping.head(3))
print("================================")

shipping["Delivery Time"] = shipping["delivery_date"] - shipping["order_date"]
print(shipping.head(3))
print("================================")

shipping["Twice As Long"] = shipping["delivery_date"] + shipping["Delivery Time"]
print(shipping.head(3))
print("--------------------------------")
print(shipping.dtypes)
print("================================")

mask = shipping["Delivery Time"] == "3423 days"
print(shipping[mask])
print("--------------------------------")
print(shipping["Delivery Time"].min())
