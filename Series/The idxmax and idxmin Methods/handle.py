import pandas as pd

google = pd.read_csv("../google_stock_price.csv", squeeze = True)

print(google.max())

print(google.min())

print(google.idxmax())

print(google[3011])

print(google.idxmin())

print(google[11])

print(google[google.idxmin()])