"""
上下文管理器 对比演示
操作目录：day06
两个写法 操作 完全同一个文件：./test.txt
"""

# ============= 1. 普通写法（手动 open / close） =============
try:
    # 假设这里发生了异常
    print("尝试打开文件...")
    file = open("./python.txt", "r", encoding="utf-8")
    content = file.read()
    print(content)
finally:
    file.close()  # 如果 file 未定义，这里会引发 NameError

# ============= 2. 上下文管理器 with 写法（自动关闭） =============

with open("./python.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)