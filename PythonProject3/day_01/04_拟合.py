import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# 生成数据
np.random.seed(666)

def dm01_under_fit():
    x = np.random.uniform(-3, 3, size=100)
    y = 0.5 * x ** 2 + x + 2 + np.random.normal(0, 1, size=100)

    # 实例化线性回归模型
    estimator = LinearRegression()

    # 训练模型
    X = x.reshape(-1, 1)
    estimator.fit(X, y)

    # 预测
    y_pred = estimator.predict(X)

    # 计算均方误差
    mse = mean_squared_error(y, y_pred)

    # 绘制数据和拟合曲线
    sort_index = np.argsort(x)  # 获取排序索引
    plt.scatter(x, y, color='blue', label='Data')
    plt.plot(x[sort_index], y_pred[sort_index], color='red', label='Linear Fit')
    plt.show()

def dm02_just_fit():
    x = np.random.uniform(-3, 3, size=100)
    y = 0.5 * x ** 2 + x + 2 + np.random.normal(0, 1, size=100)

    # 实例化线性回归模型
    estimator = LinearRegression()

    # 训练模型
    X = x.reshape(-1, 1)
    X2 = np.hstack((X, X ** 2))
    estimator.fit(X2, y)

    # 预测
    y_pred = estimator.predict(X2)

    # 计算均方误差
    mse = mean_squared_error(y, y_pred)

    # 绘制数据和拟合曲线
    sort_index = np.argsort(x)  # 获取排序索引
    plt.scatter(x, y, color='blue', label='Data')
    plt.plot(x[sort_index], y_pred[sort_index], color='red', label='Linear Fit')
    plt.show()

def dm03_over_fit():
    x = np.random.uniform(-3, 3, size=100)
    y = 0.5 * x ** 2 + x + 2 + np.random.normal(0, 1, size=100)

    # 实例化线性回归模型
    estimator = LinearRegression()

    # 训练模型
    X = x.reshape(-1, 1)
    X3 = np.hstack([X, X ** 2, X ** 3, X ** 4, X ** 5, X ** 6, X ** 7, X ** 8, X ** 9, X ** 10])
    estimator.fit(X3, y)

    # 预测
    y_pred = estimator.predict(X3)

    # 计算均方误差
    mse = mean_squared_error(y, y_pred)

    # 绘制数据和拟合曲线
    sort_index = np.argsort(x)  # 获取排序索引
    plt.scatter(x, y, color='blue', label='Data')
    plt.plot(x[sort_index], y_pred[sort_index], color='red', label='Linear Fit')
    plt.show()




if __name__ == '__main__':

    dm01_under_fit()  # 调用函数进行拟合
    
    dm02_just_fit()  # 调用函数进行拟合 

    dm03_over_fit()  # 调用函数进行拟合