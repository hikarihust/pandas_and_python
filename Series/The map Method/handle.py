import pandas as pd

pokemon_names = pd.read_csv("../pokemon.csv", usecols = ["Pokemon"], squeeze = True)
pokemon_types = pd.read_csv("../pokemon.csv", index_col = ["Pokemon"], squeeze = True)


pokemon_names = pd.read_csv("../pokemon.csv", usecols = ["Pokemon"], squeeze = True)
pokemon_types = pd.read_csv("../pokemon.csv", index_col = "Pokemon", squeeze = True).to_dict()

# pokemon_names.head()
# pokemon_types

print(pokemon_names.head(3))
# print(pokemon_types.head(3))
print(pokemon_names.map(pokemon_types))