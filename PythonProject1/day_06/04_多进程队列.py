
import multiprocessing as mp
import time
import random

# 进程，生产随机数字，放入队列
def producer(share_queue):
    # producer: 生产者，产生数据写入队列
    for _ in range(100):
        n = random.randint(1, 100)
        print(f"生产者：{n}")
        # 放入队列
        share_queue.put(n)
        time.sleep(1)

# 进程，取出数字，判断奇数还是偶数输出
def customer(share_queue):
    # customer:消费者，从队列取出数据（消费数据）
    while True:
        # get是阻塞，没有数据就卡住
        n = share_queue.get()
        print(f"消费者乘十后：{n * 10}")

if __name__ == '__main__':
    # mp.Queue(参数) 参数表示队列最大限制，不传参数表示无限制
    share_queue = mp.Queue()

    mp.Process(target=producer, args=(share_queue,)).start()
    mp.Process(target=customer, args=(share_queue,)).start()