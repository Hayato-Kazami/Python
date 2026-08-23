import torch

t1 = torch.DoubleTensor(5,2,3)
print(type(t1))
print(t1)
print(t1.size())

t2 = torch.Tensor([[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]]])
print(type(t2))
print(t2)
print(t2.size())    

