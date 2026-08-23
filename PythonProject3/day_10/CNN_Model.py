import torch
import torch.nn as nn

class CNN(nn.Module):
    def __init__(self):
        super().__init__()
        # 卷积层1
        self.conv1 = nn.Conv2d(
            in_channels=3, out_channels=6, 
            kernel_size=3, stride=1, padding=0)
        # 池化层1
        self.pool1 = nn.MaxPool2d(kernel_size=2, stride=2)
        # 卷积层2
        self.conv2 = nn.Conv2d(
            in_channels=6, out_channels=16, 
            kernel_size=3, stride=1, padding=0)
        # 池化层2
        self.pool2 = nn.MaxPool2d(kernel_size=2, stride=2)

        # 全连接层1
        self.fc1 = nn.Linear(16 * 6 * 6, 120)
        # 全连接层2
        self.fc2 = nn.Linear(120, 84)
        # 输出层
        self.fc3 = nn.Linear(84, 10)
    def forward(self, x):
        # 卷积层1 5*3*32*32 -> 5*6*30*30 -> 5*6*15*15
        x = self.pool1(torch.relu(self.conv1(x)))
        # 卷积层2 5*16*15*15 -> 5*16*13*13 -> 5*16*6*6
        x = self.pool2(torch.relu(self.conv2(x)))
        # 展平 5*16*6*6 -> 5*576
        x = x.reshape(x.size(0), -1)
        # 全连接层1
        x = torch.relu(self.fc1(x))
        # 全连接层2
        x = torch.relu(self.fc2(x))
        # 输出层
        x = self.fc3(x)
        return x

if __name__ == '__main__':
    # 创建模型实例
    from CNN_Dataloader import load_data
    model = CNN()
    # 加载数据集
    bs = 5
    train_dataset, test_dataset, train_loader, test_loader = load_data(bs)
    # 训练模型
    for x_train, y_train in train_loader:
        y_pred = model(x_train)
        print(y_pred)
        break