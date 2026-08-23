def is_prime(n):
    """判断一个数是否为质数"""
    if 1 < n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# 测试函数
# False
print(is_prime(5))   # True

