import threading
import time

def work1(num):
    for _ in range(num):
        print("Hello")
        time.sleep(1)

def work2(num,name):
    for _ in range(num):
        print(f"Hello, I am {name}")
        time.sleep(1)

if __name__ == "__main__":
    w1 = threading.Thread(target=work1,
                          kwargs={"num":10})

    w2 = threading.Thread(target=work2,
                          kwargs={"num":20,"name":"jack"})

    w1.start()
    w2.start()