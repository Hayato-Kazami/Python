"""
案例：要求输入两个整数x与y，分别输出x+y的结果和x-y的结果
"""

# 1.要求输入两个整数x与y -->键盘录入
x_str = input("请输入第一个x:")
y_str = input("请输入第二个y:")

# 2.将接收的字符串类型转为整数类型
x = int(x_str)
y = int(y_str)

# 3.计算x+y 和 x-y
add = x + y
sub = x - y

# 4.输出结果
print(f"{x} + {y} = {add}")
print(f"{x} - {y} = {sub}")