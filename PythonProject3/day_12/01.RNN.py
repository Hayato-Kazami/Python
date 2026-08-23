import torch
def batch_first():
    # 实例化RNN模型
    # input_size：输入的特征数
    # hidden_size：隐藏层的特征数
    # num_layers：RNN的层数
    rnn = torch.nn.RNN(input_size=128, hidden_size=256, num_layers=2)

    # 构建h0
    # h0的形状：(num_layers, batch_size, hidden_size)
    # num_layers：RNN的层数
    # batch_size：批量大小
    # hidden_size：隐藏层的特征数
    h0 = torch.randn(2, 2, 256)

    # 输入