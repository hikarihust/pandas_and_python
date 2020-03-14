import pandas as pd

fruits = ["Apple", "Orange", "Plum", "Grape", "Blueberry"]
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

print(pd.Series(fruits, weekdays))
print(pd.Series(data = fruits, index = weekdays))
print(pd.Series(fruits, index = weekdays))


fruits = ["Apple", "Orange", "Plum", "Grape", "Blueberry", "Watermelon"]
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Monday"]

print(pd.Series(data = fruits, index = weekdays))
s = pd.Series(data = fruits, index = weekdays)
print(s.Monday)