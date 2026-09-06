import os

import jieba

from config import Config
conf = Config()

# 数据预处理
def preprocess_data(read_path, save_path, is_char_segementation):

    # 加载数据
    data = []
    with open(read_path, 'r', encoding='utf-8') as f:
        for line in f:
            # 去除行首行尾的空格和换行符
            line = line.strip()
            # 跳过空行
            if not line:
                continue
            # 获取文本和标签
            text, label = line.split('\t')
            label_name = "__label__" + conf.class_list[int(label)]

            words = list(text) if is_char_segementation else jieba.lcut(text)
            # 将词语拼接起来去除空值
            words = ' '.join([word for word in words if word.strip()])
            x_train = label_name + ' ' + words
            data.append(x_train)
    # 2.保存数据
    save_dir = os.path.dirname(save_path)
    if save_dir:
        os.makedirs(save_dir, exist_ok=True)
    with open(save_path, 'w', encoding='utf-8') as f:
        for line in data:
            f.write(line + "\n")
            
            
            # todo 2 主函数
def main():
    # 1.字符级数据处理
    preprocess_data(conf.train_data_path, conf.processed_data_path + '/fasttext_train_char_1.txt', True)
    preprocess_data(conf.test_data_path, conf.processed_data_path + '/fasttext_test_char_1.txt', True)
    preprocess_data(conf.dev_data_path, conf.processed_data_path + '/fasttext_dev_char_1.txt', True)

    # 2.词语级数据处理
    preprocess_data(conf.train_data_path, conf.processed_data_path + '/fasttext_train_word_1.txt', False)
    preprocess_data(conf.test_data_path, conf.processed_data_path + '/fasttext_test_word_1.txt', False)
    preprocess_data(conf.dev_data_path, conf.processed_data_path + '/fasttext_dev_word_1.txt', False)


if __name__ == '__main__':
    main()
