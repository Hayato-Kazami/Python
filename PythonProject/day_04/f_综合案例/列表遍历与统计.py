"""
列表遍历与统计
列表：nums = [11, 22, 33, 44, 55, 66, 77, 88]
1. 遍历输出所有元素
2. 统计其中偶数的个数
"""
nums = [11, 22, 33, 44, 55, 66, 77, 88]

# 1. 遍历输出所有元素
print("所有元素：")
for num in nums:
    print(num, end=" ")
print()

# 2. 统计其中偶数的个数
even_count = 0
for num in nums:
    if num % 2 == 0:
        even_count += 1
print(f"偶数个数: {even_count}")
