"""
尝试打开指定文件，捕获文件操作异常；
无异常时执行文件读取并输出内容，区分异常与正常业务逻辑。
"""
"""
尝试打开指定文件，捕获文件操作异常；
无异常时执行文件读取并输出内容，区分异常与正常业务逻辑。
"""


try:
    # 尝试读取一个文件
    file = open("./python.txt","r",encoding="utf-8")
    content = file.read();
except Exception as e:
    # 报错后执行
    print(f"异常信息：{e}")
else:
    # 没报错执行
    print(content)
    # 关闭文件
    file.close()