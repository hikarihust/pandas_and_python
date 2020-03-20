import pandas as pd

nba = pd.read_csv("../nba.csv").dropna(how = "all")
nba["Salary"] = nba["Salary"].fillna(0).astype("int")
print(nba.head(3))

nba["Salary Rank"] = nba["Salary"].rank(ascending = False).astype("int")
print(nba["Salary Rank"])
print(nba.head(3))

print(nba.sort_values(by = "Salary", ascending = False))