import pandas as pd

df = pd.read_csv("../employees.csv", parse_dates = ["Start Date", "Last Login Time"])

df["Senior Management"] = df["Senior Management"].astype("bool")
df["Gender"] = df["Gender"].astype("category")
print(df.head(3))
df.info()

mask1 = df["Team"] == "Legal"
mask2 = df["Team"] == "Sales"
mask3 = df["Team"] == "Product"
print(df[mask1 | mask2 | mask3])

mark = df["Team"].isin(["Legal", "Sales", "Product"])
print(df[mark])
