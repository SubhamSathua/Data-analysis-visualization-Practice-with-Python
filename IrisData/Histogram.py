import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv("IrisData/iris.data.csv")

plt.hist(iris["sepal_length"], bins=10)

plt.title("Histogram of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")

plt.show()
