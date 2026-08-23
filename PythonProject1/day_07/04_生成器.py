import time

# 列表推导式
lst = [n * 10 for n in range(1, 11) if n % 2 == 0]

# 按推导式语法，将括号从[] 换为()，就可以得到Python的推导式生成器
gen = (n for n in range(1, 101) if n % 2 == 0)


for n in gen:           # for 循环 迭代生成器获得一个个数据
    print(n)