# ===================== 1. random 模块（随机数）=====================
import random

# 生成 0~1 之间的随机小数
print(random.random())
# 生成 1~10 之间的随机整数
print(random.randint(1, 10))
# 随机选择一个元素
print(random.choice(["苹果", "香蕉", "橙子"]))
print("-----------------")

# ===================== 2. time 模块（时间/延时）=====================
import time

# 获取当前时间戳
print(time.time())
# 程序暂停 5 秒
time.sleep(5)
print("暂停结束")
print("-----------------")
# ===================== 3. math 模块（数学计算）=====================
import math

# 圆周率
print(math.pi)
# 开平方
print(math.sqrt(16))
# 向上取整
print(math.ceil(3.2))