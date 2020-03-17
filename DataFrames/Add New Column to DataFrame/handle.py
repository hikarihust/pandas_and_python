import pandas as pd

nba = pd.read_csv("../nba.csv")
print(nba.head(3))

nba["Sport"] = "Basketball"
print(nba.head(3))

nba["League"] = "National Basketball Association"
print(nba.head(3))

nba = pd.read_csv("../nba.csv")
print(nba.head(3))

nba.insert(3, column = "Sport", value = "Basketball")
print(nba.head(3))

nba.insert(7, column = "League", value = "National Basketball Association")
print(nba)
# Output = None
