import pandas as pd
import numpy as np

data = np.random.randint(0, 100, [1000, 50])
df = pd.DataFrame(data)
pd.options.display.max_rows = 4
pd.options.display.max_columns = 8
print(df)
print("================================")
print(df.tail(2))

print("================================")
print(pd.get_option("max_rows"))
print("--------------------------------")
print(pd.get_option("max_columns"))

print("================================")
pd.set_option("max_columns", 14)
pd.options.display.max_columns = 10
print(pd.get_option("mAX_columns"))
print(pd.get_option("max_columns"))
print("--------------------------------")
pd.reset_option("max_rows")
print(pd.get_option("max_rows"))
print("--------------------------------")
print(df.tail(2))