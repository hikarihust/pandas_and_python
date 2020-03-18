import pandas as pd

nba = pd.read_csv("../nba.csv")
print(nba.head(3))

print(nba["Team"].value_counts())
nba["Position"].value_counts().head(1)
nba["Weight"].value_counts().tail()
nba["Salary"].value_counts()