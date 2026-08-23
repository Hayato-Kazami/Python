

import threading
import time

# 共享变量
num = 0
lock = threading.Lock()


def work1():
    global num
    for _ in range(10000):
        with lock:  # 获取锁
            num += 1


def work2():
    global num
    for _ in range(10000):
        with lock:  # 获取锁
            num += 1


if __name__ == '__main__':
    t1 = threading.Thread(target=work1)
    t2 = threading.Thread(target=work2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(num)
