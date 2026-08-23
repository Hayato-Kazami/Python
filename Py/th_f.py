import os
import threading
import time
import queue

def th1(queue, processed_files):
    while True:
        # 指定目录路径
        path = './Test'
        # 获取目录下的文件和文件夹迭代器
        print(f"定期检查文件夹：{path}")
        with os.scandir(path) as entries:
            for entry in entries:
                full_path = os.path.normpath(os.path.join(path, entry.name))
                if entry.is_file() and full_path not in processed_files:
                    print(f"发现新文件，即将处理：{full_path}")
                    queue.put(full_path)
                    processed_files.add(full_path)
                    
        time.sleep(1)  # 每秒刷新一次

def th2(queue):
    while True:
        # 从队列中获取文件名
        file_path = queue.get()
        try:
            # 用生成器读取并打印文件内容
            def read_lines():
                with open(file_path, 'r', encoding='utf-8') as fr:
                    for line in fr:
                        yield line.strip()
            for content in read_lines():
                print(content)
        except FileNotFoundError:
            print(f"文件 {file_path} 未找到。")
        except PermissionError:
            print(f"没有权限读取文件 {file_path}。")
        except Exception as e:
            print(f"打开文件 {file_path} 时发生错误: {e}")

if __name__ == '__main__':
    queue = queue.Queue()
    processed_files = {os.path.normpath('./Test/b.txt')}
    print(type(processed_files))
    t1 = threading.Thread(target=th1, args=(queue, processed_files))
    t2 = threading.Thread(target=th2, args=(queue,))
    t1.start()
    t2.start()
