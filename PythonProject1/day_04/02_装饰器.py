# 1. 双层嵌套，同时外层函数的形参中，接收一个函数传入
# 2. 内层函数，对外层函数传入的函数，做增强
# 3. 外层函数返回内层函数本身
def buff(fn):

    def inner():
        print("登录验证中...验证通过，登录成功")
        fn()

    return inner

def download():
    print("下载成功")

# download()    这个是原始comment函数

download = buff(download)

download()       # 这个本质是inner，叫做download，替换了原始的download功能