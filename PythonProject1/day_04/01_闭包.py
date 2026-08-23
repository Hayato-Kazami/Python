def outer():
    times = 0

    def inner(n):
        nonlocal times
        while times < n:
            times += 1
            print(times)
    return inner

count = outer()
count(10)