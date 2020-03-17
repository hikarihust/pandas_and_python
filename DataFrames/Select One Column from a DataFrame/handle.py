import pandas as pd

nba = pd.read_csv("../nba.csv")
print(nba.head(3))

print(nba.Name)
print(nba.Number)
print(nba.Salary)

print(nba["Name"])
print(nba["Salary"])
print(nba["Number"])

print(type(nba["Name"]))