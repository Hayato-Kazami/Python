class Person:

    name = "Person"

    def speak(self):
        print('i am you father')

class Student(Person):
    name = 'Student'            # 将从父类继承的name，覆盖掉

    def speak(self):              # 将从父类继承的run，覆盖掉
        print('我是子类')

stu = Student()
stu.speak()
