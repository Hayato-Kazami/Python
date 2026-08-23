import torch

torch.manual_seed(1)
# 创建一个二维张量
tensor = torch.randint(15, (4, 5))
print(tensor)

# 使用范围索引
# 获取前三行的前两列
t1 = tensor[:3, :2]
print(t1)

# 使用布尔索引
# 获取第0列大于5的行
t2 = tensor[tensor[:, 0] > 5, :]
print(t2)

# 获取第3行大于5的列
t3 = tensor[:, tensor[2, :] > 5]
print(t3)

# 获取第2行大于3.第4列小于5的元素
t4 = tensor[:, tensor[1, :] > 3]
t5 = t4[tensor[:,3]<5,:]
print(t5)

t1 = tensor[:2, :4]

t1 = tensor[2:, :3]

t5 = tensor[[[0], [3]], [0,1]] 

t2 = tensor[tensor[:, 3] > 8, :]

t2 = tensor[:, tensor[2, :] > 7]

#多维索引
tensor2 = torch.randint(15, (3, 4, 5, 6))
# 获取第0轴元素
t6 = tensor2[0, :, :, :]

# 获取第3轴的第1,2个元素
t7 = tensor2[:, :, :, 1:3]

tensor3 = torch.randint(0,10,(3,6,6))
print(tensor3)
# 获取第0轴的第1,2个元素
t8 = tensor3[1:3,:,:]
print(t8)

# 获取第1轴的第1,3,5个元素 行
t9 = tensor3[:,1:6:2,:]
print(t9)

# 获取第2轴的第1,3,5个元素 列
t9 = tensor3[:,:,1:6:2]
print(t9)

