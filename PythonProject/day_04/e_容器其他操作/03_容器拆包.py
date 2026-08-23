s = "abc"
# 拆包
a,b,c = s
print(a)
print(b)
print(c)
print("----")

# 2.列表 list
# 打包
lst = [1,2,3]
# 拆包
a,b,c = lst
print(a)
print(b)
print(c)
print("----")

# 3.元组 tuple
# 打包
t = (1,2,3)
# 拆包
a,b,c = t
print(a)
print(b)
print(c)
print("----")

# 4.集合 set
# 打包
se = {"a","c",3}
# 拆包
a,b,c=se
print(a)
print(b)
print(c)
print("----")

# 5.字典 dict
# 打包
dic = {"name":"tom","age":18,"address":"合肥"}

# 拆包
# a,b = dic
# print(a)
# print(b)

# *c 是一个可变参数（里面可以装任意个）
a,*c = dic
print(a)
print(c)

# 字典特殊拆包 **变量名（把键值对同时取出，但无法查询）
dict2 = {**dic,"gender":"男"}
print(dict2)
