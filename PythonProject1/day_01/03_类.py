class Cat(object):
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def say(self):
        print(f"cat's name is {self.name}")
        print(f"cat's color is {self.color}")
cat1 = Cat("jack", "blue")
cat1.say()
cat2 = Cat("rose", "red")
cat2.say()