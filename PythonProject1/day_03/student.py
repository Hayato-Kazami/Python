import json

class Student(object):
    def __init__(self, name,gender,tel,age,nickname):
        self.name = name
        self.gender = gender
        self.tel = tel
        self.age = age
        self.nickname = nickname

    # 定义一个特殊方法__str__，用于返回对象的字符串表示
    def __str__(self):
        stu_d = {
            "name": self.name,
            "gender": self.gender,
            "tel": self.tel,
            "age": self.age,
            "nickname": self.nickname,
        }
    # 使用json.dumps将字典stu_d转换为JSON格式的字符串，并返回
        return json.dumps(stu_d, ensure_ascii=False)

    # 定义一个静态方法generate，用于从JSON字符串生成Student对象
    @staticmethod
    def generate(json_str):
        # 使用json.loads将JSON格式的字符串转换为字典stu_d
        stu_d = json.loads(json_str)
        # 使用字典解包的方式创建Student对象，返回该对象
        # 这种方式避免了手动指定每个参数
        return Student(**stu_d)
        # return Student(name=stu_d['name'], gender=stu_d['gender'], tel=stu_d['tel'], age=stu_d['age'], nickname=stu_d['nickname'])
