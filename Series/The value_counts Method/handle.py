import pandas as pd

pokemon = pd.read_csv("../pokemon.csv", index_col = "Pokemon", squeeze = True)
print(pokemon.head(3))

print(pokemon.value_counts())
print(pokemon.value_counts().sum())

print(pokemon.count())

print(pokemon.value_counts(ascending = True))