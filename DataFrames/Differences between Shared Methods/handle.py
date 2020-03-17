import pandas as pd

rev = pd.read_csv("../revenue.csv", index_col = "Date")
print(rev.head(3))

s = pd.Series([1, 2, 3])
print(s)
print(s.sum())

print(rev.sum(axis = "columns"))