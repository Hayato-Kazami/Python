import socket
import threading

def client_thread(client,client_info):
    thread = threading.current_thread()
    name = thread.name
    print(f"客户端：{client_info}接入，线程：{name}开始服务")

    while True:
        msg_bin = client.recv(1024)

        if not msg_bin:
            # 客户端发来None，表示断开了
            print(f"客户端：{client_info}主动断开")
            break

        msg = msg_bin.decode("utf-8")

        if msg == "exit":
            print(f"客户端：{client_info}已断开")
            break

        print(f"客户端：{client_info}发来：{msg}")

    print(f"线程客户端：{client_info}结束，线程退出")
    client.close()

if __name__ == '__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind(('127.0.0.1', 8080))

    server.listen()

    while True:
        client, client_info = server.accept()
        threading.Thread(target=client_thread, args=(client,client_info,)).start()
        