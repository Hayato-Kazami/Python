class Scheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, coro):
        self.tasks.append(coro)

    def run(self):
        # 循环调度所有协程，直到全部执行完毕
        while self.tasks:
            temp = []
            for task in self.tasks:
                try:
                    # 执行协程，遇到yield暂停，交还调度器
                    next(task)
                    temp.append(task)
                except StopIteration:
                    # 协程执行完毕，丢弃
                    pass
            self.tasks = temp

# 计算任务，每循环一次主动yield交出CPU
def calc_task(name, count):
    n = 0
    while n < count:
        n += 1
        print(f"[{name}] 计算 n={n}")
        yield  # 主动移交CPU，切换其他任务

if __name__ == "__main__":
    sched = Scheduler()
    sched.add_task(calc_task("任务1", 3))
    sched.add_task(calc_task("任务2", 3))
    sched.run()