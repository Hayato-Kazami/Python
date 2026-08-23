import torch
import torch.nn as nn

torch.manual_seed(1)

# 创建数据
X = torch.ones(2, 5)
y = torch.randint(0, 20, (2, 3)).float()

# 创建模型
w = torch.randn(5, 3, requires_grad=True)
b = torch.zeros(3, requires_grad=True).float()

# 训练模型
# 前向传播
y_pred = X @ w + b
print("y_pred:", y_pred)

# 计算损失
# 手动计算
loss = ((y_pred - y) ** 2).sum()/(y.shape[0] * y.shape[1])
print("loss:", loss)

# API计算
loss1 = nn.MSELoss(reduction='mean')(y_pred, y)
print("loss1:", loss1)

# 反向传播
if w.grad is not None:
    w.grad.zero_()
if b.grad is not None:
    b.grad.zero_()

# 计算梯度
loss.backward()

# 更新参数
with torch.no_grad():
    w -= 0.01 * w.grad
    b -= 0.01 * b.grad

print("w:", w)
print("b:", b)