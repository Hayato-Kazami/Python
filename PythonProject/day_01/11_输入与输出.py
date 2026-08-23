"""
input()函数接受用户的输入信息，如果用户没有输入任何内容，则一直等待，它的返回值就是用户的输入的内容，输入内容的类型为字符串类型
变量名称 = input('提示信息：')

print()函数实现变量或数据的打印输出
print(内容1，内容2，....)
"""

# 这个写法就是将用户输入的内容存储到name变量
name = input("请输入您的名字:")
print(name, type(name))  # 王林 <class 'str'>

# 注意：输入内容的类型为字符串类型
age_str = input("请输入您的年龄:")
print(age_str, type(age_str))  # 18 <class 'str'>

# 可以手动转换为其他类型
age = int(age_str)
print(age, type(age)) # 18 <class 'int'>