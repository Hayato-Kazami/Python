import torch.nn as nn
import torch

class PhonePricePredictor(nn.Module):
    def __init__(self, input_size, output_size):
        super(PhonePricePredictor, self).__init__()
        # 加宽隐藏层 + BatchNorm：BatchNorm 能进一步稳定训练、加速收敛、提升精度
        self.net = nn.Sequential( #多个层按顺序串起来，数据依次流过每一层
            nn.Linear(input_size, 128),# 第一层：输入层，输入特征数为 input_size
            nn.BatchNorm1d(128), # BatchNorm1d：批量归一化，对每一层的特征进行归一化
            nn.ReLU(), # 激活函数：ReLU（Rectified Linear Unit），激活函数
            nn.Dropout(0.3), # Dropout：随机丢弃一部分神经元，防止过拟合
            nn.Linear(128, 64), # 第二层：隐藏层，隐藏单元数为 128
            nn.BatchNorm1d(64), # BatchNorm1d：批量归一化，对每一层的特征进行归一化
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(64, 32), # 第三层：隐藏层，隐藏单元数为 64
            nn.ReLU(), # 激活函数：ReLU（Rectified Linear Unit），激活函数
            nn.Linear(32, output_size), # 输出层，输出特征数为 output_size
        )

    def forward(self, x):
        # 输出层不接激活函数，CrossEntropyLoss 内部会自动做 softmax
        return self.net(x)

# 测试
if __name__ == '__main__':
    from PythonProject3.day_09.手机价格预测.Create_Dataloader import load_data
    train_dataset, test_dataset, input_size, output_size = load_data()
    model = PhonePricePredictor(input_size, output_size)
    print(model)  # 打印模型结构
