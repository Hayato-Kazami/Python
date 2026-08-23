import socket

# 1. 创建socket类对象
server = socket.socket(
    socket.AF_INET,         # IPv4
    socket.SOCK_STREAM      # TCP
)

# 2. bind，选择网卡（IP）和端口
"""
网卡（IP）选择：
1. 127.0.0.1，服务器仅接受127.0.0.1的客户端接入，即只能自己电脑中的客户端接入
2. 0.0.0.0，服务器接收所有来源IP的客户端，谁都可以接入，只要你和我网络是通的 
"""
server.bind(
    ('0.0.0.0', 8080)     # 元组，元素1是IP，元素2是端口
)

# 3. 启动服务器，启动监听，即服务器躲藏在端口后面，真正占用端口开始干活
server.listen()

# 4. 等待客户端接入
# accept是阻塞式，没客户端进来，就卡在这里
# 返回的变量a，是和客户端通讯的TCP对象
# 返回的变量b，是一个元组，记录了接入的客户端的IP和端口
client, client_info = server.accept()
print(f"客户端：{client_info}接入")

# 5. 从这一步开始和客户端通讯，使用上面返回的client对象
# 接收消息
msg_bin = client.recv(1024)       # 1024最大接收长度
print(f"接收客户端{client_info}发来的消息：{msg_bin.decode('utf-8')}")

# 6. 发送（服务器向客户端发）
client.send("收到了，再见".encode("utf-8"))

# 7. 关闭
client.close()      # 仅关闭和这个客户端的通讯
server.close()      # 将服务器整体关闭