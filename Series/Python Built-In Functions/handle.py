import pandas as pd

pokemon = pd.read_csv("pokemon.csv", usecols = ["Pokemon"], squeeze = True)
google = pd.read_csv("google_stock_price.csv", squeeze = True)

print(len(pokemon))
len(google)

print(type(pokemon))
#print(dir(pokemon))

print(sorted(pokemon))
print(sorted(google))

print(list(pokemon))

print(dict(google))
print(max(pokemon))
print(min(pokemon))

print(max(google))
print(min(google))