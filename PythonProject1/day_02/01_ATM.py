"""
ATM取款机案例

属性：
    用户名
    用户的密码       -- 私有
    用户的余额       -- 私有

行为：
    验证用户密码是否正确  -- 私有
    取款（先验证密码）
    存款（先验证密码）
    查询余额（先验证密码）
    修改密码（先验证密码）
"""

class ATM:

    def __init__(self, name, password):
        self.name = name
        self.__password = password      # 允许创建对象的时候，设定初始密码
        self.__money = 0                # 创建对象的时候，余额初始固定0

    def __check_password(self):
        password = input("请输入你的密码")
        if password == self.__password:
            print("密码正确")
            return True

        print("密码错误")
        return False

    def get_money(self, num):
        # 先验证密码
        if not self.__check_password():
            print("密码错误，不给取款")
            return

        # 验证余额
        if self.__money >= num:
            print(f"取款成功{num}元")
            self.__money -= num
        else:
            print(f"余额不足")

    def save_money(self, num):
        # 先验证密码
        if not self.__check_password():
            print("密码错误，不给存款")
            return

        self.__money += num
        print(f"存款成功{num}元")

    def query_money(self):
        # 先验证密码
        if not self.__check_password():
            print("密码错误，不给查询余额")
            return

        print(f"用户{self.name}，余额{self.__money}元")

    def modify_password(self):
        if not self.__check_password():
            print("密码错误，不给修改密码")
            return

        new_password = input("请输入你的新密码")
        self.__password = new_password

atm = ATM("周杰轮", "123456")

atm.save_money(100)
atm.query_money()