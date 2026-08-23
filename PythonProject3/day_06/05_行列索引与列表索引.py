import torch

torch.manual_seed(100)
# 创建一个二维张量
tensor = torch.randint(10, (4, 5))
print(tensor)

# 行列索引

t1 = tensor[1,:] # 获取第2行的所有元素
print(t1)

t2 = tensor[1, 2] # 获取第2行第3列的元素
print(t2)

# 列表索引

# 获取第0行和第2列，第2行和第4列两个位置的元素
t4 = tensor[[0,1], [2,3]] 
print(t4)

# 获取第0行，第1行，第1行第2列和第4列的元素
t5 = tensor[[[0], [1]], [1,2,4]] 
print(t5)

t6= tensor[[1,2], [0,4]]
print(t6)

t7= tensor[[[0],[2],[3]], [3,4]]
print(t7)

