class Stu:
    def say(self):
        print(f"hello,my name is {self.name}")
        print(f"my age is {self.age}")
stu1 = Stu()
stu1.name = "jack"
stu1.age = 22
stu1.say()
stu2 = Stu()
stu2.name = "rose"
stu2.age = 23
stu2.say()