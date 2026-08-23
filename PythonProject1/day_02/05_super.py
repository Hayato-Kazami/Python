class Person:

    def __init__(self, info):
        print("父类init执行了")
        self.info = info

class Student(Person):

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

        # 明确手动调用父类的init，让父类init中的属性拥有值，方便子类使用
        # super()表示，以自身为基点，指向MRO中的下一个
        super().__init__("hello")

print(Student.__mro__)
stu = Student("王大锤", 11, "男")
print(stu.name, stu.age, stu.gender)
print(stu.info)