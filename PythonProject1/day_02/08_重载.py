# 运算符重载，重新定义Student类中 + 号的逻辑
class Student:
    def __init__(self, score):
        self.score = score

    def __add__(self, other):
        # self是自己，other被+的另一个
        sum = self.score - other.score
        return Student(sum)

stu1 = Student(100)
stu2 = Student(90)
stu3 = stu1 + stu2
print(stu3.score)
print(type(stu3))