
class Computer:

    # 类属性的定义（创建），写在方法之外
    brand = "联想"

    def __init__(self, name, price):
        # 成员属性，使用self.
        self.name = name
        self.price = price

    def __str__(self):
        # 在方法中，可以通过self.brand访问类属性 ，仅在自身不存在brand成员属性的时候，会自动访问类属性
        # return f"我是{self.brand}品牌，{self.name}，{self.price}"
        # 访问类属性，标准写法：类名.
        return f"我是{Computer.brand}品牌，{self.name}，{self.price}"

cpt1 = Computer("拯救者", 9999)
cpt2 = Computer("Thinkpad", 15999)

print(cpt1)
print(cpt2)

# 类外部访问类属性，类名.
Computer.brand = "戴尔"
print(cpt1)
print(cpt2)

# 本质上访问的是：成员属性，即self系列，但是没有这个成员属性，会使用类属性
print(cpt1.brand)
print(cpt2.brand)

#
cpt1.brand = "雷神"       # 给cpt1添加了self.brand 成员属性
print(cpt1.brand)       # 雷神  访问的是cpt1的self.brand 得到雷神
print(cpt2.brand)       # 戴尔  但是没有这个成员属性，会使用类属性

print(cpt1)             # 品牌还是戴尔
print(cpt2)             # 品牌还是戴尔