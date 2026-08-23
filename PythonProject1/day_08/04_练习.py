import re
def demo1():
    str1 = input("请输入手机号码：")
    p = r"(\d)\d{9}(\d)"
    res = re.sub(p, r"\1*********\2",str1)

    print(res)

demo1()