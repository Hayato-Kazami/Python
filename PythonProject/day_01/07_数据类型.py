"""
Python中常见的数据类型
    整数(int)      10 -5 0
    浮点数/小数(float)   3.14 1.0 -3.5
    布尔(bool)    表达现实生活中的逻辑，真或假 True False
    字符串(str)    描述文本的一种数据类型    "人生苦短，我用Python"
    空值(NoneType)    表示空或无值，仅包含一个值None  None
查看数据类型
    type(要查看类型的数据)
"""

# 整数(int)      10 -5 0
print(10, type(10))  # 10 <class 'int'>

# 浮点数/小数(float)   3.14 1.0 -3.5
print(3.4, type(3.4))  # 3.4 <class 'float'>

# 布尔(bool)    表达现实生活中的逻辑，真或假 True False
print(True, type(True))  # True <class 'bool'>

# 字符串(str)    描述文本的一种数据类型    "人生苦短，我用Python"
print("你好", type("你好"))  # 你好 <class 'str'>

# 空值(NoneType)    表示空或无值，仅包含一个值None  None
print(None, type(None))  # None <class 'NoneType'>

# 变量的类型会随着保存内容的类型而产生变化
num = 1
num = "1"
print(num,type(num)) # 1 <class 'int'>   --->  1 <class 'str'>

# 常见数据类型 ---> isinstance(数据, 类型) --> bool值 --> 判定数据是否是指定的类型, 如果是: True, 否则: False
num = -100
print(type(num)) #int

print(isinstance(num, int)) #True
print(isinstance(num, float)) #False
print(isinstance(num, bool)) #False