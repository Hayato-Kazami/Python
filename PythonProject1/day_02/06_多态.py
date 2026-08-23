'''
首先定义一个父类，其可能拥有多个子类对象。当我们调用一个公共方法（接口）时，传递的对象不同，则返回的结果不同。
'''
class Fruit(object):
    def make_juice(self):
        print('i can make juice')

class Apple(Fruit):
    # 重写父类方法
    def make_juice(self):
        print('i can make apple juice')

class Banana(Fruit):
    # 重写父类方法
    def make_juice(self):
        print('i can make banana juice')

class Orange(Fruit):
    # 重写父类方法
    def make_juice(self):
        print('i can make orange juice')

# 定义一个公共接口（专门用于实现榨汁操作）
def service(obj):
    # obj要求是一个实例化对象，可以传入苹果对象/香蕉对象
    obj.make_juice()

# 调用公共方法
service(Orange())