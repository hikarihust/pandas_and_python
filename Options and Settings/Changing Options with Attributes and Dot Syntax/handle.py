import pandas as pd
import numpy as np

data = np.random.randint(0, 100, [1000, 50])
df = pd.DataFrame(data)
print(df)
print("================================")
print(df.tail(2))

print("================================")
print(pd.options.display.max_rows)
print("--------------------------------")
pd.options.display.max_rows = 4
pd.options.display.max_columns = 8
print(df)
