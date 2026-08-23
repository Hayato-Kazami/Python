import torch
from torch.nn import SmoothL1Loss
from torch.optim import SGD
class MomentumSolver(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 1)
        torch.nn.init.ones_(self.linear.weight)

    def forward(self, x):
        return self.linear(x)


model = MomentumSolver()
# 获取随机的输入特征
x = torch.randint(1, 11, (5, 3), dtype=torch.float32)
# 5x1
y = torch.tensor([[4.],
                  [5],
                  [87],
                  [1],
                  [3.]])
optimizer = SGD(model.parameters(),lr=0.5,momentum=0.9)
# 1. 前向传播
output = model(x)
# 2.计算损失
loss_f = SmoothL1Loss()
loss = loss_f(output,y)
print(loss)
# 3.梯度清零
optimizer.zero_grad()
# 4.反向传播
loss.backward()
for name,param in model.named_parameters():
    print(name,param)
# 5.参数更新
optimizer.step()
for name,param in model.named_parameters():
    print(name,param)


