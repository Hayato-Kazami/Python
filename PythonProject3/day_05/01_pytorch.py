import torch
import numpy as np

# ============================================================
# 需求1：使用numpy数组随机创建维度为(2, 4, 4)的张量
# ============================================================
print("=" * 50)
print("需求1：numpy随机创建 (2,4,4) 张量")
print("=" * 50)

np_array = np.random.randn(2, 4, 4)  # 标准正态分布随机数
tensor_from_numpy = torch.tensor(np_array)

print("NumPy数组:")
print(np_array)
print("\n转换后的张量:")
print(tensor_from_numpy)
print(f"\n张量形状: {tensor_from_numpy.shape}")
print(f"张量数据类型: {tensor_from_numpy.dtype}")

# ============================================================
# 需求2：使用列表创建三维张量
# ============================================================
print("\n" + "=" * 50)
print("需求2：列表创建三维张量")
print("=" * 50)

data = [
    [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12]],

    [[13, 14, 15, 16],
     [17, 18, 19, 20],
     [21, 22, 23, 24]]
]

tensor_from_list = torch.tensor(data)

print("三维张量:")
print(tensor_from_list)
print(f"\n张量形状: {tensor_from_list.shape}")
print(f"张量数据类型: {tensor_from_list.dtype}")
print(f"维度数: {tensor_from_list.ndim}")
