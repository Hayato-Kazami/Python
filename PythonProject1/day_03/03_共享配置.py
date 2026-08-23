"""
类属性的场景很多，核心一点都是应用在：所有创建出来的对象，共享的特性


class Order:        # 订单
    # 类属性
    TAX_RATE = 0.09                     # 增值税税点
    FREE_SHIP_LIMIT = 99                # 包邮临界价格
    SHIP_PRICE = 10                     # 邮费

    def __init__(self,order_id, amount):
        self.order_id = order_id        # 不同订单对象各自的ID
        self.amount = amount            # 不同订单对象各自的金额

    def total_price(self):
        print("计算订单的实付金额：订单+税点+邮费")
        tax = self.amount * Order.TAX_RATE

        if self.amount > Order.FREE_SHIP_LIMIT:
            ship_price = 0          # 买的多 包邮
        else:
            ship_price = Order.SHIP_PRICE

        print(f"总价格：{self.amount + tax + ship_price}，金额{self.amount}，税点{tax}，邮费{ship_price}")

o1 = Order("1", 100)
o2 = Order("2", 66)
o1.total_price()
o2.total_price()

print()
# 税点变了
Order.TAX_RATE = 0.01
# 邮费便宜了
Order.SHIP_PRICE = 3

o1.total_price()        # 修改类属性，全部对象都受到影响
o2.total_price()        # 修改类属性，全部对象都受到影响

"""




"""
类属性的场景很多，核心一点都是应用在：所有创建出来的对象，共享的特性


# 统计类有多少个对象被创建出来
class Order:
    # 类属性
    counter = 0

    def __init__(self):
        Order.counter += 1          # 创建对象的计数器+1

for _ in range(10):
    Order()

print(f"创建了{Order.counter}个对象")

for _ in range(10):
    Order()
print(f"创建了{Order.counter}个对象")


# ============================================================
# Computer 类：统计生产了多少台电脑
# ============================================================
class Computer:
    """计算机类，类属性 counter 统计实例数量"""
    count = 0          # 类属性：所有实例共享的生产计数器

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Computer.count += 1          # 每创建一个对象，计数器 +1

    @classmethod
    def total_count(cls):
        """随时查询已生产的电脑数量"""
        return cls.count


# --- 测试 ---
print("=" * 40)
pc1 = Computer("联想", "ThinkPad X1")
pc2 = Computer("华为", "MateBook 14")
pc3 = Computer("苹果", "MacBook Pro")

print(f"已生产 {Computer.count} 台电脑")        # 通过类名访问
print(f"已生产 {Computer.total_count()} 台")     # 通过类方法访问

# 再生产一批
for i in range(5):
    Computer(f"品牌{i}", f"型号{i}")

print(f"总共生产了 {Computer.count} 台电脑")
print(f"pc1: {pc1.brand} {pc1.model}")
print(f"pc2: {pc2.brand} {pc2.model}")