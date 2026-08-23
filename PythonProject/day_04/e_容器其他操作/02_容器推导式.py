# list 语法：[表达式 for 变量 in 可迭代对象 if 条件]
lst = [ele for ele in range(10)]
print(lst)

# set 语法：{表达式 for 变量 in 可迭代对象 if 条件}
set1 = {ele for ele in range(10)}
print(set1)

# dict 语法：{k表达式:v表达式 for 变量 in 可迭代对象 if 条件}
dict1 = {ele : ele ** 2 for ele in range(10)}
print(dict1)