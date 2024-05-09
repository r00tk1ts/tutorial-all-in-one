import matplotlib.pyplot as plt

# 数据
categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4']
start_values = [10, 20, 30, 40]
end_values = [15, 25, 35, 45]

# 计算柱子的宽度和位置
bar_height = 0.5
y_positions = range(len(categories))

# 绘制水平柱状图
plt.barh(y_positions, end_values, left=start_values, height=bar_height)

# 设置y轴刻度标签
plt.yticks(y_positions, categories)
plt.xlabel('Values')
plt.ylabel('Categories')
plt.title('Horizontal Bar Chart with Different Start and End Positions')
plt.grid(True)

# 显示图形
plt.show()
