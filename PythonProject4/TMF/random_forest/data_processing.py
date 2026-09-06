import sys
from pathlib import Path

# 把 TMF 项目根目录加入 sys.path，使 `from data.config import Config` 在任何目录下运行都能导入
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from pre_data.config import Config
import pandas as pd
import jieba
conf = Config()

# 分词预处理函数
def cut_sentence(s):
    # 使用jieba进行分词
    return ' '.join(jieba.lcut(s))

# 数据处理函数
def process_data(read_path, save_path):
    # 读取数据
    data = pd.read_csv(read_path,sep='\t',names=['text','label'])
    # 分词预处理
    data['words'] = data['text'].apply(cut_sentence)
    # 保存处理后的数据
    data.to_csv(save_path,sep='\t',index=False)
    print(f"数据处理完成，保存路径为：{save_path}")

# 主函数
def main():
    # 处理训练集
    process_data(conf.train_data_path, conf.processed_train_data_path)
    # 处理测试集
    process_data(conf.test_data_path, conf.processed_test_data_path)
    # 处理验证集
    process_data(conf.dev_data_path, conf.processed_dev_data_path)


if __name__ == '__main__':
    main()
