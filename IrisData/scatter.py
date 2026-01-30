import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv("IrisData/iris.data.csv")

plt.figure(figsize=(7, 5))
plt.scatter(
    iris["sepal_length"],
    iris["petal_length"],
    alpha=0.6,
    edgecolors="black"
)

plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.grid(True, linestyle="--", alpha=0.7)

plt.show()
