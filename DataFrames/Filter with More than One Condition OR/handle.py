import pandas as pd

df = pd.read_csv("../employees.csv", parse_dates = ["Start Date", "Last Login Time"])

df["Senior Management"] = df["Senior Management"].astype("bool")
df["Gender"] = df["Gender"].astype("category")
print(df.head(3))
df.info()

mask1 = df["Senior Management"]
mask2 = df["Start Date"] < "1990-01-01"
print(df[mask1 | mask2])

mask1 = df["First Name"] == "Robert"
mask2 = df["Team"] == "Client Services"
mask3 = df["Start Date"] > "2016-06-01"
print(df[(mask1 & mask2) | mask3])