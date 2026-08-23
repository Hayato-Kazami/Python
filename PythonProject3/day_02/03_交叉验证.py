from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split,GridSearchCV
import sklearn.neighbors
from sklearn.preprocessing import StandardScaler
import joblib

def demo2_train():
    iris = load_iris()
    # 数据集划分
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=2)

    # 特征工程
    transfer = StandardScaler()
    X_train = transfer.fit_transform(X_train)
    X_test = transfer.transform(X_test)

    # 模型训练
    model = sklearn.neighbors.KNeighborsClassifier(n_neighbors=5)
    estimator = GridSearchCV(model, param_grid={'n_neighbors': [1, 3, 5, 7, 9]}, cv=5)
    estimator.fit(X_train, y_train)

    # 模型评估
    print(f"{'最佳参数:':<12}{estimator.best_params_}")
    print(f"{'最佳分数:':<12}{estimator.best_score_:.4f}")
    print(f"{'交叉验证结果:':<12}{estimator.cv_results_}")
    acc = estimator.score(X_test, y_test)
    print(f"{'测试集准确率:':<12}{acc:.4f}")

    # 保存模型
    best_model = estimator.best_estimator_
    joblib.dump(best_model, 'best_knn_model.bin')




if __name__ == "__main__":
    demo2_train()

