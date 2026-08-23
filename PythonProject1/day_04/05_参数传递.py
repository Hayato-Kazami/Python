def buff(fn):

    def inner(*args, **kwargs):
        print("开始")
        r = fn(*args, **kwargs)
        print("结束")

        return r
        
    return inner

@buff
def sum_num(num):
    n = 0
    for i in range(1, num + 1):
        n += i
    return n

@buff
def add(x, y):
    return x + y

print(sum_num(5))        # 15
print(sum_num(num=6))   # 21
print(add(3, y=5))      # 8