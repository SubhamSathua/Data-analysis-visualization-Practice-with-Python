import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")

features = ["sepal_length", "sepal_width", "petal_length", "petal_width"]

for feature in features:
    plt.figure(figsize=(10, 6))
    sns.boxplot(x="species", y=feature, data=iris)
    plt.title(f"Boxplot of {feature.replace('_', ' ').title()} by Species")
    plt.show()