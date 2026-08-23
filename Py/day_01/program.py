import socket
import multiprocessing

def handle_client(client, client_info, client_connections):
    client_ip = client_info[0]
    
    # 记录客户端接入次数
    if client_ip in client_connections:
        client_connections[client_ip] += 1
    else:
        client_connections[client_ip] = 1
    
    print(f"客户端：{client_info}接入，剩余{5 - client_connections[client_ip]}次对话机会")
    
    while True:
        try:
            # 接收消息
            msg_bin = client.recv(1024)  # 1024最大接收长度
            if msg_bin:
                msg = msg_bin.decode('utf-8')
                print(f"收到客户端数据: {msg}")
                
                if msg.lower() == 'bye':
                    print(f"客户端：{client_info} 发来 'bye'，关闭连接")
                    client.send("再见！".encode('utf-8'))
                    client.close()
                    break
                
                response = f"服务器已收到您的数据，您还剩余{5 - client_connections[client_ip]}次对话机会"
                client.send(response.encode('utf-8'))
                
            else:
                print(f"客户端：{client_info} 断开连接")
                client.close()
                break
            
        except Exception as e:
            print(f"发生错误：{e}")
            client.close()
            print(f"已断开与客户端 {client_info} 的连接")
            break

def main():
    import socket
    import multiprocessing

    # 1. 创建socket类对象
    server = socket.socket(
        socket.AF_INET,         # IPv4
        socket.SOCK_STREAM      # TCP
    )

    # 2. bind，选择网卡（IP）和端口
    server.bind(
        ('127.0.0.1', 9999)     # 元组，元素1是IP，元素2是端口
    )

    # 3. 启动服务器，启动监听
    server.listen()
    print("服务器已启动，等待客户端接入...")

    client_connections = multiprocessing.Manager().dict()  # 用于记录客户端接入次数
    processes = []

    try:
        while True:
            if len(processes) >= 5:
                print("已达到最大连接数，等待客户端断开...")
                for p in processes:
                    if not p.is_alive():
                        processes.remove(p)
                        print(f"一个客户端已断开，当前连接数：{len(processes)}")
                continue

            # 4. 等待客户端接入
            client, client_info = server.accept()

            # 启动子进程来处理客户端连接
            p = multiprocessing.Process(target=handle_client, args=(client, client_info, client_connections))
            p.start()
            processes.append(p)

    except KeyboardInterrupt:
        print("服务器关闭")
        server.close()

if __name__ == '__main__':
    main()