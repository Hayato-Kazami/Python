import torch

t1 = torch.randn(2,1,3,4)

print(t1)
print(t1.shape)

# 在维度0上进行降维
t2 = t1.squeeze(dim = 0)
print(t2)

# 在维度1上进行升维
t3 = t1.unsqueeze(dim = 1)
print(t3)

# 在维度-1上进行降维
t4 = t1.squeeze(dim = -1)
print(t4)
print(t4.shape)

# 在维度-2上进行升维
t5 = t1.unsqueeze(dim = -2)
print(t5)
print(t5.shape)

# 维度交换
tensor = torch.randn(3,4,5,7)
print(tensor.shape)
tensor1 = tensor.transpose(0,3)
print(tensor1.shape)
tensor2 = tensor.permute(2,0,3,1)
print(tensor2.shape)