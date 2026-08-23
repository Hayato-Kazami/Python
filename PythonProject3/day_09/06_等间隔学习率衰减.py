from torch.optim import lr_scheduler
from torch.utils.data import DataLoader, TensorDataset
from torch.optim import SGD
import matplotlib.pyplot as plt
import torch.nn as nn
import torch

class MyModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(8,16)
        self.fc2 = nn.Linear(16,32)
        self.out = nn.Linear(32,10)

    def forward(self,x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.out(x)
        return x

# 创建数据集
x = torch.randint(0,10,[1000,],dtype=torch.float32)
x1 = torch.stack([x,x ** 2,x ** 3,x ** 4,x ** 5,x ** 6,x ** 7,x ** 8],dim = -1)
print(x1.shape)
y = torch.randint(0,10,[1000,])

# 创建数据加载器
dataset = TensorDataset(x1,y)
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

# 创建模型
model = MyModel()

# 创建优化器,损失函数，学习率衰减器
loss_fn = nn.CrossEntropyLoss()
optimizer = SGD(model.parameters(), lr=0.1)
scheduler = lr_scheduler.StepLR(optimizer, step_size=50, gamma=0.5)

# 训练模型
lr_list = []
for epoch in range(300):
    lr_list.append(scheduler.get_last_lr())
    for x,y in dataloader:
        # 前向传播
        y_pred = model(x)
        # 计算损失
        loss = loss_fn(y_pred, y)
        # 梯度清零，反向传播
        optimizer.zero_grad()
        loss.backward()
        # 更新参数
        optimizer.step()
    # 每50个epoch打印一次学习率
    scheduler.step()

# 绘制学习率曲线
plt.plot(range(300), lr_list)
plt.xlabel('Epoch')
plt.ylabel('Learning Rate')
plt.title('Learning Rate Decay')
plt.show()