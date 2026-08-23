"""
定义：
字典是用花括号 {} 括起来的一系列键值对（Key-Value）    dict1 = {key1: value1, key2: value2}

特点：
1. 存储关联数据：适合存储有对应关系的信息
2. 键唯一：键不能重复，可快速通过键找值

常见操作：
1. 字典.keys()       获取所有键
2. 字典.values()     获取所有值
3. 字典.items()以列表返回可遍历的(键,值)二元组数据
4. 字典[键] = 值     添加元素
5. 字典[键] = 新值   修改元素
6. del 字典[键]      删除指定键值对
7. 字典.clear()      清空字典
"""
"""
定义：
字典是用花括号 {} 括起来的一系列键值对（Key-Value）    dict1 = {key1: value1, key2: value2}

特点：
1. 存储关联数据：适合存储有对应关系的信息
2. 键唯一：键不能重复，可快速通过键找值

常见操作：
1. 字典.keys()       获取所有键
2. 字典.values()     获取所有值
3. 字典.items()以列表返回可遍历的(键,值)二元组数据
4. 字典[键] = 值     添加元素
5. 字典[键] = 新值   修改元素
6. del 字典[键]      删除指定键值对
7. 字典.clear()      清空字典
"""

# 创建一个有元素(kv)的字典
dict1 = {"name": "王大锤", "age": 18, "gender": "男"}
print(dict1, type(dict1))

# 创建空字典
dict2 = {}
print(dict2, type(dict2))

# 1. 存储关联数据：适合存储有对应关系的信息
print(dict1["name"])  # 王大锤

# 2. 键唯一：键不能重复（新值覆盖旧值），可快速通过键找值
dict1["name"] = "王林"
print(dict1)
print("-----------------")
# 1. 字典.keys()       获取所有键
print(dict1.keys())  # dict_keys(['name', 'age', 'gender'])
# 2. 字典.values()     获取所有值
print(dict1.values())  # dict_values(['王林', 18, '男'])
print("-----------------")
# 3. 字典.items()以列表返回可遍历的(键,值)二元组数据
for key, value in dict1.items():
    print(key, value)
print("-" * 15)
# 4. 字典[键] = 值     添加元素
dict1["address"] = "罗天星域"
print(dict1)
# 5. 字典[键] = 新值   修改元素
dict1["age"] = 230
print(dict1)
# 6. del 字典[键]      删除指定键值对
del dict1["gender"]
print(dict1)
# 7. 字典.clear()      清空字典
dict1.clear()
print(dict1)
