
class Pot(object):
    def make_rice(self):
        print('i can make rice')

class Pot1(Pot):
    # 重写父类方法
    def make_rice(self):
        print('i can make porridge')

class Pot2(Pot):
    # 重写父类方法
    def make_rice(self):
        print('i can make soup')

class Pot3(Pot):
    # 重写父类方法
    def make_rice(self):
        print('i can make hot_pot')

# 定义一个公共接口（专门用于实现榨汁操作）
def service(obj):
    # obj要求是一个实例化对象，可以传入苹果对象/香蕉对象
    obj.make_rice()

# 调用公共方法
service(Pot1())
service(Pot2())
service(Pot3())
