# 1. 普通命名函数
def out_line():
    print('--------------------')

def add(x, y):
    return x + y

out_line()
print(add(10, 20))

line_func = lambda: print('----------------')

# 有参 lambda
add_func = lambda x, y: x + y

# 调用
line_func()
print(add_func(10, 20))