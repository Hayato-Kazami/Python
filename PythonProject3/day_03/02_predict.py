import joblib
import pandas as pd
import numpy as np


# 读取数据
data = pd.read_csv('data/train.csv')

# 查看数据
# print(data.head())

# 数据预处理
# 处理缺失值
x = data[["Pclass", "Sex", "Age",]].copy()
y = data["Survived"]

x['Age'] = x['Age'].fillna(x['Age'].mean())

# 读取模型
joblib_model = joblib.load('titanic_model.bin')
joblib_onehot_encoder = joblib.load('titanic_encoder.bin')
joblib_scaler = joblib.load('titanic_scaler.bin')

# 特征预处理
category = ["Sex"]
num = ["Pclass", "Age"]
x_predict_cat = joblib_onehot_encoder.transform(x[category])
x_predict_num = joblib_scaler.transform(x[num])
x_predict = np.hstack((x_predict_cat, x_predict_num))

# 预测
res = joblib_model.predict(x_predict)
print(res)