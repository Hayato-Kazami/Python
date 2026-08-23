import multiprocessing as mp
import time

def work1():
    for i in range(10):
        print(i)
        time.sleep(1)

def work2():
    for _ in range(10):
        print("ARE U OK ?")
        time.sleep(1)

if __name__ == '__main__':
    work1_process = mp.Process(target=work1)
    work2_process = mp.Process(target=work2)
    work1_process.start()
    work2_process.start()

    time.sleep(4)

    # work1_process.terminate()
    # work2_process.terminate()
    # work1_process.join()
    work2_process.join()
    print("主进程已结束")