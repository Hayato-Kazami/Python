"""
线程无限循环，干活
主线程在5秒后停止子线程
"""

import threading
import time
import random
flag = True         # 全局变量，线程之间共享

def work():
    while flag:
        print("我爱工作，工作使我强大，成为超级牛马；")
        time.sleep(1)


if __name__ == '__main__':
    t1 = threading.Thread(target=work)
    t1.start()
    while True:
        num = random.randint(1,6)
        print(num)
        if num == 5:
            flag = False
            break
        time.sleep(1)