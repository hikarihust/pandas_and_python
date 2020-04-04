import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5, 5))
df = pd.DataFrame(df)
print(df)
print(pd.get_option("precision"))
print("================================")
pd.set_option("precision", 2)
print(df)
print("--------------------------------")
pd.reset_option("precision")
print(pd.get_option("precision"))
