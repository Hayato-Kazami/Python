import torch

torch.manual_seed(100)
t1 = torch.randint(0,11,(3,4)).float()
print(t1)

print(t1.mean()) #计算平均值
print(t1.mean(dim=0)) #计算每列的平均值
print(t1.mean(dim=0).shape)
print(t1.mean(dim=1)) #计算每行的平均值
print(t1.mean(dim=1).shape)