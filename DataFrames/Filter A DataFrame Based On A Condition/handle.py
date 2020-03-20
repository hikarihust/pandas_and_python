import pandas as pd

df = pd.read_csv("../employees.csv", parse_dates = ["Start Date", "Last Login Time"])

df["Senior Management"] = df["Senior Management"].astype("bool")
df["Gender"] = df["Gender"].astype("category")
print(df.head(3))
df.info()

print(df[df["Gender"] == "Male"])

print(df[df["Team"] == "Marketing"])

mask = df["Gender"] == "Male"
print(df[mask])

print(df[df["Senior Management"]])

print(df[df["Team"] != "Marketing"])

print(df[df["Salary"] > 110000])

print(df[df["Bonus %"] < 1.5])

print(df[df["Start Date"] <= "1985-01-01" ])