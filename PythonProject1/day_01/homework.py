class Student:
    def __init__(self, name, age,addr):
        self.name = name
        self.age = age
        self.addr = addr
        self.__score = 0
    def __del__(self):
        print("Student对象被销毁了")
    def __str__(self):
        return f"我是{self.name}，我今年{self.age}岁，我住在{self.addr}。"
    def get_score(self):
        return self.__score
    def __increment_score(self, increase):
        if self.__score<=100:
            self.__score += increase
            if self.__score > 100:
                self.__score = 100
    def __decrement_score(self, decrease):
        if self.__score>=0:
            self.__score -= decrease
            if self.__score < 0:
                self.__score = 0
    def study(self,increase=1):
        self.__increment_score(increase)
    def play(self,decrease=-1):
        self.__decrement_score(decrease)

stu1 = Student("小明", 12, "北京")
stu1.study(1)
print(stu1.get_score())
stu1.play(-1)
print(stu1.get_score())
print(stu1)
