class Stu:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __eq__(self, other):		# 接收一个other的形参，表示另一个被比较的
        # self是自己，other是另一个
        if self.name == other.name and self.age == other.age and self.gender == other.gender:
            return True
        return False
# __eq__方法，应该返回Ture or False

stu1 = Stu("lib",25,"male")
stu2 = Stu("lily",26,"female")
stu3 = Stu("lili",27,"male")
stu4 = Stu("lili",27,"male")
print(id(stu1))
print(id(stu2))
print(id(stu3))
print(id(stu4))
print(stu1 == stu2)
print(stu3 == stu4)# dog1 == dog2 本质就是 dog1.__eq__(dog2)