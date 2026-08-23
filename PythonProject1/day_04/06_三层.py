"""

1. 定义外层函数，接收参数（装饰器用），此函数名称为装饰器名称
2. 定义中层函数，接收参数（被修饰函数）
3. 定义内层函数，接收参数（被修饰函数的传参）

1. 外层函数return中层函数
2. 中层函数return内层函数
3. 内层函数return被修饰函数返回值

还是统计函数执行时间，装饰器本身是可以收参数，传入s表示统计单位秒，传入ms统计单位毫秒
"""

def time_clac(unit):

    def middle(fn):

        def inner(*args, **kwargs):
            import time
            s = time.time()     # 开始时间
            r = fn(*args, **kwargs)

            e = time.time()
            t = e - s

            if unit == 's':
                print(f"函数{fn.__name__}执行消耗时间：{t:.2f}秒")
            else:
                print(f"函数{fn.__name__}执行消耗时间：{t * 1000:.2f}毫秒")


            return r

        return inner

    return middle


@time_clac('s')
def f2(num):
    for _ in range(2000000):
        num = num + 1
f2(100)