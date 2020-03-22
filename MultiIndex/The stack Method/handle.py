import pandas as pd

world = pd.read_csv("../worldstats.csv", index_col = ["country", "year"])
print(world.head(3))

print("=============================")
print(type(world.stack()))

print("=============================")
print(world.stack())
print(world.stack().to_frame())

print("=============================")
stack = world.stack()
print(stack['Arab World'][2015]['Population'])
