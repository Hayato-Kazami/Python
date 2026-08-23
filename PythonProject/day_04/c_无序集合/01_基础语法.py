"""
定义：
- 集合使用花括号 {} 定义，多个元素间用逗号分隔：set1 = {1, 2, 3}
- 定义空集合必须使用 set()，不可使用 {}：set2 = set()
特点:
1. 无序性：元素无固定顺序，不支持通过下标 / 索引访问元素。
2. 唯一性：元素不允许重复，可利用此特性对序列快速去重。

add(元素)：向集合中添加一个元素
remove(元素)：从集合中删除指定元素，不存在则报错
len(集合)：获取集合元素个数
in：判断元素是否在集合中
支持遍历：for 变量 in 集合:
"""
"""
定义：
- 集合使用花括号 {} 定义，多个元素间用逗号分隔：set1 = {1, 2, 3}
- 定义空集合必须使用 set()，不可使用 {}：set2 = set()
特点:
1. 无序性：元素无固定顺序，不支持通过下标 / 索引访问元素。
2. 唯一性：元素不允许重复，可利用此特性对序列快速去重。

add(元素)：向集合中添加一个元素
remove(元素)：从集合中删除指定元素，不存在则报错
len(集合)：获取集合元素个数
in：判断元素是否在集合中
支持遍历：for 变量 in 集合:
"""

# 定义有元素的集合
set1 = {1, 2, 3, "哈哈"}
print(set1, type(set1))  # {1, 2, 3, '哈哈'} <class 'set'>

# 定义没有元素的集合
set2 = set()
print(set2, type(set2))  # set() <class 'set'>

# 错误示范
set3 = {}
print(set3, type(set3))  # {} <class 'dict'>

print("-------------")
# 1. 无序性：元素无固定顺序，不支持通过下标 / 索引访问元素。
set4 = {7, 9, 12, 6, 3, 2, 1}
print(set4)  # {1, 2, 3, 6, 7, 9, 12}  python进行了优化

set5 = {"你好", "python", "大模型", "RAG"}
print(set5)

# print(set5[1])# TypeError: 'set' object is not subscriptable
print("-------------")

# 2. 唯一性：元素不允许重复，可利用此特性对序列快速去重。
set6 = {1, 2, 3, 3, 2, 1}
print(set6) # {1, 2, 3}
print("-------------")


# add(元素)：向集合中添加一个元素
set6.add(4)
print(set6)
# remove(元素)：从集合中删除指定元素，不存在则报错
set6.remove(4)
# set6.remove(6) # KeyError: 6
print(set6)
# len(集合)：获取集合元素个数
print(len(set6))
# in：判断元素是否在集合中
print(3 in set6)
print("-------------")
# 支持遍历：for 变量 in 集合:
for e in set6:
    print(e)