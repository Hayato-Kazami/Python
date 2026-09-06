"""剧透检测项目配置（自包含，不依赖 danmaku_bert）。"""
from pathlib import Path

import torch
from transformers import BertTokenizer


class Config:
    def __init__(self):
        project_dir = Path(__file__).resolve().parent

        # 数据目录（sample_spoiler.py 输出 train/dev/test.txt + class.txt）
        self.data_dir = str(project_dir / 'data')
        self.train_data_path = str(project_dir / 'data' / 'train.txt')
        self.dev_data_path = str(project_dir / 'data' / 'dev.txt')
        self.test_data_path = str(project_dir / 'data' / 'test.txt')

        # 类别（剧透二分类，固定）
        self.class_list = ["非剧透", "剧透"]
        self.class_num = len(self.class_list)

        # 模型保存路径
        self.best_model_path = str(project_dir / 'model' / 'bert_spoiler_best.pth')
        self.last_model_path = str(project_dir / 'model' / 'bert_spoiler_last.pth')
        self.student_best_model_path = str(project_dir / 'model' / 'student_bilstm_best.pth')
        self.student_last_model_path = str(project_dir / 'model' / 'student_bilstm_last.pth')
        Path(self.best_model_path).parent.mkdir(parents=True, exist_ok=True)

        # 日志保存路径
        self.log_path = str(project_dir / 'logs' / 'spoiler_log.txt')
        Path(self.log_path).parent.mkdir(parents=True, exist_ok=True)

        # BERT 底座（复用 TMF 项目已下载的 bert-base-chinese）
        self.bert_model_path = str(project_dir.parent / 'PythonProject4' / 'TMF'
                                   / 'bert' / 'bert-base-chinese')
        self.tokenizer = BertTokenizer.from_pretrained(self.bert_model_path)
        self.vocab_size = self.tokenizer.vocab_size
        self.hidden_dim = 768

        # 训练参数
        self.batch_size = 16
        self.epochs = 5
        self.lr = 3e-5
        self.max_len = 32
        self.warmup_ratio = 0.1

        # 学生模型（BiLSTM）配置，用于知识蒸馏
        self.embedding_dim = 128
        self.lstm_hidden_dim = 128
        self.lstm_num_layers = 2
        self.dropout = 0.2

        # 蒸馏参数
        self.temperature = 2.0
        self.alpha = 0.7
        self.student_lr = 1e-3  # 学生模型从零训练，需要比 BERT 微调更大的学习率

        # 设备
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


if __name__ == '__main__':
    c = Config()
    print('device:', c.device)
    print('class_list:', c.class_list)
