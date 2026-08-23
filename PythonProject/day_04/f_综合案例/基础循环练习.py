"""
基础循环练习
1. 用 for 循环打印 1~20 所有偶数
2. 用 while 循环计算 1~40 的和
"""
# 1. for 循环打印 1~20 所有偶数
print("1~20 的偶数：")
for i in range(1, 21):
    if i % 2 == 0:
        print(i, end=" ")
print()

# 2. while 循环计算 1~40 的和
total = 0
i = 1
while i <= 40:
    total += i
    i += 1
print(f"1~40 的和：{total}")
