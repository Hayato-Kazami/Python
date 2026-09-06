import torch
import torch.nn as nn
from config import Config

conf = Config()

class BiLSTM(nn.Module):
    def __init__(self):
        super().__init__()
        # 嵌入层
        self.embedding = nn.Embedding(conf.vocab_size, conf.embedding_dim)
        # LSTM层
        self.lstm = nn.LSTM(conf.embedding_dim, # 词嵌入维度
                            conf.lstm_hidden_dim, # LSTM隐藏层维度
                            conf.lstm_num_layers, # LSTM层数
                            bidirectional=True,
                            dropout=conf.dropout)
        # 全连接层
        self.fc = nn.Linear(conf.lstm_hidden_dim * 2, conf.class_num)

    def forward(self, input_ids, attention_mask):
        # 嵌入
        embedded = self.embedding(input_ids)
        attention_mask = attention_mask.unsqueeze(-1)
        # 清零padding
        input = embedded * attention_mask
        # 交换维度，目的是将batch_size放在第一个维度，而LSTM需要batch_size放在第二个维度
        input = input.transpose(0, 1)
        # LSTM输出
        lstm_out, (hidden, cell) = self.lstm(input)
        # 取双向 LSTM 最后一层的最终 hidden state（而非「最后一个时间步」输出）。
        # hidden 形状 (num_layers*2, batch, hidden_dim)：最后一层的 forward/backward 各拼一半。
        # 原 lstm_out[-1] 取到 padding 位置，backward 半边几乎为 0，丢掉一半特征导致 F1 低。
        hidden = hidden.view(conf.lstm_num_layers, 2, -1, conf.lstm_hidden_dim)[-1]
        out = torch.cat([hidden[0], hidden[1]], dim=-1)  # (batch, hidden_dim*2)
        return self.fc(out)

if __name__ == '__main__':
    from utils import build_dataloader
    train_dataloader, dev_dataloader, test_dataloader = build_dataloader()
    model = BiLSTM()
    for input_ids, attention_mask, labels in train_dataloader:
        print(model(input_ids, attention_mask))
        break