import torch

def LSTM_single():
    # 创建一个LSTM层
    # input_size: 输入的特征数
    # hidden_size: 隐藏层的维度
    # num_layers: 隐藏层的层数
    # batch_first: 如果为True，输入的形状是(batch, seq_len, feature)，否则是(seq_len, batch, feature)
    
    lstm = torch.nn.LSTM(input_size=128, hidden_size=256, num_layers=2, batch_first=True)

    # 创建一个输入张量
    # 第一个参数是batch_size，第二个参数是句子长度，第三个参数是词向量维度
    x = torch.randn(2, 10, 128)  # (batch, seq_len, feature)

    # 获取隐藏状态和输出
    # h0: 初始化的隐藏状态，形状是(num_layers, batch_size, hidden_size)
    # num_layers: 隐藏层的层数
    # batch_size: 批量大小
    # hidden_size: 隐藏层的维度
    h0 = torch.randn(2, 2, 256)  

    # c0: 初始化的细胞状态，形状是(num_layers, batch_size, hidden_size)
    # num_layers: 隐藏层的层数
    # batch_size: 批量大小
    # hidden_size: 隐藏层的维度
    c0 = torch.randn(2, 2, 256)  

    # 前向传播
    # 第一维是batch_size，第二维是句子长度，第三维是隐藏层的维度
    output, (hn, cn) = lstm(x, (h0, c0))
    print(output.shape)  # (2, 10, 256)
    print(hn.shape)  # (2, 2, 256)
    print(cn.shape)  # (2, 2, 256)

def LSTM_bi():
    # 创建一个LSTM层
    # input_size: 输入的特征数
    # hidden_size: 隐藏层的维度
    # num_layers: 隐藏层的层数
    # batch_first: 如果为True，输入的形状是(batch, seq_len, feature)，否则是(seq_len, batch, feature)
    
    lstm = torch.nn.LSTM(input_size=128, hidden_size=256, num_layers=2, batch_first=True, bidirectional=True)

    # 创建一个输入张量
    # 第一个参数是batch_size，第二个参数是句子长度，第三个参数是词向量维度
    x = torch.randn(2, 10, 128)  # (batch, seq_len, feature)

    # 获取隐藏状态和输出
    # h0: 初始化的隐藏状态，形状是(num_layers, batch_size, hidden_size)
    # num_layers: 隐藏层的层数
    # batch_size: 批量大小
    # hidden_size: 隐藏层的维度
    h0 = torch.randn(4, 2, 256)  

    # c0: 初始化的细胞状态，形状是(num_layers, batch_size, hidden_size)
    # num_layers: 隐藏层的层数
    # batch_size: 批量大小
    # hidden_size: 隐藏层的维度
    c0 = torch.randn(4, 2, 256)  

    # 前向传播
    # 第一维是batch_size，第二维是句子长度，第三维是隐藏层的维度
    output, (hn, cn) = lstm(x, (h0, c0))
    print(output.shape)  # (2, 10, 512)
    print(hn.shape)  # (4, 2, 256)
    print(cn.shape)  # (4, 2, 256)

if __name__ == '__main__':
    LSTM_single()
    LSTM_bi()