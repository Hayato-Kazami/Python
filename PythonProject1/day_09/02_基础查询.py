import pymysql

# 1. 创建连接，client对象只负责维护TCP连接，不干活
client = pymysql.connect(
    host="127.0.0.1",       # MySQL服务器IP
    port=3306,              # 端口
    user="root",            # 用户名
    password="123456",      # 密码
    database="jing_dong",   # 要连接使用的数据库
    charset="utf8"          # 编码集（千万千万要写utf8  不要写 utf-8）
)

# 2. 创建一个干活的小弟，游标对象
cursor = client.cursor()

# 3. 执行SQL
# 游标对象提供：execute()方法，传参只有1个：SQL字符串
cursor.execute("SELECT name, brand_name ,price FROM goods WHERE price > 2000")

# 4. 获取结果
# cursor.fetchone()  fetch抓取 one一个， 抓取一行结果，结果是元组对象，如：('r510vc 15.6英寸笔记本', 3399)
while True:
    one_result = cursor.fetchone()
    if not one_result:
        break
    name = one_result[0]
    brand = one_result[1]
    price = one_result[2]
    print(name, brand, price)


# 5. 关闭小弟
cursor.close()

# 6. 关闭TCP
client.close()
