import pandas as pd

nba = pd.read_csv("../nba.csv")
print(nba.head(3))

print(nba[["Team", "Name"]].head(3))
print(nba[["Number", "College"]])
print(nba[["Salary", "Team", "Name"]].tail())

select = ["Salary", "Team", "Name"]
print(nba[select])