class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    # def __str__(self):
    #     # print("我是__str__，我执行了")
    #     return f"我是{self.name},颜色是{self.color}"

dog1 = Dog("jack", "blue")

print(dog1)