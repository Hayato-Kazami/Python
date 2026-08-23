import multiprocessing as mp
import time


def work(num):
    i = 1
    while i < num :
        print(i)
        i += 1
        time.sleep(1)


def sing(name, num):
    i = 0
    while i < num :
        print(f"{name}:,{i}")
        i +=1
        time.sleep(1)

if __name__ == '__main__':
    # work_process = mp.Process(
    #     target=work,
    #     args=(10, ),            # 将参数以解包元组的形式传入函数
    # )
    #
    # sing_process = mp.Process(
    #     target=sing,
    #     args=("夜曲", 20),        # 将参数以解包元组的形式传入函数
    # )
    work_process = mp.Process(
        target=work,
        kwargs={"num": 10}
    )

    sing_process = mp.Process(
        target=sing,
        kwargs={"name": "数字", "num": 20}
    )

    work_process.start()
    sing_process.start()