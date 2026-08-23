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
cursor.execute("SELECT name, price FROM goods WHERE price > 5000")

# 4. 获取结果
# cursor游标对象，提供了fetchall方法，一次性取得全部查询结果
# 返回值是：元组套元组，比如返回结果是：
# name age gender
# 周杰轮 11 男
# 王立宏 12 男
# 蔡一林 16 女
# 则fetchall得到的是：
# (
#   ('周杰轮', 11, '男'),
#   ('王立宏', 12, '男'),
#   ('蔡一林', 16, '女')
# )
# 如上，元组套元组
r = cursor.fetchall()
for one_result in r:
    name = one_result[0]
    price = one_result[1]
    print(name, price)

# 5. 关闭小弟
cursor.close()

# 6. 关闭TCP
client.close()