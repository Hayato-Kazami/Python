import torch

torch.random.manual_seed(0)

# t1 = torch.randint(0,5,[3,5,7])
# t2 = torch.randint(0,5,[3,5,7])

# t3 = torch.cat([t1,t2],dim=1)
# print(t1)
# print(t2)
# print(t3)
# print(t1.shape)
# print(t2.shape)
# print(t3.shape)

t4 = torch.randint(0,6,[2,5])
t5 = torch.randint(0,6,[2,5])

t6 = torch.stack([t4,t5],dim=0)
t7 = torch.stack([t4,t5],dim=1)
t8 = torch.stack([t4,t5],dim=2)
print(t4)
print(t5)
print(t6)
print(t7)
print(t8)
print(t4.shape)
print(t5.shape)
print(t6.shape)
print(t7.shape)
print(t8.shape)
