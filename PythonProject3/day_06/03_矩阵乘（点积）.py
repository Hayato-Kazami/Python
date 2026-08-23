import torch

# 定义两个张量
torch.manual_seed(1)
t1 = torch.randint(2, 10, (3, 4))
t2 = torch.randint(3, 14, (4, 5))
print(t1)
print(t2)

# 计算乘法

t3 = t1 @ t2
print(t3)


