import redis

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# 从左侧添加元素
r.lpush('tasks', 'task1', 'task2', 'task3')

# 从右侧添加元素
r.rpush('tasks', 'task4', 'task5')

# 获取列表长度
length = r.llen('tasks')
print(f"列表长度: {length}")

# 获取列表元素
all_tasks = r.lrange('tasks', 0, -1)
print("所有任务:", all_tasks)

# 获取指定范围的元素
first_three = r.lrange('tasks', 0, 2)
print("前三个任务:", first_three)

# 从左侧弹出元素
left_task = r.lpop('tasks')
print(f"左侧弹出: {left_task}")

# 从右侧弹出元素
right_task = r.rpop('tasks')
print(f"右侧弹出: {right_task}")

print("剩余任务:", r.lrange('tasks', 0, -1))