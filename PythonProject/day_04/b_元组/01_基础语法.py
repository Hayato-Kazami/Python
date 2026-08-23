"""
元组是与列表结构相似的有序容器数据类型，核心特征为元素不可修改。
定义格式：
- 标准定义：tuple1 = (1, 2, 3)
- 单元素规范：仅含一个元素时，必须尾随逗号：(1,)

常见操作
- 元组 [索引]：通过下标索引获取对应位置的元素
- index (元素)：查找指定元素，存在则返回首次出现的下标，不存在则报错
- count (元素)：统计指定元素在元组中出现的次数
- len (元组)：获取元组内元素的总个数
"""
"""
元组是与列表结构相似的有序容器数据类型，核心特征为元素不可修改。
定义格式：
- 标准定义：tuple1 = (1, 2, 3)
- 单元素规范：仅含一个元素时，必须尾随逗号：(1,)

常见操作
- 元组 [索引]：通过下标索引获取对应位置的元素
- index (元素)：查找指定元素，存在则返回首次出现的下标，不存在则报错
- count (元素)：统计指定元素在元组中出现的次数
- len (元组)：获取元组内元素的总个数
"""

# 定义元组，有多个元素时
tuple1 = (1, 2, 3, 3, 2, 1)
print(tuple1, type(tuple1))  # (1, 2, 3, 3, 2, 1) <class 'tuple'>

# 定义元组，仅有一个元素时
tuple2 = (1,)
print(tuple2,type(tuple2)) # (1,) <class 'tuple'>

# 错误示范
tuple3 = (1)
print(tuple3,type(tuple3)) # 1 <class 'int'>

print("---------------")
# 元组 [索引]：通过下标索引获取对应位置的元素
print(tuple1[4]) # 2
print(tuple1[0:3:1]) # (1, 2, 3)
print("---------------")
# index (元素)：查找指定元素，存在则返回首次出现的下标，不存在则报错
print(tuple1.index(3)) # 2
# print(tuple1.index(5)) # ValueError: tuple.index(x): x not in tuple
print("---------------")
# count (元素)：统计指定元素在元组中出现的次数
print(tuple1.count(3))# 2
print(tuple1.count(5))# 0
print("---------------")
# len (元组)：获取元组内元素的总个数
print(len(tuple1)) # 6
print("---------------")
# 元组是不可变的
# tuple1[2] = 6 # TypeError: 'tuple' object does not support item assignment

# 元组遍历
for e in tuple1:
    print(e)