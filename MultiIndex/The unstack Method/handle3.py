import pandas as pd

world = pd.read_csv("../worldstats.csv", index_col = ["country", "year"])
print(world.head(3))

print("=============================")
s = world.stack()
print(s.head(3))

print("=============================")
print(s.unstack(level = ["year", "country"]))

print("=============================")
print(s.unstack("year"))
print("-----------------------------")
s = s.unstack("year", fill_value = 0)
print(s.head())