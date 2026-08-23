from datetime import datetime

from tenacity import sleep


def show_time(fx):
    def inner():
        start = datetime.now()
        print(f"Now is {start}")
        fx()
        end = datetime.now()
        print(f"Now is {end}")
    return inner
@show_time
def fx():
    for i in range(100):
        print(i)


fx()
