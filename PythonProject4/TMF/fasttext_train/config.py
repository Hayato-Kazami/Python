from pathlib import Path


class Config():
    def __init__(self):
        # 项目根目录：PythonProject4（本文件位于 TMF/fasttext_train 下，向上 2 级）。
        # 用 __file__ 定位，与「在哪个目录运行脚本」无关，不再依赖 ../ 相对路径。
        project_dir = Path(__file__).resolve().parents[2]
        data_dir = project_dir / 'data'

        # 原始数据路径
        self.train_data_path = str(data_dir / 'train.txt')
        self.test_data_path = str(data_dir / 'test.txt')
        self.dev_data_path = str(data_dir / 'dev.txt')

        # 处理后的数据路径（fasttext 格式，由 data_preprocess.py 生成）
        self.processed_data_path = str(Path(__file__).resolve().parent / 'final_data')

        # 模型保存路径
        self.model_save_path = str(project_dir / 'model' / 'fasttext_model')
        Path(self.model_save_path).mkdir(parents=True, exist_ok=True)

        # 分类名称路径
        self.class_path = str(data_dir / 'class.txt')
        with open(self.class_path, 'r', encoding='utf-8') as f:
            self.class_list = f.read().split()
