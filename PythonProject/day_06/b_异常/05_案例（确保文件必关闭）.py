try:
    num = int(input('请输入一个数: '))
    print(num)
except ValueError as ve:
    print(f"ValueError异常信息：{ve}")
except Exception as e:
    # 我是所有业务异常的掌门，其他人解决不了都交给我处理
    print(f"Exception异常信息：{e}")