import redis

# 创建TCP客户端，连接redis服务器
r = redis.Redis(
    host="127.0.0.1",   # 主机就是本机
    port=6379,          # 端口6379 redis默认使用端口
    db=0,               # redis数据库是数字序号，从0开始，任选一个
    password=None,      # 没密码
    decode_responses=True,      # 自动解码（redis返回的都是二进制字节数组），可以直接看出字符串本身
)

try:
    r.ping()
    print("连接成功")
    r.close()
except Exception as e:
    print("连接失败", e)
    r.close()