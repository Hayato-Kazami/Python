class Stu:
    def __init__(self, name):
        self.name = name
        self.__money = 0

    # 公共方法：提供给外部的访问接口
    def get_money(self):
        # 内部访问：允许直接访问
        # 外部访问：根据需求要添加限制条件
        return self.__money

    # 公共方法：提供给外部的设置接口
    def set_money(self, money):
        if not isinstance(money, int):
            print("must int")
            return
        if money < 0:
            print("must bigger than 0")
            return
        self.__money = money

stu = Stu("lily")
stu.set_money(100)
stu.set_money(-50)
print(stu.get_money())