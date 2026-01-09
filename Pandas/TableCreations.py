import pandas as pd

df = pd.DataFrame({
    "A": [1, None, None, None, 5],
    "B": [None, None, None, None, 10],
    "C": [3, None, None, None, None],
    "D": [4, None, None, None, 20],
    "E": [4, 4, 4, 17, 20]
})
print("Simple: \n", df)



df2 = pd.DataFrame({
    0: [1, None, None, None, 5],
    1: [None, None, None, None, 10],
    2: [3, None, None, None, None],
    3: [4, None, None, None, 20],
    4: [4, 4, 4, 17, 20]
}, index=["A", "B", "C", "D", "E"])

print("\nWith Index: \n", df)



df1 = pd.DataFrame(
    data=[
        ["Apple", "Fruit"],
        ["Tomato", "Veg"]
    ],
    index=[1, 2],
    columns=["Name", "Type"]
)

print("\nRow wise: \n", df1)