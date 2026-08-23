# def gen_squares(n):
#     for i in range(n):
#         yield i ** 2

# # 生成器可以串联，惰性求值
# squares = gen_squares(100)
# evens = (x for x in squares if x % 2 == 0)  # 只在用到时才算
# print(list(evens))  
# list(evens)  # 此时才真正执行
# print(list(evens))  # 再次调用时，evens已经执行完毕，不会再执行

def echo():
    while True:
        received = yield      # 暂停，等外面 send 进来
        print(f'收到: {received}')

g = echo()
next(g)             # 启动生成器（必须先 next 一次）
g.send('hello')     # 收到: hello
g.send(42)          # 收到: 42
