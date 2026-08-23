import jieba.posseg
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud

# 获取句子标签数量分布
def lable_nums():
    # 读取文件
    train_file = pd.read_csv('./data/train.tsv', sep='\t')
    dev_file = pd.read_csv('./data/dev.tsv', sep='\t')

    # 绘制训练集标签分布
    sns.countplot(x=train_file['label'],data=train_file)
    plt.title('Training Set Label Distribution')
    plt.show()

    # 绘制开发集标签分布
    sns.countplot(x=dev_file['label'],data=dev_file)
    plt.title('Development Set Label Distribution')
    plt.show()

# 获取句子长度分布
def sentence_len():
    plt.style.use('fivethirtyeight')
    # 读取文件
    train_file = pd.read_csv('./data/train.tsv', sep='\t')
    dev_file = pd.read_csv('./data/dev.tsv', sep='\t')

    # 计算训练集句子长度
    # 方法一
    train_file['sentence_length'] = list(map(lambda x: len(x), train_file['sentence']))
    # 方法二
    dev_file['sentence_length'] = dev_file['sentence'].str.len()
    print(dev_file)

    # 绘制训练集句子长度分布
    sns.countplot(x=train_file['sentence_length'],data=train_file)
    # 横坐标不显示
    plt.xticks([])
    plt.show()

    sns.displot(x=train_file['sentence_length'],data=train_file)
    plt.show()

# 获取词表大小
def word_size():
    # 读取文件
    train_file = pd.read_csv('./data/train.tsv', sep='\t')
    dev_file = pd.read_csv('./data/dev.tsv', sep='\t')

    # 统计词表大小
    all_words = []
    train_words = []
    for i, row in train_file.iterrows():
        words = jieba.lcut(row['sentence'])
        for word in words:
            if word not in train_words:
                train_words.append(word)
            if word not in all_words:
                all_words.append(word)

    dev_words = []
    for i, row in dev_file.iterrows():
        words = jieba.lcut(row['sentence'])
        for word in words:
            if word not in dev_words:
                dev_words.append(word)
            if word not in all_words:
                all_words.append(word)
    print(f"训练集词表大小: {len(train_words)}")
    print(f"开发集词表大小: {len(dev_words)}")
    print(f"总词表大小: {len(all_words)}")

# 获取形容词
def get_list(sentence):
    list = jieba.posseg.lcut(sentence)
    res = []
    for pair in list:
        if pair.flag == 'a':
            res.append(pair.word)
    return res

# 获取词云
def word_cloud(word_list):
    # 实例化词云对象
    wordcloud = WordCloud(font_path='./data/SimHei.ttf', background_color='white')
    # 获取词云字符串
    wordcloud_text = ' '.join(word_list)
    wordcloud.generate(wordcloud_text)
    # 绘制词云
    plt.figure(0)
    plt.imshow(wordcloud,)
    plt.axis('off')
    plt.show()    

def word_cloud2():
    # 读取文件
    train_file = pd.read_csv('./data/train.tsv', sep='\t')
    dev_file = pd.read_csv('./data/dev.tsv', sep='\t')
    # 获取训练集词云
    p_train = train_file[train_file['label'] == 1]['sentence']
    # 获取所有形容词
    a_list = p_train.apply(lambda x: get_list(x))
    p_train_words = [word for words in a_list for word in words]
    # 绘制词云
    word_cloud(p_train_words)

    # 绘制训练集负例词云
    n_train = train_file[train_file['label'] == 0]['sentence']
    # 获取所有形容词
    a_list = n_train.apply(lambda x: get_list(x))
    n_train_words = [word for words in a_list for word in words]
    # 绘制词云
    word_cloud(n_train_words)


if __name__ == '__main__':

    word_cloud2()