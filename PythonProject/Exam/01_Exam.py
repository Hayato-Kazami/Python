
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

total = 0
for n in nums:
    if n % 2 != 0 and n % 3 == 0:
        total += n

print(f"既是奇数又是3的倍数的数字总和为: {total}")
