import pandas as pd
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.preprocessing import OrdinalEncoder, StandardScaler,OneHotEncoder
import numpy as np
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import joblib

# 读取数据
data = pd.read_csv('data/train.csv')

# 查看数据
# print(data.head())

# 数据预处理
# 处理缺失值
x = data[["Pclass", "Sex", "Age",]].copy()
y = data["Survived"]

x['Age'] = x['Age'].fillna(x['Age'].mean())
# print(x.info())

# 数据集划分
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# 特征工程
# 编码
category = ["Sex"]
num = ["Pclass", "Age"]
onehot_encoder = OrdinalEncoder()
x_train_cat = onehot_encoder.fit_transform(X_train[category])
x_test_cat = onehot_encoder.transform(X_test[category])

# 标准化
scaler = StandardScaler()
x_train_num = scaler.fit_transform(X_train[num])
x_test_num = scaler.transform(X_test[num])

# 合并特征
X_train = np.hstack((x_train_num, x_train_cat))
X_test = np.hstack((x_test_num, x_test_cat))

# 模型训练
model = DecisionTreeClassifier()
estimator = GridSearchCV(model, 
                         param_grid={'max_depth': [3, 5, 7, 9], 
                        'min_samples_split': [2, 4, 6, 8]}, 
                        cv=5)
estimator.fit(X_train, y_train)

# 模型评估
acc = estimator.score(X_test, y_test)
y_pred = estimator.predict(X_test)
report = classification_report(y_test, y_pred)
print(f"Accuracy: {acc}")
print(report)

# 可视化
plt.figure(figsize=(40,30))
plot_tree(estimator.best_estimator_,)
plt.show()

# 保存模型
joblib.dump(estimator.best_estimator_, 'titanic_model.bin')
joblib.dump(onehot_encoder, 'titanic_encoder.bin')
joblib.dump(scaler, 'titanic_scaler.bin')

