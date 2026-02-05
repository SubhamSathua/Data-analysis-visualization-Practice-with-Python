import seaborn as sns
import matplotlib.pyplot as plt
iris = sns.load_dataset("iris")
plt.figure(figsize=(10, 6))
sns.boxplot(x="species", y="sepal_length", data=iris)
plt.title("Boxplot of Sepal Length by Species")
plt.show()