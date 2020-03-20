import pandas as pd

nba = pd.read_csv("../nba.csv")
print(nba.head(3))

nba.sort_values(["Number", "Salary", "Name"], inplace = True)
print(nba.tail(3))

nba.sort_index(ascending = False, inplace = True)
print(nba.head(3))