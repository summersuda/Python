import matplotlib.pyplot as plt
values = [1, 2, 3, 4, 5]
square_values = [value ** 2 for value in values]
plt.plot(values, square_values,linewidth=5)

# 设置标题、坐标轴上的标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis="both", labelsize=14)
plt.show()