import sys
from pathlib import Path

# 把 TMF 项目根目录加入 sys.path，使 `from data.config import Config` 在任何目录下运行都能导入
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import joblib
import pandas as pd
from sklearn.model_selection import GridSearchCV
from pre_data.config import Config
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

conf = Config()

# 获取数据
# 获取训练数据
train_data = pd.read_csv(conf.processed_train_data_path,sep='\t')
train_words = train_data['words']
y_train = train_data['label']

# 获取测试数据
test_data = pd.read_csv(conf.processed_test_data_path,sep='\t')
test_words = test_data['words']
y_test = test_data['label']

# 获取验证数据
dev_data = pd.read_csv(conf.processed_dev_data_path,sep='\t')
dev_words = dev_data['words']
y_dev = dev_data['label']

# 特征提取
with open(conf.stop_words_path, 'r', encoding='utf-8') as f:
    stop_words = f.read().split()

# 实例化TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer(stop_words=stop_words)

# 获取训练数据的特征
X_train = tfidf_vectorizer.fit_transform(train_words)

# 获取测试数据的特征
X_test = tfidf_vectorizer.transform(test_words)

# 获取验证数据的特征
X_dev = tfidf_vectorizer.transform(dev_words)

# 打印特征向量的参数
print(f"词表：{len(tfidf_vectorizer.vocabulary_)}")
print(f"特征向量的维度：{X_train.shape[1]}")

# 训练模型
model = RandomForestClassifier()
grid_cv = GridSearchCV(model,
                       param_grid={'n_estimators': [50, 100],
                                   'max_depth': [10, 15]},
                                   n_jobs=-1,cv=3)

grid_cv.fit(X_train, y_train)

# 模型评估
best_model = grid_cv.best_estimator_
print(f"最佳参数：{grid_cv.best_params_}")
y_pred = best_model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred, average='macro')
rec = recall_score(y_test, y_pred, average='macro')
f1 = f1_score(y_test, y_pred, average='macro')
conf_matrix = confusion_matrix(y_test, y_pred)

print(f"测试集准确率：{acc}")
print(f"测试集精确率：{prec}")
print(f"测试集召回率：{rec}")
print(f"测试集F1分数：{f1}")
print(f"测试集混淆矩阵：'\n'{conf_matrix}")

# 保存模型
conf.model_save_path.mkdir(parents=True, exist_ok=True)
joblib.dump(best_model, conf.model_save_path / 'rf_model.pkl')
joblib.dump(tfidf_vectorizer, conf.model_save_path / 'tfidf_vectorizer.pkl')