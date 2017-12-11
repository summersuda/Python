import matplotlib.pyplot as plt
values = list(range(1,1001))
square_values = [value ** 2 for value in values]
# 用y值来设置其颜色，y值较小显示为浅蓝色，y值较大显示为深蓝色
plt.scatter(values,square_values,edgecolor='none',s=40,c=square_values,cmap=plt.cm.Blues)

# 设置标题、坐标轴上的标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis="both", labelsize=14)

# 设置坐标轴的取值范围
plt.axis([0,1100,0,1100000])

# plt.show()
plt.savefig("sqaure_plot.png",bbox_inches="tight")
# 第二个参数，bbox_inches="tight" 把图表多余的空白删除掉

