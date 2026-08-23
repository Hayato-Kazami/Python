"""
不定长参数又称可变参数，用于参数个数不确定的场景。
1. *args 可变位置参数：接收任意多个位置实参，最终以元组形式存储。
2. **kwargs 可变关键字参数：接收任意多个关键字实参，最终以字典形式存储。
注意：若不定长参数后仍有普通参数，后续参数必须以关键字方式传参。
"""


# 求二个数的和并返回
def add1(a, b):
    return a + b
# 求三个数的和并返回
def add2(a, b, c):
    return a + b + c
# 求四个数的和并返回
# 求五个数的和并返回
# 求n个数的和并返回

# 问题：参数的个数不确定，此时就可以用可变参数来解决
# 1. *args 可变位置参数：接收任意多个位置实参，最终以元组形式存储。
def add(*args,b=2):
    # 累加器
    total = 0
    # 遍历元组 args
    for e in args:
        total+=e  # 累加求和
    # 返回结果
    total+=b
    return total

# 调用函数，注意：可变参数的后面，b 必须使用关键字传参
# print(add(1, 2,3,4))
print(add(1, 2, 3, 9, 10))

print("---------------------------------")


# 打印个人信息：姓名、年龄、性别
def print_info1(name,age,gender):
    print(name,age,gender)

# 打印个人信息：姓名、年龄、性别、地址
def print_info2(name,age,gender,address):
    print(name,age,gender,address)

# 打印个人信息：姓名、年龄、性别、地址、手机号
# 问题：人的描述信息不固定的，可能随时增加，而且要提高可读性
# 2. **kwargs 可变关键字参数：接收任意多个关键字实参，最终以字典形式存储。
def print_info(**kwargs):
    print(kwargs)


print_info(name="jack",age=18,gender="男")
print_info(name="lucy",age=22,gender="女",address="武汉")
print_info(name="lucy",age=22,gender="女",address="武汉",phone="13800138001")