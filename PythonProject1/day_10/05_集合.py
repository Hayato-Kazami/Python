import redis

# 创建TCP客户端，连接redis服务器
r = redis.Redis(
    host="127.0.0.1",   # 主机就是本机
    port=6379,          # 端口6379 redis默认使用端口
    db=0,               # redis数据库是数字序号，从0开始，任选一个
    password=None,      # 没密码
    decode_responses=True,      # 自动解码（redis返回的都是二进制字节数组），可以直接看出字符串本身
)

# 存入  s->set
r.sadd("set1", "Python", "itheima", "itcast", "Python")
# 获取全部
all_tags: set = r.smembers("set1")
print(all_tags)

# 判断元素是否存在
flag = r.sismember("set1", "Python123")
print("是否存在Python123", flag)       # 1是True 0是False

# 弹出元素(随机)
# tag = r.spop("set1")
# print("弹出", tag)

# 弹出元素（指定）（即指定元素删除） rem-> remove
r.srem("set1", "itcast")


r.close()