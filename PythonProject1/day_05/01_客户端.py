import socket

# 1. 创建Socket对象
client = socket.socket(
    socket.AF_INET,         # 本质是数字2，表示地址类型是IPv4，如果用IPv6地址，参数写 AF_INET6
    socket.SOCK_STREAM      # TCP通讯
)


# 2. 创建连接，到服务器
client.connect(("127.0.0.1", 8888))

# 3. 发送
msg = "你好呀帅哥"
client.send(msg.encode("utf-8"))

# 4. 接收回复，recv方法，是阻塞式的，如果没回复，就卡在这里直到有消息
msg_bin = client.recv(1024)       # 1024表示最大接收长度
print(f"收到服务器回复：{msg_bin.decode("utf-8")}")
# 5. 关闭
client.close()
