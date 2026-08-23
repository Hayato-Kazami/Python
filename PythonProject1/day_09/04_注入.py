import pymysql

username = input("请输入用户名：")
password = input("请输入密码：")

conn = pymysql.connect(
    host="127.0.0.1",       # MySQL服务器IP
    port=3306,              # 端口
    user="root",            # 用户名
    password="123456",      # 密码
    db="jing_dong",         # 要连接使用的数据库
    charset="utf8"          # 编码集（千万千万要写utf8  不要写 utf-8）
)
cursor = conn.cursor()

sql = f"SELECT * FROM user WHERE user='{username}' AND pwd='{password}'"
print(sql)
cursor.execute(sql)
all_row = cursor.fetchall()
if len(all_row) > 0:
    print("登录成功")
else:
    print("登录失败")

cursor.close()
conn.close()

# 占位符 %s，参数放到 execute 第二个参数（元组）里 传入的必须是元组，单参数也要写 (value,)，不能写 (value)
sql = "SELECT * FROM users WHERE name=%s AND pwd=%s"
cursor.execute(sql, (username, password))

# pymysql 会自动转义/安全处理，用户输入永远不会被当成 SQL 代码执行

# 查询
cursor.execute("SELECT * FROM users WHERE id=%s", (user_id,))

# 插入
cursor.execute(
    "INSERT INTO users (name, pwd) VALUES (%s, %s)",
    (username, password)
)
conn.commit()

# 批量插入（高效）
cursor.executemany(
    "INSERT INTO users (name, pwd) VALUES (%s, %s)",
    [("a", "1"), ("b", "2"), ("c", "3")]
)
conn.commit()

# 更新 / 删除
cursor.execute("UPDATE users SET pwd=%s WHERE name=%s", (new_pwd, username))
cursor.execute("DELETE FROM users WHERE id=%s", (user_id,))
conn.commit()

# 防止查询结果里带密码等敏感字段，只取需要的列
cursor.execute("SELECT id, name FROM users WHERE name=%s", (username,))
