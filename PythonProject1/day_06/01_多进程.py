import time
import multiprocessing as mp


def aaa():
    for _ in range(10):
        print("我在唱歌")
        time.sleep(1)


def bbb():
    for _ in range(10):
        print("我在洗澡")
        time.sleep(2)


if __name__ == '__main__':
    # 如果想要在Python代码，启动其它进程，必须写在main中
    # 创建一个进程
    aaa_process = mp.Process(
        target=aaa,         # 被创建的进程的执行逻辑（函数名）
        name="aaa",         # 进程名字，一般可以不用设
        group=None,         # 固定写法，预留功能
    )

    bbb_process = mp.Process(
        target=bbb,  # 被创建的进程的执行逻辑（函数名）
    )

    aaa_process.start()
    bbb_process.start()