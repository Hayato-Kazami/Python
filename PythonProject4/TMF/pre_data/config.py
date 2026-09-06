from pathlib import Path


class Config():
    def __init__(self):
        # 数据目录：真实数据在 PythonProject4/data（从本文件向上 2 级，即 PythonProject4）。
        # 用 __file__ 定位，与「在哪个目录运行脚本」无关，不再依赖 ../ 相对路径。
        data_dir = Path(__file__).resolve().parents[2] / 'data'

        # 原始数据路径
        self.train_data_path = data_dir / 'train.txt'
        self.test_data_path = data_dir / 'test.txt'
        self.dev_data_path = data_dir / 'dev.txt'

        # 处理后的数据路径
        self.processed_train_data_path = data_dir / 'processed_train.csv'
        self.processed_test_data_path = data_dir / 'processed_test.csv'
        self.processed_dev_data_path = data_dir / 'processed_dev.csv'

        # 停用词路径
        self.stop_words_path = data_dir / 'stopwords.txt'

        # 标签分类名称路径
        self.class_data_path = data_dir / 'class.txt'
        with open(self.class_data_path, 'r', encoding='utf-8') as f:
            self.class_list = f.read().strip().split('\n')

        # 模型保存路径（放到 PythonProject4/model）
        self.model_save_path = Path(__file__).resolve().parents[2] / 'model'
        self.save_predict_path = Path(__file__).resolve().parents[1] / 'save_predict'


if __name__ == '__main__':
    config = Config()
    print(config.class_list)
