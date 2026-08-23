import torch

t1 = torch.arange(0,50,3)
print(t1)

t2 = torch.linspace(0,100,300)
print(t2)

# 使用 generator 设置随机种子
# g = torch.Generator().manual_seed(101)
t3 = torch.randn(2, 3, generator = torch.Generator().manual_seed(101))
print(t3)

# 生成[0,10)范围内的随机整数，形状为(4,10)
t4 = torch.randint(0, 10, [4, 1])
print(t4)



