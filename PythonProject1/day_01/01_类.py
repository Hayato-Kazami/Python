class Student(object):
    name = "jack"
    age = 22
    hobby = ["game","programming"]
    gender = "male"
    height = 175
    def play(self):
        print("playing lol")
    def eat(self):
        print("eating meat")
    def sleep(self):
        print("sleeping")
student = Student()
student.play()
print(f"my name is {student.name}")
print(f"my hobby is {student.hobby}")
student.age = 25
print(f"my age is {student.age}")