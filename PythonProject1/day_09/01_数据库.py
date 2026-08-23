import pymysql

# 1. 创建TCP连接
client = pymysql.connect(
    host="116.62.66.200",       # MySQL服务器IP
    port=3306,              # 端口
    user="zhaojian",            # 用户名
    password="ITheima@2026",      # 密码
    db="zhaojian_homework",         # 要连接使用的数据库
    charset="utf8"          # 编码集（千万千万要写utf8  不要写 utf-8）
)

# 2. 客户端执行方法获取信息
print(client.get_server_info())

# 3. 关闭连接
client.close()