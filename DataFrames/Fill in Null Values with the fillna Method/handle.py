import pandas as pd

nba = pd.read_csv("../nba.csv")
print(nba.head(3))

print(nba.fillna(0))

nba["Salary"].fillna(0, inplace = True)
print(nba.head())

nba["College"].fillna("No College", inplace = True)
print(nba.head())