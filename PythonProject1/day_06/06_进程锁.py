import multiprocessing as mp


def w1(share_value, lock):

    for _ in range(40000):
        lock.acquire()      # 上锁
        share_value.value += 1
        lock.release()      # 释放锁


def w2(share_value, lock):
    for _ in range(40000):
        lock.acquire()
        share_value.value += 1
        lock.release()


if __name__ == '__main__':
    # 创建一个锁，给2个进程用
    lock = mp.Lock()

    share_value = mp.Value('i', 0)
    w1_process = mp.Process(target=w1, args=(share_value, lock))
    w2_process = mp.Process(target=w2, args=(share_value, lock))

    w1_process.start()
    w2_process.start()

    w1_process.join()
    w2_process.join()

    print("期望：80000")
    print(f"实际：{share_value.value}")