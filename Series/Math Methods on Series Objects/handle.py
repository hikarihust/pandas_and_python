import pandas as pd

google = pd.read_csv("../google_stock_price.csv", squeeze = True)
print(google.head(3))

print(google.count())

print(len(google))

print(google.sum())

print(google.min())

print(google.max())