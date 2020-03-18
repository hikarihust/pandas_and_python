import pandas as pd

nba = pd.read_csv("../nba.csv")
print(nba.head(3))

print(nba.sort_values("Name", ascending = False))

print(nba.sort_values("Age", ascending = False))

nba.sort_values("Salary", ascending = False, inplace = True)
print(nba.head(3))

print(nba.sort_values("Salary", ascending = False, na_position = "first").tail())

nba.sort_values(["Team", "Name"], ascending = [True, False], inplace = True)
print(nba.head(3))