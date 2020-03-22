import pandas as pd

world = pd.read_csv("../worldstats.csv", index_col = ["country", "year"])
print(world.head(3))

print("=============================")
s = world.stack()
print(s.head(3))

print("=============================")
print(s.unstack())

print("=============================")
print(s.unstack().unstack().unstack())

