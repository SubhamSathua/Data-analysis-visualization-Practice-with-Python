import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")


sns.barplot(data=iris, x="species", y="petal_length")
plt.title("Bar plot")
plt.xlabel("Species")
plt.ylabel("Petal Length")
plt.show()
