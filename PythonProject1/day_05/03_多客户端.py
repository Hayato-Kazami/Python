"""
需求：服务器可以一个个接入客户端，和每一个客户端收发一次后，断开客户端，等待下一个客户端进入
"""
import socket

# 1. 创建socket对象
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. 选择IP和端口绑定  192.168.11.30
server.bind(("0.0.0.0", 8888))

# 3. 启动监听
server.listen()

# 4. 等待客户端接入（循环接入客户端）
while True:
    try:
        print(f"等待客户端接入中...")
        client, client_info = server.accept()
        print(f"客户端：{client_info}接入")

        # 收一个消息
        msg = client.recv(1024).decode("utf-8")
        print(f"收到客户端：{client_info}，发来的消息：{msg}")

        # 回复一个消息
        client.send("收到，再见！".encode("utf-8"))

        client.close()
    except Exception as e:
        print('出异常了', e)
        server.close()
        raise e         # raise 就是手动抛出异常，继续报错，导致代码崩溃