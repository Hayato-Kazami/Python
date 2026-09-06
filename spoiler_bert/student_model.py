"""BiLSTM 学生模型（剧透二分类），用于知识蒸馏。

结构：Embedding → 双向 LSTM → 取最后一层双向最终 hidden state → 全连接。
"""
import torch
import torch.nn as nn

from config import Config

conf = Config()


class BiLSTM(nn.Module):
    def __init__(self):
        super().__init__()
        self.embedding = nn.Embedding(conf.vocab_size, conf.embedding_dim)
        self.lstm = nn.LSTM(conf.embedding_dim,
                            conf.lstm_hidden_dim,
                            conf.lstm_num_layers,
                            bidirectional=True,
                            dropout=conf.dropout)
        self.fc = nn.Linear(conf.lstm_hidden_dim * 2, conf.class_num)

    def forward(self, input_ids, attention_mask):
        embedded = self.embedding(input_ids)
        attention_mask = attention_mask.unsqueeze(-1)
        input = embedded * attention_mask  # 清零 padding
        input = input.transpose(0, 1)  # LSTM 需要 seq_len 在第一维
        lstm_out, (hidden, cell) = self.lstm(input)
        # 取双向 LSTM 最后一层的最终 hidden state（而非最后一个时间步输出，避免 padding 干扰）
        hidden = hidden.view(conf.lstm_num_layers, 2, -1, conf.lstm_hidden_dim)[-1]
        out = torch.cat([hidden[0], hidden[1]], dim=-1)  # (batch, hidden_dim*2)
        return self.fc(out)
