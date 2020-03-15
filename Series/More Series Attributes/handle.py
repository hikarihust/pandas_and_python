import pandas as pd

pokemon = pd.read_csv("pokemon.csv", usecols = ["Pokemon"], squeeze = True)
google = pd.read_csv("google_stock_price.csv", squeeze = True)

print(pokemon.values)
print(google.values)

print(pokemon.index)
print(google.index)

print(pokemon.dtype)
print(google.dtype)

print(pokemon.is_unique)
print(google.is_unique)

print(pokemon.ndim)
print(google.ndim)

print(pokemon.shape)
print(google.shape)

print(pokemon.size)
print(google.size)

print(pokemon.name)
print(google.name)

pokemon.name = "Pocket Monsters"

print(pokemon.head())