"""传统机器学习基线（TF-IDF + 逻辑回归 / 随机森林），用于和 BERT 对比。

目的：证明「为什么需要 BERT」。用最经典的传统文本分类方法跑一遍剧透数据，
得到剧透类 F1 作为深度学习模型的下界对照。

方法：jieba 分词 → TfidfVectorizer（词级 1~2 gram）→ 逻辑回归 / 随机森林。
剧透是强不平衡二分类，class_weight='balanced' 公平对待少数类「剧透」。

运行：python baseline.py  （需先跑 label_spoiler.py + sample_spoiler.py 准备好 data/）
"""
import jieba
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, classification_report

from config import Config
from utils import load_raw_data

conf = Config()


def load(path):
    data = load_raw_data(path)
    texts = [t for t, _ in data]
    labels = [l for _, l in data]
    return texts, labels


def main():
    train_texts, y_train = load(conf.train_data_path)
    dev_texts, y_dev = load(conf.dev_data_path)
    test_texts, y_test = load(conf.test_data_path)

    print('jieba 分词中...')
    train_words = [' '.join(jieba.lcut(t)) for t in train_texts]
    dev_words = [' '.join(jieba.lcut(t)) for t in dev_texts]
    test_words = [' '.join(jieba.lcut(t)) for t in test_texts]

    vectorizer = TfidfVectorizer(ngram_range=(1, 2), min_df=2)
    X_train = vectorizer.fit_transform(train_words)
    X_dev = vectorizer.transform(dev_words)
    X_test = vectorizer.transform(test_words)
    print(f'TF-IDF 特征维度: {X_train.shape[1]}')

    models = {
        '逻辑回归(LR)': LogisticRegression(max_iter=1000, n_jobs=-1, class_weight='balanced'),
        '随机森林(RF)': RandomForestClassifier(n_estimators=100, max_depth=15,
                                            n_jobs=-1, random_state=1,
                                            class_weight='balanced'),
    }

    for name, model in models.items():
        print(f'\n===== {name} =====')
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        # 剧透是少数类，weighted F1 会被「非剧透」主导；直接看剧透类 F1 才反映检测效果
        f1 = f1_score(y_test, y_pred, average='binary', pos_label=1, zero_division=0)
        print(f'剧透类 F1: {f1:.4f}')
        print(classification_report(y_test, y_pred, zero_division=0,
                                     target_names=conf.class_list))


if __name__ == '__main__':
    main()
