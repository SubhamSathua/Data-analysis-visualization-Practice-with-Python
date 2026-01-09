import pandas as pd
import numpy as np

df = pd.DataFrame({
    "A": [1, None, None, None, 5],
    "B": [None, None, None, None, 10],
    "C": [3, None, None, None, None],
    "D": [4, None, None, None, 20],
    "E": [4, 4, 4, 17, 20]
})



print("DataFrame:")
print(df)


df1 = df.dropna(how='all')
print("\ncleaned rows: df1")
print(df1)

df2 = df.fillna(7)
print("\nfixed rows: df2")
print(df2)


df3 = df.dropna(how='any')
print("\nrows: df3")
print(df3)