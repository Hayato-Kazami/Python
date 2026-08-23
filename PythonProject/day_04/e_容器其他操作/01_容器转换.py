# 定义列表
list1 = [1, 2, 3, 4, 5]
# 定义元组
tuple1 = (1, 2, 3, 4, 5)
# 定义字符串
str1 = "12345"
# 定义集合
set1 = {1, 2, 3, 4, 5}


# 其他容器转列表
print(list(tuple1))
print(list(str1))
print(list(set1))
print("--------------")

# 其他容器转元组
print(tuple(list1))
print(tuple(str1))
print(tuple(set1))
print("--------------")

# 其他容器转集合
print(set(list1))
print(set(tuple1))
print(set(str1))
print("--------------")

# 其他容器转字符串
# 他的底层将其他容器，用引号包裹起来了
s1 = str(list1)
print(s1,type(s1)) # "[1, 2, 3, 4, 5]" <class 'str'>
s2 = str(tuple1)
print(s2,type(s2)) # "(1, 2, 3, 4, 5)" <class 'str'>
s3 = str(set1)
print(s3,type(s3)) # "{1, 2, 3, 4, 5}" <class 'str'>
print("--------------")

# eval()  将文本的类型的引号干掉
# 举例："[1, 2, 3, 4, 5]"  -> [1, 2, 3, 4, 5]
s4 = "[1, 2, 3, 4, 5]"

lst = eval(s4)
print(lst,type(lst))
