import pandas as pd

df = pd.read_csv("../employees.csv", parse_dates = ["Start Date", "Last Login Time"])

df["Senior Management"] = df["Senior Management"].astype("bool")
df["Gender"] = df["Gender"].astype("category")
print(df.head(3))
df.info()

print(df[df["Salary"].between(60000, 70000)])

print(df[df["Bonus %"].between(2.0, 5.0)])

print(df[df["Start Date"].between("1991-01-01", "1992-01-01")])

print(df[df["Last Login Time"].between("08:30AM", "12:00PM")])