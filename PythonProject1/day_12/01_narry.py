import numpy as np

arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
])

print("原始数组：\n", arr)
print("维度：", arr.ndim)

# 索引 同list
print("第一个元素：", arr[0][0])
print("最后一行：", arr[-1])
print("第二行第三列：", arr[1][2])
print("第二行第二列：", arr[1, 1])     # [x, y]  x行 y列
print("第二列：", arr[:, 1])          # :表示全要无所谓行，要下标1的列，即第二列
print("第四列：", arr[:, -1])           # -1表示最后一个列
print("第二三行：\n", arr[1:3,])
print("第二三列：\n" ,arr[:,1:3])