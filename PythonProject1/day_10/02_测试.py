import redis

# 创建TCP客户端，连接redis服务器
r = redis.Redis(
    host="127.0.0.1",   # 主机就是本机
    port=6379,          # 端口6379 redis默认使用端口
    db=0,               # redis数据库是数字序号，从0开始，任选一个
    password=None,      # 没密码
    decode_responses=True,      # 自动解码（redis返回的都是二进制字节数组），可以直接看出字符串本身
)

# 一次性存入1个字符串
r.set('name', '王大锤')        # 传参就是K V
r.set('age', '25')            # 传参就是K V

# 取出，按key取出value
name = r.get('name')
age = r.get('age')
print(name, age)

print("-------------------------")

# 一次性存入多个字符串 mset   m: multi（多）
# mset传入一个字典，将字典的多个key和v存入redis
r.mset(
    {
        "hobby": "唱跳RAP",
        "money": "12312",
        "gender": "男"
    }
)

# 一次性取出多个key的v
values = r.mget(['name', 'age', 'hobby', 'money', 'gender'])
print(f"多个值：", values)

r.close()