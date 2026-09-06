import sys
from pathlib import Path

# 把 TMF 项目根目录加入 sys.path，使 `from data.config import Config` 在任何目录下运行都能导入
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pandas as pd
from pre_data.config import Config
import joblib

conf = Config()

# 加载模型
model = joblib.load(conf.model_save_path / 'rf_model.pkl')
tfidf = joblib.load(conf.model_save_path / 'tfidf_vectorizer.pkl')

# 加载数据
data = pd.read_csv(conf.processed_dev_data_path, sep='\t')

x_pred = tfidf.transform(data['words'])

# 预测
y_pred = model.predict(x_pred)

y_pred = pd.Series(y_pred).apply(lambda x: conf.class_list[x])
print(y_pred)

# 将结果保存到文件
res = pd.DataFrame({'text': data['text'], 'label': y_pred})
conf.save_predict_path.mkdir(parents=True, exist_ok=True)
res.to_csv(conf.save_predict_path / 'rf_predict.csv', index=False)
print('预测结果已保存到文件')
