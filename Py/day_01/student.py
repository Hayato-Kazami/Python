# 导入json模块，用于处理JSON数据
import json

# 定义一个名为Student的类，继承自object
class Student(object):

    # 初始化方法，用于创建Student对象时设置各个属性
    def __init__(self, name, gender, tel, age, nickname):
        self.name = name  # 学生姓名
        self.gender = gender  # 学生性别
        self.tel = tel  # 学生电话号码
        self.age = age  # 学生年龄
        self.nickname = nickname  # 学生昵称

    # 定义一个特殊方法__str__，用于返回对象的字符串表示
    def __str__(self):
        # 创建一个字典stu_d，包含学生的各个属性
        stu_d = {
            "name": self.name,
            "gender": self.gender,
            "tel": self.tel,
            "age": self.age,
            "nickname": self.nickname
        }
        # 使用json.dumps将字典stu_d转换为JSON格式的字符串，并返回
        # 参数ensure_ascii=False用于确保中文字符正确显示，而不是被转义为ASCII码
        return json.dumps(stu_d, ensure_ascii=False)

    # 定义一个静态方法generate，用于从JSON字符串生成Student对象
    @staticmethod
    def generate(json_str):
        # 使用json.loads将JSON格式的字符串转换为字典stu_d
        stu_d = json.loads(json_str)
        # 使用字典解包的方式创建Student对象，返回该对象
        # 这种方式避免了手动指定每个参数
        return Student(**stu_d)
        # 下面是另一种创建Student对象的方式，但使用了字典解包，更为简洁
        # return Student(name=stu_d['name'], gender=stu_d['gender'], tel=stu_d['tel'], age=stu_d['age'], nickname=stu_d['nickname'])

# 判断当前模块是否作为主程序运行
if __name__ == '__main__':
    # 创建一个Student对象stu，传入姓名、性别、电话、年龄和昵称
    stu = Student("周杰轮", "女", "18500001111", 11, "舔狗")
    # 打印stu对象的字符串表示，调用了__str__方法
    print(stu)

    # 使用generate静态方法从JSON字符串创建另一个Student对象stu2
    stu2 = Student.generate('{"name": "周杰轮", "gender": "女", "tel": "18500001111", "age": 11, "nickname": "舔狗"}')
    # 分别打印stu2的各个属性
    print(stu2.name)
    print(stu2.gender)
    print(stu2.tel)
    print(stu2.age)
    print(stu2.nickname)
    print(__name__)