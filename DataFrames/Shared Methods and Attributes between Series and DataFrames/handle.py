import pandas as pd

nba = pd.read_csv("../nba.csv")

print(nba.head(2))

print(nba.tail())

print(nba.index)

print(nba.values)

print(nba.shape)

print(nba.dtypes)

nba.head()

print(nba.columns)

print(nba.axes)

print(nba.info())
