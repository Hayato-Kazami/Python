"""剧透检测模型：BERT 底座 + 二分类头（非剧透 / 剧透）。"""
import torch.nn as nn
from transformers import BertModel

from config import Config

conf = Config()


class SpoilerBertClassifier(nn.Module):
    def __init__(self):
        super().__init__()
        self.bert = BertModel.from_pretrained(conf.bert_model_path)
        self.fc = nn.Linear(conf.hidden_dim, conf.class_num)

    def forward(self, input_ids, attention_mask):
        output = self.bert(input_ids=input_ids, attention_mask=attention_mask)
        return self.fc(output.pooler_output)
