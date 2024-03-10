import numpy as np
import pandas as pd

#1
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
print(df.loc[::20, "Manufacturer":"Type"])

#2 - both methods accomplish same thing
df["Min.Price"] = df["Min.Price"].fillna(df["Price"])
df.loc[df["Max.Price"].isna(), "Max.Price"] = df.loc[df["Max.Price"].isna(), "Price"]

print(df)

#3
df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
print(df.loc[df.sum(axis=1) > 100])

#4
arr = np.random.randint(1, 101, size=(4, 4))

print(arr)

rows = arr.reshape(4, -1, 4)
cols = arr.transpose().reshape(4, -1, 4)

summer = lambda n: np.sum(n, axis=2)

row_sums = summer(rows)
col_sums = summer(cols)

print(row_sums)
print(col_sums)
