import time
from pathlib import Path
import torch
from transformers import BertTokenizer


class Config():
    def __init__(self):
        # 项目根目录：PythonProject4（本文件位于 TMF/bert/src 下，向上 3 级）
        project_dir = Path(__file__).resolve().parents[3]
        data_dir = project_dir / 'data'

        # 数据集路径
        self.train_data_path = str(data_dir / 'train.txt')
        self.test_data_path = str(data_dir / 'test.txt')
        self.dev_data_path = str(data_dir / 'dev.txt')
        self.class_path = str(data_dir / 'class.txt')
        with open(self.class_path, 'r', encoding='utf-8') as f:
            self.class_list = f.read().strip().split('\n')

        # 日志保存路径
        self.log_path = str(project_dir / 'logs' / f'{time.strftime("%Y-%m-%d")}_log.txt')

        # 模型保存路径
        self.teacher_best_model_path = str(project_dir / 'model' / 'bert_classification_best.pth')
        self.teacher_last_model_path = str(project_dir / 'model' / 'bert_classification_last.pth')
        self.student_best_model_path = str(project_dir / 'model' / 'student_bilstm_best_model.pth')
        self.student_last_model_path = str(project_dir / 'model' / 'student_bilstm_last.pth')

        # 确保日志和模型保存目录存在（logs、model），避免写文件时目录不存在报错
        Path(self.log_path).parent.mkdir(parents=True, exist_ok=True)
        Path(self.student_best_model_path).parent.mkdir(parents=True, exist_ok=True)

        # 模型文件路径，隐藏层维度
        self.bert_model_path = str(Path(__file__).resolve().parents[1] / 'bert-base-chinese')
        self.hidden_dim = 768
        self.tokenizer = BertTokenizer.from_pretrained(self.bert_model_path)
        # 学生模型词表大小，用于学生模型的词表加载和训练
        self.vocab_size = self.tokenizer.vocab_size

        # 训练参数
        self.class_num = len(self.class_list)
        self.batch_size = 16
        self.epochs = 3
        self.lr = 5e-5
        self.max_len = 32

        # 设备配置
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        # 学生模型配置
        """
        词嵌入维度 和 LSTM 隐藏层维度 和 LSTM 层数
        用于学生模型的词嵌入和 LSTM 隐藏层训练和预测
        词嵌入维度和 LSTM 隐藏层维度可以调整，以适应不同的任务和数据集
        LSTM 层数可以调整，以适应不同的任务和数据集
        dropout 用于防止过拟合，可以调整，以适应不同的任务和数据集
        """
        self.embedding_dim = 128
        self.lstm_hidden_dim = 128
        self.lstm_num_layers = 2
        self.dropout = 0.2

        # 蒸馏参数
        self.temperature = 2.0
        self.alpha = 0.7
        # 学生模型（BiLSTM）从零训练，需要比 BERT 微调更大的学习率
        self.student_lr = 1e-3

if __name__ == '__main__':
    config = Config()
    print(config.device)
