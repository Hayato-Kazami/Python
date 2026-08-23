import time
import threading as th

def music():
    for i in range(3):
        print('听音乐...')
        
        current_thread = th.current_thread()
        print(current_thread)
        time.sleep(0.2)


def coding():
    for i in range(3):
        print('敲代码...')
        
        current_thread = th.current_thread()
        print(current_thread)
        time.sleep(0.2)



if __name__ == '__main__':
    # 创建线程
    t1 = th.Thread(target=music)
    t2 = th.Thread(target=coding)

    # 启动线程
    t1.start()
    t2.start()

