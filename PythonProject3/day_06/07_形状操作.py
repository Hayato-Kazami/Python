import torch

torch.manual_seed(0)

t1 = torch.randint(0, 10, (2,8))

print(t1)

# 增加维度
t2 = t1.reshape(1, 4, 4)
print(t2)
print(t2.shape)

# 修改
t3 = t1.reshape(-1,2)
print(t3)
print(t3.shape)

tensor = torch.randint(0, 10, (2, 6, 1))
print(tensor)
print(tensor.shape)
# 减少维度
t4= tensor.reshape(2, 6)
print(t4)
print(t4.shape)

# 修改
t5 = tensor.reshape(3, 4)
print(t5)
print(t5.shape)

tensor = torch.randn(2, 3, 4)
print(tensor)
print(tensor.shape)
tensor1 = tensor.view(-1)
print(tensor1)
print(tensor1.shape)