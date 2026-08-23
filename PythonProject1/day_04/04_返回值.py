
def time_clac(fn):

    def inner(num):     # 内层函数接收参数
        import time
        s = time.time()
        fn(num)         # 将接收参数传入被修饰函数

        print(f"消耗时间：{time.time() - s: .2f}秒")
        return fn(num)
                   # 被修饰函数的返回值，通过inner中接收被修饰函数返回值并return出去
    return inner

@time_clac
def sum_num(num):
    n = 0
    for i in range(1, num + 1):
        n += i

    return n


n = sum_num(10)
print(f"累加结果：{n}")
