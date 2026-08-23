"""
案例：
键盘输入一个整数，判断这个数字是否在10-20之间
键盘输入用户名，判断是否是管理员（admin 或 root）
"""

# 键盘输入一个整数，判断这个数字是否在10-20之间
# 1-1.键盘录入一个整数
num = int(input("请输入一个整数："))

# 1-2.判断这个数字是否在10-20之间
result = (10<= num <= 20)

# 1-3.输出结果
print(f"{num}是否在10-20之间：{result}")

# 键盘输入用户名，判断是否是管理员（admin 或 root）
# 2-1.键盘录入
username = input("请输入用户名：")

# 2-2.判断是否是管理员（admin 或 root）
is_admin = username=="admin" or username =="root"

# 2-3.输出结果
print("是否是管理员：", is_admin)