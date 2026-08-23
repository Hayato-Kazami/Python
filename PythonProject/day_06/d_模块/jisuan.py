# 两个变量
name = "加法函数"
_desc = "提供两数相加的计算逻辑"


def add(a, b):
    """
    定义一个加法的函数
    """
    return a + b

# 测试
print(add(1, 2))

# 封装在函数中，避免直接执行
def print_module_info():
    print("这是 jisuan 模块中的 print 语句")
print(__name__)