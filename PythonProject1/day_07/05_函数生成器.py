import random

def func():
    i = 0
    while i < 11:
        yield random.randint(1, 100)
        i += 1

gen = func()
for n in gen:
    print(n)
# import random
#
# def random_number_generator():
#     for _ in range(10):
#         yield random.randint(1, 100)
#
# # 使用生成器
# for number in random_number_generator():
#     print(number)
