import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression,Lasso,Ridge
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 生成数据
np.random.seed(666)

def dm01_L1():
    x = np.random.uniform(-3, 3, size=100)
    y = 0.5 * x ** 2 + x + 2 + np.random.normal(0, 1, size=100)
    X = x.reshape(-1, 1)
    X1 = np.hstack([X, X ** 2, X ** 3, X ** 4, X ** 5, X ** 6, X ** 7, X ** 8, X ** 9, X ** 10])
    x_train, x_test, y_train, y_test = train_test_split(X1, y, test_size = 0.2, random_state=42)
    # 特征标准化
    scaler = StandardScaler()
    x_train_scaled = scaler.fit_transform(x_train)
    x_test_scaled = scaler.transform(x_test)
    X1_scaled = scaler.transform(X1)  # 全量数据也做同样的变换

    # 实例化岭回归模型
    estimator = Ridge(alpha=1.0)

    # 训练模型
    estimator.fit(x_train_scaled, y_train)

    # 预测
    y_pred = estimator.predict(x_test_scaled)

    # 计算均方误差
    mse = mean_squared_error(y_test, y_pred)

    # 绘制数据和拟合曲线
    sort_index = np.argsort(x)  # 获取排序索引
    plt.scatter(x, y, color='blue', label='Data')
    y_pred_plot = estimator.predict(X1_scaled)
    plt.plot(x[sort_index], y_pred_plot[sort_index], color='red', label='Linear Fit')
    plt.show()


if __name__ == '__main__':

    dm01_L1()  # 调用函数进行拟合