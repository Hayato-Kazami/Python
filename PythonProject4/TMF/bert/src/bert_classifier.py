from config import Config
import torch.nn as nn
from transformers import BertModel

conf = Config()

class TMFBertClassifier(nn.Module):
    def __init__(self):
        super(TMFBertClassifier, self).__init__()
        # 加载预训练的BERT模型
        self.bert = BertModel.from_pretrained(conf.bert_model_path)
        # 添加分类层
        self.fc = nn.Linear(conf.hidden_dim, conf.class_num)

    # 前向传播
    def forward(self, input_ids, attention_mask):
        # 获取BERT的输出
        output = self.bert(input_ids=input_ids, attention_mask=attention_mask)
       
        # 获取分类层的输出
        logits = self.fc(output.pooler_output)
        return logits

if __name__ == '__main__':
    from utils import build_dataloader

    # 构建数据加载器
    train_dataloader, dev_dataloader, test_dataloader = build_dataloader()
    # 初始化模型
    model = TMFBertClassifier()
    # 打印模型的输出形状
    for batch_idx, (input_ids, attention_mask, labels) in enumerate(train_dataloader):
        print(model(input_ids, attention_mask).shape)
        break