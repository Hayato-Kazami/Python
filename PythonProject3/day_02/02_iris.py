from sklearn.datasets import load_iris
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import sklearn.neighbors
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Load the Iris dataset
def demo1_EDA():
    iris = load_iris()

    print(f"查看特征前五列：{iris.data[:5]}")
    print(f"查看特征名称：{iris.feature_names}")
    print(f"查看标签值：{iris.target}")
    print(f"查看标签名称：{iris.target_names}")

    # 将数据转换为DataFrame
    df = pd.DataFrame(iris.data, columns=iris.feature_names)

    # 添加标签列
    df['target'] = iris.target

    print(df)

    sns.lmplot(x='sepal length (cm)', y='petal length (cm)', hue='target', data=df,fit_reg=True)
    plt.show()

def demo2_train():
    iris = load_iris()
    # 数据集划分
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=2)

    # 特征工程
    transfer = StandardScaler()
    X_train = transfer.fit_transform(X_train)
    X_test = transfer.transform(X_test)

    # 模型训练
    estimator = sklearn.neighbors.KNeighborsClassifier(n_neighbors=5)
    estimator.fit(X_train, y_train)

    # 模型评估
    # 方法一
    acc = estimator.score(X_test, y_test)
    print(f"准确率：{acc}")

    # 方法二
    y_pred = estimator.predict(X_test)
    acc2 = accuracy_score(y_test, y_pred)
    print(f"准确率：{acc2}")


    # 预测
    my_data = [[5.1, 3.5, 1.4, 0.2],[4.6, 2.9, 3.6, 1.0]]

    # 标准化
    my_data = transfer.transform(my_data)
    res = estimator.predict(my_data)
    print(f"预测结果：{res}")
    acc1 = estimator.predict_proba(my_data)
    print(f"预测概率：{acc1}")


if __name__ == "__main__":
    demo2_train()

