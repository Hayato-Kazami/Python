import torch
import torch.nn as nn
from torchsummary import summary

class Model(nn.Module):
    # 网络层搭建
    def __init__(self):
        # 继承父类方法
        super().__init__()
        # 定义第一个隐藏层
        self.linear1 = nn.Linear(3,6)
        # 参数初始化
        nn.init.xavier_normal_(self.linear1.weight)
        nn.init.zeros_(self.linear1.bias)
        # 定义第二个隐藏层
        self.linear2 = nn.Linear(6,3)
        # 参数初始化
        nn.init.kaiming_normal_(self.linear2.weight)
        nn.init.zeros_(self.linear2.bias)
        # 定义输出层
        self.out = nn.Linear(3,2)

        # 前向传播
    def forward(self,x): # 5x3
        # 经过第一个隐藏层
        x = self.linear1(x) # 5x3 @ 3x6 = 5x6
        # 经过激活函数
        x = torch.sigmoid(x) # 5x6
        # 经过第二个隐藏层
        x = self.linear2(x) # 5x6 @ 6x3 = 5x3
        # 经过激活函数
        x = torch.relu(x) # 5x3
        # 经过输出层
        logits = self.out(x) # 5x3 @ 3x2 = 5x2
        # 数据进入softmax函数
        return logits # 5x2

if __name__ == '__main__':
    # 创建模型实例
    model = Model()
    x = torch.randn(5,3) # 5x3

    out = model(x) # 5x2
    print(out) # 5x2

    # 计算模型参数大小
    summary(model,input_size = (3,),batch_size = 5,device = 'cpu') 
    # input_size=(3,)表示输入数据的形状为(3,)，即3个特征
    # batch_size=5表示批量大小为5
    # device='cpu'表示在CPU上进行计算

    print(model.named_parameters()) # 打印模型参数
    for name,params in model.named_parameters():
        print(name,params,params.shape) # 打印参数名称和形状