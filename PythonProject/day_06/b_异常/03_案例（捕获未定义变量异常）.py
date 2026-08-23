"""
访问未定义变量触发异常，通过 Exception 捕获异常，并打印详细错误信息。
"""

try:
    print(name)
except Exception as e:
    print(e)
    # 将错误信息记录到日志中
    log_file = open("./2026-06-24_log.txt", "w", encoding="utf-8")
    log_file.write(f"程序报错了，记录日志：{e}")
    log_file.close()
