import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 只要程序处于活动状态，就不断地模拟随机漫步
while True:
    rw = RandomWalk(10000)
    rw.fill_walk()

    # 设置绘图窗口的尺寸
    plt.figure(figsize=(10,6), dpi=128)
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=15)

    # 突出显示起点和终点
    plt.scatter(rw.x_values[0], rw.y_values[0], c="green", s=50, edgecolor = 'none')
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c="red", s=50, edgecolor = 'none')

    axes = plt.axes()
    axes.xaxis.set_visible(False)
    axes.yaxis.set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break

