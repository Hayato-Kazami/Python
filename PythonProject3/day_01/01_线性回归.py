# from sklearn.linear_model import LinearRegression

# x = [[160], [165], [170], [175], [180]]
# y = [50, 55, 60, 65, 70]

# model = LinearRegression()
# model.fit(x, y)

# res = model.predict([[185], [190]])
# print(f'res:{res}')

# print(f'coefficient:{model.coef_}')
# print(f'intercept:{model.intercept_}')

import numpy as np
import matplotlib.pyplot as plt

# 造数据
np.random.seed(42)
x = np.linspace(0, 10, 50)
y = 2.5 * x + 1.0 + np.random.randn(50) * 2  # 真实: w=2.5, b=1.0

# 最小二乘闭式解
x_mean, y_mean = x.mean(), y.mean()
w = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean) ** 2)
b = y_mean - w * x_mean

print(f"w = {w:.3f}, b = {b:.3f}")  # w ≈ 2.49, b ≈ 1.18

# 画图
plt.scatter(x, y, alpha=0.6, label='data')
plt.plot(x, w * x + b, 'r-', label=f'y = {w:.2f}x + {b:.2f}')
plt.legend()
plt.show()

from sklearn.linear_model import LinearRegression

model = LinearRegression()          # 底层就是最小二乘
model.fit(x.reshape(-1, 1), y)
print(model.coef_, model.intercept_)  # 与上面手写结果一致
