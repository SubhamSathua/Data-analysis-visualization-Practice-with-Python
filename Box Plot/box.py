import matplotlib.pyplot as plt
data = [100, 120, 110,150,110,140,130,170,120,220,140,110]
data2= [2, 13.2, 16.2, 35.2, 36.6, 40.5, 67.2, 70.1]

plt.boxplot(data2)
plt.title("box plot")
plt.ylabel("Valuess")
plt.show()
