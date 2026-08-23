import threading
import socket
import random

def client_thread(thread_id):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect(('127.0.0.1', 8080))
        # 【修复】每个线程随机发送 1-10 条消息（原代码虽有随机数但被 input() 阻塞）
        num_messages = random.randint(1, 10)

        for j in range(num_messages):
            message = f"Thread-{thread_id}-Msg-{j+1}"
            client.send(message.encode())
            response = client.recv(1024).decode()
            print(f"[Thread-{thread_id}] Sent: {message}, Response: {response}")
    except Exception as e:
        # 【修复】原代码无异常处理，100 并发连接必然有部分失败（连接被拒、对端断开等），
        # 线程静默崩溃，控制台无输出，误以为是"只发了 1 条"，实际是线程已死
        print(f"[Thread-{thread_id}] 异常: {e}")
    finally:
        client.close()


if __name__ == '__main__':
    for i in range(100):
        threading.Thread(target=client_thread, args=(i,)).start()
