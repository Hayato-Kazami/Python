import socket
import threading

def handle_client(client, client_info):
    # 【修复】原代码用 thread.name 赋值了变量 name 但从未使用，已删除该死代码
    try:
        while True:
            data = client.recv(1024)
            if not data:
                break
            data1 = data.decode('utf-8')

            if data1 == 'exit':
                print(f"客户端：{client_info}退出")
                break

            print(f"客户端：{client_info}发送消息：{data1}")
            # 【修复】服务端原代码只收不发，客户端 recv() 永久阻塞，已添加回复
            client.send(f"收到: {data1}".encode('utf-8'))

        print(f"客户端：{client_info}断开连接，线程：{threading.current_thread().name}结束服务")
        client.close()

    except Exception as e:
        print(f"客户端：{client_info}连接异常，线程：{threading.current_thread().name}结束服务，异常：{e}")
        client.close()
        # 【修复】原代码 raise e 在线程中只会让当前线程静默崩溃，主循环无感知，
        # 且异常信息已在上行 print 输出，直接 return 即可，不再抛异常


if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 8080))
    # 【修复】原代码 listen() 无参数，默认 backlog 过小，100 并发连接可能被拒绝
    server.listen(128)
    print("服务器已启动，监听端口：8080")
    while True:
        client, client_info = server.accept()
        thread = threading.Thread(target=handle_client, args=(client, client_info), name=f"Thread-{client_info}")
        thread.start()
