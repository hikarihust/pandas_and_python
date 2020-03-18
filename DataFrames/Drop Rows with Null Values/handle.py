import pandas as pd

nba = pd.read_csv("../nba.csv")
print(nba.head(3))

print(nba.tail(3))

print(nba.dropna())
print(nba.dropna(how = "all"))

nba.dropna(how = "all", inplace = True)
print(nba.tail(3))

print(nba.head(3))

print(nba.dropna(subset = ["Salary", "College"]))
print(nba.head(3))