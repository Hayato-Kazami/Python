"""
案例：将 a.txt 内容拷贝到 b.txt

# 同时打开 源文件 和 目标文件
with open('./1.txt', 'r', encoding='utf-8') as src_f, \
        open('./2.txt', 'w', encoding='utf-8') as dest_f:
    # 循环分块读取
    while True:
        # 一次读取 8192 字节
        data = src_f.read(8192)

        # 读完退出循环
        if not data:
            break

        # 写入目标文件
        dest_f.write(data)
"""



# 采用上下文管理器
with open("./1.jpg","rb") as r_file , open("./2.jpg","wb") as w_file:
    # 考虑文件拷贝的通用性，我们一次性读取 1024B -> 1KB
    while True:
        print("循环读取")
        data = r_file.read(1024)
        # 读不到内容就结束
        if not data:
            break
        print(data)
        # 写入到 b.txt
        w_file.write(data)