"""
通过单值共享变量，在多个进程之间共享数据；
"""

import multiprocessing as mp
import time

def work1(share_value):
    for _ in range(share_value.value):
        share_value.value -= 1
        print("work1:", share_value.value)
        time.sleep(1)

def work2(share_value):
    for _ in range(share_value.value):
        print("work2:", share_value.value)
        time.sleep(1)

if __name__ == '__main__':
    # 1. 创建单值共享变量
    share_value = mp.Value(
        'i',        # 单值共享变量支持的数据类型，  i int、f float、d double、b bool
        100       # 初始值
    )

    mp.Process(target=work1, args=(share_value,)).start()
    mp.Process(target=work2, args=(share_value,)).start()

    for _ in range(share_value.value):
        print("main:", share_value.value)
        time.sleep(1)