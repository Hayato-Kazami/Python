import fasttext
from config import Config
conf = Config()


# 1.模型训练
model = fasttext.train_supervised(input=conf.processed_data_path + '/fasttext_train_word_1.txt',
                                  seed=1)
# 2.模型保存
model.save_model(conf.model_save_path + '/fasttext_train_word_1.bin')
# 3.模型预测
print(model.predict("盘 点 2 0 1 0 留 学 表 情 ： 海 外 学 子 眼 中 这 一 年 ( 组 图 )"))

# 4.模型评估  res-->(10000, 0.9081, 0.9081)
res = model.test(conf.processed_data_path + '/fasttext_test_word_1.txt')
print(f'res-->{res}')

