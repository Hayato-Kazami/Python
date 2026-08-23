import torch
import numpy as np

t1 = torch.tensor([1])
# 提取单元素张量
print(t1.item())  

np_data = np.array([1, 2, 3])
# 将numpy数组转换为torch张量
t2 = torch.from_numpy(np_data)
np_data[0] = 100
print(np_data)
print(t2)  

t3 = torch.from_numpy(np_data.copy())
np_data[0] = 200
print(np_data)
print(t3)  

t4 = torch.tensor(np_data)
np_data[0] = 300
print(np_data)
print(t4)  

t5 = torch.tensor([1, 2, 3])
# 将torch张量转换为numpy数组
np_data2 = t5.numpy()
print(type(np_data2))  
print(np_data2)  
np_data2[0] = 400
print(t5)  

t6 = t5.numpy().copy()
np_data2[0] = 500
print(t5)  
print(np_data2)  
print(t6)  