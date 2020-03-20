import pandas as pd

df = pd.read_csv("../employees.csv", parse_dates = ["Start Date", "Last Login Time"])

df["Senior Management"] = df["Senior Management"].astype("bool")
df["Gender"] = df["Gender"].astype("category")
df.sort_values("First Name", inplace = True)
print(df.head(3))
df.info()

print(df["Gender"].unique())

print(df["Team"].unique())

print(len(df["Team"].unique()))

print(df["Team"].nunique(dropna = False))