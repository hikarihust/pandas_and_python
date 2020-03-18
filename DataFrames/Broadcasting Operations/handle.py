import pandas as pd

nba = pd.read_csv("../nba.csv")
print(nba.head(3))

print(nba["Age"].add(5))
print(nba["Age"] + 5) 

print(nba["Salary"].sub(5000000))
print(nba["Salary"] - 5000000)

print(nba["Weight"].mul(0.453592))
nba["Weight in Kilograms"] = nba["Weight"] * 0.453592
print(nba.head(3))

nba["Salary"].div(1000000)
nba["Salary in Millions"] = nba["Salary"] / 1000000

print(nba.head(3))