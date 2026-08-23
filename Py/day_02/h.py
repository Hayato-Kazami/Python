class Person:
    def __init__(self, name, age):
        self.__name = name  # 私有属性
        self.__age = age    # 私有属性

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if self.__is_valid_age(new_age):  # 调用私有方法
            self.__age = new_age
        else:
            print("年龄设置不合法")

    def __is_valid_age(self, age):
        # 私有方法，用于验证年龄是否合法
        return 0 < age < 150

# 创建Person类的一个实例
person = Person("张三", 30)

# 访问私有方法（这会引发AttributeError）
# person.__is_valid_age(35)

# 通过公共方法间接调用私有方法
print(person.get_age())  # 输出: 30
person.set_age(35)
print(person.get_age())  # 输出: 35
person.set_age(200)      # 输出: 年龄设置不合法

