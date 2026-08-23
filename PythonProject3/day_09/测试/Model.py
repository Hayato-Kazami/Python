import torch
import torch.nn as nn

class Price_Predict_Model(nn.Module):
    # 定义模型的构造函数
    def __init__(self, input_dim, output_dim):
        # 声明父类的构造函数
        super(Price_Predict_Model, self).__init__()   
        # 串联多个隐藏层
        self.net = nn.Sequential(
            nn.Linear(input_dim, 128),  # 输入层到隐藏层1
            nn.BatchNorm1d(128),  # 批量归一化，对每一层的特征进行归一化
            nn.ReLU(),  # 激活函数
            nn.Dropout(0.3), # Dropout：随机丢弃一部分神经元，防止过拟合
            nn.Linear(128, 64),  # 隐藏层1到隐藏层2
            nn.BatchNorm1d(64),  # 批量归一化
            nn.ReLU(),  # 激活函数
            nn.Dropout(0.3), # Dropout：随机丢弃一部分神经元，防止过拟合
            nn.Linear(64, 32),  # 隐藏层2到隐藏层3
            nn.ReLU(),  # 激活函数
            nn.Linear(32, output_dim)  # 隐藏层3到输出层
        )

    # 定义前向传播函数
    def forward(self,x):
        # 输出层不经过激活函数，CrossEntropyLoss 内部会自动做softmax
        return self.net(x)
    