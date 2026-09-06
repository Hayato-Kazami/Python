import sys
from pathlib import Path

# 把 TMF 项目根目录加入 sys.path，使 `from data.config import Config` 在任何目录下运行都能导入
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


import jieba
import joblib
from pre_data.config import Config
conf = Config()

# 1.加载模型
model = joblib.load(conf.model_save_path / 'rf_model.pkl')

tfidf = joblib.load(conf.model_save_path / 'tfidf_vectorizer.pkl')
print("模型和向量化器加载完成")

def predict(data: dict):
    """
    :param data: dict  {"text": "xxx"}
    :return: dict  {"text": "xxx", "pred_class": "xxx"}
    """
    # 1.分词
    words = " ".join(jieba.lcut(data["text"]))
    # 2.文本向量化
    x = tfidf.transform([words])
    # 3.模型预测
    y_pred = model.predict(x)
    data["pred_class"] = conf.class_list[y_pred[0]]

    return data


if __name__ == '__main__':
    print(predict({"text": "60年铁树开花形状似玉米芯(组图)"}))