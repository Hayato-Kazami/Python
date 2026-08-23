class Person:
    def __init__(self, eat,speak):
        self.eat = eat
        self.speak = speak

    def __play(self):
        print("playing LOL")

class Teacher(Person):
    def intro(self):
        print(f"我在{self.eat}，我会说{self.speak}")

class Stu1(Person):
    def play(self):
        print(f"playing")
stu1 = Stu1("food","cn")
stu1.play()
tea1 = Teacher("food","cn")
tea1.intro()
