import pandas as pd

world = pd.read_csv("../worldstats.csv", index_col = ["country", "year"])
print(world.head(3))

print("=============================")
s = world.stack()
print(s.head(3))

print("=============================")
print(s.unstack(-1))
print("------------------------------")
print(s.unstack(2))

print("=============================")
print(s.unstack(-2))
print("------------------------------")
print(s.unstack(1))
print("------------------------------")
print(s.unstack("year"))

print("=============================")
print(s.unstack(-3))
print("------------------------------")
print(s.unstack(0))
print("------------------------------")
print(s.unstack("country"))
