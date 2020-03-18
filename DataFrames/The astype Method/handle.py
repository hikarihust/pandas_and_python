import pandas as pd

nba = pd.read_csv("../nba.csv").dropna(how = "all")
nba["Salary"].fillna(0, inplace = True)
nba["College"].fillna("None", inplace = True)
print(nba.head(6))

print(nba.dtypes)
nba.info()

nba["Salary"] = nba["Salary"].astype("int")
print(nba.head(3))

nba["Number"] = nba["Number"].astype("int")
nba["Age"] = nba["Age"].astype("int")
print(nba.head(3))

print(nba["Age"].astype("float"))

print(nba["Position"].nunique())

nba["Position"] = nba["Position"].astype("category")
nba.info()

nba["Team"] = nba["Team"].astype("category")

print(nba.head())
