"""
购物车管理系统
功能：添加、修改、删除、查询商品、退出系统
数据结构：字典嵌套字典
shopping_cart = {
    "商品名": {"price": 价格, "num": 数量}
}
"""
print("欢迎使用购物车系统")
#定义字符串
menu = """ 
+========================================================+
|                  🛒 购物车系统                         |
+========================================================+
|                  1. 添加购物车                         |
|                  2. 修改购物车                         |
|                  3. 删除购物车                         |
|                  4. 查询购物车                         |
|                  5. 退出购物车                         |
+========================================================+
"""
dic1 = {} #初始化字典
while True: #主循环
    print(menu) #显示菜单
    #获取用户输入指令
    command = input("请选择要执行的操作（1-5）：")
    #条件判断
    match command:
        case "1":
            print("请输入商品名称：")
            name = input()
            #判断商品是否存在
            if name not in dic1.keys():
                print("请输入商品价格：")
                price = float(input())
                print("请输入商品数量：")
                nums = int(input())
                dic1[name] = {"价格": price, "数量": nums}
                print("商品添加完毕")
            else :
                print("商品已存在")
            print(dic1)
        case "2":
            # 修改商品信息
            print("输入要修改的商品名称：")
            name1 = input()
            # 判断商品是否存在，不存在跳过
            if name1 not in dic1.keys():
                print("该商品不存在")
                continue
            # 如果存在录入最新价格和数量
            else :
                print("请输入商品新价格：")
                price1 = float(input())
                print("请输入商品新数量：")
                nums1 = int(input())
                dic1[name1] = {"价格": price1, "数量": nums1}
            print(dic1)
        case "3":
            print("请输入要删除的商品名称：")
            name2 = input()
            # 判断商品是否存在，不存在跳过
            if name2 not in dic1.keys():
                print("商品不存在，请重新输入！")
                continue
            # 如果存在，根据key删除
            else :
                del dic1[name2]
                print("商品删除完毕！")
            print(dic1)
        case "4":
            # 遍历购物车（字典）
            for keys, values in dic1.items():
                name3 = keys
                price3 = values["价格"]
                nums3 = values["数量"]
                print(f"商品名称:{name3},商品价格:{price3},商品数量：{nums3}")
        case "5":
            # 终止循环
            print("Bye~~~")
            break
        case _:
            print("非法操作，不支持！！！")