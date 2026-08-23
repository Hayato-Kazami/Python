import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error,root_mean_squared_error
from sklearn.preprocessing import StandardScaler

# 使用 GitHub 上可用的备选数据源（原 CMU 链接已失效）
data_url = "https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv"

df = pd.read_csv(data_url)

# 分离特征和目标值（MEDV 是目标列）
data = df.drop("medv", axis=1).values
target = df["medv"].values

# 2.数据预处理：标准化特征数据

# 分割数据集为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(data, target, 
                                                    test_size=0.2, 
                                                    random_state=22)
# 3.特征工程

# 实例化标准化对象
transfor = StandardScaler()

# 标准化特征数据
X_train = transfor.fit_transform(X_train)
X_test = transfor.transform(X_test)

# 4.模型训练

# 创建线性回归模型
model = SGDRegressor()

# 训练模型
model.fit(X_train, y_train)

# 预测
y_pred = model.predict(X_test)

# 5.模型评估

# 计算评估指标
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = root_mean_squared_error(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"Mean Absolute Error: {mae}")
print(f"Root Mean Squared Error: {rmse}")

print(f"模型斜率：{model.coef_}")
print(f"模型截距：{model.intercept_}")

# 6.模型保存与加载
joblib.dump(model, 'boston_housing_model.pkl')
joblib.dump(transfor, 'boston_housing_transfor.pkl')

# 加载模型和转换器
model_load = joblib.load('boston_housing_model.pkl')
Standard_load = joblib.load('boston_housing_transfor.pkl')

# 预测
y_pred_load = model_load.predict(X_test)
mse_load = mean_squared_error(y_test, y_pred_load)
print(f"加载模型的 Mean Squared Error: {mse_load}")
      


