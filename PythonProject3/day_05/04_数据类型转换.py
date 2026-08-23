import torch

t1 = torch.zeros(2, 3, 4)
print(t1)

t2 = torch.ones_like(t1)
print(t2)

t3 = torch.full((2, 3), 10)
print(t3)

t4 = torch.full_like(t1, 30)
print(t4)

t5 = t4.long()
print(t5)