class Car:
    brand = "bmw"
    car_type = "gasoline"

    def __init__(self, name,price):
        self.name = name
        self.price = price

    def __str__(self):
        # 在方法中，可以通过self.brand访问类属性 ，仅在自身不存在brand成员属性的时候，会自动访问类属性
        # return f"我是{self.brand}品牌，{self.name}，{self.price}"
        # 访问类属性，标准写法：类名.
        return f"我是{Car.brand}品牌，我用{Car.car_type},{self.name}，{self.price}"

cpt1 = Car("xt5", 9999)
cpt2 = Car("zt6", 15999)

print(cpt1)
print(cpt2)

# 类外部访问类属性，类名.
Car.brand = "Benz"
print(cpt1)
print(cpt2)

# 本质上访问的是：成员属性，即self系列，但是没有这个成员属性，会使用类属性
print(cpt1.brand)
print(cpt2.brand)

#
cpt1.brand = "rolls"       # 给cpt1添加了self.brand 成员属性
print(cpt1.brand)       #  访问的是cpt1的self.brand rolls
print(cpt2.brand)       #  但是没有这个成员属性，会使用类属性 Benz

print(cpt1)             # Benz
print(cpt2)             # Benz